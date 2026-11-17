# Prompt kütüphanesi, 1. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[1. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-01/PROMPTS.md)

Bu kütüphanede, 1. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın altındaki hücreye yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

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

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 1, 1. ve 2. bölümler*

Bir kliniğin hasta kaydı bir tablo olarak düşünülebilir: Her hasta bir satırda, her değişken bir sütunda yer alır. Bu durakta Cleveland verisindeki 303 hasta ile sanal kliniğin ilk 500 hastası bir ortalama, bir oran ve bir sayıyla özetlenmektedir. Bu sayıların her birinin ardında klinik bir soru vardır.

### Adım 1.1: Hastalığı olanların ortalama yaşı

**Amaç.** Bu adımda koroner arter hastalığı olan Cleveland hastalarının ortalama yaşı hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `heart`, UCI Heart Disease veri setinde Cleveland Clinic'ten gelen 303 hastayı tutan bir
tablodur ve her hasta bir satırda yer alır. Burada kullanılan sütunlar age (yaş, yıl), sex (erkekler
için 1, kadınlar için 0) ve disease sütunlarıdır. disease, anjiyografide en az bir büyük koroner
arterin çapı yüzde 50'den fazla daralmışsa 1, değilse 0 değerini alır.
Görev: Koroner arter hastalığı olan hastaları, yani disease sütunundaki değeri 1 olanları seç ve bu
hastaların ortalama yaşını hesapla. Kaç hasta seçildiğini de yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Ortalama yaşı yıl cinsinden ve bir ondalık basamağa yuvarlayarak ver. Sonucu `mean_age`
adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her
adımın üstüne kısa bir açıklama satırı ekle.
Test: Karşılaştırma için 303 hastanın tamamının ortalama yaşını da yazdır. Bu değer 54,4 yıldır ve
hastalığı olanların ortalaması ondan farklı olmalıdır.
```

**Beklenen sonuç:** `mean_age` = 56,6

### Adım 1.2: Kadınların oranı

**Amaç.** Bu adımda Cleveland hastaları arasında kadınların oranı bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `heart`, UCI Heart Disease veri setinde Cleveland Clinic'ten gelen 303 hastayı tutan bir
tablodur ve her hasta bir satırda yer alır. Burada kullanılan sütunlar age (yaş, yıl), sex (erkekler
için 1, kadınlar için 0) ve disease sütunlarıdır. disease, anjiyografide en az bir büyük koroner
arterin çapı yüzde 50'den fazla daralmışsa 1, değilse 0 değerini alır.
Görev: Kadınları, yani sex sütunundaki değeri 0 olan hastaları say ve bu sayıyı bütün hastaların
sayısına böl. Erkeklerin oranını da yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Kadınların oranını yüzde olarak ve bir ondalık basamağa yuvarlayarak ver. Sonucu `pct_women`
adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her
adımın üstüne kısa bir açıklama satırı ekle.
Test: Kadınların ve erkeklerin oranlarının toplamı yüzde 100 etmelidir.
```

**Beklenen sonuç:** `pct_women` = 32,0

### Adım 1.3: Sanal klinikte HFrEF hastaları

