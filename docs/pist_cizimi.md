Toplanan ve işlenen tüm verilerin kullanıcı için anlamlı hale gelmesi, iyi bir görselleştirme arayüzü ile mümkündür. Projemin bu ayağını, 2D oyun ve multimedya uygulamaları geliştirmek için tasarlanmış olan pygame kütüphanesi ile hayata geçirdim.

Çizim adımlarını aşağıda belirledim:

Ekranı Temizleme: Her bir kare (frame) çizilmeden önce “screen.fill(BG_COLOR)” komutu ile ekran, arka plan rengine boyanır. Bu, önceki karedeki çizimlerin silinmesini ve animasyonun temiz görünmesini sağlar.

Pist Rotasını Çizme: KML dosyasından okunan ve ekran koordinatlarına dönüştürülen “world_to_screen fonksiyonu” ile pist noktaları, “pygame.draw.line” komutu kullanılarak ardışık çizgiler halinde ekrana çizdim. Bu, pistin ana hattını oluşturdum.

Projenin kullanıcı deneyimini zenginleştirmek için basit geometrik şekiller yerine “PNG” formatında görseller kullandım.
-	Bitiş Çizgisi (dama.png): Damalı bayrak görselini yükledim. Pist üzerindeki bitiş çizgisine uyması için “pygame.transform.rotate” ile bu görseli belirli bir açıyla döndürdüm. “screen.blit(finish_line_image,finish_line_rect)” komutu ile de bu görseli bitiş noktasının koordinatlarına çizdirdim.

-	Araç (arac.png): Benzer şekilde, aracı temsil etmesi için bir araba ikonunu (arac.png) yükledim. Görselin boyutunu ayarladım. Aracın son, filtrelenmiş ve yola oturtulmuş konumu (smoothed_final_pos) hesaplandıktan sonra, bu konuma karşılık gelen ekran pikseline “screen.blit(rotated_car_image, car_rect)” komutu ile araç görselini yerleştirdim.
