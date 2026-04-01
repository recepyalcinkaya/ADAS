import pygame
import serial
import pynmea2
import xml.etree.ElementTree as ET
import numpy as np
from filterpy.kalman import KalmanFilter
import time
import math
import os

# --- KONFİGÜRASYON AYARLARI ---
USE_SIMULATOR = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KML_FILE_PATH = os.path.join(BASE_DIR, 'data', 'yol.kml')
COM_PORT = 'COM3'
BAUD_RATE = 9600

# Ekran ve Renk Ayarları
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 600
BG_COLOR = (100, 200, 100) # Açık yeşil arka plan
ROUTE_COLOR = (100, 100, 100)  # Gri rota çizgisi
ROUTE_LINE_WIDTH = 3          # Rota çizgisi kalınlığı
RAW_GPS_COLOR = (255, 255, 0) # Sarı ham GPS noktası
KALMAN_COLOR = (0, 150, 255)  # Mavi Kalman Filtresi noktası

# Bitiş Noktası Koordinatları (Enlem, Boylam sırası)
FINISH_POINT = (37.74011, 29.10263)
FINISH_RADIUS_DEGREES = 0.00003 # Bitiş noktası algılama yarıçapı (derece cinsinden)
LAP_COOLDOWN_TIME = 3.0 # Saniye cinsinden tur sayım cooldown süresi

# --- KALMAN FİLTRESİ ---
kf = KalmanFilter(dim_x=4, dim_z=2)

kf.F = np.array([[1, 0, 0.1, 0],
                 [0, 1, 0, 0.1],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

kf.H = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0]])

# ÖLÇÜM GÜRÜLTÜSÜ KOVARYANSI (R)
kf.R *= 0.3 

# SÜREÇ GÜRÜLTÜSÜ KOVARYANSI (Q)
kf.Q = np.array([[0.002, 0, 0.002, 0], 
                 [0, 0.002, 0, 0.002],
                 [0.002, 0, 0.02, 0], 
                 [0, 0.002, 0, 0.02]])

# Başlangıç durumu [lat, lon, dlat, dlon]
kf.x = np.array([[37.74002], [29.10275], [0.], [0.]])

# --- FONKSİYONLAR ---
def parse_kml(file_path):
    points = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        namespace = {'kml': 'http://www.opengis.net/kml/2.2'}
        line_strings = root.findall(".//kml:LineString", namespace)

        if not line_strings:
            print(f"UYARI: '{file_path}' dosyasinda <LineString> etiketi bulunamadi.")
            return []

        for ls in line_strings:
            coordinates_tag = ls.find('kml:coordinates', namespace)
            if coordinates_tag is not None:
                coords_text = coordinates_tag.text.strip()
                for line in coords_text.split():
                    parts = line.split(',')
                    if len(parts) >= 2:
                        try:
                            lon = float(parts[0])
                            lat = float(parts[1])
                            points.append((lat, lon))
                        except ValueError as ve:
                            print(f"UYARI: Geçersiz koordinat formati: {line} - {ve}")
                
                if points:
                    print(f"KML dosyasindan {len(points)} rota noktasi bulundu.")
                    return points

        if not points:
            print(f"UYARI: '{file_path}' dosyasinda geçerli rota koordinatlari bulunamadi.")
            
    except FileNotFoundError:
        print(f"HATA: '{file_path}' dosyasi bulunamadi. Lütfen dosyanin doğru yerde olduğundan emin olun.")
        return []
    except ET.ParseError as pe:
        print(f"HATA: KML dosyasini ayriştirma hatasi (XML formati sorunu?): {pe}")
        return []
    except Exception as e:
        print(f"HATA: KML dosyasini işlerken beklenmeyen bir hata oluştu: {e}")
        return []

    return points

def find_route_bounds(route_points):
    """Rotalarin enlem ve boylam sinirlarini bulur."""
    lats = [p[0] for p in route_points]
    lons = [p[1] for p in route_points]
    
    # Bitiş noktasını da sınır hesaplamasına dahil et
    all_lats = lats + [FINISH_POINT[0]]
    all_lons = lons + [FINISH_POINT[1]]

    return min(all_lats), max(all_lats), min(all_lons), max(all_lons)

