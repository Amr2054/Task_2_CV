import math
import sys
import numpy as np
import cv2


# def apply_canny(image, min_val, max_val):
#     """Applies Canny edge detection to an image."""
#     if image is None:
#         return None
#
#     # Canny requires a grayscale image
#     if len(image.shape) == 3:
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     else:
#         gray = image
#
#     edges = cv2.Canny(gray, min_val, max_val)
#     return edges
#
#
# import math
# import numpy as np
# import cv2

gaussian_filter = (1.0 / 140.0) * np.array([
    [1, 1, 2, 2, 2, 1, 1],
    [1, 2, 2, 4, 2, 2, 1],
    [2, 2, 4, 8, 4, 2, 2],
    [2, 4, 8, 16, 8, 4, 2],
    [2, 2, 4, 8, 4, 2, 2],
    [1, 2, 2, 4, 2, 2, 1],
    [1, 1, 2, 2, 2, 1, 1]
])

sobelX = np.array([
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1]
])

sobelY = np.array([
    [ 1,  2,  1],
    [ 0,  0,  0],
    [-1, -2, -1]
])

def apply_canny(image, min_val, max_val):
    """
    Executing the full Canny edge detection pipeline from scratch.
    """
    if image is None:
        return None

    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    height, width = gray_image.shape

    # 1. Gaussian Smoothing
    gaussianData = gaussianSmoothing(gray_image)

    # 2. Gradients
    Gx = getGradientX(gaussianData, height, width)
    Gy = getGradientY(gaussianData, height, width)

    # 3. Magnitude and Angle
    gradient = getMagnitude(Gx, Gy, height, width)
    gradientAngle = getAngle(Gx, Gy, height, width)

    # 4. Non-Maxima Suppression
    localMaxSuppressed = localMaximization(gradient, gradientAngle, height, width)
    suppressedImage = localMaxSuppressed[0]

    # Normalize the suppressed image to 0-255
    if suppressedImage.max() > 0:
        suppressedImage = (suppressedImage / suppressedImage.max()) * 255.0

    # 5. Double Thresholding
    thresholded, weak, strong = double_thresholding(suppressedImage, min_val, max_val)

    # 6. Edge Tracking by Hysteresis
    final_edges = hysteresis(thresholded, weak, strong)

    return np.uint8(final_edges)

def gaussianSmoothing(image):
    imageArray = np.array(image)
    gaussianArr = np.copy(imageArray)  # Better practice to copy

    for i in range(3, image.shape[0] - 3):
        for j in range(3, image.shape[1] - 3):
            sum_val = applyGaussianFilterAtPoint(imageArray, i, j)
            gaussianArr[i][j] = sum_val
    return gaussianArr


def applyGaussianFilterAtPoint(imageData, row, column):
    sum_val = 0
    for i in range(row - 3, row + 4):
        for j in range(column - 3, column + 4):
            sum_val += gaussian_filter[i - row + 3][j - column + 3] * imageData[i][j]
    return sum_val


def getGradientX(imgArr, height, width):
    imageData = np.zeros(shape=(height, width))
    for i in range(3, height - 5):
        for j in range(3, width - 5):  # Fixed: size -> width
            imageData[i + 1][j + 1] = sobelAtX(imgArr, i, j)
    return abs(imageData)


def getGradientY(imgArr, height, width):
    imageData = np.zeros(shape=(height, width))
    for i in range(3, height - 5):
        for j in range(3, width - 5):  # Fixed: size -> width
            imageData[i + 1][j + 1] = sobelAtY(imgArr, i, j)
    return abs(imageData)


def getMagnitude(Gx, Gy, height, width):
    gradientData = np.empty(shape=(height, width))
    for row in range(height):
        for column in range(width):
            gradientData[row][column] = ((Gx[row][column] ** 2 + Gy[row][column] ** 2) ** 0.5) / 1.4142
    return gradientData


def getAngle(Gx, Gy, height, width):
    gradientData = np.empty(shape=(height, width))
    for i in range(height):
        for j in range(width):
            if Gx[i][j] == 0:
                angle = 90 if Gy[i][j] > 0 else -90
            else:
                angle = math.degrees(math.atan(Gy[i][j] / Gx[i][j]))
            if angle < 0:
                angle += 360
            gradientData[i][j] = angle
    return gradientData


def localMaximization(gradientData, gradientAngle, height, width):
    gradient = np.zeros(shape=(height, width))
    numberOfPixels = np.zeros(shape=(256))
    edgePixels = 0

    for row in range(5, height - 5):
        for col in range(5, width - 5):  # Fixed global 'image' reference
            theta = gradientAngle[row, col]
            gradientAtPixel = gradientData[row, col]
            value = 0

            if (0 <= theta <= 22.5 or 157.5 < theta <= 202.5 or 337.5 < theta <= 360):
                if gradientAtPixel > gradientData[row, col + 1] and gradientAtPixel > gradientData[row, col - 1]:
                    value = gradientAtPixel
            elif (22.5 < theta <= 67.5 or 202.5 < theta <= 247.5):
                if gradientAtPixel > gradientData[row + 1, col - 1] and gradientAtPixel > gradientData[
                    row - 1, col + 1]:
                    value = gradientAtPixel
            elif (67.5 < theta <= 112.5 or 247.5 < theta <= 292.5):
                if gradientAtPixel > gradientData[row + 1, col] and gradientAtPixel > gradientData[row - 1, col]:
                    value = gradientAtPixel
            elif 112.5 < theta <= 157.5 or 292.5 < theta <= 337.5:
                if gradientAtPixel > gradientData[row + 1, col + 1] and gradientAtPixel > gradientData[
                    row - 1, col - 1]:
                    value = gradientAtPixel

            gradient[row, col] = value
            if value > 0:
                edgePixels += 1
                try:
                    numberOfPixels[int(value)] += 1
                except IndexError:
                    pass

    return [gradient, numberOfPixels, edgePixels]


def sobelAtX(imageData, row, column):
    horizontal = 0
    for i in range(0, 3):
        for j in range(0, 3):
            horizontal += imageData[row + i, column + j] * sobelX[i, j]
    return horizontal

def sobelAtY(imageData, row, column):
    vertical = 0
    for i in range(0, 3):
        for j in range(0, 3):
            vertical += imageData[row + i, column + j] * sobelY[i, j]
    return vertical


def double_thresholding(img, lowThreshold, highThreshold):
    """Applies double thresholding using absolute 0-255 integer values."""
    res = np.zeros_like(img)
    weak = np.int32(75)
    strong = np.int32(255)

    # Find pixels that meet the threshold criteria
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

    # Assign values
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak

    return (res, weak, strong)

def hysteresis(img, weak, strong=255):
    M, N = img.shape
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if (img[i, j] == weak):
                if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
                        or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
                        or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (img[i - 1, j + 1] == strong)):
                    img[i, j] = strong
                else:
                    img[i, j] = 0
    return img