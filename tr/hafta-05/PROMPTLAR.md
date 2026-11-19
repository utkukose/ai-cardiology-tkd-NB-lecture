# Prompt kütüphanesi, 5. hafta

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[5. hafta](README.md) · [Prompt yolu](../../PROMPT_PATH.tr.md) · [English](../../en/week-05/PROMPTS.md)

Bu kütüphanede, 5. haftanın prompt (istem) yolundaki, yani Jupyter defterinin 1. kısmındaki bütün promptlar yer almaktadır; her prompt, eğitimin prompt kartıyla yazılmıştır. Promptlar olduğu gibi bir yapay zekâ (YZ) asistanına kopyalanabilir; GitHub her kutunun köşesinde bir kopyalama düğmesi gösterir. Asistanın yazdığı kod, defterde aynı numaralı adımın boş hücresine yapıştırılır ve orada çalıştırılır. Yolun bütününü [prompt yolu rehberi](../../PROMPT_PATH.tr.md) anlatmaktadır.

Eğitimin hiçbir promptunda hasta verisi yoktur ve promptlara hasta verisi eklenmemelidir. Gerçek hasta verileri hiçbir zaman bir prompta, bulut tabanlı bir deftere ya da bir YZ sohbetine girmez.

1. [Bir adım nasıl ilerler?](#bir-adım-nasıl-ilerler)
2. [Durak 1: Ritim: Altı etiket için bir kural ve bir ağ](#durak-1-ritim-altı-etiket-için-bir-kural-ve-bir-ağ)
3. [Durak 2: ST yükselmesi: Medyan atım, J noktası ve alarm](#durak-2-st-yükselmesi-medyan-atım-j-noktası-ve-alarm)
4. [Durak 3: Uzun süreli izlem: Pencereler, AF yükü ve yanlış alarmlar](#durak-3-uzun-süreli-izlem-pencereler-af-yükü-ve-yanlış-alarmlar)
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

## Durak 1: Ritim: Altı etiket için bir kural ve bir ağ

*[Ders sayfası, uygulama durağı 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#stop-1) · Python yolunda aynı sonuç: Python adımı 5, 1-5. bölümler*

Bu durak oturumun mini projesidir. PTB-XL'in 12 derivasyonlu EKG'leri önce bir kardiyoloğun ritmi okuduğu gibi RR aralıklarından, ardından altı etiketi aynı anda öğrenen tek boyutlu evrişimli bir ağ tarafından okunur. Ağ 1. ve 2. katlarla eğitilir, eşikleri 9. katta seçilir; kural da ağ da 10. katta değerlendirilir.

### Adım 1.1: RR aralıklarından bir kural

**Amaç.** Bu adımda AF için klinik kuralın ilk yarısı, yani düzensiz biçimde düzensiz RR aralıkları, test katında sınanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: RR aralıklarına dayanan basit bir kuralın 10 saniyelik 12 derivasyonlu EKG'lerde atriyal
fibrilasyonu (AF) ne kadar iyi bulduğunu öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; klinik ortamda alınmış 10 saniyelik 12 derivasyonlu
EKG'lerden oluşan herkese açık PTB-XL veri setinin test katındaki 2.198 kaydı tutar. Her satır bir
kayıttır: "kayıt" sütunu kaydın numarasını verir, "RR" sütunu kaydın 12 derivasyonun hepsinden
bulunan R tepelerine göre hesaplanmış RR aralıklarını saniye olarak tutar, "AF" sütunu ise
kardiyologlar atriyal fibrilasyon tanımladıysa 1, tanımlamadıysa 0'dır.
Görev: En az üç RR aralığı olan her kayıt için değişim katsayısını hesapla: Aralıkların standart
sapması (paydada aralık sayısının bir eksiği kullanılır) ortalamalarına bölünür. Değişim katsayısı
0,10'un üstünde olan kayda AF de. Kuralı "AF" sütunuyla karşılaştır; duyarlılığını, özgüllüğünü ve
pozitif öngörü değerini hesapla. AF'li ve AF'siz kayıtların değişim katsayılarını iki histogram
olarak çiz ve 0,10 düzeyine dikey bir çizgi ekle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Alarm sayısını ve üç değeri yazdır; duyarlılığı üç ondalık basamakla "cevap" adıyla sakla.
Test: Alarmların sayısı doğru ve yanlış alarmların toplamına, duyarlılık da doğru alarmların AF'li
kayıtların sayısına bölümüne eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 0,914

### Adım 1.2: Altı etiket için tek boyutlu bir ağ

**Amaç.** Bu adımda 12 derivasyonun sinyalinin tamamını okuyan ve aynı anda altı etiket veren bir ağ eğitilir. Eğitim yaklaşık bir dakika sürer.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: 10 saniyelik 12 derivasyonlu EKG'leri okuyan ve altı ritim bulgusunu aynı anda tanıyan bir
ağ eğitmek ve bu ağın bulguları yeni kayıtlarda ne kadar iyi ayırdığını öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; klinik ortamda alınmış 10 saniyelik 12 derivasyonlu
EKG'lerden oluşan herkese açık PTB-XL veri setinden 6.539 kayıt tutar. Her satır bir kayıttır:
"küme" sütunu kaydın kümesini verir ("eğitim": 1. ve 2. katlar, 4.356 kayıt; "doğrulama": 9. kat,
2.183 kayıt). "EKG" sütununun her hücresi kaydı, 100 Hz'de alınmış 12 derivasyon × 1.000 örnekten
oluşan ve mV cinsinden değerler içeren bir dizi olarak tutar; derivasyonların sırası D1, D2, D3,
aVR, aVL, aVF ve V1-V6'dır. "SR", "AFIB", "STACH", "SBRAD", "SARRH" ve "PVC" adlı altı sütun,
kardiyologlar ilgili ifadeyi verdiyse 1, vermediyse 0'dır. Bu ifadeler sırasıyla sinüs ritmi,
atriyal fibrilasyon, sinüs taşikardisi, sinüs bradikardisi, sinüs aritmisi ve ventriküler erken
vurulardır.
Görev: Altı etiketin her birine bir skor veren tek boyutlu bir evrişimli ağ kur. Ağda zaman boyunca
dört evrişim katmanı bulunur; her katmanın adımı 2'dir ve her katmanı batch normalizasyonu ile ReLU
izler. Katmanlar sırasıyla 12 derivasyon üzerinde 7 örneklik 32 çekirdek, ardından 5 örneklik 64
çekirdek, 5 örneklik 64 çekirdek ve 3 örneklik 128 çekirdekten oluşur. 128 kanalın her birinin zaman
boyunca ortalaması, altı çıktısı olan son bir doğrusal katmana verilir. Eğitimden önce sinyallerin
değerlerini −5 ile 5 mV aralığıyla sınırla. Ağı eğitim kayıtlarıyla, karıştırılmış 64 kayıtlık
gruplar hâlinde 15 epoch boyunca eğit; kayıp olarak altı etiketin ikili çapraz entropisini,
optimizasyon algoritması olarak Adam'ı kullan. Tek döngülü (one-cycle) bir öğrenme hızı kullan ve en
yüksek değerini 0,003 yap. Her epoch'tan sonra doğrulama kayıtlarında her etiketin ROC eğrisi
altındaki alanını (AUC) ve bunların ortalamasını hesapla; ortalamanın en yüksek olduğu epoch'un
ağırlıklarını sakla. Rastgele seçimler her çalıştırmada aynı olsun; bunun için başlangıç değeri
olarak 2026 sayısını kullan.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Parametre sayısını, her epoch'un ortalama AUC değerini ve en iyi epoch'u yazdır; en iyi
ortalama AUC değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Ağın 59.622 parametresi olmalı ve ortalama AUC 0,5 ile 1 arasında olmalı.
```

**Beklenen sonuç:** "cevap" = 0,881

### Adım 1.3: Test katında her etiket

**Amaç.** Bu adımda dersin ağı, hiç görmediği kayıtlarda etiket etiket değerlendirilir.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Altı ritim bulgusunun her biri için bir ağın, bulguyu taşıyan 12 derivasyonlu EKG'leri
taşımayanlardan ne kadar iyi ayırdığını öğrenmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in test katındaki 2.198 kaydı tutar. Her satır
bir kayıttır: "kayıt" sütunu kaydın numarasını verir. "SR", "AFIB", "STACH", "SBRAD", "SARRH" ve
"PVC" adlı altı sütun, kardiyologlar ilgili ifadeyi verdiyse 1, vermediyse 0'dır. Bu ifadeler
sırasıyla sinüs ritmi, atriyal fibrilasyon, sinüs taşikardisi, sinüs bradikardisi, sinüs aritmisi ve
ventriküler erken vurulardır. "olasılık SR" ile "olasılık PVC" arasındaki altı sütun, 1. ve 2.
katlarla eğitilmiş tek boyutlu evrişimli bir ağın altı etikete verdiği olasılıkları tutar.
Görev: Altı etiketin her biri için, o etiketin olasılığının 0 ve 1 değerlerinden oluşan kendi
sütununa karşı ROC eğrisi altındaki alanını (AUC) hesapla. Altı ROC eğrisini tek bir şekilde çiz ve
her birinin AUC değerini açıklamaya yaz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Etiketi, o etiketi taşıyan kayıt sayısını ve AUC değerini gösteren küçük bir tablo yazdır;
"AFIB" etiketinin AUC değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Her AUC 0 ile 1 arasında olmalı; bir kayıt birkaç etiket taşıyabildiği için kayıt sayılarının
toplamı en az 2.198 olmalı.
```

**Beklenen sonuç:** "cevap" = 0,975

### Adım 1.4: 9. katta seçilen eşikler

**Amaç.** Bu adımda olasılıklar, her etiket için 9. katta seçilip 10. katta değerlendirilen bir eşikle kararlara dönüştürülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir ağın altı ritim bulgusu için verdiği olasılıkları, her bulgu için testten ayrı tutulan
kayıtlarda seçilmiş bir eşikle kararlara dönüştürmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in 9. ve 10. katlarındaki 4.381 kaydı tutar. Her
satır bir kayıttır: "kayıt" sütunu kaydın numarasını, "küme" sütunu ise kümesini verir ("doğrulama":
9. kat; "test": 10. kat). "SR", "AFIB", "STACH", "SBRAD", "SARRH" ve "PVC" adlı altı sütun,
kardiyologlar ilgili ifadeyi verdiyse 1, vermediyse 0'dır. Bu ifadeler sırasıyla sinüs ritmi,
atriyal fibrilasyon, sinüs taşikardisi, sinüs bradikardisi, sinüs aritmisi ve ventriküler erken
vurulardır. "olasılık SR" ile "olasılık PVC" arasındaki altı sütun, 1. ve 2. katlarla eğitilmiş tek
boyutlu evrişimli bir ağın altı etikete verdiği olasılıkları tutar.
Görev: Her etiket için doğrulama kayıtlarında, duyarlılık ile özgüllüğün toplamının en yüksek olduğu
olasılık eşiğini seç. Her eşiği test kayıtlarına uygula: Bir etiketin olasılığı eşiğine ulaştığında
o etiket verilir. Her etiketin test kayıtlarındaki duyarlılığını, özgüllüğünü ve pozitif öngörü
değerini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Etiketi, eşiğini ve üç değeri gösteren bir tablo yazdır; "AFIB" etiketinin test
kayıtlarındaki pozitif öngörü değerini üç ondalık basamakla "cevap" adıyla sakla.
Test: Eşikler yalnızca doğrulama kayıtlarından gelmeli; her duyarlılık ve özgüllük 0 ile 1 arasında
olmalı.
```

**Beklenen sonuç:** "cevap" = 0,636

## Durak 2: ST yükselmesi: Medyan atım, J noktası ve alarm

*[Ders sayfası, uygulama durağı 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#stop-2) · Python yolunda aynı sonuç: 6. ve 7. bölümler*

Haftanın vakası olan 13913 numaralı kayıt, burada bir STEMI alarmının okuduğu gibi okunur. Tek tek atımlar R tepelerine göre hizalanır ve medyanları her derivasyon için temiz bir atım verir. J noktasındaki ST sapması PR segmentine göre ölçülür, alarmın kararını evrensel tanımın ölçütleri verir; aynı alarm daha sonra test katındaki sol dal bloklu kayıtlarda denenir.

### Adım 2.1: Vakanın medyan atımı

**Amaç.** Bu adımda vakanın tek tek atımlarından, bir EKG cihazının yazılımının ölçümden önce yaptığı gibi, her derivasyon için temiz bir atım oluşturulur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: ST segmenti ölçülmeden önce 10 saniyelik 12 derivasyonlu bir EKG'nin medyan atımını, yani
her derivasyon için temiz bir atımı oluşturmak istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in 13913 numaralı kaydını, yani 68 yaşında bir
erkeğin 100 Hz'de alınmış 10 saniyelik 12 derivasyonlu EKG'sini tutar. Her satır, bir öncekinden 10
ms sonra alınmış bir örnektir: "zaman" sütunu örneğin zamanını saniye olarak verir, "I" ile "V6"
arasındaki on iki sütun on iki derivasyonun değerlerini mV olarak tutar; "R tepesi" sütunu ise R
tepelerinin bulunduğu örneklerde 1, diğer örneklerde 0'dır.
Görev: Her atımı R tepesinden 0,30 s önceden 0,55 s sonraya kadar kes ve yalnızca penceresi tamamen
10 saniyenin içinde kalan atımları tut. Her derivasyon için bu atımların örnek örnek medyanını al:
Medyan atım budur. V2'nin medyan atımını, V2'nin tek tek atımlarının üzerine çiz; tek tek atımlar
açık gri olsun ve yatay eksende R tepesine göre zaman ms olarak yer alsın.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kullanılan atım sayısını yazdır ve "cevap" adıyla sakla.
Test: Her atım −300 ile 550 ms arasında 86 örnek içermeli; V2'nin medyan atımı her örnekte tek tek
atımların aralığında kalmalı.
```

**Beklenen sonuç:** "cevap" = 19

### Adım 2.2: J noktasında ST ve evrensel tanımın ölçütleri

**Amaç.** Bu adımda vakanın on iki derivasyonundaki ST sapması ölçülür ve otomatik bir STEMI alarmının yaptığı gibi evrensel tanımın ölçütleri uygulanır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Bir medyan atımın on iki derivasyonunda J noktasındaki ST sapmasını ölçmek ve EKG'nin
miyokard enfarktüsünün dördüncü evrensel tanımındaki ST ölçütlerini karşılayıp karşılamadığını
görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in 13913 numaralı kaydının, yani 68 yaşında bir
erkeğin EKG'sinin 12 derivasyonuna ait medyan atımı tutar. Medyan atım, R tepelerine göre hizalanmış
tek tek atımların örnek örnek medyanıdır. Her satır, bir öncekinden 10 ms sonra gelen bir örnektir:
"zaman" sütunu örneğin R tepesine göre zamanını −300 ile 550 ms arasında ms olarak verir, "I" ile
"V6" arasındaki on iki sütun ise on iki derivasyonun değerlerini mV olarak tutar. Bu medyan atımda
QRS kompleksi, on iki derivasyonun eğimlerinin gösterdiği gibi, R tepesinden 70 ms önce başlar ve R
tepesinden 50 ms sonra J noktasında biter.
Görev: Her derivasyon için referans düzeyi olarak R tepesinden 130, 120, 110 ve 100 ms önceki
değerlerin ortalamasını al; bunlar PR segmentinin, QRS başlangıcından 20 ms önce biten 40 ms'sidir.
Bir derivasyonun ST sapması, R tepesinden 50 ms sonraki J noktasındaki değerinden referans düzeyinin
çıkarılmasıyla bulunur. Bir derivasyon, J noktasındaki ST yükselmesi kendi eşiğine ulaştığında
miyokard enfarktüsünün dördüncü evrensel tanımındaki ölçütü karşılar. Eşikler V2 ve V3 için 40 yaş
ve üstündeki erkeklerde 0,2 mV, 40 yaşın altındaki erkeklerde 0,25 mV, kadınlarda 0,15 mV; diğer
bütün derivasyonlarda ise 0,1 mV'tur. Aynı gruptaki en az iki derivasyon ölçütü karşıladığında alarm
çalar. Ardışık derivasyon grupları anterior (V1-V6), inferior (D2, D3 ve aVF; tablodaki "II", "III"
ve "aVF" sütunları) ve lateraldir (D1 ve aVL; tablodaki "I" ve "aVL" sütunları); aVR hiçbir gruba
girmez.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her derivasyonun ST sapmasını mV ve mm olarak (1 mm = 0,1 mV), ölçütü karşılayan
derivasyonları ve alarmın çaldığı grupları yazdır; ölçütü karşılayan derivasyonların sayısını
"cevap" adıyla sakla.
Test: D3'ün (tablodaki "III" sütunu) ve aVR'nin ST sapmaları negatif olmalı; çünkü kardiyologların
raporu D3'te ST çökmesi tanımlamaktadır.
```

**Beklenen sonuç:** "cevap" = 9

### Adım 2.3: Sol dal bloğunda alarm

**Amaç.** Bu adımda aynı alarm test katındaki bütün kayıtlarda denenir ve ölçütlerin uygulanamadığı sol dal bloğunda ne yaptığı görülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Miyokard enfarktüsünün dördüncü evrensel tanımındaki ST ölçütlerine dayanan otomatik bir
STEMI alarmını bir test kümesinin bütün EKG'lerine uygulamak ve alarmın tam sol dal bloğunda ne
sıklıkla çaldığını görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in test katındaki 2.198 kaydı tutar. Her satır
bir kayıttır: "kayıt" sütunu kaydın numarasını, "cinsiyet" hastanın cinsiyetini ("E" ya da "K"),
"yaş" ise yaşını verir; "LBBB" sütunu kardiyologlar tam sol dal bloğu tanımladıysa 1, tanımlamadıysa
0'dır. "I" ile "V6" arasındaki on iki sütun, on iki derivasyonun ST sapmasını mV olarak tutar:
Kaydın medyan atımında J noktasındaki değerden PR segmentinin düzeyi çıkarılmıştır.
Görev: Bir derivasyon, J noktasındaki ST yükselmesi kendi eşiğine ulaştığında miyokard enfarktüsünün
dördüncü evrensel tanımındaki ölçütü karşılar. Eşikler V2 ve V3 için 40 yaş ve üstündeki erkeklerde
0,2 mV, 40 yaşın altındaki erkeklerde 0,25 mV, kadınlarda 0,15 mV; diğer bütün derivasyonlarda ise
0,1 mV'tur. Aynı gruptaki en az iki derivasyon ölçütü karşıladığında alarm çalar. Ardışık derivasyon
grupları anterior (V1-V6), inferior (D2, D3 ve aVF; tablodaki "II", "III" ve "aVF" sütunları) ve
lateraldir (D1 ve aVL; tablodaki "I" ve "aVL" sütunları); aVR hiçbir gruba girmez. Alarmı her kayda
uygula; V2 ve V3'ün eşiklerini kaydın sahibi olan hastanın cinsiyetine ve yaşına göre seç. Bütün
kayıtlar arasındaki ve sol dal bloğu olan kayıtlar arasındaki alarmları say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Bütün kayıtlar arasındaki ve sol dal bloğu olan kayıtlar arasındaki alarm sayılarını kayıt
sayılarıyla birlikte yazdır; sol dal bloğu olan kayıtlar arasındaki alarm sayısını "cevap" adıyla
sakla.
Test: 2.198 kayıt bulunmalı ve bunların 54'ünde sol dal bloğu olmalı; bu kayıtlar arasındaki
alarmlar 54'ten fazla olamaz.
```

**Beklenen sonuç:** "cevap" = 51

## Durak 3: Uzun süreli izlem: Pencereler, AF yükü ve yanlış alarmlar

*[Ders sayfası, uygulama durağı 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#stop-3) · Python yolunda aynı sonuç: 8. ve 9. bölümler*

Sanal kliniğin bir Holter cihazı VC-0128 numaralı hastayı 24 saat izlemiştir. Bu durakta kaydın atımları, bir kayıt cihazının algoritmasının yaptığı gibi 30 saniyelik pencereler hâlinde okunur: Her penceredeki RR aralıklarının düzensizliği alarmı belirler, alarm verilen pencereler AF yükünü verir ve yanlış alarmların hangi saatlerde çıktığı izlenir. Kayıt sentetik olduğu için gerçek durum atım atım bilinmektedir ve hiçbir şeyin indirilmesi gerekmez.

### Adım 3.1: 30 saniyelik pencerelerde ritmin düzensizliği

**Amaç.** Bu adımda 24 saat, bir monitörün yaptığı gibi pencere pencere okunur ve RR aralıkları düzensiz olan pencereler sayılır.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: 24 saatlik bir Holter kaydını 30 saniyelik pencereler hâlinde okumak ve kaç pencerede RR
aralıklarının bir atriyal fibrilasyon (AF) alarmı verecek kadar düzensiz olduğunu görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; sanal kliniğin VC-0128 numaralı hastasına, çarpıntı
yakınması olan 76 yaşındaki bir kadına ait 24 saatlik bir Holter kaydının atımlarını, kayıt
cihazının atım algılayıcısının bulduğu biçimiyle tutar. Kayıt saat 08.00'de başlar. Her satır bir
atımdır: "zaman" sütunu atımın kaydın başından itibaren saniye cinsinden zamanını, "RR" ise önceki
atımdan bu yana geçen aralığı saniye olarak verir.
Görev: 24 saati, kaydın başından başlayarak 30 saniyelik pencerelere böl ve her atımı zamanının
düştüğü pencereye ver. En az beş RR aralığı içeren her pencerede ritmin düzensizliğini değişim
katsayısıyla ölç: Penceredeki RR aralıklarının standart sapması (paydada aralık sayısının bir eksiği
kullanılır) ortalamalarına bölünür. Her pencerenin değişim katsayısını saate karşı çiz ve 0,10
düzeyinde yatay bir çizgi ekle.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Pencere sayısını yazdır; değişim katsayısı 0,10'un üstünde olan pencerelerin sayısını "cevap"
adıyla sakla.
Test: 30 saniyelik 2.880 pencere bulunmalı ve bütün değişim katsayıları pozitif olmalı.
```

**Beklenen sonuç:** "cevap" = 519

### Adım 3.2: AF yükü

**Amaç.** Bu adımda pencereler, bir Holter raporunun verdiği sayıya, yani günün AF içinde geçen bölümünün oranına dönüştürülür.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: 24 saatlik bir Holter kaydının AF yükünü, yani kaydın atriyal fibrilasyon içinde geçen
bölümünün oranını, 30 saniyelik pencereleri okuyan bir algoritmanın bildireceği biçimde öğrenmek
istiyorum.
Veri: Defterde "veri" adında bir tablo var; sanal kliniğin VC-0128 numaralı hastasına, çarpıntı
yakınması olan 76 yaşındaki bir kadına ait 24 saatlik bir Holter kaydının atımlarını, kayıt
cihazının atım algılayıcısının bulduğu biçimiyle tutar. Kayıt saat 08.00'de başlar. Her satır bir
atımdır: "zaman" sütunu atımın kaydın başından itibaren saniye cinsinden zamanını, "RR" ise önceki
atımdan bu yana geçen aralığı saniye olarak verir.
Görev: 24 saati, kaydın başından başlayarak 30 saniyelik pencerelere böl ve her atımı zamanının
düştüğü pencereye ver. En az beş RR aralığı içeren her pencerede ritmin düzensizliğini değişim
katsayısıyla ölç: Penceredeki RR aralıklarının standart sapması (paydada aralık sayısının bir eksiği
kullanılır) ortalamalarına bölünür. Değişim katsayısı 0,10'un üstünde olan pencereye AF de. AF yükü,
AF penceresi sayısının 30 saniyeyle çarpımının kaydın 24 saatine bölümüdür. İlk ve son AF
penceresinin saatini de bul.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: AF penceresi sayısını yazdır; AF yükünü yüzde olarak bir ondalık basamakla "cevap" adıyla
sakla.
Test: Yük, AF pencerelerinin 30 saniyelik bütün pencereler içindeki oranının 100 ile çarpımına eşit
olmalı.
```

**Beklenen sonuç:** "cevap" = 18,0

### Adım 3.3: Yanlış alarmlar nereden geliyor?

**Amaç.** Bu adımda alarm doğrulanmış ataklarla karşılaştırılır ve bir Holter okuyucusunun yapacağı gibi yanlış alarmların saatleri bulunur.

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: 24 saatlik bir Holter kaydının AF alarmını bir kardiyoloğun doğruladığı ataklarla
karşılaştırmak ve yanlış alarmların günün hangi saatlerinde çıktığını görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; sanal kliniğin VC-0128 numaralı hastasına, çarpıntı
yakınması olan 76 yaşındaki bir kadına ait 24 saatlik bir Holter kaydının atımlarını, kayıt
cihazının atım algılayıcısının bulduğu biçimiyle tutar. Kayıt saat 08.00'de başlar. Her satır bir
atımdır: "zaman" sütunu atımın kaydın başından itibaren saniye cinsinden zamanını, "RR" ise önceki
atımdan bu yana geçen aralığı saniye olarak verir. "AF" sütunu, bir kardiyoloğun kaydın tamamında
doğruladığı atriyal fibrilasyon ataklarındaki atımlar için 1, öteki bütün atımlar için 0'dır.
Görev: 24 saati, kaydın başından başlayarak 30 saniyelik pencerelere böl ve her atımı zamanının
düştüğü pencereye ver. En az beş RR aralığı içeren her pencerede ritmin düzensizliğini değişim
katsayısıyla ölç: Penceredeki RR aralıklarının standart sapması (paydada aralık sayısının bir eksiği
kullanılır) ortalamalarına bölünür. Değişim katsayısı 0,10'un üstünde olan pencereye AF de.
Atımlarının yarısından fazlası doğrulanmış bir atağa ait olan pencere gerçek bir AF penceresidir.
Yanlış alarmları, yani gerçek AF penceresi olmayan AF pencerelerini, ve kaçırılan pencereleri, yani
alarm verilmeyen gerçek AF pencerelerini say. Ardından yanlış alarmları her saat için ayrı ayrı say.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kaçırılan pencere sayısını ve yanlış alarmların saatlere göre dağılımını gösteren küçük bir
tablo yazdır; yanlış alarmların toplam sayısını "cevap" adıyla sakla.
Test: Bütün saatlerdeki yanlış alarmların toplamı genel toplama eşit olmalı; AF pencereleri de alarm
verilen gerçek AF pencereleriyle yanlış alarmların toplamına eşit olmalı.
```

**Beklenen sonuç:** "cevap" = 75

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

### Bir zaman serisi işlem hattını denetletmek

```text
Aşağıdaki kodu denetle; kod 12 derivasyonlu EKG'leri okuyor ve bir modelin ya da bir alarmın
sonuçlarını bildiriyor. Altı noktayı kontrol et. Bir hastanın kayıtları tek bir kümede, eğitimde,
doğrulamada ya da testte tutulmuş mu? Örnekleme frekansı ve birimler doğru mu? Derivasyonlar
konumlarına göre değil, adlarına göre mi alınmış? Eşikler test kümesinde değil, doğrulama kümesinde
mi seçilmiş? Sonuçlar her etiket için, etiketin ne sıklıkla görüldüğüyle birlikte mi bildirilmiş?
Her ölçümün kuralı, yani taban çizgisi, J noktası ve cinsiyete ve yaşa göre eşikler belirtilmiş mi?
Her sorun için ilgili satırı aktar, sonucunu klinik sözcüklerle açıkla ve düzeltilmiş satırı ver.
Başka hiçbir şeyi değiştirme.
```

## Haftalık projenin prompt yolu

[Haftalık proje](README.md#haftal%C4%B1k-proje), prompt yolunda her adım için bir prompt olmak üzere dört promptla yapılabilir. Jupyter defterinin 1. kısmının sonundaki *Prompt yolunda haftalık proje* bölümü, her promptun tablosunu hazırlar. Projede kontrol ve hazır kod yoktur, çünkü sonuçlar rapora girer. Bir adımın testi sağlanmadan sonraki prompt gönderilmez ve raporun YZ kullanım günlüğünde dört promptun hepsi yer alır.

### Adım 1: Alarm ve akut enfarktüsler

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Miyokard enfarktüsünün dördüncü evrensel tanımındaki ST ölçütlerine dayanan otomatik bir
STEMI alarmını bir göğüs ağrısı biriminin yapacağı gibi değerlendirmek istiyorum: Alarm kaç akut
enfarktüsü bulur ve alarmlarının kaçı doğrudur?
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in 9. ve 10. katlarındaki 4.381 kaydı tutar. Her
satır bir kayıttır: "kayıt" sütunu kaydın numarasını, "küme" kümesini ("doğrulama" ya da "test"),
"cinsiyet" hastanın cinsiyetini ("E" ya da "K"), "yaş" ise yaşını verir. "akut enfarktüs" sütunu,
kardiyologlar kayıttaki bir enfarktüsü akut (I. ya da I-II. evre) olarak sınıfladıysa 1,
sınıflamadıysa 0'dır. "ifadeler" sütunu kardiyologların bütün ifadelerinin kodlarını virgülle
ayrılmış olarak listeler; örneğin tam sol dal bloğu için "CLBBB", sol ventrikül hipertrofisi için
"LVH", kalp pili için "PACE". "I" ile "V6" arasındaki on iki sütun, on iki derivasyonun ST sapmasını
mV olarak tutar: Kaydın medyan atımında J noktasındaki değerden PR segmentinin düzeyi çıkarılmıştır.
Görev: Bir derivasyon, J noktasındaki ST yükselmesi kendi eşiğine ulaştığında miyokard enfarktüsünün
dördüncü evrensel tanımındaki ölçütü karşılar. Eşikler V2 ve V3 için 40 yaş ve üstündeki erkeklerde
0,2 mV, 40 yaşın altındaki erkeklerde 0,25 mV, kadınlarda 0,15 mV; diğer bütün derivasyonlarda ise
0,1 mV'tur. Aynı gruptaki en az iki derivasyon ölçütü karşıladığında alarm çalar. Ardışık derivasyon
grupları anterior (V1-V6), inferior (D2, D3 ve aVF; tablodaki "II", "III" ve "aVF" sütunları) ve
lateraldir (D1 ve aVL; tablodaki "I" ve "aVL" sütunları); aVR hiçbir gruba girmez. Alarmı her kayda
uygula; V2 ve V3'ün eşiklerini hastanın cinsiyetine ve yaşına göre seç. Alarmı "akut enfarktüs"
sütunuyla karşılaştır; duyarlılığını, özgüllüğünü ve pozitif öngörü değerini bütün kayıtlar için ve
her küme için ayrı ayrı hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Kayıt, akut enfarktüs ve alarm sayılarını ve üç değeri gösteren bir tablo göster; tabloda her
küme için bir satır ve bütün kayıtlar için bir satır olsun. Bütün kayıtlardaki duyarlılığı üç
ondalık basamakla "cevap" adıyla sakla.
Test: 4.381 kayıt ve 26 akut enfarktüs bulunmalı; doğru alarmlar 26'dan fazla olamaz.
```

### Adım 2: Yanlış alarmlar nereden geliyor?

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Otomatik bir STEMI alarmının yanlış alarmlarının hangi tanıları taşıdığını öğrenmek ve
böylece ölçütlerinin nerede uymadığını görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in 9. ve 10. katlarındaki 4.381 kaydı tutar. Her
satır bir kayıttır: "kayıt" sütunu kaydın numarasını, "küme" kümesini ("doğrulama" ya da "test"),
"cinsiyet" hastanın cinsiyetini ("E" ya da "K"), "yaş" ise yaşını verir. "akut enfarktüs" sütunu,
kardiyologlar kayıttaki bir enfarktüsü akut (I. ya da I-II. evre) olarak sınıfladıysa 1,
sınıflamadıysa 0'dır. "ifadeler" sütunu kardiyologların bütün ifadelerinin kodlarını virgülle
ayrılmış olarak listeler; örneğin tam sol dal bloğu için "CLBBB", sol ventrikül hipertrofisi için
"LVH", kalp pili için "PACE". "I" ile "V6" arasındaki on iki sütun, on iki derivasyonun ST sapmasını
mV olarak tutar: Kaydın medyan atımında J noktasındaki değerden PR segmentinin düzeyi çıkarılmıştır.
Görev: Bir derivasyon, J noktasındaki ST yükselmesi kendi eşiğine ulaştığında miyokard enfarktüsünün
dördüncü evrensel tanımındaki ölçütü karşılar. Eşikler V2 ve V3 için 40 yaş ve üstündeki erkeklerde
0,2 mV, 40 yaşın altındaki erkeklerde 0,25 mV, kadınlarda 0,15 mV; diğer bütün derivasyonlarda ise
0,1 mV'tur. Aynı gruptaki en az iki derivasyon ölçütü karşıladığında alarm çalar. Ardışık derivasyon
grupları anterior (V1-V6), inferior (D2, D3 ve aVF; tablodaki "II", "III" ve "aVF" sütunları) ve
lateraldir (D1 ve aVL; tablodaki "I" ve "aVL" sütunları); aVR hiçbir gruba girmez. Alarmı her kayda
uygula; V2 ve V3'ün eşiklerini hastanın cinsiyetine ve yaşına göre seç. Akut enfarktüsü olmayan bir
kayıttaki alarm yanlış alarmdır. Her ifade için o ifadeyi taşıyan kayıtlardaki yanlış alarmları say;
"CLBBB", "PACE" ve "LVH" ifadeleri için ayrıca bu ifadeleri taşıyan kayıtların ne kadarının alarm
verdiğini hesapla.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: En çok yanlış alarm veren 15 ifadeyi göster; "CLBBB" taşıyan kayıtlardaki yanlış alarm
sayısını "cevap" adıyla sakla.
Test: Bir ifadenin yanlış alarmları, o ifadeyi taşıyan kayıtlardan fazla olamaz; yanlış alarmların
toplamı da 1. adımdaki alarmlardan doğru alarmların çıkarılmasıyla bulunan sayıya eşit olmalı.
```

### Adım 3: Eşiklerin taranması

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Otomatik bir STEMI alarmının bütün eşikleri birlikte yükseltildiğinde duyarlılığının ve
pozitif öngörü değerinin nasıl değiştiğini görmek istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in 9. ve 10. katlarındaki 4.381 kaydı tutar. Her
satır bir kayıttır: "kayıt" sütunu kaydın numarasını, "küme" kümesini ("doğrulama" ya da "test"),
"cinsiyet" hastanın cinsiyetini ("E" ya da "K"), "yaş" ise yaşını verir. "akut enfarktüs" sütunu,
kardiyologlar kayıttaki bir enfarktüsü akut (I. ya da I-II. evre) olarak sınıfladıysa 1,
sınıflamadıysa 0'dır. "ifadeler" sütunu kardiyologların bütün ifadelerinin kodlarını virgülle
ayrılmış olarak listeler; örneğin tam sol dal bloğu için "CLBBB", sol ventrikül hipertrofisi için
"LVH", kalp pili için "PACE". "I" ile "V6" arasındaki on iki sütun, on iki derivasyonun ST sapmasını
mV olarak tutar: Kaydın medyan atımında J noktasındaki değerden PR segmentinin düzeyi çıkarılmıştır.
Görev: Bir derivasyon, J noktasındaki ST yükselmesi kendi eşiğine ulaştığında miyokard enfarktüsünün
dördüncü evrensel tanımındaki ölçütü karşılar. Eşikler V2 ve V3 için 40 yaş ve üstündeki erkeklerde
0,2 mV, 40 yaşın altındaki erkeklerde 0,25 mV, kadınlarda 0,15 mV; diğer bütün derivasyonlarda ise
0,1 mV'tur. Aynı gruptaki en az iki derivasyon ölçütü karşıladığında alarm çalar. Ardışık derivasyon
grupları anterior (V1-V6), inferior (D2, D3 ve aVF; tablodaki "II", "III" ve "aVF" sütunları) ve
lateraldir (D1 ve aVL; tablodaki "I" ve "aVL" sütunları); aVR hiçbir gruba girmez. Alarmı her kayda
uygula; V2 ve V3'ün eşiklerini hastanın cinsiyetine ve yaşına göre seç. Alarmı her eşiğe sırasıyla
0; 0,05; 0,10; 0,15 ve 0,20 mV eklenmiş olarak tekrarla. Her pay için "akut enfarktüs" sütununa göre
duyarlılığı, özgüllüğü ve pozitif öngörü değerini hesapla; duyarlılığı ve pozitif öngörü değerini
paya karşı çiz.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Her pay için bir satır içeren bir tablo göster; 0,10 mV paydaki duyarlılığı üç ondalık
basamakla "cevap" adıyla sakla.
Test: Pay büyüdükçe alarm sayısı artamaz; payın 0 olduğu satır 1. adımın sonucuna eşit olmalı.
```

### Adım 4: Ölçütlerin uygulanamadığı kayıtları dışarıda bırakmak

```text
Rol: Kod yazmayan bir kardiyoloğa yardım ediyorsun. Yazacağın kodu Jupyter defterime yapıştırıp
çalıştıracağım.
Bağlam: Otomatik bir STEMI alarmını yalnızca evrensel tanımın ST ölçütlerinin uygulanabildiği
EKG'lerde değerlendirmek; sol dal bloğunu ve kalp pili ritmini dışarıda bırakmak istiyorum.
Veri: Defterde "veri" adında bir tablo var; PTB-XL'in 9. ve 10. katlarındaki 4.381 kaydı tutar. Her
satır bir kayıttır: "kayıt" sütunu kaydın numarasını, "küme" kümesini ("doğrulama" ya da "test"),
"cinsiyet" hastanın cinsiyetini ("E" ya da "K"), "yaş" ise yaşını verir. "akut enfarktüs" sütunu,
kardiyologlar kayıttaki bir enfarktüsü akut (I. ya da I-II. evre) olarak sınıfladıysa 1,
sınıflamadıysa 0'dır. "ifadeler" sütunu kardiyologların bütün ifadelerinin kodlarını virgülle
ayrılmış olarak listeler; örneğin tam sol dal bloğu için "CLBBB", sol ventrikül hipertrofisi için
"LVH", kalp pili için "PACE". "I" ile "V6" arasındaki on iki sütun, on iki derivasyonun ST sapmasını
mV olarak tutar: Kaydın medyan atımında J noktasındaki değerden PR segmentinin düzeyi çıkarılmıştır.
Görev: İfadeleri arasında "CLBBB" ya da "PACE" bulunan her kaydı dışarıda bırak. Bir derivasyon, J
noktasındaki ST yükselmesi kendi eşiğine ulaştığında miyokard enfarktüsünün dördüncü evrensel
tanımındaki ölçütü karşılar. Eşikler V2 ve V3 için 40 yaş ve üstündeki erkeklerde 0,2 mV, 40 yaşın
altındaki erkeklerde 0,25 mV, kadınlarda 0,15 mV; diğer bütün derivasyonlarda ise 0,1 mV'tur. Aynı
gruptaki en az iki derivasyon ölçütü karşıladığında alarm çalar. Ardışık derivasyon grupları
anterior (V1-V6), inferior (D2, D3 ve aVF; tablodaki "II", "III" ve "aVF" sütunları) ve lateraldir
(D1 ve aVL; tablodaki "I" ve "aVL" sütunları); aVR hiçbir gruba girmez. Alarmı her kayda uygula; V2
ve V3'ün eşiklerini hastanın cinsiyetine ve yaşına göre seç. Kalan kayıtlarda "akut enfarktüs"
sütununa göre duyarlılığı, özgüllüğü ve pozitif öngörü değerini hesapla ve bunları 1. adımla
karşılaştır.
Kısıtlar: Yalnızca bu tabloyu kullan. Kod dosya okumamalı, internetten bir şey indirmemeli ve
program kurmamalıdır.
Çıktı: Dışarıda bırakılan kayıt sayısını ve üç değeri yazdır; pozitif öngörü değerini üç ondalık
basamakla "cevap" adıyla sakla.
Test: Dışarıda bırakılan ve kalan kayıtların toplamı 4.381 olmalı.
```

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
