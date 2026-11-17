<div align="center">

# Hafta 3: Derin öğrenme ve evrişimli sinir ağları

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği

*Tek bir nörondan kalp görüntülerini okuyan bir ağa*

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [Kurulum](../../SETUP.tr.md) · [English](../../en/week-03/README.md)

</div>

## Hafta hakkında

Tek bir nörondan derin bir ağa yapay sinir ağları: kayıp, gradyanlar ve eğitim döngüsü, dizi olarak görüntüler, evrişim ve havuzlama ve herkese açık ACDC veri setinin sine kardiyak manyetik rezonans incelemelerinde normal kalbi, dilate kardiyomiyopatiyi ve hipertrofik kardiyomiyopatiyi birbirinden ayıran bir evrişimli sinir ağı (CNN). Aşırı öğrenmeye seyreltme, yığın normalizasyonu, veri çoğaltma ve erken durdurmayla karşı konur; sonuçlar sınıf sınıf kesinlik, duyarlılık ve F1 skoruyla, uzman konturlarından elde edilen ölçümlerin yanında okunur. Ardından LeNet'ten ResNet'e bilinen mimariler, bir YZ asistanının yazdığı eğitim döngüsünün denetimi ve her katılımcının kişisel kayıtla edindiği EchoNet-Dynamic ekokardiyografi videoları gelir.

Oturumda 4 saat, haftalık proje için yaklaşık 3 saat.

## Haftanın rotası

Ders sayfası haftanın ana rotasıdır. Kod ya da prompt (istem) içermez ve etkileşimli labla birlikte yukarıdan aşağıya okunur. Her uygulama durağında her katılımcı Jupyter defterindeki iki yoldan birini seçer: Kodu hazır promptlarla bir yapay zekâ (YZ) asistanının yazdığı, katılımcının ise çalıştırıp denetlediği **prompt yolu** (Kısım 1) ya da kodu katılımcının yazdığı **Python yolu** (Kısım 2). İki yol da aynı sonuçlara varır. Defter, kurulum gerektirmeyen Google Colab'da da kendi bilgisayarınızdaki Jupyter'de de çalışır ([kurulum](../../SETUP.tr.md)).

