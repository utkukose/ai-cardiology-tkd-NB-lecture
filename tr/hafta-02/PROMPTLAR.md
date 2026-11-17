# Prompt kütüphanesi, 2. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[2. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-02/PROMPTS.md)

Bu kütüphanede, 2. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın altındaki hücreye yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

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
| 2. Kopyalayın ve gönderin | Promptu kopyalayın ve bir YZ asistanına gönderin: Google Colab'daki Gemini ya da başka bir tarayıcı sekmesindeki ChatGPT, Claude, Copilot veya Gemini. |
| 3. Çalıştırın | Asistanın kodunu promptun altındaki hücreye yapıştırın ve çalıştırın. |
| 4. Denetleyin | Kontrol hücresini çalıştırın. Hücre *doğru* ya da *henüz değil* yazar ve sonucun değerini gösterir. |
| 5. Onarın | Kontrol *henüz değil* yazarsa onarım promptunu kodla birlikte gönderin. Sonuç yine yanlışsa doğru sonucu veren *Hazır kod* hücresini çalıştırın. |
| 6. Açıklatın ve kaydedin | Asistandan kodu sade bir dille açıklamasını isteyin; aracı, promptu ve neyin denetlendiğini YZ kullanım günlüğüne yazın. |

## Durak 1: İlk risk modeli

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 2, 1. ve 2. bölümler*

UCI Heart Disease veri setindeki Cleveland hastalarına efor testi ve koroner anjiyografi yapılmıştır. Bu durakta öykü ve efor testinden alınan sekiz değişkenle bir lojistik regresyon kurulur; modelin daha önce görmediği hastalarda koroner arter hastalığını ne kadar iyi tanıdığı denetlenir.

### Adım 1.1: Model ve test AUC değeri

**Amaç.** Bu adımda modelin tablosu kurulur, hastalar eğitim ve test kümelerine ayrılır, bir lojistik regresyon eğitilir ve model test kümesinde ROC eğrisinin altındaki alanla (AUC) ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: `heart`, UCI Heart Disease veri setinde Cleveland Clinic'ten gelen 303 hastayı tutan bir
tablodur ve her hasta bir satırda yer alır. Burada kullanılan sütunlar şunlardır: age (yaş, yıl);
sex (erkekler için 1, kadınlar için 0); göğüs ağrısının tipini veren cp (1 tipik anjina, 2 atipik
anjina, 3 anjina dışı ağrı, 4 asemptomatik); trestbps (istirahat kan basıncı, mmHg); chol (serum
kolesterolü, mg/dL); thalach (efor testinde ulaşılan en yüksek kalp hızı, atım/dk); exang (eforla
ortaya çıkan anjina; varsa 1); oldpeak (eforda istirahate göre ST çökmesi, mm) ve disease. disease,
anjiyografide en az bir büyük koroner arterin çapı yüzde 50'den fazla daralmışsa 1, değilse 0
değerini alır.
Görev: Modelin X tablosunu age, sex, trestbps, chol, thalach, exang, oldpeak ve cp sütunlarından
kur. Göğüs ağrısı tipi (cp) bir kategoridir: Onu her tip için bir evet/hayır sütununa çevir ve ilk
tipi, yani tipik anjinayı, referans olarak dışarıda bırak. Sonuç değişkeni y, disease sütunudur.
Hastaları dörtte üçü eğitim, dörtte biri test kümesi olacak biçimde rastgele ayır; hastalığı
olanların oranı iki kümede de aynı kalsın ve rastgele ayırma için RANDOM_STATE değerini kullan.
Değişkenleri yalnızca eğitim hastalarının ortalama ve standart sapmalarıyla standartlaştır, eğitim
kümesinde bir lojistik regresyon eğit ve modelin test kümesindeki olasılıklarından ROC eğrisinin
altındaki alanı (AUC) hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Test kümesinin AUC değerini üç ondalık basamağa yuvarlayarak ver. X, y, X_train, X_test,
y_train ve y_test tablolarını ve eğitilmiş modeli model adıyla sakla; sonraki adımlar bunları
kullanmaktadır. Sonucu `auc_test` adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca
kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Test kümesinde 76 hasta bulunmalı ve AUC 0,5 ile 1 arasında olmalıdır.
```

**Beklenen sonuç:** `auc_test` = 0,931

### Adım 1.2: 0,5 eşiğinde duyarlılık

**Amaç.** Bu adımda olasılıklar 0,5 eşiğinde karara dönüştürülür ve modelin hastalığı olanların ne kadarını tanıdığı bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: 1.1. adımda eğitilmiş model (model) ile X_test ve y_test test kümesi (y_test: hastalık varsa
1, yoksa 0).
Görev: Modelin her test hastasına verdiği hastalık olasılığını hesapla ve olasılığı 0,5 ya da
üzerinde olan hastayı pozitif say. Doğru pozitifleri (TP; hastalığı olup pozitif sayılanlar) ve
yanlış negatifleri (FN; hastalığı olup negatif sayılanlar) say. Duyarlılık, TP / (TP + FN) oranıdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Duyarlılığı üç ondalık basamağa yuvarlayarak ver. Sonucu `sensitivity` adıyla sakla ve kısa
bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa
bir açıklama satırı ekle.
Test: TP + FN, test kümesindeki hastalığı olanların sayısına, yani 35'e eşit olmalıdır.
```

