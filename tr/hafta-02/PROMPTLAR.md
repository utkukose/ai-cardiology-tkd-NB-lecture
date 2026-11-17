# Prompt kütüphanesi, 2. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[2. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-02/PROMPTS.md)

Bu kütüphanede 2. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki her prompt, eğitimin prompt kartıyla yazılmış olarak yer almaktadır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod defterde aynı numaralı adımın altındaki hücreye yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

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

*[Ders sayfası: uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 2, 1. ve 2. bölümler*

UCI Heart Disease veri setindeki Cleveland hastalarına efor testi ve koroner anjiyografi yapılmıştır. Bu durakta öykünün ve efor testinin sekiz değişkeninden bir lojistik regresyon kurulur ve modelin, hiç görmediği hastalarda koroner arter hastalığını ne kadar iyi tanıdığı denetlenir.

### Adım 1.1: Model ve test AUC değeri

**Amaç.** Modelin tablosunu kurmak, hastaları eğitim ve test kümelerine ayırmak, bir lojistik regresyon eğitmek ve modeli test kümesinde ROC eğrisinin altındaki alanla (AUC) ölçmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: `heart`, UCI Heart Disease veri setindeki Cleveland Clinic'e ait 303 hastayı içeren bir pandas
DataFrame'idir. Burada kullanılan sütunlar: age (yaş, yıl), sex (1 erkek, 0 kadın), cp (göğüs ağrısı
tipi: 1 tipik angina, 2 atipik angina, 3 anjinal olmayan ağrı, 4 asemptomatik), trestbps (istirahat
kan basıncı, mm Hg), chol (serum kolesterolü, mg/dL), thalach (efor testinde ulaşılan en yüksek kalp
hızı, atım/dakika), exang (eforla gelen angina, 1 evet), oldpeak (eforda istirahate göre ST çökmesi,
mm) ve disease (anjiyografide en az bir ana koroner arterde yüzde 50'den fazla çap daralması varsa
1, yoksa 0).
Görev: age, sex, trestbps, chol, thalach, exang, oldpeak ve cp sütunlarından X tablosunu kur; cp'yi
pd.get_dummies(..., columns=["cp"], drop_first=True, dtype=int) ile kukla değişkenlere dönüştür.
Sonuç değişkeni y, disease sütunudur. train_test_split(X, y, test_size=0.25, stratify=y,
random_state=RANDOM_STATE) ile X_train, X_test, y_train ve y_test olarak ayır. model =
make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)) modelini eğitim kümesinde eğit,
ardından test kümesinin tahmin edilen olasılıklarından roc_auc_score ile AUC değerini hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Test kümesinin AUC değeri, üç ondalığa yuvarlanmış olarak. Sonraki adımlar kullanacağı için
X, y, X_train, X_test, y_train, y_test ve model adlarını koru. Sonucu `auc_test` adlı bir değişkene
kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa
bir yorum satırı ekle.
Test: Test kümesinde 76 hasta bulunmalı ve AUC 0,5 ile 1 arasında olmalı.
```

**Beklenen sonuç:** `auc_test` = 0,931

### Adım 1.2: 0,5 eşiğinde duyarlılık

**Amaç.** Olasılıkları 0,5 eşiğinde karara dönüştürmek ve modelin hastalığı olanların ne kadarını tanıdığını bulmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: 1.1. adımda eğitilen `model` ile `X_test` ve `y_test` test kümesi (y_test: 1 hastalık var, 0
yok).
Görev: Test hastalarının hastalık olasılıklarını model.predict_proba(X_test)[:, 1] ile hesapla.
Olasılığı 0,5 ya da daha yüksek olan hastayı pozitif say. Gerçek pozitifleri (TP) ve yanlış
negatifleri (FN) say ve duyarlılığı TP / (TP + FN) ile hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Duyarlılık, üç ondalığa yuvarlanmış olarak. Sonucu `sensitivity` adlı bir değişkene kaydet ve
kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum
satırı ekle.
Test: TP + FN, test kümesindeki hastalığı olanların sayısına, y_test.sum() değerine, yani 35'e eşit
olmalı.
```

**Beklenen sonuç:** `sensitivity` = 0,8

### Adım 1.3: En yüksek kalp hızının odds oranı

