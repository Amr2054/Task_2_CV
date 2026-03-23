import cv2
import numpy as np


def draw_hough_lines(image, lines):
    """
    Draw lines on image from hough_line_transform result.
    :param image: BGR numpy array (H x W x 3)
    :param lines: Nx2 numpy array of [r, theta] from CppModule.hough_line_transform
    :return: image with lines drawn
    """
    output = image.copy()

    if lines is None or len(lines) == 0:
        return output

    h, w = output.shape[:2]
    # Calculate the image diagonal to ensure the drawn lines cover the whole image
    diag_len = int(np.hypot(h, w)) 

    for i in range(len(lines)):
        r = lines[i, 0]
        theta_deg = lines[i, 1]
        theta_rad = np.radians(theta_deg)

        cos_t = np.cos(theta_rad)
        sin_t = np.sin(theta_rad)

        # 1. Find the base point (x0, y0) on the line closest to the origin
        x0 = r * cos_t
        y0 = r * sin_t

        # 2. Extend the line outward from the base point.
        # The direction vector of the line is (-sin_t, cos_t)
        pt1_x = int(x0 + diag_len * (-sin_t))
        pt1_y = int(y0 + diag_len * (cos_t))
        
        pt2_x = int(x0 - diag_len * (-sin_t))
        pt2_y = int(y0 - diag_len * (cos_t))

        cv2.line(output, (pt1_x, pt1_y), (pt2_x, pt2_y), (0, 255, 0), 1)

    return output


def draw_hough_circles(image, best_a, best_b, best_r):
    """
    Draw circles on image from hough_circle_transform result.
    :param image: BGR numpy array (H x W x 3)
    :param best_a: array of circle center x-coordinates
    :param best_b: array of circle center y-coordinates
    :param best_r: array of circle radii
    :return: image with circles drawn
    """
    output = image.copy()

    if best_a is None or len(best_a) == 0:
        return output

    for a, b, r in zip(best_a, best_b, best_r):
        cv2.circle(output, (int(a), int(b)), int(r), (0, 0, 255), 2)
        cv2.circle(output, (int(a), int(b)), 2, (0, 255, 255), -1)  # center dot

    return output


def draw_hough_ellipses(image, ellipses):
    """
    Draw ellipses on image from hough_ellipse_transform result.
    :param image: BGR numpy array (H x W x 3)
    :param ellipses: Nx5 numpy array of [k, h, a, b, alpha] from CppModule.hough_ellipse_transform
                     k = y-center, h = x-center, a = semi-major, b = semi-minor, alpha = angle in degrees
    :return: image with ellipses drawn
    """
    output = image.copy()

    if ellipses is None or len(ellipses) == 0:
        return output

    for i in range(len(ellipses)):
        k     = ellipses[i, 0]  # y-center
        h     = ellipses[i, 1]  # x-center
        a     = ellipses[i, 2]  # semi-major axis
        b     = ellipses[i, 3]  # semi-minor axis
        alpha = ellipses[i, 4]  # rotation angle in degrees

        center = (int(round(h)), int(round(k)))
        axes   = (int(round(a)), int(round(b)))

        if axes[0] > 0 and axes[1] > 0:
            cv2.ellipse(output, center, axes, alpha, 0, 360, (255, 0, 0), 2)

    return output