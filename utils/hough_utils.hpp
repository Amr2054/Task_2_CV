#pragma once

#include <pybind11/pybind11.h>
#include <opencv2/opencv.hpp>
#include <vector>
#include <cmath>
#include <algorithm>
#include <pybind11/numpy.h>

inline cv::Mat numpy_to_cvmat(pybind11::array_t<uint8_t> input_array) {
    pybind11::buffer_info buf = input_array.request();
    if (buf.ndim != 2) {
        throw std::runtime_error("Error: Expected a 2D NumPy array.");
    }
    int rows = buf.shape[0];
    int cols = buf.shape[1];
    return cv::Mat(rows, cols, CV_8UC1, (uint8_t*)buf.ptr);
}

struct houghlines {
    std::vector<int> r;
    std::vector<int> theta;
};
inline pybind11::array_t<int> houghlines_to_2d_numpy(const houghlines& lines) {
    size_t num_lines = lines.r.size();

    pybind11::array_t<int> result({num_lines, (size_t)2});

    auto buffer = result.mutable_unchecked<2>();

    for (size_t i = 0; i < num_lines; ++i) {
        buffer(i, 0) = lines.r[i];
        buffer(i, 1) = lines.theta[i];
    }
    return result;
}


struct EllipseData {
    double yo, xo, a, b, orientation;
};
inline pybind11::array_t<double> convert_ellipses_to_numpy(const std::vector<EllipseData>& ellipses) {
    size_t num_ellipses = ellipses.size();
    pybind11::array_t<double> result({num_ellipses, (size_t)5});
    auto r = result.mutable_unchecked<2>();
    for (size_t i = 0; i < num_ellipses; ++i) {
        r(i, 0) = ellipses[i].yo;          // k (y-center)
        r(i, 1) = ellipses[i].xo;          // h (x-center)
        r(i, 2) = ellipses[i].a;           // a (major axis / 2)
        r(i, 3) = ellipses[i].b;           // b (minor axis / 2)
        r(i, 4) = ellipses[i].orientation; // alpha (angle in degrees)
    }
    
    return result;
}