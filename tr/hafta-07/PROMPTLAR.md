# Prompt kütüphanesi, 7. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[7. hafta](README.md) · [English](../../en/week-07/PROMPTS.md)

Bu kütüphanede, 7. haftanın uygulama duraklarındaki bütün prompt (istem) metinleri, yani Jupyter Notebook'un *Prompt ile uygulama* bölümlerindeki promptlar yer almaktadır. Her prompt, eğitimin prompt kartına göre yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub'da her kutunun köşesinde bir kopyalama düğmesi bulunmaktadır. Asistanın yazdığı kod, Jupyter Notebook'ta aynı numaralı promptun altındaki boş hücreye yapıştırılıp orada çalıştırılır.

Eğitimin hiçbir promptunda hasta verisi bulunmamaktadır ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir koşulda bir prompta, bulut tabanlı bir Jupyter Notebook'a ya da bir YZ sohbetine konmamalıdır.

1. [Bir promptla çalışmak](#bir-promptla-çalışmak)
2. [Durak 1: Ekokardiyografiye aktarım: Kalite kapısı ve mini proje](#durak-1-ekokardiyografiye-aktarım-kalite-kapısı-ve-mini-proje)
3. [Durak 2: Sentetik ve gerçek anjiyogramlarda darlıklar](#durak-2-sentetik-ve-gerçek-anjiyogramlarda-darlıklar)
4. [Durak 3: Evrişimli ağ, Vision Transformer ve hibrit model](#durak-3-evrişimli-ağ-vision-transformer-ve-hibrit-model)
5. [Kodu onarmak, açıklatmak ve denetlemek için promptlar](#kodu-onarmak-açıklatmak-ve-denetlemek-için-promptlar)
6. [Haftalık projenin promptları](#haftalık-projenin-promptları)

## Bir promptla çalışmak

| Adım | Ne yapılır? |
|---|---|
| 1. Okuyunuz | Jupyter Notebook'ta promptun amacını okuyunuz. |
| 2. Veriyi hazırlayınız | Bölümün başlangıç hücresini bir kez, ardından promptun altındaki veri hücresini çalıştırınız. Veri hücresi, promptun tarif ettiği "veri" tablosunu hazırlayıp göstermektedir. |
| 3. Kopyalayınız ve gönderiniz | Promptu kopyalayınız ve bir YZ asistanına gönderiniz: Google Colab'daki Gemini ya da başka bir tarayıcı sekmesindeki ChatGPT, Claude, Copilot veya Gemini. |
| 4. Çalıştırınız | Asistanın verdiği kodu veri hücresinin altındaki hücreye yapıştırınız ve çalıştırınız. |
| 5. Denetleyiniz | Kontrol hücresini çalıştırınız. Hücre sonucu *doğru* ya da *henüz değil* biçiminde bildirmekte ve "cevap" sonucunun değerini göstermektedir. |
| 6. Onarınız | Kontrol hücresi *henüz değil* sonucunu verirse onarım promptunu kodla birlikte gönderiniz. Sonuç yine yanlışsa, doğru sonucu veren *Hazır kod* hücresini çalıştırınız. |
| 7. Açıklatınız ve kaydediniz | Asistandan kodu sade bir dille açıklamasını isteyiniz; kullandığınız aracı, promptu ve neyin denetlendiğini YZ kullanım günlüğüne yazınız. |

## Durak 1: Ekokardiyografiye aktarım: Kalite kapısı ve mini proje

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-07/ders.html#stop-1) · Jupyter Notebook: «Durak 1 · Prompt ile uygulama», [Colab'da açınız](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-07/NB07_vision_transformer.ipynb#scrollTo=stop-1-prompt)*

Fotoğraflarla önceden eğitilmiş bir Vision Transformer olan ViT-B/16, CAMUS'un her ekokardiyografi karesini 768 sayıya dönüştürür; bir lojistik regresyon da bu sayılardan uzmanların hangi kareleri kötü bulduğunu öğrenir. Aynı kapı dört basit görüntü istatistiğiyle ve 4. haftanın evrişimli ağı EfficientNet-B0 ile de kurulur; Prompt 1.4, iki ağ arasındaki farktan 50 test hastasıyla ne kadar emin olunabileceğini sorar. Prompt 1.5 oturumun mini projesidir: Küçük bir Vision Transformer önce CIFAR-10 fotoğraflarını, ardından EchoNet-Dynamic ya da CAMUS ekokardiyografi kare çiftlerinden düşük ejeksiyon fraksiyonunu öğrenir.

### Prompt 1.1: Dört görüntü istatistiğinden bir kapı

**Amaç.** Bu promptla bir karenin parlaklığını, karşıtlığını ve keskinliğini anlatan dört sayıdan ilk kalite kapısı kurulur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Otomatik bir ejeksiyon fraksiyonu ölçümünden önce kalitesi kötü ekokardiyografi karelerini
işaretlemek istiyorum ve her karenin dört basit sayısıyla başlıyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan CAMUS'tan 600 apikal
ekokardiyografi karesini, yani 300 hastanın apikal iki boşluk ve dört boşluk görüntülerinin diyastol
sonu karelerini tutar. Her satır bir karedir: "küme" sütunu hastanın kümesini ("eğitim", 200 hasta;
"doğrulama", 50 hasta; "test", 50 hasta), "hasta" hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"),
"kalite" ise CAMUS uzmanlarının verdiği görüntü kalitesini ("iyi", "orta" ya da "kötü") verir.
"kare" sütununun her hücresi kareyi gri değerleri 0 ile 1 arasında olan 224 × 224 piksellik bir
görüntü olarak tutar.
Görev: Her kare için dört sayı hesapla: Gri değerlerinin ortalaması, standart sapmaları, dikey komşu
pikseller arasındaki mutlak farkın ortalaması ve karenin en parlak pikselinin yarısından daha parlak
piksellerin oranı. Hedef, kalitesi kötü olan kare için 1, öteki kareler için 0'dır. Öznitelikleri
eğitim kareleriyle standartlaştır. Eğitim karelerinde 0,001, 0,01, 0,1 ve 1 ters düzenlileştirme
güçlerinin her biriyle bir lojistik regresyon eğit; doğrulama karelerinde ROC eğrisinin altındaki
alanı (AUC) en büyük olanı seç ve test karelerinde bu modelin olasılıklarının AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Seçilen gücü, doğrulama ve test AUC değerlerini yazdır; test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: AUC 0 ile 1 arasında olmalı ve test kareleri son adımdan önce kullanılmamalı.
```

**Beklenen sonuç:** "cevap" = 0,704

### Prompt 1.2: Bir Vision Transformer'ın sınıf token'ı

**Amaç.** Bu promptla her kare, ImageNet ile önceden eğitilmiş ViT-B/16'nın sınıf token'ındaki 768 sayıyla tarif edilir ve kapı bu sayılarla kurulur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Milyonlarca fotoğraftan öğrenmiş ve hiç ekokardiyogram görmemiş bir Vision Transformer'ın,
kalitesi kötü kareleri işaretleyecek kadar iyi tarif edip edemediğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan CAMUS'tan 600 apikal
ekokardiyografi karesini, yani 300 hastanın apikal iki boşluk ve dört boşluk görüntülerinin diyastol
sonu karelerini tutar. Her satır bir karedir: "küme" sütunu hastanın kümesini ("eğitim", 200 hasta;
"doğrulama", 50 hasta; "test", 50 hasta), "hasta" hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"),
"kalite" ise CAMUS uzmanlarının verdiği görüntü kalitesini ("iyi", "orta" ya da "kötü") verir.
"kare" sütununun her hücresi kareyi gri değerleri 0 ile 1 arasında olan 224 × 224 piksellik bir
görüntü olarak tutar.
Görev: ImageNet ağırlıklarıyla Vision Transformer ViT-B/16'yı son katmanı olmadan kullan; böylece ağ
her kare için son katmanındaki sınıf token'ını, yani 768 sayıyı döndürür. Her kareyi ağa, üç renk
kanalında aynı gri değerleri taşıyan 224 × 224 piksellik bir görüntü olarak ve ImageNet'in
ortalaması ve standart sapmasıyla ölçeklenmiş biçimde ver: Üç kanaldan 0,485, 0,456 ve 0,406
değerlerini çıkar, kanalları 0,229, 0,224 ve 0,225 değerlerine böl. Kareleri ağdan 16'şarlık gruplar
hâlinde, değerlendirme modunda ve gradyan kaydetmeden geçir. Ardından 768 sayıyı kapının
öznitelikleri olarak kullan. Hedef, kalitesi kötü olan kare için 1, öteki kareler için 0'dır.
Öznitelikleri eğitim kareleriyle standartlaştır. Eğitim karelerinde 0,001, 0,01, 0,1 ve 1 ters
düzenlileştirme güçlerinin her biriyle bir lojistik regresyon eğit; doğrulama karelerinde ROC
eğrisinin altındaki alanı (AUC) en büyük olanı seç ve test karelerinde bu modelin olasılıklarının
AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Seçilen gücü, doğrulama ve test AUC değerlerini yazdır; test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Her kare 768 sayı vermeli ve AUC 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,862

### Prompt 1.3: Evrişimli bir ağın öznitelikleri

**Amaç.** Bu promptla aynı kapı, 4. haftanın ağı EfficientNet-B0'ın 1.280 özniteliğiyle kurulur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Ekokardiyografi kareleri için bir kalite kapısında öznitelik kaynağı olarak bir Vision
Transformer'ı 4. haftada kullanılan evrişimli ağla karşılaştırmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan CAMUS'tan 600 apikal
ekokardiyografi karesini, yani 300 hastanın apikal iki boşluk ve dört boşluk görüntülerinin diyastol
sonu karelerini tutar. Her satır bir karedir: "küme" sütunu hastanın kümesini ("eğitim", 200 hasta;
"doğrulama", 50 hasta; "test", 50 hasta), "hasta" hastayı, "görüntü" görüntüyü ("2CH" ya da "4CH"),
"kalite" ise CAMUS uzmanlarının verdiği görüntü kalitesini ("iyi", "orta" ya da "kötü") verir.
"kare" sütununun her hücresi kareyi gri değerleri 0 ile 1 arasında olan 224 × 224 piksellik bir
görüntü olarak tutar.
Görev: ImageNet ağırlıklarıyla evrişimli ağ EfficientNet-B0'ı son katmanı olmadan kullan; böylece ağ
her kare için ortalama havuzlamasının çıktısını, yani 1.280 sayıyı döndürür. Her kareyi ağa, üç renk
kanalında aynı gri değerleri taşıyan 224 × 224 piksellik bir görüntü olarak ve ImageNet'in
ortalaması ve standart sapmasıyla ölçeklenmiş biçimde ver: Üç kanaldan 0,485, 0,456 ve 0,406
değerlerini çıkar, kanalları 0,229, 0,224 ve 0,225 değerlerine böl. Kareleri ağdan 16'şarlık gruplar
hâlinde, değerlendirme modunda ve gradyan kaydetmeden geçir. Ardından 1.280 sayıyı kapının
öznitelikleri olarak kullan. Hedef, kalitesi kötü olan kare için 1, öteki kareler için 0'dır.
Öznitelikleri eğitim kareleriyle standartlaştır. Eğitim karelerinde 0,001, 0,01, 0,1 ve 1 ters
düzenlileştirme güçlerinin her biriyle bir lojistik regresyon eğit; doğrulama karelerinde ROC
eğrisinin altındaki alanı (AUC) en büyük olanı seç ve test karelerinde bu modelin olasılıklarının
AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Seçilen gücü, doğrulama ve test AUC değerlerini yazdır; test AUC değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Her kare 1.280 sayı vermeli ve AUC 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,782

### Prompt 1.4: Farktan ne kadar emin olabiliriz?

**Amaç.** Bu promptla 50 test hastası yerine koyarak tekrar tekrar çekilir ve Vision Transformer'ın ne sıklıkla daha iyi olduğu görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: 50 test hastasının karelerinde ölçülen iki ekokardiyografi kalite kapısı arasındaki farkın
başka hastalarda da geçerli olup olmayacağını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir apikal ekokardiyografi veri seti
olan CAMUS'un 100 test karesini, yani 50 hastanın apikal iki boşluk ve dört boşluk görüntülerinin
diyastol sonu karelerini tutar. Her satır bir karedir: "hasta" sütunu hastayı, "görüntü" görüntüyü
("2CH" ya da "4CH") verir; "kötü" sütunu CAMUS uzmanları görüntü kalitesini kötü olarak
değerlendirdiyse 1, değilse 0 değerini alır. "olasılık, ViT-B/16" ve "olasılık, EfficientNet-B0"
adlı iki sütun, dersin iki kalite kapısının verdiği kötü kalite olasılığını tutar; bu kapılar,
ImageNet ile önceden eğitilmiş iki ağın öznitelikleri üzerinde kurulmuş lojistik regresyonlardır.
Görev: İki olasılık sütununun "kötü" sütununa göre AUC değerini hesapla. Ardından 2.000 bootstrap
örneği çek: Her örnek 50 test hastası arasından yerine koyarak 50 hasta çeker ve çekilen her
hastanın iki karesini de tutar. Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle.
İki tür kareyi de içeren her örnekte iki kapının AUC değerini ve farkı (ViT-B/16 eksi
EfficientNet-B0) hesapla. Ortalama farkı, 2,5. ve 97,5. yüzdelikler arasındaki yüzde 95 aralığını ve
farkın 0'ın üstünde olduğu örneklerin oranını bildir.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki AUC değerini, ortalama farkı ve aralığını yazdır; oranı üç ondalık basamakla "cevap"
adıyla sakla.
Test: Oran 0 ile 1 arasında olmalı ve bir hastanın iki karesi her zaman birlikte çekilmeli.
```

**Beklenen sonuç:** "cevap" = 0,925

### Prompt 1.5: Mini proje: CIFAR-10'dan ekokardiyografiye küçük bir Vision Transformer

**Amaç.** Bu promptla küçük bir Vision Transformer önce CIFAR-10 fotoğraflarıyla eğitilir, ardından düşük ejeksiyon fraksiyonunu tanımak için ekokardiyografi kare çiftleriyle ince ayar yapılır ve yalnızca ekokardiyogramlarla eğitilen aynı ağla karşılaştırılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Önce gündelik fotoğraflardan öğrenmiş küçük bir Vision Transformer'ın, ekokardiyogramlarda
düşük ejeksiyon fraksiyonunu, yalnızca ekokardiyogramlardan öğrenen aynı ağdan daha iyi tanıyıp
tanımadığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta iki tür satırdan oluşan "veri" adlı bir tablo vardır. "kaynak" değeri
"CIFAR-10" olan satırlar, uçak, kedi ve gemi gibi on gündelik sınıftan oluşan açık bir veri seti
olan CIFAR-10'un 60.000 renkli fotoğrafıdır: "küme" sütunu "eğitim" (50.000 fotoğraf) ya da "test"
(10.000) değerini alır, "görüntü" sütununun her hücresi bir fotoğrafı 0 ile 255 arasındaki
sayılardan oluşan 32 × 32 × 3 boyutlu bir dizi olarak tutar, "sınıf" sütunu da fotoğrafın sınıfını 0
ile 9 arasında bir sayı olarak verir. "kaynak" değeri "eko" olan satırlar, iki açık veri seti olan
EchoNet-Dynamic ya da CAMUS'un apikal ekokardiyografi kare çiftleridir: "küme" sütunu "eğitim",
"doğrulama" ya da "test" değerini alır, "hasta" sütunu hastayı ya da videoyu verir, "görüntü"
sütununun her hücresi 32 × 32 × 3 boyutlu bir dizi tutar; bu dizinin üç kanalı, değerleri 0 ile 1
arasında olan diyastol sonu ve sistol sonu kareler ile değerleri −1 ile 1 arasında olan farklarıdır.
"düşük EF" sütunu ejeksiyon fraksiyonu yüzde 50'nin altındaysa 1, değilse 0 olur.
Görev: 32 × 32 piksellik renkli görüntüler için küçük bir Vision Transformer kur. Görüntüyü 4 × 4
piksellik 64 kareye böl ve her kareyi aynı öğrenilen doğrusal dönüşümle 64 sayıya dönüştür. 64
token'ın önüne 64 sayılık, öğrenilen bir sınıf token'ı koy ve öğrenilen konumları ekle: 65 yerin her
biri için, standart sapması 0,02 olan küçük rastgele sayılarla başlatılan 64 sayılık bir vektör.
Token'ları dört Transformer bloğundan geçir. Her blokta katman normalleştirmesini dört başlı öz
dikkat izler ve öz dikkatin çıktısı bloğun girdisine eklenir; ikinci bir katman normalleştirmesini
128 birimlik bir gizli katman ve GELU etkinleştirmesi içeren ileri beslemeli bir ağ izler ve bu ağın
çıktısı da yeniden eklenir. Sonda sınıf token'ını al, katman normalleştirmesi uygula ve on çıktılı,
yani on sınıfın puanlarını veren doğrusal bir katmandan geçir. Ağı eğitim kümesindeki CIFAR-10
satırlarıyla eğit: Fotoğrafları 255'e böl ve her renk kanalını eğitim fotoğraflarının ortalaması ve
standart sapmasıyla standartlaştır. 128 fotoğraflık karıştırılmış gruplarla, çapraz entropi kaybıyla
ve öğrenme hızı 0,001, ağırlık azaltması 0,05 olan AdamW optimizer'ı ile 5 epoch eğit. Her grubu her
yönde 4 piksele kadar rastgele kaydır, kenarları yansıtmayla doldur ve yarı olasılıkla soldan sağa
aynala. Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. 10.000 test fotoğrafında
doğruluğu hesapla. Ardından ekokardiyografi satırları için, her biri tek çıktılı, yani düşük
ejeksiyon fraksiyonunun logitini veren doğrusal bir katmanla biten iki ağ hazırla: Biri aynı yapıda
ve yeni rastgele ağırlıklarla, diğeri de CIFAR-10 ile eğitilen ağın, son katmanı tek çıktılı yeni
bir katmanla değiştirilmiş bir kopyası olsun. Ekokardiyografi görüntülerini oldukları gibi kullan.
Her ağı eğitim satırlarıyla, 32'lik karıştırılmış gruplarla, logit üzerinde ikili çapraz entropi
kaybıyla ve öğrenme hızı 0,0005 olan Adam optimizer'ı ile 30 epoch eğit. Her epoch'tan sonra
doğrulama satırlarında AUC değerini hesapla ve doğrulama AUC değeri en büyük olan epoch'un
ağırlıklarını sakla. Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle. İki ağın test
AUC değerini "düşük EF" sütununa göre hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: CIFAR-10 doğruluğunu ve iki ağın test AUC değerini yazdır; CIFAR-10 ile başlayan ağın test
AUC değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: CIFAR-10 doğruluğu, on sınıftan birinin şans eseri verdiği 0,1 değerinin belirgin biçimde
üstünde olmalı ve test satırları sona kadar kullanılmamalı.
```

**Beklenen sonuç:** "cevap": bilgisayardan bilgisayara ve ekokardiyogram kopyasına göre değişen, 0,5 ile 1,0 arasında bir test AUC değeri

## Durak 2: Sentetik ve gerçek anjiyogramlarda darlıklar

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-07/ders.html#stop-2) · Jupyter Notebook: «Durak 2 · Prompt ile uygulama», [Colab'da açınız](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-07/NB07_vision_transformer.ipynb#scrollTo=stop-2-prompt)*

Küçük bir evrişimli ağ, merkezi anlamlı bir darlıkta olan 64 × 64 piksellik yamaları tanımayı önce sanal kliniğin sentetik anjiyogramlarında öğrenir. Aynı ağ daha sonra hiçbir değişiklik yapılmadan ARCADE'in gerçek anjiyogramlarında sınanır ve son olarak ARCADE'in eğitim anjiyogramlarıyla yeniden eğitilir.

### Prompt 2.1: Sentetik anjiyogramlarda küçük bir evrişimli ağ

**Amaç.** Bu promptla sentetik anjiyogramların yamalarıyla küçük bir evrişimli ağ eğitilir ve ağ test hastalarının yamalarında ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Küçük bir ağın koroner anjiyogramlardan, bir görüntünün küçük bir karesinin merkezinin
anlamlı bir darlıkta olup olmadığını öğrenip öğrenemeyeceğini görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; sanal kliniğin sentetik koroner
anjiyogramlarından, 500 hastanın her biri için iki görüntüden (eğitim 300 hasta, doğrulama 100, test
100) kesilmiş 64 × 64 piksellik yamaları tutar. Her satır bir yamadır: "küme" sütunu yamanın
kümesini ("eğitim", "doğrulama" ya da "test"), "hasta" hastayı verir; "yama" sütununun her hücresi
yamayı gri değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü olarak tutar. "darlık"
sütunu, yamanın merkezi anlamlı bir darlığa (sol ana koroner arterde yüzde 50 ya da daha fazla,
öteki arterlerde yüzde 70 ya da daha fazla) 6 pikselden yakınsa 1, yama her darlıktan en az 48
piksel uzakta bir damarın üzerindeyse 0 değerini alır.
Görev: Her yamayı kendi içinde standartlaştır: Gri değerlerinin ortalamasını çıkar ve standart
sapmalarının 0,02 fazlasına böl. Tek kanallı, 64 × 64 piksellik bir yama için küçük bir evrişimli ağ
kur: Her biri 3 × 3 piksellik filtreler ve bir piksellik dolgu içeren bir evrişim (16, 32, 64 ve 64
filtre), batch normalizasyonu, ReLU ve 2 × 2 en büyük havuzlamadan oluşan dört blok; ardından her
kanalın konumları üzerinden ortalaması ve tek çıktılı, yani darlığın logitini veren bir doğrusal
katman. Ağı eğitim yamalarıyla 8 epoch boyunca, karıştırılmış 64 yamalık gruplar hâlinde, logit
üzerinde ikili çapraz entropi kaybıyla ve öğrenme hızı 0,001 olan Adam optimizasyon algoritmasıyla
eğit. Veri çoğaltma için her grubu rastgele bir çeyrek tur döndür ve yarı olasılıkla soldan sağa
aynala. Her epoch'un sonunda doğrulama yamalarının olasılıklarının AUC değerini hesapla; eğitimin
sonunda doğrulama AUC değeri en büyük olan epoch'un ağırlıklarını sakla. Sonucun tekrarlanabilmesi
için seed değerini 2026 olarak sabitle. Ardından test yamalarının olasılıklarını ve bunların
"darlık" sütununa göre AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitilebilir ağırlık sayısını ve her epoch'un doğrulama AUC değerini yazdır; test AUC
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Ağın 60.641 eğitilebilir ağırlığı olmalı ve test yamaları son adımdan önce kullanılmamalı.
```

**Beklenen sonuç:** "cevap" = 0,965

### Prompt 2.2: Aynı ağ gerçek anjiyogramlarda

**Amaç.** Bu promptla yalnızca sentetik anjiyogramlardan öğrenen bir ağ, ARCADE'in gerçek anjiyogramlarında sınanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Sentetik anjiyogramlarda darlık bulmayı öğrenen bir ağın hiç görmediği gerçek X ışınlı
anjiyogramlarda nasıl çalıştığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; iki kaynaktan gelen test yamalarını tutar:
Sanal kliniğin sentetik koroner anjiyogramlarından 1.700, açık bir veri seti olan ARCADE'in gerçek X
ışınlı anjiyogramlarından 3.088 yama; yamaların her biri 64 × 64 pikseldir. Her satır bir yamadır:
"kaynak" sütunu yamanın kaynağını ("sentetik" ya da "ARCADE") verir; "darlık" sütunu, merkezi bir
darlıkta olan yama için 1, her darlıktan uzakta bir damarın üzerindeki yama için 0 değerini alır.
"olasılık" sütunu, dersin yalnızca sentetik eğitim yamalarından öğrenen küçük evrişimli ağının
verdiği darlık olasılığını tutar.
Görev: Her kaynak için ayrı ayrı "olasılık" sütununun "darlık" sütununa göre ROC eğrisinin altındaki
alanını (AUC) ve farkı (sentetik eksi ARCADE) hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki AUC değerini ve farklarını yazdır; "ARCADE" kaynağının AUC değerini üç ondalık basamakla
"cevap" adıyla sakla.
Test: Her AUC yalnızca kendi kaynağının yamalarından hesaplanmalı.
```

**Beklenen sonuç:** "cevap" = 0,538

### Prompt 2.3: Gerçek anjiyogramlarla eğitim

**Amaç.** Bu promptla aynı küçük ağ, ARCADE'in eğitim anjiyogramlarının yamalarıyla eğitilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Küçük bir evrişimli ağın gerçek anjiyogramlardan öğrendiğinde gerçek koroner anjiyogramlarda
darlıkları ne kadar iyi bulduğunu öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan ARCADE'in darlık
kümesindeki 1.500 X ışınlı koroner anjiyogramdan (eğitim 1.000 anjiyogram, doğrulama 200, test 300)
kesilmiş 64 × 64 piksellik yamaları tutar. Her satır bir yamadır: "küme" sütunu yamanın kümesini
("eğitim", "doğrulama" ya da "test"), "anjiyogram" anjiyogramının numarasını verir; "yama" sütununun
her hücresi yamayı gri değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü olarak tutar.
"darlık" sütunu, yamanın merkezi uzmanların sınırını çizdiği bir darlığın merkezine 6 pikselden
yakınsa 1, yama sınırı çizilmiş her darlıktan ve görüntünün kenarından en az 48 piksel uzakta bir
damarın üzerindeyse 0 değerini alır.
Görev: Her yamayı kendi içinde standartlaştır: Gri değerlerinin ortalamasını çıkar ve standart
sapmalarının 0,02 fazlasına böl. Tek kanallı, 64 × 64 piksellik bir yama için küçük bir evrişimli ağ
kur: Her biri 3 × 3 piksellik filtreler ve bir piksellik dolgu içeren bir evrişim (16, 32, 64 ve 64
filtre), batch normalizasyonu, ReLU ve 2 × 2 en büyük havuzlamadan oluşan dört blok; ardından her
kanalın konumları üzerinden ortalaması ve tek çıktılı, yani darlığın logitini veren bir doğrusal
katman. Ağı eğitim yamalarıyla 8 epoch boyunca, karıştırılmış 64 yamalık gruplar hâlinde, logit
üzerinde ikili çapraz entropi kaybıyla ve öğrenme hızı 0,001 olan Adam optimizasyon algoritmasıyla
eğit. Veri çoğaltma için her grubu rastgele bir çeyrek tur döndür ve yarı olasılıkla soldan sağa
aynala. Her epoch'un sonunda doğrulama yamalarının olasılıklarının AUC değerini hesapla; eğitimin
sonunda doğrulama AUC değeri en büyük olan epoch'un ağırlıklarını sakla. Sonucun tekrarlanabilmesi
için seed değerini 2026 olarak sabitle. Ardından test yamalarının olasılıklarını ve bunların
"darlık" sütununa göre AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitilebilir ağırlık sayısını ve her epoch'un doğrulama AUC değerini yazdır; test AUC
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Ağın 60.641 eğitilebilir ağırlığı olmalı ve hiçbir test anjiyogramının yaması eğitimde
kullanılmamalı.
```

**Beklenen sonuç:** "cevap" = 0,81

## Durak 3: Evrişimli ağ, Vision Transformer ve hibrit model

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-07/ders.html#stop-3) · Jupyter Notebook: «Durak 3 · Prompt ile uygulama», [Colab'da açınız](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-07/NB07_vision_transformer.ipynb#scrollTo=stop-3-prompt)*

Küçük bir Vision Transformer ve evrişimle dikkati birleştiren hibrit bir model, ARCADE'in yamalarını 2. duraktaki evrişimli ağla aynı biçimde öğrenir; böylece üç model aynı test anjiyogramlarında karşılaştırılabilir. Son adım Vision Transformer'ın nereye baktığını sorar: Sınıf token'ının dikkatinin ne kadarı, darlığın bulunduğu yama merkezine düşmektedir?

### Prompt 3.1: Küçük bir Vision Transformer

**Amaç.** Bu promptla her yamayı 64 kareye bölen ve bu karelerin birbirine dikkat etmesini sağlayan küçük bir Vision Transformer ARCADE'in yamalarıyla eğitilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Gerçek koroner anjiyogramlarda darlık bulmak için aynı biçimde eğitilmiş küçük bir Vision
Transformer'ı küçük bir evrişimli ağla karşılaştırmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan ARCADE'in darlık
kümesindeki 1.500 X ışınlı koroner anjiyogramdan (eğitim 1.000 anjiyogram, doğrulama 200, test 300)
kesilmiş 64 × 64 piksellik yamaları tutar. Her satır bir yamadır: "küme" sütunu yamanın kümesini
("eğitim", "doğrulama" ya da "test"), "anjiyogram" anjiyogramının numarasını verir; "yama" sütununun
her hücresi yamayı gri değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü olarak tutar.
"darlık" sütunu, yamanın merkezi uzmanların sınırını çizdiği bir darlığın merkezine 6 pikselden
yakınsa 1, yama sınırı çizilmiş her darlıktan ve görüntünün kenarından en az 48 piksel uzakta bir
damarın üzerindeyse 0 değerini alır.
Görev: Her yamayı kendi içinde standartlaştır: Gri değerlerinin ortalamasını çıkar ve standart
sapmalarının 0,02 fazlasına böl. Tek kanallı, 64 × 64 piksellik bir yama için küçük bir Vision
Transformer kur. Yamayı 8 × 8 piksellik 64 kareye böl ve her kareyi öğrenilen aynı doğrusal
dönüşümle 64 sayıya dönüştür. 64 token'ın önüne 64 sayıdan oluşan öğrenilen bir sınıf token'ı koy ve
öğrenilen konumları ekle: 65 yerin her biri için, standart sapması 0,02 olan küçük rastgele
sayılarla başlayan 64 sayılık bir vektör. Token'ları dört Transformer bloğundan geçir. Her blokta
katman normalleştirmesini dört başlı öz dikkat izler ve öz dikkatin çıktısı bloğun girdisine
eklenir; ikinci bir katman normalleştirmesini 128 birimlik bir gizli katman ve GELU etkinleştirmesi
içeren ileri beslemeli bir ağ izler ve bu ağın çıktısı da yeniden eklenir. Sonunda sınıf token'ını
al, katman normalleştirmesi ve tek çıktılı, yani darlığın logitini veren bir doğrusal katman uygula.
Ağı eğitim yamalarıyla 8 epoch boyunca, karıştırılmış 64 yamalık gruplar hâlinde, logit üzerinde
ikili çapraz entropi kaybıyla ve öğrenme hızı 0,001 olan Adam optimizasyon algoritmasıyla eğit. Veri
çoğaltma için her grubu rastgele bir çeyrek tur döndür ve yarı olasılıkla soldan sağa aynala. Her
epoch'un sonunda doğrulama yamalarının olasılıklarının AUC değerini hesapla; eğitimin sonunda
doğrulama AUC değeri en büyük olan epoch'un ağırlıklarını sakla. Sonucun tekrarlanabilmesi için seed
değerini 2026 olarak sabitle. Ardından test yamalarının olasılıklarını ve bunların "darlık" sütununa
göre AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitilebilir ağırlık sayısını ve her epoch'un doğrulama AUC değerini yazdır; test AUC
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Ağın 142.465 eğitilebilir ağırlığı olmalı ve hiçbir test anjiyogramının yaması eğitimde
kullanılmamalı.
```

**Beklenen sonuç:** "cevap" = 0,93

### Prompt 3.2: Evrişim ve dikkatten oluşan hibrit bir model

**Amaç.** Bu promptla hibrit bir model eğitilir: Önce üç evrişim bloğu, ardından bunların çıktısındaki konumlar üzerinde iki Transformer bloğu.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Önce evrişimlerle küçük komşuluklara bakan, ardından yamanın parçalarını dikkatle birbirine
bağlayan bir ağın gerçek anjiyogramlarda darlıkları iki türün her birinden daha iyi bulup
bulmadığını öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan ARCADE'in darlık
kümesindeki 1.500 X ışınlı koroner anjiyogramdan (eğitim 1.000 anjiyogram, doğrulama 200, test 300)
kesilmiş 64 × 64 piksellik yamaları tutar. Her satır bir yamadır: "küme" sütunu yamanın kümesini
("eğitim", "doğrulama" ya da "test"), "anjiyogram" anjiyogramının numarasını verir; "yama" sütununun
her hücresi yamayı gri değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü olarak tutar.
"darlık" sütunu, yamanın merkezi uzmanların sınırını çizdiği bir darlığın merkezine 6 pikselden
yakınsa 1, yama sınırı çizilmiş her darlıktan ve görüntünün kenarından en az 48 piksel uzakta bir
damarın üzerindeyse 0 değerini alır.
Görev: Her yamayı kendi içinde standartlaştır: Gri değerlerinin ortalamasını çıkar ve standart
sapmalarının 0,02 fazlasına böl. Tek kanallı, 64 × 64 piksellik bir yama için hibrit bir ağ kur. Her
biri 3 × 3 piksellik filtreler ve bir piksellik dolgu içeren bir evrişim (16, 32 ve 64 filtre),
batch normalizasyonu, ReLU ve 2 × 2 en büyük havuzlamadan oluşan üç evrişim bloğu, yamayı 64 sayılık
8 × 8 konuma dönüştürür. Bu 64 konum küçük bir Transformer modelinin token'larıdır: Önlerine 64
sayıdan oluşan öğrenilen bir sınıf token'ı koy, 65 yer için standart sapması 0,02 olan küçük
rastgele sayılarla başlayan öğrenilen konumları ekle ve token'ları iki Transformer bloğundan geçir.
Her blokta katman normalleştirmesini dört başlı öz dikkat izler ve öz dikkatin çıktısı bloğun
girdisine eklenir; ikinci bir katman normalleştirmesini 128 birimlik bir gizli katman ve GELU
etkinleştirmesi içeren ileri beslemeli bir ağ izler ve bu ağın çıktısı da yeniden eklenir. Sonunda
sınıf token'ını al, katman normalleştirmesi ve tek çıktılı, yani darlığın logitini veren bir
doğrusal katman uygula. Ağı eğitim yamalarıyla 8 epoch boyunca, karıştırılmış 64 yamalık gruplar
hâlinde, logit üzerinde ikili çapraz entropi kaybıyla ve öğrenme hızı 0,001 olan Adam optimizasyon
algoritmasıyla eğit. Veri çoğaltma için her grubu rastgele bir çeyrek tur döndür ve yarı olasılıkla
soldan sağa aynala. Her epoch'un sonunda doğrulama yamalarının olasılıklarının AUC değerini hesapla;
eğitimin sonunda doğrulama AUC değeri en büyük olan epoch'un ağırlıklarını sakla. Sonucun
tekrarlanabilmesi için seed değerini 2026 olarak sabitle. Ardından test yamalarının olasılıklarını
ve bunların "darlık" sütununa göre AUC değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Eğitilebilir ağırlık sayısını ve her epoch'un doğrulama AUC değerini yazdır; test AUC
değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Ağın 94.881 eğitilebilir ağırlığı olmalı ve hiçbir test anjiyogramının yaması eğitimde
kullanılmamalı.
```

**Beklenen sonuç:** "cevap" = 0,934

### Prompt 3.3: Vision Transformer nereye bakıyor?

**Amaç.** Bu promptla Vision Transformer'ın sınıf token'ının dikkatinin ne kadarının, darlığın bulunduğu yama merkezine düştüğü ölçülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Anjiyogramlarda darlık bulan bir Vision Transformer'ın dikkat haritalarını bir açıklama
olarak okumadan önce, dikkatinin darlığın bulunduğu yere düşüp düşmediğini öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir X ışınlı koroner anjiyogram veri
seti olan ARCADE'in 64 × 64 piksellik 3.088 test yamasını tutar. Her satır bir yamadır: "anjiyogram"
sütunu yamanın anjiyogramının numarasını verir; "darlık" sütunu, merkezi uzmanların sınırını çizdiği
bir darlıkta olan yama için 1, her darlıktan uzakta bir damarın üzerindeki yama için 0 değerini
alır. "dikkat" sütununun her hücresi toplamı 1 olan 8 × 8 sayılık bir tablo tutar: Dersin küçük
Vision Transformer'ın sınıf token'ının, yamanın 8 × 8 piksellik 64 karesinin her birine gösterdiği
ve dört katmanı boyunca izlenen dikkat (dikkat aktarımı). Ortadaki dört kare, yamanın ortadaki 16 ×
16 pikselini kaplar; 1'den başlayarak sayıldığında bunlar 4. ve 5. satır ve sütunlardır.
Görev: Her yama için ortadaki dört karenin dikkatini topla. Bu payın darlık içeren yamalar ve öteki
yamalar üzerindeki ortalamasını hesapla ve iki ortalamayı, dikkat eşit dağılsaydı dört karenin
alacağı pay olan 4/64 = 0,0625 ile karşılaştır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: İki ortalamayı yazdır; darlık içeren yamaların ortalamasını üç ondalık basamakla "cevap"
adıyla sakla.
Test: Her pay 0 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,153

## Kodu onarmak, açıklatmak ve denetlemek için promptlar

Bu promptlar her adımın koduyla kullanılabilir. Köşeli parantez içindeki yerler, prompt gönderilmeden önce doldurulmalıdır.

### Çalışan ama kontrolden geçmeyen kodu onarmak

```text
Aşağıdaki kod şu görev için yazıldı: [promptun Görev satırını yapıştırınız]. Kod çalışıyor, ancak
dersin kontrolü "henüz değil" yazıyor. Hatayı bul, iki cümleyle açıkla ve düzeltilmiş kodu ver.
Sonuç yine "cevap" adıyla saklanmalı.

[kodu buraya yapıştırınız]
```

### Bir hata mesajını anlamak

```text
Aşağıdaki kod bir Jupyter Notebook'ta çalıştırıldığında altta verilen hata mesajını veriyor. Hatanın
nedenini sade bir dille açıkla ve düzeltilmiş kodu ver.

[kodu buraya yapıştırınız]

[hata mesajını buraya yapıştırınız]
```

### Kodu açıklatmak

```text
Aşağıdaki kodu, kod yazmayan bir hekim için satır satır açıkla. Ardından kodun hata mesajı vermeden
yanlış sonuç verebileceği iki durumu belirt.

[kodu buraya yapıştırınız]
```

### Bir görüntü işlem hattını denetletmek

```text
Aşağıdaki kodu denetle; kod tıbbi görüntüler üzerinde bir ağı eğitiyor ya da sınıyor ve doğruluğunu
bildiriyor. Altı noktayı kontrol et. Kümeler hastaya, en azından görüntüye göre ayrılmış mı; böylece
bir hastanın ya da bir görüntünün hiçbir yaması ya da karesi iki tarafta birden bulunmuyor mu?
Normalleştirme, eşikler ve öteki bütün seçimler yalnızca eğitim ve doğrulama kümelerinde mi
öğrenilmiş? Her veri çoğaltma etiketin anlamını koruyor mu; örneğin etiket tarafa bağlıyken aynalama
yapılmıyor mu? Her görüntü testte eğitimdekiyle tamamen aynı biçimde, yani aynı boyutta, aynı değer
aralığında ve önceden eğitilmiş ağın ölçeklemesiyle mi hazırlanıyor? Sonuç kararın verildiği düzeyde
ve gerçekçi bir prevalansta mı bildiriliyor; örneğin bir tespit modeli için özenle seçilmiş
yamaların AUC değeri yerine lezyon duyarlılığı ve görüntü başına yanlış tespit sayısı mı veriliyor?
Gerçek bir hastanın herhangi bir görüntüsü ya da başlığı kurum dışına çıkabilir mi? Her nokta için
ilgili satırı alıntıla, doğru olup olmadığını söyle ve doğru değilse düzeltilmiş kodu ver.
```

## Haftalık projenin promptları

[Haftalık proje](README.md#haftal%C4%B1k-proje), her adım için bir prompt olmak üzere dört promptla yapılabilir. Her promptun tablosu, Jupyter Notebook'un sonundaki *Haftalık proje* bölümünde hazırlanmaktadır ve bu bölüm tek başına da açılabilir. Sonuçlar rapora gireceği için projede kontrol hücresi ve hazır kod bulunmamaktadır. Bir adımın testi sağlanmadan sonraki prompt gönderilmemeli ve raporun YZ kullanım günlüğünde dört promptun hepsine yer verilmelidir.

### Proje adımı 1: Üç ağ, tek bir test

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Gerçek koroner anjiyogramlarda darlık bulmak için aynı biçimde eğitilmiş ve aynı
anjiyogramlarda sınanmış evrişimli bir ağı, bir Vision Transformer'ı ve hibrit bir modeli
karşılaştırmak istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan ARCADE'in darlık
kümesindeki 1.500 X ışınlı koroner anjiyogramdan (eğitim 1.000 anjiyogram, doğrulama 200, test 300)
kesilmiş 64 × 64 piksellik yamaları tutar. Her satır bir yamadır: "küme" sütunu yamanın kümesini
("eğitim", "doğrulama" ya da "test"), "anjiyogram" anjiyogramının numarasını verir; "yama" sütununun
her hücresi yamayı gri değerleri 0 ile 1 arasında olan 64 × 64 piksellik bir görüntü olarak tutar.
"darlık" sütunu, yamanın merkezi uzmanların sınırını çizdiği bir darlığın merkezine 6 pikselden
yakınsa 1, yama sınırı çizilmiş her darlıktan ve görüntünün kenarından en az 48 piksel uzakta bir
damarın üzerindeyse 0 değerini alır.
Görev: Her yamayı kendi içinde standartlaştır: Gri değerlerinin ortalamasını çıkar ve standart
sapmalarının 0,02 fazlasına böl. Üç ağ kur. Birincisi: Tek kanallı, 64 × 64 piksellik bir yama için
küçük bir evrişimli ağ kur: Her biri 3 × 3 piksellik filtreler ve bir piksellik dolgu içeren bir
evrişim (16, 32, 64 ve 64 filtre), batch normalizasyonu, ReLU ve 2 × 2 en büyük havuzlamadan oluşan
dört blok; ardından her kanalın konumları üzerinden ortalaması ve tek çıktılı, yani darlığın
logitini veren bir doğrusal katman. İkincisi: Tek kanallı, 64 × 64 piksellik bir yama için küçük bir
Vision Transformer kur. Yamayı 8 × 8 piksellik 64 kareye böl ve her kareyi öğrenilen aynı doğrusal
dönüşümle 64 sayıya dönüştür. 64 token'ın önüne 64 sayıdan oluşan öğrenilen bir sınıf token'ı koy ve
öğrenilen konumları ekle: 65 yerin her biri için, standart sapması 0,02 olan küçük rastgele
sayılarla başlayan 64 sayılık bir vektör. Token'ları dört Transformer bloğundan geçir. Her blokta
katman normalleştirmesini dört başlı öz dikkat izler ve öz dikkatin çıktısı bloğun girdisine
eklenir; ikinci bir katman normalleştirmesini 128 birimlik bir gizli katman ve GELU etkinleştirmesi
içeren ileri beslemeli bir ağ izler ve bu ağın çıktısı da yeniden eklenir. Sonunda sınıf token'ını
al, katman normalleştirmesi ve tek çıktılı, yani darlığın logitini veren bir doğrusal katman uygula.
Üçüncüsü: Tek kanallı, 64 × 64 piksellik bir yama için hibrit bir ağ kur. Her biri 3 × 3 piksellik
filtreler ve bir piksellik dolgu içeren bir evrişim (16, 32 ve 64 filtre), batch normalizasyonu,
ReLU ve 2 × 2 en büyük havuzlamadan oluşan üç evrişim bloğu, yamayı 64 sayılık 8 × 8 konuma
dönüştürür. Bu 64 konum küçük bir Transformer modelinin token'larıdır: Önlerine 64 sayıdan oluşan
öğrenilen bir sınıf token'ı koy, 65 yer için standart sapması 0,02 olan küçük rastgele sayılarla
başlayan öğrenilen konumları ekle ve token'ları iki Transformer bloğundan geçir. Her blokta katman
normalleştirmesini dört başlı öz dikkat izler ve öz dikkatin çıktısı bloğun girdisine eklenir;
ikinci bir katman normalleştirmesini 128 birimlik bir gizli katman ve GELU etkinleştirmesi içeren
ileri beslemeli bir ağ izler ve bu ağın çıktısı da yeniden eklenir. Sonunda sınıf token'ını al,
katman normalleştirmesi ve tek çıktılı, yani darlığın logitini veren bir doğrusal katman uygula. Her
ağı eğitim yamalarıyla 8 epoch boyunca, karıştırılmış 64 yamalık gruplar hâlinde, logit üzerinde
ikili çapraz entropi kaybıyla ve öğrenme hızı 0,001 olan Adam optimizasyon algoritmasıyla eğit. Veri
çoğaltma için her grubu rastgele bir çeyrek tur döndür ve yarı olasılıkla soldan sağa aynala. Her
epoch'un sonunda doğrulama yamalarının olasılıklarının AUC değerini hesapla; eğitimin sonunda
doğrulama AUC değeri en büyük olan epoch'un ağırlıklarını sakla. Sonucun tekrarlanabilmesi için seed
değerini 2026 olarak sabitle. Ardından test yamalarının olasılıklarını ve bunların "darlık" sütununa
göre AUC değerini hesapla. 300 test anjiyogramından yerine koyarak 2.000 bootstrap örneği çek,
çekilen her anjiyogramın bütün yamalarını tut ve her AUC değerine 2,5. ve 97,5. yüzdelikler
arasındaki yüzde 95 aralığını ver. Sonucun tekrarlanabilmesi için seed değerini 2026 olarak sabitle.
Aynı örneklerde Vision Transformer'ın ve hibrit modelin AUC değerinin evrişimli ağınkine göre
farkını hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her ağ için eğitilebilir ağırlıklarını, eğitim süresini ve aralığıyla birlikte test AUC
değerini içeren bir satırdan oluşan bir tablo ile iki farkı aralıklarıyla birlikte göster; en büyük
test AUC değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Üç ağın eğitilebilir ağırlık sayıları 60.641, 142.465 ve 94.881 olmalı ve aralıklar yamalardan
değil anjiyogramlardan hesaplanmalı.
```

### Proje adımı 2: Laboratuvar için bir eşik

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Anjiyogramlarda darlık arayan ağların sabit bir eşikte uygulamada ne vereceğini, hem özenle
seçilmiş yamalar arasında hem de darlığın seyrek olduğu bütün bir anjiyogramın pencereleri arasında
öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir X ışınlı koroner anjiyogram veri
seti olan ARCADE'in 64 × 64 piksellik 6.336 doğrulama ve test yamasını (doğrulama 200 anjiyogram,
test 300) tutar. Her satır bir yamadır: "küme" sütunu yamanın kümesini ("doğrulama" ya da "test"),
"anjiyogram" anjiyogramının numarasını verir; "darlık" sütunu merkezi uzmanların sınırını çizdiği
bir darlıkta olan yama için 1, her darlıktan uzaktaki bir damarın üzerindeki yama için 0 değerini
alır. "evrişimli ağ", "Vision Transformer" ve "hibrit model" adlı üç sütun, dersin eğitim
yamalarıyla eğitilmiş üç küçük ağının verdiği darlık olasılığını tutar.
Görev: Üç ağın her biri için "doğrulama" kümesinin yamalarında, darlık içeren yamaların yüzde
90'ının ulaştığı eşiği seç. Bu eşiği "test" kümesinin yamalarına uygula; duyarlılığı, özgüllüğü ve
pozitif öngörü değerini hesapla. Ardından aynı duyarlılık ve özgüllüğün yüzde 2 prevalansta vereceği
pozitif öngörü değerini hesapla: Duyarlılık ile 0,02'nin çarpımı, kendisi ile bir eksi özgüllüğün
0,98 ile çarpımının toplamına bölünür.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her ağ için eşiğini ve dört değeri içeren bir satırdan oluşan bir tablo göster; hibrit
modelin yüzde 2 prevalanstaki pozitif öngörü değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Eşikler yalnızca doğrulama yamalarında seçilmeli ve her değer 0 ile 1 arasında olmalı.
```

### Proje adımı 3: Bütün anjiyogramlar için bir tespit modeli

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Bütün koroner anjiyogramlarda darlıkları, anjiyogram başına yaklaşık bir yanlış tespitle
işaretleyen bir program istiyorum ve programın darlıkların ne kadarını bulduğunu öğrenmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir veri seti olan ARCADE'in darlık
kümesindeki 1.500 X ışınlı koroner anjiyogramı (eğitim 1.000, doğrulama 200, test 300) tutar. Her
satır bir anjiyogramdır: "küme" sütunu kümesini ("eğitim", "doğrulama" ya da "test"), "anjiyogram"
numarasını verir; "görüntü" sütununun her hücresi anjiyogramı gri değerleri 0 ile 255 arasında olan
512 × 512 piksellik bir görüntü olarak tutar; "darlıklar" sütunu uzmanların sınırını çizdiği
darlıkların merkezlerini, 0'dan başlayarak sayılan piksel olarak (sütun, satır) çiftleri hâlinde
listeler.
Görev: Her görüntüyü 0 ile 1 arasında gri değerlere getir. Her anjiyogramdan 64 × 64 piksellik
pencereler kes: Her darlık için, darlığı ortalayan ve her yönde rastgele en fazla 16 piksel
kaydırılmış dört pencere (etiket 1); her darlık için, görüntünün kenarından en az 48 piksel uzaktaki
ince ve koyu yapıları ortalayan altı pencere (bu yapılar, yarıçapı 6 olan bir diskle uygulanan siyah
şapka dönüşümünde değeri en büyük yüzde 3 içinde kalan piksellerdir) ve rastgele yerlerde altı
pencere; bunların hepsi her darlıktan en az 48 piksel uzakta olmalı (etiket 0). Her yamayı kendi
içinde standartlaştır: Gri değerlerinin ortalamasını çıkar ve standart sapmalarının 0,02 fazlasına
böl. Tek kanallı, 64 × 64 piksellik bir yama için hibrit bir ağ kur. Her biri 3 × 3 piksellik
filtreler ve bir piksellik dolgu içeren bir evrişim (16, 32 ve 64 filtre), batch normalizasyonu,
ReLU ve 2 × 2 en büyük havuzlamadan oluşan üç evrişim bloğu, yamayı 64 sayılık 8 × 8 konuma
dönüştürür. Bu 64 konum küçük bir Transformer modelinin token'larıdır: Önlerine 64 sayıdan oluşan
öğrenilen bir sınıf token'ı koy, 65 yer için standart sapması 0,02 olan küçük rastgele sayılarla
başlayan öğrenilen konumları ekle ve token'ları iki Transformer bloğundan geçir. Her blokta katman
normalleştirmesini dört başlı öz dikkat izler ve öz dikkatin çıktısı bloğun girdisine eklenir;
ikinci bir katman normalleştirmesini 128 birimlik bir gizli katman ve GELU etkinleştirmesi içeren
ileri beslemeli bir ağ izler ve bu ağın çıktısı da yeniden eklenir. Sonunda sınıf token'ını al,
katman normalleştirmesi ve tek çıktılı, yani darlığın logitini veren bir doğrusal katman uygula. Ağı
eğitim yamalarıyla 8 epoch boyunca, karıştırılmış 64 yamalık gruplar hâlinde, logit üzerinde ikili
çapraz entropi kaybıyla ve öğrenme hızı 0,001 olan Adam optimizasyon algoritmasıyla eğit. Veri
çoğaltma için her grubu rastgele bir çeyrek tur döndür ve yarı olasılıkla soldan sağa aynala. Her
epoch'un sonunda doğrulama yamalarının olasılıklarının AUC değerini hesapla; eğitimin sonunda
doğrulama AUC değeri en büyük olan epoch'un ağırlıklarını sakla. Sonucun tekrarlanabilmesi için seed
değerini 2026 olarak sabitle. Ardından her doğrulama ve test anjiyogramını, merkezleri 8'den
başlayarak her 16 pikselde bir bulunan 64 × 64 piksellik pencerelerle tara; görüntü kenarlarında
yansıtılarak genişletilir. Her pencerenin olasılığını hesapla. Tespit, olasılığı eşiğe eşit ya da
eşikten büyük olan ve 5 × 5 merkezlik komşuluğundaki pencereler arasında en büyük olasılığa sahip
penceredir. Bir tespit bir darlığa 32 pikselden yakınsa darlık bulunmuş sayılır; öteki her tespit
yanlıştır. Doğrulama anjiyogramlarında anjiyogram başına en fazla bir yanlış tespit veren, 0,50 ile
0,99 arasında 0,01 adımlarla seçilmiş en küçük eşiği bul ve bu eşiği test anjiyogramlarına uygula.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Seçilen eşiği yazdır. Ardından 0,50, 0,70, 0,90 eşiklerinin ve seçilen eşiğin her biri için
bir satırdan oluşan bir tablo göster: Test anjiyogramlarındaki bütün darlıklar içinde bulunan darlık
sayısı ve test anjiyogramı başına yanlış tespit sayısı. Seçilen eşikte bulunan darlıkların oranını
üç ondalık basamakla "cevap" adıyla sakla.
Test: Eşik yalnızca doğrulama anjiyogramlarında seçilmeli ve test anjiyogramlarında 386 darlık
bulunmalı.
```

### Proje adımı 4: Bir kardiyoloğun okuduğu hatalar

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter Notebook'uma yapıştırıp
çalıştıracağım.
Bağlam: Böyle bir aracın kateter laboratuvarında neler yapabileceğine karar verebilmek için bir
tespit modelinin kaçırdığı darlıkları ve yanlış işaretlediği yerleri görmek istiyorum.
Veri: Jupyter Notebook'ta "veri" adında bir tablo var; açık bir X ışınlı koroner anjiyogram veri
seti olan ARCADE'in 300 test anjiyogramını tutar. Her satır bir anjiyogramdır: "anjiyogram" sütunu
numarasını verir; "görüntü" sütununun her hücresi anjiyogramı gri değerleri 0 ile 255 arasında olan
512 × 512 piksellik bir görüntü olarak tutar; "darlıklar" sütunu uzmanların sınırını çizdiği
darlıkların merkezlerini 0'dan başlayarak sayılan piksel olarak (sütun, satır) çiftleri hâlinde
listeler. "olasılıklar" sütununun her hücresi, dersin tespit modelinin verdiği darlık olasılıklarını
32 × 32 sayılık bir tablo olarak tutar; her sayı, merkezi her yönde 8, 24, 40 ve böyle 504 piksele
kadar giden noktalarda bulunan 64 × 64 piksellik bir pencereye aittir. "eşik" sütunu tespit
modelinin, doğrulama anjiyogramlarında anjiyogram başına en fazla bir yanlış tespit verecek biçimde
seçilmiş eşiğini tutar.
Görev: Tespit, olasılığı eşiğe eşit ya da eşikten büyük olan ve 5 × 5 merkezlik komşuluğundaki
pencereler arasında en büyük olasılığa sahip penceredir. Bir tespit bir darlığa 32 pikselden yakınsa
darlık bulunmuş sayılır; öteki her tespit yanlıştır. Her anjiyogram için kaçırılan darlıkları ve
yanlış tespitleri olasılıklarıyla birlikte listele. Ardından beş kaçırılmış darlığı ve olasılığı en
büyük beş yanlış tespiti, her birini çevresindeki 128 × 128 piksellik pencerede, olasılıklar
görüntünün üzerine çizilmiş, uzmanların darlıkları daire ve tespitler kare olarak gösterilmiş
biçimde göster.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: On pencereyi göster, kaçırılan darlıkların ve yanlış tespitlerin sayısını yazdır; kaçırılan
darlıkların sayısını "cevap" adıyla sakla.
Test: Kaçırılan ve bulunan darlıkların toplamı 386 olmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
