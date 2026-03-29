# Lane Tracking System (LTS)

A robust, real-time advanced lane detection pipeline built with OpenCV. This project demonstrates core Advanced Driver-Assistance Systems (ADAS) concepts by processing front-facing camera feeds to identify lane boundaries and estimate the drivable area.

## 🚀 Architecture & Pipeline
1. **Camera Calibration:** Corrects optical distortion from camera lenses using a computed camera matrix.
2. **Color & Gradient Thresholding:** Uses HLS color space (S-channel) and Sobel gradients to isolate lane pixels under various lighting conditions.
3. **Perspective Transform (Bird's-Eye View):** Maps the region of interest to a 2D top-down view to accurately measure curve geometry.
4. **Sliding Window Polynomial Fit:** Detects lane lines dynamically and fits a 2nd-order polynomial ($x = ay^2 + by + c$) to model the lane curvature.
5. **Inverse Transform:** Projects the detected lane area back onto the original frame.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Computer Vision:** OpenCV (`cv2`)
* **Math & Matrices:** NumPy

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/recepyalcinkaya/ADAS/lane-tracking-system.git](https://github.com/recepyalcinkaya/ADAS/lane-tracking-system.git)
   cd lane-tracking-system
