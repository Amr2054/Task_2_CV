import numpy as np
import cv2
import time
from skimage.transform import hough_ellipse
from skimage.feature import canny

def hough_ellipse_transform(edges,voting_threshold=60,min_dist=4):
    Y,X = np.where(edges != 0)
    ellipses = []
    i = 0
    
    while i < X.shape[0]:
        x1,y1 = X[i],Y[i]
        ellipse_detected = False
        j = i + 1
        
        while j < X.shape[0]:
            x2,y2 = X[j],Y[j]
            
            major_axis = np.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))
            
            if major_axis < min_dist:
                j+=1
                continue
            
            xo = (x1+x2) / 2
            yo = (y1+y2) / 2
            a = major_axis / 2
            orientation = np.degrees(np.arctan2((y2 - y1), (x2 - x1)))
            
            accumulator = np.zeros(int(np.ceil(a)) + 2)
            
            dist = np.sqrt((X - xo)*(X - xo) + (Y - yo)*(Y - yo))
            
            valid = (dist > min_dist) & (dist < a)
            X_val, Y_val, d = X[valid], Y[valid], dist[valid]
            
            f = np.sqrt((X_val - x2)*(X_val - x2) + (Y_val - y2)*(Y_val - y2))
            
            # ensure value is within arccos domain [-1, 1]
            val = (a*a + d*d - f*f) / (2 * a * d)
            domain_mask = (val >= -1.0) & (val <= 1.0)
            
            d = d[domain_mask]
            val = val[domain_mask]
            
            Taw = np.arccos(val)
            cosineTaw = np.cos(Taw)
            sineTaw = np.sin(Taw)
            
            denominator = (a*a - d*d*cosineTaw*cosineTaw)
            
            denominator_mask = denominator>0
            denominator = denominator[denominator_mask]
            d = d[denominator_mask]
            sineTaw = sineTaw[denominator_mask]
            
            b = np.sqrt((a*a*d*d*sineTaw*sineTaw) / (denominator))
            
            b_idx = np.round(b).astype(int)
            b_idx = b_idx[b_idx < accumulator.shape[0]]
            
            if b_idx.shape[0] > 0:
                counts = np.bincount(b_idx)
                accumulator[:counts.shape[0]] += counts
            
            best_b = np.argmax(accumulator)
            if accumulator[best_b] > voting_threshold:
                
                ellipses.append([yo, xo, a, best_b, orientation])
                
                # --- PIXEL REMOVAL LOGIC ---
                c = np.sqrt(abs(a*a - best_b*best_b)) 
                rad = np.radians(orientation)
                f1_x = xo + c * np.cos(rad)
                f1_y = yo + c * np.sin(rad)
                f2_x = xo - c * np.cos(rad)
                f2_y = yo - c * np.sin(rad)
                dist_to_f1 = np.sqrt((X - f1_x)**2 + (Y - f1_y)**2)
                dist_to_f2 = np.sqrt((X - f2_x)**2 + (Y - f2_y)**2)
                sum_of_distances = dist_to_f1 + dist_to_f2
                tolerance = 2.0  # For line thickness
                keep_mask = np.abs(sum_of_distances - (2 * a)) > tolerance
                
                # Overwrite arrays with only the remaining pixels
                X = X[keep_mask]
                Y = Y[keep_mask]
                
                ellipse_detected = True
                # Break out of the j loop immediately because our arrays just shrank!
                break 
                
            # if no ellipse was found for this pair
            j += 1
            
        # Don't need to update i because i will refer to new point when shrink points after detecting ellipse
        if not ellipse_detected:
            i += 1
        
    return ellipses

def draw_hough_ellipse(original_image,ellipses):
    """_summary_

    Args:
        ellipses: array of ellipses
    returns: drawn ellipse on the input image
    """
    output_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
    
    for ellipse in ellipses:
        k, h, a, b, alpha = ellipse
        cv2.ellipse(output_image, (int(h), int(k)), (int(a), int(b)), alpha, 0, 360, (255, 0, 0), 2)
    
    return output_image
