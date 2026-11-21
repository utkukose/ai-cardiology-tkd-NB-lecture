# Prompt kütüphanesi, 11. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[11. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-11/PROMPTS.md)

Bu kütüphanede, 11. haftanın prompt (istem) yolundaki, yani Jupyter Notebook'un 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, Jupyter Notebook'ta aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir Jupyter Notebook'a ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Soru, veriler ve bir referans](#durak-1-soru-veriler-ve-bir-referans)
3. [Durak 2: Belirsizlik ve kalibrasyon](#durak-2-belirsizlik-ve-kalibrasyon)
4. [Durak 3: Dışlama ve sınırları](#durak-3-dışlama-ve-sınırları)
5. [Kodu onarmak, açıklatmak ve denetlemek için promptlar](#kodu-onarmak-açıklatmak-ve-denetlemek-için-promptlar)
6. [Haftalık projenin prompt yolu](#haftalık-projenin-prompt-yolu)

## Bir adım nasıl ilerler?

| Adım | Ne yapılır? |
|---|---|
| 1. Okuyun | Jupyter Notebook'ta adımın amacını okuyun. |
| 2. Veriyi hazırlayın | Promptun altındaki veri hücresini çalıştırın. Hücre, promptun tarif ettiği "veri" tablosunu hazırlar ve gösterir. |
| 3. Kopyalayın ve gönderin | Promptu kopyalayın ve bir YZ asistanına gönderin: Google Colab'daki Gemini ya da başka bir tarayıcı sekmesindeki ChatGPT, Claude, Copilot veya Gemini. |
| 4. Çalıştırın | Asistanın kodunu veri hücresinin altındaki hücreye yapıştırın ve çalıştırın. |
| 5. Denetleyin | Kontrol hücresini çalıştırın. Hücre *doğru* ya da *henüz değil* yazar ve "cevap" sonucunun değerini gösterir. |
| 6. Onarın | Kontrol *henüz değil* yazarsa onarım promptunu kodla birlikte gönderin. Sonuç yine yanlışsa doğru sonucu veren *Hazır kod* hücresini çalıştırın. |
| 7. Açıklatın ve kaydedin | Asistandan kodu sade bir dille açıklamasını isteyin; aracı, promptu ve neyin denetlendiğini YZ kullanım günlüğüne yazın. |

## Durak 1: Soru, veriler ve bir referans

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 11, 1-4. bölümler*

Bu durak, haftanın çözümlü projesi üzerinde final projeleri atölyesinin ilk yarısıdır. Cleveland hastalarının verileri denetlenir, on parametreli bir modelin ihtiyaç duyduğu büyüklük eğitim hastalarıyla karşılaştırılır ve yaş, cinsiyet ve göğüs ağrısı tipinden oluşan referans test hastalarında bir kez sınanır. Duraktan sonra aynı üç adım kendi final projenizin verileriyle tekrarlanır.

### Adım 1.1: Verilerin denetimi

**Amaç.** Bu adımda verilerin eksik değerleri sütun sütun sayılır ve projenin hangi sütunları kullandığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir kardiyolog, bazı hastaların anjiyografiye gönderilmesine gerek kalmasın diye egzersiz
testinden sonra koroner arter hastalığını dışlamayı amaçlayan bir final projesi planlıyor. Herhangi
bir modelden önce veriler denetlenir: Hangi sütunlarda eksik değer var ve bunlar kararın kendi
anında sahip olacağı sütunlar mı?
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 303 hasta, bütün sütunlarıyla birlikte bulunur. Her satır bir hastadır: "hasta" hastanın
verideki numarasını (0-302) verir. Projenin sekiz değişkeni şunlardır: "yaş" (yıl), "cinsiyet"
("erkek" ya da "kadın"), "göğüs ağrısı tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya
da "ağrı yok"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı"
(egzersiz testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi
anjinaya yol açtıysa 1) ve "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm).
Veri setinden beş sütun daha gelir: "açlık kan şekeri 120 üstü" (açlık kan şekeri 120 mg/dL'nin
üstündeyse 1), "istirahat EKG'si" (0 normal, 1 ST segmenti ya da T dalgası bozukluğu, 2 sol
ventrikül hipertrofisi), "ST eğimi" (egzersizin doruğunda ST segmentinin eğimi: 1 yukarı, 2 düz, 3
aşağı), "floroskopide damar" (floroskopiyle boyanan ana damar sayısı, 0-3) ve "talyum sintigrafisi"
(3 normal, 6 sabit defekt, 7 geri dönüşlü defekt). Boş bir hücre eksik bir değerdir. "hastalık",
anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden fazla daralma görüldüyse 1, aksi
hâlde 0 olur.
Görev: "hasta" dışındaki her sütunun eksik değerlerini say. Proje dokuz sütun kullanır; bunlar sekiz
değişken ve "hastalık" sütunudur. Her sütun için projenin onu kullanıp kullanmadığını işaretle ve
projenin kullanmadığı sütunlardaki eksik değerleri topla. Ayrıca hasta sayısını, hastalığı olanların
sayısını ve oranlarını ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her sütunun eksik değerlerini ve projenin o sütunu kullanıp kullanmadığını bir tabloda
göster, hasta sayılarını yazdır; projenin kullanmadığı sütunlardaki eksik değer sayısını "cevap"
adıyla sakla.
Test: Projenin kullandığı dokuz sütunda hiç eksik değer olmamalı ve tablo 303 hasta içermeli.
```

**Beklenen sonuç:** "cevap" = 6

### Adım 1.2: Modelin ihtiyaç duyduğu veri

**Amaç.** Bu adımda Riley ve arkadaşlarının ölçütlerine göre on parametreli bir modelin ihtiyaç duyduğu üç en küçük büyüklük hesaplanır ve eğitim hastalarının sayısıyla karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Projenin tam modelinin on parametresi vardır: Yedi değişken ve göğüs ağrısı tipi için üç
sütun. Kardiyolog 227 eğitim hastasının yeterli olup olmadığını öğrenmek istiyor ve öngörülen değer
olarak yaş, cinsiyet ve göğüs ağrısı tipinden oluşan referansın R kare değerini alıyor.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 227 eğitim hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki
numarasını, "olasılık, referans" ise dersin bir referans modelinin, yani yaş, cinsiyet ve göğüs
ağrısı tipiyle kurulan bir lojistik regresyonun, aynı hastalarda kurulduktan sonra hastaya verdiği
koroner arter hastalığı olasılığını verir. "hastalık", anjiyogramda en az bir ana koroner arterde
çapın yüzde 50'sinden fazla daralma görüldüyse 1, aksi hâlde 0 olur.
Görev: Olasılıkların Cox-Snell R kare değerini hesapla: Olasılıkların log-olabilirliğini, yani her
hastada hastanın sahip olduğu sonuca verilen olasılığın doğal logaritmasının toplamını ve her
hastaya genel hastalık oranını veren bir modelin log-olabilirliğini al; R kare, boş modelin
değerinden modelin değeri çıkarılarak bulunan farkın iki katının hasta sayısına bölümünün üstelinin
birden çıkarılmasıyla elde edilir. Ardından Riley ve arkadaşlarının 10 parametreli bir model için üç
en küçük büyüklüğünü hesapla. Hastalık oranının izin verdiği en büyük R kare, genel oranın
log-olabilirliğinin iki katının hasta sayısına bölümünün üstelinin birden çıkarılmasıyla bulunur.
0,9 büzülme için (i) büyüklüğü, 10'un, (0,9 eksi 1) ile bir eksi R karenin 0,9'a bölümünün doğal
logaritmasının çarpımına bölümüdür. (ii) büyüklüğü aynı formülü kullanır; yalnızca büzülmenin yerine
R karenin, R kare ile en büyük R karenin 0,05 katının toplamına bölümü konur. (iii) büyüklüğü (1,96
bölü 0,05) karesinin hastalık oranıyla ve bir eksi oranla çarpımıdır. Her büyüklüğü tam bir hastaya
yukarı yuvarla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Cox-Snell R kare değerini, en büyük R kareyi, üç büyüklüğü ve eğitim hastası sayısını yazdır;
(i) büyüklüğünü "cevap" adıyla sakla.
Test: R kare 0 ile en büyük R kare arasında olmalı ve (iii) büyüklüğü olasılıklara bağlı olmamalı.
```

**Beklenen sonuç:** "cevap" = 241

### Adım 1.3: Test hastalarında referans

**Amaç.** Bu adımda yaş, cinsiyet ve göğüs ağrısı tipinden oluşan referans model eğitim hastalarında kurulur ve test hastalarında bir kez sınanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog egzersiz testinin sonuçlarının yardımcı olup olmadığını sormadan önce, projenin
aşması gereken çıtaya ihtiyacı vardır. Bu çıta, kardiyoloğun testten önce bildiği yaş, cinsiyet ve
göğüs ağrısı tipidir.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 303 hasta bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını (0-302),
"küme" 2. haftanın kümesini verir ("eğitim", 227 hasta; "test", 76 hasta). Klinik değişkenler
şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da "kadın"), "göğüs ağrısı tipi" ("tipik anjina",
"atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"), "istirahat kan basıncı" (mmHg), "kolesterol"
(mg/dL), "en yüksek kalp hızı" (egzersiz testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz
anjinası" (egzersiz testi anjinaya yol açtıysa 1) ve "ST çökmesi" (egzersizde ST segmentinin
istirahate göre çökmesi, mm). "hastalık", anjiyogramda en az bir ana koroner arterde çapın yüzde
50'sinden fazla daralma görüldüyse 1, aksi hâlde 0 olur.
Görev: Referansın girdilerini hazırla. Girdiler yaş, erkekler için 1 ve kadınlar için 0 olan bir
sütun ve atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ile 1 değerlerinden oluşan üç sütundur;
böylece tipik anjina referans kategori olur. Her girdiyi eğitim hastalarının ortalaması ve standart
sapmasıyla bir z-skoruna dönüştür ve hastalık için olağan lojistik regresyonu, standart ayarlarıyla
ve en fazla 1.000 yinelemeyle, yalnızca eğitim hastalarında kur. Her test hastası için hastalık
olasılığını ve test hastalarındaki ROC eğrisi altındaki alanı (AUC) hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitim ve test hastalarının sayısını ve referansın test AUC değerini yazdır; AUC değerini üç
ondalık basamakla "cevap" adıyla sakla.
Test: Model yalnızca 227 eğitim hastasında kurulmalı ve AUC 0,5 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,9

## Durak 2: Belirsizlik ve kalibrasyon

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/ders.html#stop-2) · Python yolunda aynı sonuç: 5. ve 6. bölümler*

Bu durak sonuçlardan ne kadar emin olunabileceğini sorar. Bootstrap yöntemi, referansın ve tam modelin AUC değerlerinin ve aynı yeniden örneklemlerdeki farklarının aralıklarını verir; kalibrasyon eğimi ise tam modelin olasılıklarının test hastalarında tutup tutmadığını sorar.

### Adım 2.1: İki AUC değerinin aralıkları

**Amaç.** Bu adımda referansın ve tam modelin test AUC değerleri bootstrap aralıklarıyla birlikte verilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Final projesinin raporu her sonucu belirsizliğiyle birlikte verir. 76 test hastasıyla
kardiyolog, aynı türden başka hastalarla her AUC değerinin ne kadar değişebileceğini öğrenmek
istiyor.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 76 test hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını,
"olasılık, referans" dersin bir referans modelinin (yaş, cinsiyet ve göğüs ağrısı tipiyle kurulan
bir lojistik regresyon) verdiği koroner arter hastalığı olasılığını, "olasılık, model" ise dersin
tam modelinin (buna istirahat kan basıncı, kolesterol ve egzersiz testinin üç sonucu eklenmiş hâli)
verdiği olasılığı gösterir. İki model de yalnızca 227 eğitim hastasında kurulmuştur. "hastalık",
anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden fazla daralma görüldüyse 1, aksi
hâlde 0 olur.
Görev: Test hastalarından 2.000 yeniden örneklem çek: Her yeniden örneklem, 2026 seed değeriyle
başlatılan bir rastgele sayı üreteciyle, tablodaki hasta sayısı kadar hastayı yerine koyarak çeker.
Yalnızca tek bir sonucun hastalarını içeren yeniden örneklemi atla. Her yeniden örneklemde aynı
hastalarda referansın ve modelin ROC eğrisi altındaki alanını (AUC) ve farklarını (model eksi
referans) hesapla. Bir sonucun yüzde 95'lik aralığı, değerlerinin yeniden örneklemler boyunca 2,5.
yüzdeliğinden 97,5. yüzdeliğine uzanır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kullanılan yeniden örneklem sayısını ve her modelin ve farkın bütün test hastalarındaki AUC
değerini 2,5. ve 97,5. yüzdelikleriyle veren bir tabloyu yazdır; modelin AUC değerinin 2,5.
yüzdeliğini üç ondalık basamakla "cevap" adıyla sakla.
Test: Her aralık bütün test hastalarındaki AUC değerini içermeli ve aynı yeniden örneklemler iki
model için de kullanılmalı.
```

**Beklenen sonuç:** "cevap" = 0,872

### Adım 2.2: Kazancın aralığı

**Amaç.** Bu adımda tam model ile referans arasındaki fark, aynı yeniden örneklemlerde hesaplanan bootstrap aralığıyla birlikte verilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Projenin sorusu, egzersiz testinin sonuçlarının kardiyoloğun testten önce bildiklerine bir
şey katıp katmadığıdır. Cevap yan yana konan iki AUC değeri değil, farkın aralığıdır.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 76 test hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını,
"olasılık, referans" dersin bir referans modelinin (yaş, cinsiyet ve göğüs ağrısı tipiyle kurulan
bir lojistik regresyon) verdiği koroner arter hastalığı olasılığını, "olasılık, model" ise dersin
tam modelinin (buna istirahat kan basıncı, kolesterol ve egzersiz testinin üç sonucu eklenmiş hâli)
verdiği olasılığı gösterir. İki model de yalnızca 227 eğitim hastasında kurulmuştur. "hastalık",
anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden fazla daralma görüldüyse 1, aksi
hâlde 0 olur.
Görev: Test hastalarından 2.000 yeniden örneklem çek: Her yeniden örneklem, 2026 seed değeriyle
başlatılan bir rastgele sayı üreteciyle, tablodaki hasta sayısı kadar hastayı yerine koyarak çeker.
Yalnızca tek bir sonucun hastalarını içeren yeniden örneklemi atla. Her yeniden örneklemde aynı
hastalarda referansın ve modelin ROC eğrisi altındaki alanını (AUC) ve farklarını (model eksi
referans) hesapla. Bir sonucun yüzde 95'lik aralığı, değerlerinin yeniden örneklemler boyunca 2,5.
yüzdeliğinden 97,5. yüzdeliğine uzanır. Ayrıca farkın 0 ya da daha küçük olduğu yeniden
örneklemlerin payını ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Üç sonucun aralıklarıyla birlikte tablosunu ve modelin daha iyi olmadığı yeniden
örneklemlerin payını yazdır; farkın 2,5. yüzdeliğini üç ondalık basamakla "cevap" adıyla sakla.
Test: Fark her yeniden örneklemde o yeniden örneklemin iki AUC değerinden hesaplanmalı; iki ayrı
yeniden örneklem kümesinden hesaplanmamalı.
```

**Beklenen sonuç:** "cevap" = −0,02

### Adım 2.3: Test hastalarında kalibrasyon

**Amaç.** Bu adımda tam modelin test hastalarındaki kalibrasyon sabiti ve eğimi hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir dışlama olasılıkların kendisini kullanır. Kardiyolog, olasılıkların ortalamada doğru
olup olmadığını ve fazla uç ya da fazla ılımlı olup olmadıklarını öğrenmek istiyor.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 76 test hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını,
"olasılık, model" ise dersin sekiz klinik değişkenle ve yalnızca 227 eğitim hastasında kurulan bir
lojistik regresyonunun verdiği koroner arter hastalığı olasılığını gösterir. "hastalık",
anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden fazla daralma görüldüyse 1, aksi
hâlde 0 olur.
Görev: Her olasılığı log-odds değerine, yani olasılığın bir eksi olasılığa bölümünün doğal
logaritmasına dönüştür. Kalibrasyon sabiti, hastalık için yalnızca bir sabit terim içeren ve
log-odds değerini sabit bir kayma olarak alan bir lojistik regresyondan gelir. Kalibrasyon eğimi ise
hastalık için bir sabit terim ve tek girdi olarak log-odds içeren bir lojistik regresyonda log-odds
değerinin katsayısıdır. İkisini de hiçbir ceza terimi olmadan, örneğin Newton adımlarıyla kur.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ortalama olasılığı, gözlenen hastalık oranını, kalibrasyon sabitini ve kalibrasyon eğimini
yazdır; eğimi üç ondalık basamakla "cevap" adıyla sakla.
Test: Kusursuz kalibre edilmiş bir model 0 sabit ve 1 eğim verirdi; sabitin işareti, gözlenen oran
eksi ortalama olasılık farkının işaretiyle aynı olmalı.
```

**Beklenen sonuç:** "cevap" = 1,241

## Durak 3: Dışlama ve sınırları

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/ders.html#stop-3) · Python yolunda aynı sonuç: 7-10. bölümler*

Bu durak olasılıkları bir karara dönüştürür. Dışlama eşiği eğitim hastalarının çapraz doğrulama olasılıklarında seçilir; test hastaları bu eşiğin kaç sevki önleyeceğini, test kümesindeki kadınlar ve erkekler de dışlamanın iki grupta da güvenli sayılıp sayılamayacağını gösterir.

### Adım 3.1: Dışlama eşiği

**Amaç.** Bu adımda dışlama eşiği eğitim hastalarının çapraz doğrulama olasılıklarında seçilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Eşiğin altındaki bir hasta anjiyografiye gönderilmezdi; bu yüzden eşik çok yüksek bir
duyarlılığı korumalıdır: Hastalığı olanların en az yüzde 95'i eşikte ya da eşiğin üstünde
kalmalıdır. Test hastaları bu seçimde hiçbir rol oynamamalıdır.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 227 eğitim hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki
numarasını, "olasılık, çapraz doğrulama" ise dersin sekiz klinik değişkenle kurulan bir lojistik
regresyonunun beş katlı çapraz doğrulamayla hesaplanan koroner arter hastalığı olasılığını verir:
Her hasta, eğitim hastalarının öteki beşte dördünde kurulmuş bir modelin olasılığını alır.
"hastalık", anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden fazla daralma
görüldüyse 1, aksi hâlde 0 olur.
Görev: 0,01, 0,02 ve bu biçimde 0,50'ye kadar giden eşikler arasından, hastalığı olan eğitim
hastalarının en az yüzde 95'inin olasılığının ona eşit ya da ondan büyük olduğu en yüksek eşiği al.
Bu eşikteki duyarlılığı ve olasılığı eşiğin altında kalan eğitim hastalarının payını ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eşiği, eğitim hastalarındaki duyarlılığı ve dışlanan payı yazdır; eşiği iki ondalık basamakla
"cevap" adıyla sakla.
Test: Eşikteki duyarlılık en az 0,95 olmalı; ızgaradaki bir sonraki eşikte ise 0,95'in altına
düşmeli.
```

**Beklenen sonuç:** "cevap" = 0,18

### Adım 3.2: Test hastalarında dışlama

**Amaç.** Bu adımda eşik test hastalarına bir kez uygulanır ve duyarlılık, özgüllük ve negatif öngörü değeri Wilson aralıklarıyla birlikte verilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog, dışlamanın kaç sevki önleyeceğini, hastalığı olan herhangi bir hastayı kaçırıp
kaçırmadığını ve 76 hastayla bu sayılardan ne kadar emin olunabileceğini öğrenmek istiyor.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 76 test hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını,
"olasılık, model" ise dersin sekiz klinik değişkenle ve yalnızca 227 eğitim hastasında kurulan bir
lojistik regresyonunun verdiği koroner arter hastalığı olasılığını gösterir. "hastalık",
anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden fazla daralma görüldüyse 1, aksi
hâlde 0 olur. Projenin eğitim hastalarında seçilen dışlama eşiği 0,18 değerindedir: Olasılığı bu
eşiğin altında kalan bir hasta anjiyografiye gönderilmezdi.
Görev: Olasılığı eşiğin altında kalan hasta dışlanır. Dışlananlar ve sevk edilenler arasında
hastalığı olan ve olmayan hastaları say; duyarlılığı, özgüllüğü ve negatif öngörü değerini, yani
dışlanan hastalar arasında hastalığı olmayanların payını hesapla. Her oranı yüzde 95'lik Wilson
aralığıyla ver: n hastanın k tanesi için, z = 1,96 olmak üzere merkez (k/n artı z kare bölü 2n) bölü
(1 artı z kare bölü n), yarı genişlik ise z çarpı (k/n çarpı bir eksi k/n, bölü n, artı z kare bölü
4n kare) değerinin karekökü, bölü (1 artı z kare bölü n) olur.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Dört sayının tablosunu göster, üç oranı Wilson aralıklarıyla birlikte yazdır; dışlanan hasta
sayısını "cevap" adıyla sakla.
Test: Dört sayının toplamı 76 olmalı ve her aralık 0 ile 1 arasında kalıp kendi oranını içermeli.
```

**Beklenen sonuç:** "cevap" = 27

### Adım 3.3: Kadınlar ve erkekler

**Amaç.** Bu adımda dışlamanın kadınlardaki ve erkeklerdeki duyarlılığı Wilson aralıklarının alt sınırlarıyla birlikte verilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir dışlama kullanıldığı her grupta güvenli olmalıdır. Test kümesinde kadınlar erkeklerden
azdır ve kadınların daha azında hastalık vardır.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 76 test hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını,
"cinsiyet" "erkek" ya da "kadın" değerini, "olasılık, model" ise dersin sekiz klinik değişkenle ve
yalnızca 227 eğitim hastasında kurulan bir lojistik regresyonunun verdiği koroner arter hastalığı
olasılığını gösterir. "hastalık", anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden
fazla daralma görüldüyse 1, aksi hâlde 0 olur. Projenin eğitim hastalarında seçilen dışlama eşiği
0,18 değerindedir.
Görev: Kadınlar ve erkekler için ayrı ayrı hastaları, hastalığı olanları, hastalığı olup eşikte ya
da eşiğin üstünde kalanları ve dışlananları say; duyarlılığı hesapla. Her oranı yüzde 95'lik Wilson
aralığıyla ver: n hastanın k tanesi için, z = 1,96 olmak üzere merkez (k/n artı z kare bölü 2n) bölü
(1 artı z kare bölü n), yarı genişlik ise z çarpı (k/n çarpı bir eksi k/n, bölü n, artı z kare bölü
4n kare) değerinin karekökü, bölü (1 artı z kare bölü n) olur.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her cinsiyet için bir satırdan oluşan ve duyarlılığın Wilson aralığının alt sınırını içeren
bir tablo göster; kadınlar için alt sınırı üç ondalık basamakla "cevap" adıyla sakla.
Test: İki satırın hastalarının toplamı 76 olmalı ve 1 olan bir duyarlılığın üst sınırı 1 olmalı.
```

**Beklenen sonuç:** "cevap" = 0,646

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
Aşağıdaki kod bir Jupyter Notebook'ta çalıştırıldığında altta verilen hata mesajını veriyor. Hatanın
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

### Bir final projesini denetletmek

```text
Aşağıdaki kodu denetle; kod, hekimlere yönelik bir yapay zekâ eğitiminin bir final projesinin
analizidir. Yedi noktayı kontrol et. Her girdi klinik karar anında biliniyor mu, yoksa girdilerden
biri daha sonraki bir tetkikten mi geliyor? Test kümesi, bütün seçimler eğitim verilerinde
yapıldıktan sonra bir kez mi açılmış? Sonucu olan hasta sayısı modelin parametre sayısı için
yeterince büyük mü? Model aynı test hastalarında basit bir referansla karşılaştırılmış mı? Her sonuç
bir aralık taşıyor mu ve referansa göre kazanç, aynı yeniden örneklemlerde hesaplanmış bir farkın
aralığı olarak mı verilmiş? Karar eşiği yalnızca eğitim verilerinde mi seçilmiş? Herhangi bir satır
hastaların verilerini bu bilgisayarın dışına gönderiyor mu? Her nokta için kodda bunu gösteren
satırla birlikte evet, hayır ya da belirsiz diye cevap ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter Notebook'un 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Verilerin denetimi ve ayırma

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir kardiyolog, egzersiz testinden sonra koroner arter hastalığını dışlamayı amaçlayan bir
final projesi kuruyor. Herhangi bir modelden önce veriler denetlenir ve bir kez eğitim ve test
hastalarına ayrılır. Kendi final projeniz için Veri satırını kendi tablonuza göre yeniden yazın:
Sütunları, birimlerini ve sonucun anlamını kelimelerle anlatın; hiçbir zaman bir hastanın satırını
eklemeyin.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 303 hasta, bütün sütunlarıyla birlikte bulunur. Her satır bir hastadır: "hasta" hastanın
verideki numarasını (0-302) verir. Projenin sekiz değişkeni şunlardır: "yaş" (yıl), "cinsiyet"
("erkek" ya da "kadın"), "göğüs ağrısı tipi" ("tipik anjina", "atipik anjina", "anjina dışı ağrı" ya
da "ağrı yok"), "istirahat kan basıncı" (mmHg), "kolesterol" (mg/dL), "en yüksek kalp hızı"
(egzersiz testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz anjinası" (egzersiz testi
anjinaya yol açtıysa 1) ve "ST çökmesi" (egzersizde ST segmentinin istirahate göre çökmesi, mm).
Veri setinden beş sütun daha gelir: "açlık kan şekeri 120 üstü" (açlık kan şekeri 120 mg/dL'nin
üstündeyse 1), "istirahat EKG'si" (0 normal, 1 ST segmenti ya da T dalgası bozukluğu, 2 sol
ventrikül hipertrofisi), "ST eğimi" (egzersizin doruğunda ST segmentinin eğimi: 1 yukarı, 2 düz, 3
aşağı), "floroskopide damar" (floroskopiyle boyanan ana damar sayısı, 0-3) ve "talyum sintigrafisi"
(3 normal, 6 sabit defekt, 7 geri dönüşlü defekt). Boş bir hücre eksik bir değerdir. "hastalık",
anjiyogramda en az bir ana koroner arterde çapın yüzde 50'sinden fazla daralma görüldüyse 1, aksi
hâlde 0 olur.
Görev: Hasta sayısını, hastalığı olanların sayısını ve oranını ve her sütunun eksik değerlerini ver.
Ardından hastaları, bir hastanın bütün satırları aynı kümede kalacak biçimde bir kez ayır: Dörtte
biri test için ayrılsın, iki kümede hastalık oranı aynı olsun ve rastgele sayılar için 2026 seed
değeri kullanılsın. Her kümedeki hasta sayısını ve hastalığı olan hasta sayısını ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eksik değerlerin tablosunu ve iki kümenin tablosunu göster; hastalığı olan test hastalarının
sayısını "cevap" adıyla sakla.
Test: İki küme bütün hastaları kapsamalı ve hiçbir hasta iki kümede birden bulunmamalı.
```

### Adım 2: Bir referans, model ve kazancın aralığı

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog tam modeli, egzersiz testinden önce bilinenlerle aynı test hastalarında
karşılaştırıyor ve kazancı aralığıyla birlikte veriyor.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 303 hasta bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını (0-302),
"küme" 2. haftanın kümesini verir ("eğitim", 227 hasta; "test", 76 hasta). Klinik değişkenler
şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da "kadın"), "göğüs ağrısı tipi" ("tipik anjina",
"atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"), "istirahat kan basıncı" (mmHg), "kolesterol"
(mg/dL), "en yüksek kalp hızı" (egzersiz testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz
anjinası" (egzersiz testi anjinaya yol açtıysa 1) ve "ST çökmesi" (egzersizde ST segmentinin
istirahate göre çökmesi, mm). "hastalık", anjiyogramda en az bir ana koroner arterde çapın yüzde
50'sinden fazla daralma görüldüyse 1, aksi hâlde 0 olur.
Görev: Referansın girdilerini hazırla. Girdiler yaş, erkekler için 1 ve kadınlar için 0 olan bir
sütun ve atipik anjina, anjina dışı ağrı ve ağrı yok için 0 ile 1 değerlerinden oluşan üç sütundur;
böylece tipik anjina referans kategori olur. Her girdiyi eğitim hastalarının ortalaması ve standart
sapmasıyla bir z-skoruna dönüştür ve hastalık için olağan lojistik regresyonu, standart ayarlarıyla
ve en fazla 1.000 yinelemeyle, yalnızca eğitim hastalarında kur. Tam model aynı girdileri kullanır
ve bunlara istirahat kan basıncını, kolesterolü, en yüksek kalp hızını, egzersiz anjinasını ve ST
çökmesini ekler; aynı yolla kurulur. Her test hastası için iki modelin hastalık olasılığını ve test
hastalarındaki AUC değerlerini hesapla. Test hastalarından 2.000 yeniden örneklem çek: Her yeniden
örneklem, 2026 seed değeriyle başlatılan bir rastgele sayı üreteciyle, tablodaki hasta sayısı kadar
hastayı yerine koyarak çeker. Yalnızca tek bir sonucun hastalarını içeren yeniden örneklemi atla.
Her yeniden örneklemde aynı hastalarda referansın ve modelin ROC eğrisi altındaki alanını (AUC) ve
farklarını (model eksi referans) hesapla. Bir sonucun yüzde 95'lik aralığı, değerlerinin yeniden
örneklemler boyunca 2,5. yüzdeliğinden 97,5. yüzdeliğine uzanır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki modelin ve farkın AUC değerlerini aralıklarıyla birlikte bir tabloda göster; farkın 2,5.
yüzdeliğini üç ondalık basamakla "cevap" adıyla sakla.
Test: Hiçbir test hastası iki modelden birini kurmak için kullanılmamalı ve iki model aynı yeniden
örneklemlerde değerlendirilmeli.
```

### Adım 3: Kalibrasyon ve karar eşiği

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog, tam modelin dışlama eşiğini eğitim hastalarında seçiyor ve test hastaları
açılmadan önce kalibrasyonu denetliyor.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 303 hasta bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını (0-302),
"küme" 2. haftanın kümesini verir ("eğitim", 227 hasta; "test", 76 hasta). Klinik değişkenler
şunlardır: "yaş" (yıl), "cinsiyet" ("erkek" ya da "kadın"), "göğüs ağrısı tipi" ("tipik anjina",
"atipik anjina", "anjina dışı ağrı" ya da "ağrı yok"), "istirahat kan basıncı" (mmHg), "kolesterol"
(mg/dL), "en yüksek kalp hızı" (egzersiz testinde ulaşılan en yüksek kalp hızı, dakikada), "egzersiz
anjinası" (egzersiz testi anjinaya yol açtıysa 1) ve "ST çökmesi" (egzersizde ST segmentinin
istirahate göre çökmesi, mm). "hastalık", anjiyogramda en az bir ana koroner arterde çapın yüzde
50'sinden fazla daralma görüldüyse 1, aksi hâlde 0 olur.
Görev: 2. adımdaki tam modeli eğitim hastalarında beş katlı çapraz doğrulamayla kur; katlar aynı
hastalık oranıyla ve 2026 seed değeriyle çekilsin; böylece her eğitim hastası onu görmemiş bir
modelin olasılığını alsın. Bu olasılıklarda kalibrasyon sabitini ve eğimini 2. duraktaki gibi
hesapla; 0,01, 0,02 ve bu biçimde 0,50'ye kadar giden eşikler arasından, hastalığı olan eğitim
hastalarının en az yüzde 95'inin olasılığının ona eşit ya da ondan büyük olduğu en yüksek eşiği seç.
Ardından tam modeli bütün eğitim hastalarında kur, eşiği test hastalarına bir kez uygula ve dışlanan
hastaları hastalığı olan ve olmayan olarak say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Çapraz doğrulama olasılıklarının kalibrasyonunu, eşiği ve test hastalarındaki sayıları
yazdır; dışlanan test hastalarının sayısını "cevap" adıyla sakla.
Test: Eşik herhangi bir test hastası kullanılmadan seçilmeli ve eşikteki eğitim duyarlılığı en az
0,95 olmalı.
```

### Adım 4: Rapor için sonuç tablosu

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Final projesinin raporu TRIPOD+AI'ı izler: Her sonuç, hem bütün hastalarda hem de modelin
kullanılacağı gruplarda aralığıyla birlikte verilir.
Veri: Jupyter Notebook'ta "veri" adlı bir tablo vardır. Tabloda UCI Heart Disease veri setinin
Cleveland verisinden, yani bir egzersiz testinden sonra koroner anjiyografiye gönderilmiş
hastalardan 76 test hastası bulunur. Her satır bir hastadır: "hasta" hastanın verideki numarasını,
"cinsiyet" "erkek" ya da "kadın" değerini, "olasılık, referans" dersin bir referans modelinin (yaş,
cinsiyet ve göğüs ağrısı tipiyle kurulan bir lojistik regresyon) verdiği koroner arter hastalığı
olasılığını, "olasılık, model" ise dersin tam modelinin (buna istirahat kan basıncı, kolesterol ve
egzersiz testinin üç sonucu eklenmiş hâli) verdiği olasılığı gösterir. İki model de yalnızca 227
eğitim hastasında kurulmuştur. "hastalık", anjiyogramda en az bir ana koroner arterde çapın yüzde
50'sinden fazla daralma görüldüyse 1, aksi hâlde 0 olur. Projenin eğitim hastalarında seçilen
dışlama eşiği 0,18 değerindedir.
Görev: Test hastalarından 2.000 yeniden örneklem çek: Her yeniden örneklem, 2026 seed değeriyle
başlatılan bir rastgele sayı üreteciyle, tablodaki hasta sayısı kadar hastayı yerine koyarak çeker.
Yalnızca tek bir sonucun hastalarını içeren yeniden örneklemi atla. Her yeniden örneklemde aynı
hastalarda referansın ve modelin ROC eğrisi altındaki alanını (AUC) ve farklarını (model eksi
referans) hesapla. Bir sonucun yüzde 95'lik aralığı, değerlerinin yeniden örneklemler boyunca 2,5.
yüzdeliğinden 97,5. yüzdeliğine uzanır. Ardından 0,18 dışlama eşiğinde duyarlılığı, özgüllüğü ve
negatif öngörü değerini bütün test hastaları, kadınlar ve erkekler için hesapla. Her oranı yüzde
95'lik Wilson aralığıyla ver: n hastanın k tanesi için, z = 1,96 olmak üzere merkez (k/n artı z kare
bölü 2n) bölü (1 artı z kare bölü n), yarı genişlik ise z çarpı (k/n çarpı bir eksi k/n, bölü n,
artı z kare bölü 4n kare) değerinin karekökü, bölü (1 artı z kare bölü n) olur. Bütün sonuçları
sonuç, grup, değer, alt sınır ve üst sınır sütunlarından oluşan ve rapora kopyalanmaya hazır tek bir
tabloya yaz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Tabloyu göster; bütün test hastalarındaki negatif öngörü değerinin alt sınırını üç ondalık
basamakla "cevap" adıyla sakla.
Test: Her aralık kendi değerini içermeli ve 0 ile 1 arasında kalmalı; yalnızca AUC farkının aralığı
negatif olabilir.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
