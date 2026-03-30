import time

try:
    from gpiozero import DigitalInputDevice
    PI_ENV = True
except ImportError:
    PI_ENV = False

class VCUGearMonitor:
    def __init__(self, vcu_reverse_pin=18):
        self.is_hardware = PI_ENV
        self.is_reverse = False
        
        if self.is_hardware:
            # pull_up=False, çünkü VCU'dan temiz bir 3.3V (HIGH) sinyali bekliyoruz
            self.vcu_signal = DigitalInputDevice(vcu_reverse_pin, pull_up=False) 
        else:
            self.vcu_signal = None

    def check_reverse_engaged(self):
        """VCU'dan geri vites sinyalinin gelip gelmediğini döndürür (True/False)"""
        if self.is_hardware:
            self.is_reverse = self.vcu_signal.is_active
        else:
            # Simülasyon modunda ana dosyadan manuel tetiklenecek
            pass 
        return self.is_reverse
