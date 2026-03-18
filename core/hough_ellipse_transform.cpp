#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <opencv2/opencv.hpp>
#include "../utils/hough_utils.hpp"

using namespace std;

pybind11::array_t<double> hough_ellipse_transform(pybind11::array_t<uint8_t> data, int voting_threshold = 250, double min_dist = 2.0) {
    
    cv::Mat edges = numpy_to_cvmat(data);
    
    vector<cv::Point2d> pts;
    for (int r = 0; r < edges.rows; ++r) {
        const uchar* row_ptr = edges.ptr<uchar>(r);
        for (int c = 0; c < edges.cols; ++c) {
            if (row_ptr[c] != 0) {
                // Store as double precision directly (x = col, y = row)
                pts.push_back(cv::Point2d(static_cast<double>(c), static_cast<double>(r)));
            }
        }
    }

    vector<EllipseData> ellipses;
    size_t i = 0;
    
    while (i < pts.size()) {
        double x1 = pts[i].x;
        double y1 = pts[i].y;
        bool ellipse_detected = false;
        size_t j = i + 1;
        
        while (j < pts.size()) {
            double x2 = pts[j].x;
            double y2 = pts[j].y;
            
            double dx = x1 - x2;
            double dy = y1 - y2;
            double major_axis = sqrt(dx*dx + dy*dy);
            
            if (major_axis < min_dist) {
                j++;
                continue;
            }
            
            double xo = (x1 + x2) / 2.0;
            double yo = (y1 + y2) / 2.0;
            double a = major_axis / 2.0;
            
            double orientation_rad = atan2(y2 - y1, x2 - x1);
            double orientation_deg = orientation_rad * 180.0 / CV_PI; 
            
            int max_b_size = static_cast<int>(ceil(a)) + 2;
            vector<int> accumulator(max_b_size, 0);
            
            for (const auto& p : pts) {
                double dx_c = p.x - xo;
                double dy_c = p.y - yo;
                double d = sqrt(dx_c*dx_c + dy_c*dy_c);
                
                if (d > min_dist && d < a) {
                    double dx_f = p.x - x2;
                    double dy_f = p.y - y2;
                    double f = sqrt(dx_f*dx_f + dy_f*dy_f);
                    double val = (a*a + d*d - f*f) / (2.0 * a * d);
                    
                    if (val >= -1.0 && val <= 1.0) {
                        double Taw = acos(val);
                        double cosineTaw = cos(Taw);
                        double sineTaw = sin(Taw);
                        
                        double denominator = (a*a - d*d * cosineTaw * cosineTaw);
                        
                        if (denominator > 0.0) {
                            double b_val = sqrt((a*a * d*d * sineTaw * sineTaw) / denominator);
                            int b_idx = static_cast<int>(round(b_val));
                            
                            if (b_idx >= 0 && b_idx < accumulator.size()) {
                                accumulator[b_idx]++;
                            }
                        }
                    }
                }
            }
            
            int best_b = 0;
            int max_votes = -1;
            for (size_t b_idx = 0; b_idx < accumulator.size(); ++b_idx) {
                if (accumulator[b_idx] > max_votes) {
                    max_votes = accumulator[b_idx];
                    best_b = static_cast<int>(b_idx);
                }
            }
            
            if (max_votes > voting_threshold) {
                ellipses.push_back({yo, xo, a, static_cast<double>(best_b), orientation_deg});
                
                // --- PIXEL REMOVAL LOGIC ---
                double c = sqrt(abs(a*a - best_b*best_b)); 
                double f1_x = xo + c * cos(orientation_rad);
                double f1_y = yo + c * sin(orientation_rad);
                double f2_x = xo - c * cos(orientation_rad);
                double f2_y = yo - c * sin(orientation_rad);
                
                double tolerance = 2.0;
                
                pts.erase(remove_if(pts.begin(), pts.end(), [&](const cv::Point2d& p) {
                    double dist_to_f1 = sqrt((p.x - f1_x)*(p.x - f1_x) + (p.y - f1_y)*(p.y - f1_y));
                    double dist_to_f2 = sqrt((p.x - f2_x)*(p.x - f2_x) + (p.y - f2_y)*(p.y - f2_y));
                    double sum_of_distances = dist_to_f1 + dist_to_f2;
                    
                    return abs(sum_of_distances - (2.0 * a)) <= tolerance; 
                }), pts.end());
                
                ellipse_detected = true;
                break; 
            }
            // if no ellipse was found for this pair
            j++;
        }
        //Don't need to update i because i will refer to new point when shrink points after detecting ellipse
        if (!ellipse_detected) {
            i++;
        }
    }
    
    return convert_ellipses_to_numpy(ellipses);
}