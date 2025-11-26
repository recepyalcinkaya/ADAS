GPS sistemleri, uydulardan gelen sinyallerin atmosferdeki bozulmaları, binalardan yansımaları ve uydu geometrisindeki değişimler gibi nedenlerle hatalı veya "gürültülü" veriler üretebilir. Bu durum, aracın konumunun harita üzerinde aniden zıplamasına veya titremesine neden olur. Bu gürültüyü temizlemek ve aracın gerçek hareketini daha pürüzsüz bir şekilde tahmin etmek için Kalman Filtresi'ni kullanılabilir.

Kalman Filtresi: Kalman Filtresi, güçlü bir özyinelemeli (recursive) matematiksel algoritmadır. Temel amacı, zaman içinde değişen bir sistemin durumunu, gürültülü ölçümler serisini kullanarak tahmin etmektir.

Filtre, iki ana adımda çalışır;
1.	Tahmin (Prediction): Sistem hakkında bildiğimiz dinamik modelini (örneğin, bir aracın sabit hızla gittiği varsayımı) kullanarak, bir sonraki zaman adımında sistemin durumunun ne olacağını ve bu tahmindeki belirsizliği tahmin eder.
2.	Güncelleme (Update): Gerçek sensörden (GPS) yeni bir ölçüm geldiğinde, bu ölçümü kullanarak ilk tahmini düzeltir. Filtre, hem kendi tahminindeki belirsizliği hem de gelen ölçümün gürültüsünü hesaba katarak en olası "gerçek" durumu hesaplar. Eğer filtre kendi tahminine çok güveniyorsa ve gelen ölçüm çok gürültülüyse, ölçümün etkisini azaltır. Aksi halde ise ölçüme daha fazla ağırlık verir.

Bu sürekli "tahmin et ve düzelt" döngüsü sayesinde Kalman Filtresi, anlık hatalı ölçümlerden çok fazla etkilenmeden, sistemin pürüzsüz bir şekilde çalışmasını sağlar.