**Beklenen sonuç:** `sensitivity` = 0,8

### Adım 1.3: En yüksek kalp hızının odds oranı

**Amaç.** Bu adımda efor testinde ulaşılan en yüksek kalp hızı bir standart sapma arttığında koroner arter hastalığının odds değerinin nasıl değiştiği modelden okunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: 1.1. adımda eğitim kümesinde eğitilmiş model (model): standartlaştırılmış değişkenler üzerinde
bir lojistik regresyon. Değişkenlerin adları X tablosunun sütun adlarıdır.
Görev: Lojistik regresyonun katsayılarını al, her birini ait olduğu değişkenin adıyla eşleştir ve
her katsayıyı standart sapma başına bir odds oranına, yani e'nin katsayı kadar kuvvetine çevir.
Bütün odds oranlarını yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: thalach değişkeninin odds oranını iki ondalık basamağa yuvarlayarak ver. Sonucu `or_thalach`
adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her
adımın üstüne kısa bir açıklama satırı ekle.
Test: oldpeak değişkeninin odds oranı 1'in üzerinde olmalıdır.
```

**Beklenen sonuç:** `or_thalach` = 0,58

## Durak 2: Bir modeli dürüstçe sınamak

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-2) · Python yolunda aynı sonuç: 3-6. bölümler*

76 hastalık tek bir test kümesi belirsiz bir tahmin verir ve bazı modeller olduklarından daha iyi görünür. Bu durakta test çapraz doğrulamayla tekrarlanır ve bir rastgele orman denenir. Ardından sanal kliniğin nadir bir sonucuna geçilir: 12 ay içinde ölüm ya da kalp yetersizliği nedeniyle hastaneye yatış.

### Adım 2.1: Beş katlı çapraz doğrulama

**Amaç.** Bu adımda 1. duraktaki lojistik regresyon, her seferinde hastaların başka bir beşte birinde olmak üzere beş kez sınanır ve ortalama AUC alınır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: 1.1. adımın X ve y tabloları: X, 303 Cleveland hastasının tamamı için modelin değişkenlerini;
y ise sonucu, yani hastalık varsa 1, yoksa 0 değerini tutar.
Görev: 1.1. adımdakiyle aynı türden bir modeli, yani standartlaştırma ve ardından lojistik
regresyonu, beş katlı çapraz doğrulamayla değerlendir. Hastaları RANDOM_STATE ile karıştır ve
hastalığı olanların oranını koruyan beş kata ayır. Dört katta eğit, beşincide AUC değerini hesapla;
her kat bir kez test kümesi olacak biçimde bunu beş kez tekrarla. Beş AUC değerini ve ortalamalarını
yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Beş katın ortalama AUC değerini üç ondalık basamağa yuvarlayarak ver. Sonucu `auc_cv` adıyla
sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın
üstüne kısa bir açıklama satırı ekle.
Test: Her biri 0,5 ile 1 arasında olan beş değer yazdırılmalıdır.
```