**Amaç.** Efor testinde ulaşılan en yüksek kalp hızı bir standart sapma daha yüksek olduğunda koroner arter hastalığı odds değerinin nasıl değiştiğini modelden okumak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: 1.1. adımdaki `model`: X_train üzerinde eğitilmiş, bir StandardScaler ve onu izleyen bir
LogisticRegression'dan oluşan işlem hattı. Sütun adları X.columns içindedir.
Görev: Lojistik regresyonun katsayılarını model.named_steps["logisticregression"].coef_[0] ile al,
X.columns ile eşleştir ve her sütun için standart sapma başına odds oranını, exp(katsayı), hesapla.
Hepsini yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: thalach sütununun odds oranı, iki ondalığa yuvarlanmış olarak. Sonucu `or_thalach` adlı bir
değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: oldpeak sütununun odds oranı 1'in üstünde olmalı.
```

**Beklenen sonuç:** `or_thalach` = 0,58

## Durak 2: Bir modeli dürüstçe sınamak

*[Ders sayfası: uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-2) · Python yolunda aynı sonuç: 3-6. bölümler*

76 hastalık tek bir test kümesi belirsiz bir tahmin verir ve bazı modeller olduklarından iyi görünür. Bu durakta test çapraz doğrulamayla tekrarlanır ve bir rastgele orman denenir. Ardından sanal kliniğin nadir bir sonucuna geçilir: 12 ay içinde ölüm ya da kalp yetersizliği nedeniyle hastaneye yatış.

### Adım 2.1: Beş katlı çapraz doğrulama

**Amaç.** 1. duraktaki lojistik regresyonu her seferinde hastaların başka bir beşte birinde olmak üzere beş kez sınamak ve ortalama AUC değerini almak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: Cleveland hastalarının `X` ve `y` değişkenleri: X; age, sex, trestbps, chol, thalach, exang,
oldpeak ve cp'nin kukla değişkenlerini, y ise disease sütununu (1 ya da 0) tutar.
Görev: make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)) işlem hattını
cross_val_score(pipeline, X, y, cv=StratifiedKFold(5, shuffle=True, random_state=RANDOM_STATE),
scoring="roc_auc") ile değerlendir. Beş AUC değerini ve ortalamalarını yazdır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Beş katın ortalama AUC değeri, üç ondalığa yuvarlanmış olarak. Sonucu `auc_cv` adlı bir
değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: Her biri 0,5 ile 1 arasında beş değer yazdırılmalı.
```

**Beklenen sonuç:** `auc_cv` = 0,871

### Adım 2.2: Bir rastgele orman

**Amaç.** Aynı hastalarda daha esnek bir model eğitmek ve test AUC değerini lojistik regresyonunkiyle karşılaştırmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: 1.1. adımdaki `X`, `y`, `X_train`, `X_test`, `y_train` ve `y_test`: X; age, sex, trestbps,
chol, thalach, exang, oldpeak ve cp'nin kukla değişkenlerini, y ise disease sütununu tutar; test
kümesinde 303 hastanın 76'sı bulunur.
Görev: RandomForestClassifier(n_estimators=300, random_state=RANDOM_STATE) modelini X_train ve
y_train üzerinde eğit ve X_test üzerindeki tahmin olasılıklarının AUC değerini roc_auc_score ile
hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Ormanın test AUC değeri, üç ondalığa yuvarlanmış olarak. Sonucu `auc_forest` adlı bir
değişkene kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: AUC 0,5 ile 1 arasında olmalı.
```

**Beklenen sonuç:** `auc_forest` = 0,904

### Adım 2.3: Nadir bir sonuç

**Amaç.** Hastaların yalnızca yaklaşık 100'de 3'ünde görülen 12 ay içindeki olay için bir model eğitmek ve sınıf ağırlıklarının modelin bulduklarını nasıl değiştirdiğini görmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: `registry`, sanal kliniğin 2000 sentetik hastasını ve izlemlerini içeren bir pandas
DataFrame'idir. Burada kullanılan sütunlar: age (yaş, yıl), egfr (tahmini glomerüler filtrasyon
hızı, mL/dk/1,73 m²), lvef (sol ventrikül ejeksiyon fraksiyonu, %), ntprobnp (N-terminal pro-B-tipi
natriüretik peptit, pg/mL), af (atriyal fibrilasyon, 1 evet), diabetes (1 evet), bmi (beden kitle
indeksi, kg/m²), sbp (sistolik kan basıncı, mm Hg) ve event_12m (hasta izlemin ilk 12 ayında öldüyse
ya da kalp yetersizliği nedeniyle hastaneye yattıysa 1, yoksa 0).
Görev: age, egfr, lvef, ntprobnp, af ve diabetes sütunlarından Xe tablosunu kur; ntprobnp yerine
doğal logaritmasını kullan; ye = registry["event_12m"] olsun. train_test_split(Xe, ye,
test_size=0.3, stratify=ye, random_state=RANDOM_STATE) ile ayır. make_pipeline(StandardScaler(),
LogisticRegression(class_weight="balanced", max_iter=1000)) modelini eğitim kümesinde eğit.
Olasılığı 0,5 ya da daha yüksek olan test hastasını pozitif say ve test kümesinde duyarlılığı TP /
(TP + FN) ile hesapla.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Duyarlılık, üç ondalığa yuvarlanmış olarak. Sonucu `se_balanced` adlı bir değişkene kaydet ve
kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir yorum
satırı ekle.
Test: Test kümesinde 600 hasta bulunmalı ve bunların 20'sinde olay olmalı. class_weight olmadan aynı
model 0,5 eşiğinde bunların hiçbirini bulamaz.
```

