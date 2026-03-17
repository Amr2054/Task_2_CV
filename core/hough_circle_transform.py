import numpy as np
import cv2
import time

def hough_circle_transform(edges, edge_direction, min_dist,  min_r=15, max_r=105, voting_threshold=30):
    Y,X = np.where(edges != 0)
    directions = edge_direction[Y,X]
    
    radians = np.radians(directions)
    cosines = np.cos(radians)
    sines = np.sin(radians)
    
    accumulator = np.zeros((edges.shape[0], edges.shape[1],max_r-min_r+1), dtype=int)
    
    for r in range(min_r,max_r+1):
        a_neg = np.round(X - r * cosines).astype(int)
        a_pos = np.round(X + r * cosines).astype(int)
        b_neg = np.round(Y - r * sines).astype(int)
        b_pos = np.round(Y + r * sines).astype(int)
        
        mask_neg = (a_neg >= 0) & (a_neg < edges.shape[1]) & (b_neg >= 0) & (b_neg < edges.shape[0])
        mask_pos = (a_pos >= 0) & (a_pos < edges.shape[1]) & (b_pos >= 0) & (b_pos < edges.shape[0])
        
        np.add.at(accumulator, (b_neg[mask_neg], a_neg[mask_neg], r-min_r), 1)
        np.add.at(accumulator, (b_pos[mask_pos], a_pos[mask_pos], r-min_r), 1)
    
    b_coords, a_coords, r_indices = np.where(accumulator > voting_threshold)
    votes = accumulator[b_coords, a_coords, r_indices]
    
    # Sort by vote count (highest first)
    sort_idx = np.argsort(votes)[::-1]
    a_sorted = a_coords[sort_idx]
    b_sorted = b_coords[sort_idx]
    r_sorted = r_indices[sort_idx] + min_r
    
    # Apply min_dist filtering
    final_circles = []
    for i in range(len(a_sorted)):
        a_curr, b_curr, r_curr = a_sorted[i], b_sorted[i], r_sorted[i]
        
        is_too_close = False
        for (a_fit, b_fit, _) in final_circles:
            # Euclidean distance between centers
            dist = np.sqrt((a_curr - a_fit)**2 + (b_curr - b_fit)**2)
            
            if dist < min_dist:
                is_too_close = True
                break
        
        if not is_too_close:
            final_circles.append((a_curr, b_curr, r_curr))
            
    # Convert list back to arrays for output
    if not final_circles:#Empty
        return np.array([]), np.array([]), np.array([])
        
    best_a, best_b, best_r = zip(*final_circles)
    return np.array(best_a), np.array(best_b), np.array(best_r)

def draw_hough_circles(original_image, best_a, best_b,best_r):
    # Directly convert the guaranteed 2D grayscale image to BGR so we can draw in color
    output_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
    
    for a,b,r in zip(best_a,best_b,best_r):
        
        cv2.circle(output_image,(a,b),r,(0, 0, 255), 2)
    
    return output_image