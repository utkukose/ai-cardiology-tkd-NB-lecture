# Prompt kütüphanesi, 8. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[8. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-08/PROMPTS.md)

Bu kütüphanede, 8. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: EKG, ekokardiyogram ve laboratuvarla kalp yetersizliği olayları](#durak-1-ekg-ekokardiyogram-ve-laboratuvarla-kalp-yetersizliği-olayları)
3. [Durak 2: Göğüs ağrısı ünitesinde majör olumsuz kardiyak olaylar: HEART, tek modaliteler ve füzyon](#durak-2-göğüs-ağrısı-ünitesinde-majör-olumsuz-kardiyak-olaylar-heart-tek-modaliteler-ve-füzyon)
4. [Durak 3: Triyaj: Başka bir hastane, bir taburculuk eşiği ve net yarar](#durak-3-triyaj-başka-bir-hastane-bir-taburculuk-eşiği-ve-net-yarar)
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

## Durak 1: EKG, ekokardiyogram ve laboratuvarla kalp yetersizliği olayları

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-08/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 8, 1-3. bölümler*

Bu durak oturumun mini projesidir. Sanal kliniğin kayıt sistemindeki hastalar üç modaliteyle tarif edilir: EKG, ekokardiyogram ve laboratuvar değerleri. Her modalite için tek başına ve üçü için birlikte bir model kurulur, erken ve geç füzyon karşılaştırılır; son adım ise füzyon ile en iyi tek modalite arasındaki farktan ne kadar emin olunabileceğini sorar.

### Adım 1.1: Tek başına laboratuvar değerleri

**Amaç.** Bu adımda üç laboratuvar değeriyle kalp yetersizliği olayları için ilk model kurulur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: NT-proBNP, eGFR ve troponinin tek başına 24 ay içinde ölümü ya da kalp yetersizliği
nedeniyle hastaneye yatışı ne kadar iyi öngördüğünü, EKG ve ekokardiyogramı ekleyecek modeller için
bir başlangıç noktası olarak öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin kayıt sisteminden, yani sentetik
bir kohorttan 3.227 hasta bulunur: En az 24 ay izlenen ya da daha önce olay görülen hastalar. Her
satır bir hastadır: "hasta" hastayı, "küme" kümesini verir ("eğitim", 1.936 hasta; "doğrulama", 640
hasta; "test", 651 hasta); "olay" ise hasta 24 ay içinde öldüyse ya da kalp yetersizliği nedeniyle
hastaneye yattıysa 1, aksi hâlde 0 olur. EKG; "kalp hızı" (dakikada), "QRS" ve "QT" (ms), "sol dal
bloğu" ve "atriyal fibrilasyon" (varsa 1) sütunlarını verir. Ekokardiyogram; "ejeksiyon fraksiyonu"
(%), "diyastol sonu çap" (mm), "sol atriyum hacim indeksi" (mL/m²), "E/e'", "TAPSE" (mm) ve "sol
ventrikül kütle indeksi" (g/m²) sütunlarını verir. Laboratuvar; "NT-proBNP" (pg/mL), "eGFR"
(mL/dk/1,73 m²) ve "troponin" (yüksek duyarlıklı, ng/L) sütunlarını verir.
Görev: NT-proBNP ve troponin çok çarpık dağıldığı için ikisinin de logaritmasını kullan. Üç
laboratuvar değerini öznitelik olarak kullan. Sütunları eğitim hastalarıyla standartlaştır ve eğitim
hastalarında bir lojistik regresyon kur. Düzenlileştirmenin miktarını doğrulama hastalarındaki ROC
eğrisi altındaki alana (AUC) göre seç; gücünün tersi için 0,01, 0,1, 1 ve 10 değerlerini dene ve
seçilen modelin test hastalarındaki AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Seçilen gücü, doğrulama ve test AUC değerlerini yazdır; test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: AUC 0 ile 1 arasında olmalı ve hiçbir test hastası son adımdan önce kullanılmamalı.
```

**Beklenen sonuç:** "cevap" = 0,849

### Adım 1.2: Üç modalitenin erken füzyonu

**Amaç.** Bu adımda üç modalitenin 14 değeri yan yana konur ve bunlar üzerinde tek bir model kurulur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir hastanın EKG'sini, ekokardiyogramını ve laboratuvar değerlerini birlikte gören bir
modelin kalp yetersizliği olaylarını tek başına laboratuvar değerlerinden daha iyi öngörüp
öngörmediğini öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin kayıt sisteminden, yani sentetik
bir kohorttan 3.227 hasta bulunur: En az 24 ay izlenen ya da daha önce olay görülen hastalar. Her
satır bir hastadır: "hasta" hastayı, "küme" kümesini verir ("eğitim", 1.936 hasta; "doğrulama", 640
hasta; "test", 651 hasta); "olay" ise hasta 24 ay içinde öldüyse ya da kalp yetersizliği nedeniyle
hastaneye yattıysa 1, aksi hâlde 0 olur. EKG; "kalp hızı" (dakikada), "QRS" ve "QT" (ms), "sol dal
bloğu" ve "atriyal fibrilasyon" (varsa 1) sütunlarını verir. Ekokardiyogram; "ejeksiyon fraksiyonu"
(%), "diyastol sonu çap" (mm), "sol atriyum hacim indeksi" (mL/m²), "E/e'", "TAPSE" (mm) ve "sol
ventrikül kütle indeksi" (g/m²) sütunlarını verir. Laboratuvar; "NT-proBNP" (pg/mL), "eGFR"
(mL/dk/1,73 m²) ve "troponin" (yüksek duyarlıklı, ng/L) sütunlarını verir.
Görev: NT-proBNP ve troponin çok çarpık dağıldığı için ikisinin de logaritmasını kullan. Üç modalite
EKG (kalp hızı, QRS, QT, sol dal bloğu, atriyal fibrilasyon), ekokardiyogram (ejeksiyon fraksiyonu,
diyastol sonu çap, sol atriyum hacim indeksi, E/e', TAPSE, sol ventrikül kütle indeksi) ve
laboratuvardır (NT-proBNP, eGFR, troponin). 14 değerin tamamını tek bir modelin öznitelikleri olarak
birlikte kullan. Sütunları eğitim hastalarıyla standartlaştır ve eğitim hastalarında bir lojistik
regresyon kur. Düzenlileştirmenin miktarını doğrulama hastalarındaki ROC eğrisi altındaki alana
(AUC) göre seç; gücünün tersi için 0,01, 0,1, 1 ve 10 değerlerini dene ve seçilen modelin test
hastalarındaki AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Seçilen gücü, doğrulama ve test AUC değerlerini yazdır; test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Model 14 öznitelik kullanmalı ve AUC 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,83

### Adım 1.3: Logitlerin ortalamasıyla geç füzyon

**Amaç.** Bu adımda her modalite için bir model kurulur ve tahminleri logitlerinin ortalamasıyla birleştirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bütün değerler üzerinde kurulan tek bir modeli, her modalite için birer tane olmak üzere
görüşlerinin ortalaması alınan üç ayrı modelle karşılaştırmak istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin kayıt sisteminden, yani sentetik
bir kohorttan 3.227 hasta bulunur: En az 24 ay izlenen ya da daha önce olay görülen hastalar. Her
satır bir hastadır: "hasta" hastayı, "küme" kümesini verir ("eğitim", 1.936 hasta; "doğrulama", 640
hasta; "test", 651 hasta); "olay" ise hasta 24 ay içinde öldüyse ya da kalp yetersizliği nedeniyle
hastaneye yattıysa 1, aksi hâlde 0 olur. EKG; "kalp hızı" (dakikada), "QRS" ve "QT" (ms), "sol dal
bloğu" ve "atriyal fibrilasyon" (varsa 1) sütunlarını verir. Ekokardiyogram; "ejeksiyon fraksiyonu"
(%), "diyastol sonu çap" (mm), "sol atriyum hacim indeksi" (mL/m²), "E/e'", "TAPSE" (mm) ve "sol
ventrikül kütle indeksi" (g/m²) sütunlarını verir. Laboratuvar; "NT-proBNP" (pg/mL), "eGFR"
(mL/dk/1,73 m²) ve "troponin" (yüksek duyarlıklı, ng/L) sütunlarını verir.
Görev: NT-proBNP ve troponin çok çarpık dağıldığı için ikisinin de logaritmasını kullan. Üç modalite
EKG (kalp hızı, QRS, QT, sol dal bloğu, atriyal fibrilasyon), ekokardiyogram (ejeksiyon fraksiyonu,
diyastol sonu çap, sol atriyum hacim indeksi, E/e', TAPSE, sol ventrikül kütle indeksi) ve
laboratuvardır (NT-proBNP, eGFR, troponin). Her modalite için ayrı ayrı: sütunları eğitim
hastalarıyla standartlaştır ve eğitim hastalarında bir lojistik regresyon kur. Düzenlileştirmenin
miktarını doğrulama hastalarındaki ROC eğrisi altındaki alana (AUC) göre seç; gücünün tersi için
0,01, 0,1, 1 ve 10 değerlerini dene ve seçilen modelin test hastalarındaki AUC değerini hesapla.
Ardından her hastanın üç olasılığını logite, log(p / (1 − p)), dönüştür, ortalamalarını al,
ortalamayı yeniden olasılığa çevir ve test hastalarındaki AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her modalitenin ve geç füzyonlarının test AUC değerini yazdır; geç füzyonun AUC değerini üç
ondalık basamakla "cevap" adıyla sakla.
Test: Her modalite için bir tane olmak üzere üç model olmalı ve AUC 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,833

### Adım 1.4: Farktan ne kadar emin olabiliriz?

**Amaç.** Bu adımda test hastaları yerine koyarak tekrar tekrar çekilir ve erken füzyonun tek başına laboratuvarı ne sıklıkla geçtiği görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Az sayıda olayı olan birkaç yüz test hastasında ölçülen, üç modaliteli bir model ile tek
başına laboratuvar değerleri arasındaki farkın başka hastalarda da geçerli olup olmayacağını
öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin kayıt sisteminden, yani sentetik
bir kohorttan 3.227 hasta bulunur: En az 24 ay izlenen ya da daha önce olay görülen hastalar. Her
satır bir hastadır: "hasta" hastayı, "küme" kümesini verir ("eğitim", 1.936 hasta; "doğrulama", 640
hasta; "test", 651 hasta); "olay" ise hasta 24 ay içinde öldüyse ya da kalp yetersizliği nedeniyle
hastaneye yattıysa 1, aksi hâlde 0 olur. EKG; "kalp hızı" (dakikada), "QRS" ve "QT" (ms), "sol dal
bloğu" ve "atriyal fibrilasyon" (varsa 1) sütunlarını verir. Ekokardiyogram; "ejeksiyon fraksiyonu"
(%), "diyastol sonu çap" (mm), "sol atriyum hacim indeksi" (mL/m²), "E/e'", "TAPSE" (mm) ve "sol
ventrikül kütle indeksi" (g/m²) sütunlarını verir. Laboratuvar; "NT-proBNP" (pg/mL), "eGFR"
(mL/dk/1,73 m²) ve "troponin" (yüksek duyarlıklı, ng/L) sütunlarını verir.
Görev: NT-proBNP ve troponin çok çarpık dağıldığı için ikisinin de logaritmasını kullan. Üç modalite
EKG (kalp hızı, QRS, QT, sol dal bloğu, atriyal fibrilasyon), ekokardiyogram (ejeksiyon fraksiyonu,
diyastol sonu çap, sol atriyum hacim indeksi, E/e', TAPSE, sol ventrikül kütle indeksi) ve
laboratuvardır (NT-proBNP, eGFR, troponin). Laboratuvar değerlerinin modelini ve 14 değerin
tamamının modelini şöyle kur. Sütunları eğitim hastalarıyla standartlaştır ve eğitim hastalarında
bir lojistik regresyon kur. Düzenlileştirmenin miktarını doğrulama hastalarındaki ROC eğrisi
altındaki alana (AUC) göre seç; gücünün tersi için 0,01, 0,1, 1 ve 10 değerlerini dene ve seçilen
modelin test hastalarındaki AUC değerini hesapla. Ardından 2.000 bootstrap örneği çek; her örnek
test hastaları arasından yerine koyarak test hastası sayısı kadar hasta çeksin. Sonucun
tekrarlanabilmesi için rastgelelik tohumunu 2026 olarak sabitle. Olay görülen ve görülmeyen
hastaları içeren her örnekte iki modelin AUC değerini ve farkı (erken füzyon eksi laboratuvar)
hesapla. Ortalama farkı, 2,5. ve 97,5. yüzdelikler arasındaki yüzde 95 aralığını ve farkın 0'ın
üstünde olduğu örneklerin oranını bildir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ortalama farkı ve aralığını yazdır; oranı üç ondalık basamakla "cevap" adıyla sakla.
Test: Oran 0 ile 1 arasında olmalı ve iki model her örnekte aynı hastalar üzerinde
karşılaştırılmalı.
```

**Beklenen sonuç:** "cevap" = 0,041

## Durak 2: Göğüs ağrısı ünitesinde majör olumsuz kardiyak olaylar: HEART, tek modaliteler ve füzyon

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-08/ders.html#stop-2) · Python yolunda aynı sonuç: 4-8. bölümler*

Sanal kliniğin göğüs ağrısı ünitesi 30 gün içindeki MACE'i öngörür. Çıtayı HEART skoru belirler. Bir model klinik tabloyu, troponinleri ve ekokardiyogramı birleştirir; ikinci bir model beş tek modaliteli modeli istifler; son adım ise iki tür geç füzyonun olasılıklarına güvenilip güvenilemeyeceğini sorar.

### Adım 2.1: HEART skoru

**Amaç.** Bu adımda HEART skorunun beş öğesi toplanır ve toplamın MACE görülen ve görülmeyen başvuruları ne kadar iyi ayırdığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Ünitenin her modelinin aşması gereken çıta olarak HEART skorunun göğüs ağrısı ünitesinin
test başvurularındaki sonucunu öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden 800 test başvurusu bulunur. Her satır bir başvurudur: "başvuru"
numarasını verir; "öykü", "EKG", "yaş", "risk faktörleri" ve "troponin" sütunları HEART skorunun beş
öğesinin puanlarını (her biri 0, 1 ya da 2) verir; "MACE" ise 30 gün içinde majör olumsuz kardiyak
olay (miyokard enfarktüsü, acil revaskülarizasyon ya da ölüm) görüldüyse 1, aksi hâlde 0 olur.
Görev: Beş öğeyi HEART skorunda (0-10) topla. Skorun "MACE" sütununa göre AUC değerini hesapla.
Ardından 0-3, 4-6 ve 7-10 gruplarını oluştur ve her biri için başvuru sayısını, oranını ve gruptaki
MACE oranını ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Üç grubun tablosunu yazdır; AUC değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Her skor 0 ile 10 arasında olmalı ve üç grup 800 başvurunun tamamını içermeli.
```

**Beklenen sonuç:** "cevap" = 0,903

### Adım 2.2: Klinik tablonun, troponinlerin ve ekokardiyogramın erken füzyonu

**Amaç.** Bu adımda her başvurunun klinik değerleri, troponinleri ve ekokardiyogramı tek bir satıra konur, boşluklar bir işaretle doldurulur ve tek bir model kurulur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Ekibin gelişten bir saat sonra bildikleriyle, EKG ve not olmadan, ikinci troponini ya da
ekokardiyogramı eksik olan hastaları da tutarak 30 gün içindeki MACE için bir risk modeli kurmak
istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden göğüs ağrısıyla yapılmış 4.000 başvuru bulunur. Her satır bir
başvurudur: "başvuru" numarasını, "küme" kümesini verir ("eğitim", 2.400; "doğrulama", 800; "test",
800). Klinik tablo; "yaş" (yıl), "cinsiyet" ("erkek" ya da "kadın"), varsa 1 olan yedi risk faktörü
("sigara", "diyabet", "hipertansiyon", "hiperlipidemi", "obezite", "aile öyküsü" ve "bilinen koroner
arter hastalığı"), "kalp hızı" (dakikada), "sistolik basınç" (mmHg) ve "eGFR" sütunlarını verir.
Yüksek duyarlıklı troponin T, testin üst referans sınırının katları olarak verilir: "gelişte
troponin" ve ölçülmediğinde boş kalan "bir saat sonra troponin". Yatak başı ekokardiyogram
"ekokardiyogram yapıldı" (1 ya da 0) sütununu ve yapıldıysa "ejeksiyon fraksiyonu" (%) ile "duvar
hareket bozukluğu" (bölgesel bir bozukluk görüldüyse 1) sütunlarını verir; yapılmadıysa bu iki sütun
boştur. "HEART" HEART skorudur; "MACE" ise 30 gün içinde majör olumsuz kardiyak olay görüldüyse 1,
aksi hâlde 0 olur.
Görev: Her başvurunun özniteliklerini oluştur: Yaş, erkek için 1 olan cinsiyet, yedi risk faktörü,
kalp hızı, sistolik basınç ve eGFR; gelişteki troponinin logaritması, bir saat sonraki troponinin
logaritması (ölçülmediyse gelişteki değer), bir saatteki değişim (ölçülmediyse 0) ve ikinci troponin
ölçüldüyse 1 olan bir sütun; ekokardiyogramın yapılıp yapılmadığı, ejeksiyon fraksiyonu
(yapılmadıysa 60) ve duvar hareket bozukluğu (yapılmadıysa 0). HEART skorunu kullanma. Sütunları
eğitim başvurularıyla standartlaştır ve eğitim başvurularında bir lojistik regresyon kur.
Düzenlileştirmenin miktarını doğrulama başvurularındaki ROC eğrisi altındaki alana (AUC) göre seç;
gücünün tersi için 0,01, 0,1, 1 ve 10 değerlerini dene ve seçilen modelin test başvurularındaki AUC
değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Seçilen gücü, doğrulama ve test AUC değerlerini yazdır; test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: 4.000 başvurunun tamamı tutulmalı, model 19 öznitelik kullanmalı ve HEART skoru bunların
arasında olmamalı.
```

**Beklenen sonuç:** "cevap" = 0,9

### Adım 2.3: Beş tek modaliteli modelin istiflenmesi

**Amaç.** Bu adımda beş tek modaliteli modelin her birinin ne kadar sayılması gerektiği doğrulama başvurularında öğrenilir ve birleşim sınanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Her biri göğüs ağrılı bir başvurunun bir modalitesini okuyan beş modelim var; bunların
görüşlerini eşit bir oy yerine verilerden öğrenilen ağırlıklarla tek bir riskte birleştirmek
istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden 800 doğrulama ve 800 test başvurusu bulunur. Her satır bir
başvurudur: "küme" kümesini verir ("doğrulama" ya da "test"); beş sütun ise dersin, her biri tek bir
modaliteden öğrenen ve hepsi eğitim başvurularıyla eğitilmiş beş modelinin 30 gün içinde majör
olumsuz kardiyak olay için verdiği olasılıkları içerir: "olasılık, klinik", "olasılık, troponin",
"olasılık, ekokardiyogram", "olasılık, EKG ağı" ve "olasılık, not". "MACE" böyle bir olay görüldüyse
1, aksi hâlde 0 olur.
Görev: Her başvurunun beş olasılığını logite, log(p / (1 − p)), dönüştür. Yalnızca doğrulama
başvurularında, varsayılan düzenlileştirmeyle, MACE'in beş logit üzerine bir lojistik regresyonunu
kur. Beş ağırlığını ve kesişimini bildir ve olasılıklarının test başvurularındaki AUC değerini
hesapla. Sonucu beş logitin ortalamasıyla karşılaştır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İstiflemenin ağırlıklarını, kesişimini ve test AUC değerini ve ortalamanın test AUC değerini
yazdır; istiflemenin test AUC değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: İstifleme yalnızca doğrulama başvurularında öğrenmeli ve her ağırlık yazdırılmalı.
```

**Beklenen sonuç:** "cevap" = 0,922

### Adım 2.4: Olasılıklara güvenilebilir mi?

**Amaç.** Bu adımda AUC değerleri neredeyse aynı olan iki modelin, erken füzyonun ve logitlerin ortalamasının, kalibrasyonu değerlendirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Hastalara MACE risklerini söylemek ve bir eşiğin altındakileri eve göndermek istiyorum;
hastaları eşit derecede iyi sıralayan iki modelin olasılıklarının söylediklerini ifade edip
etmediğini öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden 800 test başvurusu bulunur. Her satır bir başvurudur: "olasılık,
erken füzyon", dersin beş modaliteyi birlikte kullanan bir modelinin 30 gün içinde majör olumsuz
kardiyak olay için verdiği olasılık; "olasılık, logitlerin ortalaması", beş tek modaliteli modelin
logitlerinin ortalamasından gelen olasılıktır. "MACE" böyle bir olay görüldüyse 1, aksi hâlde 0
olur.
Görev: İki olasılık sütununun her biri için AUC değerini ve ortalama tahmin edilen riski MACE
oranının yanında hesapla. Kalibrasyon kesişimini (eğim 1'e sabitlenmişken ortalama tahmin edilen
riski gözlenen orana eşitleyen logit kayması), kalibrasyon eğimini (MACE'in olasılığın logiti
üzerine düzenlileştirmesiz bir lojistik regresyonu) ve Brier skorunu hesapla. Ardından her biri için
bir güvenilirlik eğrisi çiz: Başvuruları olasılığa göre sırala, eşit büyüklükte on gruba böl ve her
grubun ortalama olasılığını MACE oranına karşı, köşegenle birlikte çiz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki modelin AUC değerini, ortalama tahmin edilen riskini, kesişimini, eğimini ve Brier
skorunu yazdır, iki eğriyi göster; logitlerin ortalamasının kalibrasyon eğimini iki ondalık
basamakla "cevap" adıyla sakla.
Test: İki eğrinin her biri on noktadan oluşmalı ve Brier skorları 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 2,78

## Durak 3: Triyaj: Başka bir hastane, bir taburculuk eşiği ve net yarar

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-08/ders.html#stop-3) · Python yolunda aynı sonuç: 9. ve 10. bölümler*

Hastanesinden çıkan bir model, kullanıldığı yerde denetlenmelidir. İlk adım modeli B hastanesinde ilk hastalarıyla günceller. İkinci adım doğrulama başvurularında bir taburculuk eşiği seçer ve bunu test başvurularında HEART 0-3 ile karşılaştırır. Son adım, yatırma kararı için modelin ve HEART skorunun net yararını sorar.

### Adım 3.1: Başka bir hastane için bir güncelleme

**Amaç.** Bu adımda modelin logitleri, ortalama riski B hastanesinin ilk 300 hastasındaki olay oranına uyacak biçimde kaydırılır ve sonraki 700 hasta denetlenir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: B hastanesinin kardiyoloğu olarak hastaları ve uygulaması farklı olan A hastanesinden bir
model kullanmak istiyorum ve ona güvenmeden önce risklerinin düzeyini B'nin ilk hastalarıyla
düzeltmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin ikinci hastanesi olan B
hastanesinden, yani sentetik bir veri setinden göğüs ağrısıyla yapılmış 1.000 başvuru, geliş
sırasıyla bulunur. Her satır bir başvurudur: "sıra" zamandaki yerini, "olasılık" birinci hastane
olan A'da öğrenmiş bir modelin 30 gün içinde majör olumsuz kardiyak olay için verdiği olasılığı
verir; "MACE" böyle bir olay görüldüyse 1, aksi hâlde 0 olur.
Görev: Olasılıkları logite dönüştür. İlk 300 başvuruda, her logite eklendiğinde kaydırılmış
olasılıkların ortalamasını bu 300 başvurudaki MACE oranına eşitleyen kaymayı bul (örneğin Newton
adımlarıyla). Kaymayı bütün başvuruların logitlerine ekle. Kalan 700 başvuru için güncellemeden
önceki ve sonraki ortalama tahmin edilen riski, gözlenen MACE oranını ve önceki ve sonraki AUC
değerini bildir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kaymayı, ortalamaları, gözlenen oranı ve iki AUC değerini yazdır; kaymayı iki ondalık
basamakla "cevap" adıyla sakla.
Test: Kaymayı bulmak için yalnızca ilk 300 başvuru kullanılmalı ve AUC değişmemeli.
```

**Beklenen sonuç:** "cevap" = 0,37

### Adım 3.2: Bir taburculuk eşiği

**Amaç.** Bu adımda doğrulama başvurularında modelin HEART 0-3 kadar hastayı eve gönderen bir eşiği seçilir ve bu eşiğin eve gönderdiği test hastalarındaki MACE sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Eve gönderilen hasta sayısı aynı kalmak koşuluyla, hastaları HEART 0-3 yerine bir modelin
riskine göre taburcu etmenin daha az majör olumsuz kardiyak olay kaçırıp kaçırmayacağını öğrenmek
istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden 800 doğrulama ve 800 test başvurusu bulunur. Her satır bir
başvurudur: "küme" kümesini ("doğrulama" ya da "test"), "HEART" HEART skorunu (0-10), "olasılık"
dersin beş modalite kullanan bir modelinin 30 gün içinde majör olumsuz kardiyak olay için verdiği
olasılığı verir; "MACE" böyle bir olay görüldüyse 1, aksi hâlde 0 olur.
Görev: Doğrulama başvurularında HEART skoru 0-3 olan hastaları say; bu sayıya k de. Doğrulama
başvurularını olasılığa göre sırala; eşik, en düşük k. olasılıktır. Test başvurularında eşikte ya da
altında kalan her hastayı eve gönder; eve gönderilenlerin sayısını, bunlardaki MACE sayısını, yüzde
95 Wilson aralığıyla birlikte oranlarını ve MACE için duyarlılığı bildir. Aynısını test
başvurularında HEART 0-3 için de bildir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eşiği ve iki sonucu yazdır; modelin eve gönderdiği test hastalarındaki MACE sayısını "cevap"
adıyla sakla.
Test: Eşik yalnızca doğrulama başvurularından gelmeli ve modelin eve gönderdiği hasta sayısı HEART
skorununkine yakın olmalı.
```

**Beklenen sonuç:** "cevap" = 9

### Adım 3.3: Yatırma kararı için net yarar

**Amaç.** Bu adımda modelin riskine göre ve HEART 4 ya da üstüne göre yatırmanın net yararı yüzde 20 eşik olasılığında hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Yüzde 20 MACE riski olan bir hastayı, yakalanan her olay için dört gereksiz yatışı kabul
ederek yatırırdım; bir modelin olasılıklarının bu karara "HEART skoru 4 ya da üstü olan her hastayı
yatır" kuralından daha iyi hizmet edip etmediğini öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden 800 test başvurusu bulunur. Her satır bir başvurudur: "HEART" HEART
skorunu (0-10), "olasılık" dersin beş modalite kullanan bir modelinin 30 gün içinde majör olumsuz
kardiyak olay için verdiği olasılığı verir; "MACE" böyle bir olay görüldüyse 1, aksi hâlde 0 olur.
Görev: t = 0,20 eşik olasılığında doğru pozitifleri (yatırılanlarda MACE) ve yanlış pozitifleri
(yatırılanlarda MACE yok) bir kez olasılığı en az t olan her hastayı yatırmak, bir kez de HEART
skoru 4 ya da üstü olan her hastayı yatırmak için say. Net yarar, doğru pozitiflerin hasta sayısına
bölümünden yanlış pozitiflerin hasta sayısına bölümü ile t / (1 − t) çarpımının çıkarılmasıdır.
Herkesi yatırmanın net yararını da ver.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Üç stratejinin sayılarını ve net yararını yazdır; modelin net yararını üç ondalık basamakla
"cevap" adıyla sakla.
Test: Hiç kimseyi yatırmamanın net yararı 0'dır; modelinki 800 test başvurusunun tamamında
hesaplanmalı.
```

**Beklenen sonuç:** "cevap" = 0,125

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

### Bir füzyon işlem hattını denetletmek

```text
Aşağıdaki kodu denetle; kod hastalara ait birkaç veri türünü bir risk modelinde birleştiriyor ve
doğruluğunu bildiriyor. Yedi noktayı kontrol et. Her girdi karar anında var mı; sonradan kaydedilmiş
bir değer var mı? Herhangi bir girdi, örneğin kesin tanı, olay türü ya da yatış süresi, sonucu ele
veriyor mu? Ölçekleme, eksik değerlerin doldurulması, metin modelleri ve her küçültme yalnızca
eğitim verisinde mi öğrenilmiş? Eşikler ve öteki bütün seçimler test verisinden değil, doğrulama
verisinden mi alınmış? Ayırt etme gücünün yanında kalibrasyon da kesişim, eğim ve Brier skoruyla
bildiriliyor mu? Her laboratuvar değerinin birimi ve testi hastaneler arasında aynı mı ya da
dönüştürülmüş mü; örneğin troponin kendi testinin üst referans sınırının katları olarak mı verilmiş?
Gerçek bir hastanın herhangi bir kaydı ya da serbest metni kurum dışına çıkabilir mi? Her nokta için
ilgili satırı alıntıla, doğru olup olmadığını söyle ve doğru değilse düzeltilmiş kodu ver.
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter defterinin 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Tek modaliteler, füzyon ve HEART

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir göğüs ağrısı ünitesinin her modalitesinden ve hepsinden birlikte kurulan 30 gün içindeki
MACE modellerini HEART skoruyla, her farktan ne kadar emin olunabileceğini gösteren aralıklarla
karşılaştırmak istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin bir göğüs ağrısı ünitesinden,
yani sentetik bir veri setinden göğüs ağrısıyla yapılmış 4.000 başvuru bulunur. Her satır bir
başvurudur: "başvuru" numarasını, "küme" kümesini verir ("eğitim", 2.400; "doğrulama", 800; "test",
800). Klinik tablo; "yaş" (yıl), "cinsiyet" ("erkek" ya da "kadın"), varsa 1 olan yedi risk faktörü
("sigara", "diyabet", "hipertansiyon", "hiperlipidemi", "obezite", "aile öyküsü" ve "bilinen koroner
arter hastalığı"), "kalp hızı" (dakikada), "sistolik basınç" (mmHg) ve "eGFR" sütunlarını verir.
Yüksek duyarlıklı troponin T, testin üst referans sınırının katları olarak verilir: "gelişte
troponin" ve ölçülmediğinde boş kalan "bir saat sonra troponin". Yatak başı ekokardiyogram
"ekokardiyogram yapıldı" (1 ya da 0) sütununu ve yapıldıysa "ejeksiyon fraksiyonu" (%) ile "duvar
hareket bozukluğu" (bölgesel bir bozukluk görüldüyse 1) sütunlarını verir; yapılmadıysa bu iki sütun
boştur. "HEART" HEART skorudur; "MACE" ise 30 gün içinde majör olumsuz kardiyak olay görüldüyse 1,
aksi hâlde 0 olur. Dersin eğitim başvurularıyla eğitilmiş modellerinden iki sütun daha gelir: "EKG
puanı", bir ağın 12 derivasyonlu EKG'den verdiği MACE olasılığının logiti; "not puanı" ise triyaj
notundan gelen olasılığın logitidir.
Görev: Beş öznitelik grubu oluştur: Klinik tablo (yaş, erkek için 1 olan cinsiyet, yedi risk
faktörü, kalp hızı, sistolik basınç, eGFR); troponin (gelişteki troponinin logaritması, ölçülmediyse
gelişteki değerle bir saat sonraki troponinin logaritması, ölçülmediyse 0 ile bir saatteki değişim
ve ikinci troponin ölçüldüyse 1 olan bir sütun); ekokardiyogram (yapılıp yapılmadığı, yapılmadıysa
60 ile ejeksiyon fraksiyonu ve 0 ile duvar hareket bozukluğu); EKG puanı ve not puanı. Her grup için
tek başına ve bütün gruplar için birlikte (erken füzyon) birer model kur; her birini şöyle kur.
Sütunları eğitim başvurularıyla standartlaştır ve eğitim başvurularında bir lojistik regresyon kur.
Düzenlileştirmenin miktarını doğrulama başvurularındaki ROC eğrisi altındaki alana (AUC) göre seç;
gücünün tersi için 0,01, 0,1, 1 ve 10 değerlerini dene ve seçilen modelin test başvurularındaki AUC
değerini hesapla. Her AUC değerine test başvurularından çekilen 2.000 bootstrap örneğinden, 2,5. ve
97,5. yüzdelikler arasında bir yüzde 95 aralığı ver; her modelin HEART skoruna göre farkını aynı
örneklerde hesapla. Sonucun tekrarlanabilmesi için rastgelelik tohumunu 2026 olarak sabitle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her model ve HEART için bir satırdan oluşan bir tablo göster: Aralığıyla birlikte test AUC
değeri ve aralığıyla birlikte HEART skoruna göre farkı; erken füzyonun test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Hiçbir seçim için test başvurusu kullanılmamalı ve HEART skoru hiçbir modelin özniteliği
olmamalı.
```

### Adım 2: İki hastanede kalibrasyon

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: MACE için bir risk modelinin olasılıklarına, öğrendiği hastanenin test hastalarında ve
ikinci bir hastanede, o hastanenin ilk hastalarıyla yapılan bir güncellemeden önce ve sonra
güvenilip güvenilemeyeceğini öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin iki hastanesinden, yani sentetik
bir veri setinden göğüs ağrısıyla yapılmış başvurular bulunur: A hastanesinin 800 doğrulama ve 800
test başvurusu ile B hastanesinin 1.000 başvurusu. Her satır bir başvurudur: "küme" "doğrulama",
"test" ya da "B hastanesi" değerini, "sıra" B'deki bir başvurunun zamandaki yerini (1-1.000; A için
0), "HEART" HEART skorunu (0-10), "olasılık" A hastanesinin beş modaliteyi birleştiren bir modelinin
30 gün içinde majör olumsuz kardiyak olay için verdiği olasılığı verir; "MACE" böyle bir olay
görüldüyse 1, aksi hâlde 0 olur.
Görev: A'nın test başvuruları için ortalama tahmin edilen riski MACE oranının yanında hesapla.
Kalibrasyon kesişimini (eğim 1'e sabitlenmişken ortalama tahmin edilen riski gözlenen orana
eşitleyen logit kayması), kalibrasyon eğimini (MACE'in olasılığın logiti üzerine düzenlileştirmesiz
bir lojistik regresyonu) ve Brier skorunu hesapla. Köşegenle birlikte, eşit büyüklükte on gruplu bir
güvenilirlik eğrisi çiz. B hastanesi için sırası 1-300 olan başvurularda, ortalama tahmin edilen
risklerini MACE oranlarına eşitleyen logit kaymasını bul, bunu B'nin bütün başvurularının
logitlerine ekle ve ölçütleri ve eğriyi, sırası 301-1.000 olan başvurular için güncellemeden önce ve
sonra tekrarla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ölçütleri üç satırlık bir tabloda (A test, B önce, B sonra) ve üç eğriyi göster;
güncellemeden sonra B'deki kalibrasyon kesişimini iki ondalık basamakla "cevap" adıyla sakla.
Test: Kaymayı bulmak için B'nin yalnızca sırası 1-300 olan başvuruları kullanılmalı.
```

### Adım 3: İki taburculuk eşiği

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Göğüs ağrılı hastaları bir modelin riskine göre taburcu etmek için bir eşik seçmek ve bu
eşiğin, seçildiği hastanede ve başka bir hastanede, HEART 0-3'ün yanında kaç olay kaçıracağını
öğrenmek istiyorum.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin iki hastanesinden, yani sentetik
bir veri setinden göğüs ağrısıyla yapılmış başvurular bulunur: A hastanesinin 800 doğrulama ve 800
test başvurusu ile B hastanesinin 1.000 başvurusu. Her satır bir başvurudur: "küme" "doğrulama",
"test" ya da "B hastanesi" değerini, "sıra" B'deki bir başvurunun zamandaki yerini (1-1.000; A için
0), "HEART" HEART skorunu (0-10), "olasılık" A hastanesinin beş modaliteyi birleştiren bir modelinin
30 gün içinde majör olumsuz kardiyak olay için verdiği olasılığı verir; "MACE" böyle bir olay
görüldüyse 1, aksi hâlde 0 olur.
Görev: Yalnızca A'nın doğrulama başvurularında iki eşik seç. Birincisi: HEART skoru 0-3 olan
doğrulama başvurularını say (k) ve en düşük k. olasılığı al. İkincisi: MACE görülen doğrulama
başvurularının en fazla yüzde 2'sinin eşikte ya da altında kaldığı en büyük olasılık. Her eşik ve
HEART 0-3 için A'nın test başvurularında ve B'nin sırası 301-1.000 olan başvurularında şunları
bildir: Eve gönderilenlerin (eşikte ya da altında kalanların) sayısı ve oranı, yüzde 95 Wilson
aralığıyla birlikte bunlardaki MACE ve MACE için duyarlılık.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her hastanedeki her kural için bir satırdan oluşan bir tablo göster; birinci eşikte eve
gönderilen A test başvurularındaki MACE sayısını "cevap" adıyla sakla.
Test: İki eşik de yalnızca A'nın doğrulama başvurularından gelmeli.
```

### Adım 4: Kalp ekibi için bir karar eğrisi

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir MACE risk modelinin hangi karar için yardımcı olduğunu bir kalp ekibine göstermek
istiyorum; bunun için modelin net yararını bir dizi yatırma eşiğinde HEART skorununkiyle
karşılaştıracağım.
Veri: Defterde "veri" adlı bir tablo vardır. Tabloda sanal kliniğin iki hastanesinden, yani sentetik
bir veri setinden göğüs ağrısıyla yapılmış başvurular bulunur: A hastanesinin 800 doğrulama ve 800
test başvurusu ile B hastanesinin 1.000 başvurusu. Her satır bir başvurudur: "küme" "doğrulama",
"test" ya da "B hastanesi" değerini, "sıra" B'deki bir başvurunun zamandaki yerini (1-1.000; A için
0), "HEART" HEART skorunu (0-10), "olasılık" A hastanesinin beş modaliteyi birleştiren bir modelinin
30 gün içinde majör olumsuz kardiyak olay için verdiği olasılığı verir; "MACE" böyle bir olay
görüldüyse 1, aksi hâlde 0 olur.
Görev: A'nın test başvurularını kullan. 0,01'den 0,30'a 0,01'lik adımlarla her t eşik olasılığı için
olasılığı en az t olan her başvuruyu yatırmanın, HEART skoru 4 ya da üstü olan her başvuruyu
yatırmanın ve herkesi yatırmanın net yararını hesapla: Doğru pozitiflerin başvuru sayısına
bölümünden yanlış pozitiflerin başvuru sayısına bölümü ile t / (1 − t) çarpımının çıkarılması. Hiç
kimseyi yatırmamanın 0 çizgisiyle birlikte üç eğriyi çiz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Karar eğrisini göster ve 0,05, 0,10, 0,20 ve 0,30 eşiklerinde üç net yararı yazdır; modelin
0,20 eşikteki net yararını üç ondalık basamakla "cevap" adıyla sakla.
Test: Hiç kimseyi yatırmamanın net yararı her eşikte 0'dır.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
