import time
from src import DistanceSensorReader, BlindSpotAlerter, MirrorLED

def main():
    print("ADAS: Kör Nokta Sensörü ve Ayna LED Sistemi Başlatılıyor...")
    
    # 1. Donanım Pin Tanımlamaları (Raspberry Pi GPIO numaraları)
    # Kendi bağladığın pin numaralarına göre burayı değiştirebilirsin
    LEFT_ECHO_PIN, LEFT_TRIG_PIN = 24, 23
    RIGHT_ECHO_PIN, RIGHT_TRIG_PIN = 22, 27
    LEFT_LED_PIN = 17   # Sol ayna LED'inin bağlı olduğu GPIO pini
    RIGHT_LED_PIN = 26  # Sağ ayna LED'inin bağlı olduğu GPIO pini

    # 2. Sınıfları Başlat
    left_sensor = DistanceSensorReader(echo_pin=LEFT_ECHO_PIN, trig_pin=LEFT_TRIG_PIN)
    right_sensor = DistanceSensorReader(echo_pin=RIGHT_ECHO_PIN, trig_pin=RIGHT_TRIG_PIN)
    
    left_mirror_led = MirrorLED(pin=LEFT_LED_PIN, side_name="SOL")
    right_mirror_led = MirrorLED(pin=RIGHT_LED_PIN, side_name="SAĞ")

    alerter = BlindSpotAlerter(warning_threshold=2.5, danger_threshold=1.0)

    try:
        while True:
            # Sensörlerden anlık mesafeyi al
            dist_l = left_sensor.get_distance()
            dist_r = right_sensor.get_distance()

            # Mesafeleri analiz et
            status = alerter.evaluate_zone(dist_l, dist_r)

            # --- SOL AYNA LED KONTROLÜ ---
            # Eğer sol kör noktada araç varsa (DANGER veya WARNING durumu) sol LED'i yak
            if status["left_zone"] in ["WARNING", "DANGER"]:
                left_mirror_led.turn_on()
            else:
                left_mirror_led.turn_off()

            # --- SAĞ AYNA LED KONTROLÜ ---
            # Eğer sağ kör noktada araç varsa sağ LED'i yak
            if status["right_zone"] in ["WARNING", "DANGER"]:
                right_mirror_led.turn_on()
            else:
                right_mirror_led.turn_off()

            # Konsol Bilgilendirmesi (Sistem çalışıyor mu görmek için)
            if status["dashboard_warning"]:
                print(f"⚠️ KÖR NOKTA AKTİF -> Sol Mesafe: {dist_l}m | Sağ Mesafe: {dist_r}m", end='\r')
            else:
                print(f"✅ YOL TEMİZ         -> Sol Mesafe: {dist_l}m | Sağ Mesafe: {dist_r}m", end='\r')

            time.sleep(0.1) # Çok hızlı döngüyü engellemek için 100ms bekleme

    except KeyboardInterrupt:
        print("\nSistem kapatılıyor. Tüm LED'ler söndürülüyor...")
        left_mirror_led.turn_off()
        right_mirror_led.turn_off()

if __name__ == "__main__":
    main()
