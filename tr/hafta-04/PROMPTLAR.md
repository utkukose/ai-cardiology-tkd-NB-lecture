# Prompt kütüphanesi, 4. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[4. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-04/PROMPTS.md)

Bu kütüphanede, 4. haftanın prompt (istem) yolundaki, yani Jupyter Notebook'un 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, Jupyter Notebook'ta aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir Jupyter Notebook'a ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Mini proje: EfficientNet-B0 ile az sayıda etiketli görüntüden KMP sınıflandırma](#durak-1-mini-proje-efficientnet-b0-ile-az-sayıda-etiketli-görüntüden-kmp-sınıflandırma)
3. [Durak 2: Pixel-wise segmentasyon eğitimi: CAMUS'ta bir U-Net](#durak-2-pixel-wise-segmentasyon-eğitimi-camusta-bir-u-net)
4. [Durak 3: Simpson yöntemiyle otomatik EF ve uzmanla uyum](#durak-3-simpson-yöntemiyle-otomatik-ef-ve-uzmanla-uyum)
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

## Durak 1: Mini proje: EfficientNet-B0 ile az sayıda etiketli görüntüden KMP sınıflandırma

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-04/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 4, 1-4. bölümler*

ImageNet'in bir milyondan fazla fotoğrafıyla eğitilmiş bir ağ kenarları, dokuları ve biçimleri zaten tanır. Bu durakta EfficientNet-B0, ACDC'nin kardiyomiyopati grupları üzerinde iki yoldan yeniden kullanılır: Ağın öznitelikleri basit bir modele verilir ve ağın tamamına ince ayar yapılır. Ardından her gruptan yalnızca beş hasta tutulur ve sonucun, rastgele seçilen hastalara ne kadar bağlı olduğu görülür.

### Adım 1.1: Fotoğraflarla eğitilmiş bir ağın öznitelikleri

**Amaç.** Bu adımda her kesit EfficientNet-B0'ın 1.280 özniteliğiyle tarif edilir ve üç grup bu özniteliklerden basit bir modelle öğrenilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: ACDC'nin kardiyomiyopati gruplarındaki sine MR kesitlerinde, yalnızca fotoğraflarla
eğitilmiş bir ağın özniteliklerinin normal kalpleri, dilate kardiyomiyopatiyi ve hipertrofik
kardiyomiyopatiyi ne kadar iyi ayırdığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'deki 90 hastanın her birinin ortadaki üç
kısa eksen kesitinden oluşan 270 sine MR kesitini tutar. Her satır bir kesittir: "hasta" sütunu
hastayı, "grup" hastanın grubunu ("NOR", "DCM" ya da "HCM"), "küme" ise hastanın kümesini verir
("eğitim", her gruptan 15 olmak üzere 45 hasta; "doğrulama", 15 hasta; "test", 30 hasta). "görüntü"
sütununun her hücresi, kesiti fotoğraflarla eğitilmiş bir ağa uygun biçimde tutar: 128 × 128
piksellik üç renk kanalı (diyastol sonu karesi, sistol sonu karesi ve ikisinin ortalaması),
ImageNet'in ortalamaları ve standart sapmalarıyla normalleştirilmiştir.
Görev: EfficientNet-B0'ı ImageNet ağırlıklarıyla ve değerlendirme modunda kullan. Bütün kesitlerin
görüntülerini gradyan kaydetmeden, 32'şerlik gruplar hâlinde ağdan geçir ve ağın son katmanından
önceki ortalama havuzlamanın çıktısını, yani kesit başına 1.280 sayıdan oluşan öznitelikleri al.
Öznitelikleri eğitim kesitleriyle standartlaştır ve eğitim kesitlerinde bir lojistik regresyon eğit.
Ardından test kesitleri için üç grubun olasılıklarını hesapla, bu olasılıkların her test hastasının
üç kesiti üzerinden ortalamasını al ve ortalaması en büyük grubu hastanın kararı olarak seç.
Kısıtlar: Yalnızca bu tabloyu kullan. Ağ için yalnızca bu bilgisayarda hazır bulunan EfficientNet-B0
ImageNet ağırlıklarını kullan; yeni bir indirme gerekmez. Kod dosya okumamalı, internetten bir şey
indirmemeli ve program kurmamalıdır.
Çıktı: 30 test hastasından kararı kendi grubuyla aynı olanların oranını üç ondalık basamakla yazdır
ve "cevap" adıyla sakla.
Test: Öznitelikler 270 satır ve 1.280 sütundan oluşan bir tablo olmalı ve 30 test hastası bulunmalı.
```

**Beklenen sonuç:** "cevap" = 0,867

### Adım 1.2: Ağın tamamına ince ayar

**Amaç.** Bu adımda EfficientNet-B0'ın bütün katmanları, ImageNet ağırlıklarından başlayarak kesitlere uyarlanır. Eğitim yaklaşık bir dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Fotoğraflarla eğitilmiş bir ağın bütün katmanlarını ACDC'nin sine MR kesitlerine
uyarlamanın, üç grubu yalnızca ağın özniteliklerinden daha iyi ayırıp ayırmadığını öğrenmek
istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'deki 90 hastanın her birinin ortadaki üç
kısa eksen kesitinden oluşan 270 sine MR kesitini tutar. Her satır bir kesittir: "hasta" sütunu
hastayı, "grup" hastanın grubunu ("NOR", "DCM" ya da "HCM"), "küme" ise hastanın kümesini verir
("eğitim", her gruptan 15 olmak üzere 45 hasta; "doğrulama", 15 hasta; "test", 30 hasta). "görüntü"
sütununun her hücresi, kesiti fotoğraflarla eğitilmiş bir ağa uygun biçimde tutar: 128 × 128
piksellik üç renk kanalı (diyastol sonu karesi, sistol sonu karesi ve ikisinin ortalaması),
ImageNet'in ortalamaları ve standart sapmalarıyla normalleştirilmiştir.
Görev: EfficientNet-B0'ı ImageNet ağırlıklarıyla kur ve son katmanını, 0,3 oranında dropout'un
ardından gelen ve her grup için bir çıktı veren üç çıktılı yeni bir doğrusal katmanla değiştir. Ağın
tamamını eğitim kesitlerinde 15 epoch boyunca, 16 kesitlik karıştırılmış gruplarla, 0,001 öğrenme
hızıyla ve çapraz entropi kaybıyla eğit. Veri çoğaltma için her kesit grubunu rastgele bir çeyrek
tur döndür. Her epoch'un sonunda, onlardan öğrenmeden doğrulama kesitlerindeki kaybı ölç ve bu
kaybın en düşük olduğu epoch'un ağırlıklarını sakla. Rastgele seçimler her çalıştırmada aynı olsun;
bunun için başlangıç değeri olarak 2026 sayısını kullan. Ardından her test hastası için bir kliniğin
yapacağı gibi karar ver: Üç grubun olasılıklarının hastanın üç kesiti üzerinden ortalamasını al ve
ortalaması en büyük grubu seç.
Kısıtlar: Yalnızca bu tabloyu kullan. Ağ için yalnızca bu bilgisayarda hazır bulunan EfficientNet-B0
ImageNet ağırlıklarını kullan; yeni bir indirme gerekmez. Kod dosya okumamalı, internetten bir şey
indirmemeli ve program kurmamalıdır.
Çıktı: Doğrulama kaybının en düşük olduğu epoch'u ve 30 test hastasından kararı kendi grubuyla aynı
olanların oranını üç ondalık basamakla yazdır; oranı "cevap" adıyla sakla.
Test: Saklanan ağırlıklar yüklendikten sonra doğrulama kaybı yine en düşük değerini vermeli.
```

**Beklenen sonuç:** "cevap" = 0,967

### Adım 1.3: Her gruptan beş hasta

**Amaç.** Bu adımda az sayıda hastadan elde edilen bir sonucun, seçilen hastalara ne kadar bağlı olduğu görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Her gruptan yalnızca beş hastayla elde edilen bir sonucun, rastgele seçilen hastalara ne
kadar bağlı olduğunu görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; ACDC'deki 90 hastanın her birinin ortadaki üç
kısa eksen kesitinden oluşan 270 sine MR kesitini tutar. Her satır bir kesittir: "hasta" sütunu
hastayı, "grup" hastanın grubunu ("NOR", "DCM" ya da "HCM"), "küme" ise hastanın kümesini verir
("eğitim", her gruptan 15 olmak üzere 45 hasta; "doğrulama", 15 hasta; "test", 30 hasta). "ö1"den
"ö1280"e kadar olan öteki 1.280 sütun, kesitin özniteliklerini, yani ImageNet fotoğraflarıyla
eğitilmiş EfficientNet-B0'ın son katmanından önceki ortalama havuzlamanın çıktısını tutar.
Görev: Eğitim kümesinin her grubundan rastgele beşer hasta seç ve bu seçimi beş kez tekrarla.
Rastgele seçimler her çalıştırmada aynı olsun; bunun için başlangıç değeri olarak 2026 sayısını
kullan. Her seçimde öznitelikleri yalnızca seçilen 15 hastanın kesitleriyle standartlaştır ve bu
kesitlerde bir lojistik regresyon eğit. Ardından 30 test hastasındaki doğruluğu, her hasta için tek
bir kararla hesapla: Kararı, hastanın üç kesiti üzerinden ortalama olasılığı en büyük olan grup
belirler.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Beş doğruluğu yazdır; ortalamalarını üç ondalık basamakla "cevap" adıyla sakla.
Test: Her seçimde, her gruptan beşer olmak üzere 15 farklı hasta bulunmalı.
```

**Beklenen sonuç:** "cevap" = 0,62

## Durak 2: Pixel-wise segmentasyon eğitimi: CAMUS'ta bir U-Net

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-04/ders.html#stop-2) · Python yolunda aynı sonuç: 5-7. bölümler*

Bir segmentasyon ağı her piksele bir etiket verir. Bu durakta önce Dice katsayısı, birkaç piksel kaydırılmış bir sınır üzerinde elle hesaplanır. Ardından küçük bir U-Net, sol ventrikül kavitesini CAMUS'un 800 eğitim karesinden öğrenir ve 50 test hastasının 200 karesinde görüntüye ve faza göre değerlendirilir.

### Adım 2.1: Elle Dice katsayısı

**Amaç.** Bu adımda bir sınırın küçük bir kaymasının Dice katsayısını ne kadar düşürdüğü görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir sınırın küçük bir kaymasının, iki sınır arasındaki uyumun olağan ölçütü olan Dice
katsayısını ne kadar düşürdüğünü görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında 96 satır ve 96 sütunluk bir tablo var: CAMUS'taki 201
numaralı hastanın apikal dört boşluk görüntüsünün diyastol sonu karesinde uzmanın çizdiği sol
ventrikül kavitesidir; kare 96 × 96 piksele küçültülmüştür. Her hücre bir pikseldir: Kavitenin
içindeki pikseller 1, dışındakiler 0'dır.
Görev: Kaviteyi 3 piksel sağa kaydır, yani her pikseli 3 sütun sağa taşı. Özgün ve kaydırılmış
kavitenin piksellerini ve ikisinin ortak piksellerini say. Dice katsayısını hesapla: Ortak
piksellerin iki katı, iki sayının toplamına bölünür.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Üç sayıyı yazdır; Dice katsayısını üç ondalık basamakla "cevap" adıyla sakla.
Test: Kavitenin kaydırılmamış kendisiyle Dice katsayısı 1 olmalı.
```

**Beklenen sonuç:** "cevap" = 0,877

### Adım 2.2: U-Net'i eğitmek

**Amaç.** Bu adımda sol ventrikül kavitesini çizen küçük bir U-Net eğitilir ve ağ, hiç görmediği hastaların karelerinde ölçülür. Eğitim yaklaşık üç dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: CAMUS'un apikal ekokardiyogramlarında sol ventrikül kavitesinin sınırını çizen küçük bir
U-Net eğitmek ve bu ağı hiç görmediği hastalarda ölçmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'un 1.200 karesini, yani 300 hastanın
apikal iki boşluk ve dört boşluk görüntülerinin diyastol sonu ve sistol sonu karelerini tutar. Her
satır bir karedir: "hasta" sütunu hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"), "faz" fazı ("ED"
ya da "ES"), "küme" ise hastanın kümesini verir ("eğitim", 200 hasta; "doğrulama", 50 hasta; "test",
50 hasta). "kare" sütununun her hücresi kareyi değerleri 0 ile 1 arasında olan 96 × 96 piksellik bir
görüntü olarak, "kavite" sütununun her hücresi ise uzmanın çizdiği sol ventrikül kavitesini aynı
boyutta tutar: Kavitenin içindeki pikseller 1, dışındakiler 0'dır.
Görev: Her piksele, biri kavite, biri kavite dışı için olmak üzere iki skor veren küçük bir U-Net
kur. Ağda atlama bağlantılarıyla üç düzey aşağı, bir dar boğaz ve üç düzey yukarı bulunur. Her
düzeyde görüntünün boyutunu koruyan 3 × 3 çekirdekli iki evrişim vardır ve her evrişimin ardından
batch normalizasyonu ile ReLU gelir. Aşağı inerken 2 × 2 maksimum havuzlama görüntüyü yarıya
indirir; yukarı çıkarken 2 × 2'lik ters evrişim görüntüyü iki kat büyütür ve sonuç, aşağı inerken
aynı düzeyde elde edilen çıktıyla birleştirilir. İlk düzeyde 8 kanal vardır ve kanal sayısı aşağı
inilen her düzeyde iki katına çıkarak dar boğazda 64'e ulaşır. Son bir 1 × 1 evrişim iki skoru
verir. Ağı eğitim karelerinde 15 epoch boyunca, 16 karelik karıştırılmış gruplarla eğit. Kayıp,
çapraz entropi ile yumuşak Dice kaybının toplamıdır; yumuşak Dice kaybı, kavite olasılıklarından
hesaplanan Dice katsayısının 1'den çıkarılmasıyla bulunur. En yüksek değeri 0,003 olan tek döngülü
bir öğrenme hızı kullan. Her epoch'un sonunda doğrulama karelerinin ortalama Dice katsayısını
hesapla ve bu değerin en yüksek olduğu epoch'un ağırlıklarını sakla. Rastgele seçimler her
çalıştırmada aynı olsun; bunun için başlangıç değeri olarak 2026 sayısını kullan. Ardından test
karelerinin her pikselinde kavite olasılığını hesapla, olasılığı 0,5'te eşikle ve her test karesinin
Dice katsayısını uzmanın çizdiği kaviteye göre hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitilebilir parametre sayısını yazdır; 200 test karesinin ortalama Dice katsayısını üç
ondalık basamakla "cevap" adıyla sakla.
Test: 800 eğitim karesi ve 200 test karesi bulunmalı ve ağın 121.394 eğitilebilir parametresi
olmalı.
```

**Beklenen sonuç:** "cevap" = 0,924

### Adım 2.3: Görüntü ve faza göre Dice katsayısı

**Amaç.** Bu adımda, bir ekokardiyografi laboratuvarının soracağı gibi, ağın sınırları en kötü nerede çizdiği bulunur. Veri hücresi dersin U-Net'ini bir kez eğitir; bu yaklaşık üç dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir ekokardiyografi laboratuvarının soracağı gibi, bir U-Net'in sol ventrikül kavitesini
hangi görüntüde ve hangi fazda en kötü çizdiğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'un 200 test karesini, yani 50 hastanın
apikal iki boşluk ve dört boşluk görüntülerinin diyastol sonu ve sistol sonu karelerini tutar. Her
satır bir karedir: "hasta" sütunu hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"), "faz" ise fazı
("ED" ya da "ES") verir. "olasılık" sütununun her hücresi, 96 × 96 piksellik karenin her pikseli
için bir U-Net'in verdiği sol ventrikül kavitesi olasılığını 0 ile 1 arasında bir sayı olarak tutar.
"kavite" sütununun her hücresi ise uzmanın çizdiği kaviteyi aynı boyutta tutar: Kavitenin içindeki
pikseller 1, dışındakiler 0'dır.
Görev: Her karenin olasılığını 0,5'te eşikle ve karenin Dice katsayısını uzmanın çizdiği kaviteye
göre hesapla: Ortak piksellerin iki katı, iki kavitenin piksellerinin toplamına bölünür. Kareleri
görüntüye ve faza göre grupla ve dört grubun, yani 2CH ED, 2CH ES, 4CH ED ve 4CH ES gruplarının kare
sayısını ve ortalama Dice katsayısını gösteren küçük bir tablo yazdır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Dört ortalamanın en düşüğünü üç ondalık basamakla "cevap" adıyla sakla.
Test: Dört grubun her birinde 50 kare bulunmalı ve dört ortalamanın ortalaması 200 karenin ortalama
Dice katsayısına eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 0,908

## Durak 3: Simpson yöntemiyle otomatik EF ve uzmanla uyum

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-04/ders.html#stop-3) · Python yolunda aynı sonuç: 8. ve 9. bölümler*

Sınırlar, bir ekokardiyografi laboratuvarında olduğu gibi biplan disk yöntemiyle sayılara dönüşür. Bu durakta 201 numaralı hastanın hacimleri ve ejeksiyon fraksiyonu (EF) uzman sınırlarından hesaplanır, ağ 50 test hastasında bir Bland-Altman analiziyle uzmanla karşılaştırılır ve vaka, disklerin kalınlığı için başka bir kuralla yeniden ölçülür.

### Adım 3.1: Disk yöntemiyle 201 numaralı hasta

**Amaç.** Bu adımda haftanın vakası, CAMUS'un referansında olduğu gibi uzmanın sınırlarından ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: CAMUS'taki 201 numaralı hastanın diyastol sonu ve sistol sonu hacimlerini ve ejeksiyon
fraksiyonunu, CAMUS'un referansındaki gibi uzman sınırlarından biplan disk yöntemiyle hesaplamak
istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'taki 201 numaralı hastada sol ventrikül
kavitesinin dört uzman sınırına uygulanan disk yönteminin disklerini tutar. Bu sınırlar apikal iki
boşluk (2CH) ve dört boşluk (4CH) görüntülerinin diyastol sonu (ED) ve sistol sonu (ES)
karelerindedir. Her sınır, mitral halkadan apekse uzanan uzun eksenine dik 20 diske bölünmüştür. Her
satır bir disktir: "görüntü" ve "faz" sütunları sınırı, "disk" diskin 1'den 20'ye kadar numarasını,
"çap" diskin çapını mm olarak, "uzun eksen" ise sınırın uzun ekseninin uzunluğunu mm olarak verir;
uzun eksen, sınırın 20 diskinde de aynıdır. Çaplar ve uzunluklar, karelerin özgün boyutunda ve
pikselin gerçek büyüklüğüyle ölçülmüştür.
Görev: Her hacmi biplan disk yöntemiyle, V = π/4 × Σ (a_i × b_i) × h formülüyle hesapla; burada a_i,
2CH sınırındaki i. diskin çapı, b_i aynı fazın 4CH sınırındaki aynı diskin çapı, h ise bir diskin
kalınlığıdır. CAMUS'un referansındaki gibi iki faz için de tek bir kalınlık kullan; bu kalınlık,
dört sınırın uzun eksenlerinden en uzununun 20'ye bölümüdür. mm³'ü mL'ye çevirmek için 1.000'e böl,
her hacmi tam sayı mL'ye yuvarla ve EF'yi yuvarlanmış hacimlerden (EDV − ESV)/EDV × 100 formülüyle
hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: EDV ve ESV değerlerini mL olarak yazdır; EF'yi yüzde olarak bir ondalık basamakla "cevap"
adıyla sakla.
Test: EDV, ESV'den büyük olmalı ve 50 ile 300 mL arasında bulunmalı.
```

**Beklenen sonuç:** "cevap" = 42,1

### Adım 3.2: Ağın uzmanla uyumu

**Amaç.** Bu adımda otomatik EF, bir laboratuvarın kullanmadan önce yapacağı gibi 50 test hastasında uzmanınkiyle karşılaştırılır. Dersin U-Net'i henüz bellekte değilse veri hücresi önce onu eğitir; bu yaklaşık üç dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Otomatik bir ejeksiyon fraksiyonu kullanılmadan önce, bir laboratuvarın yapacağı gibi, onu
CAMUS'un 50 test hastasında bir Bland-Altman analiziyle uzmanınkiyle karşılaştırmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'un 50 test hastasını tutar. Her satır
bir hastadır: "hasta" sütunu hastayı, "uzman EF" uzmanın çizdiği sınırlardan, "ağ EF" ise bir
U-Net'in çizdiği sınırlardan elde edilen ejeksiyon fraksiyonunu verir; ikisi de yüzde olarak ve
biplan disk yöntemiyle ölçülmüştür.
Görev: Her hasta için EF farkını (ağ eksi uzman) hesapla; ardından farkların ortalamasını, standart
sapmasını ve uyum sınırlarını, yani ortalama ± 1,96 standart sapmayı bul. Bir Bland-Altman grafiği
çiz: Farkı iki EF'nin ortalamasına karşı göster; ortalama fark ve iki uyum sınırı için yatay
çizgiler ekle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Standart sapmayı ve iki uyum sınırını yazdır; ortalama farkı puan cinsinden iki ondalık
basamakla "cevap" adıyla sakla.
Test: 50 hasta bulunmalı ve patient0201 hastasının uzman EF'si yüzde 42,1 olmalı.
```

**Beklenen sonuç:** "cevap" = −4,24

### Adım 3.3: Disklerin kalınlığı için başka bir kural

**Amaç.** Bu adımda bir sınırın değil, yazılımın bir kuralının vakanın EF'sini ne kadar değiştirdiği görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bir sınırın değil, disklerin kalınlığı için seçilen kuralın 201 numaralı hastanın ejeksiyon
fraksiyonunu ne kadar değiştirdiğini görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'taki 201 numaralı hastada sol ventrikül
kavitesinin dört uzman sınırına uygulanan disk yönteminin disklerini tutar. Bu sınırlar apikal iki
boşluk (2CH) ve dört boşluk (4CH) görüntülerinin diyastol sonu (ED) ve sistol sonu (ES)
karelerindedir. Her sınır, mitral halkadan apekse uzanan uzun eksenine dik 20 diske bölünmüştür. Her
satır bir disktir: "görüntü" ve "faz" sütunları sınırı, "disk" diskin 1'den 20'ye kadar numarasını,
"çap" diskin çapını mm olarak, "uzun eksen" ise sınırın uzun ekseninin uzunluğunu mm olarak verir;
uzun eksen, sınırın 20 diskinde de aynıdır. Çaplar ve uzunluklar, karelerin özgün boyutunda ve
pikselin gerçek büyüklüğüyle ölçülmüştür.
Görev: Her hacmi biplan disk yöntemiyle, V = π/4 × Σ (a_i × b_i) × h formülüyle hesapla; burada a_i,
2CH sınırındaki i. diskin çapı, b_i aynı fazın 4CH sınırındaki aynı diskin çapı, h ise bir diskin
kalınlığıdır. Bu kez her faz için ayrı bir kalınlık kullan; bu kalınlık, o fazın iki sınırının uzun
eksenlerinden daha uzun olanının 20'ye bölümüdür. mm³'ü mL'ye çevirmek için 1.000'e böl, her hacmi
tam sayı mL'ye yuvarla ve EF'yi yuvarlanmış hacimlerden (EDV − ESV)/EDV × 100 formülüyle hesapla.
Karşılaştırma için EDV'yi, dört sınırın uzun eksenlerinden en uzunundan gelen tek bir kalınlıkla da
hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: EDV ve ESV değerlerini mL olarak yazdır; EF'yi yüzde olarak bir ondalık basamakla "cevap"
adıyla sakla.
Test: İki EDV eşit olmalı; çünkü diyastol sonunda iki kural da aynı uzun ekseni kullanır.
```

**Beklenen sonuç:** "cevap" = 50,3

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

### Bir ölçüm hattını denetletmek

```text
Aşağıdaki kod ekokardiyogramlardan hacimleri ve bir ejeksiyon fraksiyonunu ölçmektedir. Altı noktayı
denetle. Eğitim, doğrulama ve test kümeleri hastaya göre mi ayrılmış? Maskeler yeni etiketler
oluşturmadan, en yakın etiketle ya da olasılıklar üzerinden mi yeniden boyutlandırılmış? Hacimlerde
bir pikselin mm cinsinden gerçek büyüklüğü kullanılmış mı? Dice katsayısı görüntüye ve faza göre de
verilmiş mi? Hacimler hangi kuralla ve disklerin hangi kalınlığıyla hesaplanmış? Uyum yalnızca
korelasyonla değil, ortalama fark ve uyum sınırlarıyla mı bildirilmiş? Her sorun için ilgili satırı
göster, nedenini açıkla ve düzeltilmiş kodu ver.

[kodu buraya yapıştırın]
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter Notebook'un 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: U-Net'i eğitmek ve sınırlarını ölçmek

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: CAMUS ekokardiyogramlarında sol ventrikül kavitesinin sınırını çizen bir U-Net eğitmek ve
ağın sınırları nerede daha kötü çizdiğini görüntüye, faza ve görüntü kalitesine göre görmek
istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'un 1.200 karesini, yani 300 hastanın
apikal iki boşluk ve dört boşluk görüntülerinin diyastol sonu ve sistol sonu karelerini tutar. Her
satır bir karedir: "hasta" sütunu hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"), "faz" fazı ("ED"
ya da "ES"), "küme" hastanın kümesini ("eğitim", 200 hasta; "doğrulama", 50 hasta; "test", 50
hasta), "görüntü kalitesi" ise yazarların hastanın bu görüntüsüne verdiği kaliteyi ("iyi", "orta" ya
da "kötü") verir. "kare" sütununun her hücresi kareyi değerleri 0 ile 1 arasında olan 96 × 96
piksellik bir görüntü olarak, "kavite" sütununun her hücresi ise uzmanın çizdiği sol ventrikül
kavitesini aynı boyutta tutar: Kavitenin içindeki pikseller 1, dışındakiler 0'dır.
Görev: Her piksele, biri kavite, biri kavite dışı için olmak üzere iki skor veren küçük bir U-Net
kur. Ağda atlama bağlantılarıyla üç düzey aşağı, bir dar boğaz ve üç düzey yukarı bulunur. Her
düzeyde görüntünün boyutunu koruyan 3 × 3 çekirdekli iki evrişim vardır ve her evrişimin ardından
batch normalizasyonu ile ReLU gelir. Aşağı inerken 2 × 2 maksimum havuzlama görüntüyü yarıya
indirir; yukarı çıkarken 2 × 2'lik ters evrişim görüntüyü iki kat büyütür ve sonuç, aşağı inerken
aynı düzeyde elde edilen çıktıyla birleştirilir. İlk düzeyde 8 kanal vardır ve kanal sayısı aşağı
inilen her düzeyde iki katına çıkarak dar boğazda 64'e ulaşır. Son bir 1 × 1 evrişim iki skoru
verir. Ağı eğitim karelerinde 15 epoch boyunca, 16 karelik karıştırılmış gruplarla eğit. Kayıp,
çapraz entropi ile yumuşak Dice kaybının toplamıdır; yumuşak Dice kaybı, kavite olasılıklarından
hesaplanan Dice katsayısının 1'den çıkarılmasıyla bulunur. En yüksek değeri 0,003 olan tek döngülü
bir öğrenme hızı kullan. Her epoch'un sonunda doğrulama karelerinin ortalama Dice katsayısını
hesapla ve bu değerin en yüksek olduğu epoch'un ağırlıklarını sakla. Rastgele seçimler her
çalıştırmada aynı olsun; bunun için başlangıç değeri olarak 2026 sayısını kullan. Ardından test
karelerindeki kavite olasılığını 0,5'te eşikle ve her test karesinin Dice katsayısını uzmanın
çizdiği kaviteye göre hesapla. Ortalama Dice katsayısını görüntüye ve faza göre ve görüntü
kalitesine göre bildir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Görüntü ve faza göre ortalama Dice katsayısını gösteren bir tablo ile görüntü kalitesine göre
ikinci bir tablo göster; 200 test karesinin ortalama Dice katsayısını üç ondalık basamakla "cevap"
adıyla sakla.
Test: Görüntü ve fazın dört grubunun her birinde 50 test karesi bulunmalı ve 200 test karesinin
ortalama Dice katsayısı 0,85 ile 0,97 arasında olmalı.
```

### Adım 2: Hacimler, EF ve Bland-Altman

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Otomatik hacimler ve otomatik bir ejeksiyon fraksiyonu kullanılmadan önce üçünü de CAMUS'un
50 test hastasında uzmanınkilerle karşılaştırmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'un 50 test hastasını tutar. Her satır
bir hastadır: "hasta" sütunu hastayı verir; "uzman EDV" ve "ağ EDV" diyastol sonu hacmini, "uzman
ESV" ve "ağ ESV" sistol sonu hacmini mL olarak, "uzman EF" ve "ağ EF" ise ejeksiyon fraksiyonunu
yüzde olarak verir. Uzmanın değerleri uzmanın çizdiği sınırlardan, ağın değerleri ise bir U-Net'in
çizdiği sınırlardan gelir ve hepsi biplan disk yöntemiyle ölçülmüştür.
Görev: Üç ölçümün, yani EDV, ESV ve EF'nin her biri için her hastadaki farkı (ağ eksi uzman)
hesapla; ardından ortalama farkı, farkların standart sapmasını ve uyum sınırlarını, yani ortalama ±
1,96 standart sapmayı bul. Her ölçüm için bir Bland-Altman grafiği çiz: Farkı iki değerin
ortalamasına karşı göster; ortalama fark ve iki uyum sınırı için yatay çizgiler ekle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her ölçüm için bir satır ve ortalama fark, standart sapma, alt sınır ve üst sınır sütunları
bulunan bir tablo ile üç Bland-Altman grafiğini göster; EF'nin ortalama farkını iki ondalık
basamakla "cevap" adıyla sakla.
Test: 50 hasta bulunmalı ve patient0201 hastasının uzman EF'si yüzde 42,1 olmalı.
```

### Adım 3: EF aralıkları

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: 50 test hastasının kaçında ağın ve uzmanın ejeksiyon fraksiyonunu aynı klinik aralığa
yerleştirdiğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'un 50 test hastasını tutar. Her satır
bir hastadır: "hasta" sütunu hastayı verir; "uzman EDV" ve "ağ EDV" diyastol sonu hacmini, "uzman
ESV" ve "ağ ESV" sistol sonu hacmini mL olarak, "uzman EF" ve "ağ EF" ise ejeksiyon fraksiyonunu
yüzde olarak verir. Uzmanın değerleri uzmanın çizdiği sınırlardan, ağın değerleri ise bir U-Net'in
çizdiği sınırlardan gelir ve hepsi biplan disk yöntemiyle ölçülmüştür.
Görev: Uzmanın ve ağın her EF değerini üç aralıktan birine yerleştir. Birinci aralık yüzde 40 ve
altını, ikinci aralık yüzde 40'ın üzerini ve yüzde 50'nin altını, üçüncü aralık ise yüzde 50 ve
üzerini kapsar. Satırlarda uzmanın, sütunlarda ağın aralığı aralıkların sırasıyla yer alacak biçimde
bir çapraz tablo oluştur ve tablonun köşegenindeki hastaları say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Çapraz tabloyu göster ve köşegenindeki hasta sayısını "cevap" adıyla sakla.
Test: Çapraz tablonun toplamı 50 hasta olmalı.
```

### Adım 4: En büyük hatalar

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Otomatik ejeksiyon fraksiyonu uzmanınkinden en çok ayrılan test hastalarında, ağın nerede
yanıldığını değerlendirmek için kareleri ve iki sınırı görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; CAMUS'un 50 test hastasının her birinden dört
kare olmak üzere 200 test karesini tutar. Her satır bir karedir: "hasta" sütunu hastayı, "görüntü"
görüntüyü ("2CH" ya da "4CH"), "faz" fazı ("ED" ya da "ES"), "görüntü kalitesi" ise görüntünün
kalitesini ("iyi", "orta" ya da "kötü") verir. "kare" sütununun her hücresi kareyi 96 × 96 piksellik
bir görüntü olarak tutar; "uzman kavitesi" ve "ağ kavitesi" sütunları ise uzmanın ve bir U-Net'in
çizdiği sol ventrikül kavitesini aynı boyutta tutar: Kavitenin içindeki pikseller 1, dışındakiler
0'dır. "uzman EF" ve "ağ EF" sütunları hastanın ejeksiyon fraksiyonunu yüzde olarak verir; bu
değerler hastanın dört satırında da aynıdır.
Görev: İki EF arasındaki mutlak farkı en büyük olan üç hastayı bul. Her biri için dört kareyi, uzman
kavitesinin ve ağ kavitesinin sınırları kare üzerinde iki ayrı renkle çizilmiş olarak göster;
başlığa iki EF'yi ve görüntü kalitesini yaz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Üç hastanın her biri için dört kareden oluşan birer şekil göster; EF'deki en büyük mutlak
farkı puan cinsinden bir ondalık basamakla "cevap" adıyla sakla.
Test: Gösterilen üç hasta, EF'deki mutlak farkı en büyük olan üç hasta olmalı ve her şekilde dört
kare bulunmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
