try:
    from gpiozero import LED
    PI_ENV = True
except ImportError:
    PI_ENV = False

class MirrorLED:
    def __init__(self, pin, side_name):
        self.side_name = side_name
        self.is_hardware = PI_ENV
        self.state_is_on = False
        
        if self.is_hardware:
            self.led = LED(pin)
        else:
            self.led = None

    def turn_on(self):
        if not self.state_is_on: # Sadece durum değiştiğinde tetikle (İşlemciyi yormamak için)
            self.state_is_on = True
            if self.is_hardware:
                self.led.on()
            else:
                print(f"[{self.side_name} AYNASI] 🟡 UYARI LED'i YANDI!")

    def turn_off(self):
        if self.state_is_on:
            self.state_is_on = False
            if self.is_hardware:
                self.led.off()
            else:
                print(f"[{self.side_name} AYNASI] ⚫ UYARI LED'i SÖNDÜ.")
