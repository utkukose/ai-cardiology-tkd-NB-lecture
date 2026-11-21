# Veri setleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](DATASETS.md)

Eğitimdeki her veri seti ya sentetiktir ya da açık veridir. 1. haftanın dosyaları [data](data) klasöründe yer alır; böylece Jupyter Notebook'lar üyelik gerektirmeden çalışır. Her veri seti kendi lisansını korur ve künyesi aşağıda verilmiştir.

## 1. haftanın veri setleri

| Veri seti | Depodaki dosyalar | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| UCI Heart Disease, Cleveland verisi [1, 2] | `data/uci-heart-disease/processed.cleveland.data`: 303 hasta, 14 değişken. Kaggle'da paylaşılan Heart Disease veri seti bu veriden alınmıştır | UCI Machine Learning Repository, [doi:10.24432/C52P4X](https://doi.org/10.24432/C52P4X); Creative Commons Atıf 4.0 Uluslararası (CC BY 4.0) | 1. hafta, 1. bölüm; 2. hafta, Python adımı 2 ve 1-4. bölümler; 9. hafta, Python adımı 9, 1-3. uygulama durakları, 1-4. ve 10. bölümler |
| MIT-BIH Aritmi Veri Tabanı, 100 numaralı kayıt [3, 4, 5] | `data/physionet/mitdb/100.hea`, `100.dat`, `100.atr`: atım etiketleriyle birlikte 360 Hz'de iki derivasyonun (MLII ve V5) 30 dakikası | PhysioNet, [doi:10.13026/C2F305](https://doi.org/10.13026/C2F305); Open Data Commons Attribution License v1.0 (ODC-By 1.0) | 1. hafta, 6. bölüm |
| PTB Tanısal EKG Veri Tabanı, 001 numaralı hasta, s0010_re kaydı [5, 6, 7] | `data/physionet/ptbdb/patient001/s0010_re.hea`, `.dat`, `.xyz`: 1.000 Hz'de 12 standart derivasyonun ve 3 Frank derivasyonunun 38,4 saniyesi | PhysioNet, [doi:10.13026/C28C71](https://doi.org/10.13026/C28C71); ODC-By 1.0 | 1. hafta, 8. bölüm |
| Örnek kaliper ölçümleri | `data/examples/example_caliper_measurements.csv`: sanal kliniğin beş hastasına ait 20 aralık ölçümü | Eğitim için oluşturulmuştur; CC BY 4.0 | 1. hafta, 5. bölüm |

PTB veri tabanındaki kayıt, başlık dosyasında belirtildiği gibi, akut inferolateral miyokard enfarktüsüyle yatırılan 81 yaşında bir kadın hastaya aittir. Dosyalar, PhysioNet'te ve UCI deposunda yayımlanan dosyaların değiştirilmemiş kopyalarıdır.

## Sanal klinik

`vclinic` ders paketi sanal kliniğin hastalarını çalışma anında oluşturur. `vclinic.make_cohort(500)` fonksiyonu 500 sentetik hastadan oluşan bir kayıt döndürür. Kayıtta her hastanın demografik verileri, risk faktörleri, laboratuvar değerleri, ejeksiyon fraksiyonu, ana tanısı ve elektrokardiyogram (EKG) parametreleri bulunur. `vclinic.patient_ecg` bir hastanın 12 derivasyonlu EKG'sini aralıklarının ve atım zamanlarının gerçek değerleriyle birlikte döndürür. Aynı seed değeri her zaman aynı hastaları verir; böylece her katılımcı aynı kliniği görür. Değişkenler arasındaki ilişkiler genel klinik örüntüleri izler ve etki büyüklükleri `vclinic.TRUE_EFFECTS` içinde belgelenmiştir. 2. haftadan itibaren `vclinic.add_followup` fonksiyonu kayda ekokardiyografik değişkenleri, kalp yetersizliği fenogrubunu ve en fazla beş yıllık izlem verisini ekler; izlemde olay, ölüm ya da kalp yetersizliği nedeniyle hastaneye yatıştır. Veriler öğretim malzemesidir ve klinik kullanım için değildir. 3. haftadan itibaren paket, aşağıda anlatılan `vclinic.acdc` ve `vclinic.echonet` modülleriyle açık arşivlerden gerçek görüntüler de okur.

