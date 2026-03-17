
import cv2
import numpy as np

class PerimeterAreaController:
    def __init__(self, main_window, window):
        self.main_window = main_window
        self.window = window
        self.final_points = None

        self.main_window.btnCalcPerimeter.setEnabled(False)
        self.main_window.btnCalcArea.setEnabled(False)

        self.main_window.btnCalcPerimeter.clicked.connect(self.calculate_perimeter)
        self.main_window.btnCalcArea.clicked.connect(self.calculate_area)

    def set_final_points(self, final_points):
        self.final_points = final_points
        self.main_window.btnCalcPerimeter.setEnabled(True)
        self.main_window.btnCalcArea.setEnabled(True)

    def reset(self):
        self.final_points = None
        self.main_window.btnCalcPerimeter.setEnabled(False)
        self.main_window.btnCalcArea.setEnabled(False)
        self.main_window.lblResult.setText(u"")

    def calculate_perimeter(self):
        if self.final_points is None:
            return
        contour = self.final_points.astype(np.int32).reshape((-1, 1, 2))
        perimeter = cv2.arcLength(contour, True)
        self.main_window.lblResult.setText(f"Perimeter: {perimeter:.2f} px")

    def calculate_area(self):
        if self.final_points is None:
            return
        contour = self.final_points.astype(np.int32).reshape((-1, 1, 2))
        area = cv2.contourArea(contour)
        self.main_window.lblResult.setText(f"Area: {area:.2f} px²")





