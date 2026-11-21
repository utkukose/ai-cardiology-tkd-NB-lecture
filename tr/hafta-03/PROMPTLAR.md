# Prompt kütüphanesi, 3. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[3. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-03/PROMPTS.md)

Bu kütüphanede, 3. haftanın prompt (istem) yolundaki, yani Jupyter Notebook'un 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, Jupyter Notebook'ta aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir Jupyter Notebook'a ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Sayılarla sine MR](#durak-1-sayılarla-sine-mr)
3. [Durak 2: İlk evrişimli ağ](#durak-2-ilk-evrişimli-ağ)
4. [Durak 3: Mini proje: EchoNet-Dynamic, normal mi anormal mi? (kişisel kayıtla)](#durak-3-mini-proje-echonet-dynamic-normal-mi-anormal-mi-kişisel-kayıtla)
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

## Durak 1: Sayılarla sine MR

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 3, 1-3. bölümler*

ACDC'nin uzman konturları her incelemeyi sayılara dönüştürür: Hacimler, ejeksiyon fraksiyonu (EF) ve duvarların kalınlığı bu konturlardan ölçülür. Bu durakta üç grup bu sayılarla tanımlanır, 134 numaralı hastanın EF'si konturların vokselleriyle hesaplanır ve ACDC kuralları her hastaya uygulanır.

### Adım 1.1: Üç grubun ejeksiyon fraksiyonu

**Amaç.** Bu adımda EF'nin ACDC'nin üç grubunu nasıl ayırdığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Kardiyak MR veri seti ACDC'de, sol ventrikül ejeksiyon fraksiyonunun normal kalpler, dilate
kardiyomiyopati ve hipertrofik kardiyomiyopati arasında nasıl farklılaştığını görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'nin NOR (normal), DCM (dilate
kardiyomiyopati) ve HCM (hipertrofik kardiyomiyopati) gruplarındaki 90 hastayı tutar. Her satır bir
hastadır: "hasta" sütunu hastanın adını, "grup" grubunu, "LVEF" sol ventrikül ejeksiyon fraksiyonunu
yüzde olarak, "LVEDVI" vücut yüzey alanına göre indekslenmiş sol ventrikül diyastol sonu hacmini
mL/m² olarak, "en kalın duvar" da diyastol sonunda duvarın en kalın segmentini mm olarak verir.
Bütün değerler uzmanların çizdiği konturlarda ölçülmüştür.
Görev: Her grubun ortalama LVEF değerini hesapla ve üç ortalamayı bir ondalık basamakla yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: DCM grubunun ortalama LVEF değerini bir ondalık basamakla "cevap" adıyla sakla.
Test: DCM grubunun ortalaması yüzde 40'ın altında, HCM grubununki yüzde 50'nin üzerinde olmalı.
```

**Beklenen sonuç:** "cevap" = 19,8

### Adım 1.2: 134 numaralı hastanın voksellerden hesaplanan ejeksiyon fraksiyonu

**Amaç.** Bu adımda, bir KMR laboratuvarının yazılımında olduğu gibi, hacimler ve EF uzman konturlarından kesit kesit hesaplanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC'deki 134 numaralı hastanın sol ventrikül diyastol sonu ve sistol sonu hacimlerini ve
ejeksiyon fraksiyonunu, konturla çizilmiş kaviteyi kesit kesit toplayarak hesaplamak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var. Her satır, incelemenin tabandan apekse doğru
sıralanmış bir kısa eksen kesitidir: "kesit" sütunu kesitin numarasını, "diyastol sonu" ve "sistol
sonu" sütunları da o kesitte sol ventrikül kavitesinin konturu içinde kalan piksel sayısını verir.
Bir piksel 1,445 × 1,445 mm'dir ve kesitler 10 mm kalınlığındadır.
Görev: Her faz için bütün kesitlerdeki pikselleri topla ve toplamı bir vokselin hacmiyle, yani 1,445
× 1,445 × 10 mm³ ile çarp; mL'ye çevirmek için 1.000'e böl. Böylece diyastol sonu hacmi EDV ve
sistol sonu hacmi ESV bulunur. EF, (EDV − ESV)/EDV × 100 formülüyle hesaplanır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: EDV ve ESV değerlerini mL, EF'yi yüzde olarak bir ondalık basamakla yazdır; EF'yi "cevap"
adıyla sakla.
Test: EDV, ESV'den büyük olmalı ve 50 ile 300 mL arasında bulunmalı.
```

**Beklenen sonuç:** "cevap" = 62,2

### Adım 1.3: ACDC kurallarının her hastaya uygulanması

**Amaç.** Bu adımda 90 hasta ACDC tanımlarıyla sınıflanır ve ölçümlerin tek başına nerede yanıldığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC tanımlarındaki ölçüm kurallarının bir hastayı ne sıklıkla uzmanların verdiği gruba
yerleştirdiğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'nin NOR (normal), DCM (dilate
kardiyomiyopati) ve HCM (hipertrofik kardiyomiyopati) gruplarındaki 90 hastayı tutar. Her satır bir
hastadır: "hasta" sütunu hastanın adını, "grup" grubunu, "LVEF" sol ventrikül ejeksiyon fraksiyonunu
yüzde olarak, "LVEDVI" vücut yüzey alanına göre indekslenmiş sol ventrikül diyastol sonu hacmini
mL/m² olarak, "en kalın duvar" da diyastol sonunda duvarın en kalın segmentini mm olarak verir.
Bütün değerler uzmanların çizdiği konturlarda ölçülmüştür.
Görev: ACDC kurallarını her hastaya uygula: LVEF 40'ın altında ve LVEDVI 100'ün üzerindeyse hasta
DCM'dir; değilse en kalın duvar 15'in üzerinde ve LVEF 50 ya da daha yüksekse HCM'dir; ikisi de
değilse NOR'dur. Hastaları gruba ve kurala göre sayan bir çapraz tablo yazdır ve kuralı grubuyla
aynı olan hastaların oranını hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Oranı üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Çapraz tablodaki hastaların toplamı 90 olmalı ve oran 0 ile 1 arasında bulunmalı.
```

**Beklenen sonuç:** "cevap" = 0,967

## Durak 2: İlk evrişimli ağ

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-2) · Python yolunda aynı sonuç: 4-7. bölümler*

Dersin ağı üç grubu ortadaki kesitlerin piksellerinden öğrenir; her kesitin diyastol sonu ve sistol sonu kareleri ağa iki kanal olarak girer. Bu durakta kesitler normalleştirilir, ağ kurulur ve erken durdurmayla eğitilir; ardından ağ 30 test hastasında, her hasta için tek bir kararla değerlendirilir.

### Adım 2.1: Eğitim kesitleriyle normalleştirme

**Amaç.** Bu adımda ağın girdileri, yalnızca eğitim hastalarından hesaplanan istatistiklerle hazırlanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir ağ ACDC gruplarını sine MR kesitlerinden öğrenmeden önce, pikselleri yalnızca eğitim
hastalarından gelen sayılarla ölçeklemek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'deki 90 hastanın her birinin ortadaki üç
kısa eksen kesitinden oluşan 270 sine MR kesitini tutar. Her satır bir kesittir: "hasta" sütunu
hastayı, "grup" hastanın grubunu ("NOR", "DCM" ya da "HCM"), "küme" ise hastanın kümesini verir
("eğitim", 45 hasta; "doğrulama", 15 hasta; "test", 30 hasta). "diyastol sonu" ve "sistol sonu"
sütunlarının her hücresinde, değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü vardır;
bir piksel 2 mm'dir.
Görev: Eğitim kesitlerinin, yani kümesi "eğitim" olan kesitlerin iki karesindeki bütün piksellerin
ortalamasını ve standart sapmasını hesapla. Bütün kesitlerin piksellerini bu iki sayıyla
normalleştir: Ortalamayı çıkar ve standart sapmaya böl.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Ortalamayı ve standart sapmayı dört ondalık basamakla yazdır; ortalamayı "cevap" adıyla
sakla.
Test: Normalleştirmeden sonra eğitim piksellerinin ortalaması yaklaşık 0, standart sapması yaklaşık
1 olmalı; 135 eğitim kesiti 64 × 64 piksellik boyutunu korumalı.
```

