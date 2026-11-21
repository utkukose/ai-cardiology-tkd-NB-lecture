<div align="center">

# Hafta 1: Python ve kardiyoloji veri temelleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği

*Programlama bilgisi sıfırdan klinik veri analizine*

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [Kurulum](../../SETUP.tr.md) · [English](../../en/week-01/README.md)

</div>

## Hafta hakkında

İlk iki saatte Anaconda ve Jupyter Notebook ortamı tanıtılır, değişkenler, listeler ve döngüler tıbbi örneklerle öğrenilir, pandas ile hasta tablosu okunup işlenir ve Matplotlib ile ilk kardiyolojik grafik çizilir. Bu kısım Kaggle Heart Disease veri setiyle yapılan mini projeyle kapanır. Son iki saatte elektrokardiyogram (EKG) verisiyle çalışılır: EKG örneklerden oluşan bir veri olarak ele alınır, on iki derivasyon tek bir kalp vektörünün izdüşümleri olarak açıklanır, PR, QRS ve QT aralıkları otomatik olarak ölçülür ve QT kalp hızına göre düzeltilir. Ardından PhysioNet ve MIT-BIH veri setlerine erişilir, kayıtlar wfdb kütüphanesiyle okunup işlenir, R tepeleri NeuroKit2 ile bulunur, kalp hızı değişkenliği (HRV) hesaplanır ve 12 derivasyon görselleştirilir. Haftalık proje, EKG'yi görselleştiren ve temel ölçümleri (PR, QRS, QT) otomatik olarak hesaplayan bir script'tir. Hafta, bir yapay zekâ (YZ) asistanıyla kod yazmanın ilk kurallarını da içermektedir.

Oturum 4 saat sürer. Haftalık proje için yaklaşık 3 saat ayrılmalıdır.

## Haftanın vakası

**VC-0317, 67 yaşında bir kadın hastadır.** İlaç tedavisindeki bir değişiklikten sonra başlayan çarpıntı yakınmasıyla polikliniğe başvurmuştur. EKG'sinin otomatik raporu düzeltilmiş QT'yi (QTc) 465 ms olarak vermekte ve uzamış olarak işaretlemektedir. [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) bu vakayla açılır; sanal klinik de son bölümde soruyu kendi ölçümleriyle cevaplar.

## Malzemeler

| Malzeme | Aç | Ne işe yarar? |
|---|---|---|
| **Ders sayfası** | [Ders sayfasını aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) | Haftanın anlatımıdır. Yukarıdan aşağıya okunur, uygulama duraklarına götürür ve kod ya da prompt (istem) içermez. |
| **Etkileşimli lab** | [Etkileşimli labı aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/lab.html) | Kod gerektirmeyen A-F bölümleri, ders sayfasında yeri geldiğinde açılır. F bölümü prompt atölyesidir. Öz değerlendirme ve öğrenme günlüğü de labdadır. |
| **Jupyter Notebook** | [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb)<br>[Jupyter için indir](NB01_python_ve_ekg_temelleri.ipynb) | Uygulama durakları burada çalışılır: Kısım 1 prompt yolu, Kısım 2 Python yoludur. Jupyter Notebook Google Colab'da kurulum gerektirmeden ya da kendi bilgisayarınızdaki Jupyter'de çalışır. |
| **Prompt kütüphanesi** | [PROMPTLAR.md](PROMPTLAR.md) | Prompt yolunun ve haftalık projenin bütün promptlarını, kodu onarmak, açıklatmak ve denetlemek için promptlarla birlikte içerir. GitHub'da her promptun yanında bir kopyalama düğmesi bulunur. |
| **PDF ders notu** | [Hafta01_Ders_Notlari.pdf](Hafta01_Ders_Notlari.pdf) | Ders sayfasının yazdırılabilir biçimidir. |

## Çalışma yolu