**Beklenen sonuç:** `auc_cv` = 0,871

### Adım 2.2: Bir rastgele orman

**Amaç.** Bu adımda aynı hastalarda daha esnek bir model eğitilir ve test AUC değeri lojistik regresyonunkiyle karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: 1.1. adımın tabloları: X, modelin değişkenlerini, yani age, sex, trestbps, chol, thalach,
exang, oldpeak sütunlarını ve göğüs ağrısı tiplerinin evet/hayır sütunlarını; y ise disease sütununu
tutar. X_train ve y_train eğitim kümesini, X_test ve y_test ise 303 hastanın 76'sından oluşan test
kümesini oluşturur.
Görev: Eğitim kümesinde 300 ağaçlı bir rastgele orman eğit; ormanın rastgele seçimleri için
RANDOM_STATE değerini kullan. Ardından ormanın test kümesindeki olasılıklarından AUC değerini
hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Ormanın test AUC değerini üç ondalık basamağa yuvarlayarak ver. Sonucu `auc_forest` adıyla
sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın
üstüne kısa bir açıklama satırı ekle.
Test: AUC 0,5 ile 1 arasında olmalıdır.
```

**Beklenen sonuç:** `auc_forest` = 0,904

### Adım 2.3: Nadir bir sonuç

**Amaç.** Bu adımda hastaların yalnızca 100'de 3 kadarında görülen 12 aylık olay için bir model eğitilir ve sınıf ağırlıklarının modelin bulduklarını nasıl değiştirdiği görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: `registry`, sanal kliniğin 2.000 sentetik hastasını izlem bilgileriyle birlikte tutan bir
tablodur ve her hasta bir satırda yer alır. Burada kullanılan sütunlar şunlardır: age (yaş, yıl),
egfr (tahmini glomerüler filtrasyon hızı, mL/dk/1,73 m²), lvef (sol ventrikül ejeksiyon fraksiyonu,
%), ntprobnp (N-terminal pro-B tipi natriüretik peptit, pg/mL), af (atriyal fibrilasyon; varsa 1),
diabetes (varsa 1), bmi (beden kitle indeksi, kg/m²), sbp (sistolik kan basıncı, mmHg) ve event_12m.
event_12m, hasta izlemin ilk 12 ayında ölmüşse ya da kalp yetersizliği nedeniyle hastaneye yatmışsa
1, değilse 0'dır.
Görev: age, egfr, lvef, ntprobnp, af ve diabetes sütunlarından Xe tablosunu kur; ntprobnp yerine
onun doğal logaritmasını kullan. Sonuç değişkeni ye, event_12m sütunudur. Hastaları RANDOM_STATE ile
ve olay oranını koruyarak yüzde 70'i eğitim, yüzde 30'u test kümesi olacak biçimde rastgele ayır.
Değişkenleri eğitim hastalarıyla standartlaştır ve dengeli sınıf ağırlıklarıyla bir lojistik
regresyon eğit; bu ağırlıklar, olay yaşayan az sayıdaki hastaya toplamda diğer bütün hastalar kadar
ağırlık verir. Olasılığı 0,5 ya da üzerinde olan test hastasını pozitif say ve test kümesinde
duyarlılığı, yani TP / (TP + FN) oranını hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Duyarlılığı üç ondalık basamağa yuvarlayarak ver. Sonucu `se_balanced` adıyla sakla ve kısa
bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa
bir açıklama satırı ekle.
Test: Test kümesinde 600 hasta bulunmalı ve bunların 20'sinde olay olmalıdır. Sınıf ağırlıkları
olmayan aynı model, 0,5 eşiğinde bu olayların hiçbirini bulamaz.
```

**Beklenen sonuç:** `se_balanced` = 0,65

## Durak 3: Alt gruplar, sağkalım ve denetlenecek bir model

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-3) · Python yolunda aynı sonuç: 7-9. bölümler*

