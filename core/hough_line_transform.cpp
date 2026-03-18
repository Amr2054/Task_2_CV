#include <iostream>
#include <vector>
#include <cmath>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <opencv2/opencv.hpp>
#include "../utils/hough_utils.hpp"

using namespace std;
using namespace cv;

pybind11::array_t<int> hough_line_transform(pybind11::array_t<uint8_t> data, int voting_threshold = 70) {
    
    Mat edges = numpy_to_cvmat(data);

    int rows = edges.rows;
    int cols = edges.cols;

    // Find the edges coord
    vector<Point> edge_points;
    for (int y = 0; y < rows; ++y) {
        // Using ptr for fast row access in OpenCV
        const uint8_t* row_ptr = edges.ptr<uint8_t>(y);
        for (int x = 0; x < cols; ++x) {
            if (row_ptr[x] != 0) {
                edge_points.push_back(Point(x, y));
            }
        }
    }

    int diagonal = round(sqrt(rows * rows + cols * cols));
    int num_rho = 2 * diagonal + 1;
    int num_theta = 181;

    vector<double> cosines(num_theta);
    vector<double> sines(num_theta);
    for (int t = 0; t < num_theta; ++t) {
        double radians = t * CV_PI / 180.0;
        cosines[t] = cos(radians);
        sines[t] = sin(radians);
    }

    vector<int> accumulator(num_rho * num_theta, 0);

    // Cast votes
    for (const auto& pt : edge_points) {
        for (int t = 0; t < num_theta; ++t) {
            int r = round(pt.x * cosines[t] + pt.y * sines[t]);
            r += diagonal;
            accumulator[r * num_theta + t]++;
        }
    }

    // Extract lines above threshold
    houghlines best_lines;
    for (int r_idx = 0; r_idx < num_rho; ++r_idx) {
        for (int t = 0; t < num_theta; ++t) {
            if (accumulator[r_idx * num_theta + t] > voting_threshold) {
                best_lines.r.push_back(r_idx - diagonal);
                best_lines.theta.push_back(t);
            }
        }
    }

    return houghlines_to_2d_numpy(best_lines);
}
