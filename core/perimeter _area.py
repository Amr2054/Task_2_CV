import cv2
import numpy as np

def compute_perimeter_area(points):
    # OpenCV expects contour shape (N,1,2)
    contour = points.astype(np.int32).reshape((-1, 1, 2))

    perimeter = cv2.arcLength(contour, True)   
    area = cv2.contourArea(contour)

    return perimeter, area