## 3. haftanın veri setleri

3. haftanın hiçbir dosyası depoda saklanmaz. Her katılımcı görüntüleri kaynağından edinir ve kullanım koşullarını kabul eder; ders paketi de görüntüleri kaydedildikleri yerden okur.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| ACDC, Automated Cardiac Diagnosis Challenge [8]: Dijon Üniversite Hastanesinde beş grupta toplanmış 150 sine kardiyak manyetik rezonans (KMR) incelemesi. İncelemeler, diyastol sonu ve sistol sonunda sol ventrikül kavitesinin, miyokardın ve sağ ventrikül kavitesinin uzman konturlarıyla birlikte gelir. Eğitimde normal (NOR), dilate kardiyomiyopati (DCM) ve hipertrofik kardiyomiyopati (HCM) gruplarındaki 90 inceleme kullanılır. | `vclinic.acdc.download()`, üç grubun yaklaşık 105 MB'lık dosyalarını Human Heart Project'in açık veri tabanından ders klasöründeki `data/acdc` klasörüne kaydeder. İndirme Google Colab'da da Jupyter'de de aynı biçimde çalışır ve üyelik gerektirmez. | [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/), Lyon Üniversitesi (CREATIS) ve Dijon Üniversite Hastanesi; Creative Commons Atıf-GayriTicari-AynıLisanslaPaylaş 4.0 (CC BY-NC-SA 4.0), ticari olmayan bilimsel araştırma için. Eğitimde bu görüntüleri gösteren şekiller "ACDC, CC BY-NC-SA 4.0" kaynak bilgisini taşır ve aynı lisansa tabidir. | 3. hafta, Python adımı 3, 1. ve 2. uygulama durakları ve 1-9. bölümler |
| EchoNet-Dynamic [9]: Stanford Üniversitesi Tıp Merkezine ait, 112 × 112 piksellik 10.030 apikal dört boşluk ekokardiyografi videosu. Videolarla birlikte ejeksiyon fraksiyonu, hacimler ve diyastol sonu ile sistol sonunda sol ventrikülün uzman çizimleri de verilir. | Her katılımcı [Stanford AIMI](https://aimi.stanford.edu/datasets/echonet-dynamic-cardiac-ultrasound) sitesine kişisel olarak kaydolur ve kişisel bir indirme bağlantısı alır. `vclinic.echonet`, `data/echonet` içindeki zip dosyasını ya da açılmış klasörü okur. Eğitim dosyaları da bağlantıyı da paylaşmaz. | Stanford University School of Medicine EchoNet-Dynamic Dataset Research Use Agreement: Kişisel ve ticari olmayan araştırma kullanımına izin verir; her kullanıcı ayrı ayrı kaydolur. Veri seti [doi:10.71718/yqp5-y078](https://doi.org/10.71718/yqp5-y078) | 3. hafta, 3. uygulama durağı ve 10. bölüm; kaydı olan katılımcılar için |

## 4. haftanın veri setleri

4. haftanın dosyaları da depoda saklanmaz. Her katılımcı görüntüleri ve ağırlıkları kaynağından indirir; ders paketi de bunları kaydedildikleri yerden okur.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| CAMUS, Cardiac Acquisitions for Multi-structure Ultrasound Segmentation [10]: Saint-Étienne Üniversite Hastanesinde GE Vivid E95 cihazıyla kaydedilmiş, 500 hastanın apikal iki boşluk ve dört boşluk ekokardiyogramları. Her görüntü, diyastol sonu ve sistol sonunda sol ventrikül kavitesinin, miyokardın ve sol atriyumun uzman sınırlarıyla, görüntü kalitesiyle ve ejeksiyon fraksiyonuyla birlikte gelir. Eğitimde 300 hasta kullanılır: Eğitim kümesinden 200 hasta, doğrulama ve test kümelerinin her birinden ise 50 hasta. | `vclinic.camus.download()`, 300 hastanın diyastol sonu ve sistol sonu karelerini sınırları ve bilgi dosyalarıyla birlikte, yaklaşık 227 MB'lık bir indirmeyle Human Heart Project'in açık veri tabanından ders klasöründeki `data/camus` klasörüne kaydeder. İndirme Google Colab'da da Jupyter'de de aynı biçimde çalışır ve üyelik gerektirmez. | [CAMUS](https://www.creatis.insa-lyon.fr/Challenge/camus/), Lyon Üniversitesi (CREATIS) ve Saint-Étienne Üniversite Hastanesi; Creative Commons Atıf-GayriTicari-AynıLisanslaPaylaş 4.0 (CC BY-NC-SA 4.0), ticari olmayan bilimsel araştırma için ve her kullanımda CAMUS makalesine atıf yapılması koşuluyla. Eğitimde bu görüntüleri gösteren şekiller "CAMUS, CC BY-NC-SA 4.0" kaynak bilgisini taşır ve aynı lisansa tabidir. | 4. hafta, Python adımı 4, 2. ve 3. uygulama durakları ve 5-10. bölümler; 7. hafta, 1. uygulama durağı ve 4. bölüm; 9. hafta, 2. uygulama durağı, 5-7. bölümler ve haftalık proje |
| EfficientNet-B0'ın ImageNet ağırlıkları [11, 12]: ImageNet yarışmasının 1.000 sınıfıyla eğitilmiş ağın yaklaşık 21 MB'lık ağırlıkları | Jupyter Notebook'un 0. bölümü ağırlıkları torchvision aracılığıyla bir kez indirir ve bilgisayardaki PyTorch önbelleğine kaydeder. | [torchvision](https://pytorch.org/vision/stable/models/efficientnet.html) ile dağıtılır; torchvision'ın kodu BSD 3-Clause lisansına tabidir. Ağırlıklar, kullanım koşulları ticari olmayan araştırma ve eğitime izin veren ImageNet verisiyle eğitilmiştir; eğitim bu ağırlıkları yalnızca öğretim amacıyla kullanır. | 4. hafta, Python adımı 4, 1. uygulama durağı ve 1-4. bölümler; 7. hafta, 1. uygulama durağı ve 4. bölüm |

## 5. haftanın veri setleri

PTB-XL'in hiçbir kaydı depoda saklanmaz. Her katılımcı kayıtları PhysioNet'ten indirir; ders paketi de kayıtları kaydedildikleri yerden okur.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| PTB-XL [13, 14]: 18.869 hastadan alınmış 10 saniyelik 21.799 klinik 12 derivasyonlu EKG. Kayıtlar 1989 ile 1996 arasında Schiller AG cihazlarıyla alınmış, en fazla iki kardiyolog tarafından SCP-ECG standardının 71 ifadesiyle tanımlanmış ve hastaya göre on kata bölünmüştür. Eğitimde 1. ve 2. katların (eğitim), 9. katın (doğrulama) ve 10. katın (test) 100 Hz'lik kayıtları, yani 7.573 hastanın 8.737 kaydı kullanılır. | `vclinic.ptbxl.download()`, iki tabloyu ve 8.737 kaydı yaklaşık 216 MB'lık bir indirmeyle PhysioNet'ten ders klasöründeki `data/ptbxl` klasörüne kaydeder. İndirme Google Colab'da da Jupyter'de de aynı biçimde çalışır ve üyelik gerektirmez. | [PTB-XL 1.0.3](https://doi.org/10.13026/kfzx-aw45), Physikalisch-Technische Bundesanstalt, PhysioNet üzerinde; Creative Commons Atıf 4.0 Uluslararası (CC BY 4.0), her kullanımda makaleye ve veri setine atıf yapılması koşuluyla. Eğitimde bu kayıtları gösteren şekiller "PTB-XL, CC BY 4.0" kaynak bilgisini taşır. | 5. hafta, 1. ve 2. uygulama durakları, 1-8. bölümler ve haftalık proje |
| Sanal kliniğin VC-0128 numaralı hastasına ait sentetik 24 saatlik Holter kaydı: Üç paroksismal AF atağı, atriyal erken vuruların sık görüldüğü bir saat ve iki elektrot gürültüsü dönemi; gerçek durum atım atım bilinir. | `vclinic.holter.recording()` kaydı birkaç saniyede üretir; hiçbir şey indirilmez. | Sentetiktir, ders paketinin bir parçasıdır (MIT Lisansı). | 5. hafta, 3. uygulama durağı ve 9. bölüm |

## 6. haftanın veri setleri

6. haftanın hiçbir verisi depoda saklanmaz. Rapor arşivini ders paketi katılımcının bilgisayarında üretir; önceden eğitilmiş modelin tokenizer'ı ve ağırlıkları ise Hugging Face Hub'dan gelir.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| Sanal kliniğin rapor arşivi: 3.600 sentetik hastanın her biri için bir epikriz (A hastanesinin tam cümlelerle Türkçe ve İngilizce yazdığı 3.000, B hastanesinin kısa bir üslupla yazdığı 600 epikriz), açıklanmış tanılar, ilaçlar ve işlemler ile her tanının durumu; ayrıca arterleri, segmentleri ve darlıklarıyla 2.311 sentetik koroner anjiyografi raporu | `vclinic.reports.archive()` ve `vclinic.reports.angiography_archive()` bunları birkaç saniyede üretir; hiçbir şey indirilmez. | Sentetiktir, ders paketinin bir parçasıdır (MIT Lisansı). | 6. hafta, bütün bölümler ve uygulama durakları |
| Küçük Türkçe BERT modeli `ytu-ce-cosmos/turkish-tiny-bert-uncased` [15]: 2 katman, token başına 128 sayı, 32.000 parçalık bir sözlük ve yaklaşık 4,6 milyon parametre; 75 GB'tan fazla Türkçe metinle önceden eğitilmiştir. | Jupyter Notebook'un 0. bölümü ve Python adımı 6, tokenizer'ı ve ağırlıkları (yaklaşık 19 MB) transformers aracılığıyla bilgisayardaki Hugging Face önbelleğine bir kez indirir. | Yıldız Teknik Üniversitesi Cosmos Araştırma Laboratuvarı, [Hugging Face Hub](https://huggingface.co/ytu-ce-cosmos/turkish-tiny-bert-uncased) üzerinde; MIT Lisansı. | 6. hafta, 6-8. bölümler ve 2. uygulama durağı |

## 7. haftanın veri setleri

7. haftanın hiçbir verisi depoda saklanmaz. Sanal kliniğin anjiyogramlarını ders paketi katılımcının bilgisayarında çizer; ARCADE Zenodo'dan indirilir, ViT-B/16'nın ağırlıkları ise torchvision aracılığıyla gelir. CAMUS ekokardiyogramları ve EfficientNet-B0'ın ağırlıkları 4. haftadakilerle aynıdır.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| Sanal kliniğin sentetik koroner anjiyogramları: Anjiyografisi olan 2.311 hastanın her biri için 6. haftanın kayıt sistemindeki lezyonlardan çizilen, sol koroner arterin ve sağ koroner arterin birer görüntüsü (512 × 512 piksel); her darlığın yeri, derecesi ve kutusu ile birlikte | `vclinic.angiogram.patient_frames()` bir hastanın iki görüntüsünü çizer, `vclinic.angiogram.patches()` bir kümenin yamalarını keser; hiçbir şey indirilmez. | Sentetiktir, ders paketinin bir parçasıdır (MIT Lisansı). | 7. hafta, Python adımı 7, 1., 2. ve 5. bölümler, 2. uygulama durağı |
| ARCADE, Automatic Region-based Coronary Artery Disease diagnostics using X-ray angiography imagEs [16]: Darlık kümesi; uzmanların darlık oluşturan plakların sınırlarını çizdiği, 512 × 512 piksellik 1.500 X ışınlı koroner anjiyogram. Görüntülerin 1.000 tanesi eğitim, 200 tanesi doğrulama, 300 tanesi test için ayrılmıştır. | `vclinic.arcade.download()` arşivi (yaklaşık 452 MB) Zenodo'dan bir kez indirir, MD5 sağlama toplamını denetler ve darlık kümesini ders klasöründeki `data/arcade` klasöründe tutar. | [Zenodo'daki ARCADE](https://doi.org/10.5281/zenodo.10390295); Creative Commons CC0 1.0. Eğitimin bu görüntüleri gösteren şekilleri "ARCADE, Popov ve ark. 2024, CC0" notunu taşır. | 7. hafta, 6-10. bölümler, 2. ve 3. uygulama durakları ve haftalık proje |
| ViT-B/16'nın ImageNet ağırlıkları [12, 17]: torchvision'ın ImageNet yarışmasının 1.000 sınıfıyla eğittiği Vision Transformer'ın ağırlıkları; 86,6 milyon parametre, yaklaşık 330 MB | Jupyter Notebook'un 0. bölümü ağırlıkları torchvision aracılığıyla bilgisayardaki PyTorch önbelleğine bir kez indirir. | Kodu BSD 3-Clause Lisansı altında olan [torchvision](https://pytorch.org/vision/stable/models/vision_transformer.html) ile dağıtılır. Ağırlıklar, koşulları ticari olmayan araştırmaya ve eğitime izin veren ImageNet ile eğitilmiştir; eğitim bu ağırlıkları yalnızca öğretim için kullanır. | 7. hafta, 3., 4. ve 8. bölümler ve 1. uygulama durağı |

## 8. haftanın veri setleri

8. haftanın hiçbir verisi depoda saklanmaz. Sanal kliniğin hasta kaydını ve göğüs ağrısı ünitesini ders paketi katılımcının bilgisayarında oluşturur; hiçbir şey indirilmez.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| Sanal kliniğin izlem verilerini içeren hasta kaydı: 2. haftadaki gibi oluşturulan 3.600 sentetik hasta. 24 ay içinde kalp yetersizliği olayı görülen ya da en az 24 ay izlenen 3.227 hasta; EKG ölçümleri, altı ekokardiyografik değişken ve üç laboratuvar değeriyle mini projeye girer | `vclinic.followup.add_followup(vclinic.cohort.make_cohort(3600))` kaydı birkaç saniyede oluşturur; hiçbir şey indirilmez. | Sentetiktir, ders paketinin bir parçasıdır (MIT Lisansı). | 8. hafta, 1-3. bölümler ve 1. uygulama durağı |
| Sanal kliniğin göğüs ağrısı ünitesi: A hastanesinde göğüs ağrısıyla yapılmış 4.000, B hastanesinde 1.000 sentetik başvuru. Her başvuruda bir klinik tablo, Türkçe ve İngilizce bir triyaj notu, 10 saniyelik 12 derivasyonlu bir EKG, gelişte ve bir saat sonra yüksek duyarlıklı troponin, hastaların yaklaşık yarısında yatak başı ekokardiyogram, HEART skoru ve 30 gün içindeki majör olumsuz kardiyak olaylar bulunur. B hastanesinin hastaları daha yaşlı ve daha hastadır, troponin I testinin üst referans sınırı farklıdır ve notları daha kısadır | `vclinic.triage.presentations("A")` ve `vclinic.triage.presentations("B")` tabloları birkaç saniyede yazar, `vclinic.triage.ecg_array()` ise EKG'leri çizer; hiçbir şey indirilmez. | Sentetiktir, ders paketinin bir parçasıdır (MIT Lisansı). | 8. hafta, Python adımı 8, 4-10. bölümler, 2. ve 3. uygulama durakları ve haftalık proje |

## 9. haftanın veri setleri

9. hafta depoya yeni bir veri eklemez. Hafta, yukarıda anlatılan üç veri setine geri döner.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| UCI Heart Disease, Cleveland verisi [1, 2]: Koroner anjiyografiye gönderilmiş 303 hasta; 2. haftadaki ayırmayla 227 eğitim ve 76 test hastası | 1. haftadaki gibi depoda | UCI Machine Learning Repository; CC BY 4.0 | 9. hafta, Python adımı 9, 1-3. uygulama durakları, 1-4. ve 10. bölümler |
| CAMUS [10]: 4. haftanın 300 hastası; uzman sınırları ve ejeksiyon fraksiyonuyla birlikte 600 apikal iki boşluk ve dört boşluk görüntüsü | Jupyter Notebook'un 0. bölümü yaklaşık 250 MB tutan bu verileri yalnızca bilgisayarda bulunmadıklarında yeniden indirir | 4. haftadaki gibi CC BY-NC-SA 4.0; şekiller "CAMUS, CC BY-NC-SA 4.0" kaynak bilgisini taşır | 9. hafta, 2. uygulama durağı, 5-7. bölümler ve haftalık proje |
| Sanal kliniğin göğüs ağrısı ünitesi: 8. haftadaki gibi A hastanesinde göğüs ağrısıyla yapılmış 4.000, B hastanesinde 1.000 sentetik başvuru | `vclinic.triage` bunları bilgisayarda oluşturur; hiçbir şey indirilmez | Ders paketinin sentetik verisi (MIT Lisansı) | 9. hafta, 3. uygulama durağı ve 8-10. bölümler |

## 10. haftanın veri setleri

10. hafta depoda hiçbir kayıt saklamaz. Her katılımcı MIT-BIH Atriyal Fibrilasyon Veri Tabanı'nın dosyalarını PhysioNet'ten indirir; sanal kliniğin telemetri servisini ise ders paketi bilgisayarda oluşturur.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| MIT-BIH Atriyal Fibrilasyon Veri Tabanı (AFDB) [18, 19]: Çoğu paroksismal AF'li kişilerden Boston'daki Beth Israel Hastanesi'nde kaydedilmiş, yaklaşık 10 saatlik 25 Holter kaydı. Her kayıtta saniyede 250 örnekle alınmış iki EKG sinyali, elle hazırlanmış ritim işaretlemeleri ve otomatik bir bulucunun vuru işaretlemeleri vardır; 00735 ve 03665 kayıtlarında sinyal bulunmaz. Kayıtlar kişi düzeyinde ayrılır: 15 kayıt eğitim, 5 kayıt doğrulama ve kullanıcı testi, 5 kayıt da test için kullanılır. Bir dakikalık pencerelere bölünen kayıtlar 14.883 pencere verir | `vclinic.afdb.download()`, 25 kaydın 75 başlık ve işaretleme dosyasını ve 04936, 06426 ve 08219 kayıtlarının sinyal dosyalarını, yaklaşık 86 MB'lık bir indirmeyle PhysioNet'ten ders klasöründeki `data/afdb` klasörüne kaydeder ve her dosyayı PhysioNet'in yayımladığı SHA-256 değerleriyle denetler; üyelik gerekmez. | PhysioNet üzerinde [MIT-BIH AFDB 1.0.0](https://doi.org/10.13026/C2MW2D); Open Data Commons Atıf Lisansı v1.0 (ODC-By 1.0), her kullanımda makaleye ve veri tabanına atıf yapılması koşuluyla. Eğitimde bu kayıtları gösteren şekiller "MIT-BIH AFDB, PhysioNet, ODC-By 1.0" kaynak bilgisini taşır. | 10. hafta, 1-6. ve 10. bölümler, 1-3. uygulama durakları ve haftalık proje |
| Sanal kliniğin telemetri servisi: Dört sentetik hastanın 24 saatlik kayıtları: VC-0128 (paroksismal AF, atriyal erken vurular ve iki elektrot gürültüsü dönemi), VC-0347 (sık atriyal erken vurulu sinüs ritmi), VC-0519 (kalıcı AF) ve VC-0733 (uzun elektrot gürültüsü dönemleri olan sinüs ritmi). Her kayıt bir monitörün bulacağı vuru zamanlarını ve istenen herhangi bir on saniyenin DII EKG'sini içerir | `vclinic.holter.ward()` kayıtları birkaç saniyede oluşturur; hiçbir şey indirilmez. | Sentetiktir, ders paketinin bir parçasıdır (MIT Lisansı). | 10. hafta, 7-9. bölümler, 2. ve 3. uygulama durakları ve etkileşimli lab |

## 11. haftanın veri setleri

11. hafta depoya yeni bir veri eklemez. Haftanın çözümlü final projesi Cleveland verisine döner; katılımcıların final projelerinin verileri ise hiçbir zaman depoya girmez.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| UCI Heart Disease, Cleveland verisi [1, 2]: Bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş 303 hasta; 2. haftadaki ayırmayla 227 eğitim ve 76 test hastası | 1. haftadaki gibi depoda | UCI Machine Learning Repository; CC BY 4.0 | 11. hafta, Python adımı 11, 1-3. uygulama durakları, 1-10. bölümler ve final projesinin araç takımı |

## Final projelerinin veri setleri

Final projeleri başka açık veri setlerini de kullanabilir; örneğin A seçeneği için PhysioNet/Computing in Cardiology Challenge 2020 verileri ya da C seçeneği için ekokardiyografi ve kardiyak manyetik rezonans alanlarındaki açık veri setleri. Bu veriler depoda yer almaz: Her katılımcı onları kaynağından indirir ve lisanslarına uyar. EchoNet-Dynamic gibi kişisel kayıt gerektiren bir veri setinde kayıt katılımcının kendisine aittir. Kişinin kendi kurumunun verileri (G seçeneği) yalnızca kurumun bir bilgisayarında, kurumun izniyle ve bir çalışma söz konusuysa etik kurul onayıyla analiz edilir.

## Kaynaklar

1. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). *Heart Disease* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X
2. Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J.-J., Sandhu, S., Guppy, K. H., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. *The American Journal of Cardiology, 64*(5), 304–310. https://doi.org/10.1016/0002-9149(89)90524-9
3. Moody, G. B., & Mark, R. G. (2005). *MIT-BIH Arrhythmia Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C2F305
4. Moody, G. B., & Mark, R. G. (2001). The impact of the MIT-BIH Arrhythmia Database. *IEEE Engineering in Medicine and Biology Magazine, 20*(3), 45–50. https://doi.org/10.1109/51.932724
5. Goldberger, A. L., Amaral, L. A. N., Glass, L., Hausdorff, J. M., Ivanov, P. Ch., Mark, R. G., Mietus, J. E., Moody, G. B., Peng, C.-K., & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. *Circulation, 101*(23), e215–e220. https://doi.org/10.1161/01.CIR.101.23.e215
6. Bousseljot, R., Kreiseler, D., & Schnabel, A. (2004). *The PTB Diagnostic ECG Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C28C71
7. Bousseljot, R., Kreiseler, D., & Schnabel, A. (1995). Nutzung der EKG-Signaldatenbank CARDIODAT der PTB über das Internet. *Biomedizinische Technik / Biomedical Engineering, 40*(s1), 317–318. https://doi.org/10.1515/bmte.1995.40.s1.317
8. Bernard, O., Lalande, A., Zotti, C., Cervenansky, F., Yang, X., Heng, P.-A., Cetin, I., Lekadir, K., Camara, O., Gonzalez Ballester, M. A., Sanroma, G., Napel, S., Petersen, S., Tziritas, G., Grinias, E., Khened, M., Kollerathu, V. A., Krishnamurthi, G., Rohe, M.-M., Pennec, X., Sermesant, M., Isensee, F., Jager, P., Maier-Hein, K. H., Full, P. M., Wolf, I., Engelhardt, S., Baumgartner, C. F., Koch, L. M., Wolterink, J. M., Isgum, I., Jang, Y., Hong, Y., Patravali, J., Jain, S., Humbert, O., & Jodoin, P.-M. (2018). Deep learning techniques for automatic MRI cardiac multi-structures segmentation and diagnosis: Is the problem solved? *IEEE Transactions on Medical Imaging, 37*(11), 2514–2525. https://doi.org/10.1109/TMI.2018.2837502
9. Ouyang, D., He, B., Ghorbani, A., Yuan, N., Ebinger, J., Langlotz, C. P., Heidenreich, P. A., Harrington, R. A., Liang, D. H., Ashley, E. A., & Zou, J. Y. (2020). Video-based AI for beat-to-beat assessment of cardiac function. *Nature, 580*(7802), 252–256. https://doi.org/10.1038/s41586-020-2145-8
10. Leclerc, S., Smistad, E., Pedrosa, J., Østvik, A., Cervenansky, F., Espinosa, F., Espeland, T., Berg, E. A. R., Jodoin, P.-M., Grenier, T., Lartizien, C., D'hooge, J., Lovstakken, L., & Bernard, O. (2019). Deep learning for segmentation using an open large-scale dataset in 2D echocardiography. *IEEE Transactions on Medical Imaging, 38*(9), 2198–2210. https://doi.org/10.1109/TMI.2019.2900516
11. Tan, M., & Le, Q. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. In *Proceedings of the 36th International Conference on Machine Learning, PMLR 97* (pp. 6105–6114). https://proceedings.mlr.press/v97/tan19a.html
12. Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z., Karpathy, A., Khosla, A., Bernstein, M., Berg, A. C., & Fei-Fei, L. (2015). ImageNet large scale visual recognition challenge. *International Journal of Computer Vision, 115*(3), 211–252. https://doi.org/10.1007/s11263-015-0816-y
13. Wagner, P., Strodthoff, N., Bousseljot, R.-D., Kreiseler, D., Lunze, F. I., Samek, W., & Schaeffter, T. (2020). PTB-XL, a large publicly available electrocardiography dataset. *Scientific Data, 7*(1), Article 154. https://doi.org/10.1038/s41597-020-0495-6
14. Wagner, P., Strodthoff, N., Bousseljot, R., Samek, W., & Schaeffter, T. (2022). *PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3)* [Data set]. PhysioNet. https://doi.org/10.13026/kfzx-aw45
15. Kesgin, H. T., Yüce, M. K., & Amasyali, M. F. (2023). *Developing and evaluating tiny to medium-sized Turkish BERT models* (arXiv:2307.14134). arXiv. https://doi.org/10.48550/arXiv.2307.14134
16. Popov, M., Amanturdieva, A., Zhaksylyk, N., Alkanov, A., Saniyazbekov, A., Aimyshev, T., Ismailov, E., Bulegenov, A., Kuzhukeyev, A., Kulanbayeva, A., Kalzhanov, A., Temenov, N., Kolesnikov, A., Sakhov, O., & Fazli, S. (2024). Dataset for automatic region-based coronary artery disease diagnostics using X-ray angiography images. *Scientific Data, 11*, Article 20. https://doi.org/10.1038/s41597-023-02871-z
17. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. In *9th International Conference on Learning Representations (ICLR 2021)*. https://openreview.net/forum?id=YicbFdNTTy
18. Moody, G. B., & Mark, R. G. (1983). A new method for detecting atrial fibrillation using R-R intervals. *Computers in Cardiology, 10*, 227–230. https://physionet.org/content/afdb/1.0.0/
19. Moody, G. B., & Mark, R. G. (1992). *MIT-BIH Atrial Fibrillation Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C2MW2D

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
