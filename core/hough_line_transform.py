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
    
    accumulator = np.zeros((diagonal*2+1, theta.shape[0]), dtype=int)
    
    radians = np.deg2rad(theta)
    cosines = np.cos(radians)
    sines = np.sin(radians)
    
    R = np.round(X * cosines + Y * sines).astype(int)
    R += diagonal
    R = R.ravel()
    
    theta_flat = np.tile(np.arange(181), len(X))
    np.add.at(accumulator, (R, theta_flat), 1)
    
    best_r,best_theta = np.where(accumulator>voting_threshold)
    
    return best_r-diagonal,best_theta

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