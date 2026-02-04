green_light_detected_flag = False değişkeni, "Yeşil yandı!" sesli uyarısının arka arkaya, gereksiz yere tekrarlanmasını önlemek için bir kontrol bayrağı görevi görür ve modelin o an ki karede bir "Green" (yeşil) trafik ışığı algılayıp algılamadığı kontrol edilir.

Eğer yeşil ışık algılanmışsa, ikinci kontrol devreye girer. Bu kontrol, daha önce de belirtildiği gibi, "Yeşil yandı!" uyarısının zaten verilip verilmediğini kontrol eder. Eğer henüz verilmediyse konsola "Yeşil yandı!" mesajı yazdırılır.

engine.say("Yeşil yandı") komutu ile “pyttsx3” kütüphanesi kullanılarak sesli uyarı tetiklenir.

engine.runAndWait() Sesli uyarının tamamen oynatılmasını bekler.