**Amaç.** Bu adımda sanal klinikteki düşük ejeksiyon fraksiyonlu kalp yetersizliği (HFrEF) hastaları sayılır ve her tanının ejeksiyon fraksiyonu tek bir şekilde gösterilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `clinic`, sanal kliniğin ilk 500 sentetik hastasını tutan bir tablodur ve her hasta bir
satırda yer alır. Burada kullanılan sütunlar şunlardır: patient_id; "none" (tanı yok), "CCS" (kronik
koroner sendrom), "ACS" (akut koroner sendrom), "HFrEF" (düşük ejeksiyon fraksiyonlu kalp
yetersizliği) ya da "HFpEF" (korunmuş ejeksiyon fraksiyonlu kalp yetersizliği) değerini alan
main_diagnosis; yüzde cinsinden sol ventrikül ejeksiyon fraksiyonunu veren lvef.
Görev: Ana tanısı "HFrEF" olan hastaları say. Ardından her ana tanı için ejeksiyon fraksiyonunun
(lvef) kutu grafiğini çiz; yatay eksende tanılar, dikey eksende yüzde cinsinden ejeksiyon fraksiyonu
yer alsın.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: HFrEF hastalarının sayısını tam sayı olarak ver. Sonucu `n_hfref` adıyla sakla ve kısa bir
açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir
açıklama satırı ekle.
Test: Her tanıdaki hasta sayısını da yazdır; beş sayının toplamı 500 etmelidir.
```

**Beklenen sonuç:** `n_hfref` = 47

## Durak 2: Veri olarak EKG

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-2) · Python yolunda aynı sonuç: 3-5. bölümler*

Dijital bir EKG de bir sayı tablosudur: Her derivasyon bir sütunda, her örnek bir satırda yer alır. Bu durakta haftanın vakası olan VC-0317 numaralı hastanın 12 derivasyonlu EKG'si çizilip ölçülür; başka bir hastanın QT aralığı da iki formülle kalp hızına göre düzeltilir.

### Adım 2.1: Bir D2 şeridi

**Amaç.** Bu adımda D2 derivasyonunun ilk 2,5 saniyesi çizilir ve böyle bir şeridin kaç sayıdan oluştuğu görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `case`, sanal klinikteki VC-0317 numaralı hastanın 10 saniyelik, 12 derivasyonlu istirahat
EKG'sini tutar. `case.fs` örnekleme frekansıdır; kayıt saniyede 500 örnekle alınmıştır. `case.leads`
ise her derivasyon (I, II, III, aVR, aVL, aVF, V1-V6) için bir sütun ve her örnek için bir satır
içeren, milivolt cinsinden bir tablodur.
Görev: Vakanın D2 derivasyonunu al ve ilk 2,5 saniyesini ayır; bu sürenin içindeki örnek sayısı
örnekleme frekansının 2,5 katıdır. Bu bölümü, yatay eksende saniye cinsinden zaman, dikey eksende
milivolt cinsinden gerilim olacak biçimde çiz.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: 2,5 saniyedeki örnek sayısını tam sayı olarak ver. Sonucu `n_samples` adıyla sakla ve kısa
bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa
bir açıklama satırı ekle.
Test: Grafiğin zaman ekseni 2,5 saniyede bitmelidir.
```

**Beklenen sonuç:** `n_samples` = 1250

### Adım 2.2: R tepelerinden kalp hızı

**Amaç.** Bu adımda D2 derivasyonunun R tepeleri bulunur ve aralarındaki sürelerden kalp hızı hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `case`, sanal klinikteki VC-0317 numaralı hastanın 10 saniyelik, 12 derivasyonlu istirahat
EKG'sini tutar. `case.fs` örnekleme frekansıdır; kayıt saniyede 500 örnekle alınmıştır. `case.leads`
ise her derivasyon (I, II, III, aVR, aVL, aVF, V1-V6) için bir sütun ve her örnek için bir satır
içeren, milivolt cinsinden bir tablodur. Ders paketinde hazır bir R tepesi bulucusu vardır:
`measure.detect_r_peaks`. Bu araç bir derivasyonu ve örnekleme frekansını alır; R tepelerinin
yerlerini örnek numarası olarak döndürür.
Görev: Ders paketindeki R tepesi bulucusuyla D2 derivasyonunun tamamındaki R tepelerini bul. Ardışık
tepeler arasındaki uzaklıkları örnekleme frekansına bölerek saniyeye çevir. Kalp hızı, 60'ın saniye
cinsinden ortalama RR aralığına bölümüdür.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Kalp hızını dakikadaki atım sayısı olarak ve bir ondalık basamağa yuvarlayarak ver; R
tepelerinin sayısını da yazdır. Sonucu `hr_bpm` adıyla sakla ve kısa bir açıklamayla birlikte
yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: 10 saniyelik kayıtta yaklaşık 14 R tepesi bulunmalıdır.
```

**Beklenen sonuç:** `hr_bpm` = 84,9

### Adım 2.3: İki formülle QTc

**Amaç.** Bu adımda VC-0254 numaralı hastanın QT aralığı, yüksek kalp hızına göre Fridericia ve Bazett formülleriyle düzeltilir ve iki sonuç karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: Sanal kliniğin kaydında VC-0254 numaralı hastanın QT aralığı 343 ms, kalp hızı dakikada 98
atımdır.
Görev: RR aralığını saniye cinsinden, 60'ın kalp hızına bölümü olarak hesapla. Ardından düzeltilmiş
QT aralığını (QTc) iki formülle hesapla: Fridericia formülü QT'yi RR'nin küp köküne, Bazett formülü
ise RR'nin kareköküne böler.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Fridericia formülüyle bulunan QTc'yi milisaniye cinsinden ve bir ondalık basamağa
yuvarlayarak ver; Bazett formülünün sonucunu da yazdır. Sonucu `qtc_fridericia` adıyla sakla ve kısa
bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa
bir açıklama satırı ekle.
Test: Dakikada 60 atımlık kalp hızında iki formül de QT'nin kendisini vermelidir.
```

