Navigasyon sisteminin gerçek dünya koşullarında işlevselliğini test edebilmek ve doğruluğunu arttırmak amacıyla,
projemde Ublox NEO-M8N GPS modülünü kullanmaya karar verdim. Bu tercihimin en önemli nedeni, simülasyon ortamlarında 
elde edilemeyecek gerçek zamanlı, fiziksel dünya verilerine ulaşma isteğimdi.

NEO-M8N, hassas konumlama için sıklıkla tercih edilen, oldukça güvenilir bir GPS modülü olduğu kanısına vardım. Bu modül sayesinde, aracın anlık konum bilgilerini (enlem, boylam, hız, yön gibi) saniyelik güncellemelerle alabiliyorum. Projemin amacı, belirli bir parkur üzerinde yarış simülasyonu yapmak olduğundan, konum doğruluğu büyük önem taşıyor. NEO-M8N, 10 Hz'ye kadar veri güncelleme hızına çıkabilmesiyle, hızlı hareket eden araçlarda dahi oldukça stabil ve gecikmesiz veri sağlayabiliyor.

Gerçek bir GPS modülü kullanmamın en önemli faydası, projenin sahaya taşınabilirliğini sağlaması oldu. Yazılım tarafında simülasyon ortamında oluşturduğum algoritmalar, gerçek GPS verileriyle test edildiğinde olası sapmalar, gecikmeler ve çevresel etkiler daha net ortaya çıktı. Bu da beni algoritmaları daha dayanıklı ve optimize hale getirmeye zorladı. Böylece yazdığım kod sadece teorik olarak değil, pratikte de kullanılabilir bir hâl aldı.

Ayrıca, gerçek zamanlı veri akışı sayesinde projemi farklı ortamlarda test edebilme şansım oldu. Bu, modülün uydu sinyal kalitesi, şehir içi kullanımda yaşanabilecek sinyal zayıflamaları gibi gerçek hayat problemlerini gözlemlememe yardımcı oldu. Özellikle “cold start” ve “hot start” sürelerini test ederek, sistemin ilk açılışta ne kadar sürede konum verisi sağlamaya başladığını ölçtüm. Bu tür bilgiler, profesyonel bir navigasyon sisteminde performans değerlendirmesi yaparken büyük önem taşımaktadır.
