import numpy as np
import cv2 as cv
sobelX = np.array([
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1]
])

sobelY = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])


def convolve2d(img, kernel):
    kH, kW = kernel.shape
    padH, padW = kH // 2, kW // 2

    img = img.astype(np.float32)

    padded = np.pad(
        img,
        ((padH, padH), (padW, padW)),
        mode='edge'
    )
    shape = (img.shape[0], img.shape[1], kH, kW)
    strides = (
        padded.strides[0],
        padded.strides[1],
        padded.strides[0],
        padded.strides[1]
    )

    windows = np.lib.stride_tricks.as_strided(
        padded,
        shape=shape,
        strides=strides
    )

    return np.einsum('ijkl,kl->ij', windows, kernel)


def getAngle(gray):
    """Vectorized calculation of gradient angle (0 to 360 degrees)."""
    # np.arctan2 takes (y, x) and handles division by zero automatically

    Gx = convolve2d(gray, sobelX)
    Gy = convolve2d(gray, sobelY)
    angle = np.degrees(np.arctan2(Gy, Gx)) % 360

    return angle