Kalp yetersizliği olan hastalar yalnızca ejeksiyon fraksiyonuyla değil, başka özellikleriyle de birbirinden ayrılır. Bu durakta önce, yönteme sonuç bilgisi verilmeden alt gruplar aranır; ardından izlem boyunca sağkalım kestirilir. Son olarak bir YZ asistanının kusursuz bir sonuç bildirdiği bir model denetlenir.

### Adım 3.1: Üç küme

**Amaç.** Bu adımda k-ortalamalar yöntemi kalp yetersizliği olan hastalar arasında üç grup arar; ardından bu gruplar gizli fenogruplarla karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: `hf`, sanal klinikte kalp yetersizliği olan 407 hastayı, yani ana tanısı HFrEF ya da HFpEF
olanları tutan bir tablodur. `HF_FEATURES` bu tablonun dokuz sütununu sıralar: age, bmi, egfr, lvef,
ntprobnp, lavi (sol atriyum hacim indeksi, mL/m²), e_e_prime (E/e′ oranı), lv_mass_index (sol
ventrikül kütle indeksi, g/m²) ve tapse_mm (triküspit anüler düzlem sistolik hareketi, mm).
hf_phenogroup sütunu, kliniğin verileri üretirken kullandığı gizli fenogrubu tutar.
Görev: HF_FEATURES listesindeki dokuz sütunu al, ntprobnp yerine onun doğal logaritmasını kullan ve
sütunları standartlaştır. Hastaları k-ortalamalar yöntemiyle üç kümeye ayır; yöntemi RANDOM_STATE
ile ve farklı rastgele başlangıç noktalarından on kez başlat. Kümeleri gizli fenogruplarla
(hf_phenogroup) düzeltilmiş Rand indeksiyle karşılaştır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Düzeltilmiş Rand indeksini üç ondalık basamağa yuvarlayarak ver. Sonucu `ari` adıyla sakla ve
kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne
kısa bir açıklama satırı ekle.
Test: Üç kümedeki hastaların toplamı 407 olmalıdır. İndeksin 1 olması tam uyumu, 0 olması ise
rastlantısal uyumu gösterir.
```

**Beklenen sonuç:** `ari` = 0,706

### Adım 3.2: 24. ayda Kaplan-Meier

**Amaç.** Bu adımda HFrEF hastalarının izlemin başlamasından iki yıl sonra hangi oranda hayatta olduğu ve kalp yetersizliği nedeniyle hastaneye yatmadığı kestirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: `hf`, sanal klinikte kalp yetersizliği olan 407 hastayı, yani ana tanısı HFrEF ya da HFpEF
olanları tutan bir tablodur. `HF_FEATURES` bu tablonun dokuz sütununu sıralar: age, bmi, egfr, lvef,
ntprobnp, lavi (sol atriyum hacim indeksi, mL/m²), e_e_prime (E/e′ oranı), lv_mass_index (sol
ventrikül kütle indeksi, g/m²) ve tapse_mm (triküspit anüler düzlem sistolik hareketi, mm).
hf_phenogroup sütunu, kliniğin verileri üretirken kullandığı gizli fenogrubu tutar. followup_months,
izlemin başlangıcından ilk olaya ya da izlemin sonuna kadar geçen süredir (ay). event, ölüm ya da
kalp yetersizliği nedeniyle yatış için 1, izlemden olaysız ayrılan (sansürlenen) hasta için 0'dır.
Görev: Ana tanısı HFrEF olan hastalar için olaysız sağkalımın Kaplan-Meier kestirimini adım adım
hesapla. 1'den başla. En az bir olayın görüldüğü her zamanda kestirimi 1 − d/n ile çarp; burada d o
zamandaki olay sayısı, n ise o zamanda hâlâ izlenen, yani izlem süresi en az o kadar olan hasta
sayısıdır. 24. aydaki kestirim, 24 ay ya da daha kısa olan son olay zamanından sonraki değerdir.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: 24. aydaki kestirimi üç ondalık basamağa yuvarlayarak ver. Sonucu `s24_hfref` adıyla sakla ve
kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne
kısa bir açıklama satırı ekle.
Test: Aynı hesap HFpEF hastaları için 24. ayda daha yüksek bir değer vermelidir.
```

