import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QGridLayout, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class ADASDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADAS Vehicle Dashboard UI")
        # Raspberry Pi / Dokunmatik ekranlar için tam ekran başlatma ayarı
        # self.showFullScreen() # Cihazda çalıştırırken bu satırın yorumunu kaldır
        self.resize(1024, 600) # Standart 7/10 inç dokunmatik ekran çözünürlüğü
        self.setStyleSheet("background-color: #1e1e2e;") # Koyu tema arka planı

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.create_ui()

    def create_ui(self):
        # Buton tanımlamaları (Metin, Arka Plan Rengi)
        buttons_config = [
            ("HIZ SABİTLEYİCİ", "#00b4d8"),   # Cyan
            ("OTOMATİK FAR", "#e9c46a"),      # Sarı
            ("GERİ GÖRÜŞ", "#2a9d8f"),        # Yeşil
            ("KÖR NOKTA", "#e76f51"),         # Kırmızı/Turuncu
            ("TRAFİK İŞARET", "#7b2cbf"),     # Mor
            ("ŞERİT TAKİP", "#00b4d8"),       # Cyan
        ]

        # İlk iki satırı oluştur (0 ve 1. satırlar, 0-1-2. sütunlar)
        row, col = 0, 0
        for text, color in buttons_config:
            btn = self.create_button(text, color)
            self.layout.addWidget(btn, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # --- ALT SATIR (Logolu Butonlar ve Navigasyon) ---
        
        # Pamukkale Üniversitesi Butonu (Sol Alt)
        pau_btn = self.create_image_button("assets/pau_logo.png", "#00b4d8")
        self.layout.addWidget(pau_btn, 2, 0)

        # Yarış Navigasyonu Butonu (Orta Alt)
        nav_btn = self.create_button("YARIŞ NAVİGASYONU", "#f4a261")
        self.layout.addWidget(nav_btn, 2, 1)

        # Teknofest Butonu (Sağ Alt)
        tekno_btn = self.create_image_button("assets/teknofest_logo.png", "#7b2cbf")
        self.layout.addWidget(tekno_btn, 2, 2)

    def create_button(self, text, bg_color):
        btn = QPushButton(text)
        btn.setSizePolicy(btn.sizePolicy().Expanding, btn.sizePolicy().Expanding)
        btn.setFont(QFont("Arial", 16, QFont.Bold))
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color};
                color: white;
                border-radius: 15px;
                border: 2px solid rgba(255, 255, 255, 0.2);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 0.5);
                border: 2px solid white;
            }}
        """)
        # Her butonun tıklama event'ini bağlama
        btn.clicked.connect(lambda _, t=text: self.module_clicked(t))
        return btn

    def create_image_button(self, image_path, bg_color):
        btn = QPushButton()
        btn.setSizePolicy(btn.sizePolicy().Expanding, btn.sizePolicy().Expanding)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color};
                border-radius: 15px;
                border: 2px solid rgba(255, 255, 255, 0.2);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 0.5);
            }}
        """)
        
        # Eğer asset klasöründe logo varsa ikonu butona ekle
        if os.path.exists(image_path):
            btn.setIcon(QIcon(image_path))
            btn.setIconSize(QSize(150, 150))
        else:
            btn.setText("LOGO BULUNAMADI") # Geçici metin
            btn.setFont(QFont("Arial", 10, QFont.Bold))
            
        btn.clicked.connect(lambda: self.module_clicked("LOGO_BUTTON"))
        return btn

    def module_clicked(self, module_name):
        # Gerçek sistemde bu fonksiyon, diğer Python scriptlerini (.py) tetikler
        print(f"[SYSTEM ROUTING]: {module_name} modülü başlatılıyor...")
        # Örnek: if module_name == "ŞERİT TAKİP": os.system("python lane_tracking.py")
