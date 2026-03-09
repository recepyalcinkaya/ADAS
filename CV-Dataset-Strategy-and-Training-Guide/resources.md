# Kaynaklar ve Araçlar
## 🛠 Veri Etiketleme Araçları
* **CVAT (Computer Vision Annotation Tool):** Video ve resim etiketleme için endüstri standardı.
* **LabelImg:** Basit, offline, XML/TXT formatı için hızlı araç.
* **Roboflow:** Veri seti yönetimi, versiyonlama ve otomatik augmentation için platform.

## 📚 Kilit Kavramlar ve Okumalar
* **Data Augmentation (Veri Çoğaltma):**
    * *Mozaik (Mosaic) Augmentation:* 4 farklı resmi birleştirerek küçük nesnelerin tespitini iyileştirir (YOLOv4+ ile popülerleşti).
* *MixUp:* İki resmi şeffaf bir şekilde üst üste bindirerek modelin kesin kararlar yerine olasılıksal düşünmesini sağlar.
* **Curriculum Learning:**
    * Modeli önce sadece "kolay/temiz" verilerle eğitip, epoch ilerledikçe "zor/problemli" verileri kademeli olarak eğitime dahil etme stratejisi.
* **IoU (Intersection over Union):**
    * Tahmin edilen kutu ile gerçek kutunun ne kadar örtüştüğünü gösteren metrik.