**Beklenen sonuç:** `s24_hfref` = 0,733

### Adım 3.3: Bir asistanın modelini denetlemek

**Amaç.** Bir YZ asistanı, 12 ay içindeki olay için 1,000'lik bir AUC bildirmiştir. Bu adımda aynı türden bir modelin dürüst bir değerlendirmede ne verdiği bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 2. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib) ile makine öğrenmesi
paketi scikit-learn hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: `registry`, sanal kliniğin 2.000 sentetik hastasını izlem bilgileriyle birlikte tutan bir
tablodur ve her hasta bir satırda yer alır. Burada kullanılan sütunlar şunlardır: age (yaş, yıl),
egfr (tahmini glomerüler filtrasyon hızı, mL/dk/1,73 m²), lvef (sol ventrikül ejeksiyon fraksiyonu,
%), ntprobnp (N-terminal pro-B tipi natriüretik peptit, pg/mL), af (atriyal fibrilasyon; varsa 1),
diabetes (varsa 1), bmi (beden kitle indeksi, kg/m²), sbp (sistolik kan basıncı, mmHg) ve event_12m.
event_12m, hasta izlemin ilk 12 ayında ölmüşse ya da kalp yetersizliği nedeniyle hastaneye yatmışsa
1, değilse 0'dır. Asistanın modeli, ancak izlemden sonra bilinen followup_months değişkenini de
kullanmış ve AUC değerini eğitildiği hastaların kendisinde ölçmüştür.
Görev: Karar anında bilinmediği için followup_months değişkenini dışarıda bırak. event_12m sonucunu
age, egfr, lvef, ntprobnp, af, diabetes, bmi ve sbp sütunlarıyla, yaprakları en az 5 hasta içeren
200 ağaçlı bir rastgele ormanla öngör; ormanda RANDOM_STATE değerini kullan. Modeli, hastaları
RANDOM_STATE ile karıştıran ve her katta olay oranını koruyan beş katlı bir çapraz doğrulamayla ölç
ve beş katın ortalama AUC değerini al.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Ortalama AUC değerini üç ondalık basamağa yuvarlayarak ver. Sonucu `auc_review` adıyla sakla
ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne
kısa bir açıklama satırı ekle.
Test: AUC, 1,000'in belirgin biçimde altında olmalıdır.
```

**Beklenen sonuç:** `auc_review` = 0,849

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

### Model denetimi istemek

```text
Aşağıdaki kod bir öngörü modeli kurup değerlendirmektedir. Dört noktayı denetle. Model, karar anında
bilinemeyecek bir değişken kullanıyor mu? Ayırmadan önce bütün hastalardan öğrenen bir adım var mı?
Başarım hangi hastalarda ölçülüyor? Sonuç nadir mi? Kısa bir listeyle cevap ver, ardından
düzeltilmiş kodu ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Fenogrup sayısını seçmek

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 2. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy, Matplotlib ve SciPy), makine öğrenmesi paketi scikit-learn ve
vclinic ders paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: registry, sanal kliniğin 2.000 hastasını izlem bilgileriyle birlikte tutar. Kalp yetersizliği
olan hastaların ana tanısı "HFrEF" ya da "HFpEF"tir. Sütunlar şunlardır: age (yaş, yıl), sex, bmi
(kg/m²), diabetes ve af (0 ya da 1), egfr (mL/dk/1,73 m²), lvef (%), ntprobnp (pg/mL), lavi (mL/m²),
e_e_prime, lv_mass_index (g/m²), tapse_mm (mm), followup_months (ay) ve event (ölüm ya da kalp
yetersizliği nedeniyle yatış için 1, sansürlenmiş hasta için 0).
Görev: Kalp yetersizliği olan hastaları al ve dokuz değişkeni standartlaştır: age, bmi, egfr, lvef,
ntprobnp'nin doğal logaritması, lavi, e_e_prime, lv_mass_index ve tapse_mm. 2'den 6'ya kadar her
küme sayısı k için hastaları k-ortalamalar yöntemiyle kümelere ayır; yöntemi RANDOM_STATE ile ve
farklı rastgele başlangıç noktalarından on kez başlat. Her k için küme içi kareler toplamını (WCSS)
ve ortalama siluet değerini bildir, k'yi seç ve seçimin klinik gerekçesini yaz.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: k, WCSS ve siluet değerlerinden oluşan bir tablo göster ve kalp yetersizliği olan hastaların
tablosuna cluster adlı yeni bir sütun ekle. Yalnızca kodu tek bir blok hâlinde ver ve her adımın
üstüne kısa bir açıklama satırı ekle.
Test: Kalp yetersizliği olan hastaların sayısı kümelemeden önce ve sonra aynı olmalı ve her kümede
en az 30 hasta bulunmalıdır.
```

### Adım 2: Fenogrupları tanımlamak ve adlandırmak

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 2. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy, Matplotlib ve SciPy), makine öğrenmesi paketi scikit-learn ve
vclinic ders paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: 1. adımda oluşturulan, kalp yetersizliği olan hastaların tablosu; tabloda cluster sütunu ve
kaydın sütunları yer alır.
Görev: Her kümenin büyüklüğünü ve age, kadın cinsiyeti, bmi, diabetes, af, egfr, lvef, ntprobnp
(ortanca olarak), lavi, e_e_prime, lv_mass_index ve tapse_mm değişkenlerinin ortalamasını ya da
yüzdesini, ayrıca HFrEF oranını gösteren bir tablo oluştur. Her küme için kısa bir klinik ad öner.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Her küme için bir sütun içeren bir tablo göster. Yalnızca kodu tek bir blok hâlinde ver ve
her adımın üstüne kısa bir açıklama satırı ekle.
Test: Tablodaki küme büyüklüklerinin toplamı, kalp yetersizliği olan hastaların sayısına eşit
olmalıdır.
```

