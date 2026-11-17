# Prompt kütüphanesi, 1. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[1. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-01/PROMPTS.md)

Bu kütüphanede 1. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki her prompt, eğitimin prompt kartıyla yazılmış olarak yer almaktadır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod defterde aynı numaralı adımın altındaki hücreye yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Hasta tabloları](#durak-1-hasta-tabloları)
3. [Durak 2: Veri olarak EKG](#durak-2-veri-olarak-ekg)
4. [Durak 3: Gerçek kayıtlar ve denetlenecek bir fonksiyon](#durak-3-gerçek-kayıtlar-ve-denetlenecek-bir-fonksiyon)
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

## Durak 1: Hasta tabloları

*[Ders sayfası: uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 1, 1. ve 2. bölümler*

Bir kliniğin kaydı bir tablodur: her hasta için bir satır, her değişken için bir sütun. Bu durakta Cleveland verisinin 303 hastası ve sanal kliniğin ilk 500 hastası, her birinin arkasında klinik bir soru bulunan bir ortalama, bir oran ve bir sayıyla özetlenir.

### Adım 1.1: Hastalığı olanların ortalama yaşı

**Amaç.** Koroner arter hastalığı olan Cleveland hastalarının ortalama kaç yaşında olduğunu bulmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `heart`, UCI Heart Disease veri setindeki Cleveland Clinic'e ait 303 hastayı, her hasta için
bir satır olmak üzere içeren bir pandas DataFrame'idir. Burada kullanılan sütunlar: age (yaş, yıl),
sex (1 erkek, 0 kadın) ve disease (anjiyografide en az bir ana koroner arterde yüzde 50'den fazla
çap daralması varsa 1, yoksa 0).
Görev: disease değeri 1 olan hastaları seç ve ortalama yaşlarını hesapla. Kaç hasta seçildiğini de
yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Yıl cinsinden ortalama yaş, bir ondalığa yuvarlanmış olarak. Sonucu `mean_age` adlı bir
değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: 303 hastanın tamamının ortalama yaşı 54,4'tür; hastalığı olanların sonucu bundan farklı
olmalı.
```

**Beklenen sonuç:** `mean_age` = 56,6

### Adım 1.2: Kadınların oranı

**Amaç.** Cleveland hastalarının yüzde kaçının kadın olduğunu bulmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `heart`, UCI Heart Disease veri setindeki Cleveland Clinic'e ait 303 hastayı, her hasta için
bir satır olmak üzere içeren bir pandas DataFrame'idir. Burada kullanılan sütunlar: age (yaş, yıl),
sex (1 erkek, 0 kadın) ve disease (anjiyografide en az bir ana koroner arterde yüzde 50'den fazla
çap daralması varsa 1, yoksa 0).
Görev: sex değeri 0 olan hastaları say ve bütün hastaların sayısına böl. Erkeklerin oranını da
yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Kadınların yüzde cinsinden oranı, bir ondalığa yuvarlanmış olarak. Sonucu `pct_women` adlı
bir değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Kadınların ve erkeklerin oranları toplam 100 etmeli.
```

**Beklenen sonuç:** `pct_women` = 32,0

### Adım 1.3: Sanal klinikte HFrEF hastaları

**Amaç.** Sanal klinikte ejeksiyon fraksiyonu düşük kalp yetersizliği olan hastaları saymak ve her tanının ejeksiyon fraksiyonunu tek bir şekilde görmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `clinic`, sanal kliniğin ilk 500 sentetik hastasını, her hasta için bir satır olmak üzere
içeren bir pandas DataFrame'idir. Burada kullanılan sütunlar: patient_id, main_diagnosis ("none"
tanı yok, "CCS" kronik koroner sendrom, "ACS" akut koroner sendrom, "HFrEF" ejeksiyon fraksiyonu
düşük kalp yetersizliği ya da "HFpEF" ejeksiyon fraksiyonu korunmuş kalp yetersizliği) ve lvef (sol
ventrikül ejeksiyon fraksiyonu, %).
Görev: main_diagnosis değeri "HFrEF" olan hastaları say. Ardından her ana tanı için lvef değerinin
kutu grafiğini çiz; x ekseninde tanı, y ekseninde yüzde cinsinden ejeksiyon fraksiyonu olsun.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: HFrEF hastalarının sayısı, tam sayı olarak. Sonucu `n_hfref` adlı bir değişkene kaydet ve
kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum
satırı ekle.
Test: Beş tanının sayıları toplam 500 etmeli.
```

**Beklenen sonuç:** `n_hfref` = 47

## Durak 2: Veri olarak EKG

*[Ders sayfası: uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-2) · Python yolunda aynı sonuç: 3-5. bölümler*

Dijital bir EKG bir sayı tablosudur: her derivasyon için bir sütun, her örnek için bir satır. Bu durakta haftanın vakası VC-0317'nin 12 derivasyonlu EKG'si çizilir ve ölçülür; başka bir hastanın QT aralığı da iki formülle kalp hızına göre düzeltilir.

### Adım 2.1: Bir D2 şeridi

**Amaç.** D2 derivasyonunun ilk 2,5 saniyesini çizmek ve böyle bir şeridin kaç sayı tuttuğunu görmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `case`, sanal kliniğin VC-0317 numaralı hastasının 12 derivasyonlu istirahat EKG'sidir ve ders
paketinin bir nesnesidir: `case.fs` örnekleme frekansıdır (500 Hz), `case.leads` her derivasyon için
bir sütun (I, II, III, aVR, aVL, aVF, V1-V6) ve her örnek için bir satır içeren, milivolt cinsinden
bir pandas DataFrame'idir; `case.lead("II")` ise D2 derivasyonunu bir NumPy dizisi olarak döndürür.
Kayıt 10 saniye sürer.
Görev: D2 derivasyonunu case.lead("II") ile al ve ilk 2,5 saniyesini, yani case.fs × 2,5 örneği tut.
Bunları x ekseninde saniye cinsinden zaman, y ekseninde milivolt cinsinden genlik olacak biçimde
çiz.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: 2,5 saniyedeki örnek sayısı, tam sayı olarak. Sonucu `n_samples` adlı bir değişkene kaydet ve
kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum
satırı ekle.
Test: Zaman ekseni 2,5 saniyede bitmeli.
```

**Beklenen sonuç:** `n_samples` = 1250

### Adım 2.2: R tepelerinden kalp hızı

**Amaç.** D2 derivasyonunun R tepelerini bulmak ve aralarındaki sürelerden kalp hızını hesaplamak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `case`, sanal kliniğin VC-0317 numaralı hastasının 12 derivasyonlu istirahat EKG'sidir ve ders
paketinin bir nesnesidir: `case.fs` örnekleme frekansıdır (500 Hz), `case.leads` her derivasyon için
bir sütun (I, II, III, aVR, aVL, aVF, V1-V6) ve her örnek için bir satır içeren, milivolt cinsinden
bir pandas DataFrame'idir; `case.lead("II")` ise D2 derivasyonunu bir NumPy dizisi olarak döndürür.
Kayıt 10 saniye sürer. Ders paketindeki `measure.detect_r_peaks(signal, fs)`, tek bir derivasyonu
NumPy dizisi olarak ve örnekleme frekansını Hz cinsinden alır; R tepelerinin örnek numaralarını bir
NumPy dizisi olarak döndürür.
Görev: D2 derivasyonunun tamamındaki R tepelerini measure.detect_r_peaks ile bul. Ardışık tepeler
arasındaki farkları case.fs'ye bölerek saniyeye çevir ve kalp hızını 60'ın saniye cinsinden ortalama
RR aralığına bölümü olarak hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Dakikadaki atım sayısı cinsinden kalp hızı, bir ondalığa yuvarlanmış olarak. R tepelerinin
sayısını da yazdır. Sonucu `hr_bpm` adlı bir değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca
kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: 10 saniyelik kayıtta yaklaşık 14 R tepesi bulunmalı.
```

**Beklenen sonuç:** `hr_bpm` = 84,9

### Adım 2.3: İki formülle QTc

**Amaç.** VC-0254 numaralı hastanın QT aralığını, hızlı kalp atımına göre Fridericia ve Bazett formülleriyle düzeltmek ve ikisini karşılaştırmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: Sanal klinikteki VC-0254 numaralı hastanın kayıttaki QT aralığı, dakikada 98 atımlık kalp
hızında 343 ms'dir.
Görev: RR aralığını saniye cinsinden 60'ın kalp hızına bölümü olarak hesapla. Ardından QTc'yi
Fridericia formülüyle (QT bölü RR'nin küp kökü) ve Bazett formülüyle (QT bölü RR'nin karekökü)
hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Fridericia formülüyle milisaniye cinsinden QTc, bir ondalığa yuvarlanmış olarak. Bazett
formülüyle QTc'yi de yazdır. Sonucu `qtc_fridericia` adlı bir değişkene kaydet ve kısa bir etiketle
yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Dakikada 60 atımlık kalp hızında iki formül de QT'nin kendisini vermeli.
```

**Beklenen sonuç:** `qtc_fridericia` = 403,9

## Durak 3: Gerçek kayıtlar ve denetlenecek bir fonksiyon

*[Ders sayfası: uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-3) · Python yolunda aynı sonuç: 6-9. bölümler*

Gerçek kayıtlar kendi gürültülerini, işaretlemelerini ve birimlerini getirir. Bu durakta MIT-BIH Arrhythmia Database'deki 100 numaralı kayıt, kardiyologlarının atım etiketleriyle okunur ve normal atımlarından kalp hızı değişkenliği hesaplanır. Ardından PTB veri tabanından gerçek bir 12 derivasyonlu EKG çizilir ve bir YZ asistanının yazdığı bir QTc fonksiyonu denetlenip düzeltilir.

### Adım 3.1: 100 numaralı kaydın atımları

**Amaç.** 30 dakikalık bir kaydın atımlarını, kardiyologların onlara verdiği etiketlere göre saymak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `ann_symbols`, MIT-BIH Arrhythmia Database'deki 100 numaralı kaydın etiketlerinin, zaman
sırasıyla her işaretleme için bir tane olmak üzere listesidir: N normal atım, A atriyal erken atım,
V ventriküler erken atım ve + bir ritim değişikliği (atım değildir). `ann_samples` her etiketin
örnek numarasını tutar; `fs_mit` örnekleme frekansıdır, 360 Hz.
Görev: ann_symbols içinde her etiketin kaç kez geçtiğini say ve sayıları yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Atriyal erken atımların (A etiketi) sayısı, tam sayı olarak. Sonucu `n_apb` adlı bir
değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: N, A ve V etiketleri birlikte 2273 atım saymalı.
```

**Beklenen sonuç:** `n_apb` = 33

### Adım 3.2: Kalp hızı değişkenliği: SDNN

**Amaç.** Normal atımlar arasındaki sürelerin 30 dakika boyunca ne kadar değiştiğini ölçmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `ann_symbols`, MIT-BIH Arrhythmia Database'deki 100 numaralı kaydın etiketlerinin, zaman
sırasıyla her işaretleme için bir tane olmak üzere listesidir: N normal atım, A atriyal erken atım,
V ventriküler erken atım ve + bir ritim değişikliği (atım değildir). `ann_samples` her etiketin
örnek numarasını tutar; `fs_mit` örnekleme frekansıdır, 360 Hz.
Görev: Atım olan etiketleri tut (+ dışındaki bütün etiketler). ann_samples ve fs_mit ile ardışık
atımlar arasındaki RR aralıklarını milisaniye cinsinden hesapla. Yalnızca iki atımı da N etiketli
olan aralıkları, yani normalden normale (NN) aralıkları tut. NN aralıklarının ddof=1 ile standart
sapması olan SDNN'i hesapla ve ortalama NN aralığını da yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Milisaniye cinsinden SDNN, bir ondalığa yuvarlanmış olarak. Sonucu `sdnn` adlı bir değişkene
kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa
bir yorum satırı ekle.
Test: Ortalama NN aralığı 700 ile 900 ms arasında olmalı.
```

**Beklenen sonuç:** `sdnn` = 36,0

### Adım 3.3: Gerçek bir 12 derivasyonlu EKG

**Amaç.** Akut miyokart enfarktüsü olan bir hastanın gerçek 12 derivasyonlu EKG'sini kâğıttaki gibi çizmek ve kalp hızını ölçmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: `ptb`, PTB Diagnostic ECG Database'deki 1 numaralı hastanın s0010_re kaydını içeren bir pandas
DataFrame'idir: 1000 Hz'de (`fs_ptb`) örneklenmiş 38,4 saniye; her derivasyon için bir sütun (i, ii,
iii, avr, avl, avf, v1-v6 ile üç Frank derivasyonu vx, vy ve vz), milivolt cinsinden. `header`,
başlık dosyasının metin satırlarının listesidir. Ders paketindeki
`measure.detect_r_peaks(signal, fs)`, tek bir derivasyonu NumPy dizisi olarak ve örnekleme
frekansını Hz cinsinden alır; R tepelerinin örnek numaralarını bir NumPy dizisi olarak döndürür.
Görev: header içinde "Reason for admission" ya da "Acute infarction" ile başlayan satırları yazdır.
On iki standart derivasyonun ilk 3 saniyesini, her panelde derivasyonun adı yazılı olacak biçimde üç
satır ve dört sütunluk bir ızgarada çiz. Ardından ii derivasyonunun R tepelerini
measure.detect_r_peaks ile bul ve kalp hızını 60'ın saniye cinsinden ortalama RR aralığına bölümü
olarak hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Dakikadaki atım sayısı cinsinden kalp hızı, bir ondalığa yuvarlanmış olarak. Sonucu `hr_ptb`
adlı bir değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Yazdırılan satırlar infero-lateral bir enfarktüs belirtmeli.
```

**Beklenen sonuç:** `hr_ptb` = 81,8

### Adım 3.4: Bir asistanın fonksiyonunu düzeltmek

**Amaç.** Bir YZ asistanı kısa bir prompttan bir QTc fonksiyonu yazdı ve olanaksız bir değer, 17 ms QTc döndürdü. İki hatayı bulmak ve düzeltmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
vclinic ders paketi, measure modülüyle birlikte içe aktarılmıştır. RANDOM_STATE = 2026'dır.
Veri: Asistanın fonksiyonu şudur: def qtc(qt_samples, rr_samples, fs=360): qt_ms = qt_samples / fs *
1000; rr_ms = rr_samples / fs * 1000; return qt_ms / rr_ms ** 0.5. 500 Hz'de 196 örneklik bir QT ve
353 örneklik bir RR aralığı ölçülmüştür.
Görev: fs'yi varsayılan değer olmadan alan, QT'yi milisaniyeye ve RR aralığını saniyeye çeviren ve
milisaniye cinsinden QT'nin saniye cinsinden RR aralığının kareköküne bölümünü döndüren, düzeltilmiş
bir qtc_bazett(qt_samples, rr_samples, fs) fonksiyonu yaz. Yukarıdaki ölçümün QTc değerini bu
fonksiyonla hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Milisaniye cinsinden QTc, bir ondalığa yuvarlanmış olarak. Sonucu `qtc_fixed` adlı bir
değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: qt_samples = 200, rr_samples = 500 ve fs = 500 iken sonuç 400 ms olmalı; çünkü RR aralığı bu
durumda 1 s'dir.
```

**Beklenen sonuç:** `qtc_fixed` = 466,5

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

### Test yazdırmak

```text
Aşağıdaki fonksiyon için, doğru sonucu elle hesaplanabilen girdilerle üç kısa test yaz; örneğin 60
bpm'lik kalp hızında RR aralığı tam 1 s'dir. Yalnızca assert ifadeleri kullan ve her testin hangi
hatayı yakaladığını açıkla.

[fonksiyonu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: measure_ecg fonksiyonuna frontal ekseni eklemek

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 5. bölümdeki `measure_ecg(leads, fs)` fonksiyonu ve yardımcı fonksiyonları `detect_r_peaks`
ile `qrs_bounds`. `vclinic.frontal_axis(v_i, v_avf)`, D1 ve aVF derivasyonlarının net QRS
voltajlarından frontal ekseni derece cinsinden döndürür.
Görev: `measure_ecg_axis(leads, fs)` adlı bir fonksiyon yaz: Fonksiyon `measure_ecg` ile aynı
sözlüğü, "axis_deg" anahtarı eklenmiş olarak döndürsün. Her atım için D1 ve aVF derivasyonlarının
net QRS voltajını, QRS başlangıcı ile sonu arasındaki en büyük pozitif ve en büyük negatif değerin
toplamı olarak al; değerleri QRS başlangıcından önceki 30 ms'nin ortancasına göre ölç. Bütün
atımlardaki değerlerin ortancalarını vclinic.frontal_axis fonksiyonuna ver.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Fonksiyon ve VC-0317 numaralı hasta için sonucu. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Kayıtta VC-0317'nin ekseni 21°'dir. Net voltajlar küçük septal ve terminal kuvvetleri de
içerdiği için ölçülen eksen bu değerden en çok 10° kadar sapabilir.
```

### Adım 2: Gerçek değere karşı on hasta

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: patient_id, ecg_rhythm ("sinus" ya da "AF") ve ecg_conduction ("normal", "LBBB" ya da "RBBB")
sütunlarını içeren `clinic` DataFrame'i. `vclinic.patient_ecg(clinic, patient_id)` bir EKG nesnesi
döndürür; bu nesneye `e` diyelim. `e.truth` sözlüğü "hr_bpm", "pr_ms", "qrs_ms", "qt_ms" ve
"axis_deg" anahtarlarını içerir.
Görev: En az ikisinde atriyal fibrilasyon ya da dal bloğu bulunan on hasta seç. Her hasta için
`measure_ecg_axis` fonksiyonunu çalıştır (atriyal fibrilasyonda `sinus=False` ile). Kalp hızı, PR,
QRS, QT ve eksen için ölçülen değeri, gerçek değeri ve aradaki farkı gösteren bir tablo oluştur.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Hasta başına bir satırı olan bir pandas DataFrame'i. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: Tabloda on satır olmalı; VC-0317'de PR, QRS ve QT farkları birkaç milisaniyeyi geçmemeli.
```

### Adım 3: İki gerçek kayıt

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 8. bölümden `leads_ptb` (PTB kaydının on iki derivasyonunu tutan NumPy dizisi) ve `fs_ptb`
(1000 Hz). 6. bölümden `found` (MIT-BIH 100 numaralı kayıtta bulunan R tepelerinin örnek konumları)
ve `fs_mit` (360 Hz).
Görev: `measure_ecg_axis` fonksiyonunu PTB kaydında çalıştır ve MIT-BIH 100 numaralı kaydın ortalama
kalp hızını bulunan atımlardan hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: PTB kaydının ölçümleri ve 100 numaralı kaydın ortalama kalp hızı. Yalnızca kodu, tek bir blok
olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: 8. bölümde PTB kaydı için kalp hızı 81,8 bpm, PR aralığı 225 ms, QRS süresi 137 ms ve QT 436,7
ms bulunmuştur.
```

### Adım 4: Her hasta için Bazett mi Fridericia mı?

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 2. adımdaki tablo (her hastanın ölçülen QT değeri ve kalp hızı) ve `clinic` tablosundaki
cinsiyet bilgisi.
Görev: Her hasta için QTc'yi Bazett ve Fridericia formülleriyle hesapla ve kadınlar için 460 ms,
erkekler için 450 ms eşiğiyle uzamış olup olmadığına karar ver. İki formülün farklı karar verdiği
hastaları listele.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: İki yeni sütun eklenmiş tablo ve iki formülün farklı karar verdiği hastaların listesi.
Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: 85 bpm kalp hızındaki bir kadın olan VC-0317'de QTc, Bazett formülüne göre uzamış, Fridericia
formülüne göre normal çıkmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
