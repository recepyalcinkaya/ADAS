GPS Simülatörü ve Faydaları:
Her test için dışarıya çıkıp GPS sinyali test etmenin yanı sıra bilgisayar ortamında test edebilmem için bir simülator kullanmaya karar verdim. Bu nedenle "USE_SIMULATOR = True" bayrağı ile aktif hale gelen bir "GpsSimulator" sınıfı oluşturdum.

Simülatör kullanmanın faydaları:
•	Bilgisayar ortamında test: Donanıma veya GPS sinyaline ihtiyaç duymadan, bilgisayar ortamında kodun mantığını test etme imkanı sunar.
•	Tekrarlanabilirlik: Simülatör, KML dosyasındaki rota noktalarını sırayla takip ettiği için, algoritmalarımın (Kalman, Map Matching) davranışını her seferinde aynı koşullar altında gözlemlememi ve hataları ayıklamamı kolaylaştırır.
•	Gürültü Simülasyonu: Kodda self.noise_level ile gerçek dünyadaki GPS hatalarını taklit eden rastgele küçük sapmalar ekledim. Bu, Kalman Filtresi'nin gürültüyü ne kadar iyi temizlediğini test etmek için çok faydalı oldu.
