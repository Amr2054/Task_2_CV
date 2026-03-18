import numpy as np

def get_chain_code(contour):
    step_size = 3.5  # Adjustable step size for interpolation
    chain_code = ""
    contour = np.asarray(contour).astype(float)

    if contour.ndim != 2 or contour.shape[1] != 2 or len(contour) < 2:
        return chain_code

    # 8-direction mapping
    direction_map = {
        (1, 0): '0',    # East
        (1, -1): '1',   # North-East
        (0, -1): '2',   # North
        (-1, -1): '3',  # North-West
        (-1, 0): '4',   # West
        (-1, 1): '5',   # South-West
        (0, 1): '6',    # South
        (1, 1): '7'     # South-East
    }

    for i in range(len(contour)):
        x1, y1 = contour[i]
        x2, y2 = contour[(i + 1) % len(contour)]  # circular

        dx = x2 - x1
        dy = y2 - y1

        # Determine the number of steps based on adjustable step_size
        steps = max(int(max(abs(dx), abs(dy)) // step_size), 1)

        for s in range(1, steps + 1):
            # Interpolate intermediate point
            curr_x = x1 + dx * s / steps
            curr_y = y1 + dy * s / steps

            # Calculate unit direction from previous point
            prev_x = x1 if s == 1 else x1 + dx * (s-1) / steps
            prev_y = y1 if s == 1 else y1 + dy * (s-1) / steps

            dir_x = int(np.sign(curr_x - prev_x))
            dir_y = int(np.sign(curr_y - prev_y))

            if (dir_x, dir_y) != (0, 0):
                code = direction_map.get((dir_x, dir_y))
                if code is not None:
                    chain_code += code

    # Format into groups of 6 digits
    formatted_chain_code = " ".join(chain_code[i:i+6] for i in range(0, len(chain_code), 6))
    return formatted_chain_code




# def get_chain_code(contour):
#     chain_code = ""
#     contour = np.asarray(contour).astype(float)

#     if contour.ndim != 2 or contour.shape[1] != 2 or len(contour) < 2:
#         return chain_code

#     # 8-direction mapping
#     direction_map = {
#         (1, 0): '0',    # East
#         (1, -1): '1',   # North-East
#         (0, -1): '2',   # North
#         (-1, -1): '3',  # North-West
#         (-1, 0): '4',   # West
#         (-1, 1): '5',   # South-West
#         (0, 1): '6',    # South
#         (1, 1): '7'     # South-East
#     }

#     for i in range(len(contour)):
#         x1, y1 = contour[i]
#         x2, y2 = contour[(i + 1) % len(contour)]  # circular

#         dir_x = int(np.sign(x2 - x1))
#         dir_y = int(np.sign(y2 - y1))

#         if (dir_x, dir_y) != (0, 0):
#             code = direction_map.get((dir_x, dir_y))
#             if code is not None:
#                 chain_code += code

#     # Format into groups of 6 digits
#     formatted_chain_code = " ".join(chain_code[i:i+6] for i in range(0, len(chain_code), 6))
#     return formatted_chain_code