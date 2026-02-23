# Veri Seti Stratejisi ve Dağılım Oranları

Bu doküman, modelin gerçek dünya koşullarında kararlı (robust) çalışabilmesi için kurgulanan veri mühendisliği stratejisini içerir.


## 1. Veri Kompozisyonu (Data Composition)
Bir derin öğrenme modelinin sadece laboratuvar ortamında değil, sahada da çalışabilmesi için veri setinde aşağıdaki dağılım hedeflenmiştir:

### A. Nominal (Temiz) Veri (%60 - %70)
* **Tanım:** Nesnenin net görüldüğü, iyi ışıklandırılmış, standart açılı görüntüler.
* **Amaç:** Modelin nesnenin temel özniteliklerini (şekil, renk, doku) öğrenmesini sağlar. Temel doğruluk (mAP) bu veriyle oluşturulur.

### B. "Hard-Positive" / Problemli Veri (%20 - %25)
* **Tanım:** Modelin tespit etmekte zorlanacağı, gürültülü veriler.
    * **Occlusion (Kapanma):** Nesnenin %10-%50'sinin başka bir nesne tarafından kapatılması.
    * **Blur (Bulanıklık):** Hareket bulanıklığı veya odak kaybı.
    * **Lighting (Aydınlatma):** Aşırı parlak (parlama) veya çok karanlık (gölge) ortamlar.
    * **Deformasyon:** Nesnenin ezilmiş, bükülmüş veya rengi solmuş halleri.
* **Amaç:** Modelin ezberlemesini (overfitting) engellemek ve zor koşullarda genelleme yapabilmesini sağlamak.
