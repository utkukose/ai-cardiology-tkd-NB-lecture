# Veri setleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](DATASETS.md)

Eğitimdeki her veri seti ya sentetiktir ya da açık veridir. 1. haftanın dosyaları [data](data) klasöründe yer alır; böylece Jupyter defterleri üyelik gerektirmeden çalışır. Her veri seti kendi lisansını korur ve künyesi aşağıda verilmiştir.

## 1. haftanın veri setleri

| Veri seti | Depodaki dosyalar | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| UCI Heart Disease, Cleveland verisi [1, 2] | `data/uci-heart-disease/processed.cleveland.data`: 303 hasta, 14 değişken | UCI Machine Learning Repository, [doi:10.24432/C52P4X](https://doi.org/10.24432/C52P4X); Creative Commons Atıf 4.0 Uluslararası (CC BY 4.0) | 1. hafta, 1. bölüm; 2. hafta, Python adımı 2 ve 1-4. bölümler |
| MIT-BIH Aritmi Veri Tabanı, 100 numaralı kayıt [3, 4, 5] | `data/physionet/mitdb/100.hea`, `100.dat`, `100.atr`: atım etiketleriyle birlikte 360 Hz'de iki derivasyonun (MLII ve V5) 30 dakikası | PhysioNet, [doi:10.13026/C2F305](https://doi.org/10.13026/C2F305); Open Data Commons Attribution License v1.0 (ODC-By 1.0) | 1. hafta, 6. bölüm |
| PTB Tanısal EKG Veri Tabanı, 001 numaralı hasta, s0010_re kaydı [5, 6, 7] | `data/physionet/ptbdb/patient001/s0010_re.hea`, `.dat`, `.xyz`: 1.000 Hz'de 12 standart derivasyonun ve 3 Frank derivasyonunun 38,4 saniyesi | PhysioNet, [doi:10.13026/C28C71](https://doi.org/10.13026/C28C71); ODC-By 1.0 | 1. hafta, 8. bölüm |
| Örnek kumpas ölçümleri | `data/examples/example_caliper_measurements.csv`: sanal kliniğin beş hastasına ait 20 aralık ölçümü | Eğitim için oluşturulmuştur; CC BY 4.0 | 1. hafta, 5. bölüm |

PTB veri tabanındaki kayıt, başlık dosyasında belirtildiği gibi, akut inferolateral miyokard enfarktüsüyle yatırılan 81 yaşında bir kadın hastaya aittir. Dosyalar, PhysioNet'te ve UCI deposunda yayımlanan dosyaların değiştirilmemiş kopyalarıdır.

## Sanal klinik

`vclinic` ders paketi sanal kliniğin hastalarını çalışma anında oluşturur. `vclinic.make_cohort(500)` fonksiyonu 500 sentetik hastadan oluşan bir kayıt döndürür. Kayıtta her hastanın demografik verileri, risk faktörleri, laboratuvar değerleri, ejeksiyon fraksiyonu, ana tanısı ve elektrokardiyogram (EKG) parametreleri bulunur. `vclinic.patient_ecg` bir hastanın 12 derivasyonlu EKG'sini aralıklarının ve atım zamanlarının gerçek değerleriyle birlikte döndürür. Aynı tohum değeri her zaman aynı hastaları verir; böylece her katılımcı aynı kliniği görür. Değişkenler arasındaki ilişkiler genel klinik örüntüleri izler ve etki büyüklükleri `vclinic.TRUE_EFFECTS` içinde belgelenmiştir. 2. haftadan itibaren `vclinic.add_followup` fonksiyonu kayda ekokardiyografik değişkenleri, kalp yetersizliği fenogrubunu ve en fazla beş yıllık izlem verisini ekler; izlemde olay, ölüm ya da kalp yetersizliği nedeniyle hastaneye yatıştır. Veriler öğretim malzemesidir ve klinik kullanım için değildir. 3. haftadan itibaren paket, aşağıda anlatılan `vclinic.acdc` ve `vclinic.echonet` modülleriyle açık arşivlerden gerçek görüntüler de okur.

## 3. haftanın veri setleri

3. haftanın hiçbir dosyası depoda saklanmaz. Her katılımcı görüntüleri kaynağından edinir ve kullanım koşullarını kabul eder; ders paketi de görüntüleri kaydedildikleri yerden okur.

| Veri seti | Erişim | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| ACDC, Automated Cardiac Diagnosis Challenge [8]: Dijon Üniversite Hastanesinde beş grupta toplanmış 150 sine kardiyak manyetik rezonans (KMR) incelemesi. İncelemeler, diyastol sonu ve sistol sonunda sol ventrikül boşluğunun, miyokardın ve sağ ventrikül boşluğunun uzman konturlarıyla birlikte gelir. Eğitimde normal (NOR), dilate kardiyomiyopati (DCM) ve hipertrofik kardiyomiyopati (HCM) gruplarındaki 90 inceleme kullanılır. | `vclinic.acdc.download()`, üç grubun yaklaşık 105 MB'lık dosyalarını Human Heart Project'in açık veri tabanından ders klasöründeki `data/acdc` klasörüne kaydeder. İndirme Google Colab'da da Jupyter'de de aynı biçimde çalışır ve üyelik gerektirmez. | [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/), Lyon Üniversitesi (CREATIS) ve Dijon Üniversite Hastanesi; Creative Commons Atıf-GayriTicari-AynıLisanslaPaylaş 4.0 (CC BY-NC-SA 4.0), ticari olmayan bilimsel araştırma için. Eğitimde bu görüntüleri gösteren şekiller "ACDC, CC BY-NC-SA 4.0" kaynak bilgisini taşır ve aynı lisansa tabidir. | 3. hafta, Python adımı 3, 1. ve 2. uygulama durakları ve 1-9. bölümler |
| EchoNet-Dynamic [9]: Stanford Üniversitesi Tıp Merkezine ait, 112 × 112 piksellik 10.030 apikal dört boşluk ekokardiyografi videosu. Videolarla birlikte ejeksiyon fraksiyonu, hacimler ve diyastol sonu ile sistol sonunda sol ventrikülün uzman çizimleri de verilir. | Her katılımcı [Stanford AIMI](https://aimi.stanford.edu/datasets/echonet-dynamic-cardiac-ultrasound) sitesine kişisel olarak kaydolur ve kişisel bir indirme bağlantısı alır. `vclinic.echonet`, `data/echonet` içindeki zip dosyasını ya da açılmış klasörü okur. Eğitim dosyaları da bağlantıyı da paylaşmaz. | Stanford University School of Medicine EchoNet-Dynamic Dataset Research Use Agreement: Kişisel ve ticari olmayan araştırma kullanımına izin verir; her kullanıcı ayrı ayrı kaydolur. Veri seti [doi:10.71718/yqp5-y078](https://doi.org/10.71718/yqp5-y078) | 3. hafta, 3. uygulama durağı ve 10. bölüm; kaydı olan katılımcılar için |

## Sonraki haftaların veri setleri

Sonraki haftaların veri setleri, her hafta yayımlandığında burada belgelenir. Programda PTB-XL, PhysioNet/Computing in Cardiology Challenge 2020 verileri, MIT-BIH Atriyal Fibrilasyon Veri Tabanı ve ekokardiyografi, kardiyak manyetik rezonans ve koroner anjiyografi alanlarındaki açık veri setleri yer almaktadır. Bir veri seti EchoNet-Dynamic gibi kişisel kayıt gerektirdiğinde defter bu kaydı gerektiren hücreleri işaretler; kaydı olmayan katılımcılar eğitmenin çalıştırmasını izler.

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

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
