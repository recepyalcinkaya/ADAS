GPS Simülatörü ve Faydaları:
Her test için dışarıya çıkıp GPS sinyali test etmenin yanı sıra bilgisayar ortamında test edebilmem için bir simülator kullanmaya karar verdim. Bu nedenle "USE_SIMULATOR = True" bayrağı ile aktif hale gelen bir "GpsSimulator" sınıfı oluşturdum.

Simülatör kullanmanın faydaları:
•	Bilgisayar ortamında test: Donanıma veya GPS sinyaline ihtiyaç duymadan, bilgisayar ortamında kodun mantığını test etme imkanı sunar.
•	Tekrarlanabilirlik: Simülatör, KML dosyasındaki rota noktalarını sırayla takip ettiği için, algoritmalarımın (Kalman, Map Matching) davranışını her seferinde aynı koşullar altında gözlemlememi ve hataları ayıklamamı kolaylaştırır.
•	Gürültü Simülasyonu: Kodda self.noise_level ile gerçek dünyadaki GPS hatalarını taklit eden rastgele küçük sapmalar ekledim. Bu, Kalman Filtresi'nin gürültüyü ne kadar iyi temizlediğini test etmek için çok faydalı oldu.

Simülatör, get_mock_data() fonksiyonu ile KML rotasındaki bir sonraki noktayı alıp üzerine küçük bir miktar rastgele gürültü ekleyerek sahte bir GPS mesaj nesnesi oluşturur. Bu nesne, pynmea2'nin oluşturduğu gerçek nesneyle aynı niteliklere (latitude, longitude) sahip olduğu için, programın geri kalanı verinin gerçek mi yoksa simülasyondan mı geldiğini fark etmeden çalışmaya devam edebilir. Bu "soyutlama" (abstraction) ilkesinin güzel bir örneğidir.
