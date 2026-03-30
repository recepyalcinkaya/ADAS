import cv2
import time
from src.vcu_monitor import VCUGearMonitor
from src.rear_camera import RearCameraStream
from src.distance_sensor import RearDistanceSensor

def main():
    print("ATAY EV ADAS: Rear-View System Initialized.")
    print("VCU sinyali bekleniyor... (Simülasyon: OpenCV penceresinde 'R' tuşuna basılı tutun)")

    # VCU'dan gelen geri vites sinyali için Raspberry Pi GPIO 18
    vcu_monitor = VCUGearMonitor(vcu_reverse_pin=18)
    rear_cam = RearCameraStream(camera_index=0) 
    ultrasonic = RearDistanceSensor(echo_pin=20, trig_pin=21)

    try:
        while True:
            is_reverse = vcu_monitor.check_reverse_engaged()

            # Simülasyon (Donanım yoksa R tuşu ile tetikle)
            key = cv2.waitKey(1) & 0xFF
            if not vcu_monitor.is_hardware:
                is_reverse = (key == ord('r'))

            if key == ord('q'):
                break

            if is_reverse:
                rear_cam.start()
                dist = ultrasonic.get_distance()
                frame = rear_cam.get_frame(dist)
                
                if frame is not None:
                    cv2.imshow("Dashboard: Rear-View Camera", frame)
            else:
                rear_cam.stop()
                cv2.destroyWindow("Dashboard: Rear-View Camera")
                
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nSistem kapatılıyor...")
        rear_cam.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
