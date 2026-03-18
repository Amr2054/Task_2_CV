#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <vector>
#include <cmath>
#include <algorithm>

namespace py = pybind11;

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Helper function to simulate np.pad(mode='edge')
inline int clamp(int val, int min, int max) {
    if (val < min) return min;
    if (val > max) return max;
    return val;
}

// 1. Equivalent to your convolve2d
std::vector<float> convolve2d(const std::vector<float>& input, int h, int w, 
                              const std::vector<float>& kernel, int kh, int kw) {
    std::vector<float> output(h * w, 0.0f);
    int pad_y = kh / 2;
    int pad_x = kw / 2;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            float sum = 0.0f;
            for (int kr = 0; kr < kh; ++kr) {
                for (int kc = 0; kc < kw; ++kc) {
                    // Clamp to edges to simulate padding
                    int img_r = clamp(r + kr - pad_y, 0, h - 1);
                    int img_c = clamp(c + kc - pad_x, 0, w - 1);
                    sum += input[img_r * w + img_c] * kernel[kr * kw + kc];
                }
            }
            output[r * w + c] = sum;
        }
    }
    return output;
}

// Main processing function
py::array_t<uint8_t> apply_canny_cpp(py::array_t<uint8_t> input_image, int min_val, int max_val) {
    
    // Request buffer from Python NumPy array
    py::buffer_info buf_info = input_image.request();
    uint8_t* in_ptr = static_cast<uint8_t*>(buf_info.ptr);
    
    int height = buf_info.shape[0];
    int width = buf_info.shape[1];
    int total_pixels = height * width;

    // Convert uint8 input to float vector for math
    std::vector<float> gray_image(total_pixels);
    for (int i = 0; i < total_pixels; ++i) {
        gray_image[i] = static_cast<float>(in_ptr[i]);
    }

    // --- Kernels ---
    std::vector<float> gaussian_filter = {
        1.f/273.f,  4.f/273.f,  7.f/273.f,  4.f/273.f, 1.f/273.f,
        4.f/273.f, 16.f/273.f, 26.f/273.f, 16.f/273.f, 4.f/273.f,
        7.f/273.f, 26.f/273.f, 41.f/273.f, 26.f/273.f, 7.f/273.f,
        4.f/273.f, 16.f/273.f, 26.f/273.f, 16.f/273.f, 4.f/273.f,
        1.f/273.f,  4.f/273.f,  7.f/273.f,  4.f/273.f, 1.f/273.f
    };

    std::vector<float> sobelX = {
        -1.f, 0.f, 1.f,
        -2.f, 0.f, 2.f,
        -1.f, 0.f, 1.f
    };

    std::vector<float> sobelY = {
         1.f,  2.f,  1.f,
         0.f,  0.f,  0.f,
        -1.f, -2.f, -1.f
    };

    // 1. Gaussian Smoothing
    std::vector<float> gaussianData = convolve2d(gray_image, height, width, gaussian_filter, 5, 5);

    // 2. Gradients
    std::vector<float> Gx = convolve2d(gaussianData, height, width, sobelX, 3, 3);
    std::vector<float> Gy = convolve2d(gaussianData, height, width, sobelY, 3, 3);

    // 3. Magnitude and Angle
    std::vector<float> gradient(total_pixels, 0.0f);
    std::vector<float> gradientAngle(total_pixels, 0.0f);

    for (int i = 0; i < total_pixels; ++i) {
        // Magnitude
        gradient[i] = std::hypot(Gx[i], Gy[i]);
        
        // Angle in degrees
        float angle = std::atan2(Gy[i], Gx[i]) * 180.0f / M_PI;
        if (angle < 0) angle += 360.0f;
        gradientAngle[i] = angle;
    }

    // 4. Non-Maxima Suppression
    std::vector<float> suppressed(total_pixels, 0.0f);
    for (int r = 1; r < height - 1; ++r) {
        for (int c = 1; c < width - 1; ++c) {
            int idx = r * width + c;
            float theta = std::fmod(gradientAngle[idx], 180.0f);
            float val = gradient[idx];
            float v = 0.0f;

            if ((theta >= 0 && theta < 22.5f) || (theta >= 157.5f && theta < 180.0f)) {
                if (val > gradient[r * width + (c + 1)] && val > gradient[r * width + (c - 1)]) v = val;
            } else if (theta >= 22.5f && theta < 67.5f) {
                if (val > gradient[(r - 1) * width + (c + 1)] && val > gradient[(r + 1) * width + (c - 1)]) v = val;
            } else if (theta >= 67.5f && theta < 112.5f) {
                if (val > gradient[(r - 1) * width + c] && val > gradient[(r + 1) * width + c]) v = val;
            } else if (theta >= 112.5f && theta < 157.5f) {
                if (val > gradient[(r - 1) * width + (c - 1)] && val > gradient[(r + 1) * width + (c + 1)]) v = val;
            }
            suppressed[idx] = v;
        }
    }

    // 5. Double Thresholding
    if (min_val == 0) min_val = 1;
    uint8_t WEAK = 75;
    uint8_t STRONG = 255;
    
    // Allocate output array memory
    auto output_image = py::array_t<uint8_t>({height, width});
    py::buffer_info out_buf = output_image.request();
    uint8_t* out_ptr = static_cast<uint8_t*>(out_buf.ptr);

    for (int i = 0; i < total_pixels; ++i) {
        if (suppressed[i] >= max_val) {
            out_ptr[i] = STRONG;
        } else if (suppressed[i] >= min_val) {
            out_ptr[i] = WEAK;
        } else {
            out_ptr[i] = 0;
        }
    }

    // 6. Hysteresis
    for (int r = 1; r < height - 1; ++r) {
        for (int c = 1; c < width - 1; ++c) {
            int idx = r * width + c;
            if (out_ptr[idx] == WEAK) {
                if (out_ptr[(r + 1) * width + (c - 1)] == STRONG || 
                    out_ptr[(r + 1) * width + c] == STRONG || 
                    out_ptr[(r + 1) * width + (c + 1)] == STRONG ||
                    out_ptr[r * width + (c - 1)] == STRONG || 
                    out_ptr[r * width + (c + 1)] == STRONG ||
                    out_ptr[(r - 1) * width + (c - 1)] == STRONG || 
                    out_ptr[(r - 1) * width + c] == STRONG || 
                    out_ptr[(r - 1) * width + (c + 1)] == STRONG) {
                    
                    out_ptr[idx] = STRONG;
                } else {
                    out_ptr[idx] = 0;
                }
            }
        }
    }

    return output_image;
}

