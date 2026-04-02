from ultralytics import YOLO
import cv2
import sys
import os
import pyttsx3

def main():
    print("🚦 ADAS: Traffic Light Detection System Initializing...")

    # --- DOSYA YOLLARI VE MODEL YÜKLEME ---
    # Kodun çalıştığı dizini bulup, model dosyasının yerini dinamik olarak belirliyoruz
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    trained_model_path = os.path.join(BASE_DIR, "models", "best.pt")

    if not os.path.exists(trained_model_path):
        print(f"❌ HATA: Model dosyası bulunamadı. Lütfen eğittiğiniz 'best.pt' dosyasını 'models' klasörüne koyun.")
        print(f"Beklenen konum: {trained_model_path}")
        sys.exit()

    model = YOLO(trained_model_path)

    # --- SES MOTORU BAŞLATMA ---
    engine = pyttsx3.init()
    engine.setProperty('rate', 135)  # Konuşma hızı biraz hızlandırıldı (daha tepkisel olması için)

    # --- KAMERA AYARLARI ---
    camera_index = 0
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"❌ HATA: Kamera açılamadı. '{camera_index}' indeksinde donanım bulunamadı.")
        sys.exit()

    actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    actual_fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"✅ Kamera aktif. Çözünürlük: {actual_width}x{actual_height}, FPS: {actual_fps:.2f}")
    print("Sistem devrede. Çıkmak için 'q' tuşuna basın.")

    # Sesli uyarının sürekli tekrar etmemesi için kontrol bayrağı
    green_light_detected_flag = False

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Kameradan görüntü alınamıyor, döngü kırılıyor...")
                break

            # YOLO ile çıkarım (Inference)
            results = model(frame, conf=0.6, verbose=False)
            annotated_frame = results[0].plot()
            detected_class_names = [model.names[int(box.cls)] for box in results[0].boxes]

            # --- MANTIK VE SESLİ UYARI ---
            if "Green" in detected_class_names:
                if not green_light_detected_flag:
                    print("🟢 Yeşil Işık Algılandı! Sürücü uyarılıyor...")
                    engine.say("Yeşil yandı") 
                    engine.runAndWait()
                    green_light_detected_flag = True
            else:
                # Ekranda yeşil ışık yoksa bayrağı sıfırla ki bir sonraki yeşilde tekrar ötsün
                green_light_detected_flag = False

            # Görüntüyü ekrana yansıt
            cv2.imshow("ADAS: Traffic Light Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nSistem kullanıcı tarafından durduruldu.")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Kamera kapatıldı. Sistem güvenli bir şekilde sonlandırıldı.")

if __name__ == '__main__':
    main()
