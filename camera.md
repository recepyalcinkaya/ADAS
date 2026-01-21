Modelimi gerçek dünya senaryolarında test etmek için Logitech 1080p kameramı kullandım. Bu kamera, yüksek çözünürlüklü (1920x1080 piksel) görüntü yakalama yeteneği sayesinde, trafik ışıklarının detaylarını net bir şekilde algılamam için yeterli kalitede bir görüntü akışı sağladı. Kamerayı bilgisayarıma bağladım ve OpenCV kütüphanesi aracılığıyla canlı video akışını aldım. Kameranın 1080p çözünürlüğü, algılama modelimin küçük boyutlu veya uzaktaki trafik ışıklarını bile daha iyi ayırt eder

Bir bilgisayar görüşü uygulamasında kameraya erişim, kamera ayarlarını ayarlama ve kullanıcıya bilgi verme işlemlerini gerçekleştirmektedir.

camera_index: Bilgisayarda takılı olan kameraları temsil eden bir sayıdır.

cap = cv2.VideoCapture(camera_index): OpenCV kütüphanesini kullanarak belirlenen kamera indeksinden video akışını yakalamak için bir “VideoCapture” nesnesi oluşturur.

print(f"Hata: Kamera açılamadı. '{camera_index}' indeksinde kamera bulunamadı."): Eğer önceki if koşulu True ise (yani kamera açılamadıysa), bu hata mesajı konsola yazdırılır.

sys.exit(): Eğer kamera açılamazsa, bu satır programın hemen sonlandırılmasını sağlar.

actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)): Kameranın anlık video akışının genişliğini piksel cinsinden alır.

actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)): Kameranın anlık video akışının yüksekliğini piksel cinsinden alır ve “actual_height” değişkenine atar.

actual_fps = cap.get(cv2.CAP_PROP_FPS): Kameranın anlık kare hızını (FPS’ini) alır.
