import cv2
import numpy as np

class RearCameraStream:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None

    def start(self):
        if self.cap is None or not self.cap.isOpened():
            self.cap = cv2.VideoCapture(self.camera_index)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def stop(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def draw_ev_hud(self, frame, distance):
        h, w = frame.shape[:2]
        
        # Park Çizgileri (Yeşil, Sarı, Kırmızı)
        center_x, bottom_y, top_y = w // 2, h, h // 2 + 50
        width_bottom, width_top = 400, 150

        # Yeşil (Güvenli)
        pts_green = np.array([[center_x - width_top//2, top_y], [center_x + width_top//2, top_y], 
                              [center_x + width_bottom//2 - 50, bottom_y - 100], [center_x - width_bottom//2 + 50, bottom_y - 100]], np.int32)
        cv2.polylines(frame, [pts_green], isClosed=False, color=(0, 255, 0), thickness=2)

        # Kırmızı (Tehlike)
        pts_red = np.array([[center_x - width_bottom//2 + 10, bottom_y - 40], [center_x + width_bottom//2 - 10, bottom_y - 40], 
                            [center_x + width_bottom//2 + 20, bottom_y], [center_x - width_bottom//2 - 20, bottom_y]], np.int32)
        cv2.polylines(frame, [pts_red], isClosed=False, color=(0, 0, 255), thickness=3)

        # --- YARIŞ ARACI TELEMETRİSİ (OSD) ---
        # Üst Bilgi Çubuğu
        cv2.rectangle(frame, (0, 0), (w, 40), (0, 0, 0), -1)
        cv2.putText(frame, "ATAY EV - REAR CAM", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, "VCU: LINKED", (w - 150, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Mesafe Sensörü Verisi
        warning_text = f"REAR DISTANCE: {distance}m"
        text_color = (0, 255, 0) if distance > 1.5 else (0, 0, 255)
        cv2.putText(frame, warning_text, (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)
        
        if distance <= 0.5:
             cv2.putText(frame, "STOP!", (center_x - 80, h // 2), cv2.FONT_HERSHEY_DUPLEX, 2.5, (0, 0, 255), 4)

        return frame

    def get_frame(self, distance):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return self.draw_ev_hud(frame, distance)
        return None
