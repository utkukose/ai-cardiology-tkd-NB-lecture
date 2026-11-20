# Prompt kütüphanesi, 9. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[9. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-09/PROMPTS.md)

Bu kütüphanede, 9. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Koroner arter hastalığı modelinin ardındaki klinik etkenler](#durak-1-koroner-arter-hastalığı-modelinin-ardındaki-klinik-etkenler)
3. [Durak 2: Tek bir hasta için LIME ve eko ağının baktığı yer](#durak-2-tek-bir-hasta-için-lime-ve-eko-ağının-baktığı-yer)
4. [Durak 3: Kayma, izlem ve alt gruplar](#durak-3-kayma-izlem-ve-alt-gruplar)
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

## Durak 1: Koroner arter hastalığı modelinin ardındaki klinik etkenler

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-09/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 9, 1-3. bölümler*

Bu durak oturumun mini projesidir. 2. haftanın koroner arter hastalığı için kurduğu iki model, yani bir rastgele orman ve bir lojistik regresyon, Cleveland verisinin eğitim hastalarıyla öğrenir. Modellerin 59 yaşındaki bir kadın olan 172 numaralı hasta için verdiği tahminler, kesin Shapley değerleriyle hastanın sekiz klinik değişkeni arasında paylaştırılır; lojistik regresyon için kapalı bir form, log-odds ölçeğinde aynı değerleri verir. 1.4. adım her test hastasının değerlerini genel bir açıklamaya dönüştürür; 1.5. adım ise LDL, yaş ve ejeksiyon fraksiyonunun da aralarında bulunduğu dokuz faktörden hangisinin sanal kliniğin kayıt sistemi üzerindeki bir modeli en çok etkilediğini sorar.

### Adım 1.1: 2. haftanın iki modeli

**Amaç.** Bu adımda 2. haftanın iki modeli eğitim hastalarında yeniden kurulur ve test hastalarında değerlendirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kalite ve güvenlik kurulunun kullanılmadan önce inceleyebilmesi için önceki bir analizdeki
koroner arter hastalığı modellerini yeniden kurmak istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin Cleveland
verisinden, yani koroner anjiyografiye gönderilmiş hastalardan 303 hasta bulunur. Her satır bir
hastadır: "hasta" hastanın verideki numarasını (0-302), "küme" 2. haftanın kümesini verir ("eğitim",
227 hasta; "test", 76 hasta). Klinik değişkenler şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da
"kadın"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı" (egzersiz
testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi anjinaya yol
açtıysa 1), "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm) ve "göğüs ağrısı
tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"). "hastalık"
anjiyogramda koroner arter hastalığı görüldüyse 1, aksi hâlde 0 olur.
Görev: Tabloyu bu sırayla bir modelin sütunlarına dönüştür: Yaş, erkek için 1 ve kadın için 0 olan
cinsiyet, istirahat kan basıncı, kolesterol, en yüksek kalp hızı, egzersiz anjinası, ST çökmesi ve
tipik anjinayı referans alan, atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ve 1 değerli üç
sütun. Satırları tablonun sırasında tut. Eğitim hastalarında iki model kur: Sütunları eğitim
hastalarıyla standartlaştırılmış ve en fazla 1.000 yinelemeli bir lojistik regresyon ile 300 ağaçlı
bir rastgele orman. Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. İki modelin
test hastalarındaki ROC eğrisi altındaki alanını (AUC) ve her birinin 172 numaralı hastaya verdiği
olasılığı hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki test AUC değerini ve 172 numaralı hastanın iki olasılığını yazdır; ormanın test AUC
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Hiçbir test hastası modellerden birini kurmak için kullanılmamalı ve AUC 0 ile 1 arasında
olmalı.
```

**Beklenen sonuç:** "cevap" = 0,904

### Adım 1.2: 172 numaralı hastanın Shapley değerleri

**Amaç.** Bu adımda ormanın 172 numaralı hastaya verdiği olasılık, hastanın sekiz klinik değişkeni arasında paylaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, ormanın egzersiz testinde anjinası ortaya çıkan 59 yaşındaki bir kadın olan 172
numaralı hastaya, ortalama hastaya kıyasla neden yüksek bir koroner arter hastalığı olasılığı
verdiğini soruyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin Cleveland
verisinden, yani koroner anjiyografiye gönderilmiş hastalardan 303 hasta bulunur. Her satır bir
hastadır: "hasta" hastanın verideki numarasını (0-302), "küme" 2. haftanın kümesini verir ("eğitim",
227 hasta; "test", 76 hasta). Klinik değişkenler şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da
"kadın"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı" (egzersiz
testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi anjinaya yol
açtıysa 1), "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm) ve "göğüs ağrısı
tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"). "hastalık"
anjiyogramda koroner arter hastalığı görüldüyse 1, aksi hâlde 0 olur.
Görev: Tabloyu bu sırayla bir modelin sütunlarına dönüştür: Yaş, erkek için 1 ve kadın için 0 olan
cinsiyet, istirahat kan basıncı, kolesterol, en yüksek kalp hızı, egzersiz anjinası, ST çökmesi ve
tipik anjinayı referans alan, atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ve 1 değerli üç
sütun. Satırları tablonun sırasında tut. Eğitim hastalarında 300 ağaçlı bir rastgele orman kur.
Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. Sekiz klinik değişkeni sekiz
oyuncu olarak ele al; göğüs ağrısı tipinin üç sütunu her zaman tek bir oyuncu olarak birlikte
hareket etsin. 172 numaralı hasta için ormanın verdiği olasılığın kesin Shapley değerlerini hesapla:
256 oyuncu grubunun her biri için gruptaki oyunculara hastanın değerlerini, öteki oyunculara sırayla
her eğitim hastasının değerlerini ver, tahmin et ve eğitim hastaları üzerinden ortalama al; bu,
grubun değeridir. Bir oyuncunun Shapley değeri, onu içermeyen bütün gruplar üzerinden, grubun
oyuncuyla birlikteki değeri eksi oyuncu olmadan değerinin s!(7 − s)!/8! ağırlığıyla çarpımlarının
toplamıdır; burada s, oyuncu olmadan grubun büyüklüğüdür. Sekiz değerin toplamının hastanın tahmini
eksi boş grubun değerine eşit olduğunu kontrol et.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Sekiz Shapley değerini mutlak değeri en büyükten en küçüğe, boş grubun değeri ve tahminle
birlikte göster; göğüs ağrısı tipinin Shapley değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Sekiz değerin toplamı, altıncı ondalık basamağa kadar tahmin eksi boş grubun değerine eşit
olmalı.
```

**Beklenen sonuç:** "cevap" = 0,155

### Adım 1.3: Lojistik regresyonun kapalı formu

**Amaç.** Bu adımda lojistik regresyonun 172 numaralı hasta için log-odds ölçeğindeki Shapley değerleri kapalı bir formla hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, lojistik regresyonun 172 numaralı hastaya neden ormandan daha düşük bir olasılık
verdiğini ve iki modelin hangi değişkenlerde ayrıştığını görmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin Cleveland
verisinden, yani koroner anjiyografiye gönderilmiş hastalardan 303 hasta bulunur. Her satır bir
hastadır: "hasta" hastanın verideki numarasını (0-302), "küme" 2. haftanın kümesini verir ("eğitim",
227 hasta; "test", 76 hasta). Klinik değişkenler şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da
"kadın"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı" (egzersiz
testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi anjinaya yol
açtıysa 1), "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm) ve "göğüs ağrısı
tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"). "hastalık"
anjiyogramda koroner arter hastalığı görüldüyse 1, aksi hâlde 0 olur.
Görev: Tabloyu bu sırayla bir modelin sütunlarına dönüştür: Yaş, erkek için 1 ve kadın için 0 olan
cinsiyet, istirahat kan basıncı, kolesterol, en yüksek kalp hızı, egzersiz anjinası, ST çökmesi ve
tipik anjinayı referans alan, atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ve 1 değerli üç
sütun. Satırları tablonun sırasında tut. Eğitim hastalarında, sütunları eğitim hastalarıyla
standartlaştırılmış ve en fazla 1.000 yinelemeli bir lojistik regresyon kur. Log-odds ölçeğinde bir
değişkenin bir hasta için Shapley değeri, özgün sütunun birimi başına katsayısı ile hastanın değeri
eksi eğitim hastalarının ortalamasının çarpımıdır; göğüs ağrısı tipi için sütunlarının üç terimini
topla. 172 numaralı hasta için sekiz değeri hesapla ve toplamlarının hastanın log-odds değeri eksi
eğitim hastalarının ortalama log-odds değerine eşit olduğunu kontrol et.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Sekiz değeri değişkenleriyle birlikte göster; cinsiyetin değerini üç ondalık basamakla
"cevap" adıyla sakla.
Test: Sekiz değerin toplamı, hastanın log-odds değeri eksi eğitim hastalarının ortalama log-odds
değerine eşit olmalı.
```

**Beklenen sonuç:** "cevap" = −1,175

### Adım 1.4: Tek bir hastadan bütün hastalara

**Amaç.** Bu adımda ormanın her test hastası için Shapley değerleri hesaplanır ve değişkenler sıralanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, ormanın bütün test hastalarında hangi klinik değişkenlere dayandığını ve bunlardan
herhangi birinin hastalıktan çok hastaların nasıl sevk edildiğini yansıtıp yansıtmadığını öğrenmek
istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin Cleveland
verisinden, yani koroner anjiyografiye gönderilmiş hastalardan 303 hasta bulunur. Her satır bir
hastadır: "hasta" hastanın verideki numarasını (0-302), "küme" 2. haftanın kümesini verir ("eğitim",
227 hasta; "test", 76 hasta). Klinik değişkenler şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da
"kadın"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı" (egzersiz
testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi anjinaya yol
açtıysa 1), "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm) ve "göğüs ağrısı
tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"). "hastalık"
anjiyogramda koroner arter hastalığı görüldüyse 1, aksi hâlde 0 olur.
Görev: Tabloyu bu sırayla bir modelin sütunlarına dönüştür: Yaş, erkek için 1 ve kadın için 0 olan
cinsiyet, istirahat kan basıncı, kolesterol, en yüksek kalp hızı, egzersiz anjinası, ST çökmesi ve
tipik anjinayı referans alan, atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ve 1 değerli üç
sütun. Satırları tablonun sırasında tut. Eğitim hastalarında 300 ağaçlı bir rastgele orman kur.
Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. Sekiz klinik değişkeni sekiz
oyuncu olarak ele al; göğüs ağrısı tipinin üç sütunu her zaman tek bir oyuncu olarak birlikte
hareket etsin. Her test hastası için ormanın verdiği olasılığın kesin Shapley değerlerini hesapla:
256 oyuncu grubunun her biri için gruptaki oyunculara hastanın değerlerini, öteki oyunculara sırayla
her eğitim hastasının değerlerini ver, tahmin et ve eğitim hastaları üzerinden ortalama al; bu,
grubun değeridir. Bir oyuncunun Shapley değeri, onu içermeyen bütün gruplar üzerinden, grubun
oyuncuyla birlikteki değeri eksi oyuncu olmadan değerinin s!(7 − s)!/8! ağırlığıyla çarpımlarının
toplamıdır; burada s, oyuncu olmadan grubun büyüklüğüdür. Sekiz değerin toplamının hastanın tahmini
eksi boş grubun değerine eşit olduğunu kontrol et. Ardından her değişken için test hastaları
üzerinden mutlak Shapley değerlerinin ortalamasını hesapla ve her değişkenin en büyük mutlak değere
sahip olduğu test hastalarını say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ortalama mutlak değerleri en büyükten en küçüğe, sayılarla birlikte göster; göğüs ağrısı
tipinin ortalama mutlak değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Sayıların toplamı test hastalarının sayısına eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 0,138

### Adım 1.5: Mini proje: LDL, yaş, EF ve kayıt sistemi modeli

**Amaç.** Bu adımda dokuz klinik faktörden hangisinin koroner arter hastalığı modelini en çok etkilediği kesin Shapley değerleriyle bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: LDL, yaş ya da ejeksiyon fraksiyonu gibi klinik faktörlerden hangisinin bir koroner arter
hastalığı modelini en çok etkilediğini öğrenmek istiyorum.
Veri: Defterde sanal kliniğin kayıt sistemindeki 3.600 hastayı içeren "veri" adlı bir tablo vardır;
bu sentetik bir veri setidir. Her satır bir hastadır: "küme" sütunu "eğitim" (2.700 hasta) ya da
"test" (900 hasta) değerini alır. Dokuz klinik faktör şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya
da "kadın"), varsa 1, yoksa 0 olan "sigara", "diyabet", "hipertansiyon" ve "aile öyküsü", "LDL" ve
"HDL" (mg/dL) ve "ejeksiyon fraksiyonu" (%). "koroner arter hastalığı" sütunu hastada koroner arter
hastalığı varsa 1, yoksa 0 olur.
Görev: Cinsiyeti erkek için 1, kadın için 0 olarak kodla. Koroner arter hastalığını dokuz faktörden
öngörmek için eğitim hastalarıyla, her yaprağında en az 10 hasta bulunan 200 ağaçlı bir rastgele
orman kur. Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. Her biri seed değeri
2026 olmak üzere arka plan olarak 100 eğitim hastası ve 100 test hastası çek. 100 test hastasının
her biri için, dokuz faktörü dokuz oyuncu sayarak ormanın olasılığının kesin Shapley değerlerini
hesapla: 512 oyuncu grubunun her biri için gruptaki oyunculara hastanın değerlerini, öteki
oyunculara sırayla her arka plan hastasının değerlerini ver, tahmin et ve arka plan üzerinden
ortalama al; bu, grubun değeridir. Bir oyuncunun Shapley değeri, onu içermeyen bütün gruplar
üzerinden, grubun oyuncuyla birlikteki değeri eksi oyuncu olmadan değerinin s!(8 − s)!/9!
ağırlığıyla çarpımlarının toplamıdır; burada s, oyuncu olmadan grubun büyüklüğüdür. Ardından her
faktör için 100 test hastası üzerinden mutlak Shapley değerlerinin ortalamasını hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Dokuz ortalama mutlak değeri en büyükten en küçüğe göster; değeri en büyük olan faktörün
yukarıdaki faktör listesindeki yerini, 1'den başlayarak sayıp "cevap" adıyla sakla: Yaş 1, cinsiyet
2 ve böyle devam ederek ejeksiyon fraksiyonu 9.
Test: Her test hastasının Shapley değerlerinin toplamı, ormanın o hasta için verdiği olasılık eksi
boş grubun değerine eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 9

## Durak 2: Tek bir hasta için LIME ve eko ağının baktığı yer

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-09/ders.html#stop-2) · Python yolunda aynı sonuç: 4-7. bölümler*

Bu durak tahminleri iki yolla daha açıklar. LIME, 1. duraktaki ormanı 172 numaralı hastanın çevresinde ağırlıklı doğrusal bir modelle taklit eder; yirmi seed değeriyle yapılan bir tekrar da cevabının ne kadar kararlı olduğunu gösterir. Ardından küçük bir evrişimli ağ, CAMUS ekokardiyogramlarında yüzde 45'in altındaki ejeksiyon fraksiyonunu işaretlemeyi öğrenir ve ağın Grad-CAM haritaları sol ventrikülün uzman sınırlarıyla karşılaştırılır.

### Adım 2.1: 172 numaralı hasta için LIME

**Amaç.** Bu adımda ormanın 172 numaralı hastaya verdiği olasılık, hastanın çevresine uydurulan ağırlıklı doğrusal bir modelle açıklanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, 172 numaralı hastanın tahmini için Shapley değerlerinden farklı bir yolla yapılmış
ikinci bir açıklama görmek ve ikisinin uyuşup uyuşmadığını anlamak istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin Cleveland
verisinden, yani koroner anjiyografiye gönderilmiş hastalardan 303 hasta bulunur. Her satır bir
hastadır: "hasta" hastanın verideki numarasını (0-302), "küme" 2. haftanın kümesini verir ("eğitim",
227 hasta; "test", 76 hasta). Klinik değişkenler şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da
"kadın"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı" (egzersiz
testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi anjinaya yol
açtıysa 1), "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm) ve "göğüs ağrısı
tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"). "hastalık"
anjiyogramda koroner arter hastalığı görüldüyse 1, aksi hâlde 0 olur.
Görev: Tabloyu bu sırayla bir modelin sütunlarına dönüştür: Yaş, erkek için 1 ve kadın için 0 olan
cinsiyet, istirahat kan basıncı, kolesterol, en yüksek kalp hızı, egzersiz anjinası, ST çökmesi ve
tipik anjinayı referans alan, atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ve 1 değerli üç
sütun. Satırları tablonun sırasında tut. Eğitim hastalarında 300 ağaçlı bir rastgele orman kur.
Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. Sekiz klinik değişkeni sekiz
oyuncu olarak ele al; göğüs ağrısı tipinin üç sütunu her zaman tek bir oyuncu olarak birlikte
hareket etsin. Ormanın 172 numaralı hastaya verdiği olasılığı LIME ile açıkla. Hastanın komşularını
çek: Her komşu için rastgele bir eğitim hastası çek; sekiz oyuncunun her biri yarı olasılıkla 172
numaralı hastanın değerini korusun, aksi hâlde çekilen eğitim hastasının değerini alsın. Her komşu
için hangi oyuncuların hastanın değerini koruduğunu (1) ve hangilerinin değiştirildiğini (0) kaydet.
Her komşuyu exp(−d²/w²) ile ağırlıklandır; burada d değiştirilen oyuncu sayısının karekökü, w = 0,75
× √8 olsun. Komşular için ormanın verdiği olasılıkları sekiz adet 0-1 sütunu üzerine bu
ağırlıklarla, cezası 1 olan bir ridge regresyonuyla modelle; sekiz katsayı açıklamadır. Tek bir
rastgele sayı üreteciyle önce bütün komşuların 0 ve 1 değerlerini, ardından eğitim hastalarını çek.
2.000 komşu ve 2026 seed değerini kullan.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Sekiz katsayıyı mutlak değeri en büyükten en küçüğe göster; göğüs ağrısı tipinin katsayısını
üç ondalık basamakla "cevap" adıyla sakla.
Test: Hastanın sekiz değerinin hepsini koruyan bir komşunun ağırlığı 1 olmalı.
```

**Beklenen sonuç:** "cevap" = 0,145

### Adım 2.2: LIME ne kadar kararlı?

**Amaç.** Bu adımda LIME az sayıda komşu ve yirmi seed değeriyle tekrarlanır ve başı çeken değişkenin ne sıklıkla değiştiği görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, tek bir hastanın açıklamasına güvenmeden önce LIME ile yapılan bir açıklamanın
yeniden çalıştırıldığında aynı kalıp kalmayacağını öğrenmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin Cleveland
verisinden, yani koroner anjiyografiye gönderilmiş hastalardan 303 hasta bulunur. Her satır bir
hastadır: "hasta" hastanın verideki numarasını (0-302), "küme" 2. haftanın kümesini verir ("eğitim",
227 hasta; "test", 76 hasta). Klinik değişkenler şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da
"kadın"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı" (egzersiz
testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi anjinaya yol
açtıysa 1), "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm) ve "göğüs ağrısı
tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"). "hastalık"
anjiyogramda koroner arter hastalığı görüldüyse 1, aksi hâlde 0 olur.
Görev: Tabloyu bu sırayla bir modelin sütunlarına dönüştür: Yaş, erkek için 1 ve kadın için 0 olan
cinsiyet, istirahat kan basıncı, kolesterol, en yüksek kalp hızı, egzersiz anjinası, ST çökmesi ve
tipik anjinayı referans alan, atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ve 1 değerli üç
sütun. Satırları tablonun sırasında tut. Eğitim hastalarında 300 ağaçlı bir rastgele orman kur.
Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. Sekiz klinik değişkeni sekiz
oyuncu olarak ele al; göğüs ağrısı tipinin üç sütunu her zaman tek bir oyuncu olarak birlikte
hareket etsin. Ormanın 172 numaralı hastaya verdiği olasılığı LIME ile açıkla. Hastanın komşularını
çek: Her komşu için rastgele bir eğitim hastası çek; sekiz oyuncunun her biri yarı olasılıkla 172
numaralı hastanın değerini korusun, aksi hâlde çekilen eğitim hastasının değerini alsın. Her komşu
için hangi oyuncuların hastanın değerini koruduğunu (1) ve hangilerinin değiştirildiğini (0) kaydet.
Her komşuyu exp(−d²/w²) ile ağırlıklandır; burada d değiştirilen oyuncu sayısının karekökü, w = 0,75
× √8 olsun. Komşular için ormanın verdiği olasılıkları sekiz adet 0-1 sütunu üzerine bu
ağırlıklarla, cezası 1 olan bir ridge regresyonuyla modelle; sekiz katsayı açıklamadır. Tek bir
rastgele sayı üreteciyle önce bütün komşuların 0 ve 1 değerlerini, ardından eğitim hastalarını çek.
Yalnızca 100 komşu kullan ve 1'den 20'ye kadar seed değerleriyle tekrarla. Her seed değeri için
mutlak katsayısı en büyük olan oyuncuyu bul.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her oyuncunun kaç kez ilk sıraya geldiğini ve göğüs ağrısı tipinin en küçük ve en büyük
katsayısını göster; göğüs ağrısı tipinin ilk sıraya geldiği seed değerlerinin payını iki ondalık
basamakla "cevap" adıyla sakla.
Test: Oyuncuların sayılarının toplamı 20 olmalı.
```

**Beklenen sonuç:** "cevap" = 0,7

### Adım 2.3: Düşük ejeksiyon fraksiyonu için bir ağ

**Amaç.** Bu adımda tek bir görüntüde yüzde 45'in altındaki ejeksiyon fraksiyonunu işaretleyen küçük bir evrişimli ağ eğitilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul ekokardiyogramları okuyan bir ağı inceliyor. Ağın haritaları değerlendirilmeden önce,
görmediği hastaların görüntülerinde düşük ejeksiyon fraksiyonunu ne kadar iyi işaretlediğini
öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda herkese açık bir ekokardiyogram veri seti olan
CAMUS'tan 600 görüntü, yani 300 hastanın apikal iki boşluk ve dört boşluk görüntüleri bulunur. Her
satır bir görüntüdür: "hasta" hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"), "küme" hastanın
kümesini ("eğitim", 200 hasta; "doğrulama", 50 hasta; "test", 50 hasta), "görüntü kalitesi" ise
uzmanların verdiği derecesini ("Good", "Medium" ya da "Poor") verir. "diyastol sonu" ve "sistol
sonu" sütunlarının her hücresi kareyi 0 ile 1 arasında değerler alan 96 × 96 piksellik bir görüntü
olarak tutar. "sınır" sütununun her hücresinde ise sol ventrikül kavitesinin ve miyokardın diyastol
sonu ya da sistol sonundaki uzman sınırı aynı boyutta yer alır: İçeride 1, dışarıda 0. "düşük
ejeksiyon fraksiyonu" hastanın ejeksiyon fraksiyonu yüzde 45'in altındaysa 1, aksi hâlde 0 olur.
Görev: Tek bir görüntü için diyastol sonu ve sistol sonu karelerini 96 × 96 piksellik iki kanal
olarak alan küçük bir evrişimli ağ kur. Ağda dört blok bulunsun; her blok, boyutu koruyan 3 × 3
çekirdekli bir evrişimden (sırasıyla 16, 32, 64 ve 64 kanal), batch normalizasyonundan, ReLU'dan ve
2 × 2 en büyük değer havuzlamasından oluşsun. Bloklardan sonra ağ her kanalın görüntü üzerindeki
ortalamasını alsın ve 0,3 oranında dropout uygulasın; tek çıktılı bir doğrusal katman da düşük
ejeksiyon fraksiyonunun logitini versin. Ağı eğitim görüntülerinde Adam (öğrenme hızı 0,001, ağırlık
azaltma 0,0001) ve ikili çapraz entropiyle, 32 görüntülük karıştırılmış gruplarla 30 epoch eğit. Her
grubu her yönde en fazla 4 piksel rastgele kaydır ve doğrulama görüntülerinde AUC değeri en iyi olan
epoch'un ağırlıklarını sakla. Ağ kütüphanesinin rastgele sayı üretecini ağı kurmadan önce ve
eğitimden önce yeniden 2026 ile başlat. Test görüntülerindeki AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: En iyi doğrulama AUC değerini ve test AUC değerini yazdır; test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Epoch'u seçmek için hiçbir test görüntüsü kullanılmamalı ve bir hastanın görüntüleri tek bir
kümede kalmalı.
```