### Adım 3: Fenogruba göre prognoz

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 2. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy, Matplotlib ve SciPy), makine öğrenmesi paketi scikit-learn ve
vclinic ders paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: 1. adımın cluster, main_diagnosis, followup_months ve event sütunlarını içeren tablosu ile
Jupyter defterinin 8. bölümündeki sağkalım eğrileri ve log-rank testi için kaplan_meier ve logrank
araçları.
Görev: Kümelerin Kaplan-Meier eğrilerini ve ikinci bir panelde HFrEF ile HFpEF eğrilerini çiz. Her
grubun 24. aydaki sağkalımını ve iki gruplamanın her biri için log-rank testini bildir.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: İki panelli bir şekil, 24. aydaki sağkalım tablosu ve iki log-rank testini göster. Yalnızca
kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Eğriler 1'den başlamalı ve hiç yükselmemelidir; HFrEF ile HFpEF'yi karşılaştıran log-rank
testi 8. bölümdeki p değerini vermelidir.
```

### Adım 4: Gizli gerçekle karşılaştırmak

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, 2. haftanın Jupyter defterinde çalışacak. Tablolar, hesaplar ve grafikler için
kullanılan paketler (pandas, NumPy, Matplotlib ve SciPy), makine öğrenmesi paketi scikit-learn ve
vclinic ders paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı
sabit değeri tutar.
Veri: 1. adımın cluster ve hf_phenogroup sütunlarını içeren tablosu; hf_phenogroup, eğitimin her
hastaya gizli olarak atadığı fenogruptur.
Görev: Kümeleri hf_phenogroup ile çapraz tabloya dök ve düzeltilmiş Rand indeksini hesapla.
Kümelemenin, yalnızca ejeksiyon fraksiyonuna bakıldığında gözden kaçan neyi bulduğunu üç cümleyle
yaz.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Çapraz tabloyu, düzeltilmiş Rand indeksini ve üç cümleyi ver. Yalnızca kodu tek bir blok
hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Düzeltilmiş Rand indeksi −1 ile 1 arasında olmalı; üç kümeyle 0,5'in belirgin biçimde üzerinde
bulunmalıdır.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
