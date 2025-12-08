Gerçek GPS ile Haberleşme: Seri Port (COM)
Fiziksel bir GPS modülü, topladığı konum verisini genellikle NMEA formatında seri iletişim üzerinden bilgisayara gönderir.

Burada iki önemli konfigürasyon ayarı bulunmaktadır:

1-) BAUD_RATE = 9600 (Baud Hızı): Baud hızı, saniyede iletilen sinyal sayısını (ve dolayısıyla veri aktarım hızını) belirtir. Bu değerin hem GPS modülünün ayarlarında hem de benim kodumda aynı olması, verinin doğru ve kayıpsız bir şekilde okunabilmesi için zorunludur. 9600, birçok GPS modülü için standart bir varsayılan değerdir. Daha yüksek bir baud hızı (örn: 115200), daha yüksek frekansta (Hz) veri gönderen GPS modülleri için veri darboğazını önleyebilir.

2-) Hz (Frekans) ve Baud Hızı İlişkisi: GPS modülleri genellikle 1 Hz, 5 Hz veya 10 Hz gibi farklı güncelleme frekanslarında çalışabilir. Örneğin 10 Hz'lik bir GPS, saniyede 10 konum bilgisi üretir. Bu kadar sık veri gönderimi, yeterli bir BAUD_RATE gerektirir. Eğer baud hızı düşük kalırsa, seri porttaki tampon (buffer) dolarak veri kaybına veya gecikmelere (latency) yol açabilir. Projemde kullandığım standart 9600 baud hızı, 1 Hz'lik veri akışı için fazlasıyla yeterlidir. 