**Beklenen sonuç:** "cevap" = 0,2961

### Adım 2.2: Ağ ve parametreleri

**Amaç.** Bu adımda dersin ağı kurulur ve ağırlıkları sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC grupları için küçük bir evrişimli ağ kurmak ve ağın kaç ağırlık öğrendiğini bilmek
istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'deki 90 hastanın her birinin ortadaki üç
kısa eksen kesitinden oluşan 270 sine MR kesitini tutar. Her satır bir kesittir: "hasta" sütunu
hastayı, "grup" hastanın grubunu ("NOR", "DCM" ya da "HCM"), "küme" ise hastanın kümesini verir
("eğitim", 45 hasta; "doğrulama", 15 hasta; "test", 30 hasta). "diyastol sonu" ve "sistol sonu"
sütunlarının her hücresinde, değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü vardır;
bir piksel 2 mm'dir.
Görev: Bir kesitin iki karesini iki kanal olarak alan küçük bir evrişimli ağ kur. Ağ üç bloktan
oluşur; her blokta görüntünün boyutunu koruyan 3 × 3 çekirdekli bir evrişim, batch normalizasyonu,
ReLU ve 2 × 2 maksimum havuzlama bulunur. Bloklarda sırasıyla 8, 16 ve 32 çekirdek vardır. Blokların
ardından düzleştirme, 0,3 oranında dropout ve üç grubun her birine bir skor veren tek bir doğrusal
katman gelir. Ağın öğrendiği ağırlıkları, yani eğitilebilir parametrelerini say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitilebilir parametre sayısını yazdır ve "cevap" adıyla sakla.
Test: Ağ, ilk dört eğitim kesiti için her biri üç skordan oluşan dört satır vermeli.
```

**Beklenen sonuç:** "cevap" = 12.219

### Adım 2.3: Erken durdurmayla eğitim ve hasta başına karar

**Amaç.** Bu adımda ağ eğitilir ve bir kliniğin yapacağı gibi değerlendirilir: Her hasta için tek bir karar verilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC'nin sine MR kesitlerinde küçük bir evrişimli ağ eğitmek ve ağı test hastalarında bir
kliniğin yapacağı gibi, her hasta için tek bir kararla değerlendirmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'deki 90 hastanın her birinin ortadaki üç
kısa eksen kesitinden oluşan 270 sine MR kesitini tutar. Her satır bir kesittir: "hasta" sütunu
hastayı, "grup" hastanın grubunu ("NOR", "DCM" ya da "HCM"), "küme" ise hastanın kümesini verir
("eğitim", 45 hasta; "doğrulama", 15 hasta; "test", 30 hasta). "diyastol sonu" ve "sistol sonu"
sütunlarının her hücresinde, değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü vardır;
bir piksel 2 mm'dir.
Görev: Pikselleri eğitim kesitlerinin ortalaması ve standart sapmasıyla normalleştir. Bir kesitin
iki karesini iki kanal olarak alan küçük bir evrişimli ağ kur. Ağ üç bloktan oluşur; her blokta
görüntünün boyutunu koruyan 3 × 3 çekirdekli bir evrişim, batch normalizasyonu, ReLU ve 2 × 2
maksimum havuzlama bulunur. Bloklarda sırasıyla 8, 16 ve 32 çekirdek vardır. Blokların ardından
düzleştirme, 0,3 oranında dropout ve üç grubun her birine bir skor veren tek bir doğrusal katman
gelir. Ağı eğitim kesitlerinde çapraz entropi kaybıyla eğit. Her epoch'un sonunda, onlardan
öğrenmeden doğrulama kesitlerindeki kaybı ölç ve bu kaybın en düşük olduğu epoch'un ağırlıklarını
sakla (erken durdurma). Rastgele seçimler her çalıştırmada aynı olsun; bunun için başlangıç değeri
olarak 2026 sayısını kullan. Ardından her test kesiti için üç grubun olasılıklarını hesapla, bu
olasılıkların her test hastasının üç kesiti üzerinden ortalamasını al ve ortalaması en büyük grubu
hastanın kararı olarak seç.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Doğrulama kaybının en düşük olduğu epoch'u ve 30 test hastasından kararı kendi grubuyla aynı
olanların oranını üç ondalık basamakla yazdır; oranı "cevap" adıyla sakla.
Test: 30 test hastası olmalı ve her hastanın üç ortalama olasılığının toplamı 1 etmeli.
```