**Beklenen sonuç:** `se_balanced` = 0,65

## Durak 3: Alt gruplar, sağkalım ve denetlenecek bir model

*[Ders sayfası: uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-3) · Python yolunda aynı sonuç: 7-9. bölümler*

Kalp yetersizliği olan hastalar ejeksiyon fraksiyonundan daha fazlasıyla birbirinden ayrılır. Bu durakta yönteme cevap söylenmeden alt gruplar aranır ve izlem boyunca sağkalım tahmin edilir. Ardından bir YZ asistanının kusursuz sonuç bildirdiği bir model denetlenir.

### Adım 3.1: Üç küme

**Amaç.** k-ortalamalar yönteminin kalp yetersizliği olan hastalar arasında üç grup bulmasını sağlamak, ardından grupları gizli fenogruplarla karşılaştırmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: `hf`, sanal kliniğin kalp yetersizliği olan 407 hastasını (main_diagnosis HFrEF ya da HFpEF)
içeren bir pandas DataFrame'idir. `HF_FEATURES`, tablonun dokuz sütununu listeler: age, bmi, egfr,
lvef, ntprobnp, lavi (sol atriyum hacim indeksi, mL/m²), e_e_prime (E/e′ oranı), lv_mass_index (sol
ventrikül kütle indeksi, g/m²) ve tapse_mm (triküspit anüler düzlem sistolik hareketi, mm).
hf_phenogroup sütunu, kliniğin verileri üretirken kullandığı gizli fenogrubu tutar.
Görev: HF_FEATURES'taki dokuz sütunu, ntprobnp yerine doğal logaritmasını koyarak al; StandardScaler
ile standartlaştır; KMeans(n_clusters=3, n_init=10, random_state=RANDOM_STATE) modelini eğit ve
etiketlerini hf["hf_phenogroup"] ile adjusted_rand_score kullanarak karşılaştır.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Düzeltilmiş Rand indeksi, üç ondalığa yuvarlanmış olarak. Sonucu `ari` adlı bir değişkene
kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa
bir yorum satırı ekle.
Test: Üç küme toplam 407 hasta tutmalı. İndeksin 1 olması tam uyum, 0 olması rastlantısal uyum
demektir.
```

**Beklenen sonuç:** `ari` = 0,706

### Adım 3.2: 24. ayda Kaplan-Meier

**Amaç.** HFrEF hastalarının izlemin başlangıcından iki yıl sonra hangi oranda hayatta ve kalp yetersizliği nedeniyle yatış olmadan kaldığını tahmin etmek.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: `hf`, sanal kliniğin kalp yetersizliği olan 407 hastasını (main_diagnosis HFrEF ya da HFpEF)
içeren bir pandas DataFrame'idir. `HF_FEATURES`, tablonun dokuz sütununu listeler: age, bmi, egfr,
lvef, ntprobnp, lavi (sol atriyum hacim indeksi, mL/m²), e_e_prime (E/e′ oranı), lv_mass_index (sol
ventrikül kütle indeksi, g/m²) ve tapse_mm (triküspit anüler düzlem sistolik hareketi, mm).
hf_phenogroup sütunu, kliniğin verileri üretirken kullandığı gizli fenogrubu tutar. followup_months,
izlemin başlangıcından ilk olaya ya da izlemin sonuna kadar geçen süredir (ay). event, ölüm ya da
kalp yetersizliği nedeniyle yatış için 1, izlemden olaysız ayrılan (sansürlenen) hasta için 0'dır.
Görev: main_diagnosis değeri HFrEF olan hastalar için olaysız sağkalımın Kaplan-Meier tahminini
NumPy ile hesapla: 1'den başla ve en az bir olayın olduğu her zamanda 1 − d / n ile çarp; d o
zamandaki olay sayısı, n ise izlem süresi en az o zaman kadar olan hasta sayısıdır. 24. aydaki
tahmin, 24 ay ya da daha kısa olan son olay zamanından sonraki değerdir.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: 24. aydaki tahmin, üç ondalığa yuvarlanmış olarak. Sonucu `s24_hfref` adlı bir değişkene
kaydet ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa
bir yorum satırı ekle.
Test: Aynı hesap HFpEF hastaları için 24. ayda daha yüksek bir değer vermeli.
```

