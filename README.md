🚗 ADAS (Advanced Driver Assistance Systems) Development:

📖 Proje Hakkında (About)

Bu repo, **Pamukkale Üniversitesi ATAY Takımı** bünyesinde geliştirilen otonom ve elektrikli araçlar için **İleri Sürüş Destek Sistemleri (ADAS)** algoritmalarını ve kaynak kodlarını içermektedir.

Geliştirilen modüller, **Teknofest Robotaksi Binek Otonom Araç** ve **Elektrikli Araç** yarışmalarının parkur ve güvenlik standartlarına uygun olarak tasarlanmıştır. Proje; gerçek zamanlı görüntü işleme, derin öğrenme tabanlı nesne tespiti ve otonom karar verme mekanizmalarına odaklanmaktadır.

Temel hedef, aracın çevresel farkındalığını (perception) artırarak karmaşık trafik senaryolarında güvenli ve stabil bir sürüş sağlamaktır.

🚀 Modüller ve Özellikler (Modules)

Bu repo şu an için aşağıdaki temel otonom sürüş ADAS fonksiyonları bileşenlerini barındırmaktadır ve geliştirilmeye devam edilmektedir:

🚦 1. Trafik Işıkları Tanıma (Traffic Light Recognition)

Otonom aracın kavşaklarda ışık durumunu analiz ederek (Kırmızı, Sarı, Yeşil) durma veya geçme kararı vermesini sağlayan modüldür.
**Teknik Yaklaşım:** Renk uzayı analizi (HSV) ve morfolojik işlemler ile ışık tespiti.

**Kabiliyet:**
    * Gerçek zamanlı durum sınıflandırma.
    * Farklı ışık koşullarına (gölge/parlama) adaptasyon.
    * Araç kontrolcüsüne "Dur/Geç" ses sinyali üretimi.

🏁 2. Yarış Navigasyonu (Race Navigation)
Aracın yarış parkurunu çizerek en optimum rotada kalmasını sağlayan navigasyon sistemidir.

🛠️ Teknoloji Yığını (Tech Stack)

Proje geliştirme sürecinde aşağıdaki teknolojiler kullanılmaktadır:

| **Programlama Dili** | Python 3.x |

| **Görüntü İşleme** | OpenCV, NumPy |

| **Derin Öğrenme** | PyTorch, Ultralytics YOLO |

| **Donanım** | Raspberry Pi 5, Kamera Modülleri |

| **Veri Analizi** | Pandas, Matplotlib |

📅 Gelecek Planları (Roadmap)

Proje, otonom sürüşün diğer katmanlarını da kapsayacak şekilde genişletilmektedir:

-Yarış Navigasyonu: Görüntü işleme tabanlı şerit tespiti ve rota planlama algoritmaları ile desteklenmesi.

-Trafik Levhası Tanıma: Derin öğrenme (YOLO) ile trafik işaretlerinin tespiti ve sınıflandırılması.

-Hasarlı Levha Analizi: Zorlu koşullarda (yıpranmış, kapanmış) levha tespiti için özelleşmiş modeller.

-Nesne Tespiti: Yaya ve engel algılama sistemlerinin entegrasyonu.

-Sensör Füzyonu: Kamera verilerinin diğer sensörlerle birleştirilmesi.
