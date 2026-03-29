import cv2
import argparse
from src.camera_calibrator import CameraCalibrator
from src.lane_detector import LaneTracker

def main():
    parser = argparse.ArgumentParser(description="ADAS Lane Tracking System")
    parser.add_argument("--video", type=str, default="data/test_videos/test_video.mp4", help="Test videosunun yolu")
    parser.add_argument("--calibrate", action="store_true", help="Kamerayı yeniden kalibre et")
    args = parser.parse_args()

    calibrator = CameraCalibrator()
    
    if args.calibrate or not calibrator.load_calibration("camera_calib.npz"):
        print("Kalibrasyon verisi bulunamadı veya yeniden isteniyor. Hesaplanıyor...")
        calibrator.calibrate("data/calibration_images/", "camera_calib.npz")
        calibrator.load_calibration("camera_calib.npz")

    tracker = LaneTracker(calibrator)

    cap = cv2.VideoCapture(args.video)
    
    if not cap.isOpened():
        print(f"Hata: {args.video} açılamadı. Dosya yolunu kontrol edin.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        result_frame = tracker.process_frame(frame)
        
        cv2.imshow("Lane Tracking System", result_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