**Beklenen sonuç:** `s24_hfref` = 0,733

### Adım 3.3: Bir asistanın modelini denetlemek

**Amaç.** Bir asistan 12 ay içindeki olay için 1,000 AUC bildirdi. Aynı türden bir modelin dürüst bir değerlendirmede ne verdiğini bulmak.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt adıyla içe aktarılmıştır.
scikit-learn'den şunlar içe aktarılmıştır: train_test_split, StratifiedKFold, cross_val_score,
make_pipeline, StandardScaler, LogisticRegression, RandomForestClassifier, KMeans, roc_auc_score,
confusion_matrix ve adjusted_rand_score. RANDOM_STATE = 2026'dır.
Veri: `registry`, sanal kliniğin 2000 sentetik hastasını ve izlemlerini içeren bir pandas
DataFrame'idir. Burada kullanılan sütunlar: age (yaş, yıl), egfr (tahmini glomerüler filtrasyon
hızı, mL/dk/1,73 m²), lvef (sol ventrikül ejeksiyon fraksiyonu, %), ntprobnp (N-terminal pro-B-tipi
natriüretik peptit, pg/mL), af (atriyal fibrilasyon, 1 evet), diabetes (1 evet), bmi (beden kitle
indeksi, kg/m²), sbp (sistolik kan basıncı, mm Hg) ve event_12m (hasta izlemin ilk 12 ayında öldüyse
ya da kalp yetersizliği nedeniyle hastaneye yattıysa 1, yoksa 0). Asistanın modeli, yalnızca
izlemden sonra bilinen followup_months değişkenini de kullanmış ve AUC değerini eğitildiği
hastaların kendisinde ölçmüştür.
Görev: followup_months değişkenini çıkar. RandomForestClassifier(n_estimators=200,
min_samples_leaf=5, random_state=RANDOM_STATE) modelini age, egfr, lvef, ntprobnp, af, diabetes, bmi
ve sbp sütunlarında cross_val_score(..., cv=StratifiedKFold(5, shuffle=True,
random_state=RANDOM_STATE), scoring="roc_auc") ile değerlendir ve ortalama AUC değerini al.
Kısıtlar: Yalnızca burada adı geçen paketleri ve değişkenleri kullan. Dosya okuma, bir şey indirme
ve paket kurma.
Çıktı: Ortalama AUC, üç ondalığa yuvarlanmış olarak. Sonucu `auc_review` adlı bir değişkene kaydet
ve kısa bir etiketle yazdır. Yalnızca kodu, tek bir blok hâlinde ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: AUC, 1,000'in belirgin biçimde altında olmalı.
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
Aşağıdaki kod bir öngörü modeli kurup değerlendirmektedir. Dört şeyi denetle: karar anında
bilinemeyecek değişkenler, ayırmadan önce bütün hastalardan öğrenen bir adım, performansın ölçüldüğü
hastalar ve sonucun nadir olup olmadığı. Kısa bir listeyle cevap ver, ardından düzeltilmiş kodu ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Fenogrup sayısını seçmek

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `registry`, sanal kliniğin izlem verileri olan 2000 hastası;
`vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))` ile oluşturulur. Kalp
yetersizliği olan hastaların main_diagnosis değeri "HFrEF" ya da "HFpEF"tir. Sütunlar: age (yıl),
sex, bmi (kg/m²), diabetes ve af (0 ya da 1), egfr (mL/dk/1,73 m²), lvef (%), ntprobnp (pg/mL), lavi
(mL/m²), e_e_prime, lv_mass_index (g/m²), tapse_mm (mm), followup_months (ay) ve event (ölüm ya da
kalp yetersizliği nedeniyle yatış için 1, sansürlenmiş için 0).
Görev: Kalp yetersizliği olan hastaları al; age, bmi, egfr, lvef, ntprobnp'nin logaritması, lavi,
e_e_prime, lv_mass_index ve tapse_mm olmak üzere dokuz değişkeni standartlaştır ve k = 2-6 için
k-ortalamalar uydur (n_init=10, random_state=RANDOM_STATE). Her k için WCSS ve ortalama siluet
değerini bildir, k'yı seç ve seçimin klinik gerekçesini yaz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: k, WCSS ve siluet değerlerinden oluşan bir tablo; kalp yetersizliği hastalarının
DataFrame'ine eklenmiş bir cluster sütunu. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne
kısa bir yorum satırı ekle.
Test: Kalp yetersizliği olan hasta sayısı kümelemeden önce ve sonra aynı olmalı; her kümede en az 30
hasta bulunmalı.
```

### Adım 2: Fenogrupları tanımlamak ve adlandırmak

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 1. adımdaki kalp yetersizliği hastalarının DataFrame'i; cluster sütunu ve kaydın sütunlarıyla
birlikte.
Görev: Her kümenin büyüklüğünü; age, kadın cinsiyet, bmi, diabetes, af, egfr, lvef, ntprobnp
(ortanca), lavi, e_e_prime, lv_mass_index ve tapse_mm değerlerinin ortalamasını ya da yüzdesini ve
HFrEF oranını gösteren bir tablo oluştur. Her küme için kısa bir klinik ad öner.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Her kümenin bir sütun olduğu bir pandas DataFrame'i. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: Tablodaki büyüklüklerin toplamı kalp yetersizliği olan hasta sayısına eşit olmalı.
```

