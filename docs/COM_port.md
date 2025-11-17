Gerçek GPS ile Haberleşme: Seri Port (COM)
Fiziksel bir GPS modülü, topladığı konum verisini genellikle NMEA formatında seri iletişim üzerinden bilgisayara gönderir.

Burada iki önemli konfigürasyon ayarı bulunmaktadır:

1-) BAUD_RATE = 9600 (Baud Hızı): Baud hızı, saniyede iletilen sinyal sayısını (ve dolayısıyla veri aktarım hızını) belirtir. Bu değerin hem GPS modülünün ayarlarında hem de benim kodumda aynı olması, verinin doğru ve kayıpsız bir şekilde okunabilmesi için zorunludur. 9600, birçok GPS modülü için standart bir varsayılan değerdir. Daha yüksek bir baud hızı (örn: 115200), daha yüksek frekansta (Hz) veri gönderen GPS modülleri için veri darboğazını önleyebilir.
