import time
import random

try:
    from gpiozero import DistanceSensor
    PI_ENV = True
except ImportError:
    PI_ENV = False
    print("Uyarı: Simülasyon modunda çalışılıyor. Gerçek sensör verisi alınamıyor.")

class RearDistanceSensor:
    def __init__(self, echo_pin=20, trig_pin=21, max_distance=4.0):
        self.is_hardware = PI_ENV
        self.max_distance = max_distance
        
        if self.is_hardware:
            # Arka tampon mesafe sensörü pinleri
            self.sensor = DistanceSensor(echo=echo_pin, trigger=trig_pin, max_distance=max_distance)
        else:
            self.sensor = None
            self.mock_distance = max_distance # Simülasyon başlangıç mesafesi

    def get_distance(self):
        """Sensörden gelen mesafeyi metre cinsinden döndürür."""
        if self.is_hardware:
            return round(self.sensor.distance, 2)
        else:
            # Simülasyon: Geri geri giderken arkadaki duvara yaklaşmayı simüle et
            self.mock_distance -= 0.05
            
            # Duvara çok yaklaşınca (0.2m) tekrar başa sar (Testi sürdürmek için)
            if self.mock_distance < 0.2: 
                self.mock_distance = self.max_distance
                
            time.sleep(0.05) # Sensör okuma gecikmesi
            return round(self.mock_distance, 2)
