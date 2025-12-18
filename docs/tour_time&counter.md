Bir yarış takip sisteminin en temel özelliklerinden biri, atılan turları doğru bir şekilde saymak ve tur sürelerini ölçmektir. Kodumda bu mantığı, coğrafi konum kontrolü ve zaman damgalarını kullanarak oluşturdum.
Sistemin temel çalışma prensibi, aracın önceden tanımlanmış bir "bitiş çizgisi"ne girip çıkmasını tespit etmektir.
1.	Bitiş Çizgisinin Tanımlanması: Kodun başında “FINISH_POINT” ile bitiş çizgisinin tam coğrafi koordinatlarını ve “FINISH_RADIUS_DEGREES” ile bu noktanın etrafında küçük bir dairesel algılama alanının yarıçapını tanımladım. Bu yarıçap, GPS'in küçük sapmalarına rağmen aracın bitiş çizgisinden geçtiğini güvenilir bir şekilde tespit etmek içindir.

2.	Mesafenin Hesaplanması: Ana döngünün her adımında, aracın o anki son konumu (final_pos) ile bitiş noktası (FINISH_POINT) arasındaki mesafe, haversine_distance fonksiyonu kullanılarak metre cinsinden hesaplanır.

3.	Bitiş Çizgisinden Geçiş Tespiti: Hesaplanan bu mesafe, tanımlanan yarıçaptan (FINISH_RADIUS_DEGREES)’den küçükse, aracın bitiş çizgisinden geçtiği kabul edilir.