**Beklenen sonuç:** "cevap" = 0,933

### Adım 2.4: Karışıklık matrisi ve makro F1

**Amaç.** Bu adımda sonuç sınıf sınıf okunur ve ağın kaçırdığı hastalar bulunur. Veri hücresi dersin ağını bir kez eğitir; bu yaklaşık bir dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC'nin 30 test hastasında bir ağın kararlarını grup grup okumak ve ağın kaçırdığı
hastaları bulmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var. Her satır bir test hastasıdır: "hasta" sütunu
hastanın adını, "gerçek grup" uzmanların verdiği grubu, "karar" ise ağın seçtiği grubu verir; ikisi
de "NOR", "DCM" ya da "HCM" değerlerinden biridir.
Görev: Satırlarda gerçek gruplar, sütunlarda kararlar NOR, DCM, HCM sırasıyla yer alacak biçimde
karışıklık matrisini oluştur ve yazdır. Her grubun F1 skorunu ve bunların düz ortalaması olan makro
F1'i hesapla. Kararı gerçek grubundan farklı olan hastaların adlarını yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Makro F1'i üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Karışıklık matrisinin toplamı 30, her satırının toplamı 10 olmalı.
```

**Beklenen sonuç:** "cevap" = 0,933

## Durak 3: Mini proje: EchoNet-Dynamic, normal mi anormal mi? (kişisel kayıtla)

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-3) · Python yolunda aynı sonuç: 8-10. bölümler*

Oturumun mini projesi, her katılımcının Stanford AIMI'ye kişisel kayıtla edindiği ekokardiyografi videolarını, yani EchoNet-Dynamic'i kullanmaktadır. Kaydınız yoksa eğitmenin ortak ekrandaki çalıştırmasını izleyin. Kaydınız varsa kişisel indirme bağlantınızı Jupyter Notebook'ta bu durağın ilk hücresine yapıştırın ya da zip dosyasını ders klasöründeki data/echonet klasörüne koyun. Veriler Colab oturumunuzda ya da bilgisayarınızda kalır ve hiçbir zaman bir prompta girmez: Promptlar yalnızca Jupyter Notebook'un hazırladığı tabloyu tarif eder.

### Adım 3.1: Videolar ve kümeleri

**Amaç.** Bu adımda her analizden önce kopyanın eksiksiz olduğu denetlenir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Her analizden önce, ekokardiyografi veri seti EchoNet-Dynamic'ten edindiğim kopyanın
eksiksiz olduğunu denetlemek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; bir ekokardiyografi video veri seti olan
EchoNet-Dynamic'in kendi kopyamdaki videolarını tutar. Her satır bir videodur: "video" sütunu
videonun adını, "EF" ejeksiyon fraksiyonunu yüzde olarak, "küme" ise yazarların seçtiği kümeyi verir
("eğitim", "doğrulama" ya da "test").
Görev: Her kümedeki video sayısını ve toplam video sayısını yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Toplam video sayısını "cevap" adıyla sakla.
Test: "eğitim", "doğrulama" ve "test" kümelerinde sırasıyla 7.465, 1.288 ve 1.277 video bulunmalı.
```

