# Prompt kütüphanesi, 2. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[2. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-02/PROMPTS.md)

Bu kütüphanede, 2. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: İlk risk modeli](#durak-1-ilk-risk-modeli)
3. [Durak 2: Bir modeli dürüstçe sınamak](#durak-2-bir-modeli-dürüstçe-sınamak)
4. [Durak 3: Alt gruplar, sağkalım ve denetlenecek bir model](#durak-3-alt-gruplar-sağkalım-ve-denetlenecek-bir-model)
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

## Durak 1: İlk risk modeli

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 2, 1. ve 2. bölümler*

UCI Heart Disease veri setindeki Cleveland hastalarına efor testi ve koroner anjiyografi yapılmıştır. Bu durakta öykü ve efor testinden alınan sekiz değişkenle bir lojistik regresyon kurulur; modelin daha önce görmediği hastalarda koroner arter hastalığını ne kadar iyi tanıdığı denetlenir.

### Adım 1.1: Model ve test AUC değeri

**Amaç.** Bu adımda eğitim kümesinde bir lojistik regresyon eğitilir ve model test kümesinde ROC eğrisinin altındaki alanla (AUC) ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Cleveland Clinic'te efor testi ve koroner anjiyografi yapılmış 303 hastada, öykü ve efor
testindeki sekiz değişkenden koroner arter hastalığını öngören bir model kurmak ve modeli görmediği
hastalarda sınamak istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "yaş" sütunu yaşı yıl olarak
verir; "cinsiyet" erkekler için 1, kadınlar için 0'dır. "göğüs ağrısı" sütununda "tipik anjina",
"atipik anjina", "anjina dışı ağrı" ya da "asemptomatik" yazar. "istirahat kan basıncı"
istirahatteki sistolik kan basıncını mmHg, "kolesterol" serum kolesterolünü mg/dL, "en yüksek kalp
hızı" da efor testinde ulaşılan en yüksek kalp hızını atım/dk olarak verir. "efor anjinası", eforla
anjina ortaya çıkmışsa 1, çıkmamışsa 0'dır; "ST çökmesi" ise eforda istirahate göre ST çökmesini mm
olarak verir. "KAH" sütunu, anjiyografide en az bir büyük koroner arterinin çapı yüzde 50'den fazla
daralmış hastalar için 1, diğer hastalar için 0'dır. "küme" sütununda "eğitim" ya da "test" yazar;
test kümesinde 76 hasta vardır.
Görev: Göğüs ağrısı tipini, tipik anjina referans olmak üzere üç evet/hayır sütununa çevir. "KAH" ve
"küme" dışındaki sekiz değişkeni modelin girdisi olarak kullan. Bu değişkenleri yalnızca eğitim
kümesindeki hastaların ortalama ve standart sapmalarıyla standartlaştır. Eğitim kümesinde bir
lojistik regresyon modeli eğit ve modelin test hastalarına verdiği olasılıklardan ROC eğrisinin
altındaki alanı (AUC) hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Test kümesinin AUC değerini üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Test kümesinde 76 hasta bulunmalı ve AUC 0,5 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,931

### Adım 1.2: 0,5 eşiğinde duyarlılık

**Amaç.** Bu adımda modelin olasılıkları 0,5 eşiğinde karara dönüştürülür ve modelin hastalığı olanların ne kadarını tanıdığı bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir modelin, olasılığı 0,5 ya da daha yüksek olan hastayı pozitif saydığında koroner arter
hastalığı olanların ne kadarını tanıdığını öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır test kümesindeki bir hastadır: "olasılık"
sütunu modelin bu hastaya verdiği koroner arter hastalığı olasılığını, "KAH" sütunu da gerçek durumu
verir (hastalık varsa 1, yoksa 0).
Görev: Olasılığı 0,5 ya da daha yüksek olan hastayı pozitif say. Doğru pozitifleri (TP; hastalığı
olup pozitif sayılanlar) ve yanlış negatifleri (FN; hastalığı olup negatif sayılanlar) say.
Duyarlılık, TP / (TP + FN) oranıdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: TP ve FN sayılarını ve duyarlılığı üç ondalık basamakla yazdır; duyarlılığı "cevap" adıyla
sakla.
Test: TP + FN, tablodaki hastalığı olanların sayısına, yani 35'e eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 0,8

### Adım 1.3: En yüksek kalp hızının odds oranı

**Amaç.** Bu adımda efor testinde ulaşılan en yüksek kalp hızı bir standart sapma arttığında koroner arter hastalığının odds değerinin nasıl değiştiği modelden okunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir koroner arter hastalığı modelindeki değişkenlerin, özellikle de efor testinde ulaşılan
en yüksek kalp hızının, hastalığın odds değeriyle ilişkisini odds oranı olarak görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır, standartlaştırılmış değişkenlerle eğitilmiş
bir lojistik regresyon modelinin bir değişkenidir: "değişken" sütunu değişkenin adını, "katsayı"
sütunu da modelin katsayısını, yani bir standart sapmalık artışa karşılık gelen log-odds değişimini
verir. Göğüs ağrısı tiplerinin katsayıları her tipi tipik anjinayla karşılaştırır.
Görev: Her katsayıyı standart sapma başına bir odds oranına çevir: e sayısının katsayı kadar
kuvvetini al. Bütün odds oranlarını değişkenlerin adlarıyla birlikte yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: En yüksek kalp hızının odds oranını iki ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Katsayısı 0 olan bir değişkenin odds oranı tam 1 olmalı; ST çökmesinin odds oranı da 1'in
üzerinde çıkmalı.
```

**Beklenen sonuç:** "cevap" = 0,58

## Durak 2: Bir modeli dürüstçe sınamak

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-2) · Python yolunda aynı sonuç: 3-6. bölümler*

76 hastalık tek bir test kümesi belirsiz bir kestirim verir ve bazı modeller olduklarından daha iyi görünür. Bu durakta test çapraz doğrulamayla tekrarlanır ve bir rastgele orman denenir. Ardından sanal kliniğin nadir bir sonucuna geçilir: 12 ay içinde ölüm ya da kalp yetersizliği nedeniyle hastaneye yatış.

### Adım 2.1: Beş katlı çapraz doğrulama

**Amaç.** Bu adımda 1. duraktaki lojistik regresyon, her seferinde hastaların başka bir beşte birinde olmak üzere beş kez sınanır ve ortalama AUC alınır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Cleveland Clinic'teki 303 hastada, bir koroner arter hastalığı modelinin AUC değeri için 76
hastalık tek bir test kümesinin verebileceğinden daha güvenilir bir kestirim istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "yaş" sütunu yaşı yıl olarak
verir; "cinsiyet" erkekler için 1, kadınlar için 0'dır. "göğüs ağrısı" sütununda "tipik anjina",
"atipik anjina", "anjina dışı ağrı" ya da "asemptomatik" yazar. "istirahat kan basıncı"
istirahatteki sistolik kan basıncını mmHg, "kolesterol" serum kolesterolünü mg/dL, "en yüksek kalp
hızı" da efor testinde ulaşılan en yüksek kalp hızını atım/dk olarak verir. "efor anjinası", eforla
anjina ortaya çıkmışsa 1, çıkmamışsa 0'dır; "ST çökmesi" ise eforda istirahate göre ST çökmesini mm
olarak verir. "KAH" sütunu, anjiyografide en az bir büyük koroner arterinin çapı yüzde 50'den fazla
daralmış hastalar için 1, diğer hastalar için 0'dır. "kat" sütunu hastanın beş kattan hangisinde
olduğunu (1-5) gösterir; KAH oranı her katta aşağı yukarı aynıdır.
Görev: Göğüs ağrısı tipini, tipik anjina referans olmak üzere üç evet/hayır sütununa çevir. "KAH" ve
"kat" dışındaki sekiz değişkeni girdi olarak kullan. Her katı sırayla test kümesi, diğer dört katı
eğitim kümesi olarak kullan: Değişkenleri eğitim hastalarıyla standartlaştır, bir lojistik regresyon
modeli eğit ve test katında AUC değerini hesapla. Beş AUC değerini ve ortalamalarını yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Beş katın ortalama AUC değerini üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Her biri 0,5 ile 1 arasında olan beş değer yazdırılmalı.
```

**Beklenen sonuç:** "cevap" = 0,871

### Adım 2.2: Bir rastgele orman

**Amaç.** Bu adımda aynı hastalarda daha esnek bir model eğitilir ve test AUC değeri lojistik regresyonunkiyle karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Cleveland Clinic'teki 303 hastada, daha esnek bir model olan rastgele ormanın koroner arter
hastalığını lojistik regresyondan daha iyi öngörüp öngörmediğini öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "yaş" sütunu yaşı yıl olarak
verir; "cinsiyet" erkekler için 1, kadınlar için 0'dır. "göğüs ağrısı" sütununda "tipik anjina",
"atipik anjina", "anjina dışı ağrı" ya da "asemptomatik" yazar. "istirahat kan basıncı"
istirahatteki sistolik kan basıncını mmHg, "kolesterol" serum kolesterolünü mg/dL, "en yüksek kalp
hızı" da efor testinde ulaşılan en yüksek kalp hızını atım/dk olarak verir. "efor anjinası", eforla
anjina ortaya çıkmışsa 1, çıkmamışsa 0'dır; "ST çökmesi" ise eforda istirahate göre ST çökmesini mm
olarak verir. "KAH" sütunu, anjiyografide en az bir büyük koroner arterinin çapı yüzde 50'den fazla
daralmış hastalar için 1, diğer hastalar için 0'dır. "küme" sütununda "eğitim" ya da "test" yazar;
test kümesinde 76 hasta vardır.
Görev: Göğüs ağrısı tipini, tipik anjina referans olmak üzere üç evet/hayır sütununa çevir. "KAH" ve
"küme" dışındaki sekiz değişkeni girdi olarak kullan. Eğitim kümesinde bir rastgele orman modeli
eğit. Rastgele seçimler her çalıştırmada aynı olsun; bunun için başlangıç değeri olarak 2026
sayısını kullan. Ormanın test hastalarına verdiği olasılıklardan AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ormanın test AUC değerini üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: AUC 0,5 ile 1 arasında olmalı. Karşılaştırma için aynı kümelerde bir lojistik regresyonun test
AUC değerini de hesapla ve iki değeri yan yana yazdır.
```

**Beklenen sonuç:** "cevap" = 0,911

### Adım 2.3: Nadir bir sonuç

**Amaç.** Bu adımda hastaların yalnızca 100'de 3 kadarında görülen 12 aylık olay için bir model eğitilir ve sınıf ağırlıklarının modelin bulduklarını nasıl değiştirdiği görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal kliniğin 2.000 hastasında, nadir bir olayı, yani ilk 12 ay içinde ölüm ya da kalp
yetersizliği nedeniyle hastaneye yatışı öngören bir model kurmak istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır bir hastadır: "yaş" (yıl), "eGFR" (tahmini
glomerüler filtrasyon hızı, mL/dk/1,73 m²), "LVEF" (sol ventrikül ejeksiyon fraksiyonu, %),
"NT-proBNP" (pg/mL), "AF" (atriyal fibrilasyon; varsa 1) ve "diyabet" (varsa 1). "olay" sütunu, ilk
12 ay içinde ölüm ya da kalp yetersizliği nedeniyle yatış için 1, diğer hastalar için 0'dır. "küme"
sütununda "eğitim" ya da "test" yazar; test kümesinde 600 hasta vardır.
Görev: NT-proBNP yerine onun doğal logaritmasını kullan. Altı değişkeni eğitim hastalarıyla
standartlaştır ve eğitim kümesinde bir lojistik regresyon modeli eğit. Eğitimde sınıfları dengele:
Olay yaşayan az sayıdaki hasta, toplamda olay yaşamayan bütün hastalar kadar ağırlık taşısın.
Olasılığı 0,5 ya da daha yüksek olan test hastasını pozitif say ve duyarlılığı, yani TP / (TP + FN)
oranını hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Duyarlılığı üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Test kümesinde 600 hasta bulunmalı ve bunların 20'sinde olay olmalı. Sınıflar dengelenmeden
eğitilen aynı model, 0,5 eşiğinde bu olayların hiçbirini bulamamalı.
```

**Beklenen sonuç:** "cevap" = 0,65

## Durak 3: Alt gruplar, sağkalım ve denetlenecek bir model

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-3) · Python yolunda aynı sonuç: 7-9. bölümler*

Kalp yetersizliği olan hastalar yalnızca ejeksiyon fraksiyonuyla değil, başka özellikleriyle de birbirinden ayrılır. Bu durakta önce, yönteme sonuç bilgisi verilmeden alt gruplar aranır; ardından izlem boyunca sağkalım kestirilir. Son olarak bir YZ asistanının kusursuz bir sonuç bildirdiği bir model denetlenir.

### Adım 3.1: Üç küme

**Amaç.** Bu adımda k-ortalamalar yöntemi kalp yetersizliği olan hastalar arasında üç grup arar; ardından bu gruplar gizli fenogruplarla karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal klinikte kalp yetersizliği olan 407 hastada, yönteme hiçbir cevap vermeden alt gruplar
bulmak ve bu grupların kliniğin kurulurken kullandığı fenogruplarla ne kadar örtüştüğünü görmek
istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kalp yetersizliği olan bir hastadır: "yaş"
(yıl), "BKİ" (beden kitle indeksi, kg/m²), "eGFR" (tahmini glomerüler filtrasyon hızı, mL/dk/1,73
m²), "LVEF" (sol ventrikül ejeksiyon fraksiyonu, %), "NT-proBNP" (pg/mL), "LAVI" (sol atriyum hacim
indeksi, mL/m²), "E/e'" (bir oran), "LV kütle indeksi" (sol ventrikül kütle indeksi, g/m²) ve
"TAPSE" (triküspit anüler düzlem sistolik hareketi, mm). "fenogrup" sütunu, kliniğin hastayı
üretirken kullandığı gizli grubu verir: "HFrEF", "HFpEF-metabolik" ya da "HFpEF-kardiyorenal".
Görev: NT-proBNP yerine onun doğal logaritmasını kullan ve dokuz değişkeni standartlaştır;
"fenogrup" sütununu kümelemede kullanma. Hastaları k-ortalamalar yöntemiyle üç kümeye ayır. Yöntemi
farklı rastgele başlangıç noktalarından on kez çalıştır ve en iyi çözümü al; rastgele seçimler için
başlangıç değeri olarak 2026 sayısını kullan. Ardından kümeleri fenogruplarla düzeltilmiş Rand
indeksiyle karşılaştır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her kümedeki hasta sayısını ve düzeltilmiş Rand indeksini üç ondalık basamakla yazdır;
indeksi "cevap" adıyla sakla.
Test: Üç kümedeki hastaların toplamı 407 olmalı. İndeksin 1 olması tam uyumu, 0 olması rastlantısal
uyumu gösterir.
```

**Beklenen sonuç:** "cevap" = 0,706

### Adım 3.2: 24. ayda Kaplan-Meier

**Amaç.** Bu adımda HFrEF hastalarının izlemin başlamasından iki yıl sonra hangi oranda hayatta olduğu ve kalp yetersizliği nedeniyle hastaneye yatmadığı kestirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal klinikteki HFrEF hastalarının, izlemin başlamasından 24 ay sonra hangi oranda hayatta
olduğunu ve kalp yetersizliği nedeniyle hastaneye yatmadığını kestirmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kalp yetersizliği olan bir hastadır: "ana
tanı" sütununda "HFrEF" ya da "HFpEF" yazar. "izlem süresi", izlemin başlangıcından ilk olaya ya da
izlemin sonuna kadar geçen süreyi ay olarak verir. "olay" sütunu ölüm ya da kalp yetersizliği
nedeniyle yatış için 1, izlemden olaysız ayrılan (sansürlenen) hasta için 0'dır.
Görev: Ana tanısı HFrEF olan hastalar için olaysız sağkalımın Kaplan-Meier kestirimini adım adım
hesapla. 1'den başla. En az bir olayın görüldüğü her zamanda kestirimi 1 − d/n ile çarp; burada d o
zamandaki olay sayısı, n ise o zamanda hâlâ izlenen, yani izlem süresi en az o kadar olan hasta
sayısıdır. 24. aydaki kestirim, 24 ay ya da daha kısa olan son olay zamanından sonraki değerdir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: 24. aydaki kestirimi üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Aynı hesap, HFpEF hastalarında 24. ayda daha yüksek bir değer vermeli.
```

**Beklenen sonuç:** "cevap" = 0,733

### Adım 3.3: Bir asistanın modelini denetlemek

**Amaç.** Bir YZ asistanı, 12 ay içindeki olay için 1,000'lik bir AUC bildirmiştir. Asistanın modeli izlem süresini de kullanmış ve eğitildiği hastaların kendisinde ölçülmüştür. Bu adımda aynı türden bir modelin dürüst bir değerlendirmede ne verdiği bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal kliniğin 2.000 hastasında, bir asistan kusursuz bir sonuç bildirdikten sonra, bir
rastgele ormanın 12 ay içindeki ölümü ya da kalp yetersizliği nedeniyle yatışı ne kadar iyi
öngördüğüne dair dürüst bir kestirim istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır sanal klinikteki bir hastadır: "yaş" (yıl),
"eGFR" (tahmini glomerüler filtrasyon hızı, mL/dk/1,73 m²), "LVEF" (sol ventrikül ejeksiyon
fraksiyonu, %), "NT-proBNP" (pg/mL), "AF" (atriyal fibrilasyon; varsa 1), "diyabet" (varsa 1), "BKİ"
(beden kitle indeksi, kg/m²) ve "sistolik kan basıncı" (mmHg). "izlem süresi" izlemin ay olarak
süresidir ve ancak izlem bittikten sonra bilinir. "olay" sütunu, ilk 12 ay içinde ölüm ya da kalp
yetersizliği nedeniyle yatış için 1, diğer hastalar için 0'dır. "kat" sütunu hastanın beş kattan
hangisinde olduğunu (1-5) gösterir; olay oranı her katta aşağı yukarı aynıdır.
Görev: Karar anında bilinmediği için "izlem süresi" sütununu girdilerden çıkar. "olay" sütununu
diğer sekiz değişkenle bir rastgele orman modeli kullanarak öngör. Rastgele seçimler her
çalıştırmada aynı olsun; bunun için başlangıç değeri olarak 2026 sayısını kullan. Modeli beş katlı
çapraz doğrulamayla ölç: Her katı bir kez test kümesi, diğer dört katı eğitim kümesi olarak kullan
ve beş katın ortalama AUC değerini al.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ortalama AUC değerini üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Çapraz doğrulanmış AUC, 1,000'in belirgin biçimde altında olmalı. Aynı orman bütün hastalarda
eğitilip yine bütün hastalarda ölçüldüğünde bulunan AUC değerini de yazdır; bu değer belirgin
biçimde daha yüksek çıkmalı.
```

**Beklenen sonuç:** "cevap" = 0,849

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

### Model denetimi istemek

```text
Aşağıdaki kod bir öngörü modeli kurup değerlendirmektedir. Dört noktayı denetle. Model, karar anında
bilinemeyecek bir değişken kullanıyor mu? Ayırmadan önce bütün hastalardan öğrenen bir adım var mı?
Başarım hangi hastalarda ölçülüyor? Sonuç nadir mi? Kısa bir listeyle cevap ver, ardından
düzeltilmiş kodu ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter defterinin 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Fenogrup sayısını seçmek

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal klinikte kalp yetersizliği olan 407 hastada fenogrupları bulmak ve sayılarını seçmek
istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kalp yetersizliği olan bir hastadır: "yaş"
(yıl), "BKİ" (beden kitle indeksi, kg/m²), "eGFR" (tahmini glomerüler filtrasyon hızı, mL/dk/1,73
m²), "LVEF" (sol ventrikül ejeksiyon fraksiyonu, %), "NT-proBNP" (pg/mL), "LAVI" (sol atriyum hacim
indeksi, mL/m²), "E/e'" (bir oran), "LV kütle indeksi" (sol ventrikül kütle indeksi, g/m²) ve
"TAPSE" (triküspit anüler düzlem sistolik hareketi, mm).
Görev: NT-proBNP yerine onun doğal logaritmasını kullan ve dokuz değişkeni standartlaştır. 2'den
6'ya kadar her küme sayısı için hastaları k-ortalamalar yöntemiyle kümelere ayır; yöntemi farklı
rastgele başlangıç noktalarından on kez çalıştır, en iyi çözümü al ve başlangıç değeri olarak 2026
sayısını kullan. Her küme sayısı için küme içi kareler toplamını (WCSS) ve ortalama siluet değerini
hesapla. Küme sayısını seç ve seçimin klinik gerekçesini bir iki cümleyle yaz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Küme sayısını, WCSS değerini ve siluet değerini gösteren bir tablo yazdır; seçtiğin küme
sayısını tam sayı olarak "cevap" adıyla sakla.
Test: Küme sayısı arttıkça WCSS azalmalı ve her siluet değeri −1 ile 1 arasında bulunmalı.
```

### Adım 2: Fenogrupları tanımlamak ve adlandırmak

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kalp yetersizliği olan hastaların fenogruplarını tanımlamak ve her birine kısa bir klinik ad
vermek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kalp yetersizliği olan bir hastadır: "küme"
sütunu, proje adımı 1'de seçilen küme sayısıyla bulunan fenogrubu verir. Diğer sütunlar "yaş" (yıl),
"BKİ" (kg/m²), "eGFR" (mL/dk/1,73 m²), "LVEF" (%), "NT-proBNP" (pg/mL), "LAVI" (mL/m²), "E/e'", "LV
kütle indeksi" (g/m²), "TAPSE" (mm), "kadın" (kadınlarda 1), "diyabet" ve "AF" (varsa 1) ile "ana
tanı" ("HFrEF" ya da "HFpEF") değerlerini tutar.
Görev: Her küme için bir sütun içeren bir tablo kur: hasta sayısı; yaş, BKİ, eGFR, LVEF, LAVI, E/e',
LV kütle indeksi ve TAPSE ortalamaları; NT-proBNP ortancası; kadınların, diyabetin, AF'nin ve
HFrEF'nin yüzdesi. Ardından her küme için kısa bir klinik ad öner.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Tabloyu ve adları yazdır; tabloyu "cevap" adıyla sakla.
Test: Tablodaki hasta sayılarının toplamı 407 olmalı.
```

### Adım 3: Fenogruba göre prognoz

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Fenogrupların prognozunu iki klasik grubun, yani HFrEF ve HFpEF gruplarının prognozuyla
karşılaştırmak istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kalp yetersizliği olan bir hastadır: "küme"
sütunu proje adımı 1'deki fenogrubu verir; "ana tanı" sütununda "HFrEF" ya da "HFpEF" yazar. "izlem
süresi" ilk olaya ya da izlemin sonuna kadar geçen süreyi ay olarak verir; "olay" ise ölüm ya da
kalp yetersizliği nedeniyle yatış için 1, izlemden olaysız ayrılan (sansürlenen) hasta için 0'dır.
Görev: Olaysız sağkalımın Kaplan-Meier eğrilerini bir panelde kümeler için, ikinci bir panelde HFrEF
ve HFpEF için çiz. Her grubun 24. aydaki sağkalımını hesapla ve her paneldeki grupları log-rank
testiyle karşılaştır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Şekli, 24. aydaki sağkalım tablosunu ve iki log-rank testinin p değerlerini göster; kümelerin
p değerini "cevap" adıyla sakla.
Test: Her eğri 1'den başlamalı ve hiç yükselmemeli.
```

### Adım 4: Gizli gerçekle karşılaştırmak

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Sanal klinik, kalp yetersizliği olan her hastaya gizli bir fenogrup atamıştır. Proje adımı
1'de bulunan kümelerin bu fenogrupları ne kadar yakaladığını öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var. Her satır kalp yetersizliği olan bir hastadır: "küme"
sütunu proje adımı 1'deki kümeyi, "fenogrup" sütunu da gizli fenogrubu verir: "HFrEF",
"HFpEF-metabolik" ya da "HFpEF-kardiyorenal".
Görev: Kümeleri fenogruplarla çapraz tabloya dök ve düzeltilmiş Rand indeksini hesapla. Ardından
kümelemenin, yalnızca ejeksiyon fraksiyonuna bakıldığında gözden kaçan neyi bulduğunu üç cümleyle
yaz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Çapraz tabloyu, üç ondalık basamaklı indeksi ve üç cümleyi yazdır; indeksi "cevap" adıyla
sakla.
Test: İndeks −1 ile 1 arasında olmalı; üç kümeyle 0,5'in belirgin biçimde üzerinde bulunmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
