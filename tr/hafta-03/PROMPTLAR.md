# Prompt kütüphanesi, 3. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[3. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-03/PROMPTS.md)

Bu kütüphanede, 3. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın altındaki hücreye yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Sayılarla sine MR](#durak-1-sayılarla-sine-mr)
3. [Durak 2: İlk evrişimli ağ](#durak-2-ilk-evrişimli-ağ)
4. [Durak 3: EchoNet-Dynamic: Normal mi, anormal mi? (kişisel kayıtla)](#durak-3-echonet-dynamic-normal-mi-anormal-mi-kişisel-kayıtla)
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

## Durak 1: Sayılarla sine MR

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 3, 1-3. bölümler*

ACDC'nin uzman konturları her incelemeyi sayılara dönüştürür: Hacimler, ejeksiyon fraksiyonu (EF) ve duvarların kalınlığı bu konturlardan ölçülür. Bu durakta üç grup bu sayılarla tanımlanır, 134 numaralı hastanın EF'si konturların vokselleriyle hesaplanır ve ACDC kuralları her hastaya uygulanır.

### Adım 1.1: Üç grubun ejeksiyon fraksiyonu

**Amaç.** Bu adımda EF'nin ACDC'nin üç grubunu nasıl ayırdığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `acdc_table`, ACDC'nin NOR (normal), DCM (dilate kardiyomiyopati) ve HCM (hipertrofik
kardiyomiyopati) gruplarındaki 90 hastayı tutan bir tablodur ve her hasta bir satırda yer alır.
Burada kullanılan sütunlar şunlardır: group; split ("training" ya da "testing"); sol ventrikül
ejeksiyon fraksiyonunu veren lv_ef (%); vücut yüzey alanına göre indekslenmiş sol ventrikül diyastol
sonu hacmini veren lv_edvi (mL/m²) ve diyastol sonunda duvarın en kalın segmentini veren max_wall_mm
(mm). Bu değerlerin hepsi uzman konturlarından ölçülmüştür.
Görev: Her grubun ortalama ejeksiyon fraksiyonunu (lv_ef) hesapla ve üç ortalamayı bir ondalık
basamağa yuvarlayarak yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: DCM grubunun ortalama EF'sini bir ondalık basamağa yuvarlayarak ver. Sonucu `mean_ef_dcm`
adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her
adımın üstüne kısa bir açıklama satırı ekle.
Test: DCM grubunun ortalama EF'si yüzde 40'ın altında, HCM grubununki yüzde 50'nin üzerinde
olmalıdır.
```

**Beklenen sonuç:** `mean_ef_dcm` = 19,8

### Adım 1.2: 134 numaralı hastanın voksellerden hesaplanan ejeksiyon fraksiyonu

**Amaç.** Bu adımda, bir KMR laboratuvarının yazılımında olduğu gibi, hacimler ve EF uzman konturlarından hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `gt_ed` ve `gt_es`, 134 numaralı hastanın diyastol sonu ve sistol sonundaki uzman konturlarını
tutar; her vokselin bir etiketi vardır: 0 arka plan, 1 sağ ventrikül boşluğu, 2 miyokard, 3 sol
ventrikül boşluğu. `spacing`, bir vokselin üç yöndeki boyutunu mm cinsinden verir.
Görev: gt_ed ve gt_es içinde sol ventrikül boşluğuna ait vokselleri, yani etiketi 3 olanları say.
Her sayıyı bir vokselin hacmiyle, yani spacing içindeki üç boyutun mm³ cinsinden çarpımıyla çarp ve
mL'ye çevirmek için 1000'e böl. Böylece diyastol sonu hacmi EDV ve sistol sonu hacmi ESV elde
edilir. EF, (EDV − ESV)/EDV × 100 formülüyle hesaplanır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: EF'yi yüzde olarak ve bir ondalık basamağa yuvarlayarak ver; EDV ve ESV değerlerini de mL
cinsinden yazdır. Sonucu `ef_case` adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca
kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: EDV, ESV'den büyük olmalı ve 50 ile 300 mL arasında bulunmalıdır.
```

**Beklenen sonuç:** `ef_case` = 62,2

### Adım 1.3: ACDC kurallarının her hastaya uygulanması

**Amaç.** Bu adımda 90 hasta ACDC tanımlarıyla sınıflanır ve ölçümlerin tek başına nerede yanıldığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `acdc_table`, ACDC'nin NOR (normal), DCM (dilate kardiyomiyopati) ve HCM (hipertrofik
kardiyomiyopati) gruplarındaki 90 hastayı tutan bir tablodur ve her hasta bir satırda yer alır.
Burada kullanılan sütunlar şunlardır: group; split ("training" ya da "testing"); sol ventrikül
ejeksiyon fraksiyonunu veren lv_ef (%); vücut yüzey alanına göre indekslenmiş sol ventrikül diyastol
sonu hacmini veren lv_edvi (mL/m²) ve diyastol sonunda duvarın en kalın segmentini veren max_wall_mm
(mm). Bu değerlerin hepsi uzman konturlarından ölçülmüştür.
Görev: ACDC kurallarını her hastaya uygula. lv_ef 40'ın altında ve lv_edvi 100'ün üzerindeyse hasta
DCM'dir; değilse max_wall_mm 15'in üzerinde ve lv_ef 50 ya da daha yüksekse HCM'dir; ikisi de
değilse NOR'dur. Sonucu rule adlı yeni bir sütuna yaz, hastaları gruba ve kurala göre sayan bir
çapraz tablo yazdır ve kuralı grubuyla aynı olan hastaların oranını hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Oranı üç ondalık basamağa yuvarlayarak ver. Sonucu `rule_accuracy` adıyla sakla ve kısa bir
açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir
açıklama satırı ekle.
Test: Çapraz tablodaki hastaların toplamı 90 olmalı ve oran 0 ile 1 arasında bulunmalıdır.
```

**Beklenen sonuç:** `rule_accuracy` = 0,967

## Durak 2: İlk evrişimli ağ

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-2) · Python yolunda aynı sonuç: 4-7. bölümler*

Dersin ağı üç grubu ortadaki kesitlerin piksellerinden öğrenir; her kesitin diyastol sonu ve sistol sonu kareleri ağa iki kanal olarak girer. Bu durakta kesitler normalleştirilir, ağ kurulur ve erken durdurmayla eğitilir; ardından ağ 30 test hastasında, her hasta için tek bir kararla değerlendirilir.

### Adım 2.1: Eğitim kesitleriyle normalleştirme

**Amaç.** Bu adımda ağın girdileri, yalnızca eğitim hastalarından hesaplanan istatistiklerle hazırlanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `X`, 270 kesit tutar: 90 hastanın her birinin ortadaki üç kısa eksen kesiti. Her kesitte
diyastol sonu ve sistol sonu olmak üzere 64 × 64 piksellik iki kare vardır; değerler 0 ile 1
arasındadır ve bir piksel 2 mm'dir. `y` her kesitin grubunu (0 NOR, 1 DCM, 2 HCM), `patients`
hastasını, `sets` ise kümesini tutar: "train" (45 hasta), "val" (15 hasta) ya da "test" (30 hasta).
Görev: Eğitim kesitlerinin, yani kümesi "train" olan kesitlerin bütün piksellerinin ortalamasını ve
standart sapmasını hesapla. Bütün kesitleri bu iki sayıyla normalleştir: Ortalamayı çıkar ve
standart sapmaya böl. Ardından üç kümenin kesitlerini ve gruplarını PyTorch'un okuyabileceği biçime
getir; kesitleri X_train, X_val ve X_test, grupları da y_train, y_val ve y_test adlarıyla hazırla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Eğitim piksellerinin ortalamasını dört ondalık basamağa yuvarlayarak ver. Hazırlanan altı
diziyi sakla; sonraki adımlar onları kullanmaktadır. Sonucu `train_mean` adıyla sakla ve kısa bir
açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir
açıklama satırı ekle.
Test: X_train, her biri 64 × 64 piksellik iki kareden oluşan 135 kesit içermeli; normalleştirilmiş
eğitim piksellerinin ortalaması yaklaşık 0, standart sapması yaklaşık 1 olmalıdır.
```

**Beklenen sonuç:** `train_mean` = 0,2961

### Adım 2.2: Ağ ve parametreleri

**Amaç.** Bu adımda dersin ağı kurulur ve ağırlıkları sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: 2.1. adımda hazırlanan kesitler: `X_train`, `X_val` ve `X_test` üç kümenin kesitlerini, eğitim
piksellerinin ortalaması ve standart sapmasıyla normalleştirilmiş olarak; `y_train`, `y_val` ve
`y_test` ise bu kesitlerin gruplarını tutar. `patients` ve `sets`, her kesitin hastasını ve kümesini
verir.
Görev: Dersin ağını CmrCNN adlı bir sınıf olarak kur. Ağ üç bloktan oluşur; her blokta görüntünün
boyutunu koruyan 3 × 3 çekirdekli bir evrişim, yığın normalizasyonu, ReLU ve 2 × 2 maksimum
havuzlama bulunur. Bloklarda sırasıyla 8, 16 ve 32 çekirdek vardır; girdi, iki kare olmak üzere iki
kanallıdır. Blokların ardından düzleştirme, 0,3 oranında seyreltme ve üç grubun her birine bir skor
veren tek bir doğrusal katman gelir. Rastlantıyı RANDOM_STATE ile sabitle, model adlı bir ağ oluştur
ve eğitilebilir parametrelerini say.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Eğitilebilir parametre sayısını tam sayı olarak ver. CmrCNN sınıfını ve model ağını sakla.
Sonucu `n_params` adıyla sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok
hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Ağ, ilk dört eğitim kesiti için her biri üç skordan oluşan dört satır döndürmelidir.
```

**Beklenen sonuç:** `n_params` = 12219

### Adım 2.3: Erken durdurmayla eğitim ve hasta başına karar

**Amaç.** Bu adımda ağ eğitilir ve bir kliniğin yapacağı gibi değerlendirilir: Her hasta için tek bir karar verilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: 2.1. adımda hazırlanan kesitler: `X_train`, `X_val` ve `X_test` üç kümenin kesitlerini, eğitim
piksellerinin ortalaması ve standart sapmasıyla normalleştirilmiş olarak; `y_train`, `y_val` ve
`y_test` ise bu kesitlerin gruplarını tutar. `patients` ve `sets`, her kesitin hastasını ve kümesini
verir. `model`, 2.2. adımda kurulan ve henüz eğitilmemiş ağdır.
Görev: Ağı eğitim kesitleriyle 40 dönem boyunca eğit. Her dönemde kesitleri karıştır ve 16'şar
kesitlik küçük gruplar hâlinde kullan. Öğrenme yöntemi olarak Adam'ı, öğrenme hızı olarak 0,003'ü,
kayıp olarak da çapraz entropiyi kullan. Her dönemin sonunda, onlardan öğrenmeden doğrulama
kesitlerindeki kaybı ölç ve bu kaybın en düşük olduğu dönemin ağırlıklarının bir kopyasını sakla.
Eğitim bitince bu ağırlıklara geri dön. Ardından test kesitleri için üç grubun olasılıklarını
hesapla, her test hastasının kesitleri üzerinden ortalamalarını al ve ortalama olasılığı en yüksek
grubu o hastanın kararı olarak seç. Eğitimin tekrarlanabilmesi için rastlantıyı RANDOM_STATE ile
sabitle.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Kararı kendi grubuyla aynı olan test hastalarının oranını üç ondalık basamağa yuvarlayarak
ver. Hastaların ortalama olasılıklarını patient_prob, gruplarını patient_true, kararları da
patient_pred adıyla, hasta adlarının alfabetik sırasına göre sakla. Sonucu `patient_accuracy` adıyla
sakla ve kısa bir açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın
üstüne kısa bir açıklama satırı ekle.
Test: 30 test hastası olmalı ve her hastanın üç olasılığının toplamı 1 etmelidir.
```

**Beklenen sonuç:** `patient_accuracy` = 0,933

### Adım 2.4: Karışıklık matrisi ve makro F1

**Amaç.** Bu adımda sonuç sınıf sınıf okunur ve ağın kaçırdığı hastalar bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: 2.3. adımdaki patient_true ve patient_pred: 30 test hastasının grupları ve kararları (0 NOR, 1
DCM, 2 HCM); patient_prob ise bu hastaların ortalama olasılıklarıdır.
Görev: Gruplar ve kararlar için karışıklık matrisini oluştur; satırlarda gerçek gruplar, sütunlarda
kararlar NOR, DCM, HCM sırasıyla yer alsın ve matrisi bu adlarla yazdır. Her grubun F1 skorunu ve
bunların düz ortalaması olan makro F1'i hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Makro F1'i üç ondalık basamağa yuvarlayarak ver. Sonucu `macro_f1` adıyla sakla ve kısa bir
açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir
açıklama satırı ekle.
Test: Karışıklık matrisindeki sayıların toplamı 30 olmalıdır.
```

**Beklenen sonuç:** `macro_f1` = 0,933

## Durak 3: EchoNet-Dynamic: Normal mi, anormal mi? (kişisel kayıtla)

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-3) · Python yolunda aynı sonuç: 8-10. bölümler*

Oturumun mini projesi, her katılımcının Stanford AIMI'ye kişisel kayıtla edindiği ekokardiyografi videolarını, yani EchoNet-Dynamic'i kullanmaktadır. Kaydınız yoksa eğitmenin ortak ekrandaki çalıştırmasını izleyin. Kaydınız varsa kişisel indirme bağlantınızı aşağıdaki ilk hücreye yapıştırın ya da zip dosyasını ders klasöründeki data/echonet klasörüne koyun. Veriler Colab oturumunuzda ya da bilgisayarınızda kalır ve hiçbir zaman başka bir yere yüklenmez.

### Adım 3.1: Videolar ve kümeleri

**Amaç.** Bu adımda her analizden önce kopyanın eksiksiz olduğu denetlenir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `echo`, katılımcının kendi EchoNet-Dynamic kopyasıdır; ders paketi bu kopyayı iki araçla okur.
Okuma aracı `echonet.file_list`, kopyayı alır ve her video için bir satır içeren video tablosunu
verir; sütunlar FileName, EF (ejeksiyon fraksiyonu, %) ve Split'tir ("TRAIN", "VAL" ya da "TEST").
Kare aracı `echonet.frame_pairs` ise kopyayı, kümenin adını, video sayısını, görüntülerin piksel
cinsinden boyutunu ve videoların rastgele seçimi için bir tohum değerini alır. Seçilen her video
için çizilmiş diyastol sonu ve sistol sonu karelerini 0 ile 1 arasındaki değerlerle iki kanal olarak
(images) verir; abnormal değeri ise EF yüzde 50'nin altındaysa 1'dir.
Görev: Ders paketinin okuma aracıyla video tablosunu al. Split sütunundaki her kümenin video
sayısını ve toplam video sayısını yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Toplam video sayısını tam sayı olarak ver. Sonucu `n_videos` adıyla sakla ve kısa bir
açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir
açıklama satırı ekle.
Test: Üç kümede sırasıyla 7.465, 1.288 ve 1.277 video bulunmalıdır.
```

**Beklenen sonuç:** `n_videos`: eksiksiz bir kopya için 10.030

### Adım 3.2: Anormal EF oranı

**Amaç.** Bu adımda bir model değerlendirilmeden önce anormal sınıfın ne kadar sık olduğu öğrenilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `echo`, katılımcının kendi EchoNet-Dynamic kopyasıdır; ders paketi bu kopyayı iki araçla okur.
Okuma aracı `echonet.file_list`, kopyayı alır ve her video için bir satır içeren video tablosunu
verir; sütunlar FileName, EF (ejeksiyon fraksiyonu, %) ve Split'tir ("TRAIN", "VAL" ya da "TEST").
Kare aracı `echonet.frame_pairs` ise kopyayı, kümenin adını, video sayısını, görüntülerin piksel
cinsinden boyutunu ve videoların rastgele seçimi için bir tohum değerini alır. Seçilen her video
için çizilmiş diyastol sonu ve sistol sonu karelerini 0 ile 1 arasındaki değerlerle iki kanal olarak
(images) verir; abnormal değeri ise EF yüzde 50'nin altındaysa 1'dir.
Görev: Split değeri "TEST" olan videoları seç ve bunlar arasında EF'si yüzde 50'nin altında
olanların oranını hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: Oranı üç ondalık basamağa yuvarlayarak ver. Sonucu `share_low_ef` adıyla sakla ve kısa bir
açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir
açıklama satırı ekle.
Test: Oran 0 ile 1 arasında olmalı ve test videosu sayısı 1.277 olmalıdır.
```

**Beklenen sonuç:** `share_low_ef`: hazır kodun kopyanızdaki değeri

### Adım 3.3: Dersin ağı ekokardiyografide

**Amaç.** Bu adımda aynı ağ videoların diyastol sonu ve sistol sonu karelerinde eğitilir ve anormal EF'yi ne kadar iyi tanıdığı ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazdığın kod, bir Jupyter defterindeki hücreye
yapıştırılıp orada çalıştırılacak.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `echo`, katılımcının kendi EchoNet-Dynamic kopyasıdır; ders paketi bu kopyayı iki araçla okur.
Okuma aracı `echonet.file_list`, kopyayı alır ve her video için bir satır içeren video tablosunu
verir; sütunlar FileName, EF (ejeksiyon fraksiyonu, %) ve Split'tir ("TRAIN", "VAL" ya da "TEST").
Kare aracı `echonet.frame_pairs` ise kopyayı, kümenin adını, video sayısını, görüntülerin piksel
cinsinden boyutunu ve videoların rastgele seçimi için bir tohum değerini alır. Seçilen her video
için çizilmiş diyastol sonu ve sistol sonu karelerini 0 ile 1 arasındaki değerlerle iki kanal olarak
(images) verir; abnormal değeri ise EF yüzde 50'nin altındaysa 1'dir.
Görev: Ders paketinin kare aracıyla 1.000 eğitim videosunun ve 400 test videosunun çizilmiş iki
karesini 64 × 64 pikselde yükle; videoların seçimi için RANDOM_STATE değerini kullan. İki kümeyi de
eğitim piksellerinin ortalaması ve standart sapmasıyla normalleştir. Rastlantıyı RANDOM_STATE ile
sabitle ve dersin ağı CmrCNN'i normal ve anormal olmak üzere iki grupla, karıştırılmış 32'şer eğitim
videosundan oluşan küçük gruplar hâlinde 15 dönem eğit; öğrenme yöntemi olarak Adam'ı, öğrenme hızı
olarak 0,003'ü, kayıp olarak çapraz entropiyi kullan. Ardından her test videosu için anormal EF
olasılığını ve ROC eğrisinin altındaki alanı (AUC) hesapla.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı, bir şey
indirmemeli ve paket kurmamalıdır.
Çıktı: AUC değerini üç ondalık basamağa yuvarlayarak ver. Sonucu `auc_echo` adıyla sakla ve kısa bir
açıklamayla birlikte yazdır. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir
açıklama satırı ekle.
Test: Eğitim kareleri 64 × 64 piksellik 1.000 çift olmalı ve AUC 0,5 ile 1 arasında bulunmalıdır.
```

**Beklenen sonuç:** `auc_echo`: 0,6 ile 1,0 arasında, bilgisayardan bilgisayara biraz değişen bir değer

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

### Bir eğitim döngüsünü denetletmek

```text
Aşağıdaki kod tıbbi görüntüler için bir sınıflandırıcıyı eğitip değerlendirmektedir. Altı noktayı
denetle. Eğitim, doğrulama ve test kümelerine ayırma hastaya göre mi yapılmış? Normalleştirme
yalnızca eğitim görüntülerinin istatistiklerini mi kullanıyor? Ağ, öğrenirken eğitim moduna,
ölçülürken değerlendirme moduna alınıyor mu? Değerlendirme gradyan kaydedilmeden mi yapılıyor? Çıktı
katmanı kayıp fonksiyonuna uyuyor mu; yani softmax'ı kendisi uygulayan bir çapraz entropiden önce
ayrıca softmax uygulanmamış mı? Bildirilen ölçüt sınıflara uygun mu ve her hasta için tek bir karar
veriyor mu? Kısa bir listeyle cevap ver, ardından düzeltilmiş kodu ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla kurulabilir. Her adım bir öncekinin üzerine kurulduğu için bir adımın testi sağlanmadan sonraki prompt gönderilmez. Raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Ağı eğitmek

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `X`, 270 kesit tutar: 90 hastanın her birinin ortadaki üç kısa eksen kesiti. Her kesitte
diyastol sonu ve sistol sonu olmak üzere 64 × 64 piksellik iki kare vardır; değerler 0 ile 1
arasındadır ve bir piksel 2 mm'dir. `y` her kesitin grubunu (0 NOR, 1 DCM, 2 HCM), `patients`
hastasını, `sets` ise kümesini tutar: "train" (45 hasta), "val" (15) ya da "test" (30). `CmrCNN`, 5.
bölümdeki ağdır: İki kanallı bir girdi üzerinde, her birinde boyutu koruyan 3 × 3'lük bir evrişim,
yığın normalizasyonu, ReLU ve 2 × 2 maksimum havuzlama bulunan ve sırasıyla 8, 16 ve 32 çekirdek
içeren üç blok; ardından düzleştirme, 0,3 oranında seyreltme ve 2048 değeri 3 skora çeviren bir
doğrusal katman.
Görev: X'i eğitim piksellerinin, yani kümesi "train" olan kesitlerin ortalaması ve standart
sapmasıyla normalleştir ve üç kümeyi PyTorch için hazırla. Rastlantıyı RANDOM_STATE ile sabitle ve
CmrCNN'i Adam yöntemi, 0,003 öğrenme hızı, çapraz entropi kaybı ve karıştırılmış 16'şar eğitim
kesitlik küçük gruplarla 40 dönem eğit. Her dönemden sonra, ondan öğrenmeden doğrulama kaybını ölç
ve doğrulama kaybının en düşük olduğu ağırlıkların bir kopyasını sakla. Eğitim ve doğrulama kaybını
dönemlere karşı çiz.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Saklanan ağırlıklarla eğitilmiş ağı ve iki kaybın şeklini göster. Yalnızca kodu tek bir blok
hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Doğrulama kaybının en düşük olduğu dönemi yazdır; saklanan ağırlıklar yüklendikten sonra
doğrulama kaybı yine bu en düşük değeri vermelidir.
```

### Adım 2: Ağın karışıklık matrisi

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: 1. adımdaki ağ ve hazırlanmış test kesitleri ile kesitlerin y ve patients dizileri; test
kesitleri, kümesi "test" olanlardır.
Görev: Değerlendirme modunda ve gradyan kaydetmeden test kesitleri için üç grubun olasılıklarını
hesapla, her hastanın kesitleri üzerinden ortalamalarını al ve ortalaması en büyük grubu karar
olarak seç. 30 test hastasının NOR, DCM ve HCM gruplarıyla karışıklık matrisini, her grubun
kesinlik, duyarlılık ve F1 değerini ve makro F1'i bildir.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Karışıklık matrisini bir tablo olarak ve gruplara göre üç ölçütün tablosunu göster. Yalnızca
kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Matrisin toplamı 30, her satırının toplamı 10 olmalıdır.
```

### Adım 3: Aynı hastalarda ACDC kuralları

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: `acdc_table`, ACDC'nin NOR (normal), DCM (dilate kardiyomiyopati) ve HCM (hipertrofik
kardiyomiyopati) gruplarındaki 90 hastayı tutan bir tablodur ve her hasta bir satırda yer alır.
Burada kullanılan sütunlar şunlardır: group; split ("training" ya da "testing"); sol ventrikül
ejeksiyon fraksiyonunu veren lv_ef (%); vücut yüzey alanına göre indekslenmiş sol ventrikül diyastol
sonu hacmini veren lv_edvi (mL/m²) ve diyastol sonunda duvarın en kalın segmentini veren max_wall_mm
(mm). Bu değerlerin hepsi uzman konturlarından ölçülmüştür.
Görev: ACDC kurallarını acdc_table tablosunda split değeri "testing" olan hastalara uygula: lv_ef
40'ın altında ve lv_edvi 100'ün üzerindeyse DCM; değilse max_wall_mm 15'in üzerinde ve lv_ef 50 ya
da daha yüksekse HCM; ikisi de değilse NOR. Grup ile kuralın karışıklık matrisini NOR, DCM, HCM
sırasıyla ve doğruluğu bildir.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Karışıklık matrisini bir tablo olarak ve doğruluğu üç ondalık basamağa yuvarlanmış olarak
göster. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Matrisin toplamı 30 olmalıdır; aynı kurallar 90 hastanın tamamında 1.3. adımdaki doğruluğu
vermelidir.
```

### Adım 4: Hatalar

```text
Rol: Programlamaya yeni başlayan bir kardiyoloğa yardım ediyorsun.
Bağlam: Kod, aşağıdaki verilerin önceden yüklendiği 3. hafta Jupyter defterinde çalışacak. Tablolar,
hesaplar ve grafikler için kullanılan paketler (pandas, NumPy ve Matplotlib), derin öğrenme paketi
PyTorch, makine öğrenmesi paketi scikit-learn ve acdc ile echonet modülleriyle birlikte vclinic ders
paketi hazırdır. RANDOM_STATE, defterin rastlantının rol oynadığı her yerde kullandığı sabit değeri
tutar.
Veri: 2. adımdaki kararlar ve test hastalarının adları, acdc_table ve S. S, her hastanın ortadaki üç
kesitini, bu kesitlerin 64 × 64 piksellik görüntülerini, hastalarını ve fazlarını ("ED" ya da "ES")
tutar; ders paketinin acdc.slices aracı S'yi NOR, DCM ve HCM grupları için hazırlamıştır. Paketin
bir başka aracı olan acdc.walls ise bir hastanın adını alır ve o hastanın diyastol sonundaki her
kesitinde en kalın duvarı mm cinsinden, tabandan (0. kesit) apekse doğru verir.
Görev: Kararı grubundan farklı olan her test hastası için ağın gördüğü üç diyastol sonu kesitini,
başlıkta grup, karar ve max_wall_mm değeriyle göster. Ardından incelemenin her kesitindeki en kalın
duvarı tabandan apekse doğru yazdır.
Kısıtlar: Yalnızca burada adı geçen verileri ve araçları kullan. Kod dosya okumamalı ve paket
kurmamalıdır.
Çıktı: Yanlış sınıflanan her hasta için bir şekil ve kesitlere göre en kalın duvarın listesini
göster. Yalnızca kodu tek bir blok hâlinde ver ve her adımın üstüne kısa bir açıklama satırı ekle.
Test: Gösterilen hasta sayısı, 2. adımdaki karışıklık matrisindeki hata sayısına eşit olmalıdır.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