**Beklenen sonuç:** "cevap" = 0,796

### Adım 2.4: Uzman sınırına karşı Grad-CAM haritaları

**Amaç.** Bu adımda her test görüntüsünün Grad-CAM haritası ve haritanın uzman sınırı içindeki payı hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, ağın düşük ejeksiyon fraksiyonunu uzmanın baktığı sol ventrikülden mi, yoksa
görüntünün başka yerlerinden mi işaretlediğini öğrenmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda herkese açık bir ekokardiyogram veri seti olan
CAMUS'tan 600 görüntü, yani 300 hastanın apikal iki boşluk ve dört boşluk görüntüleri bulunur. Her
satır bir görüntüdür: "hasta" hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"), "küme" hastanın
kümesini ("eğitim", 200 hasta; "doğrulama", 50 hasta; "test", 50 hasta), "görüntü kalitesi" ise
uzmanların verdiği derecesini ("Good", "Medium" ya da "Poor") verir. "diyastol sonu" ve "sistol
sonu" sütunlarının her hücresi kareyi 0 ile 1 arasında değerler alan 96 × 96 piksellik bir görüntü
olarak tutar. "sınır" sütununun her hücresinde ise sol ventrikül kavitesinin ve miyokardın diyastol
sonu ya da sistol sonundaki uzman sınırı aynı boyutta yer alır: İçeride 1, dışarıda 0. "düşük
ejeksiyon fraksiyonu" hastanın ejeksiyon fraksiyonu yüzde 45'in altındaysa 1, aksi hâlde 0 olur.
Görev: Tek bir görüntü için diyastol sonu ve sistol sonu karelerini 96 × 96 piksellik iki kanal
olarak alan küçük bir evrişimli ağ kur. Ağda dört blok bulunsun; her blok, boyutu koruyan 3 × 3
çekirdekli bir evrişimden (sırasıyla 16, 32, 64 ve 64 kanal), batch normalizasyonundan, ReLU'dan ve
2 × 2 en büyük değer havuzlamasından oluşsun. Bloklardan sonra ağ her kanalın görüntü üzerindeki
ortalamasını alsın ve 0,3 oranında dropout uygulasın; tek çıktılı bir doğrusal katman da düşük
ejeksiyon fraksiyonunun logitini versin. Ağı eğitim görüntülerinde Adam (öğrenme hızı 0,001, ağırlık
azaltma 0,0001) ve ikili çapraz entropiyle, 32 görüntülük karıştırılmış gruplarla 30 epoch eğit. Her
grubu her yönde en fazla 4 piksel rastgele kaydır ve doğrulama görüntülerinde AUC değeri en iyi olan
epoch'un ağırlıklarını sakla. Ağ kütüphanesinin rastgele sayı üretecini ağı kurmadan önce ve
eğitimden önce yeniden 2026 ile başlat. Her test görüntüsü için çıktının Grad-CAM haritasını son
bloğun ReLU katmanında, havuzlamadan önce hesapla. Bunun için çıktının bu katmandaki 12 × 12 boyutlu
64 öznitelik haritasına göre gradyanını al, her kanalın ortalama gradyanını o kanalın ağırlığı
olarak kullan ve 64 haritanın ağırlıklı toplamını oluştur. Toplamın yalnızca pozitif kısmını tut ve
çift doğrusal interpolasyonla 96 × 96 boyutuna büyüt. Her görüntü için haritanın toplamının sınırın
içine düşen payını hesapla. Test görüntüleri üzerinden payların ortalamasını ve karşılaştırma için
sınırın kapladığı görüntü payının ortalamasını bildir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki ortalamayı yazdır; haritaların sınır içindeki ortalama payını üç ondalık basamakla
"cevap" adıyla sakla.
Test: Her pay 0 ile 1 arasında olmalı ve hiçbir harita eğitim kipindeki bir ağdan hesaplanmamalı.
```

**Beklenen sonuç:** "cevap" = 0,317

## Durak 3: Kayma, izlem ve alt gruplar

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-09/ders.html#stop-3) · Python yolunda aynı sonuç: 8-10. bölümler*

Bu durak bir modelin güvenilir kalıp kalmadığını sorar. 8. haftanın göğüs ağrısı ünitesinde bir sınıflandırıcı, henüz hiçbir sonuç bilinmeden, B hastanesinin başvurularını A hastanesininkilerden ayırmayı öğrenir. Ardından B'de gözlenen ve beklenen olaylar geliş sırasıyla izlenir. Risk modeli bir taburculuk eşiğinde cinsiyet ve yaş gruplarında değerlendirilir; koroner arter hastalığı modeli de cinsiyetle ve cinsiyet olmadan kurulur.

### Adım 3.1: İki hastane birbirinden ayrılabiliyor mu?

**Amaç.** Bu adımda B hastanesinin başvurularını A hastanesininkilerden, hiçbir sonuç kullanmadan, girdilerine bakarak ayıran bir sınıflandırıcı eğitilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: A hastanesinin göğüs ağrısı ünitesi için kurulan bir risk modeli B hastanesinde
kullanılacak. Kurul, ilk sonuçlar gelmeden önce B'nin hastalarının ve kayıtlarının A'nınkilere
benzeyip benzemediğini ve nerede ayrıldıklarını öğrenmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin iki hastanesinden, yani sentetik
bir veri setinden göğüs ağrısıyla yapılmış başvurular bulunur: A hastanesinde 4.000, B hastanesinde
1.000 başvuru. Her satır bir başvurudur: "hastane" hastaneyi ("A" ya da "B"), "küme" kümesini (A'da
"eğitim", "doğrulama" ve "test"; B'de "B hastanesi") verir. Klinik tablo; "yaş" (yıl), "cinsiyet"
("erkek" ya da "kadın"), varsa 1 olan yedi risk faktörü ("sigara", "diyabet", "hipertansiyon",
"hiperlipidemi", "obezite", "aile öyküsü" ve "bilinen koroner arter hastalığı"), "kalp hızı"
(dakikada), "sistolik basınç" (mmHg) ve "eGFR" sütunlarını verir. Troponin, her hastanenin kendi
testinin üst referans sınırının katları olarak verilir: "gelişte troponin" ve ölçülmediğinde boş
kalan "bir saat sonra troponin". Yatak başı ekokardiyogram "ekokardiyogram yapıldı" (1 ya da 0)
sütununu ve yapıldıysa "ejeksiyon fraksiyonu" (%) ile "duvar hareket bozukluğu" (bölgesel bir
bozukluk görüldüyse 1) sütunlarını verir; yapılmadıysa bu iki sütun boştur. "triyaj notu" triyaj
hemşiresinin Türkçe notudur.
Görev: Her başvuru için MACE risk modelinin girdilerini oluştur: Klinik tablo (yaş, erkek için 1
olan cinsiyet, yedi risk faktörü, kalp hızı, sistolik basınç, eGFR); troponin (gelişteki troponinin
logaritması, ölçülmediyse gelişteki değerle bir saat sonraki troponinin logaritması, ölçülmediyse 0
ile bir saatteki değişim ve ikinci troponin ölçüldüyse 1); ekokardiyogram (ekokardiyogram yapıldı,
yapılmadıysa 60 ile ejeksiyon fraksiyonu, yapılmadıysa 0 ile duvar hareket bozukluğu); ve 20 sayı
olarak not (en az 3 notta geçen kelimelerin ve kelime çiftlerinin alt doğrusal terim sıklıklı TF-IDF
değerleri; A'nın eğitim notlarında öğrenilir ve aynı notlarda öğrenilen bir tekil değer ayrışımıyla
2026 seed değeriyle 20 bileşene indirilir). Ardından B hastanesini (1) A hastanesinden (0) ayıran,
sütunları standartlaştırılmış ve en fazla 5.000 yinelemeli bir lojistik regresyon kur; tahminleri
5.000 başvurunun tamamında, 2026 seed değeriyle karıştırılmış beş katlı tabakalı çapraz doğrulamadan
al ve AUC değerini hesapla. Her girdi grubunun sütunlarıyla tek başına tekrarla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Bütün girdiler ve her grup için AUC değerini göster; bütün girdilerle elde edilen AUC
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Hiçbir sonuç kullanılmamalı ve not modeli yalnızca A'nın eğitim notlarından öğrenmeli.
```

