Toplanan ve işlenen tüm verilerin kullanıcı için anlamlı hale gelmesi, iyi bir görselleştirme arayüzü ile mümkündür. Projemin bu ayağını, 2D oyun ve multimedya uygulamaları geliştirmek için tasarlanmış olan pygame kütüphanesi ile hayata geçirdim.

Çizim adımlarını aşağıda belirledim:

Ekranı Temizleme: Her bir kare (frame) çizilmeden önce “screen.fill(BG_COLOR)” komutu ile ekran, arka plan rengine boyanır. Bu, önceki karedeki çizimlerin silinmesini ve animasyonun temiz görünmesini sağlar.

Pist Rotasını Çizme: KML dosyasından okunan ve ekran koordinatlarına dönüştürülen “world_to_screen fonksiyonu” ile pist noktaları, “pygame.draw.line” komutu kullanılarak ardışık çizgiler halinde ekrana çizdim. Bu, pistin ana hattını oluşturdum.
