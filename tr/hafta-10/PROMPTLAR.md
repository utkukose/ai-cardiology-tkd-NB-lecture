# Prompt kütüphanesi, 10. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[10. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-10/PROMPTS.md)

Bu kütüphanede, 10. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Prototipin AF modeli](#durak-1-prototipin-af-modeli)
3. [Durak 2: Açıklama, rapor ve servis](#durak-2-açıklama-rapor-ve-servis)
4. [Durak 3: Kullanıcı testi ve 1.1 sürümü](#durak-3-kullanıcı-testi-ve-11-sürümü)
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

## Durak 1: Prototipin AF modeli

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-10/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 10, 1-4. bölümler*

Bu durak oturumun mini projesidir. AFDB'nin 25 kaydının dakikaları RR aralıklarından elde edilen dört sayıyla tarif edilir; bir lojistik regresyon AF'yi eğitim kayıtlarından öğrenir, eşiği doğrulama kayıtlarında seçilir ve test kayıtları her kaydın AF yükünü ve alarm ataklarını verir.

### Adım 1.1: Bir dakikanın dört sayısı

**Amaç.** Bu adımda AFDB'nin her dakikası RR aralıklarından elde edilen dört sayıyla tarif edilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir telemetri servisinin kardiyoloğu, vuruların zamanlarından olası AF dakikalarını
işaretleyen bir karar destek prototipi istiyor. İlk adım, her dakikayı RR aralıklarının ne kadar
düzensiz olduğunu ölçen sayılarla tarif etmektir.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'ndaki
(AFDB) çoğu paroksismal atriyal fibrilasyonu (AF) olan kişilerin yaklaşık on saatlik 25 Holter
kaydından elde edilen bir dakikalık pencereler bulunur. Her satır bir dakikadır: "kayıt" kaydı,
"küme" kaydın kümesini ("eğitim", 15 kayıt; "doğrulama", 5 kayıt; "test", 5 kayıt), "başlangıç (s)"
ise dakikanın kaydın başından itibaren saniye cinsinden başlangıcını verir. Dakikanın yarısından
fazlası uzmanların işaretlediği AF içindeyse "AF" 1, değilse 0 olur. "RR aralıkları (s)" sütununun
her hücresi, dakikanın RR aralıklarını saniye cinsinden ve sırasıyla, 20 ya da daha fazla sayıdan
oluşan bir liste olarak tutar.
Görev: Her dakika için RR aralıklarından dört sayı hesapla: Kalp hızı, yani 60'ın ortalama aralığa
bölümü; değişim katsayısı, yani aralıkların standart sapmasının (n − 1 ile) ortalamalarına bölümü;
RMSSD'nin ortalama aralığa bölümü (RMSSD, ardışık aralıklar arasındaki farkların karelerinin
ortalamasının kareköküdür); ve pNN50, yani 0,05 saniyeden büyük ardışık farkların oranı. Ardından
eğitim kayıtlarında AF olan ve olmayan dakikaların dört sayısını karşılaştır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitim dakikalarında her sayının AF olan ve olmayan dakikalardaki medyanını yazdır; AF olan
eğitim dakikalarının medyan CV değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Her dakikanın kalp hızı dakikada 20 ile 250 arasında, pNN50 değeri ise 0 ile 1 arasında
olmalı.
```

**Beklenen sonuç:** "cevap" = 0,222

### Adım 1.2: Model ve eşiği

**Amaç.** Bu adımda AF modelinin 1.0 sürümü eğitim kayıtlarında kurulur ve eşiği doğrulama kayıtlarında seçilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog prototipin olabildiğince az AF dakikası kaçırmasını istiyor: AF dakikalarının en
az yüzde 95'i alarm vermeli. Yanlış alarmlar bunun bedelidir; test kayıtları da son değerlendirmeye
kadar hiç kullanılmamalıdır.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'ndaki
(AFDB) çoğu paroksismal atriyal fibrilasyonu (AF) olan kişilerin yaklaşık on saatlik 25 Holter
kaydından elde edilen bir dakikalık pencereler bulunur. Her satır bir dakikadır: "kayıt" kaydı,
"küme" kaydın kümesini ("eğitim", 15 kayıt; "doğrulama", 5 kayıt; "test", 5 kayıt), "başlangıç (s)"
ise dakikanın saniye cinsinden başlangıcını verir. Dakikanın yarısından fazlası uzmanların
işaretlediği AF içindeyse "AF" 1, değilse 0 olur. Dört sayı dakikanın RR aralıklarını tarif eder:
"kalp hızı" (dakikada), "CV" (aralıkların standart sapmasının ortalamalarına bölümü), "RMSSD/RR"
(ardışık farkların karelerinin ortalamasının karekökünün ortalama aralığa bölümü) ve "pNN50" (50
ms'den büyük ardışık farkların oranı).
Görev: Yalnızca eğitim dakikalarında AF için bir lojistik regresyon kur; en fazla 3.000 yineleme
kullan. Girdileri kalp hızı, CV'nin doğal logaritması, RMSSD/RR'nin doğal logaritması ve pNN50'dir;
her biri eğitim dakikalarının ortalaması ve standart sapmasıyla bir z-skoruna dönüştürülür. Her
doğrulama dakikası için AF olasılığını ve doğrulama dakikalarındaki ROC eğrisi altındaki alanı (AUC)
hesapla. Eşiği yalnızca doğrulama dakikalarında seç: 0,05, 0,06, 0,07 ve bu biçimde 0,95'e kadar
giden değerler arasından, AF olan doğrulama dakikalarının en az yüzde 95'inin olasılığının ona eşit
ya da ondan büyük olduğu en yüksek değeri al.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Doğrulama AUC değerini, eşiği ve modelin katsayılarını yazdır; eşiği iki ondalık basamakla
"cevap" adıyla sakla.
Test: Hiçbir test dakikası kullanılmamalı ve AF olan doğrulama dakikalarının eşikte ya da üstünde
kalan payı en az 0,95 olmalı.
```

**Beklenen sonuç:** "cevap" = 0,37

### Adım 1.3: Test kayıtlarının AF yükü ve alarm atakları

**Amaç.** Bu adımda test dakikalarının olasılıkları her test kaydı için alarm ataklarına ve bir AF yüküne dönüştürülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog tek tek dakikaları değil, art arda gelen alarm dakikalarını inceler ve her kaydın
AF yükünü raporun vereceği biçimde görmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'nın 5
test kaydının, yani çoğu paroksismal atriyal fibrilasyonu (AF) olan kişilerin Holter kayıtlarının
bir dakikalık pencereleri bulunur. Her satır bir dakikadır: "kayıt" kaydı, "başlangıç (s)" ise
dakikanın saniye cinsinden başlangıcını verir. Dakikanın yarısından fazlası uzmanların işaretlediği
AF içindeyse "AF" 1 olur; "AF payı" dakikanın AF içinde geçen payıdır ve 0 ile 1 arasında değer
alır; "olasılık" ise dersin bir modelinin dakikaya verdiği AF olasılığıdır. Model, olasılığı en az
0,37 olan bir dakika için alarm verir.
Görev: Her kayıt içinde dakikaları başlangıçlarına göre sırala. Bir alarm atağı, alarm veren art
arda dakikalardan oluşan bir dizidir; içinde AF olan hiçbir dakika bulunmayan atak ise bir yanlış
alarm atağıdır. Her kayıt için işaretlemenin AF yükünü, yani dakikalarının ortalama AF payının 100
katını; modelin AF yükünü, yani alarm veren dakikalarının payının 100 katını; alarm ataklarının
sayısını ve yanlış alarm ataklarının sayısını hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her kayıt için bir satırdan oluşan bir tablo göster; test kayıtlarındaki toplam yanlış alarm
atağı sayısını "cevap" adıyla sakla.
Test: Bir kaydın alarm atakları dakikalarının yarısından bir fazlasını geçemez ve yükler 0 ile 100
arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 22

## Durak 2: Açıklama, rapor ve servis

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-10/ders.html#stop-2) · Python yolunda aynı sonuç: 5-8. bölümler*

Bu durak bir alarmı ve bir hastayı izler. 08219 kaydındaki bir yanlış alarm dakikası dört sayısının katkılarıyla açıklanır, telemetri servisindeki VC-0128'in sonucu bir HL7 FHIR raporu olarak yazılır ve aynı hastanın vuru zamanları dersin tahmin servisine gönderilir.

### Adım 2.1: Dakika neden alarm verdi?

**Amaç.** Bu adımda bir yanlış alarm dakikasında dört sayının her birinin AF'nin log-odds değerine kattığı değer hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Hekim 08219 kaydındaki bir yanlış alarmı açıyor ve EKG şeridine bakmadan önce dakikanın
hangi sayılarının modeli alarm vermeye yönelttiğini soruyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tablo, MIT-BIH Atriyal Fibrilasyon Veri Tabanı'nın
08219 kaydından, AF olmadığı hâlde dersin bir lojistik regresyonunun alarm verdiği bir dakikayı
tarif eder. İlk dört satır dakikanın dört sayısıdır: "sayı" sayıyı adlandırır, "dakikadaki değer"
değerini verir, "önce logaritma" modelin her şeyden önce değerin doğal logaritmasını alıp almadığını
söyler ("evet" ya da "hayır"); "ortalama, eğitim" ve "standart sapma, eğitim" değerin ya da
logaritmasının eğitim dakikalarındaki ortalaması ve standart sapmasıdır; "katsayı" ise sayının
modeldeki katsayısıdır. Son satır olan "sabit terim", "katsayı" sütununda yalnızca modelin sabit
terimini tutar.
Görev: Dört sayının her biri için "önce logaritma" evet diyorsa değerin doğal logaritmasını al,
ortalamayı çıkar ve standart sapmaya bölerek z-skorunu bul; z-skorunu katsayıyla çarp. Bu, sayının
log-odds değerine katkısıdır. Dakikanın log-odds değerini bulmak için sabit terim ile dört katkıyı
topla ve 1 / (1 + e üzeri eksi log-odds) ile bir olasılığa dönüştür.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her sayının z-skorunu ve katkısını bir tabloda göster, log-odds değerini ve olasılığı yazdır;
olasılığı üç ondalık basamakla "cevap" adıyla sakla.
Test: Sabit terim ile dört katkının toplamı log-odds değerini vermeli ve olasılık 0 ile 1 arasında
olmalı.
```

**Beklenen sonuç:** "cevap" = 0,985

### Adım 2.2: HL7 FHIR kaynakları olarak rapor

**Amaç.** Bu adımda VC-0128'in sonucu, bir hastane bilgi sisteminin okuyabileceği bir HL7 FHIR R4 raporu olarak yazılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Prototipin 24 saatlik raporu, bir kardiyolog onaylayana ya da reddedene kadar ön rapor
olarak hastanın kaydına ulaşmalı ve raporu hangi modelin yazdığını belirtmelidir.
Veri: Defterde "veri" adlı ve tek satırlık bir tablo vardır. Satır, dersin bir karar destek
prototipinin sanal kliniğin telemetri servisindeki bir hasta olan VC-0128 için verdiği sonuçtur;
veriler sentetiktir. "hasta" hastanın kimliğini, "AF yükü (%)" incelenen dakikalardan atriyal
fibrilasyon (AF) alarmı verenlerin payını, "alarm atakları" art arda gelen alarm dakikalarından
oluşan dizilerin sayısını, "en uzun atak (dakika)" ise bunların en uzununu verir. "kaydın
başlangıcı" ve "kaydın sonu" 24 saatlik kaydın dönemini; "model", "sürüm" ve "SHA-256" modeli ve
dosyasının parmak izini; "raporun zamanı" ise raporun yazıldığı zamanı verir. Bütün zamanlar UTC'ye
göre farklarıyla birlikte ISO biçimindedir.
Görev: "collection" türünde, dört kaynaktan oluşan bir FHIR Bundle yaz; her kaynağın bir kimliği ve
http://example.org/fhir altında bir fullUrl değeri olsun. Modelin adını, sürümünü ve SHA-256
değerini içeren bir not taşıyan "af-rr" kimlikli bir Device. Durumu "preliminary", kategorisi
"procedure" olan; http://example.org/vclinic sisteminden "af-burden" yerel kodunu "AF yükü" metniyle
taşıyan; hastayı konu olarak, kaydın dönemini, AF yükünü UCUM'un "%" biriminde bir nicelik olarak
(sistem http://unitsofmeasure.org, kod "%") ve Device'a bir başvuruyu içeren "af-burden" kimlikli
bir Observation. Durumu "preliminary" olan; "Holter kaydı, AF analizi" metnini, hastayı, raporun
zamanını, Observation'a bir başvuruyu ve kelimelerle bir sonucu içeren "af-report" kimlikli bir
DiagnosticReport. Raporu hedef olarak adlandıran, raporun zamanını kaydeden ve Device'ı yazar olarak
veren bir Provenance. Ardından hasta dışında paketin içindeki her başvurunun paketteki bir kaynağa
ulaştığını denetle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Observation'ı JSON olarak yazdır, kaynakların ve bir kaynağa ulaşmayan başvuruların sayısını
yazdır; Observation'daki AF yükünün değerini "cevap" adıyla sakla.
Test: Paket dört kaynak içermeli, içindeki hiçbir başvuru eksik bir kaynağı göstermemeli ve iki
durum da "preliminary" olmalı.
```

**Beklenen sonuç:** "cevap" = 15,5

### Adım 2.3: Tahmin servisine bir istek

**Amaç.** Bu adımda VC-0128'in vuru zamanları dersin tahmin servisine gönderilir ve servisin cevabı okunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Servisin web arayüzü modeli kendisi tutmamalı: Sonucu ve modelin sürümünü veren tahmin
servisine sormalıdır.
Veri: Defterde "veri" adlı ve tek sütunlu bir tablo vardır: "vuru zamanı (s)". Sütun, sanal kliniğin
telemetri servisindeki bir hasta olan VC-0128'in 24 saatlik kaydında monitörün bulduğu 104.314
vurunun zamanlarını, kaydın başından itibaren saniye cinsinden verir; veriler sentetiktir. Veri
hücresi ayrıca dersin bir tahmin servisini bu bilgisayarda http://127.0.0.1:8765/predict adresinde
başlatmıştır. Servis "patient_id" ve "beat_times_s" (saniye cinsinden vuru zamanlarının listesi)
alanlarını içeren JSON biçiminde bir istek alır; modeli, sürümünü ve parmak izini, eşiği, incelenen
dakikaları, atriyal fibrilasyon (AF) alarmı veren dakikaları, yüzde cinsinden AF yükünü ve alarm
ataklarını içeren JSON biçiminde bir cevap verir.
Görev: "VC-0128" hastası için bütün vuru zamanlarını içeren isteği hazırla, POST yöntemiyle JSON
olarak servise gönder ve cevabı JSON olarak oku. Servis bu bilgisayarda çalıştığı için istek bir
vekil sunucudan (proxy) geçmemelidir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İsteğin kilobayt cinsinden büyüklüğünü, modeli, sürümünü ve parmak izinin ilk on iki
basamağını, dakikaları, AF dakikalarını ve AF yükünü yazdır; alarm ataklarını bir tablo olarak
göster ve AF dakikalarının sayısını "cevap" adıyla sakla.
Test: Cevaptaki AF yükü, AF dakikalarının dakikalara bölümünün 100 katına bir ondalık basamakla
yuvarlanmış olarak eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 222

## Durak 3: Kullanıcı testi ve 1.1 sürümü

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-10/ders.html#stop-3) · Python yolunda aynı sonuç: 9. ve 10. bölümler*

Bu durak kullanıcı testini yapar ve prototipi iyileştirir. Telemetri servisindeki dört hastanın alarm atakları bir hekimin 24 saatte neyi inceleyeceğini gösterir; 1.1 sürümü örneklem entropisini ekler ve eğitim kayıtlarında yeniden öğrenir; test kayıtları da iki sürümü bir kez değerlendirir.

### Adım 3.1: Servisin alarm atakları

**Amaç.** Bu adımda servis hekiminin 24 saatte inceleyeceği alarm atakları ve bunların yanlış olanları sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kullanıcı testi, prototipin servis hekimine ne kadar iş çıkardığını ve yanlış alarmlarının
nereden geldiğini soruyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin telemetri servisindeki dört
hastanın 24 saatlik kayıtlarının dakikaları bulunur; veriler sentetiktir: VC-0128 (paroksismal
atriyal fibrilasyon, atriyal erken vurular ve iki elektrot gürültüsü dönemi), VC-0347 (sık atriyal
erken vurulu sinüs ritmi, AF yok), VC-0519 (kalıcı AF) ve VC-0733 (uzun elektrot gürültüsü dönemleri
olan sinüs ritmi, AF yok). Her satır bir dakikadır: "hasta" hastayı, "başlangıç (sa)" dakikanın
kaydın başından itibaren saat cinsinden başlangıcını verir; dakikanın yarısından fazlası kaydın
gerçeğinde AF içindeyse "AF" 1 olur; "olasılık" ise dersin bir modelinin 1.0 sürümünün verdiği AF
olasılığıdır. Model, olasılık en az 0,37 olduğunda alarm verir.
Görev: Her hasta içinde dakikaları başlangıçlarına göre sırala. Bir alarm atağı, alarm veren art
arda dakikalardan oluşan bir dizidir; içinde AF olan hiçbir dakika bulunmayan atak ise bir yanlış
alarm atağıdır. Her hasta için alarm dakikalarını, yanlış alarm dakikalarını (AF olmayan alarm
dakikaları), alarm ataklarını ve yanlış alarm ataklarını say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her hasta için bir satırdan oluşan bir tablo göster, alarm ataklarının ve yanlış olanların
toplamını yazdır; toplam yanlış alarm atağı sayısını "cevap" adıyla sakla.
Test: Hiç AF dakikası olmayan bir hastanın doğru alarm atağı olamaz ve yanlış alarm atakları alarm
ataklarından fazla olamaz.
```

**Beklenen sonuç:** "cevap" = 76

### Adım 3.2: Örneklem entropisiyle 1.1 sürümü

**Amaç.** Bu adımda örneklem entropisi beşinci sayı olarak eklenir, 1.1 sürümü eğitim kayıtlarında kurulur ve doğrulama kayıtlarındaki yanlış alarm atakları sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kullanıcı testi, yanlış alarmların çoğunu erken vuruların verdiğini göstermiştir. Erken
vurular aynı kısa ve uzun aralıkları tekrarlar, AF'de ise örüntü yoktur; bu yüzden örüntüyü ölçen
bir sayı yardımcı olabilir. Test kayıtlarına dokunulmamalıdır.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'ndaki
(AFDB) çoğu paroksismal atriyal fibrilasyonu (AF) olan kişilerin yaklaşık on saatlik 25 Holter
kaydından elde edilen bir dakikalık pencereler arasından eğitim ve doğrulama dakikaları bulunur;
test kayıtları tabloda yoktur. Her satır bir dakikadır: "kayıt" kaydı, "küme" kaydın kümesini
("eğitim", 15 kayıt; "doğrulama", 5 kayıt), "başlangıç (s)" ise dakikanın saniye cinsinden
başlangıcını verir. Dakikanın yarısından fazlası uzmanların işaretlediği AF içindeyse "AF" 1 olur.
"RR aralıkları (s)" sütununun her hücresi dakikanın RR aralıklarını saniye cinsinden ve sırasıyla
tutar. Dakikanın dört sayısı, önceki adımlarda olduğu gibi "kalp hızı" (dakikada), "CV", "RMSSD/RR"
ve "pNN50" sütunlarındadır.
Görev: Her dakika için ayrıca RR aralıklarının örneklem entropisini bir aralıklı dizilerle ve 0,03
saniyelik bir toleransla hesapla: Dakikanın ilk n − 1 aralığı arasında en fazla 0,03 saniye farklı
olan çiftleri say (B); bu çiftlerden kaçının, her aralığa bir sonraki aralık eklendiğinde de benzer
kaldığını say (A). Örneklem entropisi, B'nin A'ya bölümünün doğal logaritmasıdır; A 0 ise 1 say, B 0
ise dakikaya n'nin doğal logaritmasını ver. Eğitim dakikalarında en fazla 3.000 yinelemeyle AF için
beş girdili bir lojistik regresyon kur: Kalp hızı, CV'nin doğal logaritması, RMSSD/RR'nin doğal
logaritması, pNN50 ve örneklem entropisi; her biri eğitim dakikalarının ortalaması ve standart
sapmasıyla bir z-skoruna dönüştürülür. Eşiği yalnızca doğrulama dakikalarında seç: 0,05, 0,06, 0,07
ve bu biçimde 0,95'e kadar giden değerler arasından, AF olan doğrulama dakikalarının en az yüzde
95'inin olasılığının ona eşit ya da ondan büyük olduğu en yüksek değeri al. Ardından her doğrulama
kaydı içinde dakikaları başlangıçlarına göre sırala, alarm ataklarını, yani alarm veren art arda
dakikaları bul ve içinde AF olan hiçbir dakika bulunmayan yanlış alarm ataklarını say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Doğrulama AUC değerini, eşiği, yanlış alarm ataklarının sayısını ve AF olan ve olmayan eğitim
dakikalarının medyan örneklem entropisini yazdır; yanlış alarm ataklarının sayısını "cevap" adıyla
sakla.
Test: Hiçbir test dakikası kullanılmamalı ve her dakikanın örneklem entropisi 0 ya da daha büyük
olmalı.
```

**Beklenen sonuç:** "cevap" = 69

### Adım 3.3: Test kayıtlarında iki sürüm

**Amaç.** Bu adımda test kayıtları bir kez açılır ve modelin iki sürümü karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Klinik servisteki deneme için bir sürüm seçmeden önce kardiyolog, iki sürümün de görmediği
kayıtlarda, 1.1 sürümünün kazanç ve bedelleriyle birlikte değerlendirilmesini istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'nın 5
test kaydının, yani çoğu paroksismal atriyal fibrilasyonu (AF) olan kişilerin Holter kayıtlarının
bir dakikalık pencereleri bulunur. Her satır bir dakikadır: "kayıt" kaydı, "başlangıç (s)" ise
dakikanın saniye cinsinden başlangıcını verir. Dakikanın yarısından fazlası uzmanların işaretlediği
AF içindeyse "AF" 1 olur; "AF payı" dakikanın AF içinde geçen payıdır ve 0 ile 1 arasında değer
alır. "olasılık, 1.0 sürümü" ve "olasılık, 1.1 sürümü" dersin bir modelinin iki sürümünün verdiği AF
olasılıklarıdır. 1.0 sürümü olasılığı en az 0,37, 1.1 sürümü ise olasılığı en az 0,28 olduğunda
alarm verir.
Görev: Her kayıt içinde dakikaları başlangıçlarına göre sırala. Bir alarm atağı, alarm veren art
arda dakikalardan oluşan bir dizidir; içinde AF olan hiçbir dakika bulunmayan atak ise bir yanlış
alarm atağıdır. Her sürüm için bütün test dakikalarında AUC değerini, duyarlılığı (alarm veren AF
dakikalarının payı) ve özgüllüğü (alarm vermeyen öteki dakikaların payı) hesapla. Test
kayıtlarındaki yanlış alarm ataklarını say ve AF yükündeki hatayı hesapla: Her kayıt için alarm
veren dakikalarının payının 100 katı ile ortalama AF payının 100 katı arasındaki mutlak fark,
kayıtlar üzerinden ortalaması alınarak.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her sürüm için bir satırdan oluşan bir tablo göster; 1.1 sürümünün duyarlılığını üç ondalık
basamakla "cevap" adıyla sakla.
Test: Her AUC, duyarlılık ve özgüllük 0 ile 1 arasında olmalı ve her eşik doğrulama kayıtlarında
seçilen eşik olmalı.
```

**Beklenen sonuç:** "cevap" = 0,924

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

### Bir karar destek prototipini denetletmek

```text
Aşağıdaki kodu denetle; kod hekimler için bir karar destek prototipinin ve web arayüzünün bir
parçasıdır. Yedi noktayı kontrol et. Kayıtlar kişi düzeyinde mi ayrılmış, yani hiçbir test kişisinin
dakikası eğitimde kullanılmamış mı? Eşik doğrulama verilerinde mi seçilmiş, testte hiç seçilmemiş
mi? Bir alarmın birimi nedir ve bir kullanıcı hasta ve gün başına kaç alarm görecek? Her çıktı, yani
ekran, rapor ve bir servisin cevabı, modelin sürümünü ve dosyasının parmak izini taşıyor mu? Hekim
her alarmın arkasındaki sinyali görebiliyor ve alarmı onaylamak kadar kolay biçimde, bir kayda giren
bir gerekçeyle reddedebiliyor mu? Her rapor durumu konusunda dürüst mü, yani bir hekim karar verene
kadar ön rapor olarak mı kalıyor? Gerçek bir hastanın herhangi bir kaydı, örneğin çevrim içi bir
servise, kurum dışına çıktı mı? Her nokta için onu cevaplayan satırları aktar, doğru olup
olmadıklarını söyle ve doğru olmadıkları yerde bir düzeltme öner. Başka hiçbir şeyi değiştirme.
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter defterinin 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Kullanıcı testinin alarm atakları

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog bir AF prototipinin kullanıcı testini beş doğrulama kaydında ve bir telemetri
servisinin dört hastasında yapıyor ve incelenecek alarm ataklarının, her atak için bir satır olmak
üzere, listesine ihtiyaç duyuyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda kullanıcı testinin dakikaları bulunur: MIT-BIH
Atriyal Fibrilasyon Veri Tabanı'nın 5 doğrulama kaydı ve sanal kliniğin telemetri servisindeki dört
hastanın 24 saatlik kayıtları; servisin verileri sentetiktir. Her satır bir dakikadır: "kaynak"
"AFDB" ya da "servis" değerini, "kayıt" kaydı ya da hastayı, "başlangıç (sa)" ise dakikanın kaydın
başından itibaren saat cinsinden başlangıcını verir. Dakikanın yarısından fazlası işaretlemede ya da
kaydın gerçeğinde atriyal fibrilasyon (AF) içindeyse "AF" 1 olur; "olasılık, 1.0 sürümü" ise dersin
bir modelinin 1.0 sürümünün verdiği AF olasılığıdır; model 0,37 ya da daha yüksek olasılıkta alarm
verir.
Görev: Her kayıt içinde dakikaları başlangıçlarına göre sırala. Bir alarm atağı, alarm veren art
arda dakikalardan oluşan bir dizidir. Her alarm atağı için kaynağı, kaydı, saat cinsinden
başlangıcı, dakika cinsinden uzunluğu, en yüksek olasılığı ve atağın herhangi bir dakikasında AF
olup olmadığını içeren bir satır oluştur.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Tablonun ilk satırlarını ve her kaydın atak sayısını göster; toplam alarm atağı sayısını
"cevap" adıyla sakla.
Test: Atakların uzunluklarının toplamı alarm veren dakikaların sayısına eşit olmalı.
```

### Adım 2: Hekimin iş yükü

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog, 1.0 sürümüyle bir hekimin 24 saatte kaç alarm atağını inceleyeceğini, bunların
kaçının yanlış olduğunu ve yanlış olanların hangi kayıtlarda toplandığını öğrenmek istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda kullanıcı testinin dakikaları bulunur: MIT-BIH
Atriyal Fibrilasyon Veri Tabanı'nın 5 doğrulama kaydı ve sanal kliniğin telemetri servisindeki dört
hastanın 24 saatlik kayıtları; servisin verileri sentetiktir. Her satır bir dakikadır: "kaynak"
"AFDB" ya da "servis" değerini, "kayıt" kaydı ya da hastayı, "başlangıç (sa)" ise dakikanın kaydın
başından itibaren saat cinsinden başlangıcını verir. Dakikanın yarısından fazlası işaretlemede ya da
kaydın gerçeğinde atriyal fibrilasyon (AF) içindeyse "AF" 1 olur; "olasılık, 1.0 sürümü" ise dersin
bir modelinin 1.0 sürümünün verdiği AF olasılığıdır; model 0,37 ya da daha yüksek olasılıkta alarm
verir.
Görev: Her kayıt içinde dakikaları başlangıçlarına göre sırala. Bir alarm atağı, alarm veren art
arda dakikalardan oluşan bir dizidir; içinde AF olan hiçbir dakika bulunmayan atak ise bir yanlış
alarm atağıdır. Her kayıt için dakikaları, alarm ataklarını ve yanlış alarm ataklarını say; alarm
ataklarını ve yanlış olanları kaydın 24 saati başına ver. Ardından aynısını AFDB ve servis için bir
bütün olarak ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her kayıt için bir satırdan ve iki toplamdan oluşan bir tablo göster; bütün kayıtlarda yanlış
alarm ataklarının payını üç ondalık basamakla "cevap" adıyla sakla.
Test: Bir kaydın yanlış alarm atakları alarm ataklarını aşamaz.
```

### Adım 3: Doğrulama kayıtlarında iyileştirilmiş bir sürüm

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kullanıcı testi yanlış alarmların çoğunu erken vuruların verdiğini göstermiştir. Kardiyolog,
eğitim kayıtlarında kurulan ve yalnızca doğrulama kayıtlarında değerlendirilen iyileştirilmiş bir
sürüm istiyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'ndaki
(AFDB) çoğu paroksismal atriyal fibrilasyonu (AF) olan kişilerin yaklaşık on saatlik 25 Holter
kaydından elde edilen bir dakikalık pencereler bulunur. Test kayıtları tabloda yoktur. Her satır bir
dakikadır: "kayıt" kaydı, "küme" kaydın kümesini ("eğitim", 15 kayıt; "doğrulama", 5 kayıt),
"başlangıç (s)" ise dakikanın kaydın başından itibaren saniye cinsinden başlangıcını verir.
Dakikanın yarısından fazlası uzmanların işaretlediği AF içindeyse "AF" 1, değilse 0 olur. "RR
aralıkları (s)" sütununun her hücresi, dakikanın RR aralıklarını saniye cinsinden ve sırasıyla, 20
ya da daha fazla sayıdan oluşan bir liste olarak tutar. Dakikanın dört sayısı "kalp hızı", "CV",
"RMSSD/RR" ve "pNN50" sütunlarındadır.
Görev: Her dakika için ayrıca RR aralıklarının örneklem entropisini bir aralıklı dizilerle ve 0,03
saniyelik bir toleransla hesapla: Dakikanın ilk n − 1 aralığı arasında en fazla 0,03 saniye farklı
olan çiftleri say (B); bu çiftlerden kaçının, her aralığa bir sonraki aralık eklendiğinde de benzer
kaldığını say (A). Örneklem entropisi, B'nin A'ya bölümünün doğal logaritmasıdır; A 0 ise 1 say, B 0
ise dakikaya n'nin doğal logaritmasını ver. Eğitim dakikalarında en fazla 3.000 yinelemeyle AF için
beş girdili bir lojistik regresyon kur: Kalp hızı, CV'nin doğal logaritması, RMSSD/RR'nin doğal
logaritması, pNN50 ve örneklem entropisi; her biri eğitim dakikalarının ortalaması ve standart
sapmasıyla bir z-skoruna dönüştürülür. Eşiği yalnızca doğrulama dakikalarında seç: 0,05, 0,06, 0,07
ve bu biçimde 0,95'e kadar giden değerler arasından, AF olan doğrulama dakikalarının en az yüzde
95'inin olasılığının ona eşit ya da ondan büyük olduğu en yüksek değeri al. Doğrulama AUC değerini,
eşikteki duyarlılığı ve özgüllüğü ve her doğrulama kaydının yanlış alarm ataklarını ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Sonuçları göster, katsayıları ve eşiği yazdır; eşiği iki ondalık basamakla "cevap" adıyla
sakla.
Test: Hiçbir test dakikası kullanılmamalı ve doğrulama kayıtlarındaki duyarlılık en az 0,95 olmalı.
```

### Adım 4: Test kayıtlarında iki sürüm ve değişiklik kaydı

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Kardiyolog test kayıtlarını iki sürüm için bir kez açıyor ve yeni sürümün değişiklik kaydını
kazançları ve bedelleriyle birlikte yazıyor.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'nın 5
test kaydının, yani çoğu paroksismal atriyal fibrilasyonu (AF) olan kişilerin Holter kayıtlarının
bir dakikalık pencereleri bulunur. Her satır bir dakikadır: "kayıt" kaydı, "başlangıç (s)" dakikanın
saniye cinsinden başlangıcını verir; dakikanın yarısından fazlası uzmanların işaretlediği AF
içindeyse "AF" 1 olur; "AF payı" dakikanın AF içinde geçen payıdır. "RR aralıkları (s)" sütununun
her hücresi dakikanın RR aralıklarını saniye cinsinden tutar; dakikanın dört sayısı "kalp hızı",
"CV", "RMSSD/RR" ve "pNN50" sütunlarındadır.
Görev: 1.0 sürümü dört girdi kullanır: Kalp hızı, CV'nin doğal logaritması, RMSSD/RR'nin doğal
logaritması ve pNN50; 1.1 sürümü bunlara RR aralıklarının bir aralıklı dizilerle ve 0,03 saniyelik
toleransla hesaplanan örneklem entropisini ekler. İki sürümü 1. duraktaki ve 3. adımdaki
biçimleriyle, eğitim dakikalarında kurulduğu gibi ve doğrulama dakikalarından gelen eşikleriyle
kullan. Her kayıt içinde dakikaları başlangıçlarına göre sırala. Bir alarm atağı, alarm veren art
arda dakikalardan oluşan bir dizidir; içinde AF olan hiçbir dakika bulunmayan atak ise bir yanlış
alarm atağıdır. Her sürüm için test dakikalarında AUC değerini, duyarlılığı, özgüllüğü, yanlış alarm
ataklarını ve kayıt başına AF yükündeki ortalama mutlak hatayı yüzde puan olarak hesapla. Ardından
yeni sürüm için sürüm numarasını, değişikliği, gerekçeyi, eşiği, doğrulama ve test kayıtlarındaki
etkileri ve neyin iyileşmediğini içeren bir değişiklik kaydı yaz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki sürümün tablosunu göster ve değişiklik kaydını yazdır; yeni sürümün test kayıtlarındaki
duyarlılığını üç ondalık basamakla "cevap" adıyla sakla.
Test: Test kayıtları her sürüm için bir kez kullanılmalı ve onlara bakıldıktan sonra hiçbir eşik
değiştirilmemeli.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
