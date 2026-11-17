# Prompt kütüphanesi, 3. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[3. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-03/PROMPTS.md)

Bu kütüphanede 3. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki her prompt, eğitimin prompt kartıyla yazılmış olarak yer almaktadır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod defterde aynı numaralı adımın altındaki hücreye yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Sayılarla sine MR](#durak-1-sayılarla-sine-mr)
3. [Durak 2: İlk evrişimli ağ](#durak-2-ilk-evrişimli-ağ)
4. [Durak 3: EchoNet-Dynamic: normal mi, anormal mi (kaydınızla)](#durak-3-echonet-dynamic-normal-mi-anormal-mi-kaydınızla)
5. [Kodu onarmak, açıklatmak ve denetlemek için promptlar](#kodu-onarmak-açıklatmak-ve-denetlemek-için-promptlar)
6. [Haftalık projenin prompt yolu](#haftalık-projenin-prompt-yolu)

## Bir adım nasıl ilerler?

| Adım | Ne yapılır? |
|---|---|
| 1. Okuyun | Defterde adımın amacını okuyun. |
| 2. Kopyalayın ve gönderin | Promptu kopyalayın ve bir YZ asistanına gönderin: Google Colab'daki Gemini ya da başka bir tarayıcı sekmesindeki ChatGPT, Claude, Copilot veya Gemini. |
| 3. Çalıştırın | Asistanın kodunu promptun altındaki hücreye yapıştırın ve çalıştırın. |
| 4. Denetleyin | Kontrol hücresini çalıştırın. Hücre *doğru* ya da *henüz değil* yazar ve sonucun değerini gösterir. |
| 5. Onarın | Kontrol *henüz değil* yazarsa onarım promptunu kodla birlikte gönderin. Sonuç yine yanlışsa doğru sonucu veren *Hazır kod* hücresini çalıştırın. |
| 6. Açıklatın ve kaydedin | Asistandan kodu sade bir dille açıklamasını isteyin; aracı, promptu ve neyin denetlendiğini YZ kullanım günlüğüne yazın. |

## Durak 1: Sayılarla sine MR

*[Ders sayfası: uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 3, 1-3. bölümler*

ACDC'nin uzman konturları her incelemeyi sayılara dönüştürür: hacimler, ejeksiyon fraksiyonu (EF) ve duvarların kalınlığı. Bu durakta üç grup bu sayılarla tarif edilir, 134 numaralı hastanın EF'si konturların vokselleriyle hesaplanır ve ACDC kuralları her hastaya uygulanır.

### Adım 1.1: Üç grubun ejeksiyon fraksiyonu

**Amaç.** EF'nin ACDC'nin üç grubunu nasıl ayırdığını görmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `acdc_table`, ACDC'nin NOR (normal), DCM (dilate kardiyomiyopati) ve HCM (hipertrofik
kardiyomiyopati) gruplarındaki 90 hastayı, her hasta için bir satır olmak üzere içeren bir pandas
DataFrame'idir. Burada kullanılan sütunlar: group, split ("training" ya da "testing"), lv_ef (sol
ventrikül ejeksiyon fraksiyonu, %), lv_edvi (vücut yüzey alanına göre indekslenmiş sol ventrikül
diyastol sonu hacmi, mL/m²) ve max_wall_mm (diyastol sonunda en kalın duvar segmenti, mm); hepsi
uzman konturlarından ölçülmüştür.
Görev: groupby ile her grup için lv_ef ortalamasını hesapla ve bir ondalığa yuvarlanmış üç
ortalamayı yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: DCM grubunun ortalama EF'si, bir ondalığa yuvarlanmış olarak. Sonucu `mean_ef_dcm` adlı bir
değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: DCM grubunun ortalama EF'si yüzde 40'ın altında, HCM grubununki yüzde 50'nin üzerinde olmalı.
```

**Beklenen sonuç:** `mean_ef_dcm` = 19,8

### Adım 1.2: 134 numaralı hastanın ejeksiyon fraksiyonu voksellerden

**Amaç.** Bir KMR laboratuvarının yazılımı gibi, uzman konturlarından hacimleri ve EF'yi hesaplamak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `gt_ed` ve `gt_es`, 134 numaralı hastanın diyastol sonu ve sistol sonundaki uzman
konturlarını, her voksel için bir değer olmak üzere içeren NumPy dizileridir: 0 arka plan, 1 sağ
ventrikül boşluğu, 2 miyokard, 3 sol ventrikül boşluğu. `spacing`, bir vokselin mm cinsinden
boyutunu (x, y, z) olarak tutar.
Görev: gt_ed ve gt_es içinde değeri 3 olan vokselleri say. Her sayıyı bir vokselin hacmiyle, yani
spacing'in üç değerinin mm³ cinsinden çarpımıyla çarp ve mL'ye çevirmek için 1000'e böl. Diyastol
sonu hacmi EDV'yi, sistol sonu hacmi ESV'yi ve EF'yi (EDV − ESV)/EDV × 100 olarak hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Yüzde cinsinden EF, bir ondalığa yuvarlanmış olarak; EDV ve ESV'yi de mL cinsinden yazdır.
Sonucu `ef_case` adlı bir değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok
hâlinde ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: EDV, ESV'den büyük olmalı ve 50 ile 300 mL arasında bulunmalı.
```

**Beklenen sonuç:** `ef_case` = 62,2

### Adım 1.3: ACDC kuralları her hastada

**Amaç.** 90 hastayı ACDC tanımlarıyla sınıflamak ve ölçümlerin tek başına nerede yanıldığını görmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `acdc_table`, ACDC'nin NOR (normal), DCM (dilate kardiyomiyopati) ve HCM (hipertrofik
kardiyomiyopati) gruplarındaki 90 hastayı, her hasta için bir satır olmak üzere içeren bir pandas
DataFrame'idir. Burada kullanılan sütunlar: group, split ("training" ya da "testing"), lv_ef (sol
ventrikül ejeksiyon fraksiyonu, %), lv_edvi (vücut yüzey alanına göre indekslenmiş sol ventrikül
diyastol sonu hacmi, mL/m²) ve max_wall_mm (diyastol sonunda en kalın duvar segmenti, mm); hepsi
uzman konturlarından ölçülmüştür.
Görev: ACDC kurallarını her satıra uygula: lv_ef < 40 ve lv_edvi > 100 ise DCM; değilse max_wall_mm
> 15 ve lv_ef >= 50 ise HCM; değilse NOR. Sonucu rule adlı yeni bir sütuna kaydet, group ile rule'un
çapraz tablosunu yazdır ve rule değeri group değerine eşit olan hastaların oranını hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Oran, üç ondalığa yuvarlanmış olarak. Sonucu `rule_accuracy` adlı bir değişkene kaydet ve
kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum
satırı ekle.
Test: Çapraz tablo toplam 90 hasta içermeli ve oran 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** `rule_accuracy` = 0,967

## Durak 2: İlk evrişimli ağ

*[Ders sayfası: uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-2) · Python yolunda aynı sonuç: 4-7. bölümler*

Dersin ağı üç grubu ortadaki kesitlerin piksellerinden öğrenir; her kesitin diyastol sonu ve sistol sonu kareleri iki kanal olarak girer. Bu durakta kesitler normalleştirilir, ağ kurulur, erken durdurmayla eğitilir ve 30 test hastasında hasta hasta değerlendirilir.

### Adım 2.1: Eğitim kesitleriyle normalleştirme

**Amaç.** Ağın tensörlerini yalnızca eğitim hastalarından gelen istatistiklerle hazırlamak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `X`, (270, 2, 64, 64) boyutunda bir NumPy dizisidir: 90 hastanın her birinin ortadaki üç kısa
eksen kesiti; değerler 0 ile 1 arasında, piksel başına 2 mm. 0. kanal kesitin diyastol sonu, 1.
kanal sistol sonu karesidir. `y` her kesitin sınıfını (0 NOR, 1 DCM, 2 HCM), `patients` her kesitin
hastasını, `sets` ise kümesini tutar: "train" (45 hasta), "val" (15 hasta) ya da "test" (30 hasta).
Görev: Eğitim kesitlerindeki (sets == "train") bütün piksellerin ortalamasını ve SS'sini hesapla.
Bütün kesitleri bunlarla (X − ortalama)/SS biçiminde normalleştir. Üç küme için float türü X_train,
X_val ve X_test tensörlerini ve long türü y_train, y_val ve y_test tensörlerini oluştur.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Eğitim piksellerinin ortalaması, dört ondalığa yuvarlanmış olarak. Sonraki adımlar
kullanacağı için altı tensörü koru. Sonucu `train_mean` adlı bir değişkene kaydet ve kısa bir
etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: X_train'in boyutu (135, 2, 64, 64) olmalı; normalleştirilmiş eğitim piksellerinin ortalaması
yaklaşık 0, SS'si yaklaşık 1 olmalı.
```

**Beklenen sonuç:** `train_mean` = 0,2961

### Adım 2.2: Ağ ve parametreleri

**Amaç.** Dersin ağını kurmak ve ağırlıklarını saymak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: 2.1. adımdaki float türü `X_train`, `X_val` ve `X_test` tensörleri ile long türü `y_train`,
`y_val` ve `y_test` tensörleri: eğitim piksellerinin ortalaması ve SS'siyle normalleştirilmiş
kesitler ve sınıfları. `patients` ve `sets` her kesitin hastasını ve kümesini tutar.
Görev: Üç bloklu bir CmrCNN(nn.Module) sınıfı tanımla. Her blok, 3 × 3 çekirdekli ve dolgusu 1 olan
nn.Conv2d, nn.BatchNorm2d, nn.ReLU ve nn.MaxPool2d(2)'den oluşur; kanallar 2'den 8, 16 ve 32'ye
çıkar. Blokların ardından nn.Flatten(), nn.Dropout(0.3) ve nn.Linear(32 * 8 * 8, 3) gelir. model =
CmrCNN() oluştur ve eğitilebilir parametrelerini say.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Eğitilebilir parametre sayısı, tam sayı olarak. CmrCNN sınıfını ve model nesnesini koru.
Sonucu `n_params` adlı bir değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok
hâlinde ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: X_train[:4] üzerine uygulanan model (4, 3) boyutunda bir tensör döndürmeli.
```

**Beklenen sonuç:** `n_params` = 12219

### Adım 2.3: Erken durdurmayla eğitim ve hasta başına karar

**Amaç.** Ağı eğitmek ve onu bir kliniğin yapacağı gibi değerlendirmek: her hasta için tek bir karar.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: 2.1. adımdaki float türü `X_train`, `X_val` ve `X_test` tensörleri ile long türü `y_train`,
`y_val` ve `y_test` tensörleri: eğitim piksellerinin ortalaması ve SS'siyle normalleştirilmiş
kesitler ve sınıfları. `patients` ve `sets` her kesitin hastasını ve kümesini tutar.
Görev: torch.manual_seed(RANDOM_STATE) çağrısından sonra modeli torch.optim.Adam(model.parameters(),
lr=0.003, weight_decay=1e-4), F.cross_entropy ve karıştırılmış 16 eğitim kesitinden oluşan mini
yığınlarla 40 dönem eğit. Her dönemin sonunda değerlendirme kipinde ve gradyansız olarak X_val ve
y_val üzerindeki kaybı hesapla ve doğrulama kaybının en düşük olduğu dönemin ağırlıklarının bir
kopyasını sakla. Sonunda bu ağırlıkları yükle, değerlendirme kipinde X_test'in softmax
olasılıklarını hesapla, bunların her test hastasının kesitleri üzerinden ortalamasını al ve hasta
için karar olarak ortalama olasılığı en yüksek sınıfı seç.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Kararı kendi sınıfına eşit olan test hastalarının oranı, üç ondalığa yuvarlanmış olarak.
Hastaların ortalama olasılıklarını patient_prob'a, sınıflarını patient_true'ya, kararları da
patient_pred'e, sıralanmış hasta adları düzeninde NumPy dizileri olarak kaydet. Sonucu
`patient_accuracy` adlı bir değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir
blok hâlinde ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: 30 test hastası olmalı ve patient_prob'un her satırının toplamı 1 olmalı.
```

**Beklenen sonuç:** `patient_accuracy` = 0,933

### Adım 2.4: Karışıklık matrisi ve makro F1

**Amaç.** Sonucu sınıf sınıf okumak ve ağın kaçırdığı hastaları bulmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: 2.3. adımdaki `patient_true` ve `patient_pred`: 30 test hastasının sınıfları ve kararları (0
NOR, 1 DCM, 2 HCM); `patient_prob` ise hastaların ortalama olasılıkları.
Görev: patient_true ve patient_pred'in karışıklık matrisini confusion_matrix(..., labels=[0, 1, 2])
ile hesapla ve satır ile sütun adları NOR, DCM ve HCM olacak biçimde yazdır. Makro F1'i
f1_score(..., average="macro") ile hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Makro F1, üç ondalığa yuvarlanmış olarak. Sonucu `macro_f1` adlı bir değişkene kaydet ve kısa
bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum
satırı ekle.
Test: Karışıklık matrisinin toplamı 30 hasta olmalı.
```

**Beklenen sonuç:** `macro_f1` = 0,933

## Durak 3: EchoNet-Dynamic: normal mi, anormal mi (kaydınızla)

*[Ders sayfası: uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-3) · Python yolunda aynı sonuç: 8-10. bölümler*

Oturumun mini projesi, her katılımcının Stanford AIMI'ye kişisel kayıtla edindiği ekokardiyografi videoları olan EchoNet-Dynamic'i kullanır. Kaydınız yoksa eğitmenin ortak ekrandaki çalıştırmasını izleyin. Kaydınız varsa kişisel indirme bağlantınızı aşağıdaki ilk hücreye yapıştırın ya da zip dosyasını ders klasöründeki data/echonet klasörüne koyun. Veriler Colab oturumunuzda ya da bilgisayarınızda kalır ve hiçbir zaman başka bir yere yüklenmez.

### Adım 3.1: Videolar ve kümeleri

**Amaç.** Her analizden önce kopyanın eksiksiz olduğunu denetlemek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `echo`, katılımcının kendi EchoNet-Dynamic kopyasıdır. `echonet.file_list(echo)`, FileList.csv
dosyasını her video için bir satır içeren bir pandas DataFrame'i olarak döndürür; burada kullanılan
sütunlar: FileName, EF (ejeksiyon fraksiyonu, %) ve Split ("TRAIN", "VAL" ya da "TEST").
`echonet.frame_pairs(echo, split=..., n=..., size=64, seed=...)` bir sözlük döndürür: images,
kümenin n videosunun çizilmiş diyastol sonu ve sistol sonu karelerini iki kanal olarak ve 0-1
aralığındaki değerlerle tutan (n, 2, 64, 64) boyutunda bir dizi; abnormal ise EF yüzde 50'nin
altındaysa 1'dir.
Görev: Videoların tablosunu echonet.file_list(echo) ile al; Split sütununun her değeri için video
sayısını ve toplam video sayısını yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Toplam video sayısı, tam sayı olarak. Sonucu `n_videos` adlı bir değişkene kaydet ve kısa bir
etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Üç kümede 7465, 1288 ve 1277 video bulunmalı.
```

**Beklenen sonuç:** `n_videos`: eksiksiz bir kopya için 10030

### Adım 3.2: Anormal EF oranı

**Amaç.** Bir modeli değerlendirmeden önce anormal sınıfın ne kadar sık olduğunu bilmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `echo`, katılımcının kendi EchoNet-Dynamic kopyasıdır. `echonet.file_list(echo)`, FileList.csv
dosyasını her video için bir satır içeren bir pandas DataFrame'i olarak döndürür; burada kullanılan
sütunlar: FileName, EF (ejeksiyon fraksiyonu, %) ve Split ("TRAIN", "VAL" ya da "TEST").
`echonet.frame_pairs(echo, split=..., n=..., size=64, seed=...)` bir sözlük döndürür: images,
kümenin n videosunun çizilmiş diyastol sonu ve sistol sonu karelerini iki kanal olarak ve 0-1
aralığındaki değerlerle tutan (n, 2, 64, 64) boyutunda bir dizi; abnormal ise EF yüzde 50'nin
altındaysa 1'dir.
Görev: Split değeri "TEST" olan videoları seç ve EF'si 50'nin altında olanların oranını hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Oran, üç ondalığa yuvarlanmış olarak. Sonucu `share_low_ef` adlı bir değişkene kaydet ve kısa
bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum
satırı ekle.
Test: Oran 0 ile 1 arasında olmalı ve test videosu sayısı 1277 olmalı.
```

**Beklenen sonuç:** `share_low_ef`: hazır kodun kopyanızdaki değeri

### Adım 3.3: Dersin ağı ekokardiyografide

**Amaç.** Aynı ağı videoların diyastol sonu ve sistol sonu karelerinde eğitmek ve anormal EF'yi ne kadar iyi tanıdığını ölçmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `echo`, katılımcının kendi EchoNet-Dynamic kopyasıdır. `echonet.file_list(echo)`, FileList.csv
dosyasını her video için bir satır içeren bir pandas DataFrame'i olarak döndürür; burada kullanılan
sütunlar: FileName, EF (ejeksiyon fraksiyonu, %) ve Split ("TRAIN", "VAL" ya da "TEST").
`echonet.frame_pairs(echo, split=..., n=..., size=64, seed=...)` bir sözlük döndürür: images,
kümenin n videosunun çizilmiş diyastol sonu ve sistol sonu karelerini iki kanal olarak ve 0-1
aralığındaki değerlerle tutan (n, 2, 64, 64) boyutunda bir dizi; abnormal ise EF yüzde 50'nin
altındaysa 1'dir.
Görev: echonet.frame_pairs(echo, split="TRAIN", n=1000, size=64, seed=RANDOM_STATE) ile 1000 eğitim
videosunun, split="TEST" ve n=400 ile de 400 test videosunun kare çiftlerini yükle. İkisini de
eğitim piksellerinin ortalaması ve SS'siyle normalleştir. torch.manual_seed(RANDOM_STATE)
çağrısından sonra CmrCNN(n_classes=2) modelini etiket olarak abnormal ile, torch.optim.Adam (lr
0.003), F.cross_entropy ve karıştırılmış 32 eğitim videosundan oluşan mini yığınlarla 15 dönem eğit.
Ardından değerlendirme kipinde ve gradyansız olarak test videolarında 1. sınıfın softmax olasılığını
ve roc_auc_score ile AUC değerini hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: AUC, üç ondalığa yuvarlanmış olarak. Sonucu `auc_echo` adlı bir değişkene kaydet ve kısa bir
etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Eğitim görüntülerinin boyutu (1000, 2, 64, 64) olmalı ve AUC 0,5 ile 1 arasında bulunmalı.
```

**Beklenen sonuç:** `auc_echo`: 0,6 ile 1,0 arasında, bilgisayardan bilgisayara biraz değişen bir değer

## Kodu onarmak, açıklatmak ve denetlemek için promptlar

Bu promptlar her adımın koduyla kullanılabilir. Köşeli parantez içindeki yerler, prompt gönderilmeden önce doldurulur.

### Çalışan ama kontrolden geçmeyen kodu onarmak

```text
Aşağıdaki kod şu görev için yazıldı: [promptun Görev satırını yapıştırın]. Kod çalışıyor, ancak
dersin kontrolü "henüz değil" yazıyor. Hatayı bul, iki cümleyle açıkla ve düzeltilmiş kodu ver.
Sonucu tutan değişkenin adını koru.

[kodu buraya yapıştırın]
```

### Bir hata mesajını anlamak

```text
Aşağıdaki kod bir Jupyter defterinde çalıştırıldığında altta verilen hata mesajını veriyor. Hatanın
nedenini sade bir dille açıkla ve düzeltilmiş kodu ver.

[kodu buraya yapıştırın]

[hata mesajını buraya yapıştırın]
```

### Kodu açıklatmak

```text
Aşağıdaki Python kodunu, Python'a yeni başlayan bir hekim için satır satır açıkla. Ardından kodun
hata mesajı vermeden yanlış sonuç döndürebileceği iki durumu belirt.

[kodu buraya yapıştırın]
```

### Bir eğitim döngüsünü denetletmek

```text
Aşağıdaki PyTorch kodu tıbbi görüntüler için bir sınıflandırıcıyı eğitip değerlendirmektedir. Altı
şeyi denetle: eğitim, doğrulama ve test kümelerine ayırmanın hastaya göre yapılıp yapılmadığı,
normalleştirmenin yalnızca eğitim görüntülerinin istatistiklerini kullanıp kullanmadığı,
model.train() ve model.eval() çağrılarının doğru yerlerde olup olmadığı, değerlendirmenin
torch.no_grad() içinde yapılıp yapılmadığı, çıktı katmanının kayıp fonksiyonuna uyup uymadığı
(F.cross_entropy öncesinde softmax olmamalı) ve bildirilen ölçütün sınıflara uygun olup olmadığı ve
her hasta için tek bir karar verip vermediği. Kısa bir listeyle cevap ver, ardından düzeltilmiş kodu
ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Ağı eğitmek

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `X`, (270, 2, 64, 64) boyutunda bir NumPy dizisidir: 90 hastanın her birinin ortadaki üç kısa
eksen kesiti; 0. kanalda diyastol sonu, 1. kanalda sistol sonu karesi, değerler 0 ile 1 arasında,
piksel başına 2 mm. `y` her kesitin sınıfını (0 NOR, 1 DCM, 2 HCM), `patients` hastasını, `sets` ise
kümesini tutar: "train" (45 hasta), "val" (15) ya da "test" (30). `CmrCNN`, 5. bölümdeki sınıftır: 2
kanallı bir girdi üzerinde 8, 16 ve 32 kanallı üç Conv2d (3 × 3, padding 1), BatchNorm2d, ReLU ve
MaxPool2d(2) bloğu; ardından Flatten, Dropout(0.3) ve Linear(2048, 3).
Görev: `X` dizisini eğitim piksellerinin (`sets == "train"`) ortalaması ve SS'siyle normalleştir; üç
kümeyi (n, 2, 64, 64) boyutunda float tensörlere, sınıflarını da long tensörlere dönüştür.
`torch.manual_seed(RANDOM_STATE)` çağrısından sonra `CmrCNN()` modelini Adam (öğrenme hızı 0,003),
`F.cross_entropy` ve karıştırılmış 16 eğitim kesitlik mini yığınlarla 40 dönem eğit. Her dönemden
sonra doğrulama kaybını değerlendirme kipinde ve gradyansız hesapla; doğrulama kaybı en düşük olan
ağırlıkların bir kopyasını sakla. Eğitim ve doğrulama kaybını döneme karşı çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Saklanan ağırlıklarla eğitilmiş model ve iki kaybın şekli. Yalnızca kodu, tek bir blok olarak
ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Doğrulama kaybının en düşük olduğu dönemi yazdır; saklanan ağırlıklar yüklendikten sonra
doğrulama kaybı yine bu en düşük değeri vermeli.
```

### Adım 2: Ağın karışıklık matrisi

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: 1. adımdaki model, 1. adımdaki test tensörü ve kesitlerin `y` ve `patients` dizileri;
`sets == "test"` test kesitlerini işaretler.
Görev: Değerlendirme kipinde ve `torch.no_grad()` içinde test kesitlerinin softmax olasılıklarını
hesapla, bunların her hastanın kesitleri üzerinden ortalamasını al ve ortalaması en büyük sınıfı
karar olarak seç. 30 test hastasının NOR, DCM ve HCM sınıflarıyla karışıklık matrisini, her sınıfın
kesinlik, duyarlılık ve F1 değerini ve makro F1'i bildir.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir pandas DataFrame'i olarak karışıklık matrisi ve sınıflara göre üç ölçütün tablosu.
Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Matrisin toplamı 30, her satırının toplamı 10 olmalı.
```

### Adım 3: Aynı hastalarda kurallar

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `acdc_table`, ACDC'nin NOR (normal), DCM (dilate kardiyomiyopati) ve HCM (hipertrofik
kardiyomiyopati) gruplarındaki 90 hastayı, her hasta için bir satır olmak üzere içeren bir pandas
DataFrame'idir. Burada kullanılan sütunlar: group, split ("training" ya da "testing"), lv_ef (sol
ventrikül ejeksiyon fraksiyonu, %), lv_edvi (vücut yüzey alanına göre indekslenmiş sol ventrikül
diyastol sonu hacmi, mL/m²) ve max_wall_mm (diyastol sonunda en kalın duvar segmenti, mm); hepsi
uzman konturlarından ölçülmüştür.
Görev: ACDC kurallarını `acdc_table` tablosunun split değeri "testing" olan satırlarına uygula:
lv_ef < 40 ve lv_edvi > 100 ise DCM; değilse max_wall_mm > 15 ve lv_ef >= 50 ise HCM; değilse NOR.
group ile kuralın sonucunun karışıklık matrisini NOR, DCM, HCM sırasıyla ve doğruluğu bildir.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir pandas DataFrame'i olarak karışıklık matrisi ve üç ondalığa yuvarlanmış doğruluk.
Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Matrisin toplamı 30 olmalı; aynı kurallar 90 hastanın tamamında 1.3. adımın doğruluğunu
vermeli.
```

### Adım 4: Hatalar

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, torch, torch.nn nn ve
torch.nn.functional F adıyla; copy de kendi adıyla içe aktarılmıştır. scikit-learn'den şunlar içe
aktarılmıştır: confusion_matrix, f1_score, accuracy_score ve roc_auc_score. vclinic ders paketi acdc
ve echonet modülleriyle, vclinic.nifti'den de read_nifti içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: 2. adımdaki kararlar ve test hastalarının adları, `acdc_table` ve
`S = acdc.slices(("NOR", "DCM", "HCM"))`; sonuncusu her hastanın ortadaki üç kesitine ait images (n,
64, 64), patient ve phase ("ED" ya da "ES") dizilerini tutan bir sözlüktür. `acdc.walls(name)`,
hastanın diyastol sonundaki her kesitinde en kalın duvarı mm cinsinden, tabandan (0. kesit) apekse
doğru veren bir sözlük döndürür.
Görev: Kararı sınıfından farklı olan her test hastası için ağın gördüğü üç diyastol sonu kesitini,
başlıkta sınıf, karar ve max_wall_mm değeriyle göster. Ardından incelemenin her kesitindeki en kalın
duvarı tabandan apekse doğru yazdır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Yanlış sınıflanan her hasta için bir şekil ve kesit başına en kalın duvarın listesi. Yalnızca
kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Gösterilen hasta sayısı, 2. adımdaki karışıklık matrisinin hata sayısına eşit olmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