**Beklenen sonuç:** "cevap" = 0,988

### Adım 3.2: B hastanesinde gözlenen ve beklenen olaylar

**Amaç.** Bu adımda B hastanesinde gözlenen eksi beklenen olaylar geliş sırasıyla izlenir ve ilk alarm bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: A hastanesinin modeli artık B hastanesinde kullanılıyor ve hastaların sonuçları birbiri
ardına geliyor. Kurul, model gereğinden az ya da fazla olay beklediğinde alarm veren basit bir
grafik istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin ikinci hastanesi olan B
hastanesinden, yani sentetik bir veri setinden göğüs ağrısıyla yapılmış 1.000 başvuru, geliş
sırasıyla bulunur. Her satır bir başvurudur: "sıra" zamandaki yerini, "olasılık" birinci hastane
olan A'da öğrenmiş bir modelin 30 gün içinde majör olumsuz kardiyak olay için verdiği olasılığı
verir; "MACE" böyle bir olay görüldüyse 1, aksi hâlde 0 olur.
Görev: Başvuruları sıralarıyla ilerle. Her m başvurusundan sonra m'ye kadarki MACE toplamı eksi
olasılıkların toplamını ve m'ye kadarki p(1 − p) toplamının karekökünün 1,96 katı olan bandı
hesapla. Farkın bandın üstünde kaldığı ilk başvuruyu bul; farkı ve bandı sıraya karşı çiz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Grafiği göster, bütün başvurulardan sonraki farkı ve bandı yazdır; bandın üstündeki ilk
başvurunun sırasını "cevap" adıyla sakla.
Test: Bant 0'a yakın başlamalı ve başvuru sayısıyla genişlemeli.
```

**Beklenen sonuç:** "cevap" = 253

### Adım 3.3: Bir taburculuk eşiğinde alt gruplar

**Amaç.** Bu adımda doğrulama başvurularında bir taburculuk eşiği seçilir ve eşik test başvurularında cinsiyete ve yaşa göre değerlendirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, ortalamada güvenli olan bir taburculuk eşiğinin kadınlar, erkekler, 65 yaş altındaki
ve 65 yaş ve üstündeki hastalar için de güvenli olup olmadığını öğrenmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden 800 doğrulama ve 800 test başvurusu bulunur. Her satır bir
başvurudur: "küme" kümesini ("doğrulama" ya da "test"), "cinsiyet" cinsiyeti ("erkek" ya da
"kadın"), "yaş" yaşı (yıl), "olasılık" dersin eğitim başvurularıyla öğrenmiş bir modelinin 30 gün
içinde majör olumsuz kardiyak olay için verdiği olasılığı verir; "MACE" böyle bir olay görüldüyse 1,
aksi hâlde 0 olur.
Görev: Eşiği yalnızca doğrulama başvurularında seç: MACE görülen doğrulama başvurularının en fazla
yüzde 2'sinin eşikte ya da altında kaldığı en büyük olasılık. Eşikte ya da altında kalan başvurular
eve gönderilir. Test başvurularında hepsi, kadınlar, erkekler, 65 yaş altındaki ve 65 yaş ve
üstündeki hastalar için başvuru ve MACE sayısını, ROC eğrisi altındaki alanı (AUC), ortalama
olasılığı, gözlenen MACE oranını, eve gönderilenlerin sayısını, bunlardaki MACE sayısını ve
duyarlılığı hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her grup için bir satırdan oluşan bir tablo göster; kadınlardaki duyarlılığı üç ondalık
basamakla "cevap" adıyla sakla.
Test: Eşik yalnızca doğrulama başvurularından gelmeli.
```

