# Prompt kütüphanesi, 1. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[1. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-01/PROMPTS.md)

Bu kütüphanede 1. haftada kullanılan her prompt (istem), eğitimin prompt kartıyla yazılmış olarak yer almaktadır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir. Asistanın yazdığı kod, Jupyter defterinde aynı adı taşıyan alıştırmanın ya da prompt görevinin altına yapıştırılır ve orada çalıştırılır. Alıştırmalarda `teach.check` satırı sonucun doğru olup olmadığını hemen gösterir. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Prompt döngüsü](#prompt-döngüsü)
2. [Alıştırmaların promptları](#alıştırmaların-promptları)
3. [Bölümlerin prompt görevleri](#bölümlerin-prompt-görevleri)
4. [Kodu açıklatmak, onarmak ve sınamak için kalıplar](#kodu-açıklatmak-onarmak-ve-sınamak-için-kalıplar)
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

### Alıştırma 1.1: Kalp hızından RR aralığı

*Jupyter defteri, "Python adımı 1: Değerler, listeler, sözlükler, koşullar, döngüler ve fonksiyonlar"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: Dakikada 72 atımlık (bpm) bir kalp hızı.
Görev: RR aralığını saniye cinsinden RR = 60 / HR formülüyle hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: RR aralığını üç ondalığa yuvarla. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma 1.1", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 60 bpm için RR aralığını da yazdır; tam olarak 1,0 s olmalı.
```

### Alıştırma 1.2: Fridericia düzeltmesi için bir fonksiyon

*Jupyter defteri, "Python adımı 1: Değerler, listeler, sözlükler, koşullar, döngüler ve fonksiyonlar"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: Milisaniye cinsinden QT aralığı ve saniye cinsinden RR aralığı. Haftanın vakasında kalp hızı
85 bpm iken QT 391 ms'dir; dolayısıyla RR = 60 / 85 s.
Görev: Fridericia formülüyle (QTc = QT / RR^(1/3)) düzeltilmiş QT aralığını döndüren bir
`qtc_fridericia(qt_ms, rr_s)` fonksiyonu yaz ve fonksiyonu haftanın vakasına uygula.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Vakanın QTc değerini bir ondalığa yuvarla. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma 1.2", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: assert ifadeleriyle denetle: `qtc_fridericia(400, 1.0)` 400,0, `qtc_fridericia(400, 0.729)`
ise yuvarlandıktan sonra 444,4 döndürmeli (0,729 = 0,9³).
```

### Alıştırma 1.3: Döngüyle saymak

*Jupyter defteri, "Python adımı 1: Değerler, listeler, sözlükler, koşullar, döngüler ve fonksiyonlar"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `clinic` adlı liste her hastayı bir sözlük olarak tutar. Sözlüklerde "id", "hr" (bpm cinsinden
kalp hızı) ve "qt" (ms cinsinden QT aralığı) anahtarları bulunur; örneğin {"id": "VC-0317", "hr":
85, "qt": 391}.
Görev: Kalp hızı 80 bpm'nin üstünde olan hastaları say.
Kısıtlar: pandas kullanmadan bir for döngüsü ve bir if ifadesi kullan. Yalnızca bu paketleri ve
burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir paket kurma.
Çıktı: Hasta sayısı. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma 1.3", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Kalp hızları 72, 85 ve 81 olan bir listede aynı döngü 2 hasta saymalıdır.
```

### Alıştırma A: Hastalığı olanların ortalama yaşı

*Jupyter defteri, 1. bölüm, "Hasta kaydı: pandas ile UCI Heart Disease verisi"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `heart` adlı pandas DataFrame'i, UCI Heart Disease veri setinin Cleveland verilerini her
satırda bir hasta olacak biçimde tutar. age sütunu yaşı yıl olarak verir; disease sütunu koroner
arter hastalığı varsa 1, yoksa 0'dır.
Görev: disease değeri 1 olan hastaların ortalama yaşını hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Ortalama yaşı bir ondalığa yuvarla. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma A", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Her hastalık grubundaki hasta sayısını yazdır; iki sayının toplamı 303 olmalı.
```

### Alıştırma B: Kadınların yüzdesi

*Jupyter defteri, 1. bölüm, "Hasta kaydı: pandas ile UCI Heart Disease verisi"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: sex sütunu erkekler için 1, kadınlar için 0 olarak kodlanmış `heart` DataFrame'i.
Görev: Kadınların bütün hastalar içindeki yüzdesini hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Yüzdeyi bir ondalığa yuvarla. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma B", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Erkeklerin yüzdesini de aynı biçimde hesapla ve iki yüzdenin toplamını yazdır; toplam 100
olmalı.
```

### Alıştırma C: Sanal klinikte bir tanıyı saymak

*Jupyter defteri, 2. bölüm, "Sanal klinik açılıyor"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `clinic` adlı bir pandas DataFrame'i sanal kliniğin 500 sentetik hastasını tutar.
main_diagnosis sütunu "none", "CCS", "HFpEF", "HFrEF" ve "ACS" etiketlerinden birini içerir.
Görev: Ana tanısı tam olarak "HFrEF" olan hastaları say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Hasta sayısı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma C", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Bütün tanıların sayılarını value_counts() ile yazdır; toplamları 500 olmalı.
```

### Alıştırma D: Büyük bir karedeki örnek sayısı

*Jupyter defteri, 3. bölüm, "Veri olarak EKG: Örnekler, örnekleme frekansı ve birimler"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 500 Hz'de örneklenmiş bir EKG. EKG kâğıdında büyük bir kare 0,2 s'ye karşılık gelir.
Görev: Büyük bir karenin kaç örnek içerdiğini N = süre × örnekleme frekansı ile hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Örnek sayısı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma D", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Aynı örnekleme frekansında 0,04 s'lik küçük bir kare 20 örnek içermelidir.
```

### Alıştırma E: aVL derivasyonunun voltajı

*Jupyter defteri, 4. bölüm, "Tek kalp vektöründen on iki derivasyon"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `vclinic.LEAD_VECTORS`, her derivasyon adını ("I", "II", "III", "aVR", "aVL", "aVF" ve
"V1"-"V6") üç sayılık bir NumPy dizisine eşleyen bir sözlüktür. x ekseni sola, y ekseni ayaklara, z
ekseni öne doğrudur. Bir derivasyonun milivolt cinsinden voltajı, derivasyon vektörünün kalp vektörü
H ile nokta çarpımıdır.
Görev: H = (0,6; 0,8; -0,2) mV için aVL derivasyonunun voltajını hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Voltajı üç ondalığa yuvarla ve float türüne çevir. Sonucu `answer` adlı bir değişkende sakla
ve kodu `teach.check("Alıştırma E", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak
ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: D1 derivasyonunun (sözlükte "I") vektörü (1; 0; 0) olduğundan aynı kod D1 için 0,6 mV
vermelidir.
```

### Alıştırma F: Kayıttan Fridericia QTc'si

*Jupyter defteri, 5. bölüm, "PR, QRS ve QT ölçümü"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: Kalp hızı 98 bpm iken 343 ms'lik bir QT aralığı.
Görev: QTc'yi Fridericia formülüyle (QTc = QT / RR^(1/3)) hesapla; saniye cinsinden RR aralığını RR
= 60 / HR ile bul.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: QTc'yi bir ondalığa yuvarla. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma F", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 60 bpm'de RR aralığı 1 s olduğundan QTc, QT'ye eşit olmalıdır.
```

### Alıştırma G: VC-0188 numaralı hastanın PR aralığı

*Jupyter defteri, 5. bölüm, "PR, QRS ve QT ölçümü"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: Defterde `measure_ecg(leads, fs)` adlı bir fonksiyon tanımlıdır. Fonksiyon, on iki derivasyonu
milivolt cinsinden I, II, III, aVR, aVL, aVF, V1-V6 sırasıyla tutan (örnek sayısı, 12) boyutlu bir
NumPy dizisini ve Hz cinsinden örnekleme frekansını alır. "hr_bpm", "pr_ms", "qrs_ms", "qt_ms",
"qtc_bazett_ms" ve "qtc_fridericia_ms" anahtarlarını içeren bir sözlük döndürür.
`vclinic.patient_ecg(clinic, patient_id)` bir EKG nesnesi döndürür; bu nesneye `e` diyelim.
`e.leads` on iki derivasyonu tutan bir pandas DataFrame'idir, `e.fs` ise Hz cinsinden örnekleme
frekansıdır.
Görev: "VC-0188" numaralı hastanın PR aralığını ölç ve birinci derece atriyoventriküler blok
tanımını, yani 200 ms'nin üstünde bir PR aralığını, karşılayıp karşılamadığına karar ver.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: PR aralığını en yakın milisaniyeye yuvarla ve kararı yazdır. Sonucu `answer` adlı bir
değişkende sakla ve kodu `teach.check("Alıştırma G", answer)` satırıyla bitir. Yalnızca kodu, tek
bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Aynı kodu kayıttaki PR aralığı 190 ms olan "VC-0317" numaralı hasta için de çalıştır; ölçülen
değer 190 ms'den en çok 10 ms sapmalı.
```

### Alıştırma H: MIT-BIH 100 numaralı kayıtta atriyal erken atımlar

*Jupyter defteri, 6. bölüm, "Gerçek bir kayıtta her atımı bulmak: MIT-BIH 100 numaralı kayıt"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `ann_symbols` adlı bir Python listesi, MIT-BIH 100 numaralı kaydın etiket sembollerini (her
etiket için bir sembol) tutar: normal atım için "N", atriyal erken atım için "A", ventriküler erken
atım için "V" ve ritim değişikliği için "+".
Görev: Atriyal erken atımları say.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Atım sayısı, tam sayı olarak. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma H", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Her sembolü collections.Counter ile say ve sayıları yazdır; toplamları len(ann_symbols)
değerine eşit olmalı.
```

### Alıştırma I: Beş RR aralığının RMSSD değeri

*Jupyter defteri, 7. bölüm, "Kalp hızı değişkenliği"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 1000, 960, 1010, 990 ve 1030 ms'lik RR aralıkları.
Görev: Ardışık farkların karelerinin ortalamasının karekökünü (RMSSD) hesapla: Komşu aralıklar
arasındaki farkları al, karelerini al, karelerin ortalamasını bul ve karekökünü al.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: RMSSD'yi iki ondalığa yuvarla. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma I", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 800, 800 ve 800 ms'lik aralıklar 0; 800, 820 ve 800 ms'lik aralıklar ise 20 vermelidir.
```

### Alıştırma J: Örnek sayılarından güvenli bir QTc

*Jupyter defteri, 9. bölüm, "YZ ile eşli kodlama: Kod güvenlik kontrol listesi"*

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: fs Hz'de örneklenmiş bir EKG; QT ve RR aralıkları örnek sayısı olarak verilmiştir.
Görev: Bir `qtc_from_samples_fixed(qt_samples, rr_samples, fs)` fonksiyonu yaz; fs parametresine
varsayılan değer verme. Fonksiyon QT aralığını qt_samples / fs × 1000 ile milisaniyeye, RR aralığını
rr_samples / fs ile saniyeye çevirsin ve Bazett formülüyle (QTc = QT / √RR) hesaplanan QTc'yi
milisaniye cinsinden döndürsün. Fonksiyonu 500 Hz'de 196 ve 353 örnek için kullan.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: QTc'yi bir ondalığa yuvarla. Sonucu `answer` adlı bir değişkende sakla ve kodu
`teach.check("Alıştırma J", answer)` satırıyla bitir. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: 500 Hz'de 200 ve 500 örnek için QT 400 ms, RR aralığı 1 s olduğundan fonksiyon 400,0
döndürmelidir.
```

## Bölümlerin prompt görevleri

Jupyter defterindeki her numaralı bölüm bir prompt göreviyle biter. Prompt görevinde bir prompt vardır, ancak hazır kod ve `teach.check` satırı yoktur. Sonucun doğru olup olmadığını her promptun altındaki beklenen sonuç gösterir.

### 1. bölüm: Hastalık durumuna göre kolesterol

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: chol (mg/dL cinsinden serum kolesterolü) ve disease (koroner arter hastalığı için 1, yoksa 0)
sütunlarını içeren `heart` DataFrame'i.
Görev: İki hastalık grubunun chol değerleri için yan yana iki kutu grafiği çiz; eksen adlarını
birimleriyle yaz. Her grubun ortanca kolesterol değerini yazdır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve iki ortanca değer. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne
kısa bir yorum satırı ekle.
Test: Her gruptaki hasta sayısını yazdır; iki sayının toplamı 303 olmalı.
```

**Beklenen sonuç.** Ortanca değer hastalığı olmayanlarda 234,5 mg/dL, hastalığı olanlarda 249,0 mg/dL'dir.

### 2. bölüm: Cinsiyete göre tanılar

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: Sanal kliniğin `clinic` DataFrame'i; main_diagnosis sütununu ve "F" ya da "M" olarak kodlanmış
sex sütununu içerir.
Görev: pd.crosstab ile her ana tanı için cinsiyete göre hasta sayılarını gösteren, satır ve sütun
toplamları olan bir tablo oluştur.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Tablo. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Genel toplam 500 olmalı.
```

**Beklenen sonuç.** Klinikte 221 kadın ve 279 erkek vardır. HFrEF tanılı 47 hastanın 16'sı kadın, 31'i erkektir.

### 3. bölüm: D2'nin bir saniyesi, örnek örnek

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `case`, haftanın vakasının EKG'sidir: case.time saniye cinsinden zamanları, case.lead("II") D2
derivasyonunun milivolt cinsinden voltajlarını, case.fs ise Hz cinsinden örnekleme frekansını tutar.
Görev: D2'nin ilk saniyesini, her örneği küçük bir işaretle göstererek çiz; zaman ekseni milisaniye,
voltaj ekseni milivolt cinsinden olsun. Çizilen örnek sayısını yazdır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve bir sayı. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: 500 Hz'de bir saniye 500 örnek içerir.
```

**Beklenen sonuç.** Yazdırılan sayı 500'dür (iki uç da dâhil edildiyse 501) ve zaman ekseni 0'dan 1000 ms'ye uzanır.

### 4. bölüm: Bütün kliniğin frontal ekseni

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: Derece cinsinden frontal QRS eksenini tutan ecg_axis sütununu içeren `clinic` DataFrame'i.
Görev: ecg_axis değerlerinin histogramını çiz ve -30° ile +90°'ye dikey birer çizgi koy. Sol eksen
sapması (eksen -30°'nin altında) ve sağ eksen sapması (eksen +90°'nin üstünde) olan hastaların
sayısını ve yüzdesini yazdır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve dört sayı. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: Sol, normal ve sağ olmak üzere üç grubun sayılarının toplamı 500 olmalı.
```

**Beklenen sonuç.** Altı hastada (yüzde 1,2) sol eksen sapması, 25 hastada (yüzde 5,0) sağ eksen sapması vardır.

### 5. bölüm: Kalp hızları boyunca Bazett ve Fridericia

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: ecg_hr (bpm cinsinden kalp hızı) ve ecg_qt (ms cinsinden QT aralığı) sütunlarını içeren
`clinic` DataFrame'i.
Görev: İlk 50 hasta için QTc'yi Bazett (QT / √RR) ve Fridericia (QT / RR^(1/3)) formülleriyle
hesapla; saniye cinsinden RR aralığını RR = 60 / ecg_hr ile bul. Bazett eksi Fridericia farkını kalp
hızına karşı çiz, sıfır düzeyine yatay bir çizgi ekle ve en büyük farkı yazdır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve bir sayı. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: Tam 60 bpm'de iki formül aynı QTc'yi verir; dolayısıyla fark sıfırdır.
```

**Beklenen sonuç.** Fark, 60 bpm'nin üstündeki her hastada pozitif, 60 bpm'nin altındaki üç hastada negatiftir. En büyük fark 48,6 ms'dir.

### 6. bölüm: Otuz dakika boyunca kalp hızı

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `found`, MIT-BIH 100 numaralı kayıtta bulunan R tepelerini örnek konumları olarak, `fs_mit`
ise kaydın örnekleme frekansını (360 Hz) tutar.
Görev: Her atımın kalp hızını 60 / RR ile hesapla (RR saniye cinsinden) ve zamana karşı çiz; zaman
ekseni dakika cinsinden olsun. Ortalama kalp hızını yazdır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve bir sayı. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: 360 Hz'de 360 örneklik bir RR aralığı 1 s, yani 60 bpm'dir.
```

**Beklenen sonuç.** Ortalama kalp hızı yaklaşık 75,8 bpm'dir; atımdan atıma hız yaklaşık 53 ile 115 bpm arasında değişir.

### 7. bölüm: Bir Poincaré grafiği

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `rr5`, haftanın vakasındaki D2 derivasyonunun beş dakikasına ait RR aralıklarını milisaniye
cinsinden tutar.
Görev: Her RR aralığını bir sonrakine karşı çizen bir Poincaré grafiği oluştur; eksenler eşit
ölçekli olsun ve y = x doğrusu da çizilsin. SDNN'yi (ddof=1 ile standart sapma) ve RMSSD'yi yazdır.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Bir şekil ve iki sayı. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: 800, 820 ve 800 ms'lik aralıklar için RMSSD 20 ms'dir.
```

**Beklenen sonuç.** SDNN 17,7 ms, RMSSD 17,4 ms çıkar; bunlar 7. bölümde yazdırılan değerlerle aynıdır.

### 8. bölüm: Gerçek bir enfarktüsün göğüs derivasyonları

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: `ptb`, PTB s0010_re kaydını tutan bir pandas DataFrame'idir. v1-v6 sütunları göğüs
derivasyonlarını milivolt cinsinden tutar; örnekleme frekansı `fs_ptb`, yani 1000 Hz'dir.
Görev: V1-V6'nın ilk 3 saniyesini, saniye cinsinden ortak bir zaman ekseni ve milivolt cinsinden
voltajla alt alta çiz.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Altı satırlı bir şekil. Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir
yorum satırı ekle.
Test: 1000 Hz'de üç saniye derivasyon başına 3000 örnek içerir.
```

**Beklenen sonuç.** Şekil, her biri 3 s'lik altı satırdan oluşur. Kaydın başlığı akut inferolateral bir enfarktüs belirtir: Lateral duvara hangi göğüs derivasyonları bakar?

### 9. bölüm: YZ'nin yazdığı koda ikinci görüş

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: Bu bölümde bir YZ asistanının kısa bir promptla yazdığı `qtc_from_samples` fonksiyonu.
Fonksiyonun kodunu bu promptun altına yapıştırın.
Görev: Fonksiyonu üç soruyla gözden geçir. Birimler doğru mu? Örnekleme frekansı doğru kullanılıyor
mu? 500 Hz'de 196 örneklik bir QT ve 353 örneklik bir RR aralığı için sonuç fizyolojik bir değer mi?
Ardından düzeltilmiş bir fonksiyon ver.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Üç kısa maddelik bir değerlendirme ve düzeltilmiş fonksiyon. Yalnızca kodu, tek bir blok
olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: Düzeltilmiş fonksiyon 500 Hz'de 200 ve 500 örnek için 400,0 ms döndürmelidir.
```

**Beklenen sonuç.** Değerlendirme iki sorunu bulmalıdır: RR aralığının saniye yerine milisaniye cinsinden kullanılması ve 360 Hz'lik varsayılan örnekleme frekansı.

## Kodu açıklatmak, onarmak ve sınamak için kalıplar

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

### Test yazdırmak

```text
Aşağıdaki fonksiyon için, doğru sonucu elle hesaplanabilen girdilerle üç kısa test yaz; örneğin 60
bpm'lik kalp hızında RR aralığı tam 1 s'dir. Yalnızca assert ifadeleri kullan ve her testin hangi
hatayı yakaladığını açıkla.

[fonksiyonu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: measure_ecg fonksiyonuna frontal ekseni eklemek

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 5. bölümdeki `measure_ecg(leads, fs)` fonksiyonu ve yardımcı fonksiyonları `detect_r_peaks`
ile `qrs_bounds`. `vclinic.frontal_axis(v_i, v_avf)`, D1 ve aVF derivasyonlarının net QRS
voltajlarından frontal ekseni derece cinsinden döndürür.
Görev: `measure_ecg_axis(leads, fs)` adlı bir fonksiyon yaz: Fonksiyon `measure_ecg` ile aynı
sözlüğü, "axis_deg" anahtarı eklenmiş olarak döndürsün. Her atım için D1 ve aVF derivasyonlarının
net QRS voltajını, QRS başlangıcı ile sonu arasındaki en büyük pozitif ve en büyük negatif değerin
toplamı olarak al; değerleri QRS başlangıcından önceki 30 ms'nin ortancasına göre ölç. Bütün
atımlardaki değerlerin ortancalarını vclinic.frontal_axis fonksiyonuna ver.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Fonksiyon ve VC-0317 numaralı hasta için sonucu. Yalnızca kodu, tek bir blok olarak ver; her
adımın üstüne kısa bir yorum satırı ekle.
Test: Kayıtta VC-0317'nin ekseni 21°'dir. Net voltajlar küçük septal ve terminal kuvvetleri de
içerdiği için ölçülen eksen bu değerden en çok 10° kadar sapabilir.
```

### Adım 2: Gerçek değere karşı on hasta

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: patient_id, ecg_rhythm ("sinus" ya da "AF") ve ecg_conduction ("normal", "LBBB" ya da "RBBB")
sütunlarını içeren `clinic` DataFrame'i. `vclinic.patient_ecg(clinic, patient_id)` bir EKG nesnesi
döndürür; bu nesneye `e` diyelim. `e.truth` sözlüğü "hr_bpm", "pr_ms", "qrs_ms", "qt_ms" ve
"axis_deg" anahtarlarını içerir.
Görev: En az ikisinde atriyal fibrilasyon ya da dal bloğu bulunan on hasta seç. Her hasta için
`measure_ecg_axis` fonksiyonunu çalıştır (atriyal fibrilasyonda `sinus=False` ile). Kalp hızı, PR,
QRS, QT ve eksen için ölçülen değeri, gerçek değeri ve aradaki farkı gösteren bir tablo oluştur.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: Hasta başına bir satırı olan bir pandas DataFrame'i. Yalnızca kodu, tek bir blok olarak ver;
her adımın üstüne kısa bir yorum satırı ekle.
Test: Tabloda on satır olmalı; VC-0317'de PR, QRS ve QT farkları birkaç milisaniyeyi geçmemeli.
```

### Adım 3: İki gerçek kayıt

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 8. bölümden `leads_ptb` (PTB kaydının on iki derivasyonunu tutan NumPy dizisi) ve `fs_ptb`
(1000 Hz). 6. bölümden `found` (MIT-BIH 100 numaralı kayıtta bulunan R tepelerinin örnek konumları)
ve `fs_mit` (360 Hz).
Görev: `measure_ecg_axis` fonksiyonunu PTB kaydında çalıştır ve MIT-BIH 100 numaralı kaydın ortalama
kalp hızını bulunan atımlardan hesapla.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: PTB kaydının ölçümleri ve 100 numaralı kaydın ortalama kalp hızı. Yalnızca kodu, tek bir blok
olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: 8. bölümde PTB kaydı için kalp hızı 81,8 bpm, PR aralığı 225 ms, QRS süresi 137 ms ve QT 436,7
ms bulunmuştur.
```

### Adım 4: Her hasta için Bazett mi Fridericia mı?

```text
Rol: Python öğrenen bir kardiyoloğa yardım ediyorsun.
Bağlam: Bir Jupyter defteri. NumPy np, pandas pd, matplotlib.pyplot da plt adıyla içe aktarılmıştır;
vclinic ders paketi ve teach modülü de kullanılabilir.
Veri: 2. adımdaki tablo (her hastanın ölçülen QT değeri ve kalp hızı) ve `clinic` tablosundaki
cinsiyet bilgisi.
Görev: Her hasta için QTc'yi Bazett ve Fridericia formülleriyle hesapla ve kadınlar için 460 ms,
erkekler için 450 ms eşiğiyle uzamış olup olmadığına karar ver. İki formülün farklı karar verdiği
hastaları listele.
Kısıtlar: Yalnızca bu paketleri ve burada adı geçen değişkenleri kullan. Hiçbir dosya okuma, hiçbir
paket kurma.
Çıktı: İki yeni sütun eklenmiş tablo ve iki formülün farklı karar verdiği hastaların listesi.
Yalnızca kodu, tek bir blok olarak ver; her adımın üstüne kısa bir yorum satırı ekle.
Test: 85 bpm kalp hızındaki bir kadın olan VC-0317'de QTc, Bazett formülüne göre uzamış, Fridericia
formülüne göre normal çıkmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
