#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

py::array_t<int> hough_line_transform(py::array_t<uint8_t> data, int voting_threshold);
py::array_t<double> hough_ellipse_transform(pybind11::array_t<uint8_t> data, int voting_threshold = 60, double min_dist = 4.0);
py::array_t<uint8_t> apply_canny_cpp(py::array_t<uint8_t> input_image, int min_val, int max_val);

PYBIND11_MODULE(CppModule, m) {
    m.doc() = "My custom computer vision Python module";

    // Hough Line Transform binding
    m.def("hough_line_transform", &hough_line_transform, 
          "Perform Hough Line Transform. Returns a 2D Nx2 numpy array of [r, theta].",
          py::arg("data"), 
          py::arg("voting_threshold") = 70);

    // Hough Ellipse Transform binding
    m.def("hough_ellipse_transform", &hough_ellipse_transform, 
          "Perform Hough Ellipse Transform. Returns a 2D Nx5 numpy array of [k, h, a, b, alpha].",
          py::arg("data"), 
          py::arg("voting_threshold") = 60,
          py::arg("min_dist") = 4.0);

    m.def("apply_canny", &apply_canny_cpp, "Run Canny Edge Detection natively",
          py::arg("input_image"), py::arg("min_val"), py::arg("max_val"));

}

