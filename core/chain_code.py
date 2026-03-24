import numpy as np
import math

def get_chain_code(contour):
    """
    8-direction Chain Code 
    """
    chain_code = []
    contour = np.asarray(contour).astype(float)

    if contour.ndim != 2 or contour.shape[1] != 2 or len(contour) < 2:
        return chain_code

    n = len(contour)

    for i in range(n):
        x1, y1 = contour[i]
        x2, y2 = contour[(i + 1) % n]  # circular

        dx = x2 - x1
        dy = y2 - y1

        # Round for exact pixel movements
        dx_r = int(round(dx))
        dy_r = int(round(dy))

        # Direct mapping (ideal case)
        if dx_r == 1 and dy_r == 0:
            code = 0
        elif dx_r == 1 and dy_r == 1:
            code = 1
        elif dx_r == 0 and dy_r == 1:
            code = 2
        elif dx_r == -1 and dy_r == 1:
            code = 3
        elif dx_r == -1 and dy_r == 0:
            code = 4
        elif dx_r == -1 and dy_r == -1:
            code = 5
        elif dx_r == 0 and dy_r == -1:
            code = 6
        elif dx_r == 1 and dy_r == -1:
            code = 7

        else:
            # Fallback: use angle
            angle = math.atan2(dy, dx)  # [-pi, pi]
            code = int(round(4 * angle / math.pi)) % 8

        chain_code.append(code)

    return chain_code