Ders sayfası yukarıdan aşağıya okunur ve etkileşimli labın bölümlerini yeri geldikçe açar. Her uygulama durağında çalışma Jupyter Notebook'ta, iki yoldan biriyle sürer. **Prompt yolunda** (Jupyter Notebook'un 1. kısmı) kodu hazır promptlarla bir YZ asistanı yazar; katılımcı kodu çalıştırır ve sonucu denetler. **Python yolunda** (2. kısım) kodu katılımcı kendisi yazar. İki yol da aynı sonuçlara varır. Lab bölümlerinin ve Jupyter Notebook'taki durakların sonunda sizi ders sayfasına, okumanın devam ettiği yere geri götüren bir bağlantı vardır. Nerede kaldığınızı bulamazsanız bu tabloya dönün. Oturuma katılanlar adımları oturumda tamamlar. Süreler, haftayı kendi başına izleyenler, örneğin bir oturumu kaçıranlar içindir.

| Adım | Ne yapılır? | Prompt yolu (Kısım 1) | Python yolu (Kısım 2) |
|---|---|---|---|
| 1 | Haftanın vakasını ve ders sayfasını 1. uygulama durağına kadar [okuyun](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html): Uygulamanın iki yolu, sanal klinik ve Anaconda ile Jupyter Notebook'tan mini projeye kadar ilk iki saatin konuları bu kısımdadır | 50 dakika | 50 dakika |
| 2 | **[1. uygulama durağı: Mini proje: Kaggle Heart Disease veri seti](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-1)** | Kısım 1, Durak 1 ([promptlar](PROMPTLAR.md#durak-1-mini-proje-kaggle-heart-disease-veri-seti))<br>30 dakika | Python adımı 1, 1. ve 2. bölümler<br>1 saat 15 dakika |
| 3 | 2. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#last-two-hours-working-with-ecg-data): Veri olarak EKG, kalp vektörü, aralıklar ve QT düzeltmesi bu kısımdadır; etkileşimli labın A, B ve C bölümlerini yapın ve bilgi kontrolü sorularını cevaplayın | 1 saat | 1 saat |
| 4 | **[2. uygulama durağı: Veri olarak EKG](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-2)** | Kısım 1, Durak 2 ([promptlar](PROMPTLAR.md#durak-2-veri-olarak-ekg))<br>30 dakika | 3-5. bölümler<br>1 saat |
| 5 | 3. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#real-data-physionet-records): PhysioNet ve MIT-BIH, wfdb kütüphanesi, NeuroKit2 ile R-peak tespiti, HRV ve 12 derivasyon bu kısımdadır; etkileşimli labın D, E ve F bölümlerini yapın | 55 dakika | 55 dakika |
| 6 | **[3. uygulama durağı: Gerçek kayıtlar ve özensiz bir prompt](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-3)** | Kısım 1, Durak 3 ([promptlar](PROMPTLAR.md#durak-3-ger%C3%A7ek-kay%C4%B1tlar-ve-%C3%B6zensiz-bir-prompt))<br>35 dakika | 6-9. bölümler<br>1 saat 10 dakika |
| 7 | Haftanın makalesini, sanal kliniğin bu haftaki aşamasını ve "Kendi verinizle" bölümünü [okuyun](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-paper-of-the-week) | 30 dakika | 30 dakika |
| 8 | [Etkileşimli labın](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/lab.html) "Kendini sına" sekmesindeki öz değerlendirmeyi yapın, yansıtma yazınızı yazın ve öğrenme günlüğünü dışa aktarın | 20 dakika | 20 dakika |
| | **Haftalık proje dışında toplam** | **5 saat 10 dakika** | **7 saat** |
| 9 | [Haftalık projeyi](#haftal%C4%B1k-proje) iki yoldan biriyle tamamlayın | [Promptlar](PROMPTLAR.md#haftal%C4%B1k-projenin-prompt-yolu)<br>3 saat | 3 saat |

<table>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_b_bolumu_kalp_vektoru.png" alt="Etkileşimli lab, B bölümü: VC-0317'nin kalp vektörü üç boyutlu bir gövdenin içinde gösterilir ve on iki derivasyondaki izdüşümleri izlenir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_12_derivasyonlu_ekg.png" alt="Jupyter Notebook, Python yolu, 4. bölüm: VC-0317'nin 12 derivasyonlu EKG'si çizilir." width="100%"></td></tr>
<tr><td>Etkileşimli lab, B bölümü: VC-0317'nin kalp vektörü üç boyutlu bir gövdenin içinde gösterilir ve on iki derivasyondaki izdüşümleri izlenir.</td><td>Jupyter Notebook, Python yolu, 4. bölüm: VC-0317'nin 12 derivasyonlu EKG'si çizilir.</td></tr>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_f_bolumu_prompt_atolyesi.png" alt="Etkileşimli lab, F bölümü: Prompt atölyesinde prompt kartının yedi alanı doldurulur; bir kalite göstergesi ve bir mahremiyet denetimi yazılanı değerlendirir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_prompt_yolu.png" alt="Jupyter Notebook, prompt yolu, 2. durak: Hazır prompt bir YZ asistanına gönderilir, asistanın kodu çalıştırılır ve sonucu eğitimin kontrolü sınar." width="100%"></td></tr>
<tr><td>Etkileşimli lab, F bölümü: Prompt atölyesinde prompt kartının yedi alanı doldurulur; bir kalite göstergesi ve bir mahremiyet denetimi yazılanı değerlendirir.</td><td>Jupyter Notebook, prompt yolu, 2. durak: Hazır prompt bir YZ asistanına gönderilir, asistanın kodu çalıştırılır ve sonucu eğitimin kontrolü sınar.</td></tr>
</table>

## Haftalık proje

**Proje.** EKG görselleştirme ve temel ölçümleri (PR, QRS, QT) otomatik hesaplayan script.

**Ne yapılacak?** Önce Jupyter Notebook'un 5. bölümündeki `measure_ecg` fonksiyonunu alın ve onu, D1 ve aVF derivasyonlarının net QRS gerilimlerinden frontal QRS eksenini de hesaplayacak biçimde genişletin; bu iş için bir YZ asistanından yardım alabilirsiniz. İkinci olarak fonksiyonlarınızı haftanın klasöründe `ecg_measure.py` adlı bir script dosyası olarak kaydedin. Script bir EKG'yi (sanal klinikten bir hastayı ya da bir PhysioNet kaydını) okur, 12 derivasyonunu 8. bölümdeki standart düzende çizer ve kalp hızını, PR, QRS, QT ve QTc değerlerini yazdırır. Scripti Jupyter Notebook'ta `%run ecg_measure.py` komutuyla ya da Anaconda Prompt penceresinde `python ecg_measure.py` komutuyla çalıştırın. Üçüncü olarak scripti kendi seçeceğiniz on sanal klinik hastasında çalıştırın; bu hastaların en az ikisinde atriyal fibrilasyon ya da dal bloğu bulunmalıdır. Her ölçümü bir tabloda gerçek değerle karşılaştırın. Dördüncü olarak scripti 8. bölümdeki PTB kaydında çalıştırın ve MIT-BIH'in 100 numaralı kaydında kalp hızını ve kalp hızı değişkenliğini (ilk beş dakikanın SDNN ve RMSSD değerleri) bulunan atımlardan hesaplayarak raporlayın. Son olarak on hastanızın her biri için QTc'nin Bazett ve Fridericia formüllerine göre uzun olup olmadığına karar verin ve iki formülün farklı sonuç verdiği hastaları tartışın.

**Nereye bakılacak?** Ders sayfasında "Vektör olarak kalp: On iki derivasyon, tek kaynak", "Aralıklar: PR, QRS ve QT", "QT'nin kalp hızına göre düzeltilmesi", "Wfdb kütüphanesi ile EKG okuma ve işleme", "R-peak tespiti (NeuroKit2)", "HRV (kalp hızı değişkenliği) hesaplama", "12 derivasyon görselleştirme" ve "YZ asistanıyla çalışmak, 1. bölüm: Kod güvenlik kontrol listesi" bölümlerine bakın. Etkileşimli labda B, C, D, E ve F bölümleri, Jupyter Notebook'ta ise 4-9. bölümler ile E, F, H, I ve J alıştırmaları yardımcı olur.

**Prompt yolu.** Proje, [prompt kütüphanesindeki](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/PROMPTLAR.md#haftal%C4%B1k-projenin-prompt-yolu) dört promptla da tamamlanabilir; her adım için bir prompt vardır. Jupyter Notebook'un 1. kısmının sonundaki "Prompt yolunda haftalık proje" bölümü her promptun tablosunu hazırlar. Bir promptun testi sağlanmadan sonraki prompta geçilmez ve dört promptun tamamı YZ kullanım günlüğüne kaydedilir. Testleri geçen kod `ecg_measure.py` scripti olarak kaydedilir.

**Örnek.** D1'de 0,9 mV, aVF'de −0,3 mV net QRS gerilimi olan bir hastada $H_y = -0{,}3/0{,}866 = -0{,}346$ ve frontal eksen $\operatorname{atan2}(-0{,}346;\ 0{,}9) = -21{,}0°$ bulunur. Bu değer normal sınırlar içindedir. Başka bir hastada −45°'lik bir eksen, sol eksen sapmasını gösterirdi.

**Ne teslim edilecek?** `ecg_measure.py` scripti ve [rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılmış, bir ya da iki sayfalık bir rapor teslim edilir. Raporda on hastanızın tablosu, iki gerçek kaydın sonuçları ve iki QT düzeltmesinin tartışması yer almalıdır. Rapora YZ kullanım günlüğünü (kullanılan araç, prompt, neyin denetlendiği ve neyin değiştirildiği) ve 1. haftanın alıştırmalarını tamamladığınız Jupyter Notebook'u ekleyin.

**Teslim.** Haftalık proje, 2. haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. E-postaya "Ne teslim edilecek?" başlığında sayılan öğeler ve etkileşimli labdan dışa aktarılan öğrenme günlüğü eklenir. Haftalık projeler değerlendirmenin yüzde 40'ını oluşturur ve sertifika için her birinden en az yüzde 70 almak gerekir (izlenceye bakın).

## Öğrenme çıktıları

Haftanın sonunda katılımcıların Anaconda içinde Jupyter Notebook'u başlatabilmeleri, bir Jupyter Notebook'u açıp hücrelerini sırayla çalıştırabilmeleri ve kaydedebilmeleri beklenmektedir. Klinik değerlerle değişkenleri, listeleri, döngüleri, sözlükleri, koşulları ve fonksiyonları kullanabilmeli, pandas ile bir hasta tablosunu okuyup işleyebilmeli ve onu ortalama, standart sapma, medyan ve çeyrekler arası açıklıkla özetleyebilmelidirler. Matplotlib ile ilk kardiyolojik grafiği çizebilmeli ve Kaggle Heart Disease veri setiyle yapılan mini projeyi tamamlayabilmelidirler. Bir EKG'yi örneklerden oluşan bir tablo olarak ele alabilmeli, örnekleme frekansının ve çözünürlüğün etkisini açıklayabilmelidirler. On iki derivasyonu tek bir kalp vektörünün izdüşümleri olarak açıklayabilmeli, Einthoven yasasını uygulayabilmeli ve frontal QRS eksenini hesaplayabilmelidirler. PR, QRS ve QT aralıklarını elle ve bilgisayarla ölçebilmeli, QT'yi Bazett ve Fridericia formülleriyle düzeltebilmeli ve iki ölçüm yöntemini Bland-Altman analiziyle karşılaştırabilmelidirler. Ayrıca PhysioNet ve MIT-BIH veri setlerine erişebilmeli, bir kaydı wfdb kütüphanesiyle okuyup işleyebilmeli, R tepelerini NeuroKit2 ile bulabilmeli ve duyarlılığı ve pozitif öngörü değerini raporlayabilmelidirler. Normalden normale aralıkların standart sapmasını (SDNN) ve ardışık farklarının karelerinin ortalamasının karekökünü (RMSSD) hesaplayabilmeli ve 12 derivasyonu standart düzende görselleştirebilmelidirler. Son olarak birimleri ve bir testi içeren bir prompt yazabilmeli ve bir YZ asistanının yazdığı kodu kod güvenlik kontrol listesiyle denetleyebilmelidirler.

## Oturumun eğitim akışı

Haftanın dört saatlik oturumu aşağıdaki plana göre işlenir. Plan, malzemelerin canlı bir oturumda nasıl bir araya geldiğini göstermek için paylaşılmaktadır.

| Süre | Etkinlik |
|---|---|
| 0:00-0:15 | Haftanın vakası VC-0317 tanıtılır ve eğitimin rotası anlatılır: Ana rotayı ders sayfası oluşturur, uygulama iki yoldan yapılır ve sanal klinik eğitim boyunca kullanılır. |
| 0:15-0:40 | İlk iki saat, Python'a giriş ve Jupyter Notebook ortamı: Anaconda ve Jupyter Notebook ortamı tanıtılır ve ilk kez kullanılır. Her katılımcı Anaconda içinde Jupyter Notebook'u başlatır ya da Jupyter Notebook'u Google Colab'da açar ve 0. bölümü çalıştırır. |
| 0:40-1:05 | Değişkenler, listeler ve döngüler tıbbi örneklerle anlatılır; Python adımı 1'in ilk hücreleri ortak ekranda çalıştırılır. |
| 1:05-1:30 | Pandas ile hasta tablosu okunur ve işlenir; Matplotlib ile ilk kardiyolojik grafik çizilir. |
| 1:30-2:00 | Oturumun mini projesi, 1. uygulama durağı: Katılımcılar prompt yolu ve Python yolu olmak üzere iki gruba ayrılır. Kaggle Heart Disease veri seti yüklenir, istatistiksel olarak özetlenir ve görselleştirilir. |
| 2:00-2:10 | Ara. |
| 2:10-2:50 | Son iki saat, EKG verisi ile çalışma: EKG bir veri olarak ele alınır. Etkileşimli labın A ve B bölümleriyle on iki derivasyonun tek bir kalp vektöründen nasıl oluştuğu, C bölümüyle aralıklar ve QT düzeltmesi çalışılır. Ardından 2. uygulama durağına geçilir. |
| 2:50-3:35 | PhysioNet ve MIT-BIH veri setlerine erişim, wfdb kütüphanesi ile EKG okuma ve işleme, NeuroKit2 ile R-peak tespiti, D bölümüyle HRV hesaplama ve 12 derivasyon görselleştirme çalışılır; E ve F bölümleriyle kod güvenlik kontrol listesi ele alınır. Ardından 3. uygulama durağına geçilir. |
| 3:35-3:50 | Haftalık proje tanıtılır: EKG'yi görselleştiren ve PR, QRS ve QT aralıklarını otomatik olarak hesaplayan bir script yazılacaktır. Haftanın makalesi ve sanal kliniğin ilk aşaması da kısaca ele alınır. |
| 3:50-4:00 | Sorular cevaplanır. |

## Kendi verinizle

Ders sayfası, haftanın yöntemlerini kendi verinize nasıl uygulayacağınızı anlatan bir bölümle biter. Bu bölümde hangi sorunun hangi yönteme uyduğu, önce neyin denetleneceği, etik kurul onayı, Kişisel Verilerin Korunması Kanunu (KVKK) ve analizin nerede yapılacağı ele alınır. [Bölümü ders sayfasında okuyun](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#with-your-own-data).

## İsteğe bağlı araştırma ödevi

PubMed'de, 2023 ya da sonrasında yayımlanmış ve 12 derivasyonlu EKG için geliştirilmiş bir yapay zekâ modelini, modelin geliştirildiği hastanenin dışındaki bir hastanenin verileriyle sınayan bir çalışma bulun. Çalışmayı yarım sayfada özetleyin; özette hasta grubu, referans standart, başarım ölçütü ve çalışmanın bir sınırlılığı yer almalıdır. [Haftanın makalesindeki](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-paper-of-the-week) üç soru özetinize yön verebilir. Bu ödev notlandırılmaz; 2. haftadaki doğrulama tartışmasına hazırlık amacı taşır.

## Bu haftadan sonra sanal klinik

Sanal klinik 1. haftada açılır: 500 sentetik hastadan oluşan bir hasta kaydı ve her EKG'yi otomatik olarak ölçen bir EKG laboratuvarı kurulur. Bu aşamanın sonuçları ve otomatik ölçümün hataları, ders sayfasının [Sanal klinik, 1. aşama](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-virtual-clinic-stage-1-the-clinic-opens) bölümünde yer almaktadır.

## Gelecek hafta

**Hafta 2: Makine öğrenmesi temelleri.** Sanal klinik risk polikliniğini açar. UCI Heart Disease verisinde ve hasta kaydında koroner arter hastalığını öngören modeller kurulur ve bu modeller çapraz doğrulama ile alıcı işletim karakteristiği (ROC) analiziyle değerlendirilir. Ayrıntılar için [eğitimin planına](../../README.tr.md#on-bir-hafta) bakın.

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
