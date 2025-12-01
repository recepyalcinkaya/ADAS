GPS sistemleri, uydulardan gelen sinyallerin atmosferdeki bozulmaları, binalardan yansımaları ve uydu geometrisindeki değişimler gibi nedenlerle hatalı veya "gürültülü" veriler üretebilir. Bu durum, aracın konumunun harita üzerinde aniden zıplamasına veya titremesine neden olur. Bu gürültüyü temizlemek ve aracın gerçek hareketini daha pürüzsüz bir şekilde tahmin etmek için Kalman Filtresi'ni kullanılabilir.

Kalman Filtresi: Kalman Filtresi, güçlü bir özyinelemeli (recursive) matematiksel algoritmadır. Temel amacı, zaman içinde değişen bir sistemin durumunu, gürültülü ölçümler serisini kullanarak tahmin etmektir.

Filtre, iki ana adımda çalışır;
1.	Tahmin (Prediction): Sistem hakkında bildiğimiz dinamik modelini (örneğin, bir aracın sabit hızla gittiği varsayımı) kullanarak, bir sonraki zaman adımında sistemin durumunun ne olacağını ve bu tahmindeki belirsizliği tahmin eder.
2.	Güncelleme (Update): Gerçek sensörden (GPS) yeni bir ölçüm geldiğinde, bu ölçümü kullanarak ilk tahmini düzeltir. Filtre, hem kendi tahminindeki belirsizliği hem de gelen ölçümün gürültüsünü hesaba katarak en olası "gerçek" durumu hesaplar. Eğer filtre kendi tahminine çok güveniyorsa ve gelen ölçüm çok gürültülüyse, ölçümün etkisini azaltır. Aksi halde ise ölçüme daha fazla ağırlık verir.

Bu sürekli "tahmin et ve düzelt" döngüsü sayesinde Kalman Filtresi, anlık hatalı ölçümlerden çok fazla etkilenmeden, sistemin pürüzsüz bir şekilde çalışmasını sağlar.

Kalman Filtresi'nin teorik yapısını, kodumda “filterpy” kütüphanesi ve numpy matrisleri kullanarak somut bir şekilde uyguladım. Filtrenin davranışını belirleyen en önemli unsurlar, onun matematiksel modelini tanımlayan matrislerdir.

ÖLÇÜM VE SÜREÇ GÜRÜLTÜ KOVARYANSINI OPTİMİZE ETME:
kf.x (Durum Vektörü): Filtrenin takip ettiği değişkenleri temsil eder. Benim modelimde 4 durum değişkeni var: [enlem, boylam, enlemdeki_hız, boylamdaki_hız]. Filtrenin amacı bu dört değeri en doğru şekilde tahmin etmektir.

kf.F (Durum Geçiş Matrisi): Sistemin bir zaman adımından diğerine nasıl geçtiğini modeller. Benim kullandığım "sabit hız" modeline göre, yeni konum = eski konum + (hız * zaman_aralığı) ve yeni hız = eski hız. Bu matris, ana döngü içinde geçen süreye bağlı olarak sürekli güncellenir.

kf.H (Ölçüm Matrisi): Durum vektörünü, sensörden gelen ölçüm formatına dönüştürür. GPS'imiz bize sadece konumu (enlem, boylam) verir, hızı doğrudan ölçmez. Bu matris, 4 boyutlu durum vektörümüzden sadece ilk iki elemanı (enlem ve boylamı) alarak bunu modeller.

kf.R (Ölçüm Gürültüsü Kovaryansı): Bu matris, sensörümüzün (GPS) ne kadar "gürültülü" veya güvenilmez olduğunu filtreye söyler. R matrisindeki değerler ne kadar büyükse, filtre GPS'ten gelen ölçümlere o kadar az güvenir. 
