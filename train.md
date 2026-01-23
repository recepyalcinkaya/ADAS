“Ultralytics” kütüphanesini kullanarak bir YOLOv8 trafik işareti algılama modeli eğitiyorum.
“from ultralytics import YOLO” Bu satır, Ultralytics kütüphanesinden YOLO sınıfını içe aktarır.

"yolov8n.pt": Burada belirtilen .pt uzantılı dosya, önceden eğitilmiş model ağırlıklarını (pre-trained weights) temsil eder. "n" harfi "nano" anlamına gelir; yani bu, YOLOv8 ailesinin en küçük ve en hızlı modellerinden biridir

data="data.yaml": Bu parametre, modelin eğitileceği veri setinin yapılandırma dosyasının yolunu belirtir. data.yaml dosyası aşağıdaki bilgileri içerir:

•	train: Eğitim veri setini içeren görüntü ve etiket dosyalarının yolu.

•	val: Doğrulama (validation) veri setini içeren görüntü ve etiket dosyalarının yolu. Bu set, modelin eğitim sırasında görmediği veriler üzerindeki performansını izlemek için kullanılır ve aşırı öğrenmeyi (overfitting) tespit etmeye yardımcı olur.

•	names: Sınıf isimlerinin listesi (örneğin, ['traffic_light', 'car', 'person']).

“epochs=30”: Bu parametre, modelin tüm eğitim veri setini kaç kez göreceğini ve üzerinden öğreneceğini belirtir. Epoch, bir eğitim döngüsünün tamamlanması anlamına gelir. 30 epoch, bu özel durum için belirlenmiş eğitim süresidir. Daha fazla epoch genellikle daha iyi performans sağlayabilir, ancak aynı zamanda aşırı öğrenmeye yol açabilir (overfitting).

imgsz=640: Bu parametre, modelin giriş görüntülerinin boyutunu belirler. Görüntüler, modele beslenmeden önce 640x640 piksel boyutuna yeniden boyutlandırılır. Bu, YOLO modellerinde yaygın olarak kullanılan bir boyuttur ve hız ile doğruluk arasında iyi bir denge sunar.

Eğittiğim YOLOv8 modelimin ağırlıklarını (parametrelere verilen isim) Python programıma yüklememi sağlıyor. Bu adım, modelin canlı kamera görüntüleri üzerinde nesne algılama yapabilmesi için gereklidir. 

“trained_model_path” eğittiğim modelimin bilgisayarımda kayıtlı olduğu yolu tanımlar.
