# Veri setleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](DATASETS.md)

Eğitimdeki her veri seti ya sentetiktir ya da açık veridir. 1. haftanın dosyaları [data](data) klasöründe yer alır; böylece Jupyter defterleri üyelik gerektirmeden çalışır. Her veri seti kendi lisansını korur ve künyesi aşağıda verilmiştir.

## 1. haftanın veri setleri

| Veri seti | Depodaki dosyalar | Kaynak ve lisans | Kullanıldığı yer |
|---|---|---|---|
| UCI Heart Disease, Cleveland verisi [1, 2] | `data/uci-heart-disease/processed.cleveland.data`: 303 hasta, 14 değişken | UCI Machine Learning Repository, [doi:10.24432/C52P4X](https://doi.org/10.24432/C52P4X); Creative Commons Atıf 4.0 Uluslararası (CC BY 4.0) | 1. hafta, 1. bölüm; 2. hafta, Python adımı 2 ve 1-4. bölümler |
| MIT-BIH Arrhythmia Database, 100 numaralı kayıt [3, 4, 5] | `data/physionet/mitdb/100.hea`, `100.dat`, `100.atr`: atım etiketleriyle birlikte 360 Hz'de iki derivasyonun (MLII ve V5) 30 dakikası | PhysioNet, [doi:10.13026/C2F305](https://doi.org/10.13026/C2F305); Open Data Commons Attribution License v1.0 (ODC-By 1.0) | 1. hafta, 6. bölüm |
| PTB Diagnostic ECG Database, 001 numaralı hasta, s0010_re kaydı [5, 6, 7] | `data/physionet/ptbdb/patient001/s0010_re.hea`, `.dat`, `.xyz`: 1000 Hz'de 12 standart derivasyonun ve 3 Frank derivasyonunun 38,4 saniyesi | PhysioNet, [doi:10.13026/C28C71](https://doi.org/10.13026/C28C71); ODC-By 1.0 | 1. hafta, 8. bölüm |
| Örnek kumpas ölçümleri | `data/examples/example_caliper_measurements.csv`: sanal kliniğin beş hastasına ait 20 aralık ölçümü | Eğitim için oluşturulmuştur; CC BY 4.0 | 1. hafta, 5. bölüm |

PTB veri tabanındaki kayıt, başlık dosyasında belirtildiği gibi akut inferolateral miyokart enfarktüsüyle yatırılan 81 yaşında bir kadına aittir. Dosyalar, PhysioNet'te ve UCI deposunda yayımlanan dosyaların değiştirilmemiş kopyalarıdır.

## Sanal klinik

`vclinic` ders paketi sanal kliniğin hastalarını çalışma anında oluşturur. `vclinic.make_cohort(500)` fonksiyonu 500 sentetik hastadan oluşan bir kayıt döndürür. Kayıtta her hastanın demografik verileri, risk faktörleri, laboratuvar değerleri, ejeksiyon fraksiyonu, ana tanısı ve elektrokardiyogram (EKG) parametreleri bulunur. `vclinic.patient_ecg` bir hastanın 12 derivasyonlu EKG'sini aralıklarının ve atım zamanlarının gerçek değerleriyle birlikte döndürür. Aynı tohum değeri her zaman aynı hastaları verir; böylece her katılımcı aynı kliniği görür. Değişkenler arasındaki ilişkiler genel klinik örüntüleri izler ve etki büyüklükleri `vclinic.TRUE_EFFECTS` içinde belgelenmiştir. 2. haftadan itibaren `vclinic.add_followup` fonksiyonu kayda ekokardiyografik değişkenleri, kalp yetersizliği fenogrubunu ve en fazla beş yıllık izlem verisini ekler; izlemde olay, ölüm ya da kalp yetersizliği nedeniyle hastaneye yatıştır. 3. haftadan itibaren `vclinic.imaging` modülü görüntüler çizer: `echo_images` bir kayıttaki her hasta için, hastanın kendi çapından ve duvar kalınlığından çizilen bir diyastol sonu parasternal kısa eksen karesi verir; `make_cmr_set` ise üç sınıf için, yani normal, dilate kardiyomiyopati ve hipertrofik kardiyomiyopati için sine kardiyak manyetik rezonans (KMR) kısa eksen kesitleri verir. Veriler öğretim malzemesidir ve klinik kullanım için değildir.

## 3. haftanın dosyaları

| Dosya | İçerik | Lisans | Kullanıldığı yer |
|---|---|---|---|
| `data/examples/echo/VC-0821.png`, `VC-1873.png`, `VC-1212.png` | Sanal kliniğin eko laboratuvarından üç kare; 64 × 64 piksel, gri tonlu, bir piksel = 2 mm: normal bir ventrikül, dilate bir ventrikül ve kalın bir septum | Eğitim için oluşturulmuştur; CC BY 4.0 | 3. hafta, Python adımı 3 ve 4. bölüm |
| `models/week03/echo_cnn.pt`, `echo_cnn.json` | Eko laboratuvarı ağının ağırlıkları (10.098 parametreli bir PyTorch durum sözlüğü), normalleştirmesinin ortalaması ile standart sapması ve sınıflarının adları | Eğitim için sanal kliniğin kareleriyle eğitilmiştir; CC BY 4.0 | 3. hafta, 9. bölüm |

## Sonraki haftaların veri setleri

Sonraki haftaların veri setleri, her hafta yayımlandığında burada belgelenir. Programda PTB-XL, PhysioNet/Computing in Cardiology Challenge 2020 verileri, MIT-BIH Atrial Fibrillation Database ve ekokardiyografi, kardiyak manyetik rezonans ve koroner anjiyografi alanlarındaki açık veri setleri yer almaktadır. Bazı görüntüleme veri setleri üyelik ve bir veri kullanım sözleşmesinin kabulünü gerektirir. Bu haftalarda sanal klinik sentetik veriler sağlar; böylece her defter üyelik olmadan da çalışır.

## Kaynaklar

1. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). *Heart Disease* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X
2. Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J.-J., Sandhu, S., Guppy, K. H., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. *The American Journal of Cardiology, 64*(5), 304–310. https://doi.org/10.1016/0002-9149(89)90524-9
3. Moody, G. B., & Mark, R. G. (2005). *MIT-BIH Arrhythmia Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C2F305
4. Moody, G. B., & Mark, R. G. (2001). The impact of the MIT-BIH Arrhythmia Database. *IEEE Engineering in Medicine and Biology Magazine, 20*(3), 45–50. https://doi.org/10.1109/51.932724
5. Goldberger, A. L., Amaral, L. A. N., Glass, L., Hausdorff, J. M., Ivanov, P. Ch., Mark, R. G., Mietus, J. E., Moody, G. B., Peng, C.-K., & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. *Circulation, 101*(23), e215–e220. https://doi.org/10.1161/01.CIR.101.23.e215
6. Bousseljot, R., Kreiseler, D., & Schnabel, A. (2004). *The PTB Diagnostic ECG Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C28C71
7. Bousseljot, R., Kreiseler, D., & Schnabel, A. (1995). Nutzung der EKG-Signaldatenbank CARDIODAT der PTB über das Internet. *Biomedizinische Technik / Biomedical Engineering, 40*(s1), 317–318. https://doi.org/10.1515/bmte.1995.40.s1.317

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