**Beklenen sonuç:** "cevap" = 0,956

### Adım 3.4: Cinsiyet içermeyen bir model

**Amaç.** Bu adımda 2. haftanın lojistik regresyonu cinsiyetle ve cinsiyet olmadan kurulur ve kalibrasyonu ile hataları kadınlarda ve erkeklerde karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Biri, kadınlara ve erkeklere aynı biçimde davransın diye cinsiyetin koroner arter hastalığı
modelinden çıkarılmasını öneriyor. Kurul bunun kadınlar ve erkekler için tahminlere ne yapacağını
öğrenmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin Cleveland
verisinden, yani koroner anjiyografiye gönderilmiş hastalardan 303 hasta bulunur. Her satır bir
hastadır: "hasta" hastanın verideki numarasını (0-302), "küme" 2. haftanın kümesini verir ("eğitim",
227 hasta; "test", 76 hasta). Klinik değişkenler şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da
"kadın"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı" (egzersiz
testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi anjinaya yol
açtıysa 1), "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm) ve "göğüs ağrısı
tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"). "hastalık"
anjiyogramda koroner arter hastalığı görüldüyse 1, aksi hâlde 0 olur.
Görev: Tabloyu bu sırayla bir modelin sütunlarına dönüştür: Yaş, erkek için 1 ve kadın için 0 olan
cinsiyet, istirahat kan basıncı, kolesterol, en yüksek kalp hızı, egzersiz anjinası, ST çökmesi ve
atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ve 1 değerli üç sütun. Satırları tablonun
sırasında tut ve 303 hastanın tamamını kullan. Sütunları standartlaştırılmış ve en fazla 1.000
yinelemeli bir lojistik regresyonun 2026 seed değeriyle karıştırılmış beş katlı tabakalı çapraz
doğrulamasıyla her hasta için bir tahmin al; bunu bir kez cinsiyetle, bir kez de cinsiyet sütunu
olmadan yap. Kadınlar ve erkekler için ortalama tahmin edilen riski gözlenen hastalık oranıyla
karşılaştır; 0,5 olasılıkta duyarlılığı ve özgüllüğü hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her model ve cinsiyet için bir satırdan oluşan bir tablo göster; cinsiyet olmadan kadınlar
için ortalama tahmin edilen riski üç ondalık basamakla "cevap" adıyla sakla.
Test: Her tahmin, hastayı içermeyen bir kattan gelmeli.
```

**Beklenen sonuç:** "cevap" = 0,417

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

### Bir açıklamayı denetletmek

```text
Aşağıdaki kodu denetle; kod bir modelin hastalar için verdiği tahminleri açıklıyor ve sonucu
çiziyor. Yedi noktayı kontrol et. Her hasta kimlerle karşılaştırılıyor; arka plan tek bir yapay
satırdan değil de gerçek eğitim hastalarından mı oluşuyor? Kategorik bir değişkenin kukla sütunları
gibi tek bir değişkene ait sütunlar birlikte mi açıklanıyor? Seed değeri ya da örnek sayısı
değiştiğinde açıklama aynı kalıyor mu? Her belirginlik haritası, ağırlıkları rastgele hâle
getirilmiş bir ağla yapılan bir sağlamlık testinden geçmiş mi? Herhangi bir cümle bir katkıyı bir
neden ya da bir hasta için öneri olarak mı okuyor? Sonuçlar kadınlar, erkekler ve yaş grupları için
ayrıca bildiriliyor mu? Gerçek bir hastanın herhangi bir görüntüsü ya da kaydı kurum dışına
çıkabilir mi? Her nokta için ilgili satırı alıntıla, doğru olup olmadığını söyle ve doğru değilse
düzeltilmiş kodu ver.
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter defterinin 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Eko ağının doğruluğu

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, ekokardiyogramlarda düşük ejeksiyon fraksiyonunu işaretleyen bir ağı inceliyor ve
haritalara bakmadan önce ağın tek tek görüntülerdeki ve hastalardaki doğruluğunu aralıklarıyla
birlikte görmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda herkese açık bir ekokardiyogram veri seti olan
CAMUS'tan 600 görüntü, yani 300 hastanın apikal iki boşluk ve dört boşluk görüntüleri bulunur. Her
satır bir görüntüdür: "hasta" hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"), "küme" hastanın
kümesini ("eğitim", 200 hasta; "doğrulama", 50 hasta; "test", 50 hasta), "görüntü kalitesi" ise
uzmanların verdiği derecesini ("Good", "Medium" ya da "Poor") verir. "diyastol sonu" ve "sistol
sonu" sütunlarının her hücresi kareyi 0 ile 1 arasında değerler alan 96 × 96 piksellik bir görüntü
olarak tutar. "sınır" sütununun her hücresinde ise sol ventrikül kavitesinin ve miyokardın diyastol
sonu ya da sistol sonundaki uzman sınırı aynı boyutta yer alır: İçeride 1, dışarıda 0. "düşük
ejeksiyon fraksiyonu" hastanın ejeksiyon fraksiyonu yüzde 45'in altındaysa 1, aksi hâlde 0 olur.
Görev: Tek bir görüntü için diyastol sonu ve sistol sonu karelerini 96 × 96 piksellik iki kanal
olarak alan küçük bir evrişimli ağ kur. Ağda dört blok bulunsun; her blok, boyutu koruyan 3 × 3
çekirdekli bir evrişimden (sırasıyla 16, 32, 64 ve 64 kanal), batch normalizasyonundan, ReLU'dan ve
2 × 2 en büyük değer havuzlamasından oluşsun. Bloklardan sonra ağ her kanalın görüntü üzerindeki
ortalamasını alsın ve 0,3 oranında dropout uygulasın; tek çıktılı bir doğrusal katman da düşük
ejeksiyon fraksiyonunun logitini versin. Ağı eğitim görüntülerinde Adam (öğrenme hızı 0,001, ağırlık
azaltma 0,0001) ve ikili çapraz entropiyle, 32 görüntülük karıştırılmış gruplarla 30 epoch eğit. Her
grubu her yönde en fazla 4 piksel rastgele kaydır ve doğrulama görüntülerinde AUC değeri en iyi olan
epoch'un ağırlıklarını sakla. Ağ kütüphanesinin rastgele sayı üretecini ağı kurmadan önce ve
eğitimden önce yeniden 2026 ile başlat. AUC değerini test görüntülerinde ve her hastanın iki
görüntüsünün olasılıklarının ortalamasıyla test hastalarında hesapla. Her AUC değerine test
görüntülerinden ya da test hastalarından çekilen 2.000 bootstrap örneğinden, 2,5. ve 97,5.
yüzdelikler arasında bir yüzde 95 aralığı ver. Sonucun tekrarlanabilmesi için seed değerini 2026
olarak sabitle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki AUC değerini aralıklarıyla birlikte bir tabloda göster; görüntü düzeyindeki test AUC
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Epoch'u seçmek için hiçbir test görüntüsü kullanılmamalı ve hastaların bootstrap örnekleri
görüntüleri değil, hastaları çekmeli.
```

### Adım 2: Uzman sınırına karşı haritalar

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, ağın düşük ejeksiyon fraksiyonunu işaretlerken sol ventriküle bakıp bakmadığını ve
bunun ejeksiyon fraksiyonu düşük ve normal olan görüntüler, doğru ve yanlış tahminler ve görüntü
kalitesi dereceleri arasında değişip değişmediğini öğrenmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda herkese açık bir ekokardiyogram veri seti olan
CAMUS'tan dersin 100 test görüntüsü, yani 50 hastanın apikal iki boşluk ve dört boşluk görüntüleri
bulunur. Her satır bir görüntüdür: "hasta", "görüntü", "küme" ve "görüntü kalitesi" (uzmanların
verdiği derece: "Good", "Medium" ya da "Poor") görüntüyü tanımlar. "diyastol sonu" ve "sistol sonu"
kareleri 0 ile 1 arasında değerler alan 96 × 96 piksellik görüntüler olarak tutar; "sınır" sol
ventrikül kavitesinin ve miyokardın uzman sınırını aynı boyutta, içeride 1 ve dışarıda 0 olarak
tutar; "düşük ejeksiyon fraksiyonu" hastanın ejeksiyon fraksiyonu yüzde 45'in altındaysa 1 olur. İki
sütun, dersin eğitim görüntüleriyle eğitilmiş eko ağından gelir: "olasılık" ağın düşük ejeksiyon
fraksiyonu için verdiği olasılık, "harita" ise ağın son bloktaki Grad-CAM haritası, yani 0 ya da
daha büyük 96 × 96 değerden oluşan bir görüntüdür.
Görev: Her görüntü için üç ölçüt hesapla: "harita" toplamının "sınır" içine düşen payı; "harita"
sütununun en yüksek değerli pikseli "sınır" içindeyse 1, değilse 0; ve "sınır" sütununun görüntüde
kapladığı pay. Bir tahmin, düşük ejeksiyon fraksiyonlu bir görüntüde "olasılık" en az 0,5 olduğunda
ya da düşük ejeksiyon fraksiyonu olmayan bir görüntüde 0,5'in altında kaldığında doğrudur. Üç
ölçütün ortalamalarını bütün görüntüler, ejeksiyon fraksiyonu düşük ve normal olan görüntüler, doğru
ve yanlış tahminler ve her görüntü kalitesi derecesi için, her gruptaki görüntü sayısıyla birlikte
göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Grupların tablosunu göster; bütün görüntülerde sınır içindeki ortalama payı üç ondalık
basamakla "cevap" adıyla sakla.
Test: Her pay 0 ile 1 arasında olmalı ve her karşılaştırmadaki grupların toplamı 100 görüntü etmeli.
```

