Sistemin aracı doğru bir şekilde pist üzerinde gösterebilmesi için öncelikle pistin geometrisini bilmesi gerekir.
Bu bilgiyi sisteme tanıtmak için “Google Maps” gibi platformlarda “My maps” üzerinden kolayca oluşturulabilen
ve coğrafi verileri saklamak için standartlaşmış bir format olan KML (Keyhole Markup Language) dosyası kullanacağım.

KML Dosyası: KML, XML tabanlı bir dosya formatıdır ve coğrafi verileri ve bunlarla ilişkili özellikleri tanımlamak için kullanılır.
Benim projemde KML dosyası, yarış pistinin ideal sürüş çizgisini temsil eden bir dizi coğrafi koordinatı
(enlem, boylam) barındıran bir <LineString> etiketi içerecektir.

KML Dosyasının Okunması ve İşlenmesi: KML dosyasını okuyup içindeki koordinatları ayıklamakla görevlidir.

Bu fonksiyonun çalışma adımları şöyledir:
1.	Dosyayı Ayrıştırma: xml.etree.ElementTree.parse(file_path) komutu ile KML dosyasını bir XML ağaç yapısı olarak belleğe yükledim.
2.	Namespace Tanımlama: KML dosyaları genellikle bir "namespace" (isim alanı) kullanır. Kodda {'kml': 'http://www.opengis.net/kml/2.2'} şeklinde 
    tanımlanan bu namespace, XML etiketlerini doğru bir şekilde bulabilmem için gerekli.
3.	Koordinatları Bulma: root.findall(".//kml:LineString", namespace) komutu ile dosya içindeki tüm <LineString> etiketlerini bulur. 
    Ardından her bir LineString içindeki <coordinates> etiketine ulaşır.
4.	Metni İşleme: <coordinates> etiketinin içindeki metin, "boylam,enlem,irtifa" formatında ve boşluklarla ayrılmış bir listesidir. 
    Bu metni split() ile satırlara, ardından her satırı da virgüllerden ayırarak (enlem, boylam) demetleri (tuple) haline getiriyorum. 
    Bu veriyi daha sonra kullanmak üzere points adlı bir listeye ekliyorum.
