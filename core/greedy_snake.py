# =============================
# Image energy with Gaussian Pyramid
# =============================
import cv2
import numpy as np


def ImgEnrgPyramid(img, levels=3, sigma=1):
    pyr = [img.astype(np.float32)]
    for i in range(1, levels):
        pyr.append(cv2.pyrDown(pyr[i - 1]))

    energy = np.zeros_like(img, dtype=np.float32)
    for level_img in pyr[::-1]:
        blur = cv2.GaussianBlur(level_img, (5, 5), sigma)
        sobelx = cv2.Sobel(blur, cv2.CV_32F, 1, 0, ksize=5)
        sobely = cv2.Sobel(blur, cv2.CV_32F, 0, 1, ksize=5)
        e = np.sqrt(sobelx ** 2 + sobely ** 2)
        e_resized = cv2.resize(e, (img.shape[1], img.shape[0]))
        energy += e_resized
    return energy / levels


# =============================
# Average distance
# =============================
def getAvgDist(points):
    n = len(points)
    tot = np.sum([np.linalg.norm(points[i] - points[j])
                  for i in range(n - 1) for j in range(i + 1, n)])
    return tot / ((n * (n - 1)) / 2)


# =============================
# Greedy Snake with automatic convergence
# =============================
def GreedyAlgorithmAuto(points, img, alpha, beta, gamma, step=1, movement_thresh=0.5, max_iter=5000):
    points = points.astype(np.float32)
    n = len(points)

    energy_img = ImgEnrgPyramid(img, levels=3)
    avgDist = getAvgDist(points)

    iteration = 0
    while True:
        old_points = points.copy()
        moves = np.array([[dx, dy] for dx in [-step, 0, step] for dy in [-step, 0, step]])

        for i in range(n):
            prev = points[(i - 1) % n]
            nextp = points[(i + 1) % n]
            candidates = points[i] + moves
            candidates[:, 0] = np.clip(candidates[:, 0], 0, img.shape[1] - 1)
            candidates[:, 1] = np.clip(candidates[:, 1], 0, img.shape[0] - 1)

            Econt = np.abs(np.linalg.norm(candidates - prev, axis=1) - avgDist)
            Ecurv = np.linalg.norm(prev - 2 * candidates + nextp, axis=1) ** 2
            Eimg = -energy_img[candidates[:, 1].astype(int), candidates[:, 0].astype(int)]
            E = alpha * Econt + beta * Ecurv + gamma * Eimg

            best_idx = np.argmin(E)
            points[i] = candidates[best_idx]

        # Convergence based on max movement
        max_movement = np.max(np.linalg.norm(points - old_points, axis=1))
        iteration += 1
        if max_movement < movement_thresh:
            print(f"Snake converged at iteration {iteration}, max movement={max_movement:.3f}")
            break
        if iteration > max_iter:
            print("Reached max iterations (safety stop)")
            break

    return points











# =============================
#REMOVE DUPLICATED POINTS
def remove_duplicate_contour_points(contour):
    """Remove only points that map to the same pixel (after rounding to int)."""
    contour = np.asarray(contour, dtype=np.float32)
    if contour.ndim != 2 or contour.shape[1] != 2 or len(contour) == 0:
        return contour

    cleaned = [contour[0]]
    seen = {(int(round(contour[0, 0])), int(round(contour[0, 1])))}

    for p in contour[1:]:
        key = (int(round(p[0])), int(round(p[1])))
        if key not in seen:
            cleaned.append(p)
            seen.add(key)

    cleaned = np.asarray(cleaned, dtype=np.float32)
    if len(cleaned) > 1 and np.array_equal(cleaned[0], cleaned[-1]):
        cleaned = cleaned[:-1]

    return cleaned


