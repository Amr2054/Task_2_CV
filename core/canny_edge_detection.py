# import numpy as np
# import cv2
#
#
# # def apply_canny(image, min_val, max_val):
# #     """Applies Canny edge detection to an image."""
# #     if image is None:
# #         return None
# #
# #     # Canny requires a grayscale image
# #     if len(image.shape) == 3:
# #         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #     else:
# #         gray = image
# #
# #     edges = cv2.Canny(gray, min_val, max_val)
# #     return edges
#
#
#
# gaussian_filter = (1.0 / 273.0) * np.array([
#     [1,  4,  7,  4, 1],
#     [4, 16, 26, 16, 4],
#     [7, 26, 41, 26, 7],
#     [4, 16, 26, 16, 4],
#     [1,  4,  7,  4, 1]
# ], dtype=np.float32)
#
# sobelX = np.array([
#     [-1,  0,  1],
#     [-2,  0,  2],
#     [-1,  0,  1]
# ])
#
# sobelY = np.array([
#     [ 1,  2,  1],
#     [ 0,  0,  0],
#     [-1, -2, -1]
# ])
#
# def apply_canny(image, min_val, max_val):
#
#     if image is None:
#         return None
#
#     if len(image.shape) == 3:
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     else:
#         gray_image = image
#
#
#     # 1. Gaussian Smoothing (Vectorized)
#     gaussianData = convolve2d(gray_image, gaussian_filter)
#
#     # 2. Gradients (Vectorized)
#     Gx = convolve2d(gaussianData, sobelX)
#     Gy = convolve2d(gaussianData, sobelY)
#
#     # 3. Magnitude and Angle (Vectorized)
#     gradient = getMagnitude(Gx, Gy)
#     gradientAngle = getAngle(Gx, Gy)
#
#     # 4. Non-Maxima Suppression
#     suppressedImage = localMaximization(gradient, gradientAngle)
#
#     # # Normalize the suppressed image to 0-255
#     # if suppressedImage.max() > 0:
#     #     suppressedImage = (suppressedImage / suppressedImage.max()) * 255.0
#
#     # 5. Double Thresholding
#     thresholded, weak, strong = double_thresholding(suppressedImage, min_val, max_val)
#
#     # 6. Edge Tracking by Hysteresis
#     final_edges = hysteresis(thresholded, weak, strong)
#
#     return np.uint8(final_edges)
#
#
# def convolve2d(img, kernel):
#     kH, kW = kernel.shape
#     padH, padW = kH // 2, kW // 2
#
#     img = img.astype(np.float32)
#
#     padded = np.pad(
#         img,
#         ((padH, padH), (padW, padW)),
#         mode='edge'
#     )
#
#     shape = (img.shape[0], img.shape[1], kH, kW)
#     strides = (
#         padded.strides[0],
#         padded.strides[1],
#         padded.strides[0],
#         padded.strides[1]
#     )
#
#     windows = np.lib.stride_tricks.as_strided(
#         padded,
#         shape=shape,
#         strides=strides
#     )
#
#     return np.einsum('ijkl,kl->ij', windows, kernel)
#
#
# def getMagnitude(Gx, Gy):
#     """Vectorized calculation of gradient magnitude."""
#     return np.sqrt(Gx ** 2 + Gy ** 2)
#
#
# def getAngle(Gx, Gy):
#     """Vectorized calculation of gradient angle (0 to 360 degrees)."""
#     # np.arctan2 takes (y, x) and handles division by zero automatically
#     angle = np.degrees(np.arctan2(Gy, Gx))
#
#     # Convert negative angles to 0-360 range to match NMS logic
#     angle[angle < 0] += 360
#     return angle
#
#
# def localMaximization(gradientData, gradientAngle):
#
#     height, width = gradientData.shape
#     gradient = np.zeros(shape=(height, width), dtype=np.float32)
#
#     for row in range(1, height - 1):
#         for col in range(1, width - 1):
#
#             # FOLD THE ANGLE TO 0-180 DEGREES
#             theta = gradientAngle[row, col] % 180
#             gradientAtPixel = gradientData[row, col]
#             value = 0
#
#             # Sector 1: Horizontal Edge (0 degrees)
#             # We check the Left and Right neighbors
#             if (0 <= theta < 22.5) or (157.5 <= theta < 180):
#                 if gradientAtPixel > gradientData[row, col + 1] and gradientAtPixel > gradientData[row, col - 1]:
#                     value = gradientAtPixel
#
#             # Sector 2: Diagonal / (45 degrees)
#             # We check the Top-Right and Bottom-Left neighbors
#             elif (22.5 <= theta < 67.5):
#                 if gradientAtPixel > gradientData[row - 1, col + 1] and gradientAtPixel > gradientData[
#                     row + 1, col - 1]:
#                     value = gradientAtPixel
#
#             # Sector 3: Vertical Edge (90 degrees)
#             # We check the Top and Bottom neighbors
#             elif (67.5 <= theta < 112.5):
#                 if gradientAtPixel > gradientData[row - 1, col] and gradientAtPixel > gradientData[row + 1, col]:
#                     value = gradientAtPixel
#
#             # Sector 4: Diagonal \ (135 degrees)
#             # We check the Top-Left and Bottom-Right neighbors
#             elif (112.5 <= theta < 157.5):
#                 if gradientAtPixel > gradientData[row - 1, col - 1] and gradientAtPixel > gradientData[
#                     row + 1, col + 1]:
#                     value = gradientAtPixel
#
#             gradient[row, col] = value
#
#     return gradient
#
#
# def double_thresholding(img, lowThreshold, highThreshold):
#
#     if lowThreshold ==0:
#         lowThreshold = 1
#
#     res = np.zeros_like(img)
#     weak = np.int32(75)
#     strong = np.int32(255)
#
#     strong_i, strong_j = np.where(img >= highThreshold)
#     # zeros_i, zeros_j = np.where(img < lowThreshold)
#     weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
#
#     res[strong_i, strong_j] = strong
#     res[weak_i, weak_j] = weak
#
#     return (res, weak, strong)
#
# def hysteresis(img, weak, strong=255):
#     M, N = img.shape
#     for i in range(1, M - 1):
#         for j in range(1, N - 1):
#             if (img[i, j] == weak):
#                 if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
#                         or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
#                         or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (img[i - 1, j + 1] == strong)):
#                     img[i, j] = strong
#                 else:
#                     img[i, j] = 0
#     return img

import cv2
import numpy as np

# Import your newly compiled C++ module!
from core import CppModule

def apply_canny(image, min_val, max_val):
    """
    Wrapper function that prepares the image and sends it to C++.
    """
    if image is None:
        return None


    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image


    contiguous_gray = np.ascontiguousarray(gray_image, dtype=np.uint8)


    edges = CppModule.apply_canny(contiguous_gray, min_val, max_val)

    return edges