### Adım 3: Haritaların sağlamlık testleri

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, haritaların ağın öğrendiklerine bağlı olup olmadığını öğrenmek istiyor. Ağın
ağırlıkları rastgele değerlerle değiştirildiğinde aynı kalan bir harita modeli değil, görüntüyü
anlatır; tek bir rastgele çekiliş de yanıltabilir.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda herkese açık bir ekokardiyogram veri seti olan
CAMUS'tan 600 görüntü, yani 300 hastanın apikal iki boşluk ve dört boşluk görüntüleri bulunur. Her
satır bir görüntüdür: "hasta" hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"), "küme" hastanın
kümesini ("eğitim", 200 hasta; "doğrulama", 50 hasta; "test", 50 hasta), "görüntü kalitesi" ise
uzmanların verdiği derecesini ("Good", "Medium" ya da "Poor") verir. "diyastol sonu" ve "sistol
sonu" sütunlarının her hücresi kareyi 0 ile 1 arasında değerler alan 96 × 96 piksellik bir görüntü
olarak tutar. "sınır" sütununun her hücresinde ise sol ventrikül kavitesinin ve miyokardın diyastol
sonu ya da sistol sonundaki uzman sınırı aynı boyutta yer alır: İçeride 1, dışarıda 0. "düşük
ejeksiyon fraksiyonu" hastanın ejeksiyon fraksiyonu yüzde 45'in altındaysa 1, aksi hâlde 0 olur.
Görev: Tek bir görüntü için diyastol sonu ve sistol sonu karelerini 96 × 96 piksellik iki kanal
olarak alan küçük bir evrişimli ağ kur. Ağda dört blok bulunsun; her blok, boyutu koruyan 3 × 3
çekirdekli bir evrişimden (sırasıyla 16, 32, 64 ve 64 kanal), batch normalizasyonundan, ReLU'dan ve
2 × 2 en büyük değer havuzlamasından oluşsun. Bloklardan sonra ağ her kanalın görüntü üzerindeki
ortalamasını alsın ve 0,3 oranında dropout uygulasın; tek çıktılı bir doğrusal katman da düşük
ejeksiyon fraksiyonunun logitini versin. Ağı eğitim görüntülerinde Adam (öğrenme hızı 0,001, ağırlık
azaltma 0,0001) ve ikili çapraz entropiyle, 32 görüntülük karıştırılmış gruplarla 30 epoch eğit. Her
grubu her yönde en fazla 4 piksel rastgele kaydır ve doğrulama görüntülerinde AUC değeri en iyi olan
epoch'un ağırlıklarını sakla. Ağ kütüphanesinin rastgele sayı üretecini ağı kurmadan önce ve
eğitimden önce yeniden 2026 ile başlat. Her test görüntüsü için çıktının Grad-CAM haritasını son
bloğun ReLU katmanında, havuzlamadan önce hesapla. Bunun için çıktının bu katmandaki 12 × 12 boyutlu
64 öznitelik haritasına göre gradyanını al, her kanalın ortalama gradyanını o kanalın ağırlığı
olarak kullan ve 64 haritanın ağırlıklı toplamını oluştur. Toplamın yalnızca pozitif kısmını tut ve
çift doğrusal interpolasyonla 96 × 96 boyutuna büyüt. Her görüntü için haritanın toplamının sınırın
içine düşen payını hesapla. Ardından 1'den 20'ye kadar her seed değeri için şunu iki kez tekrarla:
Bir kez son bloğuna ve çıktı katmanına yeni rastgele ağırlıklar verilen bir kopya için, bir kez de
bütün katmanlarına yeni rastgele ağırlıklar verilen bir kopya için. Yeni ağırlıklar çekilmeden hemen
önce ağ kütüphanesinin rastgele sayı üretecini o seed değeriyle başlat ve eğitilmiş ağı
değiştirmeden tut. Kopya için aynı haritaları hesapla; her görüntü için eğitilmiş ağın haritasının
9.216 pikseli ile kopyanın haritasının pikselleri arasındaki Spearman sıra korelasyonunu ve kopyanın
haritasının sınır içindeki payını hesapla. İki haritadan biri her pikselde aynı değeri alıyorsa o
görüntüyü korelasyonun dışında bırak. Her kopya için ortalama sıra korelasyonunu, sınırın içindeki
ortalama payı ve boş harita sayısını kaydet. Her kopya türü için ortalama sıra korelasyonunun ve
sınırın içindeki ortalama payın 20 seed değeri üzerindeki medyanını ve aralığını, haritaların
yarısından fazlasının boş kaldığı seed değeri sayısını ve bunların yanında eğitilmiş ağın sınır
içindeki ortalama payını bildir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Sonuçları küçük bir tabloda göster; son bloğu rastgele olan kopyalar için ortalama sıra
korelasyonunun medyanını üç ondalık basamakla "cevap" adıyla sakla.
Test: Her sıra korelasyonu −1 ile 1 arasında olmalı ve eğitilmiş ağ, kopyalar alınmadan önce ve
sonra aynı haritaları vermeli.
```

### Adım 4: Kurul için altı görüntü

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kurul, ağın yanıldığı görüntüler de dahil olmak üzere birkaç görüntünün haritalarını uzman
sınırlarının yanında görmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda herkese açık bir ekokardiyogram veri seti olan
CAMUS'tan dersin 100 test görüntüsü, yani 50 hastanın apikal iki boşluk ve dört boşluk görüntüleri
bulunur. Her satır bir görüntüdür: "hasta", "görüntü", "küme" ve "görüntü kalitesi" (uzmanların
verdiği derece: "Good", "Medium" ya da "Poor") görüntüyü tanımlar. "diyastol sonu" ve "sistol sonu"
kareleri 0 ile 1 arasında değerler alan 96 × 96 piksellik görüntüler olarak tutar; "sınır" sol
ventrikül kavitesinin ve miyokardın uzman sınırını aynı boyutta, içeride 1 ve dışarıda 0 olarak
tutar; "düşük ejeksiyon fraksiyonu" hastanın ejeksiyon fraksiyonu yüzde 45'in altındaysa 1 olur. İki
sütun, dersin eğitim görüntüleriyle eğitilmiş eko ağından gelir: "olasılık" ağın düşük ejeksiyon
fraksiyonu için verdiği olasılık, "harita" ise ağın son bloktaki Grad-CAM haritası, yani 0 ya da
daha büyük 96 × 96 değerden oluşan bir görüntüdür.
Görev: Altı görüntü seç: Düşük ejeksiyon fraksiyonlu ve "olasılık" değeri en az 0,5 olan iki
görüntü, düşük ejeksiyon fraksiyonlu ve "olasılık" değeri 0,5'in altında olan bir görüntü, düşük
ejeksiyon fraksiyonu olmayan ve "olasılık" değeri en az 0,5 olan bir görüntü, düşük ejeksiyon
fraksiyonu olmayan ve "olasılık" değeri 0,5'in altında olan bir görüntü ve görüntü kalitesi "Poor"
olanlar arasında "olasılık" değeri en yüksek görüntü. Bunları üçer panelli iki satırda çiz: Diyastol
sonu karesi gri tonlarda, üstünde kısmen saydam ve sıcak bir renk ölçeğinde "harita", "sınır" ise
bir kontur çizgisi olarak. Her panelin başlığına hastayı, görüntüyü, olasılığı, gerçek sınıfı ve
haritanın sınır içindeki payını yaz; şeklin altına "CAMUS, CC BY-NC-SA 4.0" notunu ekle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Şekli göster; altı panelin hasta ve görüntülerini bir liste olarak "cevap" adıyla sakla.
Test: Altı panelden en az ikisi yanlış bir tahmini göstermeli.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