### Adım 3: Fenogruba göre prognoz

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 1. adımdaki DataFrame (cluster, main_diagnosis, followup_months ve event sütunlarıyla) ve
Jupyter defterinin 8. bölümündeki `kaplan_meier(time, event)` ile `logrank(time, event, group)`
fonksiyonları.
Görev: Kümelerin Kaplan-Meier eğrilerini ve ikinci bir panelde HFrEF ile HFpEF eğrilerini çiz. Her
grup için S(24) değerini ve her gruplamanın log-rank testini bildir.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: İki panelli bir şekil, bir S(24) tablosu ve iki log-rank testi. Yalnızca kodu, tek bir blok
olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Eğriler 1'den başlamalı ve hiçbir zaman yükselmemeli; HFrEF ile HFpEF'nin log-rank testi 8.
bölümdeki p değerini vermeli.
```

### Adım 4: Gizli gerçekle karşılaştırmak

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 1. adımdaki DataFrame (cluster ve dersin her hastaya gizlediği fenogrup olan hf_phenogroup
sütunlarıyla).
Görev: Kümeleri hf_phenogroup ile çapraz tabloya dök ve düzeltilmiş Rand indeksini hesapla.
Kümelemenin, tek başına ejeksiyon fraksiyonunun kaçırdığı neyi bulduğunu üç cümleyle yaz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Çapraz tablo, düzeltilmiş Rand indeksi ve üç cümle. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: Düzeltilmiş Rand indeksi −1 ile 1 arasında olmalı; k = 3 için 0,5'in belirgin biçimde üstünde
olmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
