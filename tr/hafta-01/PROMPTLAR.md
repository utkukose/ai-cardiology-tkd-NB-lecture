# Prompt kütüphanesi, 1. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[1. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-01/PROMPTS.md)

Bu kütüphanede, 1. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Mini proje: Kaggle Heart Disease veri seti](#durak-1-mini-proje-kaggle-heart-disease-veri-seti)
3. [Durak 2: Veri olarak EKG](#durak-2-veri-olarak-ekg)
4. [Durak 3: Gerçek kayıtlar ve özensiz bir prompt](#durak-3-gerçek-kayıtlar-ve-özensiz-bir-prompt)
5. [Kodu onarmak, açıklatmak ve denetlemek için promptlar](#kodu-onarmak-açıklatmak-ve-denetlemek-için-promptlar)
6. [Haftalık projenin prompt yolu](#haftalık-projenin-prompt-yolu)

## Bir adım nasıl ilerler?

| Adım | Ne yapılır? |
|---|---|
| 1. Okuyun | Defterde adımın amacını okuyun. |
| 2. Veriyi hazırlayın | Promptun altındaki veri hücresini çalıştırın. Hücre, promptun tarif ettiği "veri" tablosunu hazırlar ve gösterir. |
| 3. Kopyalayın ve gönderin | Promptu kopyalayın ve bir YZ asistanına gönderin: Google Colab'daki Gemini ya da başka bir tarayıcı sekmesindeki ChatGPT, Claude, Copilot veya Gemini. |
| 4. Çalıştırın | Asistanın kodunu veri hücresinin altındaki hücreye yapıştırın ve çalıştırın. |
| 5. Denetleyin | Kontrol hücresini çalıştırın. Hücre *doğru* ya da *henüz değil* yazar ve "cevap" sonucunun değerini gösterir. |
| 6. Onarın | Kontrol *henüz değil* yazarsa onarım promptunu kodla birlikte gönderin. Sonuç yine yanlışsa doğru sonucu veren *Hazır kod* hücresini çalıştırın. |
| 7. Açıklatın ve kaydedin | Asistandan kodu sade bir dille açıklamasını isteyin; aracı, promptu ve neyin denetlendiğini YZ kullanım günlüğüne yazın. |

## Durak 1: Mini proje: Kaggle Heart Disease veri seti

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 1, 1. ve 2. bölümler*

Bu durak oturumun mini projesidir: UCI Heart Disease koleksiyonunun Cleveland verisi olan Kaggle Heart Disease veri seti yüklenir, istatistiksel olarak özetlenir ve görselleştirilir. Bir kliniğin hasta kaydı bir tablo olarak düşünülebilir: Her hasta bir satırda, her değişken bir sütunda yer alır. Bu durakta veri setindeki 303 hasta ile sanal kliniğin ilk 500 hastası bir ortalama, bir oran ve bir sayıyla özetlenmektedir. Bu sayıların her birinin ardında klinik bir soru vardır.

### Adım 1.1: Hastalığı olanların ortalama yaşı

**Amaç.** Bu adımda koroner arter hastalığı olan Cleveland hastalarının ortalama yaşı hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Cleveland Clinic'te koroner anjiyografi yapılmış 303 hastada, koroner arter hastalığı
olanların ortalama yaşını öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "yaş" sütunu hastanın yaşını yıl
olarak verir. "KAH" sütununda, anjiyografide en az bir büyük koroner arterinin çapı yüzde 50'den
fazla daralmış hastalar için "var", diğer hastalar için "yok" yazar.
Görev: Koroner arter hastalığı olan hastaları seç ve ortalama yaşlarını hesapla. Kaç hasta
seçildiğini de yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ortalama yaşı yıl olarak, bir ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Karşılaştırma için bütün hastaların ortalama yaşını da yazdır; bu değer 54,4 yıl olmalı.
Hastalığı olanların ortalaması bundan farklı çıkmalı.
```

**Beklenen sonuç:** "cevap" = 56,6

### Adım 1.2: Kadınların oranı

**Amaç.** Bu adımda Cleveland hastaları arasında kadınların oranı bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Cleveland Clinic'te koroner anjiyografi yapılmış 303 hastanın yüzde kaçının kadın olduğunu
öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "yaş" sütunu hastanın yaşını yıl
olarak verir; "cinsiyet" sütununda "kadın" ya da "erkek" yazar.
Görev: Kadın hastaların sayısını bütün hastaların sayısına böl ve sonucu yüzde olarak ifade et.
Erkeklerin yüzdesini de aynı yolla hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kadınların yüzdesini bir ondalık basamakla yazdır ve "cevap" adıyla sakla. Erkeklerin
yüzdesini de yazdır.
Test: Kadınların ve erkeklerin yüzdelerinin toplamı 100 olmalı.
```

**Beklenen sonuç:** "cevap" = 32,0

### Adım 1.3: Sanal klinikte HFrEF hastaları

**Amaç.** Bu adımda sanal klinikteki düşük ejeksiyon fraksiyonlu kalp yetersizliği (HFrEF) hastaları sayılır ve her tanının ejeksiyon fraksiyonu tek bir şekilde gösterilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal kliniğin 500 sentetik hastasında düşük ejeksiyon fraksiyonlu kalp yetersizliği (HFrEF)
olanları saymak ve ejeksiyon fraksiyonunun tanılara göre nasıl değiştiğini görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "hasta" sütunu hastanın
numarasını, "ana tanı" sütunu ana tanıyı, "LVEF" sütunu da sol ventrikül ejeksiyon fraksiyonunu
yüzde olarak verir. Ana tanı şu değerlerden biridir: "yok" (tanı yok), "CCS" (kronik koroner
sendrom), "ACS" (akut koroner sendrom), "HFrEF" (düşük ejeksiyon fraksiyonlu kalp yetersizliği) ve
"HFpEF" (korunmuş ejeksiyon fraksiyonlu kalp yetersizliği).
Görev: Ana tanısı HFrEF olan hastaları say. Ardından her ana tanı için ejeksiyon fraksiyonunun kutu
grafiğini çiz; tanılar yatay eksende, yüzde cinsinden ejeksiyon fraksiyonu dikey eksende yer alsın.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: HFrEF hastalarının sayısını yazdır ve "cevap" adıyla sakla. Grafiği de göster.
Test: Her tanıdaki hasta sayısını da yazdır; beş sayının toplamı 500 olmalı. Hiçbir HFrEF hastasının
ejeksiyon fraksiyonu yüzde 40'ı geçmemeli.
```

**Beklenen sonuç:** "cevap" = 47

## Durak 2: Veri olarak EKG

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-2) · Python yolunda aynı sonuç: 3-5. bölümler*

Dijital bir EKG de bir sayı tablosudur: Her derivasyon bir sütunda, her örnek bir satırda yer alır. Bu durakta haftanın vakası olan VC-0317 numaralı hastanın EKG'sinden D2 derivasyonu çizilir ve ölçülür; başka bir hastanın QT aralığı da iki formülle kalp hızına göre düzeltilir.

### Adım 2.1: Bir D2 şeridi

**Amaç.** Bu adımda D2 derivasyonunun ilk 2,5 saniyesi çizilir ve böyle bir şeridin kaç sayıdan oluştuğu görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: 67 yaşında bir kadın hastanın 10 saniyelik istirahat EKG'sinden D2 derivasyonunun ilk 2,5
saniyesini görmek ve bu kısa şeridin kaç örnekten oluştuğunu öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kaydın bir anıdır: "zaman" sütunu saniyeyi,
"D2" sütunu D2 derivasyonundaki gerilimi milivolt olarak verir. Kayıt saniyede 500 kez
örneklenmiştir.
Görev: Zamanı 2,5 saniyeden küçük olan satırları ayır ve say. Bu bölümü, yatay eksende saniye
cinsinden zaman, dikey eksende milivolt cinsinden gerilim olacak biçimde çiz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Bu 2,5 saniyedeki örnek sayısını yazdır ve "cevap" adıyla sakla. Grafiği de göster.
Test: Grafiğin zaman ekseni 0'da başlamalı ve 2,5 saniyede bitmeli.
```

**Beklenen sonuç:** "cevap" = 1250

### Adım 2.2: R tepelerinden kalp hızı

**Amaç.** Bu adımda D2 derivasyonunun R tepeleri bulunur ve aralarındaki sürelerden kalp hızı hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: 67 yaşında bir kadın hastanın 10 saniyelik istirahat EKG'sinden kalp hızını ölçmek
istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kaydın bir anıdır: "zaman" sütunu saniyeyi,
"D2" sütunu D2 derivasyonundaki gerilimi milivolt olarak verir. Kayıt saniyede 500 kez
örneklenmiştir.
Görev: R tepelerini bul. En yüksek değerin yarısını aşan ve birbirinden en az 0,3 saniye uzakta
duran tepeleri R tepesi kabul et. Ardışık R tepeleri arasındaki ortalama süreden kalp hızını
dakikadaki atım sayısı olarak hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kalp hızını bir ondalık basamakla yazdır ve "cevap" adıyla sakla. D2 derivasyonunu, R
tepeleri işaretli olarak çiz.
Test: 10 saniyede yaklaşık 14 R tepesi bulunmalı; kalp hızı dakikada 40 ile 150 atım arasında
olmalı.
```

**Beklenen sonuç:** "cevap" = 84,9

### Adım 2.3: İki formülle QTc

**Amaç.** Bu adımda VC-0254 numaralı hastanın QT aralığı, yüksek kalp hızına göre Fridericia ve Bazett formülleriyle düzeltilir ve iki sonuç karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kalp hızı yüksek olan 58 yaşında bir erkek hastanın QT aralığını iki formülle düzeltmek ve
sonuçları karşılaştırmak istiyorum.
Veri: Defterde "veri" adında tek satırlık bir tablo var: "hasta" sütunu hastanın numarasını, "kalp
hızı" sütunu dakikadaki atım sayısını, "QT" sütunu da QT aralığını milisaniye olarak verir.
Görev: RR aralığını saniye olarak, 60'ın kalp hızına bölümüyle hesapla. Ardından QT aralığını iki
formülle düzelt: Fridericia formülü QT'yi RR'nin küp köküne, Bazett formülü ise RR'nin kareköküne
böler.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Fridericia formülüyle bulunan QTc'yi milisaniye olarak, bir ondalık basamakla yazdır ve
"cevap" adıyla sakla. Bazett formülünün sonucunu da yazdır.
Test: Kalp hızı dakikada 60 atım olduğunda iki formül de QT'nin kendisini vermeli.
```

**Beklenen sonuç:** "cevap" = 403,9

## Durak 3: Gerçek kayıtlar ve özensiz bir prompt

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-3) · Python yolunda aynı sonuç: 6-9. bölümler*

Gerçek kayıtlar kendi gürültüsü, işaretlemeleri ve birimleriyle gelir. Bu durakta MIT-BIH Aritmi Veri Tabanı'ndaki 100 numaralı kayıt, kardiyologların verdiği atım etiketleriyle birlikte okunur ve normal atımlardan kalp hızı değişkenliği hesaplanır. Ardından PTB veri tabanındaki gerçek bir 12 derivasyonlu EKG çizilir. Son olarak, bir YZ asistanının kısa ve özensiz bir prompttan yazdığı QTc hesabı prompt kartıyla yeniden istenir ve sonucu denetlenir.

### Adım 3.1: 100 numaralı kaydın atımları

**Amaç.** Bu adımda 30 dakikalık bir kaydın atımları, kardiyologların onlara verdiği etiketlere göre sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: MIT-BIH Aritmi Veri Tabanı'ndaki 100 numaralı kayıt, 69 yaşında bir erkeğin 30 dakikalık
ambulatuvar EKG kaydıdır. Bu kayıttaki atımları, kardiyologların onlara verdiği etiketlere göre
saymak istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır, kardiyologların kayda koyduğu bir işarettir:
"zaman" sütunu işaretin yerini saniye olarak, "etiket" sütunu da türünü verir. "N" normal atımı, "A"
atriyal erken atımı, "V" ventriküler erken atımı gösterir; "+" ise ritim değişikliğini belirtir ve
bir atım değildir.
Görev: Her etiketin kaç kez geçtiğini say ve sayıları yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Atriyal erken atımların sayısını yazdır ve "cevap" adıyla sakla.
Test: N, A ve V etiketlerinin toplamı 2.273 atım olmalı.
```

**Beklenen sonuç:** "cevap" = 33

### Adım 3.2: Kalp hızı değişkenliği: SDNN

**Amaç.** Bu adımda normal atımlar arasındaki sürelerin 30 dakika boyunca ne kadar değiştiği ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: MIT-BIH Aritmi Veri Tabanı'ndaki 100 numaralı kayıtta, yani 69 yaşında bir erkeğin 30
dakikalık ambulatuvar EKG'sinde, kalp hızı değişkenliğini SDNN ile ölçmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır, kardiyologların kayda koyduğu bir işarettir:
"zaman" sütunu işaretin yerini saniye olarak, "etiket" sütunu da türünü verir. "N" normal atımı, "A"
atriyal erken atımı, "V" ventriküler erken atımı gösterir; "+" ise ritim değişikliğini belirtir ve
bir atım değildir.
Görev: Yalnızca atımları, yani "+" dışındaki etiketleri tut. Ardışık atımlar arasındaki RR
aralıklarını milisaniye olarak hesapla. Bunlardan yalnızca iki ucu da normal atım ("N") olan
aralıkları, yani NN aralıklarını kullan. SDNN, NN aralıklarının standart sapmasıdır; bu sapmayı bir
örneklem için olduğu gibi, paydada aralık sayısının bir eksiğiyle hesapla. Ortalama NN aralığını da
yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: SDNN değerini milisaniye olarak, bir ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Ortalama NN aralığı 700 ile 900 ms arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 36,0

### Adım 3.3: Gerçek bir 12 derivasyonlu EKG

**Amaç.** Bu adımda akut miyokard enfarktüsü geçiren bir hastanın gerçek 12 derivasyonlu EKG'si, EKG kâğıdındaki düzende çizilir ve kalp hızı ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Akut infero-lateral miyokard enfarktüsüyle yatırılmış 81 yaşında bir kadın hastanın gerçek
12 derivasyonlu EKG'sini kâğıttaki düzende görmek ve kalp hızını ölçmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kaydın bir anıdır: "zaman" sütunu saniyeyi;
"D1", "D2", "D3", "aVR", "aVL", "aVF" ve "V1"-"V6" sütunları da on iki standart derivasyondaki
gerilimi milivolt olarak verir. Kayıt 38,4 saniye sürer ve saniyede 1.000 kez örneklenmiştir.
Görev: On iki derivasyonun ilk 3 saniyesini EKG kâğıdındaki gibi üç satır ve dört sütun hâlinde çiz:
Birinci sütunda D1, D2 ve D3; ikincide aVR, aVL ve aVF; üçüncüde V1-V3; dördüncüde V4-V6 yer alsın
ve her panelin üstünde derivasyonun adı yazsın. Ardından D1 derivasyonunda R tepelerini bul. En
yüksek değerin yarısını aşan ve birbirinden en az 0,3 saniye uzakta duran tepeleri R tepesi kabul
et. Ardışık R tepeleri arasındaki ortalama süreden kalp hızını dakikadaki atım sayısı olarak
hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kalp hızını bir ondalık basamakla yazdır ve "cevap" adıyla sakla. Şekli de göster.
Test: Kalp hızı dakikada 40 ile 150 atım arasında olmalı ve R tepelerinin sayısı bu hızla uyumlu
olmalı: Dakikada 80 atımla 38,4 saniyede yaklaşık 51 atım bulunur.
```

**Beklenen sonuç:** "cevap" = 81,8

### Adım 3.4: Özensiz bir prompttan prompt kartına

**Amaç.** Bir YZ asistanı, "örnek sayısı olarak verilen qt ve rr'den qtc veren bir python fonksiyonu yaz" biçimindeki kısa prompta karşılık 17 ms gibi olanaksız bir QTc veren bir kod yazmıştır. Bu adımın veri hücresi bu sonucu da göstermektedir. Bu adımda aynı hesap, prompt kartının yedi alanıyla yeniden istenir ve sonuç denetlenir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Saniyede 500 kez örneklenmiş bir EKG'de QT ve RR aralıkları örnek sayısı olarak ölçüldü.
Bazett yöntemiyle düzeltilmiş QT aralığını milisaniye olarak bulmak istiyorum.
Veri: Defterde "veri" adında tek satırlık bir tablo var: "QT" sütunu QT aralığını, "RR" sütunu RR
aralığını örnek sayısı olarak verir. Kayıt saniyede 500 kez örneklenmiştir.
Görev: QT aralığını milisaniyeye, RR aralığını saniyeye çevir. QT'yi Bazett yöntemiyle düzelt:
Milisaniye cinsinden QT'yi, saniye cinsinden RR aralığının kareköküne böl.
Kısıtlar: Yalnızca bu tabloyu kullan. Saniyedeki örnek sayısını kendin varsayma; burada verilen 500
değerini kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve program kurmamalıdır.
Çıktı: Düzeltilmiş QT'yi milisaniye olarak, bir ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Aynı hesap, QT 200 örnek ve RR 500 örnek olduğunda tam 400 ms vermeli; çünkü bu durumda RR
aralığı tam 1 saniyedir.
```

**Beklenen sonuç:** "cevap" = 466,5

## Kodu onarmak, açıklatmak ve denetlemek için promptlar

Bu promptlar her adımın koduyla kullanılabilir. Köşeli parantez içindeki yerler, prompt gönderilmeden önce doldurulur.

### Çalışan ama kontrolden geçmeyen kodu onarmak

```text
Aşağıdaki kod şu görev için yazıldı: [promptun Görev satırını yapıştırın]. Kod çalışıyor, ancak
dersin kontrolü "henüz değil" yazıyor. Hatayı bul, iki cümleyle açıkla ve düzeltilmiş kodu ver.
Sonuç yine "cevap" adıyla saklanmalı.

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
Aşağıdaki kodu, kod yazmayan bir hekim için satır satır açıkla. Ardından kodun hata mesajı vermeden
yanlış sonuç verebileceği iki durumu belirt.

[kodu buraya yapıştırın]
```

### Test yazdırmak

```text
Aşağıdaki kod için, doğru sonucu elle hesaplanabilen girdilerle üç kısa test yaz; örneğin dakikada
60 atımlık kalp hızında RR aralığı tam olarak 1 saniyedir. Her test, sonuç yanlışsa kodu açık bir
mesajla durdurmalı. Her testin hangi hatayı yakaladığını bir cümleyle açıkla.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter defterinin 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Vakanın frontal ekseni

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: 67 yaşında bir kadın hastanın istirahat EKG'sinden frontal QRS eksenini atım atım ölçmek
istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir atımdır: "atım" sütunu atımın sırasını,
"D1" ve "aVF" sütunları da bu derivasyonlardaki net QRS gerilimini milivolt olarak verir. Net
gerilim, QRS kompleksindeki en büyük pozitif ve en büyük negatif sapmanın toplamıdır.
Görev: Her atım için yatay bileşeni D1 gerilimi, dikey bileşeni aVF geriliminin 0,866'ya bölümü olan
vektörü kur. Frontal eksen, bu vektörün derece cinsinden açısıdır; açı D1 yönünden ölçülür ve
ayaklara doğru artı değer alır. Ardından bütün atımların medyan eksenini bul ve −30 ile +90 derece
arasındaki normal aralıkta olup olmadığını yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Medyan ekseni derece olarak, bir ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: D1'de 0,9 mV, aVF'de −0,3 mV olan bir atım yaklaşık −21 derecelik bir eksen vermeli. Kayıtta
bu hastanın ekseni 21 derecedir; sonuç bu değerin yaklaşık 10 derece yakınında olmalı, çünkü net
gerilimler küçük septal ve terminal kuvvetleri de içerir.
```

### Adım 2: Gerçek değerlere karşı on hasta

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Otomatik bir EKG ölçümünün, aralarında atriyal fibrilasyonu ya da sol dal bloğu olanların da
bulunduğu on sanal klinik hastasında gerçek değerlerle ne kadar uyuştuğunu öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastanın bir ölçümüdür: "hasta" sütunu
hastanın numarasını verir; "ritim" sütununda "sinüs" ya da "AF", "ileti" sütununda "normal" ya da
"LBBB" (sol dal bloğu) yazar. "ölçüm" sütunu ölçümün adını ("kalp hızı", "PR", "QRS", "QT" ya da
"eksen"), "ölçülen" sütunu otomatik ölçümün değerini, "gerçek" sütunu da gerçek değeri verir. Kalp
hızları dakikadaki atım sayısı, aralıklar milisaniye, eksenler derece olarak verilmiştir. Atriyal
fibrilasyonda PR aralığı olmadığından bu hücreler boştur.
Görev: Her satır için ölçülen ile gerçek değer arasındaki farkı (ölçülen eksi gerçek) hesapla. Her
ölçüm türü için ortalama mutlak farkı ve en büyük mutlak farkı, bu farkın görüldüğü hastayla
birlikte yazdır. Ardından bütün farkları, her hastanın bir satırda, her ölçümün bir sütunda yer
aldığı tek bir tabloda göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki özeti ve tabloyu yazdır; QT aralığının ortalama mutlak farkını milisaniye olarak "cevap"
adıyla sakla.
Test: Tabloda on satır bulunmalı. VC-0317 numaralı hastada PR, QRS ve QT farkları yalnızca birkaç
milisaniye olmalı.
```

### Adım 3: 100 numaralı kayıtta otuz dakika boyunca kalp hızı

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: MIT-BIH Aritmi Veri Tabanı'ndaki 100 numaralı kayıtta, yani 69 yaşında bir erkeğin 30
dakikalık ambulatuvar EKG'sinde, kalp hızının zaman içinde nasıl değiştiğini görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır, kardiyologların kayda koyduğu bir işarettir:
"zaman" sütunu işaretin yerini saniye olarak, "etiket" sütunu da türünü verir. "N" normal atımı, "A"
atriyal erken atımı, "V" ventriküler erken atımı gösterir; "+" ise ritim değişikliğini belirtir ve
bir atım değildir.
Görev: Yalnızca atımları, yani "+" dışındaki etiketleri tut. İlk atımdan sonraki her atım için kalp
hızını, 60'ın saniye cinsinden RR aralığına bölümü olarak hesapla. Bu kalp hızını dakika cinsinden
zamana karşı çiz. Ardından kaydın tamamının ortalama kalp hızını, 60'ın ortalama RR aralığına
bölümüyle hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ortalama kalp hızını dakikadaki atım sayısı olarak, bir ondalık basamakla yazdır ve "cevap"
adıyla sakla. Grafiği de göster.
Test: Tam 1 saniyelik bir RR aralığı dakikada 60 atım vermeli; ortalama kalp hızı da dakikada 60 ile
90 atım arasında olmalı.
```

### Adım 4: Her hasta için Bazett mi Fridericia mı?

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal klinikteki on hastada, Bazett ya da Fridericia düzeltmesini seçmenin QT aralığının
uzun olup olmadığı kararını değiştirip değiştirmediğini öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "hasta" sütunu hastanın
numarasını verir; "cinsiyet" sütununda "kadın" ya da "erkek" yazar. "kalp hızı" sütunu ölçülen kalp
hızını dakikadaki atım sayısı olarak, "QT" sütunu da ölçülen QT aralığını milisaniye olarak verir.
Görev: Her hasta için RR aralığını saniye olarak, 60'ın kalp hızına bölümüyle hesapla. QTc'yi Bazett
formülüyle (QT bölü RR'nin karekökü) ve Fridericia formülüyle (QT bölü RR'nin küp kökü) bul.
Kadınlarda 460 ms ya da daha uzun, erkeklerde 450 ms ya da daha uzun bir QTc'yi uzun kabul et. İki
formülün farklı karara götürdüğü hastaları listele.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki düzeltmeyi ve iki kararı içeren tabloyu ve kararları uyuşmayan hastaların listesini
yazdır. Kararları farklı olan hastaların sayısını "cevap" adıyla sakla.
Test: Dakikada yaklaşık 85 atımlık kalp hızıyla bir kadın olan VC-0317, Bazett formülüne göre uzun,
Fridericia formülüne göre normal çıkmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
