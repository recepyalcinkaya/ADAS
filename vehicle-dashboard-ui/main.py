import sys
from PyQt5.QtWidgets import QApplication
from src.dashboard_app import ADASDashboard

def main():
    app = QApplication(sys.argv)
    
    # Dokunmatik ekranlar için tıklama hassasiyetini artırma
    app.setAttribute(0xAA) # Qt.AA_EnableHighDpiScaling
    
    dashboard = ADASDashboard()
    dashboard.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
