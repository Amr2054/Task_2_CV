import cv2
import numpy as np
from core.hough_circle_transform import hough_circle_transform
from core import CppModule
from utils.hough_drawing import draw_hough_lines, draw_hough_circles, draw_hough_ellipses


class HoughController:
    def __init__(self, ui, model, display_callback):
        self.ui = ui
        self.model = model
        self.display_callback = display_callback

    def run_hough(self, edges):
        result_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        any_checked = (self.ui.checkLines.isChecked() or
                       self.ui.checkCircles.isChecked() or
                       self.ui.checkEllipses.isChecked())

        if not any_checked:
            self.model.processed_image = edges
            self.display_callback(edges)
            self.ui.statusbar.showMessage("Canny Edge Detection applied.", 3000)
            return

        gray = cv2.cvtColor(self.model.original_image, cv2.COLOR_BGR2GRAY)
        Gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        Gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        edge_direction = np.degrees(np.arctan2(Gy, Gx)) % 360

        if self.ui.checkLines.isChecked():
            lines = CppModule.hough_line_transform(edges)
            print(f"Found {len(lines)} Lines")
            result_image = draw_hough_lines(result_image, lines)

        if self.ui.checkCircles.isChecked():
            best_a, best_b, best_r = hough_circle_transform(edges, edge_direction, min_dist=20, min_r=2, max_r=205,voting_threshold=30)
            print(f"Found {len(best_a)} Circles")
            result_image = draw_hough_circles(result_image, best_a, best_b, best_r)

        if self.ui.checkEllipses.isChecked():
            ellipses = CppModule.hough_ellipse_transform(edges,voting_threshold = 100)
            print(f"Found {len(ellipses)} Ellipses")
            result_image = draw_hough_ellipses(result_image, ellipses)

        self.model.processed_image = result_image
        self.display_callback(result_image)
        self.ui.statusbar.showMessage("Hough Transformation applied.", 3000)