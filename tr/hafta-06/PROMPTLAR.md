# Prompt kütüphanesi, 6. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[6. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-06/PROMPTS.md)

Bu kütüphanede, 6. haftanın prompt (istem) yolundaki, yani Jupyter Notebook'un 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, Jupyter Notebook'ta aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir Jupyter Notebook'a ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Epikrizlerden altı tanı: Kurallar ve bir model](#durak-1-epikrizlerden-altı-tanı-kurallar-ve-bir-model)
3. [Durak 2: Mini proje: NER pipeline ile STEMI, AF ve kalp yetersizliği](#durak-2-mini-proje-ner-pipeline-ile-stemi-af-ve-kalp-yetersizliği)
4. [Durak 3: Anjiyografi raporları: Darlık derecesi ve damar](#durak-3-anjiyografi-raporları-darlık-derecesi-ve-damar)
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

## Durak 1: Epikrizlerden altı tanı: Kurallar ve bir model

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-06/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 6, 1-5. bölümler*

Altı kronik tanı sanal kliniğin epikrizlerinden okunur: Önce tanıların kelimeleri aranır, sonra her geçişin durumu belirlenir, ardından ilaçlar ve iki laboratuvar değeri eklenir; son olarak eğitim epikrizlerinden öğrenen bir model kurulur. Her yöntem A hastanesinin test kümesinde, model ayrıca B hastanesinin epikrizlerinde değerlendirilir.

### Adım 1.1: Bir anahtar kelime kuralı

**Amaç.** Bu adımda epikrizlerde altı tanının kelimeleri aranır ve bir kelime aramasının nerede yanıldığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir tanının kelimelerini arayan basit bir aramanın epikrizlerde altı kronik tanıyı ne kadar
iyi bulduğunu öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki 600 epikrizi tutar. Her satır bir hastadır: "epikriz"
sütunu Türkçe epikrizi tutar; "KY", "AF", "KAH", "HT", "DM" ve "KBH" adlı altı sütun 0 ya da 1
değerini alır; kayıt sisteminde sırasıyla kalp yetersizliği, atriyal fibrilasyon, koroner arter
hastalığı, hipertansiyon, diyabetes mellitus ve kronik böbrek hastalığı kayıtlıysa değer 1, değilse
0 olur.
Görev: Her metni Türkçe kurallarına göre küçük harfe çevir: Önce I'yı ı, İ'yi i yap, ardından öteki
harfleri küçült. Her tanının şu kelimelerini tam kelime olarak ara; böylece hiçbir kelime daha uzun
bir kelimenin içinde bulunmaz: Kalp yetersizliği için "kalp yetersizliği", "kalp yetmezliği",
"konjestif kalp yetmezliği", "ky" ve "kky"; atriyal fibrilasyon için "atriyal fibrilasyon", "af" ve
"afib"; koroner arter hastalığı için "koroner arter hastalığı", "kah", "iskemik kalp hastalığı",
"miyokard enfarktüsü" ve "akut koroner sendrom"; hipertansiyon için "hipertansiyon" ve "ht";
diyabetes mellitus için "diyabet", "diyabetes mellitus" ve "dm"; kronik böbrek hastalığı için
"kronik böbrek hastalığı", "kronik böbrek yetmezliği", "kbh" ve "kby". Kelimelerinden en az biri
epikrizin herhangi bir yerinde bulunan tanı var kabul edilir. Altı kararı kayıt sistemindeki altı
sütunla karşılaştır; her tanı için duyarlılığı, pozitif öngörü değerini ve F1 değerini (doğru
pozitiflerin iki katı, doğru pozitiflerin iki katı ile yanlış pozitiflerin ve yanlış negatiflerin
toplamına bölünür) ve altı F1 değerinin ortalamasını, yani makro F1 değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her tanı için bir satır ve üç değer içeren bir tablo ile makro F1 değerini yazdır. Atriyal
fibrilasyonun pozitif öngörü değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Her değer 0 ile 1 arasında olmalı ve VC-2444 numaralı hastanın epikrizi kalp yetersizliği,
atriyal fibrilasyon ve koroner arter hastalığı için pozitif bulunmalı.
```

**Beklenen sonuç:** "cevap" = 0,19

### Adım 1.2: Her geçişin durumu

**Amaç.** Bu adımda yok sayılan, olası ya da bir yakına ait geçişler dışarıda bırakılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Epikrizlerde altı tanının kelimelerini arayan bir aramanın, yok sayılan, yalnızca
şüphelenilen ya da bir yakına ait geçişler dışarıda bırakıldığında ne kadar iyileştiğini öğrenmek
istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki 600 epikrizi tutar. Her satır bir hastadır: "epikriz"
sütunu Türkçe epikrizi tutar; "KY", "AF", "KAH", "HT", "DM" ve "KBH" adlı altı sütun 0 ya da 1
değerini alır; kayıt sisteminde sırasıyla kalp yetersizliği, atriyal fibrilasyon, koroner arter
hastalığı, hipertansiyon, diyabetes mellitus ve kronik böbrek hastalığı kayıtlıysa değer 1, değilse
0 olur.
Görev: Her metni Türkçe kurallarına göre küçük harfe çevir: Önce I'yı ı, İ'yi i yap, ardından öteki
harfleri küçült. Her tanının şu kelimelerini tam kelime olarak ara; böylece hiçbir kelime daha uzun
bir kelimenin içinde bulunmaz: Kalp yetersizliği için "kalp yetersizliği", "kalp yetmezliği",
"konjestif kalp yetmezliği", "ky" ve "kky"; atriyal fibrilasyon için "atriyal fibrilasyon", "af" ve
"afib"; koroner arter hastalığı için "koroner arter hastalığı", "kah", "iskemik kalp hastalığı",
"miyokard enfarktüsü" ve "akut koroner sendrom"; hipertansiyon için "hipertansiyon" ve "ht";
diyabetes mellitus için "diyabet", "diyabetes mellitus" ve "dm"; kronik böbrek hastalığı için
"kronik böbrek hastalığı", "kronik böbrek yetmezliği", "kbh" ve "kby". Bir geçişten sonra,
cümlesinin sonuna ya da başka bir tanının bir sonraki geçişine kadar şu kelimelerden biri geliyorsa
geçiş sayılmaz: "yok", "izlenmedi", "saptanmadı", "tanımlamıyor", "dışlandı" ya da "(-)" (olumsuz);
"şüphe", "olası" ya da "ön tanı" (olası). Aynı cümlede geçişten önce şu kelimelerden biri duruyorsa
da geçiş sayılmaz: "babası", "annesi", "kardeşi", "babada", "annede" ya da "soygeçmiş" (bir yakın).
Geçişlerinden en az biri sayılan tanı var kabul edilir. Altı kararı kayıt sistemindeki altı sütunla
karşılaştır; her tanı için duyarlılığı, pozitif öngörü değerini ve F1 değerini (doğru pozitiflerin
iki katı, doğru pozitiflerin iki katı ile yanlış pozitiflerin ve yanlış negatiflerin toplamına
bölünür) ve altı F1 değerinin ortalamasını, yani makro F1 değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her tanı için bir satır ve üç değer içeren bir tablo yazdır; makro F1 değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Atriyal fibrilasyonun pozitif öngörü değeri 1.1. adımdakinden yüksek olmalı ve VC-2444
numaralı hastanın epikrizi yalnızca kalp yetersizliği için pozitif bulunmalı.
```

**Beklenen sonuç:** "cevap" = 0,856

### Adım 1.3: İlaçlar ve laboratuvar değerleri

**Amaç.** Bu adımda hastalığın adı olmayan kanıtlar eklenir: İlaçlar, eGFR ve HbA1c.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Epikrizlerde altı kronik tanıyı, epikriz bu tanıların adını anmadığında ama onlar için
verilen bir ilacı ya da onları tanımlayan bir laboratuvar değerini andığında da bulmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki 600 epikrizi tutar. Her satır bir hastadır: "epikriz"
sütunu Türkçe epikrizi tutar; "KY", "AF", "KAH", "HT", "DM" ve "KBH" adlı altı sütun 0 ya da 1
değerini alır; kayıt sisteminde sırasıyla kalp yetersizliği, atriyal fibrilasyon, koroner arter
hastalığı, hipertansiyon, diyabetes mellitus ve kronik böbrek hastalığı kayıtlıysa değer 1, değilse
0 olur.
Görev: Her metni Türkçe kurallarına göre küçük harfe çevir: Önce I'yı ı, İ'yi i yap, ardından öteki
harfleri küçült. Her tanının şu kelimelerini tam kelime olarak ara; böylece hiçbir kelime daha uzun
bir kelimenin içinde bulunmaz: Kalp yetersizliği için "kalp yetersizliği", "kalp yetmezliği",
"konjestif kalp yetmezliği", "ky" ve "kky"; atriyal fibrilasyon için "atriyal fibrilasyon", "af" ve
"afib"; koroner arter hastalığı için "koroner arter hastalığı", "kah", "iskemik kalp hastalığı",
"miyokard enfarktüsü" ve "akut koroner sendrom"; hipertansiyon için "hipertansiyon" ve "ht";
diyabetes mellitus için "diyabet", "diyabetes mellitus" ve "dm"; kronik böbrek hastalığı için
"kronik böbrek hastalığı", "kronik böbrek yetmezliği", "kbh" ve "kby". Bir geçişten sonra,
cümlesinin sonuna ya da başka bir tanının bir sonraki geçişine kadar şu kelimelerden biri geliyorsa
geçiş sayılmaz: "yok", "izlenmedi", "saptanmadı", "tanımlamıyor", "dışlandı" ya da "(-)" (olumsuz);
"şüphe", "olası" ya da "ön tanı" (olası). Aynı cümlede geçişten önce şu kelimelerden biri duruyorsa
da geçiş sayılmaz: "babası", "annesi", "kardeşi", "babada", "annede" ya da "soygeçmiş" (bir yakın).
Geçişlerinden en az biri sayılan tanı var kabul edilir. Epikriz bir tanının ilaçlarından birini tam
kelime ya da bir kelimenin başı olarak anıyorsa da tanı var kabul edilir: Kalp yetersizliği için
"furosemid" ya da "sakubitril"; atriyal fibrilasyon için "apiksaban", "rivaroksaban", "edoksaban" ya
da "dabigatran"; koroner arter hastalığı için "klopidogrel", "tikagrelor", "pkg", "kabg" ya da
"stent"; hipertansiyon için "amlodipin" ya da "hidroklorotiyazid"; diyabetes mellitus için
"metformin", "gliklazid", "insülin" ya da "sitagliptin". "egfr" ifadesinden sonraki ilk sayı 60'ın
altındaysa kronik böbrek hastalığı, "hba1c" ifadesinden ve isteğe bağlı bir yüzde işaretinden
sonraki ilk sayı 6,5 ya da üstündeyse diyabetes mellitus vardır; bu sayılarda ondalık ayırıcı
virgüldür. Altı kararı kayıt sistemindeki altı sütunla karşılaştır; her tanı için duyarlılığı,
pozitif öngörü değerini ve F1 değerini (doğru pozitiflerin iki katı, doğru pozitiflerin iki katı ile
yanlış pozitiflerin ve yanlış negatiflerin toplamına bölünür) ve altı F1 değerinin ortalamasını,
yani makro F1 değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her tanı için bir satır ve üç değer içeren bir tablo yazdır; makro F1 değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Kronik böbrek hastalığının duyarlılığı 1 olmalı ve VC-2444 numaralı hastanın epikrizi kalp
yetersizliği, hipertansiyon ve kronik böbrek hastalığı için pozitif bulunmalı.
```

**Beklenen sonuç:** "cevap" = 0,98

### Adım 1.4: Epikrizlerden öğrenen bir model: TF-IDF ve lojistik regresyon

**Amaç.** Bu adımda A hastanesinin epikrizleriyle bir model eğitilir ve A ile B hastanelerinde değerlendirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Epikrizlerde altı kronik tanıyı örneklerden öğrenerek bulan bir model eğitmek ve bu modelin
kendi hastanesinde ve başka bir üslupla yazan başka bir hastanede ne kadar iyi çalıştığını öğrenmek
istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin 3.600 epikrizini tutar. Her satır bir hastadır: "küme" sütunu epikrizin kümesini verir
("eğitim": 1.800 epikriz; "doğrulama": 600; "test": 600; bu üçü A hastanesindendir; "dış": B
hastanesinden, (+) ve (-) işaretli kısa bir üslupla yazılmış 600 epikriz). "epikriz" sütunu Türkçe
epikrizi tutar; "KY", "AF", "KAH", "HT", "DM" ve "KBH" adlı altı sütun 0 ya da 1 değerini alır;
kayıt sisteminde sırasıyla kalp yetersizliği, atriyal fibrilasyon, koroner arter hastalığı,
hipertansiyon, diyabetes mellitus ve kronik böbrek hastalığı kayıtlıysa değer 1, değilse 0 olur.
Görev: Her metni Türkçe kurallarına göre küçük harfe çevir: Önce I'yı ı, İ'yi i yap, ardından öteki
harfleri küçült. Her epikrizi, kelimelerinin ve yan yana duran kelime çiftlerinin TF-IDF
ağırlıklarından oluşan bir vektöre dönüştür; kelime, harf ve rakamlardan oluşan kesintisiz bir
dizidir ve yalnızca en az iki eğitim epikrizinde geçen terimler tutulur. Terimleri ve ağırlıklarını
yalnızca eğitim epikrizlerinden öğren; bir terimin sıklığı olarak sayısının bir fazlasının
logaritmasını kullan ve her vektörü 1 uzunluğuna ölçekle. Her tanı için eğitim epikrizlerinde ters
düzenlileştirme gücü 10 olan bir lojistik regresyon eğit. Doğrulama epikrizlerinde her tanı için
olasılık eşiğini, 0,05'ten 0,95'e 0,05'lik adımlarla, F1 değerinin en yüksek olduğu değer olarak
seç. Bu eşiklerle her tanının F1 değerini ve makro F1 değerini test epikrizlerinde ve dış
epikrizlerde hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her tanının test ve dış epikrizlerdeki F1 değerini gösteren bir tablo yazdır; dış
epikrizlerdeki makro F1 değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Terimler yalnızca eğitim epikrizlerinden, eşikler yalnızca doğrulama epikrizlerinden gelmeli;
test epikrizlerindeki makro F1 değeri 0,9'un üstünde olmalı.
```

**Beklenen sonuç:** "cevap" = 0,708

## Durak 2: Mini proje: NER pipeline ile STEMI, AF ve kalp yetersizliği

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-06/ders.html#stop-2) · Python yolunda aynı sonuç: 6-8. bölümler*

Bu durak oturumun mini projesidir. Burada epikrizleri Hugging Face Hub'dan alınan, önceden eğitilmiş Türkçe bir dil modeli okur. Modelin tokenizer'ı önce B hastanesinin büyük harflerinin bir modele ne yaptığını gösterir. Model ardından tanıları, ilaçları ve işlemleri bulmak için ince ayarla eğitilir; bulduğu varlıklar, 1. duraktaki durum kuralı ve ilaçlarla birlikte B hastanesinin epikrizlerindeki altı tanıyı verir. Son adım, epikrizlerdeki akut koroner sendromdan ve ST yükselmesinden okunan STEMI'yi ekler.

### Adım 2.1: Önceden eğitilmiş Türkçe bir modelin token'ları

**Amaç.** Bu adımda önceden eğitilmiş Türkçe bir modelin B hastanesinin epikrizlerini nasıl token'lara böldüğü ve harflerin büyük ya da küçük olmasının neyi değiştirdiği görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Kısmen büyük harflerle yazılmış epikrizlerde önceden eğitilmiş Türkçe bir dil modeli
kullanmak ve modelin bu epikrizlerin kelimelerini bilip bilmediğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin B hastanesine ait, büyük harfli kısaltmalar içeren kısa bir üslupla Türkçe yazılmış 600
epikrizi tutar. Her satır bir hastadır ve "epikriz" sütunu epikrizi tutar.
Görev: "ytu-ce-cosmos/turkish-tiny-bert-uncased" modelinin tokenizer'ını Hugging Face Hub'dan yükle.
Her epikrizi üç kez token'lara böl: Yazıldığı gibi, programlama dilinin olağan küçük harf işleminden
sonra ve Türkçe küçük harf işleminden sonra (önce I, ı; İ, i olur, ardından öteki harfler küçülür).
Üçünün her biri için baştaki ve sondaki özel token'lar hariç token'ları say ve bunların yüzde
kaçının bilinmeyen token olduğunu hesapla. İlk epikrizin token'larını da üç biçimde göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Üç biçim için token sayısını ve bilinmeyen token'ların yüzdesini yazdır; yazıldığı gibi
verilen metindeki yüzdeyi bir ondalık basamakla "cevap" adıyla sakla.
Test: Türkçe küçük harf işleminden sonra hiç bilinmeyen token kalmamalı; ilk epikriz olağan küçük
harf işleminden sonra Türkçe işlemden sonrakinden daha çok ya da aynı sayıda token vermeli.
```

**Beklenen sonuç:** "cevap" = 19,5

### Adım 2.2: Varlıklar için modele ince ayar

**Amaç.** Bu adımda önceden eğitilmiş modele tanıları, ilaçları ve işlemleri etiketlemesi öğretilir. Eğitim birkaç dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Küçük ve önceden eğitilmiş Türkçe bir dil modelini epikrizlerdeki tanıları, ilaçları ve
işlemleri bulacak biçimde uyarlamak ve modelin bunları görmediği epikrizlerde ne kadar doğru
bulduğunu öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
klinikten 3.000 epikriz tutar. Her satır bir hastadır: "küme" sütunu kümeyi verir ("eğitim": A
hastanesinden 1.800 epikriz; "test": A hastanesinden 600; "dış": B hastanesinden 600). "epikriz"
sütunu Türkçe epikrizi tutar; "varlıklar" sütunu epikrizdeki açıklanmış varlıkları, 0'dan başlayarak
sayılan (ilk karakter, son karakter artı bir, tür) üçlüleri hâlinde listeler. Türler tanı için
"DIAG", ilaç için "DRUG", işlem için "PROC" olarak yazılmıştır; "KY", "AF", "KAH", "HT", "DM" ve
"KBH" adlı altı sütun 0 ya da 1 değerini alır; kayıt sisteminde sırasıyla kalp yetersizliği, atriyal
fibrilasyon, koroner arter hastalığı, hipertansiyon, diyabetes mellitus ve kronik böbrek hastalığı
kayıtlıysa değer 1, değilse 0 olur.
Görev: "ytu-ce-cosmos/turkish-tiny-bert-uncased" modelini Hugging Face Hub'dan, her token'a yedi
etiketten birini veren bir katmanla kullan: Varlığın dışında ya da bir tanının, bir ilacın veya bir
işlemin başlangıcı ya da içi. Her epikrizi Türkçe küçük harfe çevir (önce I, ı; İ, i olur); bu işlem
karakterlerin konumlarını korur. Epikrizi en fazla 384 token'a böl. Bir token, ilk karakterinin
içinde bulunduğu varlığın etiketini alır: Varlığı başlatıyorsa başlangıç etiketini, başlatmıyorsa iç
etiketini. Modele eğitim epikrizleriyle 4 epoch boyunca, karıştırılmış 16 epikrizlik gruplar
hâlinde, AdamW optimizasyon algoritması ve 0,0003 öğrenme hızıyla ince ayar yap. Ardından test ve
dış epikrizleri etiketle, her varlığın token'larını yeniden bir karakter parçasına birleştir ve
varlıkların kesinliğini, duyarlılığını ve F1 değerini hesapla; tahmin edilen bir varlık ancak türü,
ilk karakteri ve son karakteri açıklanmış bir varlıkla eşleştiğinde sayılır. Sonucun
tekrarlanabilmesi için seed değerini 2026 olarak sabitle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her epoch'un kaybını ve test ile dış epikrizlerde bütün varlıklar ve her tür için kesinliği,
duyarlılığı ve F1 değerini gösteren bir tablo yazdır; test epikrizlerinde bütün varlıkların F1
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Kayıp ilk epoch'tan son epoch'a düşmeli ve F1 değeri 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,981

### Adım 2.3: Varlıklardan B hastanesindeki altı tanıya

**Amaç.** Bu adımda modelin varlıkları, 1. duraktaki durum kuralı ve ilaçlarla B hastanesinin her epikrizi için altı tanıya dönüştürülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir dil modelinin başka bir hastanenin epikrizlerinde bulduğu tanıları ve ilaçları her
hastanın altı kronik tanısına dönüştürmek ve bunun ne kadar iyi çalıştığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin B hastanesine ait, kısa bir üslupla Türkçe yazılmış 600 epikrizi tutar. Her satır bir
hastadır: "epikriz" sütunu epikrizi tutar; "varlıklar" sütunu epikrizdeki açıklanmış varlıkları,
"model varlıkları" sütunu ise A hastanesinin eğitim epikrizleriyle ince ayar yapılmış küçük Türkçe
dil modelinin epikrizde bulduğu varlıkları listeler. İki sütunda da varlıklar, 0'dan başlayarak
sayılan (ilk karakter, son karakter artı bir, tür) üçlüleri hâlinde yazılmıştır; türler tanı için
"DIAG", ilaç için "DRUG" ve işlem için "PROC" olarak gösterilir. "KY", "AF", "KAH", "HT", "DM" ve
"KBH" adlı altı sütun 0 ya da 1 değerini alır; kayıt sisteminde sırasıyla kalp yetersizliği, atriyal
fibrilasyon, koroner arter hastalığı, hipertansiyon, diyabetes mellitus ve kronik böbrek hastalığı
kayıtlıysa değer 1, değilse 0 olur.
Görev: "model varlıkları" sütununu kullan. Her tanı varlığını, 1. duraktaki gibi kelimelerine göre
altı tanıdan birine ver ve durumunu 1. duraktaki kuralla belirle; varlıklarından biri var durumunda
olan tanı var kabul edilir. 1. duraktaki gibi ilaç varlıklarının ve eGFR ile HbA1c değerlerinin
gösterdiği tanıları ekle. Altı kararı kayıt sistemindeki altı sütunla karşılaştır; her tanı için
duyarlılığı, pozitif öngörü değerini ve F1 değerini (doğru pozitiflerin iki katı, doğru pozitiflerin
iki katı ile yanlış pozitiflerin ve yanlış negatiflerin toplamına bölünür) ve altı F1 değerinin
ortalamasını, yani makro F1 değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her tanı için bir satır ve üç değer içeren bir tablo yazdır; makro F1 değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Her değer 0 ile 1 arasında olmalı; hiç varlığı olmayan bir epikriz, laboratuvar değerlerinden
gelebilen kronik böbrek hastalığı ve diyabet dışında her tanı için negatif olmalı.
```

**Beklenen sonuç:** "cevap" = 0,754

### Adım 2.4: Seyirden ve EKG'den STEMI

**Amaç.** Bu adımda epikrizlerin akut koroner sendrom ve ST segmenti hakkında yazdıklarından STEMI geçiren hastalar bulunur ve sonuç iki hastanede değerlendirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: İki hastanenin epikrizlerinde ST yükselmeli miyokard enfarktüsü geçiren hastaları bulmak ve
basit bir kuralın onları ne kadar güvenilir biçimde bulduğunu öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; A hastanesinin test kümesine ait, tam
cümlelerle yazılmış 600 epikrizi ve B hastanesine ait, kısa bir üslupla yazılmış 600 epikrizi, yani
Türkçe yazılmış toplam 1.200 epikrizi tutar. Her satır bir hastadır: "küme" sütunu kümeyi ("test" ya
da "dış"), "epikriz" sütunu epikrizi verir; "STEMI" sütunu sanal kliniğin kayıt sistemi ST
yükselmeli miyokard enfarktüsü kaydettiyse 1, kaydetmediyse 0'dır.
Görev: Her epikrizi Türkçe kurallarına göre küçük harfe çevir: Önce I'yı ı, İ'yi i yap, ardından
öteki harfleri küçült. Bir epikriz akut koroner sendromdan, yani "akut koroner sendrom" ifadesinden
ya da tam kelime olarak "aks" kısaltmasından söz ediyorsa ve aynı cümlede ardından "dışlandı",
"yok", "izlenmedi" ya da "saptanmadı" kelimelerinden biri gelmiyorsa, ayrıca "st yükselmesi"
ifadesini de içeriyorsa ona STEMI de. Sonucu "STEMI" sütunuyla karşılaştır ve her küme için STEMI
geçiren hasta sayısını, bulunan hasta sayısını, duyarlılığı, pozitif öngörü değerini ve F1 değerini
hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her küme için bir satır ve bu değerleri içeren bir tablo yazdır; "test" kümesinin F1 değerini
üç ondalık basamakla "cevap" adıyla sakla.
Test: Her değer 0 ile 1 arasında olmalı ve her kümedeki STEMI geçiren hasta sayısı o kümedeki
"STEMI" sütununun toplamına eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 1,0

## Durak 3: Anjiyografi raporları: Darlık derecesi ve damar

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-06/ders.html#stop-3) · Python yolunda aynı sonuç: 9. bölüm*

Burada sanal kliniğin anjiyografi raporları bir kayıt sisteminin okuyacağı gibi okunur. Dersteki işlem hattı bir rapordaki arterleri, segmentleri ve darlık derecelerini bulur, her bölgenin en büyük darlığını tutar ve hastalıklı damarları sayar. İşlem hattı önce tek bir rapora, sonra A hastanesinin test raporlarına, son olarak da büyük harflerle yazılmış B hastanesi raporlarına uygulanır.

### Adım 3.1: Tek bir rapor, cümle cümle

**Amaç.** Bu adımda tek bir anjiyografi raporu dersteki işlem hattının yaptığı gibi okunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Türkçe yazılmış bir koroner anjiyografi raporunu okuyan ve her koroner bölgenin en büyük
darlığını ve hastalıklı damar sayısını veren bir program istiyorum.
Veri: Jupyter Notebook'ta "veri" adında tek satırlık bir tablo var: "rapor" sütunu, sentetik bir
kayıt sistemi olan sanal kliniğin VC-2914 numaralı hastasının Türkçe yazılmış koroner anjiyografi
raporunu tutar.
Görev: Raporu cümle cümle oku; bir cümle, ardından bir boşluk ve bir büyük harf ya da bir rakam
gelen noktada biter. Her cümleyi Türkçe kurallarına göre küçük harfe çevir (önce I, ı; İ, i olur).
"endikasyon", "öykü", "sol ventrikülografi", "sv:", "girişim" ya da "işlem" ile başlayan cümleleri
atla. Öteki her cümlede, cümlenin andığı ilk arteri bul: Sol ana koroner için "sol ana koroner" ya
da "lmca"; LAD için "sol ön inen" ya da "lad", dalları için "birinci diyagonal", "1. diyagonal" ya
da "d1" ve "ikinci diyagonal", "2. diyagonal" ya da "d2"; sirkumfleks için "sirkumfleks", "cx" ya da
"lcx", dalları için "birinci obtus", "1. obtus" ya da "om1" ve "ikinci obtus", "2. obtus" ya da
"om2"; RCA için "sağ koroner" ya da "rca" ve "arka inen", "posterior desendan" ya da "pda". Kısa
adlar yalnızca tam kelime olarak sayılır. Arter adı geçmeyen bir cümle, önceki cümlenin arterine
aittir. Cümledeki her darlık derecesini oku: "%" ya da "yüzde " ifadesinden sonraki sayı ("%70-80"
gibi bir aralık üst ucuyla, yani 80 olarak sayılır) ve "total oklüzyon", "tam tıkanıklık" ya da "to"
(100), "subtotal" (99), "kritik" (95), "ileri derecede" (80), "orta derecede" (60) ile "hafif",
"plak" ya da "plaklı" (30) kelimeleri. Her değeri arterinin bölgesine ver (dallar ana arterlerinin
bölgesine aittir) ve her bölgenin en büyük değerini tut; değeri olmayan bölge 0 alır. Hastalıklı
damar sayısı, değeri 70 ya da daha fazla olan LAD, CX ve RCA bölgelerini sayar. Her cümleyi ait
olduğu arterle ve içinde bulunan değerlerle birlikte göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Cümleleri, LM, LAD, CX ve RCA bölgelerinin en büyük darlığını ve hastalıklı damar sayısını
yazdır; hastalıklı damar sayısını "cevap" adıyla sakla.
Test: "Proksimal segmentinde ileri derecede darlık saptandı." cümlesi RCA'ya ait olmalı ve
kateterlerin numarası olan 6 bir darlık olarak görünmemeli.
```

**Beklenen sonuç:** "cevap" = 3

### Adım 3.2: A hastanesinin bütün test raporları

**Amaç.** Bu adımda işlem hattı her test raporuna uygulanır ve kayıt sistemiyle karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Koroner anjiyografi raporlarını okuyan bir programın ne sıklıkla kayıt sistemiyle aynı
hastalıklı damar sayısını ve aynı darlık derecesini verdiğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki Türkçe yazılmış 394 koroner anjiyografi raporunu tutar.
Her satır bir hastadır: "rapor" sütunu raporu tutar; "LM", "LAD", "CX" ve "RCA" adlı dört sütun,
kayıt sistemine göre sırasıyla sol ana koroner arterin, diyagonal dallarıyla sol ön inen arterin,
obtus marjinal dallarıyla sirkumfleks arterin ve arka inen arterle sağ koroner arterin
bölgelerindeki en büyük darlığı yüzde olarak verir. "hastalıklı damar" sütunu, yüzde 70 ya da daha
fazla darlığı olan LAD, CX ve RCA bölgelerinin sayısını verir.
Görev: Raporu cümle cümle oku; bir cümle, ardından bir boşluk ve bir büyük harf ya da bir rakam
gelen noktada biter. Her cümleyi Türkçe kurallarına göre küçük harfe çevir (önce I, ı; İ, i olur).
"endikasyon", "öykü", "sol ventrikülografi", "sv:", "girişim" ya da "işlem" ile başlayan cümleleri
atla. Öteki her cümlede, cümlenin andığı ilk arteri bul: Sol ana koroner için "sol ana koroner" ya
da "lmca"; LAD için "sol ön inen" ya da "lad", dalları için "birinci diyagonal", "1. diyagonal" ya
da "d1" ve "ikinci diyagonal", "2. diyagonal" ya da "d2"; sirkumfleks için "sirkumfleks", "cx" ya da
"lcx", dalları için "birinci obtus", "1. obtus" ya da "om1" ve "ikinci obtus", "2. obtus" ya da
"om2"; RCA için "sağ koroner" ya da "rca" ve "arka inen", "posterior desendan" ya da "pda". Kısa
adlar yalnızca tam kelime olarak sayılır. Arter adı geçmeyen bir cümle, önceki cümlenin arterine
aittir. Cümledeki her darlık derecesini oku: "%" ya da "yüzde " ifadesinden sonraki sayı ("%70-80"
gibi bir aralık üst ucuyla, yani 80 olarak sayılır) ve "total oklüzyon", "tam tıkanıklık" ya da "to"
(100), "subtotal" (99), "kritik" (95), "ileri derecede" (80), "orta derecede" (60) ile "hafif",
"plak" ya da "plaklı" (30) kelimeleri. Her değeri arterinin bölgesine ver (dallar ana arterlerinin
bölgesine aittir) ve her bölgenin en büyük değerini tut; değeri olmayan bölge 0 alır. Hastalıklı
damar sayısı, değeri 70 ya da daha fazla olan LAD, CX ve RCA bölgelerini sayar. Bunu her rapora
uygula. Programın ve kayıt sisteminin verdiği her en büyük darlığı beş kategoriden birine koy:
50'nin altı, 50-69, 70-89, 90-99 ve 100. Her bölge için kategorilerin uyuştuğu raporların oranını ve
hastalıklı damar sayısının uyuştuğu raporların oranını hesapla. Hastalıklı damar sayısının farklı
olduğu raporları göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Bölgelere ait dört oranı ve hastalıklı damar sayısına ait oranı yazdır; sonuncusunu üç
ondalık basamakla "cevap" adıyla sakla.
Test: Her oran 0 ile 1 arasında olmalı ve program VC-2914 numaralı hastanın raporunda 3 hastalıklı
damar bulmalı.
```

**Beklenen sonuç:** "cevap" = 0,959

### Adım 3.3: B hastanesinin büyük harfli raporları

**Amaç.** Bu adımda aynı işlem hattı, büyük harflerle ve kısa bir üslupla yazılmış başka bir hastanenin raporlarına uygulanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir hastanenin koroner anjiyografi raporlarını okuyan bir programın, büyük harflerle ve kısa
bir üslupla yazılmış başka bir hastanenin raporlarını da okuyup okumadığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin B hastanesinden gelen ve Türkçe yazılmış 373 koroner anjiyografi raporunu tutar; raporlar
büyük harflerle yazılmıştır. Her satır bir hastadır: "rapor" sütunu raporu tutar; "LM", "LAD", "CX"
ve "RCA" adlı dört sütun, kayıt sistemine göre sırasıyla sol ana koroner arterin, diyagonal
dallarıyla sol ön inen arterin, obtus marjinal dallarıyla sirkumfleks arterin ve arka inen arterle
sağ koroner arterin bölgelerindeki en büyük darlığı yüzde olarak verir. "hastalıklı damar" sütunu,
yüzde 70 ya da daha fazla darlığı olan LAD, CX ve RCA bölgelerinin sayısını verir.
Görev: Raporu cümle cümle oku; bir cümle, ardından bir boşluk ve bir büyük harf ya da bir rakam
gelen noktada biter. Her cümleyi Türkçe kurallarına göre küçük harfe çevir (önce I, ı; İ, i olur).
"endikasyon", "öykü", "sol ventrikülografi", "sv:", "girişim" ya da "işlem" ile başlayan cümleleri
atla. Öteki her cümlede, cümlenin andığı ilk arteri bul: Sol ana koroner için "sol ana koroner" ya
da "lmca"; LAD için "sol ön inen" ya da "lad", dalları için "birinci diyagonal", "1. diyagonal" ya
da "d1" ve "ikinci diyagonal", "2. diyagonal" ya da "d2"; sirkumfleks için "sirkumfleks", "cx" ya da
"lcx", dalları için "birinci obtus", "1. obtus" ya da "om1" ve "ikinci obtus", "2. obtus" ya da
"om2"; RCA için "sağ koroner" ya da "rca" ve "arka inen", "posterior desendan" ya da "pda". Kısa
adlar yalnızca tam kelime olarak sayılır. Arter adı geçmeyen bir cümle, önceki cümlenin arterine
aittir. Cümledeki her darlık derecesini oku: "%" ya da "yüzde " ifadesinden sonraki sayı ("%70-80"
gibi bir aralık üst ucuyla, yani 80 olarak sayılır) ve "total oklüzyon", "tam tıkanıklık" ya da "to"
(100), "subtotal" (99), "kritik" (95), "ileri derecede" (80), "orta derecede" (60) ile "hafif",
"plak" ya da "plaklı" (30) kelimeleri. Her değeri arterinin bölgesine ver (dallar ana arterlerinin
bölgesine aittir) ve her bölgenin en büyük değerini tut; değeri olmayan bölge 0 alır. Hastalıklı
damar sayısı, değeri 70 ya da daha fazla olan LAD, CX ve RCA bölgelerini sayar. Bunu her rapora
uygula ve hastalıklı damar sayısının kayıt sistemiyle uyuştuğu raporların oranını hesapla. Ardından
Türkçe küçük harf işlemi yerine programlama dilinin olağan küçük harf işlemini kullanarak tekrarla
ve oranı yeniden hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki oranı yazdır; Türkçe küçük harf işlemiyle bulunan oranı üç ondalık basamakla "cevap"
adıyla sakla.
Test: Türkçe küçük harf işlemiyle bulunan oran, olağan küçük harf işlemiyle bulunandan yüksek
olmalı.
```

**Beklenen sonuç:** "cevap" = 1,0

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

### Bir metin işlem hattını denetletmek

```text
Aşağıdaki kodu denetle; kod Türkçe klinik raporları okuyor ve tanıları, varlıkları ya da darlıkları
bildiriyor. Altı noktayı kontrol et. Metin Türkçe kurallarına göre, I ı ve İ i olacak biçimde küçük
harfe çevrilmiş mi ve kod karakterlerin konumlarını koruyor mu? Bir hastanın raporları ve dış
hastanenin raporları eğitim kümesinin dışında tutulmuş mu; sözlük ve eşikler yalnızca eğitim ve
doğrulama kümelerinde mi öğrenilmiş? Her kural olumsuzluğu, yakın akrabayı ve belirsizliği Türkçeye
uygun yönde, yani olumsuzluğun çoğunlukla hastalıktan sonra geldiğini göz önünde tutarak mı arıyor?
Sayılar ondalık virgül ve aralıklarla birlikte sayı olarak okunuyor ve doz, kateter boyutu ya da
ejeksiyon fraksiyonu gibi başka türden sayılardan ayrılıyor mu? Sonuçlar her tanı için duyarlılık,
pozitif öngörü değeri ve F1 ile ve bir dış test kümesinde veriliyor mu? Gerçek bir hastanın herhangi
bir metni kurumun dışındaki bir hizmete gönderiliyor mu? Her nokta için kodun yanlış satırını
alıntıla ve düzeltmesini öner.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter Notebook'un 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: İki hastanede bölge bölge

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir kayıt sistemi için iki hastanenin koroner anjiyografi raporlarını okuyan bir program
kurmak ve programın her koroner bölgede ne sıklıkla kayıt sistemiyle aynı darlık derecesini
verdiğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki 394 ve B hastanesindeki 373 koroner anjiyografi
raporunu, yani Türkçe yazılmış toplam 767 raporu tutar; B hastanesi büyük harflerle ve kısa bir
üslupla yazar. Her satır bir hastadır: "küme" sütunu kümeyi ("test" ya da "dış"), "hasta" hastayı,
"rapor" raporu verir; "LM", "LAD", "CX" ve "RCA" adlı dört sütun kayıt sistemine göre dört koroner
bölgenin en büyük darlığını yüzde olarak, "hastalıklı damar" ise yüzde 70 ya da daha fazla darlığı
olan LAD, CX ve RCA bölgelerinin sayısını verir. "epikriz" sütunu aynı hastanın epikrizini tutar.
Görev: Raporu cümle cümle oku; bir cümle, ardından bir boşluk ve bir büyük harf ya da bir rakam
gelen noktada biter. Her cümleyi Türkçe kurallarına göre küçük harfe çevir (önce I, ı; İ, i olur).
"endikasyon", "öykü", "sol ventrikülografi", "sv:", "girişim" ya da "işlem" ile başlayan cümleleri
atla. Öteki her cümlede, cümlenin andığı ilk arteri bul: Sol ana koroner için "sol ana koroner" ya
da "lmca"; LAD için "sol ön inen" ya da "lad", dalları için "birinci diyagonal", "1. diyagonal" ya
da "d1" ve "ikinci diyagonal", "2. diyagonal" ya da "d2"; sirkumfleks için "sirkumfleks", "cx" ya da
"lcx", dalları için "birinci obtus", "1. obtus" ya da "om1" ve "ikinci obtus", "2. obtus" ya da
"om2"; RCA için "sağ koroner" ya da "rca" ve "arka inen", "posterior desendan" ya da "pda". Kısa
adlar yalnızca tam kelime olarak sayılır. Arter adı geçmeyen bir cümle, önceki cümlenin arterine
aittir. Cümledeki her darlık derecesini oku: "%" ya da "yüzde " ifadesinden sonraki sayı ("%70-80"
gibi bir aralık üst ucuyla, yani 80 olarak sayılır) ve "total oklüzyon", "tam tıkanıklık" ya da "to"
(100), "subtotal" (99), "kritik" (95), "ileri derecede" (80), "orta derecede" (60) ile "hafif",
"plak" ya da "plaklı" (30) kelimeleri. Her değeri arterinin bölgesine ver (dallar ana arterlerinin
bölgesine aittir) ve her bölgenin en büyük değerini tut; değeri olmayan bölge 0 alır. Hastalıklı
damar sayısı, değeri 70 ya da daha fazla olan LAD, CX ve RCA bölgelerini sayar. Bunu her rapora
uygula. Programın ve kayıt sisteminin verdiği her en büyük darlığı beş kategoriden birine koy:
50'nin altı, 50-69, 70-89, 90-99 ve 100. Her küme ve her bölge için kategorilerin uyuştuğu
raporların oranını ve dört bölgenin de uyuştuğu raporların oranını hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her küme için bir satır ve beş oran içeren bir tablo göster; "test" kümesinde dört bölgenin
de uyuştuğu raporların oranını üç ondalık basamakla "cevap" adıyla sakla.
Test: "test" kümesinde 394, "dış" kümesinde 373 rapor bulunmalı ve her oran 0 ile 1 arasında olmalı.
```

### Adım 2: Sol ana koroner arter ve hastalıklı damar sayısı

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Koroner anjiyografi raporlarını okuyan bir programın, cerrahi ile stent arasındaki kararı
belirleyen iki bulguyu, yani sol ana koroner arter hastalığını ve hastalıklı damar sayısını ne kadar
iyi bulduğunu öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki 394 ve B hastanesindeki 373 koroner anjiyografi
raporunu, yani Türkçe yazılmış toplam 767 raporu tutar; B hastanesi büyük harflerle ve kısa bir
üslupla yazar. Her satır bir hastadır: "küme" sütunu kümeyi ("test" ya da "dış"), "hasta" hastayı,
"rapor" raporu verir; "LM", "LAD", "CX" ve "RCA" adlı dört sütun kayıt sistemine göre dört koroner
bölgenin en büyük darlığını yüzde olarak, "hastalıklı damar" ise yüzde 70 ya da daha fazla darlığı
olan LAD, CX ve RCA bölgelerinin sayısını verir. "epikriz" sütunu aynı hastanın epikrizini tutar.
Görev: Raporu cümle cümle oku; bir cümle, ardından bir boşluk ve bir büyük harf ya da bir rakam
gelen noktada biter. Her cümleyi Türkçe kurallarına göre küçük harfe çevir (önce I, ı; İ, i olur).
"endikasyon", "öykü", "sol ventrikülografi", "sv:", "girişim" ya da "işlem" ile başlayan cümleleri
atla. Öteki her cümlede, cümlenin andığı ilk arteri bul: Sol ana koroner için "sol ana koroner" ya
da "lmca"; LAD için "sol ön inen" ya da "lad", dalları için "birinci diyagonal", "1. diyagonal" ya
da "d1" ve "ikinci diyagonal", "2. diyagonal" ya da "d2"; sirkumfleks için "sirkumfleks", "cx" ya da
"lcx", dalları için "birinci obtus", "1. obtus" ya da "om1" ve "ikinci obtus", "2. obtus" ya da
"om2"; RCA için "sağ koroner" ya da "rca" ve "arka inen", "posterior desendan" ya da "pda". Kısa
adlar yalnızca tam kelime olarak sayılır. Arter adı geçmeyen bir cümle, önceki cümlenin arterine
aittir. Cümledeki her darlık derecesini oku: "%" ya da "yüzde " ifadesinden sonraki sayı ("%70-80"
gibi bir aralık üst ucuyla, yani 80 olarak sayılır) ve "total oklüzyon", "tam tıkanıklık" ya da "to"
(100), "subtotal" (99), "kritik" (95), "ileri derecede" (80), "orta derecede" (60) ile "hafif",
"plak" ya da "plaklı" (30) kelimeleri. Her değeri arterinin bölgesine ver (dallar ana arterlerinin
bölgesine aittir) ve her bölgenin en büyük değerini tut; değeri olmayan bölge 0 alır. Hastalıklı
damar sayısı, değeri 70 ya da daha fazla olan LAD, CX ve RCA bölgelerini sayar. Bunu her rapora
uygula. Sol ana koroner arter hastalığı, LM bölgesinde en büyük darlığın yüzde 50 ya da daha fazla
olmasıdır. Her küme için programın sol ana koroner arter hastalığındaki duyarlılığını ve pozitif
öngörü değerini "LM" sütununa göre hesapla; kayıt sistemindeki hastalıklı damar sayısını
programınkine karşı gösteren bir tablo göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her küme için iki değeri ve iki tabloyu yazdır; "test" kümesinde sol ana koroner arter
hastalığının pozitif öngörü değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: İki tablonun sayılarının toplamı kümedeki rapor sayısına eşit olmalı.
```

### Adım 3: Hatalar ve nedenleri

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Koroner anjiyografi raporlarını okuyan bir programın yanlış okuduğu her raporu görmek ve
programı yanıltan cümleyi bulmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki 394 ve B hastanesindeki 373 koroner anjiyografi
raporunu, yani Türkçe yazılmış toplam 767 raporu tutar; B hastanesi büyük harflerle ve kısa bir
üslupla yazar. Her satır bir hastadır: "küme" sütunu kümeyi ("test" ya da "dış"), "hasta" hastayı,
"rapor" raporu verir; "LM", "LAD", "CX" ve "RCA" adlı dört sütun kayıt sistemine göre dört koroner
bölgenin en büyük darlığını yüzde olarak, "hastalıklı damar" ise yüzde 70 ya da daha fazla darlığı
olan LAD, CX ve RCA bölgelerinin sayısını verir. "epikriz" sütunu aynı hastanın epikrizini tutar.
Görev: Raporu cümle cümle oku; bir cümle, ardından bir boşluk ve bir büyük harf ya da bir rakam
gelen noktada biter. Her cümleyi Türkçe kurallarına göre küçük harfe çevir (önce I, ı; İ, i olur).
"endikasyon", "öykü", "sol ventrikülografi", "sv:", "girişim" ya da "işlem" ile başlayan cümleleri
atla. Öteki her cümlede, cümlenin andığı ilk arteri bul: Sol ana koroner için "sol ana koroner" ya
da "lmca"; LAD için "sol ön inen" ya da "lad", dalları için "birinci diyagonal", "1. diyagonal" ya
da "d1" ve "ikinci diyagonal", "2. diyagonal" ya da "d2"; sirkumfleks için "sirkumfleks", "cx" ya da
"lcx", dalları için "birinci obtus", "1. obtus" ya da "om1" ve "ikinci obtus", "2. obtus" ya da
"om2"; RCA için "sağ koroner" ya da "rca" ve "arka inen", "posterior desendan" ya da "pda". Kısa
adlar yalnızca tam kelime olarak sayılır. Arter adı geçmeyen bir cümle, önceki cümlenin arterine
aittir. Cümledeki her darlık derecesini oku: "%" ya da "yüzde " ifadesinden sonraki sayı ("%70-80"
gibi bir aralık üst ucuyla, yani 80 olarak sayılır) ve "total oklüzyon", "tam tıkanıklık" ya da "to"
(100), "subtotal" (99), "kritik" (95), "ileri derecede" (80), "orta derecede" (60) ile "hafif",
"plak" ya da "plaklı" (30) kelimeleri. Her değeri arterinin bölgesine ver (dallar ana arterlerinin
bölgesine aittir) ve her bölgenin en büyük değerini tut; değeri olmayan bölge 0 alır. Hastalıklı
damar sayısı, değeri 70 ya da daha fazla olan LAD, CX ve RCA bölgelerini sayar. Bunu "test"
kümesindeki her rapora uygula. Programın ve kayıt sisteminin verdiği her en büyük darlığı beş
kategoriden birine koy: 50'nin altı, 50-69, 70-89, 90-99 ve 100. En az bir bölgesi uyuşmayan rapor
yanlıştır. Her yanlış rapor için uyuşmayan bölgeleri ve programın tanıdığı hiçbir arteri anmayan ama
bir darlık derecesi içeren cümleleri göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Yanlış raporları bölgeleri ve cümleleriyle birlikte yazdır; yanlış raporların sayısını
"cevap" adıyla sakla.
Test: Yanlış rapor sayısı 394'ten büyük olamaz.
```

### Adım 4: Anjiyografi ve epikriz birlikte

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Anjiyografide anlamlı koroner darlığı olan hastalardan kaçının epikrizinde, epikrizleri
tarayan bir aramanın bulacağı biçimde koroner arter hastalığı bulunmadığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sentetik bir kayıt sistemi olan sanal
kliniğin A hastanesine ait test kümesindeki 394 ve B hastanesindeki 373 koroner anjiyografi
raporunu, yani Türkçe yazılmış toplam 767 raporu tutar; B hastanesi büyük harflerle ve kısa bir
üslupla yazar. Her satır bir hastadır: "küme" sütunu kümeyi ("test" ya da "dış"), "hasta" hastayı,
"rapor" raporu verir; "LM", "LAD", "CX" ve "RCA" adlı dört sütun kayıt sistemine göre dört koroner
bölgenin en büyük darlığını yüzde olarak, "hastalıklı damar" ise yüzde 70 ya da daha fazla darlığı
olan LAD, CX ve RCA bölgelerinin sayısını verir. "epikriz" sütunu aynı hastanın epikrizini tutar.
Görev: Raporu cümle cümle oku; bir cümle, ardından bir boşluk ve bir büyük harf ya da bir rakam
gelen noktada biter. Her cümleyi Türkçe kurallarına göre küçük harfe çevir (önce I, ı; İ, i olur).
"endikasyon", "öykü", "sol ventrikülografi", "sv:", "girişim" ya da "işlem" ile başlayan cümleleri
atla. Öteki her cümlede, cümlenin andığı ilk arteri bul: Sol ana koroner için "sol ana koroner" ya
da "lmca"; LAD için "sol ön inen" ya da "lad", dalları için "birinci diyagonal", "1. diyagonal" ya
da "d1" ve "ikinci diyagonal", "2. diyagonal" ya da "d2"; sirkumfleks için "sirkumfleks", "cx" ya da
"lcx", dalları için "birinci obtus", "1. obtus" ya da "om1" ve "ikinci obtus", "2. obtus" ya da
"om2"; RCA için "sağ koroner" ya da "rca" ve "arka inen", "posterior desendan" ya da "pda". Kısa
adlar yalnızca tam kelime olarak sayılır. Arter adı geçmeyen bir cümle, önceki cümlenin arterine
aittir. Cümledeki her darlık derecesini oku: "%" ya da "yüzde " ifadesinden sonraki sayı ("%70-80"
gibi bir aralık üst ucuyla, yani 80 olarak sayılır) ve "total oklüzyon", "tam tıkanıklık" ya da "to"
(100), "subtotal" (99), "kritik" (95), "ileri derecede" (80), "orta derecede" (60) ile "hafif",
"plak" ya da "plaklı" (30) kelimeleri. Her değeri arterinin bölgesine ver (dallar ana arterlerinin
bölgesine aittir) ve her bölgenin en büyük değerini tut; değeri olmayan bölge 0 alır. Hastalıklı
damar sayısı, değeri 70 ya da daha fazla olan LAD, CX ve RCA bölgelerini sayar. Bunu her rapora
uygula; program en az bir hastalıklı damar ya da sol ana koroner arter hastalığı bulduğunda hastada
anlamlı darlık vardır. Ardından aynı hastanın epikrizini oku: Her metni Türkçe kurallarına göre
küçük harfe çevir: Önce I'yı ı, İ'yi i yap, ardından öteki harfleri küçült. "koroner arter
hastalığı", "kah", "iskemik kalp hastalığı", "miyokard enfarktüsü" ya da "akut koroner sendrom" tam
kelime olarak geçiyor, cümlesinin sonuna ya da başka bir tanının bir sonraki geçişine kadar ardından
"yok", "izlenmedi", "saptanmadı", "tanımlamıyor", "dışlandı", "(-)", "şüphe", "olası" ya da "ön
tanı" gelmiyor ve cümlesinde önünde "babası", "annesi", "kardeşi", "babada", "annede" ya da
"soygeçmiş" durmuyorsa ya da epikriz "klopidogrel", "tikagrelor", "pkg", "kabg" ya da "stent"
kelimelerinden birini anıyorsa epikrizde koroner arter hastalığı vardır. Her küme için anlamlı
darlığı olduğu hâlde epikrizinde koroner arter hastalığı bulunmayan hastaları say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her küme için sayıları ve bu epikrizlerden üçünü yazdır; "test" kümesindeki sayıyı "cevap"
adıyla sakla.
Test: Sayı, kümede anlamlı darlığı olan hastaların sayısından büyük olamaz.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