def world_to_screen(lat, lon, bounds, screen_size):
    min_lat, max_lat, min_lon, max_lon = bounds
    screen_w, screen_h = screen_size

    lat_range = max_lat - min_lat
    lon_range = max_lon - min_lon

    if lat_range == 0:
        lat_range = 0.0001
    if lon_range == 0:
        lon_range = 0.0001

    # Ekran ve rota oranlarını hesapla
    route_aspect_ratio = lon_range / lat_range
    screen_aspect_ratio = screen_w / screen_h

    # Harita en-boy oranını koruyacak şekilde en küçük ölçek faktörünü kullan
    scale_x = screen_w / lon_range
    scale_y = screen_h / lat_range
    scale = min(scale_x, scale_y) * 0.9  # %10 margin bırak

    # Pist ekran ortasına gelsin diye offset hesapla
    offset_x = (screen_w - (lon_range * scale)) / 2
    offset_y = (screen_h - (lat_range * scale)) / 2

    # Koordinatı ekrana çevir
    x = (lon - min_lon) * scale + offset_x
    y = (max_lat - lat) * scale + offset_y

    return int(x), int(y)

def find_closest_point_on_route(point, route_segments):
    """Verilen bir noktaya rota üzerindeki en yakin noktayi bulur (Map Matching)."""
    point_vec = np.array(point)
    min_dist_sq = float('inf')
    closest_point = None
    closest_segment_idx = -1

    for i, (p1, p2) in enumerate(route_segments):
        p1_vec, p2_vec = np.array(p1), np.array(p2)
        line_vec = p2_vec - p1_vec
        
        line_len_sq = np.dot(line_vec, line_vec)
        if line_len_sq == 0:
            continue
            
        point_line_vec = point_vec - p1_vec
        
        t = np.dot(point_line_vec, line_vec) / line_len_sq
        t = max(0, min(1, t))

        projection = p1_vec + t * line_vec
        
        dist_sq = np.sum((point_vec - projection)**2)

        if dist_sq < min_dist_sq:
            min_dist_sq = dist_sq
            closest_point = tuple(projection)
            closest_segment_idx = i
            
    return closest_point, closest_segment_idx

def haversine_distance(lat1, lon1, lat2, lon2):
    """İki coğrafi nokta arasindaki mesafeyi metre cinsinden hesaplar (Haversine formülü)."""
    R = 6371000 # Dünya'nın ortalama yarıçapı metre cinsinden

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

# --- GPS SİMÜLATÖRÜ ---
class GpsSimulator:
    def __init__(self, route_points):
        self.route_points = route_points
        self.index = 0
        self.noise_level = 0.00001

    def get_mock_data(self):
        base_point = self.route_points[self.index]
        self.index = (self.index + 1) % len(self.route_points)

        mock_lat = base_point[0] + (np.random.rand() - 0.5) * self.noise_level
        mock_lon = base_point[1] + (np.random.rand() - 0.5) * self.noise_level
        
        class MockMsg:
            def __init__(self, lat, lon):
                self.latitude = lat
                self.longitude = lon
                self.is_valid = True

        return MockMsg(mock_lat, mock_lon)

