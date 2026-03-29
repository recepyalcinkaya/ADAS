import numpy as np
import cv2
from src.utils import threshold_image, get_perspective_transform_matrices

class LaneTracker:
    def __init__(self, calibrator):
        self.calibrator = calibrator
        self.left_fit = None
        self.right_fit = None

    def process_frame(self, frame):
        # 1. Distorsiyonu düzelt
        undistorted = self.calibrator.undistort(frame)
        h, w = undistorted.shape[:2]

        # 2. Renk ve Gradyan Eşikleme
        binary_img = threshold_image(undistorted)

        # 3. Kuş Bakışı (Perspective Transform)
        M, Minv = get_perspective_transform_matrices((w, h))
        binary_warped = cv2.warpPerspective(binary_img, M, (w, h), flags=cv2.INTER_LINEAR)

        # 4. Şerit Piksellerini Bul ve Eğri Uydur
        ploty, left_fitx, right_fitx = self.fit_polynomial(binary_warped)

        # 5. Tespit edilen şeridi orijinal resme çiz
        result = self.draw_lane(undistorted, binary_warped, Minv, ploty, left_fitx, right_fitx)
        return result

    def fit_polynomial(self, binary_warped):
        # Resmin alt yarısının histogramını alarak şeritlerin başlangıç noktalarını bul
        histogram = np.sum(binary_warped[binary_warped.shape[0]//2:, :], axis=0)
        midpoint = int(histogram.shape[0]//2)
        leftx_base = np.argmax(histogram[:midpoint])
        rightx_base = np.argmax(histogram[midpoint:]) + midpoint

        # Sliding Window (Kayan Pencere) Parametreleri
        nwindows = 9
        window_height = int(binary_warped.shape[0]//nwindows)
        nonzero = binary_warped.nonzero()
        nonzeroy = np.array(nonzero[0])
        nonzerox = np.array(nonzero[1])
        
        leftx_current = leftx_base
        rightx_current = rightx_base
        margin = 100
        minpix = 50
        
        left_lane_inds = []
        right_lane_inds = []

        # Pencereleri yukarı doğru kaydır
        for window in range(nwindows):
            win_y_low = binary_warped.shape[0] - (window+1)*window_height
            win_y_high = binary_warped.shape[0] - window*window_height
            win_xleft_low = leftx_current - margin
            win_xleft_high = leftx_current + margin
            win_xright_low = rightx_current - margin
            win_xright_high = rightx_current + margin
            
            good_left_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & 
            (nonzerox >= win_xleft_low) &  (nonzerox < win_xleft_high)).nonzero()[0]
            good_right_inds = ((nonzeroy >= win_y_low) & (nonzeroy < win_y_high) & 
            (nonzerox >= win_xright_low) &  (nonzerox < win_xright_high)).nonzero()[0]
            
            left_lane_inds.append(good_left_inds)
            right_lane_inds.append(good_right_inds)
            
            if len(good_left_inds) > minpix:
                leftx_current = int(np.mean(nonzerox[good_left_inds]))
            if len(good_right_inds) > minpix:
                rightx_current = int(np.mean(nonzerox[good_right_inds]))

        left_lane_inds = np.concatenate(left_lane_inds)
        right_lane_inds = np.concatenate(right_lane_inds)

        leftx = nonzerox[left_lane_inds]
        lefty = nonzeroy[left_lane_inds] 
        rightx = nonzerox[right_lane_inds]
        righty = nonzeroy[right_lane_inds] 

        # 2. dereceden polinom uydur: x = ay^2 + by + c
        if len(leftx) > 0 and len(rightx) > 0:
            self.left_fit = np.polyfit(lefty, leftx, 2)
            self.right_fit = np.polyfit(righty, rightx, 2)

        ploty = np.linspace(0, binary_warped.shape[0]-1, binary_warped.shape[0])
        
        if self.left_fit is not None and self.right_fit is not None:
            left_fitx = self.left_fit[0]*ploty**2 + self.left_fit[1]*ploty + self.left_fit[2]
            right_fitx = self.right_fit[0]*ploty**2 + self.right_fit[1]*ploty + self.right_fit[2]
        else:
            left_fitx, right_fitx = None, None

        return ploty, left_fitx, right_fitx

    def draw_lane(self, original_img, binary_warped, Minv, ploty, left_fitx, right_fitx):
        if left_fitx is None or right_fitx is None:
            return original_img

        warp_zero = np.zeros_like(binary_warped).astype(np.uint8)
        color_warp = np.dstack((warp_zero, warp_zero, warp_zero))

        pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
        pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
        pts = np.hstack((pts_left, pts_right))

        # Şeridin içini yeşil ile doldur
        cv2.fillPoly(color_warp, np.int_([pts]), (0, 255, 0))

        # Kuş bakışından orijinal perspektife geri dön
        newwarp = cv2.warpPerspective(color_warp, Minv, (original_img.shape[1], original_img.shape[0])) 
        
        # Orijinal resim ile şerit maskesini birleştir
        result = cv2.addWeighted(original_img, 1, newwarp, 0.3, 0)
        
        # Bilgi Ekranı Ekle
        cv2.putText(result, "Lane Tracking Active", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return result
