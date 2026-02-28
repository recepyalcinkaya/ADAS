# Eğitim ve Hiperparametre Rehberi

Bu bölüm, veri seti üzerinde model eğitilirken dikkat edilmesi gereken teknik kilit noktaları içerir.

## 1. Epoch Sayısı Nasıl Belirlenir?
Sabit bir sayı (örneğin "100 epoch") her zaman doğru değildir. Aşağıdaki strateji izlenmelidir:

* **Başlangıç:** Genellikle 100-300 epoch ile başlanabilir (Dataset boyutuna göre değişir).

* **Early Stopping (Erken Durdurma):** "Validation Loss" değeri belirli bir süre (örneğin 10-20 epoch boyunca) düşmeyi bırakıp artmaya başlarsa eğitim otomatik durdurulmalıdır. Bu, "Overfitting" (Ezberleme) başladığının işaretidir.

* **Kural:** Training Loss düşüyor ama Validation Loss artıyorsa -> **Overfitting**. Epoch sayısını azaltın veya Regularization (Dropout, Weight Decay) artırın.

## 2. Batch Size
* GPU belleğinin izin verdiği en yüksek 2'nin üssü (16, 32, 64) seçilmelidir.
* Küçük Batch Size (8-16): Daha gürültülü gradyanlar oluşturur, bazen yerel minimumlardan kaçmaya yardımcı olur (Regularization etkisi).
* Büyük Batch Size (64+): Daha stabil eğitim sağlar ancak "Learning Rate"in de orantılı artırılması gerekir.

## 3. Dikkat Edilmesi Gereken Metrikler
Sadece "Accuracy" yeterli değildir. Nesne tespiti için şu metrikleri takip edin:
* **mAP@0.5 (mean Average Precision):** Nesnenin ne kadar doğru sınıflandırıldığı ve kutunun ne kadar doğru çizildiği.