# --- ANA UYGULAMA ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("GPS Pist Takibi")
    clock = pygame.time.Clock()

    try:
        font = pygame.font.Font(None, 36)
    except pygame.error:
        print("Sistem fontu yüklenemedi, varsayilan font kullanilacak.")
        font = pygame.font.SysFont("Arial", 36)

    try:
        route_points = parse_kml(KML_FILE_PATH)
        if not route_points:
            print(f"HATA: '{KML_FILE_PATH}' dosyasindan rota verisi okunamadi veya dosya boş.")
            return
    except FileNotFoundError:
        print(f"HATA: '{KML_FILE_PATH}' dosyasi bulunamadi. Lütfen dosyanin doğru yerde olduğundan emin olun.")
        return
        
    bounds = find_route_bounds(route_points)
    route_segments = list(zip(route_points, route_points[1:]))
    screen_route = [world_to_screen(lat, lon, bounds, (SCREEN_WIDTH, SCREEN_HEIGHT)) for lat, lon in route_points]
    
    screen_finish_point = world_to_screen(FINISH_POINT[0], FINISH_POINT[1], bounds, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # GÖRSEL YÜKLEME
    try:
        finish_img_path = os.path.join(BASE_DIR, 'assets', 'dama.png')
        car_img_path = os.path.join(BASE_DIR, 'assets', 'arac.png')
        
        finish_line_image = pygame.image.load(finish_img_path).convert_alpha()
        car_image = pygame.image.load(car_img_path).convert_alpha()
    except pygame.error as e:
        print(f"Görsel yüklenirken hata oluştu: {e}")
        pygame.quit()
        return

    # Görsel Boyutlandırma:
    # Bitiş çizgisi için:
    TARGET_FINISH_LINE_WIDTH = 40   # Piksel olarak istediğiniz genişlik
    TARGET_FINISH_LINE_HEIGHT = 15  # Piksel olarak istediğiniz yükseklik
    finish_line_image = pygame.transform.scale(finish_line_image, (TARGET_FINISH_LINE_WIDTH, TARGET_FINISH_LINE_HEIGHT))
    
    FINISH_LINE_ROTATION = 0 # Derece cinsinden döndürme (saat yönünün tersine pozitif)
    finish_line_image = pygame.transform.rotate(finish_line_image, FINISH_LINE_ROTATION)
    finish_line_rect = finish_line_image.get_rect(center=screen_finish_point) 

    # Araç markerı için:
    # 'arac.png' görseli için uygun boyutlandırma
    TARGET_CAR_WIDTH = 25   # Piksel olarak istediğiniz genişlik
    TARGET_CAR_HEIGHT = 25 # Piksel olarak istediğiniz yükseklik
    car_image = pygame.transform.scale(car_image, (TARGET_CAR_WIDTH, TARGET_CAR_HEIGHT))

    gps_source = None
    if USE_SIMULATOR:
        print("GPS Simülatörü kullaniliyor.")
        gps_source = GpsSimulator(route_points)
    else: # Gerçek GPS
        try:
            print(f"{COM_PORT} portu üzerinden GPS modülüne bağlaniliyor...")
            gps_source = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
            print("Bağlanti başarili.")
        except serial.SerialException as e:
            print(f"HATA: GPS modülüne bağlanilamadi: {e}")
            return

    raw_gps_pos = None
    kalman_pos = None
    final_pos = None
    
    last_update_time = time.time()

    lap_count = 0
    is_in_finish_zone = False 
    lap_cooldown_active = False
    lap_cooldown_end_time = 0.0

    SMOOTHING_ALPHA = 0.6 
    smoothed_final_pos = None 

    fixed_car_heading = 0 # Aracın sabit yönü (derece cinsinden)
    
    # Yarışma süresi için başlangıç zamanı
    start_time = time.time()
    total_race_time = 0.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = time.time()
        dt = current_time - last_update_time
        last_update_time = current_time

        kf.F = np.array([[1, 0, dt, 0],
                         [0, 1, 0, dt],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

        # --- VERİ ALMA VE İŞLEME ---
        msg = None
        if USE_SIMULATOR:
            msg = gps_source.get_mock_data()
        else: # Gerçek GPS
            try:
                line = gps_source.readline().decode('utf-8', errors='ignore')
                if (line.startswith('$GPRMC') or line.startswith('$GNGGA')) and 'V' not in line.split(',')[2]:
                    msg = pynmea2.parse(line)
                elif line.startswith('$GPGGA') and int(line.split(',')[6]) > 0:
                    msg = pynmea2.parse(line)

            except pynmea2.ParseError as e:
                pass
            except Exception as e:
                print(f"GPS verisi okunurken hata: {e}")
                time.sleep(0.1)
                continue

        if msg and hasattr(msg, 'latitude') and hasattr(msg, 'longitude') and msg.latitude != 0.0:
            raw_gps_pos = (msg.latitude, msg.longitude)
            
            if np.array_equal(kf.x[:2].flatten(), np.array([37.74002, 29.10275])): #başlangıç koordinatları
                 kf.x[0] = raw_gps_pos[0]
                 kf.x[1] = raw_gps_pos[1]

            kf.predict()
            kf.update(np.array([[raw_gps_pos[0]], [raw_gps_pos[1]]]))
            kalman_pos = (kf.x[0, 0], kf.x[1, 0])
            
            if kalman_pos:
                matched_pos, _ = find_closest_point_on_route(kalman_pos, route_segments)
                
                if matched_pos:
                    if smoothed_final_pos is None:
                        smoothed_final_pos = matched_pos
                    else:
                        smoothed_final_pos = (
                            SMOOTHING_ALPHA * matched_pos[0] + (1 - SMOOTHING_ALPHA) * smoothed_final_pos[0],
                            SMOOTHING_ALPHA * matched_pos[1] + (1 - SMOOTHING_ALPHA) * smoothed_final_pos[1]
                        )
                final_pos = smoothed_final_pos 

                # --- TUR SAYACI VE SÜRE MANTIĞI ---
                if final_pos: 
                    dist_to_finish = haversine_distance(final_pos[0], final_pos[1], FINISH_POINT[0], FINISH_POINT[1])
                    
                    if dist_to_finish < FINISH_RADIUS_DEGREES * 111139:
                        if not is_in_finish_zone:
                            is_in_finish_zone = True
                            if not lap_cooldown_active:
                                lap_count += 1
                                total_race_time = time.time() - start_time
                                print(f"Tur Tamamlandı! Tur Sayısı: {lap_count}")
                                print(f"Yarışma Süreniz: {total_race_time:.2f}") # Terminale çıktı
                                lap_cooldown_active = True
                                lap_cooldown_end_time = current_time + LAP_COOLDOWN_TIME
                    else:
                        is_in_finish_zone = False 
                        if lap_cooldown_active and current_time >= lap_cooldown_end_time:
                            lap_cooldown_active = False

        # --- ÇİZİM ---
        screen.fill(BG_COLOR)

        # Rotayı çiz
        if len(screen_route) > 1:
            for i in range(len(screen_route) - 1):
                start_pos = screen_route[i]
                end_pos = screen_route[i+1]
                pygame.draw.line(screen, ROUTE_COLOR, start_pos, end_pos, ROUTE_LINE_WIDTH)

        # Bitiş çizgisini çiz (dama.png ile)
        screen.blit(finish_line_image, finish_line_rect)

        # Ham GPS pozisyonunu çiz
        if raw_gps_pos:
            pos = world_to_screen(raw_gps_pos[0], raw_gps_pos[1], bounds, (SCREEN_WIDTH, SCREEN_HEIGHT))
            # pygame.draw.circle(screen, RAW_GPS_COLOR, pos, 6)

        # Kalman Filtresinden geçen pozisyonu çiz
        if kalman_pos:
            pos = world_to_screen(kalman_pos[0], kalman_pos[1], bounds, (SCREEN_WIDTH, SCREEN_HEIGHT))
            # pygame.draw.circle(screen, KALMAN_COLOR, pos, 8)
            
        # Yumuşatılmış yola yapıştırılmış araç markerını çiz
        if smoothed_final_pos:
            screen_car_pos = world_to_screen(smoothed_final_pos[0], smoothed_final_pos[1], bounds, (SCREEN_WIDTH, SCREEN_HEIGHT))

            # Aracın görselini sabit bir açıyla döndür (fixed_car_heading değeri)
            rotated_car_image = pygame.transform.rotate(car_image, fixed_car_heading) 
            
            # Döndürülmüş görselin yeni merkezini hesapla
            car_rect = rotated_car_image.get_rect(center=screen_car_pos)
            
            # Aracın görselini ekrana çiz
            screen.blit(rotated_car_image, car_rect)

        # Tur sayacını ekrana yazdır
        lap_text = font.render(f"Tur: {lap_count}", True, (0, 0, 0))
        screen.blit(lap_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    if not USE_SIMULATOR and gps_source and gps_source.is_open:
        gps_source.close()
        print("GPS bağlantısı kapatıldı.")

if __name__ == '__main__':
    main()
