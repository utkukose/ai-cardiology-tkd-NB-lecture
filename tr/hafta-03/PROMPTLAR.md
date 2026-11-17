# Prompt kütüphanesi, 3. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[3. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-03/PROMPTS.md)

Bu kütüphanede 3. haftada kullanılan her prompt (istem), eğitimin prompt kartıyla yazılmış olarak yer almaktadır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir. Asistanın yazdığı kod, Jupyter defterinde aynı adı taşıyan alıştırmanın ya da prompt görevinin altına yapıştırılır ve orada çalıştırılır. Alıştırmalarda `teach.check` satırı sonucun doğru olup olmadığını hemen gösterir. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Prompt döngüsü](#prompt-döngüsü)
2. [Alıştırmaların promptları](#alıştırmaların-promptları)
3. [Bölümlerin prompt görevleri](#bölümlerin-prompt-görevleri)
4. [Kodu açıklatmak, onarmak ve denetlemek için kalıplar](#kodu-açıklatmak-onarmak-ve-denetlemek-için-kalıplar)
5. [Haftalık projenin prompt yolu](#haftalık-projenin-prompt-yolu)

## Prompt döngüsü

| Adım | Ne yapılır? |
|---|---|
| 1. Tarif et | Alıştırmanın prompt kartını kopyalayın ya da kartı yedi alanıyla kendiniz yazın: rol, bağlam, veri, görev, kısıtlar, çıktı ve test. |
| 2. Gönder | Promptu bir YZ asistanına gönderin. |
| 3. Çalıştır | Asistanın kodunu alıştırmanın altındaki boş hücreye yapıştırın ve çalıştırın. |
| 4. Denetle | `teach.check` satırının yazdığı sonuca (*doğru* ya da *henüz değil*) ve promptun Test satırına bakın. Sonuç *henüz değil* ise kodu onarım promptuyla asistana geri gönderin. |
| 5. Açıkla | Asistandan kodu satır satır açıklamasını isteyin, ardından kodu bir kez de kendi sözcüklerinizle açıklayın. |
| 6. Kaydet | Aracı, promptu, neyin denetlendiğini ve neyin değiştirildiğini YZ kullanım günlüğüne yazın. |

## Alıştırmaların promptları

Jupyter defterindeki her alıştırmanın hemen altında, katlanmış bir hücrede o alıştırmanın prompt yolu bulunur; aşağıdaki promptlar bunlarla aynıdır. Asistanın kodunu alıştırmanın boş cevap hücresine yapıştırın ve çalıştırın.

### Alıştırma 3.1: Bir kare yığınındaki sayılar

*Jupyter defteri, "Python adımı 3: Görüntüleri dizi olarak işlemek"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X12`, (12, 64, 64) boyutunda bir NumPy dizisidir: 64 × 64 piksellik 12 kare, değerler 0 ile 1
arasında.
Görev: `X12` dizisinin tuttuğu bütün sayıları say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Sayı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma 3.1", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Yöntemi önce 24 sayı tutan `np.zeros((2, 3, 4))` dizisinde dene.
```

### Alıştırma 3.2: Dosyadan okunan bir karenin ortalaması

*Jupyter defteri, "Python adımı 3: Görüntüleri dizi olarak işlemek"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `frame`, VC-1212.png dosyasından `plt.imread` ile okunmuş (64, 64) boyutunda bir NumPy
dizisidir; değerler 0 ile 1 arasındadır.
Görev: Bütün piksellerinin ortalama değerini hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Ortalama, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma 3.2", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: En küçük ve en büyük değeri de yazdır; ortalama bu ikisinin arasında olmalı, en büyük değer
1'i aşmamalı.
```

### Alıştırma 3.3: Daha küçük bir öğrenme hızı

*Jupyter defteri, "Python adımı 3: Görüntüleri dizi olarak işlemek"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `Xs`, 2000 hastanın standartlaştırılmış lvedd_mm ve ivs_mm değerlerini tutan (2000, 2)
boyutunda bir NumPy dizisidir (ortalama 0, SS 1). `target`, 0 ya da 1 değerlerinden oluşan bir NumPy
dizisidir (1 anormal).
Görev: Tek bir lojistik nöronu gradyan inişiyle eğit: w = [0, 0] ve b = 0'dan başla, 0,05 öğrenme
hızıyla 200 güncelleme yap. Her güncelleme p = sigmoid(Xs @ w + b) değerini hesaplar, ardından Xs.T
@ (p − target) / n ve mean(p − target) gradyanlarının 0,05 katını çıkarır. 200 güncellemeden sonra
ortalama ikili çapraz entropiyi hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: 200 güncellemeden sonraki kayıp, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir
değişkende sakla ve kodu `teach.check("Alıştırma 3.3", answer)` satırıyla bitir. Yalnızca kodu, tek
bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Python adımındaki 0,5 öğrenme hızıyla aynı döngü, orada 200. adımda yazdırılan kaybı vermeli.
```

### Alıştırma A: Tek bir nöronun çıktısı

*Jupyter defteri, 1. bölüm, "NumPy ile bir nöron ve bir ağ"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: İki standartlaştırılmış ölçüm `x = [1.2, -0.5]`, ağırlıklar `w = [0.8, -1.5]` ve sabit terim
`b = 0.1`.
Görev: Ağırlıklı toplam z = w · x + b'yi ve sigmoid çıktısını, 1 / (1 + e^(−z)), hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Sigmoid çıktısı, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve
kodu `teach.check("Alıştırma A", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: w = [0, 0] ve b = 0 iken çıktı 0,5 olmalı.
```

### Alıştırma B: Autograd ile bir gradyan

*Jupyter defteri, 2. bölüm, "Öğrenme: PyTorch ile kayıp, gradyanlar ve eğitim döngüsü"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `x = [1.0, 2.0]` değerli ve `y = 1` etiketli tek bir hasta ile ağırlıkları `w = [0.5, -0.25]`,
sabit terimi 0 olan ve sigmoid kullanan tek bir nöron. Kayıp, ikili çapraz entropidir.
Görev: w'yi `requires_grad=True` ile bir tensör yap, kaybı `F.binary_cross_entropy` ile hesapla,
`backward()` çağır ve kaybın ilk ağırlığa göre gradyanını oku.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: w1'e göre gradyan, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla
ve kodu `teach.check("Alıştırma B", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak
ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Sonucu (p − y) · x1 formülüyle karşılaştır; iki değer eşit olmalı.
```

### Alıştırma C: Test kümesindeki anormal kareler

*Jupyter defteri, 3. bölüm, "Eko laboratuvarının kareleri"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X`, sanal kliniğin her hastası için bir diyastol sonu parasternal kısa eksen karesi içeren
(2000, 64, 64) boyutunda bir NumPy dizisidir; piksel değerleri 0 ile 1 arasındadır ve bir piksel 2
mm'dir. `y`, eko laboratuvarının raporunu tutar, 0 ya da 1'dir (1 anormal: sol ventrikül diyastol
sonu çapı 58 mm'nin üstünde ya da septum 13 mm veya daha kalın). `echo_table`; patient_id, lvedd_mm,
ivs_mm ve pw_mm (mm) ile dilated ve thick_septum (0 ya da 1) sütunlarını tutar. `train_idx`,
`val_idx` ve `test_idx`, `y`'ye göre tabakalı olarak ayrılmış 1200, 400 ve 400 karenin indisleridir.
`Xtr`, `Xva` ve `Xte`, eğitim karelerinin ortalaması ve SS'siyle normalleştirilmiş (n, 1, 64, 64)
boyutunda float tensörlerdir; `ytr`, `yva` ve `yte` ise 0 ya da 1 olan etiket tensörleridir.
Görev: Test kümesindeki anormal kareleri (etiket 1) say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Sayı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma C", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Eğitim, doğrulama ve test kümeleri toplam 2000 kare etmeli; anormal karelerin oranı üç kümede
de yaklaşık aynı olmalı.
```

### Alıştırma D: Bir evrişimden sonraki boyut

*Jupyter defteri, 4. bölüm, "Elle ve PyTorch ile evrişim"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: Tek kanallı, 64 × 64 piksellik kare bir girdi.
Görev: 5 × 5 çekirdekli, adımı (stride) 2 ve dolgusu (padding) 1 olan bir evrişimin çıktı boyutunu
floor((n + 2p − k) / s) + 1 formülüyle hesapla ve `torch.zeros(1, 1, 64, 64)` üzerinde `F.conv2d`
ile doğrula.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Çıktı boyutu (bir kenar), tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma D", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 3 × 3 çekirdek, 1 adım ve 1 dolguyla boyut 64 kalmalı.
```

### Alıştırma E: Ağın parametreleri

*Jupyter defteri, 5. bölüm, "İlk evrişimli ağ"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `EchoCNN`, 5. bölümdeki sınıftır: 8, 16 ve 32 kanallı üç Conv2d (3 × 3, padding 1),
BatchNorm2d, ReLU ve MaxPool2d(2) bloğu; ardından Flatten, Dropout(0.3) ve Linear(2048, n_classes).
Görev: `EchoCNN(n_classes=2)` oluştur ve eğitilebilir parametrelerini say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Parametre sayısı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma E", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: `nn.Conv2d(1, 8, 3)` katmanının parametrelerini de say; 80 olmalı.
```

### Alıştırma F: Seyreltmenin ölçeği

*Jupyter defteri, 6. bölüm, "Aşırı öğrenme: Seyreltme, yığın normalizasyonu ve veri çoğaltma"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: On tane birden oluşan bir tensör, `torch.ones(10)`.
Görev: `F.dropout` fonksiyonunu eğitim kipinde p = 0,3 ile uygula ve korunan elemanların aldığı
değeri bul.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Korunan bir elemanın değeri, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir
değişkende sakla ve kodu `teach.check("Alıştırma F", answer)` satırıyla bitir. Yalnızca kodu, tek
bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: `training=False` ile tensör değişmeden geri dönmeli.
```

### Alıştırma G: Üç sınıfın makro F1 değeri

*Jupyter defteri, 7. bölüm, "Sonucu okumak: Kesinlik, duyarlılık ve F1"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: Bir ağın 180 kısa eksen KMR kesitindeki karışıklık matrisi; satırlar gerçek, sütunlar tahmin
edilen sınıf, sıra normal, DCM ve HCM: [[51, 8, 1], [0, 60, 0], [6, 0, 54]].
Görev: Matristen her sınıfın kesinliğini, duyarlılığını ve F1 değerini, ardından bunların ortalaması
olan makro F1'i hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Makro F1, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma G", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: DCM'nin F1 değeri 0,938 olmalı.
```

### Alıştırma H: Bir evrişim katmanının parametreleri

*Jupyter defteri, 8. bölüm, "Bilinen mimariler ve atlama bağlantıları"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 16 giriş kanalı, 32 çıkış kanalı, 3 × 3 çekirdeği ve her çıkış kanalı için bir sabit terimi
olan bir evrişim katmanı.
Görev: Parametrelerini c_in × c_out × k × k + c_out formülüyle say ve sonucu `nn.Conv2d` ile
doğrula.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Parametre sayısı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma H", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: `nn.Conv2d(1, 8, 3)` katmanının 80 parametresi olmalı.
```

### Alıştırma I: Bir artık bloğun parametreleri

*Jupyter defteri, 8. bölüm, "Bilinen mimariler ve atlama bağlantıları"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 64 kanallı bir ResNet temel bloğu: dolgusu 1 olan ve sabit terim içermeyen iki 3 × 3 evrişim,
her birinin ardından `nn.BatchNorm2d(64)`, ilkinin ardından ReLU ve son ReLU'dan önce girdinin
çıktıya eklenmesi.
Görev: Bloğu `nn.Module` alt sınıfı olarak yaz ve eğitilebilir parametrelerini say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Parametre sayısı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma I", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Bloğun `torch.randn(1, 64, 16, 16)` için verdiği çıktı, girdiyle aynı boyutta olmalı.
```

### Alıştırma J: Ders modelini doğru değerlendirmek

*Jupyter defteri, 9. bölüm, "YZ ile eşli kodlama, bölüm 3: Bir eğitim döngüsünü denetlemek"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `course_model`, models/week03/echo_cnn.pt dosyasından yüklenmiş, dersin ağırlıklarını taşıyan
bir `EchoCNN` nesnesidir. `Xte` ve `yte`, 400 test karesi ve etiketleridir (0 ya da 1, 40'ı
anormal).
Görev: Modeli değerlendirme kipine al, `torch.no_grad()` içinde her test karesi için en büyük
çıktıya sahip sınıfı tahmin et ve anormal sınıfın F1 değerini `f1_score` ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: F1, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma J", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Doğruluğu da yazdır: 0,95'in üstünde olmalı, F1 ise belirgin biçimde daha düşük kalmalı.
```

## Bölümlerin prompt görevleri

Jupyter defterindeki her numaralı bölüm bir prompt göreviyle biter. Prompt görevinde bir prompt vardır, ancak hazır kod ve `teach.check` satırı yoktur. Sonucun doğru olup olmadığını her promptun altındaki beklenen sonuç gösterir.

### 1. bölüm: Aktivasyon fonksiyonları ve eğimleri

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: Veri yok: −5 ile 5 arasında z değerlerinden oluşan bir ızgara.
Görev: Sigmoid, tanh ve ReLU fonksiyonlarını bir panelde, türevlerini ikinci bir panelde çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: İki panelli bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: Her türevin en büyük değerini yazdır.
```

**Beklenen sonuç.** Sigmoidin türevi z = 0'da 0,25 ile, tanh'nin türevi 1 ile en yüksek değerine ulaşır; ReLU'nun türevi negatif z için 0, pozitif z için 1'dir.

### 2. bölüm: Üç öğrenme hızı

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `Xs`, 2000 hastanın standartlaştırılmış lvedd_mm ve ivs_mm değerlerini tutan (2000, 2)
boyutunda bir NumPy dizisidir (ortalama 0, SS 1). `target`, 0 ya da 1 değerlerinden oluşan bir NumPy
dizisidir (1 anormal).
Görev: Python adımındaki lojistik nöronu her seferinde sıfır ağırlıklardan başlayarak 0,01, 0,1 ve
1,0 öğrenme hızlarıyla 300 güncelleme boyunca eğit; üç hız için kaybı güncelleme sayısına karşı çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Üç çizgili bir şekil ve her hızın son kaybı. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Kayıplar aynı değerden, log(2) = 0,693'ten başlamalı.
```

**Beklenen sonuç.** 0,01 hızı diğer ikisinin belirgin biçimde üstünde kalır; en hızlı düşüş 1,0 hızındadır. Çok küçük bir hız adımları boşa harcar.

### 3. bölüm: Yan yana normal ve anormal kareler

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X`, sanal kliniğin her hastası için bir diyastol sonu parasternal kısa eksen karesi içeren
(2000, 64, 64) boyutunda bir NumPy dizisidir; piksel değerleri 0 ile 1 arasındadır ve bir piksel 2
mm'dir. `y`, eko laboratuvarının raporunu tutar, 0 ya da 1'dir (1 anormal: sol ventrikül diyastol
sonu çapı 58 mm'nin üstünde ya da septum 13 mm veya daha kalın). `echo_table`; patient_id, lvedd_mm,
ivs_mm ve pw_mm (mm) ile dilated ve thick_septum (0 ya da 1) sütunlarını tutar.
Görev: Dört normal ve dört anormal kareyi 2 × 4'lük bir ızgarada, her birinin başlığına lvedd_mm ve
ivs_mm değerini yazarak göster.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Gösterilen her karenin etiketini yazdır; ilk satır tamamen 0, ikinci satır tamamen 1 olmalı.
```

**Beklenen sonuç.** Anormal kareler ya geniş bir boşluk ya da kalın bir duvar gösterir; kalın duvarların bazılarını gözle normalden ayırmak zordur.

### 4. bölüm: Dilate bir ventrikülde iki filtre

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `frame_d`, VC-1873'ün karesidir; değerleri 0 ile 1 arasında olan (64, 64) boyutunda bir NumPy
dizisi.
Görev: 3 × 3'lük bir ortalama çekirdeği (bütün değerler 1/9) ile 3 × 3'lük Laplace çekirdeğini [[0,
1, 0], [1, −4, 1], [0, 1, 0]] `F.conv2d` ve 1 dolguyla uygula; kareyi ve iki sonucu yan yana göster.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Üç panelli bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: İki sonuç da (64, 64) boyutunda olmalı.
```

**Beklenen sonuç.** Ortalama çekirdeği benek gürültüsünü yumuşatır; Laplace çekirdeği miyokardın sınırlarını belirginleştirir.

### 5. bölüm: Dönem başına doğruluk

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `train_idx`, `val_idx` ve `test_idx`, `y`'ye göre tabakalı olarak ayrılmış 1200, 400 ve 400
karenin indisleridir. `Xtr`, `Xva` ve `Xte`, eğitim karelerinin ortalaması ve SS'siyle
normalleştirilmiş (n, 1, 64, 64) boyutunda float tensörlerdir; `ytr`, `yva` ve `yte` ise 0 ya da 1
olan etiket tensörleridir. `EchoCNN`, 5. bölümdeki sınıftır: 8, 16 ve 32 kanallı üç Conv2d (3 × 3,
padding 1), BatchNorm2d, ReLU ve MaxPool2d(2) bloğu; ardından Flatten, Dropout(0.3) ve Linear(2048,
n_classes).
Görev: Yeni bir `EchoCNN` modelini Adam ile (öğrenme hızı 0,003, 32'lik yığınlar) 10 dönem eğit; her
dönemden sonra eğitim ve doğrulama kümesindeki doğruluğu kaydet. İkisini döneme karşı çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: İki çizgili bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: Doğruluğu değerlendirme kipinde ve `torch.no_grad()` içinde hesapla; iki değer de 0 ile 1
arasında olmalı.
```

**Beklenen sonuç.** İki eğri de ilk dönemlerden sonra 0,9'u aşar, çünkü karelerin yüzde 90'ı normaldir. 7. bölümdeki F1 değeri daha çok şey söyler.

### 6. bölüm: Vakanın sekiz çoğaltılmış kopyası

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `frame`, VC-1212'nin karesidir, (64, 64) boyutunda bir NumPy dizisi; `augment(x)` ise 6.
bölümdeki, (n, 1, 64, 64) boyutunda bir tensör alan fonksiyondur.
Görev: `augment` ile karenin sekiz çoğaltılmış kopyasını oluştur ve 2 × 4'lük bir ızgarada göster.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Her kopya (64, 64) boyutunu korumalı ve değerleri karenin değer aralığına yakın kalmalı.
```

**Beklenen sonuç.** Kalp birkaç piksel döner ve kayar, parlaklık değişir; anatomi ise akla yatkın kalır. Sağ-sol çevirme sağ ventrikülü yanlış tarafa taşırdı.

### 7. bölüm: Eşiklere göre kesinlik ve duyarlılık

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `p_test`, 400 test karesi için anormal sınıfın olasılıkları; `y_test`, etiketleri (0 ya da 1).
Görev: 0,1, 0,2, …, 0,9 eşiklerinin her biri için anormal sınıfın kesinliğini ve duyarlılığını
hesapla; ikisini eşiğe karşı çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve dokuz eşiğin tablosu. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne
kısa bir yorum satırı ekle.
Test: 0,5 eşiğinde tablo, üstteki değerlendirmenin değerlerini göstermeli.
```

**Beklenen sonuç.** Eşik büyüdükçe duyarlılık düşer, kesinlik yükselir; daha düşük bir eşik, daha fazla yanlış alarm pahasına daha çok kalın septum bulur.

### 8. bölüm: Katman katman parametreler

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `EchoCNN`, 5. bölümdeki sınıftır: 8, 16 ve 32 kanallı üç Conv2d (3 × 3, padding 1),
BatchNorm2d, ReLU ve MaxPool2d(2) bloğu; ardından Flatten, Dropout(0.3) ve Linear(2048, n_classes).
Görev: `EchoCNN(n_classes=2)` modelinin parametresi olan her katmanı için bir satır içeren bir tablo
oluştur: katmanın adı, türü ve parametre sayısı.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir pandas DataFrame'i. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: Parametre sütununun toplamı Alıştırma E'deki toplama eşit olmalı.
```

**Beklenen sonuç.** 10098 parametrenin 4098'i doğrusal katmandadır; üç evrişim katmanı toplam 5888 parametre tutar.

### 9. bölüm: Bir modeli değerlendiren fonksiyon

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: Dersin `EchoCNN` modeli olan `course_model` ile `Xte` ve `yte` test tensörleri.
Görev: Modeli değerlendirme kipine alan, `torch.no_grad()` içinde tahmin yapan ve anormal sınıfın
doğruluk, kesinlik, duyarlılık ve F1 değerlerini içeren bir sözlük döndüren `evaluate(model, X, y)`
fonksiyonunu yaz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Fonksiyon ve ders modeli için sonucu, üç ondalığa yuvarlanmış olarak. Yalnızca kodu, tek bir
blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Fonksiyon iki kez çağrıldığında aynı sayıları vermeli.
```

**Beklenen sonuç.** Ders modeli için: doğruluk 0,968, kesinlik 0,909, duyarlılık 0,75 ve F1 0,822.

## Kodu açıklatmak, onarmak ve denetlemek için kalıplar

Bu dört kalıp her alıştırmanın koduyla kullanılabilir. Köşeli parantez içindeki yerler, prompt gönderilmeden önce doldurulur.

### Kodu açıklatmak

```text
Aşağıdaki Python kodunu, Python'a yeni başlayan bir hekim için satır satır açıkla. Ardından kodun
hata mesajı vermeden yanlış sonuç döndürebileceği iki durumu belirt.

[kodu buraya yapıştırın]
```

### Denetimden geçmeyen kodu onarmak

```text
Aşağıdaki kod şu görev için yazıldı: [promptun Görev satırını yapıştırın]. Kod çalışıyor, ancak
teach.check satırı "henüz değil" yazıyor. Hatayı bul, iki cümleyle açıkla ve düzeltilmiş kodu ver.
Değişken adlarını ve teach.check satırını koru.

[kodu buraya yapıştırın]
```

### Bir hata mesajını anlamak

```text
Aşağıdaki hücre bir Jupyter defterinde çalıştırıldığında altta verilen hata mesajını veriyor.
Hatanın nedenini sade bir dille açıkla ve düzeltilmiş kodu ver.

[kodu buraya yapıştırın]

[hata mesajını buraya yapıştırın]
```

### Bir eğitim döngüsünü denetletmek

```text
Aşağıdaki PyTorch kodu bir görüntü sınıflandırıcısını eğitip değerlendirmektedir. Beş şeyi denetle:
normalleştirmenin yalnızca eğitim görüntülerinin istatistiklerini kullanıp kullanmadığı,
model.train() ve model.eval() çağrılarının doğru yerlerde olup olmadığı, değerlendirmenin
torch.no_grad() içinde yapılıp yapılmadığı, çıktı katmanının kayıp fonksiyonuna uyup uymadığı
(CrossEntropyLoss öncesinde softmax olmamalı) ve bildirilen ölçütün nadir bir sınıfa uygun olup
olmadığı. Kısa bir listeyle cevap ver, ardından düzeltilmiş kodu ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Kesitleri hazırlamak

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `Xc, yc, cmr_table = make_cmr_set(300)` çağrısı, 900 kısa eksen sine kardiyak manyetik
rezonans (KMR) kesiti verir: değerleri 0 ile 1 arasında olan (900, 64, 64) boyutunda bir NumPy
dizisi; bir piksel 2 mm'dir. `yc`, normal için 0, dilate kardiyomiyopati (DCM) için 1, hipertrofik
kardiyomiyopati (HCM) için 2'dir. `cmr_table`; study_id, lvedd_mm, septum_mm ve posterior_mm (mm)
ile diagnosis sütunlarını tutar.
Görev: 900 kesiti `yc`'ye göre tabakalı olarak yüzde 60, 20 ve 20'lik eğitim, doğrulama ve test
kümelerine ayır (random_state=RANDOM_STATE). Her kümeyi eğitim kesitlerinin ortalaması ve SS'siyle
normalleştir ve kümeleri (n, 1, 64, 64) boyutunda tensörlere dönüştür.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Altı tensör, Xc_tr, Xc_va, Xc_te, yc_tr, yc_va ve yc_te, ve her kümenin sınıf sayılarını
gösteren bir tablo. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Üç küme 540, 180 ve 180 kesit tutmalı; test kümesinde her sınıftan 60 kesit bulunmalı.
```

### Adım 2: Üç sınıflı bir ağ eğitmek

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 1. adımdaki tensörler, 5. bölümdeki `EchoCNN` sınıfı ve 6. bölümdeki `augment(x)` fonksiyonu.
Görev: `EchoCNN(n_classes=3)` modelini Adam ile (öğrenme hızı 0,003, 32'lik yığınlar) eğitim
yığınlarını çoğaltarak en çok 30 dönem eğit; doğrulama kaybının en düşük olduğu dönemin
ağırlıklarını sakla. Eğitim ve doğrulama kaybını çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Eğitilmiş model ve iki kaybın şekli. Yalnızca kodu, tek bir blok olarak ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: Doğrulama kaybının en düşük olduğu dönemi yazdır; saklanan ağırlıkların doğrulama kaybı
çalıştırmanın en küçüğü olmalı.
```

### Adım 3: Ağı test kesitlerinde ölçmek

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 2. adımdaki model ile Xc_te ve yc_te test tensörleri.
Görev: Değerlendirme kipinde ve `torch.no_grad()` içinde her test kesitinin sınıfını tahmin et.
Karışıklık matrisini, her sınıfın kesinlik, duyarlılık ve F1 değerini ve makro F1'i bildir.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Sınıf adlarıyla bir pandas DataFrame'i olarak karışıklık matrisi ve sınıflara göre üç ölçütün
tablosu. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Karışıklık matrisinin toplamı 180, her satırının toplamı 60 olmalı.
```

### Adım 4: Hatalara bakmak

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla; PyTorch torch,
torch.nn nn ve torch.nn.functional F adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders
paketi, teach ve imaging modülleriyle birlikte kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 3. adımdaki tahminler, `Xc` ve `cmr_table`.
Görev: Yanlış sınıflanan her test kesitini, başlığına gerçek ve tahmin edilen sınıfı ile lvedd_mm ve
septum_mm değerlerini yazarak göster; hataların ölçümlerini bir tabloda özetle.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve bir tablo. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: Gösterilen kesit sayısı, karışıklık matrisindeki hata sayısına eşit olmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
