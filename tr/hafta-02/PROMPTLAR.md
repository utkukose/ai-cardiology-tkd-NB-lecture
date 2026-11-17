# Prompt kütüphanesi, 2. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[2. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-02/PROMPTS.md)

Bu kütüphanede 2. haftada kullanılan her prompt (istem), eğitimin prompt kartıyla yazılmış olarak yer almaktadır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir. Asistanın yazdığı kod, Jupyter defterinde aynı adı taşıyan alıştırmanın ya da prompt görevinin altına yapıştırılır ve orada çalıştırılır. Alıştırmalarda `teach.check` satırı sonucun doğru olup olmadığını hemen gösterir. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Prompt döngüsü](#prompt-döngüsü)
2. [Alıştırmaların promptları](#alıştırmaların-promptları)
3. [Bölümlerin prompt görevleri](#bölümlerin-prompt-görevleri)
4. [Kodu açıklatmak, onarmak ve denetlemek için kalıplar](#kodu-açıklatmak-onarmak-ve-denetlemek-için-kalıplar)
5. [Haftalık projenin prompt yolu](#haftalık-projenin-prompt-yolu)

## Prompt döngüsü

| Adım | Ne yapılır? |
|---|---|
| 1. Tarif et | Alıştırmanın prompt kartını kopyalayın ya da kartı yedi alanıyla kendiniz yazın: rol, bağlam, veri, görev, kısıtlar, çıktı ve test. |
| 2. Gönder | Promptu bir YZ asistanına gönderin. |
| 3. Çalıştır | Asistanın kodunu alıştırmanın altındaki boş hücreye yapıştırın ve çalıştırın. |
| 4. Denetle | `teach.check` satırının yazdığı sonuca (*doğru* ya da *henüz değil*) ve promptun Test satırına bakın. Sonuç *henüz değil* ise kodu onarım promptuyla asistana geri gönderin. |
| 5. Açıkla | Asistandan kodu satır satır açıklamasını isteyin, ardından kodu bir kez de kendi sözcüklerinizle açıklayın. |
| 6. Kaydet | Aracı, promptu, neyin denetlendiğini ve neyin değiştirildiğini YZ kullanım günlüğüne yazın. |

## Alıştırmaların promptları

Jupyter defterindeki her alıştırmanın hemen altında, katlanmış bir hücrede o alıştırmanın prompt yolu bulunur; aşağıdaki promptlar bunlarla aynıdır. Asistanın kodunu alıştırmanın boş cevap hücresine yapıştırın ve çalıştırın.

### Alıştırma 2.1: Tablodaki eksik hücreler

*Jupyter defteri, "Python adımı 2: Veriyi modele hazırlamak"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `heart` adlı pandas DataFrame'i UCI Heart Disease veri setinin Cleveland verisini tutar: 303
hasta, her satırda bir hasta. disease sütunu 0 ya da 1'dir: Koroner arter hastalığı (KAH) varsa 1,
yoksa 0. Eksik değerler NaN olarak durur.
Görev: `heart` tablosundaki bütün satır ve sütunlarda eksik olan hücrelerin toplamını say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Eksik hücre sayısı, tamsayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma 2.1", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Yöntemi önce `pd.DataFrame({"a": [1, None], "b": [None, 4]})` tablosunda dene; sonuç 2 olmalı.
Ardından eksik değeri olan her sütunun eksik sayısını yazdır; listede yalnızca ca ve thal sütunları
görünmeli.
```

### Alıştırma 2.2: Test kümesinin büyüklüğü

*Jupyter defteri, "Python adımı 2: Veriyi modele hazırlamak"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X`, 303 satırlı ve 10 sayısal sütunlu bir DataFrame; `y` ise 0 ya da 1 olan 303 değerli bir
Series.
Görev: `X` ve `y` verilerini
`train_test_split(X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)` ile ayır ve test
kümesindeki hastaları say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Test kümesindeki hasta sayısı. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma 2.2", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: İki kümenin büyüklüğünü yazdır; toplamları 303 olmalı.
```

### Alıştırma 2.3: İlk işlem hattının doğruluğu

*Jupyter defteri, "Python adımı 2: Veriyi modele hazırlamak"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X_train`, `X_test`, `y_train` ve `y_test`,
`train_test_split(X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)` çağrısından gelir.
`X` şu sütunları içerir: age (yıl), sex (1 erkek, 0 kadın), trestbps (istirahat sistolik kan
basıncı, mmHg), chol (serum kolesterolü, mg/dL), thalach (en yüksek kalp hızı, bpm), exang
(egzersizle angina, 0 ya da 1), oldpeak (ST çökmesi, mm) ve göğüs ağrısı tipinin üç kukla sütunu
cp_2.0, cp_3.0 ve cp_4.0. `y`, disease sütunudur.
Görev: `make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))` kur, eğitim kümesinde
uydur ve test kümesindeki doğruluğunu `score` ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Test kümesindeki doğruluk, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir
değişkende sakla ve kodu `teach.check("Alıştırma 2.3", answer)` satırıyla bitir. Yalnızca kodu, tek
bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Eğitim kümesindeki doğruluğu da yazdır; benzer büyüklükte olmalı ve 1,0 olmamalı.
```

### Alıştırma A: Tipik angina ile vakanın olasılığı

*Jupyter defteri, 1. bölüm, "İlk model: Koroner arter hastalığı için lojistik regresyon"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `model`, KAH için uydurulmuş bir StandardScaler ve LogisticRegression işlem hattı; `case` ise
`X` ile aynı sütunlara sahip tek satırlık bir DataFrame: age 57 yıl, sex 1, trestbps 119 mmHg, chol
230 mg/dL, thalach 132 bpm, exang 1, oldpeak 1,6 mm, cp_2.0 1, cp_3.0 0 ve cp_4.0 0.
Görev: `case` tablosunu kopyala, cp_2.0 değerini 0 yaparak üç göğüs ağrısı sütununu da 0'a getir
(tipik angina) ve KAH olasılığını `model.predict_proba` ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Olasılık, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma A", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Değiştirilmemiş `case` için olasılığı da yazdır; iki olasılık farklı olmalı ve ikisi de 0 ile
1 arasında kalmalı.
```

### Alıştırma B: Test kümesinde AUC

*Jupyter defteri, 2. bölüm, "Bir modeli ölçmek: Karışıklık matrisi ve ROC eğrisi"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `model`, KAH için uydurulmuş bir işlem hattı; test kümesi `X_test`, `y_test` (76 hasta;
`y_test` 0 ya da 1'dir, KAH için 1).
Görev: `model` işlem hattının test kümesindeki olasılıklarının alıcı işletim karakteristiği eğrisi
altındaki alanını (AUC) `roc_auc_score` ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: AUC, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma B", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 1 eksi olasılıkların AUC değerini de hesapla; iki değerin toplamı 1 olmalı.
```

### Alıştırma C: 0,5 eşiğinde duyarlılık

*Jupyter defteri, 2. bölüm, "Bir modeli ölçmek: Karışıklık matrisi ve ROC eğrisi"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `model`, KAH için uydurulmuş bir işlem hattı; test kümesi `X_test`, `y_test` (76 hasta,
35'inde KAH var; `y_test` 0 ya da 1'dir).
Görev: KAH olasılığı 0,5 ya da üstündeyse hastayı pozitif say; TP, FP, TN ve FN sayılarını
`confusion_matrix(...).ravel()` ile bul ve duyarlılığı TP / (TP + FN) ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Duyarlılık, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma C", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: TP ve FN değerlerini yazdır; toplamları, test kümesinde KAH olan hasta sayısı olan 35 olmalı.
```

### Alıştırma D: Çapraz doğrulanmış AUC

*Jupyter defteri, 3. bölüm, "Çapraz doğrulama ve veri sızıntısı"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X` ve `y`, 303 Cleveland hastası (`y` 0 ya da 1'dir, KAH için 1); `pipe`, StandardScaler ve
LogisticRegression(max_iter=1000) adımlarından oluşan uydurulmamış bir işlem hattı.
Görev: `StratifiedKFold(5, shuffle=True, random_state=RANDOM_STATE)` ve
`cross_val_score(..., scoring="roc_auc")` ile beş katlı çapraz doğrulama yap ve beş AUC değerinin
ortalamasını al.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Ortalama AUC, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve
kodu `teach.check("Alıştırma D", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: Beş AUC değerini yazdır; her biri 0,5 ile 1 arasında olmalı.
```

### Alıştırma E: Kök düğümün Gini safsızlığı

*Jupyter defteri, 4. bölüm, "Karar ağaçları ve rastgele ormanlar"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `y_train`, 227 eğitim hastasının 0 ya da 1 olan sonucu.
Görev: p0 = n0 / (n0 + n1) ve p1 = n1 / (n0 + n1) olmak üzere 1 - (p0² + p1²) döndüren bir
`gini(n0, n1)` fonksiyonu yaz ve `y_train` içindeki 0 ve 1 sayılarına uygula.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Gini safsızlığı, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve
kodu `teach.check("Alıştırma E", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: assert ifadeleriyle denetle: gini(50, 50) 0,5, gini(100, 0) ise 0,0 olmalı.
```

### Alıştırma F: Kayıtta sigaranın katsayısı

*Jupyter defteri, 5. bölüm, "Risk polikliniği: Kayıttaki koroner arter hastalığı"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `registry` adlı pandas DataFrame'i sanal kliniğin 2000 sentetik hastasını, her satırda bir
hasta olacak biçimde tutar; `vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))` ile
oluşturulmuştur. Sütunları arasında age (yıl), sex ("M" ya da "F"), smoker, diabetes, hypertension,
family_history ve cad (0 ya da 1), ldl ve hdl (mg/dL), egfr (mL/dk/1,73 m²), lvef (%), ntprobnp
(pg/mL), af (0 ya da 1), bmi (kg/m²), sbp (mmHg), main_diagnosis, followup_months (ay) ve event
(ölüm ya da kalp yetersizliği nedeniyle yatış için 1, sansürlenmiş için 0) bulunur.
Görev: Değişkenleri `vclinic.TRUE_EFFECTS` ile aynı biçimde kodla: age_per_10y = (age - 60) / 10,
sex "M" ise male = 1, smoker, diabetes, hypertension, ldl_per_40 = (ldl - 130) / 40, hdl_per_15 =
(hdl - 50) / 15 ve family_history. cad sütununa `LogisticRegression(C=np.inf, max_iter=2000)` uydur
ve smoker katsayısını oku.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: smoker katsayısı, iki ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla
ve kodu `teach.check("Alıştırma F", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak
ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Öğrenilen bütün katsayıları `vclinic.TRUE_EFFECTS` değerlerinin yanına yazdır; her biri gerçek
değerinin yaklaşık 0,2 yakınında olmalı.
```

### Alıştırma G: Prevalanstan PPV

*Jupyter defteri, 6. bölüm, "Nadir sonuçlar: Dengesiz veri"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: Duyarlılığı 0,85 ve özgüllüğü 0,90 olan bir tarama modeli; prevalansın 0,05 (%5) olduğu bir
toplulukta kullanılmaktadır.
Görev: Bayes teoremiyle PPV = se × prev / (se × prev + (1 - sp) × (1 - prev)) döndüren bir
`ppv(se, sp, prev)` fonksiyonu yaz ve uygula.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: PPV, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma G", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: assert ifadesiyle denetle: ppv(0.85, 0.85, 0.5) değeri 0,85 olmalı.
```

### Alıştırma H: Üç kümenin siluet değeri

*Jupyter defteri, 7. bölüm, "Alt grupları bulmak: Kalp yetersizliği olan hastalarda k-ortalamalar"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X_hf`, kalp yetersizliği olan her hasta için bir satırı olan bir NumPy dizisi; yaş (yıl),
lvef (%) ve tapse_mm (mm) gibi dokuz sütunu z skoruna standartlaştırılmıştır.
Görev: `X_hf` dizisine `KMeans(n_clusters=3, n_init=10, random_state=RANDOM_STATE)` uydur ve
etiketlerinin ortalama siluet değerini `silhouette_score` ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Ortalama siluet değeri, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende
sakla ve kodu `teach.check("Alıştırma H", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok
olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Her kümedeki hasta sayısını yazdır; üç sayının toplamı `X_hf` dizisinin satır sayısı olan
407'ye eşit olmalı.
```

### Alıştırma I: 24. ayda Kaplan-Meier

*Jupyter defteri, 8. bölüm, "Sağkalım analizi: Kaplan-Meier ve log-rank testi"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `hf`, kalp yetersizliği olan hastaların DataFrame'i; main_diagnosis ("HFrEF" ya da "HFpEF"),
followup_months (ay) ve event (ölüm ya da yatış için 1, sansürlenmiş için 0) sütunlarını içerir.
Görev: Basamakların zamanlarını ve her basamaktan sonraki sağkalımı döndüren bir
`kaplan_meier(time, event)` fonksiyonu yaz; S(t), t'ye kadarki olay zamanları üzerinden (1 - d_i /
n_i) çarpımıdır. Fonksiyonu HFrEF hastalarına uygula ve 24. aydaki S değerini oku.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: S(24), üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma I", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 2, 3, 3, 5, 6, 8, 9, 11, 12, 12 aylık zamanlar ve 1, 1, 0, 1, 0, 1, 0, 1, 0, 0 olayları için
11. aydan sonraki sağkalım, dört ondalığa yuvarlandığında 0,3657 olmalı.
```

### Alıştırma J: Asistanın modelinin düzeltilmiş hâli

*Jupyter defteri, 9. bölüm, "YZ ile eşli kodlama, bölüm 2: Bir asistanın kurduğu modeli denetlemek"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `registry` adlı pandas DataFrame'i sanal kliniğin 2000 sentetik hastasını, her satırda bir
hasta olacak biçimde tutar; `vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))` ile
oluşturulmuştur. Sütunları arasında age (yıl), sex ("M" ya da "F"), smoker, diabetes, hypertension,
family_history ve cad (0 ya da 1), ldl ve hdl (mg/dL), egfr (mL/dk/1,73 m²), lvef (%), ntprobnp
(pg/mL), af (0 ya da 1), bmi (kg/m²), sbp (mmHg), main_diagnosis, followup_months (ay) ve event
(ölüm ya da kalp yetersizliği nedeniyle yatış için 1, sansürlenmiş için 0) bulunur. event_12m sütunu
12 ay içinde olay varsa 1'dir. `features` listesi age, egfr, lvef, ntprobnp, af, diabetes, bmi, sbp
ve followup_months sütunlarını tutar.
Görev: followup_months değişkenini çıkar, çünkü karar anında bilinmez. Ardından
`RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=RANDOM_STATE)` modelinin
event_12m için ortalama AUC değerini beş katlı
`StratifiedKFold(5, shuffle=True, random_state=RANDOM_STATE)` ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Ortalama çapraz doğrulanmış AUC, üç ondalığa yuvarlanmış olarak. Sonucu `answer` adlı bir
değişkende sakla ve kodu `teach.check("Alıştırma J", answer)` satırıyla bitir. Yalnızca kodu, tek
bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Aynı ormanın bütün hastalarda uydurulup yine onlarda puanlanan AUC değerini de yazdır; bu
değer çapraz doğrulanmış değerden belirgin biçimde yüksek, 0,95'in üstünde olmalı.
```

## Bölümlerin prompt görevleri

Jupyter defterindeki her numaralı bölüm bir prompt göreviyle biter. Prompt görevinde bir prompt vardır, ancak hazır kod ve `teach.check` satırı yoktur. Sonucun doğru olup olmadığını her promptun altındaki beklenen sonuç gösterir.

### 1. bölüm: Odds oranlarının orman grafiği

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `model`, KAH için uydurulmuş bir StandardScaler ve LogisticRegression işlem hattı; `X`,
sütunları modelin değişkenleri olan tablo.
Görev: Her değişkenin standart sapma başına odds oranını logaritmik yatay eksende bir nokta olarak
çiz; 1'de dikey bir çizgi koy ve değişken adlarını dikey eksene yaz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Odds oranlarını da yazdır; thalach 1'in altında, oldpeak 1'in üstünde olmalı.
```

**Beklenen sonuç.** SS başına odds oranı thalach için yaklaşık 0,58, oldpeak için yaklaşık 2,07'dir; sex ve cp_4.0 2'nin üstündedir.

### 2. bölüm: Yan yana üç eşik

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `p_test`, 76 test hastasının KAH olasılıkları; `y_test`, sonuçları.
Görev: 0,3, 0,5 ve 0,7 eşiklerinin her biri için bir satırı ve Se, Sp, PPV ve NPV sütunları olan bir
tablo oluştur.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Üç ondalığa yuvarlanmış bir pandas DataFrame'i. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 0,5 eşiğinde tablo, 2. bölümdeki gibi Se 0,800 ve Sp 0,902 göstermeli.
```

**Beklenen sonuç.** 0,3 ile 0,7 eşikleri arasında duyarlılık 0,857'den 0,571'e düşer, özgüllük 0,805'ten 0,951'e yükselir.

### 3. bölüm: Lojistik regresyon mu, rastgele orman mı?

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X` ve `y`, 303 Cleveland hastası; katmanlar
`cv = StratifiedKFold(5, shuffle=True, random_state=RANDOM_STATE)`.
Görev: StandardScaler ve LogisticRegression(max_iter=1000) işlem hattının ortalama çapraz
doğrulanmış AUC değerini aynı katmanlarda
`RandomForestClassifier(n_estimators=300, random_state=RANDOM_STATE)` ile karşılaştır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: İki ortalama ve standart sapmaları. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne
kısa bir yorum satırı ekle.
Test: Lojistik regresyon, Alıştırma D'deki ortalama AUC değerini vermeli.
```

**Beklenen sonuç.** İki model de yaklaşık 0,87'lik bir ortalama AUC'ye ulaşır; bu 303 hastada rastgele orman daha iyi değildir.

### 4. bölüm: Bir ağaç ne kadar derin olmalı?

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `X_train`, `X_test`, `y_train` ve `y_test`,
`train_test_split(X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)` çağrısından gelir.
`X` şu sütunları içerir: age (yıl), sex (1 erkek, 0 kadın), trestbps (istirahat sistolik kan
basıncı, mmHg), chol (serum kolesterolü, mg/dL), thalach (en yüksek kalp hızı, bpm), exang
(egzersizle angina, 0 ya da 1), oldpeak (ST çökmesi, mm) ve göğüs ağrısı tipinin üç kukla sütunu
cp_2.0, cp_3.0 ve cp_4.0. `y`, disease sütunudur.
Görev: 1'den 8'e kadar her d için eğitim kümesinde
`DecisionTreeClassifier(max_depth=d, random_state=RANDOM_STATE)` uydur ve test AUC değerini
derinliğe karşı çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve sekiz AUC değeri. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa
bir yorum satırı ekle.
Test: 3 derinliği, 4. bölümdeki ağacın test AUC değerini vermeli.
```

**Beklenen sonuç.** AUC yaklaşık 0,81 ile 3 derinliğinde en yüksek değerine ulaşır ve daha derin ağaçlarda 0,75'in altına düşer: aşırı öğrenmenin bir görüntüsü.

### 5. bölüm: Vakanın riski yaşlara göre

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `registry` adlı pandas DataFrame'i sanal kliniğin 2000 sentetik hastasını, her satırda bir
hasta olacak biçimde tutar; `vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))` ile
oluşturulmuştur. Sütunları arasında age (yıl), sex ("M" ya da "F"), smoker, diabetes, hypertension,
family_history ve cad (0 ya da 1), ldl ve hdl (mg/dL), egfr (mL/dk/1,73 m²), lvef (%), ntprobnp
(pg/mL), af (0 ya da 1), bmi (kg/m²), sbp (mmHg), main_diagnosis, followup_months (ay) ve event
(ölüm ya da kalp yetersizliği nedeniyle yatış için 1, sansürlenmiş için 0) bulunur. `cad_model`,
`risk_table(registry)` tablosuna uydurulmuş bir LogisticRegression modelidir; `risk_table(df)`
fonksiyonu değişkenleri `vclinic.TRUE_EFFECTS` ile aynı biçimde kodlar.
Görev: VC-0246 numaralı hastanın satırını al, yalnızca yaşı 40'tan 80'e birer yıl artırarak değiştir
ve `cad_model` modelinin KAH olasılığını yaşa karşı çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Eğri, 57 yaşta 5. bölümün VC-0246 için yazdırdığı olasılıktan geçmeli.
```

**Beklenen sonuç.** Eğri 40 yaşta yaklaşık 0,55'ten 80 yaşta yaklaşık 0,9'a yükselir ve 57 yaşta yaklaşık 0,76'dan geçer.

### 6. bölüm: İki kesinlik-duyarlılık eğrisi

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `Xe_train`, `Xe_test`, `ye_train` ve `ye_test`, 12 ay içindeki olayın eğitim ve test kümeleri
(prevalans yaklaşık 0,034); sütunlar age, egfr, lvef, ntprobnp'nin logaritması, af ve diabetes.
Görev: StandardScaler ve LogisticRegression(max_iter=1000) işlem hattını bir kez sınıf ağırlığı
olmadan, bir kez `class_weight="balanced"` ile uydur ve iki kesinlik-duyarlılık eğrisini prevalansta
yatay bir çizgiyle birlikte tek bir şekilde çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve iki ortalama kesinlik değeri. Yalnızca kodu, tek bir blok olarak ver; her adımın
üstüne kısa bir yorum satırı ekle.
Test: İki ortalama kesinlik değeri 6. bölümdeki tablonun AP sütunuyla aynı olmalı.
```

**Beklenen sonuç.** İki eğri neredeyse üst üste biner ve ortalama kesinlik yaklaşık 0,10'dur: Sınıf ağırlıkları hastaların sıralamasını değil, eşiği kaydırır.

### 7. bölüm: Kümelerin ısı haritası

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `hf`, kalp yetersizliği olan hastaların cluster sütunu (0, 1 ya da 2) içeren DataFrame'i;
`HF_FEATURES`, dokuz kümeleme değişkeninin listesi.
Görev: Her kümede her değişkenin ortalamasını hesapla, her değişkeni üç küme boyunca z skoruna çevir
ve tabloyu hücrelere değerleri yazılmış bir ısı haritası olarak çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı
ekle.
Test: Ortalama lvef değeri en düşük olan küme, ortalama ntprobnp değeri en yüksek olan küme de
olmalı.
```

**Beklenen sonuç.** Kümelerden birinde ejeksiyon fraksiyonu düşük ve NT-proBNP en yüksektir (HFrEF); biri en yaşlı, sol atriyumu büyük ve TAPSE değeri düşük olandır; biri de en genç, BKİ ve eGFR değeri en yüksek olandır.

### 8. bölüm: Risk altındaki hasta sayıları

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: `hf`, kalp yetersizliği olan hastaların cluster, followup_months ve event sütunlarını içeren
DataFrame'i.
Görev: Bir makalede Kaplan-Meier şeklinin altına yazılan biçimde, her küme için 0, 12, 24, 36 ve 48.
aylarda risk altındaki, yani hâlâ izlenen ve olay yaşamamış hasta sayılarının tablosunu oluştur.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Her kümenin bir satır olduğu bir pandas DataFrame'i. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: 0. ayda sayılar kümelerin büyüklüklerine eşit olmalı.
```

**Beklenen sonuç.** Sayılar her kümede azalır; en hızlı azalma en yaşlı hastaların kümesindedir.

### 9. bölüm: Asistanın modelinin denetimi

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot plt, SciPy'nin stats modülü de
stats adıyla içe aktarılmıştır; scikit-learn kuruludur. vclinic ders paketi ve teach modülü
kullanılabilir; RANDOM_STATE = 2026'dır.
Veri: 9. bölümdeki YZ asistanı kodu, prompta metin olarak yapıştırılmış hâlde.
Görev: Kodu dört soruyla denetle: Hangi değişkenler karar anında bilinemez? Ayırmadan önce bütün
hastalardan öğrenen bir adım var mı? AUC hangi hastalarda ölçülmektedir? Sonuç nadir mi? Ardından
düzeltilmiş kodu ver.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Sorunların kısa bir listesi ve düzeltilmiş kod. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Düzeltilmiş kod, eğitim hastalarındaki AUC değerini değil, çapraz doğrulanmış AUC değerini
bildirmeli.
```

**Beklenen sonuç.** Denetim, izlem süresini gelecekten gelen bir bilgi olarak ve AUC'nin eğitim hastalarında ölçülmesini sorun olarak adlandırır; düzeltilmiş AUC 1,0 yerine yaklaşık 0,85'tir.

## Kodu açıklatmak, onarmak ve denetlemek için kalıplar

Bu dört kalıp her alıştırmanın koduyla kullanılabilir. Köşeli parantez içindeki yerler, prompt gönderilmeden önce doldurulur.

### Kodu açıklatmak

```text
Aşağıdaki Python kodunu, Python'a yeni başlayan bir hekim için satır satır açıkla. Ardından kodun
hata mesajı vermeden yanlış sonuç döndürebileceği iki durumu belirt.

[kodu buraya yapıştırın]
```

### Denetimden geçmeyen kodu onarmak

```text
Aşağıdaki kod şu görev için yazıldı: [promptun Görev satırını yapıştırın]. Kod çalışıyor, ancak
teach.check satırı "henüz değil" yazıyor. Hatayı bul, iki cümleyle açıkla ve düzeltilmiş kodu ver.
Değişken adlarını ve teach.check satırını koru.

[kodu buraya yapıştırın]
```

### Bir hata mesajını anlamak

```text
Aşağıdaki hücre bir Jupyter defterinde çalıştırıldığında altta verilen hata mesajını veriyor.
Hatanın nedenini sade bir dille açıkla ve düzeltilmiş kodu ver.

[kodu buraya yapıştırın]

[hata mesajını buraya yapıştırın]
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