**Beklenen sonuç:** `qtc_fridericia` = 403,9

## Durak 3: Gerçek kayıtlar ve denetlenecek bir fonksiyon

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-3) · Python yolunda aynı sonuç: 6-9. bölümler*

Gerçek kayıtlar kendi gürültüsü, işaretlemeleri ve birimleriyle gelir. Bu durakta MIT-BIH Aritmi Veri Tabanı'ndaki 100 numaralı kayıt, kardiyologların verdiği atım etiketleriyle birlikte okunur ve normal atımlardan kalp hızı değişkenliği hesaplanır. Ardından PTB veri tabanındaki gerçek bir 12 derivasyonlu EKG çizilir; son olarak bir YZ asistanının yazdığı QTc fonksiyonu denetlenip düzeltilir.

### Adım 3.1: 100 numaralı kaydın atımları

**Amaç.** Bu adımda 30 dakikalık bir kaydın atımları, kardiyologların onlara verdiği etiketlere göre sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `ann_symbols`, MIT-BIH Aritmi Veri Tabanı'ndaki 100 numaralı kayda kardiyologların verdiği
etiketlerin zaman sırasına göre dizilmiş listesidir. N normal atımı, A atriyal erken atımı, V
ventriküler erken atımı, + ise bir ritim değişikliğini gösterir; sonuncusu bir atım değildir.
`ann_samples` her etiketin yerini örnek numarası olarak tutar. `fs_mit` örnekleme frekansını tutar:
Saniyede 360 örnek.
Görev: ann_symbols listesinde her etiketin kaç kez geçtiğini say ve sayıları yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Atriyal erken atımların (A etiketi) sayısını tam sayı olarak ver. Sonucu `n_apb` adıyla sakla
ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne
kısa bir açıklama satırı ekle.
Test: N, A ve V etiketlerinin toplamı 2.273 atım olmalıdır.
```

**Beklenen sonuç:** `n_apb` = 33

### Adım 3.2: Kalp hızı değişkenliği: SDNN

**Amaç.** Bu adımda normal atımlar arasındaki sürelerin 30 dakika boyunca ne kadar değiştiği ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `ann_symbols`, MIT-BIH Aritmi Veri Tabanı'ndaki 100 numaralı kayda kardiyologların verdiği
etiketlerin zaman sırasına göre dizilmiş listesidir. N normal atımı, A atriyal erken atımı, V
ventriküler erken atımı, + ise bir ritim değişikliğini gösterir; sonuncusu bir atım değildir.
`ann_samples` her etiketin yerini örnek numarası olarak tutar. `fs_mit` örnekleme frekansını tutar:
Saniyede 360 örnek.
Görev: Yalnızca atım olan etiketleri, yani + dışındaki bütün etiketleri tut. Atımların yerlerinden
ve örnekleme frekansından ardışık atımlar arasındaki RR aralıklarını milisaniye cinsinden hesapla.
Bunlardan yalnızca iki ucu da normal atım (N) olan aralıkları, yani NN aralıklarını tut. SDNN, NN
aralıklarının standart sapmasıdır; bu sapmayı bir örneklem için olduğu gibi, paydada aralık
sayısının bir eksiğini kullanarak hesapla. Ortalama NN aralığını da yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: SDNN değerini milisaniye cinsinden ve bir ondalık basamağa yuvarlayarak ver. Sonucu `sdnn`
adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her
adımın üstüne kısa bir açıklama satırı ekle.
Test: Ortalama NN aralığı 700 ile 900 ms arasında olmalıdır.
```

**Beklenen sonuç:** `sdnn` = 36,0

### Adım 3.3: Gerçek bir 12 derivasyonlu EKG

