“Ultralytics” kütüphanesini kullanarak bir YOLOv8 trafik işareti algılama modeli eğitiyorum.
“from ultralytics import YOLO” Bu satır, Ultralytics kütüphanesinden YOLO sınıfını içe aktarır.

"yolov8n.pt": Burada belirtilen .pt uzantılı dosya, önceden eğitilmiş model ağırlıklarını (pre-trained weights) temsil eder. "n" harfi "nano" anlamına gelir; yani bu, YOLOv8 ailesinin en küçük ve en hızlı modellerinden biridir

data="data.yaml": Bu parametre, modelin eğitileceği veri setinin yapılandırma dosyasının yolunu belirtir. data.yaml dosyası aşağıdaki bilgileri içerir:

•	train: Eğitim veri setini içeren görüntü ve etiket dosyalarının yolu.

•	val: Doğrulama (validation) veri setini içeren görüntü ve etiket dosyalarının yolu. Bu set, modelin eğitim sırasında görmediği veriler üzerindeki performansını izlemek için kullanılır ve aşırı öğrenmeyi (overfitting) tespit etmeye yardımcı olur.
•	names: Sınıf isimlerinin listesi (örneğin, ['traffic_light', 'car', 'person']).
