# Veri Seti Stratejisi ve Dağılım Oranları

Bu doküman, modelin gerçek dünya koşullarında kararlı (robust) çalışabilmesi için kurgulanan veri mühendisliği stratejisini içerir.


## 1. Veri Kompozisyonu (Data Composition)
Bir derin öğrenme modelinin sadece laboratuvar ortamında değil, sahada da çalışabilmesi için veri setinde aşağıdaki dağılım hedeflenmiştir:

### A. Nominal (Temiz) Veri (%60 - %70)
* **Tanım:** Nesnenin net görüldüğü, iyi ışıklandırılmış, standart açılı görüntüler.
* **Amaç:** Modelin nesnenin temel özniteliklerini (şekil, renk, doku) öğrenmesini sağlar. Temel doğruluk (mAP) bu veriyle oluşturulur.
