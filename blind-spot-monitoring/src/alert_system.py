class BlindSpotAlerter:
    def __init__(self, warning_threshold=2.5, danger_threshold=1.0):
        # Uyarı (Sarı) ve Tehlike (Kırmızı) mesafeleri (Metre cinsinden)
        self.warning_threshold = warning_threshold
        self.danger_threshold = danger_threshold

    def evaluate_zone(self, left_distance, right_distance):
        """Kör noktalardaki nesnelere göre aracın durumunu değerlendirir."""
        status = {
            "left_zone": "CLEAR",
            "right_zone": "CLEAR",
            "dashboard_warning": False
        }

        # Sol Sensör Kontrolü
        if left_distance <= self.danger_threshold:
            status["left_zone"] = "DANGER"
        elif left_distance <= self.warning_threshold:
            status["left_zone"] = "WARNING"

        # Sağ Sensör Kontrolü
        if right_distance <= self.danger_threshold:
            status["right_zone"] = "DANGER"
        elif right_distance <= self.warning_threshold:
            status["right_zone"] = "WARNING"

        # Eğer herhangi bir tarafta araç varsa, gösterge paneline uyarı gönder (Dashboard UI entegrasyonu için)
        if status["left_zone"] != "CLEAR" or status["right_zone"] != "CLEAR":
            status["dashboard_warning"] = True

        return status