**Beklenen sonuç:** "cevap": eksiksiz bir kopya için 10.030

### Adım 3.2: Anormal EF oranı

**Amaç.** Bu adımda bir model değerlendirilmeden önce anormal sınıfın ne kadar sık olduğu öğrenilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: EchoNet-Dynamic için bir model değerlendirilmeden önce, test videoları arasında yüzde 50'nin
altındaki anormal bir ejeksiyon fraksiyonunun ne kadar sık olduğunu öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; bir ekokardiyografi video veri seti olan
EchoNet-Dynamic'in kendi kopyamdaki videolarını tutar. Her satır bir videodur: "video" sütunu
videonun adını, "EF" ejeksiyon fraksiyonunu yüzde olarak, "küme" ise yazarların seçtiği kümeyi verir
("eğitim", "doğrulama" ya da "test").
Görev: Kümesi "test" olan videoları seç ve bunlar arasında EF'si yüzde 50'nin altında olanların
oranını hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Oranı üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: Oran 0 ile 1 arasında olmalı ve test videosu sayısı 1.277 olmalı.
```

**Beklenen sonuç:** "cevap": hazır kodun kopyanızdaki değeri

### Adım 3.3: Dersin ağı ekokardiyografide

**Amaç.** Bu adımda aynı ağ videoların diyastol sonu ve sistol sonu karelerinde eğitilir ve anormal EF'yi ne kadar iyi tanıdığı ölçülür. Veri hücresi 1.400 videoyu okur; bu birkaç dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Küçük bir evrişimli ağın, bir ekokardiyografi videosunun iki karesinden, yani diyastol sonu
ve sistol sonu karelerinden yüzde 50'nin altındaki bir ejeksiyon fraksiyonunu ne kadar iyi
tanıdığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; EchoNet-Dynamic'ten 1.000 eğitim ve 400 test
videosunu tutar. Her satır bir videodur: "küme" sütununda "eğitim" ya da "test" yazar; "anormal"
sütunu EF yüzde 50'nin altındaysa 1, değilse 0'dır. "diyastol sonu" ve "sistol sonu" sütunlarının
her hücresi, o fazın çizilmiş karesini değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü
olarak tutar.
Görev: Pikselleri eğitim videolarının ortalaması ve standart sapmasıyla normalleştir. Bir videonun
iki karesini iki kanal olarak alan küçük bir evrişimli ağ kur. Ağ üç bloktan oluşur; her blokta
görüntünün boyutunu koruyan 3 × 3 çekirdekli bir evrişim, batch normalizasyonu, ReLU ve 2 × 2
maksimum havuzlama bulunur. Bloklarda sırasıyla 8, 16 ve 32 çekirdek vardır. Blokların ardından
düzleştirme, 0,3 oranında dropout ve normal EF ile anormal EF için birer skor veren tek bir doğrusal
katman gelir. Ağı eğitim videolarında çapraz entropi kaybıyla eğit. Rastgele seçimler her
çalıştırmada aynı olsun; bunun için başlangıç değeri olarak 2026 sayısını kullan. Ardından her test
videosu için anormal EF olasılığını ve ROC eğrisinin altındaki alanı (AUC) hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: AUC değerini üç ondalık basamakla yazdır ve "cevap" adıyla sakla.
Test: İki karesi 64 × 64 piksel olan 1.000 eğitim videosu bulunmalı ve AUC 0,5 ile 1 arasında
olmalı.
```