|  | Ana rota: ders sayfası ve etkileşimli lab | Uygulama durağı: yolunuzu seçin |
|---|---|---|
| 1 | [Tek sayfada yapay sinir ağları](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#neural-networks-in-one-page), [Öğrenme: Kayıp, gradyanlar ve eğitim döngüsü](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#learning-loss-gradients-and-the-training-loop), [Dizi olarak görüntüler: ACDC'nin sine kardiyak MR görüntüleri](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#images-as-arrays-cine-cardiac-mr-of-acdc) | **[Durak 1: Sayılarla sine MR](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-1)**<br>Prompt yolu: Kısım 1, Durak 1<br>Python yolu: Kısım 2, Python adımı 3, 1-3. bölümler |
| 2 | [Evrişim: Görüntü üzerinde kayan filtreler](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#convolution-filters-that-slide-over-an-image), [Sine MR için bir evrişimli ağ](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#a-convolutional-network-for-cine-mr), [Aşırı öğrenme: Seyreltme, yığın normalizasyonu ve veri çoğaltma](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#overfitting-dropout-batch-normalisation-and-augmentation), [Sonucu okumak: Kesinlik, duyarlılık ve F1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#reading-the-result-precision-recall-and-f1) | **[Durak 2: İlk evrişimli ağ](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-2)**<br>Prompt yolu: Kısım 1, Durak 2<br>Python yolu: Kısım 2, 4-7. bölümler |
| 3 | [Bilinen mimariler: LeNet'ten ResNet'e](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#known-architectures-from-lenet-to-resnet), [YZ asistanıyla çalışmak, 3. bölüm: Bir eğitim döngüsünü denetlemek](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#ai-pair-programming-part-3-reviewing-a-training-loop), [EchoNet-Dynamic: Kişisel kayıtla ekokardiyografi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#echonet-dynamic-echocardiography-with-personal-registration) | **[Durak 3: EchoNet-Dynamic: normal mi, anormal mi (kaydınızla)](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#stop-3)**<br>Prompt yolu: Kısım 1, Durak 3<br>Python yolu: Kısım 2, 8-10. bölümler |
|  | [Haftanın makalesi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#the-paper-of-the-week), [Sanal klinik, 3. aşama: Görüntüleme laboratuvarı açılıyor](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#the-virtual-clinic-stage-3-the-imaging-laboratory-opens) | Kendi verinizle bölümü, haftanın makalesi ve sanal klinik |

## Malzemeler

| Malzeme | Aç | İçeriği |
|---|---|---|
| **Ders sayfası (ana rota)** | [Ders sayfasını aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html) | Vaka, çözümlü örnekleriyle kavramlar, ağın içini gösteren üç boyutlu (3B) bir sahne, iki animasyon, bilgi kontrolleri, üç uygulama durağı, kendi verinizle bölümü, tekrar kartları ve kaynaklar. Kod ve prompt içermez. |
| **Etkileşimli lab** | [Etkileşimli labı aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/lab.html) | F bölümündeki prompt atölyesi dâhil kod gerektirmeyen A-F bölümleri, öz değerlendirme, yansıtma ve dışa aktarılabilen öğrenme günlüğü |
| **Jupyter defteri** | [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-03/NB03_derin_ogrenme_ve_evrisimli_aglar.ipynb)<br>[Jupyter için indir](NB03_derin_ogrenme_ve_evrisimli_aglar.ipynb) | Kısım 1, prompt yolu: her biri hazır bir prompt, YZ asistanının kodu için bir hücre, otomatik bir kontrol ve hazır kod içeren on adımlı üç durak. Kısım 2, Python yolu: Python adımı 3, A-J alıştırmalarıyla 1-10. bölümler ve yedi alanın uygulama görevleri. |
| **Prompt kütüphanesi** | [PROMPTLAR.md](PROMPTLAR.md) | Prompt yolunun bütün promptları (GitHub'da her birinin yanında kopyalama düğmesi bulunur), kodu onarmak için promptlar ve haftalık projenin prompt yolu |
| **PDF ders notu** | [Hafta03_Ders_Notlari.pdf](Hafta03_Ders_Notlari.pdf) | Uygulama duraklarıyla ve kendi verinizle bölümüyle birlikte ders sayfasının yazdırılabilir biçimi |

<table>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_b_bolumu_evrisim.png" alt="Etkileşimli lab, B bölümü: 3 × 3'lük bir çekirdek ACDC'nin bir kısa eksen kesiti üzerinde kayar; bir konumun çarpımları ve büyüyen öznitelik haritası görünür." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_ogrenme_egrileri.png" alt="Jupyter defteri, 6. bölüm: 45 eğitim hastasında eğitilen ağın seyreltmesiz ve seyreltmeli eğitim ve doğrulama kaybı." width="100%"></td></tr>
<tr><td>Etkileşimli lab, B bölümü: 3 × 3'lük bir çekirdek ACDC'nin bir kısa eksen kesiti üzerinde kayar; bir konumun çarpımları ve büyüyen öznitelik haritası görünür.</td><td>Jupyter defteri, 6. bölüm: 45 eğitim hastasında eğitilen ağın seyreltmesiz ve seyreltmeli eğitim ve doğrulama kaybı.</td></tr>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_c_bolumu_asiri_ogrenme.png" alt="Etkileşimli lab, C bölümü: aşırı öğrenmeye karşı dört ayarın öğrenme eğrileri ve bir kesitin döndürülmüş kopyaları." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/lab_f_bolumu_prompt_atolyesi.png" alt="Etkileşimli lab, F bölümü: prompt atölyesi. Prompt kartının yedi alanı, kalite göstergesi ve hasta verisi uyarısı." width="100%"></td></tr>
<tr><td>Etkileşimli lab, C bölümü: aşırı öğrenmeye karşı dört ayarın öğrenme eğrileri ve bir kesitin döndürülmüş kopyaları.</td><td>Etkileşimli lab, F bölümü: prompt atölyesi. Prompt kartının yedi alanı, kalite göstergesi ve hasta verisi uyarısı.</td></tr>
</table>

## Haftanın vakası

**ACDC test kümesindeki 134 numaralı hasta** 185 cm boyunda ve 104 kg ağırlığındadır ve hipertrofik kardiyomiyopati grubundadır. Sine kardiyak manyetik rezonans incelemesinin uzman konturları yüzde 62,2'lik bir ejeksiyon fraksiyonu ve 16,4 mm'lik en kalın duvar segmenti verir. 45 başka hastayla eğitilen bir ağın hastalığı piksellerden tanıması gerekmektedir. [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html) bu vakayla açılır; sanal kliniğin görüntüleme laboratuvarı soruyu son bölümde cevaplar.

## Öğrenme çıktıları

Hafta sonunda katılımcıların bir nöronun, bir katmanın ve bir ağın çıktılarını nasıl hesapladığını, bir kaybın, gradyanlarının ve ağırlık güncellemesinin bir ağı nasıl öğrettiğini açıklayabilmeleri beklenmektedir. Bir sine kardiyak manyetik rezonans incelemesini bir dizi olarak tarif edebilmeli, uzman konturlarından hacimleri ve ejeksiyon fraksiyonunu hesaplayabilmeli ve bir çalışmanın hastalarını her türlü öğrenmeden önce ayırabilmelidirler. Bir evrişim ve bir havuzlama adımını izleyebilmeli, küçük bir evrişimli ağ eğitebilmeli, öğrenme eğrilerinde aşırı öğrenmeyi tanıyabilmeli ve sonucu her sınıf için kesinlik, duyarlılık ve F1 skoruyla okuyabilmelidirler. Son olarak ağı bilinen mimariler arasına yerleştirebilmeli, bir YZ asistanının yazdığı eğitim döngüsünü denetleyebilmeli ve EchoNet-Dynamic gibi kayıt gerektiren bir veri setini kullanım koşullarına uygun biçimde edinebilmelidirler.

## Çalışma yolu

Oturuma katılanlar ana rotayı ve uygulama duraklarını oturumda tamamlar. Haftayı kendi başına izleyenler, örneğin bir oturumu kaçıranlar, aşağıdaki sürelerle plan yapabilir.

| Adım | Etkinlik | Prompt yolu | Python yolu |
|---|---|---|---|
| 1 | Haftanın vakasını ve ders sayfasını 1. uygulama durağına kadar okuyun; etkileşimli labın A bölümünü ve bilgi kontrollerini yapın | 55 dakika | 55 dakika |
| 2 | 1. uygulama durağı: Prompt yolunda Kısım 1, Durak 1; Python yolunda Python adımı 3 ile 1-3. bölümler | 25 dakika | 1 saat 15 dakika |
| 3 | 2. uygulama durağına kadar okumayı sürdürün: evrişim, ağın üç boyutlu görünümü, aşırı öğrenme ve sonucu okumak; etkileşimli labın B-D bölümlerini yapın | 1 saat | 1 saat |
| 4 | 2. uygulama durağı: Kısım 1, Durak 2 ya da 4-7. bölümler | 35 dakika | 1 saat 15 dakika |
| 5 | 3. uygulama durağına kadar okumayı sürdürün: bilinen mimariler, bir eğitim döngüsünün denetimi ve EchoNet-Dynamic; etkileşimli labın E ve F bölümlerini yapın | 40 dakika | 40 dakika |
| 6 | EchoNet-Dynamic için kişisel kayıtla 3. uygulama durağı: Kısım 1, Durak 3 ya da 8-10. bölümler | 30 dakika | 50 dakika |
| 7 | Haftanın makalesini, sanal kliniğin aşamasını ve kendi verinizle bölümünü okuyun | 30 dakika | 30 dakika |
| 8 | Etkileşimli labdaki öz değerlendirmeyi yapın (sekme: Kendini sına), yansıtmayı yazın ve öğrenme günlüğünü dışa aktarın | 20 dakika | 20 dakika |
| | **Haftalık proje dışında toplam** | **4 saat 55 dakika** | **6 saat 45 dakika** |
| 9 | Haftalık projeyi iki yoldan biriyle tamamlayın | 3 saat | 3 saat |

## Oturumun eğitim akışı

Haftanın dört saatlik oturumu aşağıdaki plana göre işlenir. Plan, malzemelerin canlı bir oturumda nasıl bir araya geldiğini göstermek için paylaşılmaktadır.

| Süre | Etkinlik |
|---|---|
| 0:00-0:15 | Haftanın vakası, ACDC'nin 134 numaralı hastası, ve haftanın rotası. Her katılımcı defteri Google Colab'da ya da Jupyter'de açar ve üç grubun ACDC dosyalarını, yaklaşık 105 MB'ı, açık kaynağından indiren 0. bölümü çalıştırır. |
| 0:15-0:55 | Ana rota: tek sayfada yapay sinir ağları, etkileşimli labın A bölümüyle öğrenme, dizi olarak sine kardiyak manyetik rezonans. |
| 0:55-1:30 | İki grupta 1. uygulama durağı: prompt yolu ve Python yolu. İki grup 134 numaralı hastanın ejeksiyon fraksiyonunu ve ACDC kurallarının doğruluğunu karşılaştırır. |
| 1:30-1:45 | Ara. |
| 1:45-2:30 | Ana rota: B bölümüyle evrişim, ağın üç boyutlu görünümü, C bölümüyle aşırı öğrenme ve D bölümüyle sonucu okumak. |
| 2:30-3:05 | 2. uygulama durağı: Ağ yaklaşık bir dakikada eğitilir ve hasta hasta konturlardan elde edilen ölçümlerle karşılaştırılır. |
| 3:05-3:40 | Ana rota: bilinen mimariler, E ve F bölümleriyle bir eğitim döngüsünü denetlemek, EchoNet-Dynamic. Oturumun mini projesi, 3. uygulama durağı: Kaydı olan katılımcılar durağı kendi kopyalarında çalıştırır; diğerleri için eğitmen ortak ekranda çalıştırır. |
| 3:40-4:00 | Haftanın makalesi, sanal kliniğin görüntüleme laboratuvarı, kendi verinizle bölümü ve haftalık proje. |

## Haftalık proje

**Ne yapılacak?** ACDC'nin sine kardiyak manyetik rezonans incelemelerinde dilate kardiyomiyopatiyi (DCM), hipertrofik kardiyomiyopatiyi (HCM) ve normal kalbi sınıflandırın ve ağı kardiyoloğun ölçümleriyle karşılaştırın. Önce dersin ağını 45 eğitim hastasında, erken durdurma için 15 doğrulama hastasını kullanarak eğitin. İkinci olarak 30 test hastasının karışıklık matrisini, her sınıfın kesinlik, duyarlılık ve F1 değerini ve makro F1'i bildirin. Üçüncü olarak ACDC kurallarını aynı 30 hastanın uzman konturlarından elde edilen ölçümlere uygulayın ve iki karışıklık matrisini karşılaştırın. Dördüncü olarak yanlış sınıflanan her hasta için ağın gördüğü kesitleri ve en kalın duvarın bulunduğu kesiti gösterin; klinikte hangi hataların en çok önem taşıyacağını ve nedenini yazın.

**Nereye bakılacak?** Ders: "Dizi olarak görüntüler: ACDC'nin sine kardiyak MR görüntüleri", "Sine MR için bir evrişimli ağ", "Aşırı öğrenme: Seyreltme, yığın normalizasyonu ve veri çoğaltma" ve "Sonucu okumak: Kesinlik, duyarlılık ve F1" bölümleri. Etkileşimli lab: C, D ve F bölümleri. Jupyter defteri: Kısım 1, 1. ve 2. duraklar ya da Kısım 2, 3, 5, 6 ve 7. bölümler.

**Prompt yolu.** Proje, her adım için bir prompt olmak üzere [prompt kütüphanesindeki](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-03/PROMPTLAR.md#haftal%C4%B1k-projenin-prompt-yolu) dört promptla da kurulabilir. Bir promptun testi sağlanmadan sonraki prompta geçilmez.

**Örnek.** Ağın 12 test hastasına normal dediğini, bunların 10'unda haklı olduğunu ve HCM'li 10 hastanın 2'sini kaçırdığını varsayın: Normal sınıfı için $TP = 10$, $FP = 2$, $FN = 0$'dır. Kesinliği $10/12 = 0{,}833$, duyarlılığı $10/10 = 1{,}000$ olur. F1 değeri $2TP/(2TP + FP + FN)$ ile hesaplanır; burada $20/22 = 0{,}909$'dur. Makro F1, üç sınıfın F1 değerlerinin düz ortalamasıdır.

**Ne teslim edilecek?** [Rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılmış, bir-iki sayfalık bir rapor: iki kaybın şekli, iki karışıklık matrisi, sınıflara göre ölçütlerin tablosu ve hataların şekli. Rapora YZ kullanım günlüğünü (araç, prompt, neyin denetlendiği, neyin değiştirildiği) ve çıktılarıyla birlikte Jupyter defterini ekleyin. ACDC görüntüleri içeren şekiller, kullanım koşullarının gerektirdiği gibi "ACDC, CC BY-NC-SA 4.0" kaynak bilgisini taşır ve yalnızca ticari olmayan amaçlarla kullanılır.

**Teslim.** Haftalık proje, 4. haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. E-postaya "Ne teslim edilecek?" başlığında sayılan öğeler ve etkileşimli labdan dışa aktarılan öğrenme günlüğü eklenir. Haftalık projeler değerlendirmenin yüzde 40'ını oluşturur; değerlendirme ölçütleri izlencede yer almaktadır.

## Kendi verinizle

Ders sayfası, haftanın yöntemlerini kendi verinize uygulamayı anlatan bir bölümle biter: hangi sorunun hangi yönteme uyduğu, önce neyin denetleneceği, etik kurul onayı, Kişisel Verilerin Korunması Kanunu (KVKK) ve hesabın nerede yapılacağı. [Ders sayfasında okuyun](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#with-your-own-data).

## İsteğe bağlı araştırma ödevi

PubMed'de, 2020 ya da sonrasında yayımlanmış ve ekokardiyogramlar ya da kardiyak manyetik rezonans görüntüleri üzerinde bir hastalığı saptamak için derin öğrenme modeli eğiten bir çalışma bulun. Çalışmayı yarım sayfada özetleyin: görüntüler ve kaç hastadan geldikleri, etiketler ve etiketleri kimin verdiği, ağ, her sınıf için bildirilen ölçütler ve model başka bir hastanenin hastalarında sınandıysa bunun nasıl yapıldığı. [Haftanın makalesindeki](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#the-paper-of-the-week) üç soru özete yol gösterebilir. Ödev notlandırılmaz; 4. haftadaki transfer öğrenme tartışmasına hazırlık niteliğindedir.

## Bu haftadan sonra sanal klinik

Sanal klinik 3. haftada açık görüntüleri okuyan görüntüleme laboratuvarını açar: her katılımcının kaynağından indirdiği ACDC sine kardiyak manyetik rezonans incelemeleri ve kişisel kaydı olanlar için EchoNet-Dynamic ekokardiyografi videoları. Bir evrişimli ağ ACDC'nin üç grubunu piksellerden öğrenir ve uzman konturlarından elde edilen ölçümlerle karşılaştırılır. Sonuçlar ders sayfasının [Sanal klinik, 3. aşama](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html#the-virtual-clinic-stage-3-the-imaging-laboratory-opens) bölümündedir.

## Gelecek hafta

**Hafta 4: Transfer öğrenme.** Görüntüleme laboratuvarı ölçüm yapmaya başlar: ImageNet üzerinde önceden eğitilmiş bir ağ olan EfficientNet-B0, az sayıda etiketli örnekle kalp görüntülerine uyarlanır; bir U-Net CAMUS ekokardiyogramlarında sol ventrikülün sınırlarını çizer ve ejeksiyon fraksiyonu bu sınırlardan disk yöntemiyle hesaplanır. [Eğitimin planına](../../README.tr.md#on-bir-hafta) bakın.

---

<div align="center">

**Prof. Dr. Utku Köse**

Profesör, Bilgisayar Mühendisliği Bölümü, Süleyman Demirel Üniversitesi, Isparta, Türkiye<br>
Kurucu Müdür, Yapay Zekâ Uygulama ve Araştırma Merkezi (YAZEM), Süleyman Demirel Üniversitesi<br>
Bilgisayar Bilimleri Anabilim Dalı Başkanı, Bilgisayar Mühendisliği Bölümü, Süleyman Demirel Üniversitesi<br>
Diğer kurumlar: University of North Dakota (ABD), Universidad Panamericana (Meksiko, Meksika), Vel Tech University (Chennai, Hindistan)<br>
IEEE Kıdemli Üyesi, ACM Profesyonel Üyesi

[ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) | [utkukose.com](https://www.utkukose.com) | [github.com/utkukose](https://github.com/utkukose)

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) | [utku.kose@und.edu](mailto:utku.kose@und.edu) | [ukose@up.edu.mx](mailto:ukose@up.edu.mx) | [utkukose@gmail.com](mailto:utkukose@gmail.com)

*İlk sürüm: Kasım 2026. İçerik CC BY 4.0, kod MIT.*

</div>