**Amaç.** Bu adımda akut miyokard enfarktüsü geçiren bir hastanın gerçek 12 derivasyonlu EKG'si, EKG kâğıdındaki düzende çizilir ve kalp hızı ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: `ptb`, PTB Tanısal EKG Veri Tabanı'ndaki 1 numaralı hastanın s0010_re kaydını tutan bir
tablodur. Kayıt 38,4 saniye sürer ve saniyede 1.000 örnekle (`fs_ptb`) alınmıştır; her derivasyon
(i, ii, iii, avr, avl, avf, v1-v6 ve üç Frank derivasyonu vx, vy, vz) milivolt cinsinden bir sütunda
yer alır. `header`, kaydın başlık dosyasındaki metin satırlarının listesidir. Ders paketinde hazır
bir R tepesi bulucusu vardır: `measure.detect_r_peaks`. Bu araç bir derivasyonu ve örnekleme
frekansını alır; R tepelerinin yerlerini örnek numarası olarak döndürür.
Görev: Önce header listesinde "Reason for admission" ya da "Acute infarction" ile başlayan satırları
yazdır. Ardından on iki standart derivasyonun ilk 3 saniyesini üç satır ve dört sütunluk bir düzende
çiz; her panelin üstünde derivasyonun adı yazsın. Son olarak ders paketindeki R tepesi bulucusuyla
ii derivasyonunun R tepelerini bul ve kalp hızını, 60'ın saniye cinsinden ortalama RR aralığına
bölümü olarak hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Kalp hızını dakikadaki atım sayısı olarak ve bir ondalık basamağa yuvarlayarak ver. Sonucu
`hr_ptb` adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde
ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Yazdırılan satırlarda infero-lateral bir enfarktüs belirtilmelidir.
```

**Beklenen sonuç:** `hr_ptb` = 81,8

### Adım 3.4: Bir asistanın fonksiyonunu düzeltmek

**Amaç.** Bir YZ asistanı kısa bir prompttan QTc hesaplayan bir fonksiyon yazmış ve 17 ms gibi olanaksız bir sonuç vermiştir. Bu adımda iki hata bulunup düzeltilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin ve measure modülüyle birlikte vclinic ders paketinin önceden
yüklendiği 1. hafta Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için kullanılan
paketler (pandas, NumPy ve Matplotlib) hazırdır.
Veri: Asistanın fonksiyonu şudur: def qtc(qt_samples, rr_samples, fs=360): qt_ms = qt_samples / fs *
1000; rr_ms = rr_samples / fs * 1000; return qt_ms / rr_ms ** 0.5. Saniyede 500 örnekle kaydedilmiş
bir EKG'de QT 196 örnek, RR aralığı 353 örnek olarak ölçülmüştür.
Görev: qtc_bazett adlı, düzeltilmiş bir fonksiyon yaz. Fonksiyon QT'yi ve RR aralığını örnek sayısı
olarak, örnekleme frekansını da ayrıca alsın; frekans her zaman verilmeli, hiçbir zaman
varsayılmamalıdır. Fonksiyon QT'yi milisaniyeye, RR aralığını saniyeye çevirsin ve Bazett QTc'sini,
yani milisaniye cinsinden QT'nin saniye cinsinden RR aralığının kareköküne bölümünü döndürsün.
Ardından yukarıdaki ölçümün QTc değerini bu fonksiyonla hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: QTc'yi milisaniye cinsinden ve bir ondalık basamağa yuvarlayarak ver. Sonucu `qtc_fixed`
adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her
adımın üstüne kısa bir açıklama satırı ekle.
Test: Saniyede 500 örnekle QT 200 örnek, RR aralığı 500 örnek olduğunda fonksiyon 400 ms vermelidir;
çünkü bu durumda RR aralığı tam olarak 1 saniyedir.
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
Aşağıdaki fonksiyon için doğru sonucu elle hesaplanabilen girdilerle üç kısa test yaz; örneğin
dakikada 60 atımlık kalp hızında RR aralığı tam olarak 1 saniyedir. Her test, sonuç yanlışsa kodu
açık bir mesajla durdurmalıdır. Her testin hangi hatayı yakaladığını bir cümleyle açıkla.

[fonksiyonu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: measure_ecg fonksiyonuna frontal ekseni eklemek

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 1. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy ve Matplotlib) ile vclinic ders paketi hazırdır.
Veri: 5. bölümdeki measure_ecg ölçüm aracı ile R tepelerini ve QRS kompleksinin sınırlarını bulan
yardımcı araçları. Ders paketindeki vclinic.frontal_axis aracı, I ve aVF derivasyonlarının net QRS
gerilimlerinden derece cinsinden frontal QRS eksenini verir.
Görev: measure_ecg'nin döndürdüğü her şeyi ve ek olarak axis_deg adıyla derece cinsinden frontal
ekseni döndüren measure_ecg_axis adlı yeni bir ölçüm aracı yaz. Her atım için I ve aVF
derivasyonlarının net QRS gerilimini bul: QRS başlangıcı ile sonu arasındaki en büyük pozitif ve en
büyük negatif değerin toplamı. Bu değerleri, başlangıçtan önceki 30 ms'nin ortanca gerilimine göre
ölç. Bütün atımların ortancalarını vclinic.frontal_axis aracına ver.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Yeni aracı ve VC-0317 numaralı hasta için verdiği sonucu göster. Yalnızca kodu tek bir blok
hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Kayıtta VC-0317 için eksen 21 derecedir. Ölçülen eksen bu değerin yaklaşık 10 derece yakınında
olmalıdır; çünkü net gerilimler küçük septal ve terminal kuvvetleri de içerir.
```