**Beklenen sonuç:** "cevap": 0,6 ile 1,0 arasında, bilgisayardan bilgisayara biraz değişen bir değer

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

### Bir eğitim döngüsünü denetletmek

```text
Aşağıdaki kod, tıbbi görüntüler için bir sınıflandırıcıyı eğitip değerlendirmektedir. Altı noktayı
denetle. Eğitim, doğrulama ve test kümelerine ayırma hastaya göre mi yapılmış? Normalleştirme
yalnızca eğitim görüntülerinin istatistiklerini mi kullanıyor? Ağ, öğrenirken eğitim moduna,
ölçülürken değerlendirme moduna alınıyor mu? Değerlendirme gradyan kaydedilmeden mi yapılıyor? Çıktı
katmanı kayba uyuyor mu; softmax'ı kendisi uygulayan bir çapraz entropiden önce ayrıca softmax
uygulanmış mı? Bildirilen ölçüt sınıflara uygun mu ve her hasta için tek bir karar veriyor mu? Kısa
bir listeyle cevap ver, ardından düzeltilmiş kodu ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter Notebook'un 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Ağı eğitmek

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC'nin sine MR kesitlerinde küçük bir evrişimli ağı erken durdurmayla eğitmek ve eğitim
ile doğrulama kesitlerinin kayıplarının nasıl değiştiğini görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'deki 90 hastanın her birinin ortadaki üç
kısa eksen kesitinden oluşan 270 sine MR kesitini tutar. Her satır bir kesittir: "hasta" sütunu
hastayı, "grup" hastanın grubunu ("NOR", "DCM" ya da "HCM"), "küme" ise hastanın kümesini verir
("eğitim", 45 hasta; "doğrulama", 15 hasta; "test", 30 hasta). "diyastol sonu" ve "sistol sonu"
sütunlarının her hücresinde, değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü vardır;
bir piksel 2 mm'dir.
Görev: Pikselleri eğitim kesitlerinin ortalaması ve standart sapmasıyla normalleştir. Bir kesitin
iki karesini iki kanal olarak alan küçük bir evrişimli ağ kur. Ağ üç bloktan oluşur; her blokta
görüntünün boyutunu koruyan 3 × 3 çekirdekli bir evrişim, batch normalizasyonu, ReLU ve 2 × 2
maksimum havuzlama bulunur. Bloklarda sırasıyla 8, 16 ve 32 çekirdek vardır. Blokların ardından
düzleştirme, 0,3 oranında dropout ve üç grubun her birine bir skor veren tek bir doğrusal katman
gelir. Ağı eğitim kesitlerinde çapraz entropi kaybıyla eğit. Rastgele seçimler her çalıştırmada aynı
olsun; bunun için başlangıç değeri olarak 2026 sayısını kullan. Her epoch'un sonunda, onlardan
öğrenmeden doğrulama kesitlerindeki kaybı ölç ve bu kaybın en düşük olduğu epoch'un ağırlıklarını
sakla. Eğitim ve doğrulama kaybını epoch'lara karşı çiz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki kaybın şeklini göster; doğrulama kaybının en düşük olduğu epoch'u "cevap" adıyla sakla.
Test: Saklanan ağırlıklar yüklendikten sonra doğrulama kaybı yine en düşük değerini vermeli.
```

