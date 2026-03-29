import cv2
import numpy as np

def threshold_image(img, s_thresh=(170, 255), sx_thresh=(20, 100)):
    # Resmi HLS formatına çevir (Işık değişimlerine daha dayanıklıdır)
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    l_channel = hls[:, :, 1]
    s_channel = hls[:, :, 2]

    # Sobel X (Dikey çizgileri - şeritleri - bulmak için gradyan hesapla)
    sobelx = cv2.Sobel(l_channel, cv2.CV_64F, 1, 0)
    abs_sobelx = np.absolute(sobelx)
    scaled_sobel = np.uint8(255 * abs_sobelx / np.max(abs_sobelx))
    
    # Gradyan eşikleme
    sxbinary = np.zeros_like(scaled_sobel)
    sxbinary[(scaled_sobel >= sx_thresh[0]) & (scaled_sobel <= sx_thresh[1])] = 1

    # Renk eşikleme (S kanalı)
    s_binary = np.zeros_like(s_channel)
    s_binary[(s_channel >= s_thresh[0]) & (s_channel <= s_thresh[1])] = 1

    # İkisini birleştir
    combined_binary = np.zeros_like(sxbinary)
    combined_binary[(s_binary == 1) | (sxbinary == 1)] = 1

    return combined_binary

def get_perspective_transform_matrices(img_size):
    w, h = img_size
    # Bu noktalar kameranın açısına göre yola bakarak manuel ayarlanır (Örnek değerlerdir)
    src = np.float32([
        [w * 0.45, h * 0.65],
        [w * 0.55, h * 0.65],
        [w * 0.15, h],
        [w * 0.95, h]
    ])
    dst = np.float32([
        [w * 0.2, 0],
        [w * 0.8, 0],
        [w * 0.2, h],
        [w * 0.8, h]
    ])
    
    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)
    return M, Minv
