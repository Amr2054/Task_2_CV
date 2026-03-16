import numpy as np
import cv2
import time

def hough_line_transform(edges,voting_threshold=70):
    Y,X = np.where(edges != 0)
    # This changes their shape from (N,) to (N, 1)
    X = X[:, np.newaxis]
    Y = Y[:, np.newaxis]
    
    diagonal = round(np.sqrt((edges.shape[0])*(edges.shape[0]) + (edges.shape[1])*(edges.shape[1])))
    theta = np.arange(0,181,1)
    
    accumulator = np.zeros((diagonal*2+1, theta.shape[0]+1), dtype=int)
    
    radians = np.deg2rad(theta)
    cosines = np.cos(radians)
    sines = np.sin(radians)
    
    R = np.round(X * cosines + Y * sines).astype(int).ravel()
    theta_flat = np.tile(np.arange(181), len(X))
    np.add.at(accumulator, (R, theta_flat), 1)
    
    best_r,best_theta = np.where(accumulator>voting_threshold)
    
    return best_r,best_theta

def draw_hough_lines(original_image, best_r, best_theta):
    output_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
        
    for r, theta_deg in zip(best_r, best_theta):
        theta_rad = np.radians(theta_deg)
        a = np.cos(theta_rad)
        b = np.sin(theta_rad)
        
        x0 = a * r
        y0 = b * r
        
        # Stretch the lines across the image
        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * (a))
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * (a))
        
        # Draw the line in RED (B=0, G=0, R=255)
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        
    return output_image

# if __name__ == "__main__":
#     image_path = '../Dataset/test_3.jpg' 
#     original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
#     if original_image is None:
#         print(f"Error: Could not load image at '{image_path}'. Check the file path.")
#     else:
#         edges = cv2.Canny(original_image, threshold1=50, threshold2=150)
    
#     start_time = time.time()
#     best_r, best_theta = hough_line_transform(edges, voting_threshold=70)
#     custom_time = time.time() - start_time
    
#     print(f"Custom Function: Detected {len(best_r)} lines in {custom_time:.4f} seconds.")
#     output_image_custom = draw_hough_lines(original_image, best_r, best_theta)
    
#     start_time = time.time()
#     # cv2.HoughLines parameters: image, rho resolution (1 pixel), theta resolution (1 degree in radians), threshold
#     cv2_lines = cv2.HoughLines(edges, 1, np.pi / 180, 70)
#     cv2_time = time.time() - start_time
    
#     num_cv2_lines = len(cv2_lines) if cv2_lines is not None else 0
#     print(f"OpenCV Function: Detected {num_cv2_lines} lines in {cv2_time:.4f} seconds.")
    
#     output_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
#     # Draw OpenCV lines
#     if cv2_lines is not None:
#         for line in cv2_lines:
#             rho, theta = line[0]
#             # Math to convert polar coordinates to Cartesian endpoints for drawing
#             a = np.cos(theta)
#             b = np.sin(theta)
#             x0 = a * rho
#             y0 = b * rho
#             # Extend the line by 1000 pixels in both directions
#             x1 = int(x0 + 1000 * (-b))
#             y1 = int(y0 + 1000 * (a))
#             x2 = int(x0 - 1000 * (-b))
#             y2 = int(y0 - 1000 * (a))
            
#             # Draw a red line, 2 pixels thick
#             cv2.line(output_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
#     # --- 3. DISPLAY RESULTS ---
#     cv2.imshow("1 - Canny Edges", edges)
#     cv2.imshow("2 - Custom Hough Lines", output_image_custom)
#     cv2.imshow("3 - OpenCV Hough Lines", output_image)
    
#     # Wait for the user to press any key, then close the windows safely
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()