### Adım 2: Ağın karışıklık matrisi

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC'nin 30 test hastasında, her hasta için tek bir kararla bir ağın karışıklık matrisini ve
her grubun kesinlik, duyarlılık ve F1 değerlerini görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; 30 test hastasının her birinden üç kesit
olmak üzere 90 test kesitini tutar. Her satır bir kesittir: "hasta" sütunu hastayı, "gerçek grup"
uzmanların verdiği grubu, "NOR", "DCM" ve "HCM" sütunları da dersin ağının bu kesite verdiği üç
grubun olasılıklarını 0 ile 1 arasında bir sayı olarak verir. Veri hücresi bu ağı bir kez eğitir; bu
yaklaşık bir dakika sürer.
Görev: Olasılıkların her hastanın kesitleri üzerinden ortalamasını al ve ortalaması en büyük grubu
karar olarak seç. 30 hastanın karışıklık matrisini, satırlarda gerçek gruplar ve sütunlarda kararlar
NOR, DCM, HCM sırasıyla yer alacak biçimde oluştur. Her grubun kesinlik, duyarlılık ve F1 değerini
ve makro F1'i hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Matrisi ve gruplara göre üç ölçütün tablosunu göster; makro F1'i "cevap" adıyla sakla.
Test: Matrisin toplamı 30, her satırının toplamı 10 olmalı.
```

### Adım 3: Aynı hastalarda ACDC kuralları

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Ağı, aynı 30 test hastasında ACDC'nin ölçüm kurallarıyla karşılaştırmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'nin NOR (normal), DCM (dilate
kardiyomiyopati) ve HCM (hipertrofik kardiyomiyopati) gruplarındaki 30 test hastasını tutar. Her
satır bir hastadır: "hasta" sütunu hastanın adını, "grup" grubunu, "LVEF" sol ventrikül ejeksiyon
fraksiyonunu yüzde olarak, "LVEDVI" vücut yüzey alanına göre indekslenmiş sol ventrikül diyastol
sonu hacmini mL/m² olarak, "en kalın duvar" da diyastol sonunda duvarın en kalın segmentini mm
olarak verir. Bütün değerler uzmanların çizdiği konturlarda ölçülmüştür.
Görev: ACDC kurallarını uygula: LVEF 40'ın altında ve LVEDVI 100'ün üzerindeyse hasta DCM'dir;
değilse en kalın duvar 15'in üzerinde ve LVEF 50 ya da daha yüksekse HCM'dir; ikisi de değilse
NOR'dur. Grup ile kuralın karışıklık matrisini NOR, DCM, HCM sırasıyla oluştur ve doğruluğu hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Matrisi göster ve doğruluğu üç ondalık basamakla yazdır; doğruluğu "cevap" adıyla sakla.
Test: Matrisin toplamı 30 olmalı.
```

### Adım 4: Hatalar

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir ACDC ağının yanlış sınıfladığı test hastalarında, sol ventrikülün en kalın duvarının
tabandan apekse doğru nerede bulunduğunu görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; dersin ağının yanlış sınıfladığı test
hastalarını tutar. Her satır bu hastalardan birinin diyastol sonundaki bir kısa eksen kesitidir:
"hasta" sütunu hastayı, "gerçek grup" ve "karar" uzmanların ve ağın verdiği grubu, "kesit" kesitin
tabandan (0) apekse doğru numarasını, "en kalın duvar" o kesitteki duvarın en kalın segmentini mm
olarak verir. "ağın gördüğü" sütununda, ağın gördüğü tek kesitler olan ortadaki üç kesit için "evet"
yazar.
Görev: Her hasta için en kalın duvarı kesit numarasına karşı çiz ve ağın gördüğü kesitleri işaretle.
İncelemenin en kalın duvarının bulunduğu kesiti ve ağın bu kesiti görüp görmediğini yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her hasta için bir şekil göster; yanlış sınıflanan hasta sayısını "cevap" adıyla sakla.
Test: Her hastada "ağın gördüğü" sütununda tam üç "evet" bulunmalı; hasta sayısı da proje adımı
2'deki karışıklık matrisinin hata sayısına eşit olmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