### Adım 2: Gerçek değere karşı on hasta

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 1. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy ve Matplotlib) ile vclinic ders paketi hazırdır.
Veri: clinic tablosunda patient_id, ecg_rhythm ("sinus" ya da "AF") ve ecg_conduction ("normal",
"LBBB" ya da "RBBB") sütunları bulunur. Bir hastanın EKG'sini vclinic ders paketinin patient_ecg
aracı verir; bu araç clinic tablosunu ve hastanın numarasını alır. EKG'nin truth bölümü gerçek kalp
hızını, PR aralığını, QRS süresini, QT aralığını ve ekseni tutar.
Görev: En az ikisinde atriyal fibrilasyon ya da dal bloğu bulunan on hasta seç. Her birini
measure_ecg_axis ile ölç; atriyal fibrilasyonu olan hastalarda araca ritmin sinüs olmadığını bildir.
Kalp hızı, PR aralığı, QRS süresi, QT aralığı ve eksen için ölçülen değeri, gerçek değeri ve
ikisinin farkını gösteren bir tablo oluştur.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Her hasta için bir satır içeren bir tablo göster. Yalnızca kodu tek bir blok hâlinde ver ve
her adımın üstüne kısa bir açıklama satırı ekle.
Test: Tabloda on satır bulunmalı; VC-0317 için PR, QRS ve QT farkları yalnızca birkaç milisaniye
olmalıdır.
```

### Adım 3: İki gerçek kayıt

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 1. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy ve Matplotlib) ile vclinic ders paketi hazırdır.
Veri: 8. bölümden PTB kaydının on iki derivasyonu (leads_ptb) ve saniyede 1.000 örneklik örnekleme
frekansı (fs_ptb). 6. bölümden MIT-BIH veri tabanındaki 100 numaralı kaydın örnek numarası olarak
bulunmuş R tepeleri (found) ve saniyede 360 örneklik örnekleme frekansı (fs_mit).
Görev: PTB kaydını measure_ecg_axis ile ölç ve MIT-BIH veri tabanındaki 100 numaralı kaydın ortalama
kalp hızını bulunan atımlardan hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: PTB kaydının ölçümlerini ve 100 numaralı kaydın ortalama kalp hızını göster. Yalnızca kodu
tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: 8. bölüm, PTB kaydı için dakikada 81,8 atımlık kalp hızı, 225 ms'lik PR aralığı, 137 ms'lik
QRS süresi ve 436,7 ms'lik QT bildirmektedir.
```

### Adım 4: Her hasta için Bazett mi Fridericia mı?

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 1. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy ve Matplotlib) ile vclinic ders paketi hazırdır.
Veri: 2. adımdaki, her hastanın ölçülen QT değerini ve kalp hızını içeren tablo ile clinic
tablosundan her hastanın cinsiyeti.
Görev: Her hasta için QTc'yi Bazett ve Fridericia formülleriyle hesapla; kadınlarda 460 ms,
erkeklerde 450 ms sınırına göre uzun olup olmadığına karar ver. İki formülün farklı sonuç verdiği
hastaları listele.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: İki yeni sütunuyla tabloyu ve uyuşmazlıkların listesini göster. Yalnızca kodu tek bir blok
hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Dakikada 85 atımlık kalp hızıyla bir kadın olan VC-0317, Bazett formülüne göre uzun,
Fridericia formülüne göre normaldir.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
