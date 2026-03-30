import time
import random

# Raspberry Pi ortamında olup olmadığımızı kontrol ediyoruz
try:
    from gpiozero import DistanceSensor
    PI_ENV = True
except ImportError:
    PI_ENV = False
    print("Uyarı: gpiozero kütüphanesi bulunamadı veya Raspberry Pi'de değilsiniz. Simülasyon modunda çalışılacak.")

class DistanceSensorReader:
    def __init__(self, echo_pin, trig_pin, max_distance=4.0):
        self.is_hardware = PI_ENV
        self.max_distance = max_distance
        
        if self.is_hardware:
            # Gerçek ultrasonik/radar sensör pin tanımlamaları
            self.sensor = DistanceSensor(echo=echo_pin, trigger=trig_pin, max_distance=max_distance)
        else:
            self.sensor = None
            self.mock_distance = max_distance # Başlangıçta araç yok

    def get_distance(self):
        """Sensörden gelen mesafeyi metre cinsinden döndürür."""
        if self.is_hardware:
            return self.sensor.distance
        else:
            # Simülasyon: Rastgele araç yaklaşıp uzaklaşması simüle ediliyor
            fluctuation = random.uniform(-0.5, 0.5)
            self.mock_distance += fluctuation
            self.mock_distance = max(0.2, min(self.mock_distance, self.max_distance))
            time.sleep(0.1) # Sensör okuma gecikmesi simülasyonu
            return round(self.mock_distance, 2)
