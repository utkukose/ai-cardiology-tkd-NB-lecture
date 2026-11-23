<div align="center">

# Hafta 1: Python ve kardiyoloji veri temelleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği

*Programlama bilgisi sıfırdan klinik veri analizine*

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [Kurulum](../../SETUP.tr.md) · [English](../../en/week-01/README.md)

</div>

Hafta hakkında daha ayrıntılı bilgi için bu sayfayı okumaya devam ediniz. Haftaya doğrudan ders sayfasından devam etmek isterseniz bu bağlantıyı kullanınız: **[Haftanın ders sayfasını açınız](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html)**. Ders sayfası haftanın ana rotasıdır; sayfadaki kutular etkileşimli labı ve Jupyter Notebook'u ilgili yerde açmaktadır.

## Hafta hakkında

İlk iki saatte önce Anaconda ve Jupyter Notebook ortamı tanıtılır. Ardından değişkenler, listeler ve döngüler tıbbi örneklerle öğrenilir, pandas ile bir hasta tablosu okunup işlenir ve Matplotlib ile ilk kardiyolojik grafik çizilir. Bu kısım Kaggle Heart Disease veri setiyle yapılan mini projeyle kapanır. Son iki saatte elektrokardiyogram (EKG) verisiyle çalışılır. EKG örneklerden oluşan bir veri olarak ele alınır ve on iki derivasyon tek bir kalp vektörünün izdüşümleri olarak açıklanır; ardından PR, QRS ve QT aralıkları otomatik olarak ölçülür ve QT kalp hızına göre düzeltilir. Ardından PhysioNet ve MIT-BIH veri setlerine erişilir, kayıtlar wfdb kütüphanesiyle okunup işlenir, R tepeleri NeuroKit2 ile bulunur, kalp hızı değişkenliği (HRV) hesaplanır ve 12 derivasyon görselleştirilir. Haftalık proje, EKG'yi görselleştiren ve temel ölçümleri (PR, QRS, QT) otomatik olarak hesaplayan bir script'tir. Hafta, bir yapay zekâ (YZ) asistanıyla kod yazmanın ilk kurallarını da içermektedir.

Oturum 4 saat sürer. Haftalık proje için yaklaşık 3 saat ayrılmalıdır.

## Haftanın vakası

**VC-0317, 67 yaşında bir kadın hastadır.** İlaç tedavisindeki bir değişiklikten sonra başlayan çarpıntı yakınmasıyla polikliniğe başvurmuştur. EKG'sinin otomatik raporu düzeltilmiş QT'yi (QTc) 465 ms olarak vermekte ve uzamış olarak işaretlemektedir. [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) bu vakayla açılır; sanal klinik de son bölümde soruyu kendi ölçümleriyle cevaplar.

## Malzemeler

| Malzeme | Aç | Ne işe yarar? |
|---|---|---|
| **Ders sayfası** | [Ders sayfasını aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) | Haftanın konu anlatımını içeren bu sayfa yukarıdan aşağıya doğru okunmak üzere hazırlanmıştır. Sayfadaki kutular sizi uygulama duraklarına yönlendirir; sayfada kod ya da prompt (istem) bulunmamaktadır. |
| **Etkileşimli lab** | [Etkileşimli labı aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/lab.html) | Kod gerektirmeyen A-F bölümleri, ders sayfasında yeri geldiğinde açılmaktadır. F bölümü bir prompt atölyesidir. Öz değerlendirme ve öğrenme günlüğü de bu labda yer alır. |
| **Python Notebook** | [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb)<br>[Jupyter Notebook için indir (zip)](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/raw/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.zip) | Uygulama durakları burada çalışılır; her durakta Python temelleri, promptlar ve hazır bir uygulama bulunmaktadır. Python Notebook, Google Colab'da kurulum gerektirmeden ya da kendi bilgisayarınızdaki Jupyter Notebook'ta çalışabilir. Jupyter için zip dosyasını indiriniz, içindeki .ipynb dosyasını bir klasöre çıkarınız ve dosyayı Jupyter'de açınız. Her bölüm, bölümün kullandığı kurulumu ve veri çağrılarını yineleyen bir başlangıç hücresiyle açılır. |
| **Prompt kütüphanesi** | [PROMPTLAR.md](PROMPTLAR.md) | Uygulama duraklarının ve haftalık projenin bütün promptları, kodu onarmaya, açıklatmaya ve denetlemeye yönelik promptlarla birlikte burada toplanmıştır. GitHub'da her promptun yanında bir kopyalama düğmesi bulunur. |
| **PDF ders notu** | [Hafta01_Ders_Notlari.pdf](Hafta01_Ders_Notlari.pdf) | Ders sayfasının yazdırılabilir biçimidir. |

## Çalışma yolu

Ders sayfası yukarıdan aşağıya doğru okunur; etkileşimli labın bölümleri de sayfada yeri geldikçe açılır. Uygulama duraklarında çalışma Jupyter Notebook'ta sürmektedir ve oradaki her durak üç bölümden oluşur. **Python temelleri** bölümünde durağın gerektirdiği Python bilgisi öğretilir. **Prompt ile uygulama** bölümünde kodu hazır promptlarla bir YZ asistanı yazar; katılımcının görevi bu kodu çalıştırmak ve sonucu denetlemektir. **Hazır uygulama** bölümünde ise durağın baştan sona çalışan programı yer almaktadır. Bölümleri bu sırayla izlemeniz önerilir; Python biliyorsanız promptlarla, yalnızca sonucu görmek istiyorsanız hazır uygulamayla başlayabilirsiniz. Her bölüm, bölümün kullandığı kurulumu ve veri çağrılarını yineleyen bir başlangıç hücresiyle açılır; bu sayede bölüm doğrudan açıldığında da çalışabilmektedir. Lab bölümlerinin ve Jupyter Notebook'taki durakların sonunda, sizi ders sayfasında okumanın devam ettiği yere geri götüren bir bağlantı bulunmaktadır. Nerede kaldığınızı bulamazsanız bu tabloya dönünüz. Oturuma katılanlar bu adımları oturum sırasında yapar. Tablodaki süreler, haftayı kendi başına izleyenler, örneğin bir oturumu kaçıranlar için verilmiştir.

| Adım | Ne yapılır? | Süre |
|---|---|---|
| 1 | Haftanın vakasını ve ders sayfasını 1. uygulama durağına kadar [okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html): Uygulama durakları, sanal klinik ve Anaconda ile Jupyter Notebook'tan mini projeye kadar ilk iki saatin konuları bu kısımdadır | 50 dakika |
| 2 | **[1. uygulama durağı: Mini proje: Kaggle Heart Disease veri seti](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-1)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-1-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-1-prompt) ([promptlar](PROMPTLAR.md#durak-1-mini-proje-kaggle-heart-disease-veri-seti)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-1-app) | 1 saat 15 dakika |
| 3 | 2. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#last-two-hours-working-with-ecg-data): Veri olarak EKG, kalp vektörü, aralıklar ve QT düzeltmesi bu kısımdadır; etkileşimli labın A, B ve C bölümlerini yapınız ve bilgi kontrolü sorularını cevaplayınız | 1 saat |
| 4 | **[2. uygulama durağı: Veri olarak EKG](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-2)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-2-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-2-prompt) ([promptlar](PROMPTLAR.md#durak-2-veri-olarak-ekg)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-2-app) | 1 saat |
| 5 | 3. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#real-data-physionet-records): PhysioNet ve MIT-BIH, wfdb kütüphanesi, NeuroKit2 ile R-peak tespiti, HRV ve 12 derivasyon bu kısımdadır; etkileşimli labın D, E ve F bölümlerini yapınız | 55 dakika |
| 6 | **[3. uygulama durağı: Gerçek kayıtlar ve özensiz bir prompt](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-3)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-3-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-3-prompt) ([promptlar](PROMPTLAR.md#durak-3-ger%C3%A7ek-kay%C4%B1tlar-ve-%C3%B6zensiz-bir-prompt)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=stop-3-app) | 1 saat 10 dakika |
| 7 | Haftanın makalesini, sanal kliniğin bu haftaki aşamasını ve "Kendi verinizle" bölümünü [okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-paper-of-the-week) | 30 dakika |
| 8 | [Etkileşimli labın](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/lab.html) "Kendini sına" sekmesindeki öz değerlendirmeyi yapınız, yansıtma yazınızı yazınız ve öğrenme günlüğünü dışa aktarınız | 20 dakika |
| | **Haftalık proje dışında toplam** | **7 saat** |
| 9 | [Haftalık projeyi](#haftal%C4%B1k-proje) tamamlayınız<br>[Promptlar](PROMPTLAR.md#haftal%C4%B1k-projenin-promptlar%C4%B1) · [Jupyter Notebook'ta haftalık proje](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb#scrollTo=project) | 3 saat |

<table>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_b_bolumu_kalp_vektoru.png" alt="Etkileşimli lab, B bölümü: VC-0317'nin kalp vektörü üç boyutlu bir gövdenin içinde gösterilir ve on iki derivasyondaki izdüşümleri izlenir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_12_derivasyonlu_ekg.png" alt="Jupyter Notebook, 2. uygulama durağı, hazır uygulama: VC-0317'nin 12 derivasyonlu EKG'si çizilir." width="100%"></td></tr>
<tr><td>Etkileşimli lab, B bölümü: VC-0317'nin kalp vektörü üç boyutlu bir gövdenin içinde gösterilir ve on iki derivasyondaki izdüşümleri izlenir.</td><td>Jupyter Notebook, 2. uygulama durağı, hazır uygulama: VC-0317'nin 12 derivasyonlu EKG'si çizilir.</td></tr>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_f_bolumu_prompt_atolyesi.png" alt="Etkileşimli lab, F bölümü: Prompt atölyesinde prompt kartının yedi alanı doldurulur; bir kalite göstergesi ve bir mahremiyet denetimi yazılanı değerlendirir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_prompt_yolu.png" alt="Jupyter Notebook, 2. uygulama durağı, prompt ile uygulama: Hazır prompt bir YZ asistanına gönderilir, asistanın kodu çalıştırılır ve sonucu eğitimin kontrolü sınar." width="100%"></td></tr>
<tr><td>Etkileşimli lab, F bölümü: Prompt atölyesinde prompt kartının yedi alanı doldurulur; bir kalite göstergesi ve bir mahremiyet denetimi yazılanı değerlendirir.</td><td>Jupyter Notebook, 2. uygulama durağı, prompt ile uygulama: Hazır prompt bir YZ asistanına gönderilir, asistanın kodu çalıştırılır ve sonucu eğitimin kontrolü sınar.</td></tr>
</table>

## Haftalık proje

**Proje.** EKG görselleştirme ve temel ölçümleri (PR, QRS, QT) otomatik hesaplayan script.

**Ne yapılacak?** Önce Jupyter Notebook'un 2. uygulama durağındaki hazır uygulamadan `measure_ecg` fonksiyonunu alınız ve onu, D1 ve aVF derivasyonlarının net QRS gerilimlerinden frontal QRS eksenini de hesaplayacak biçimde genişletiniz; bu iş için bir YZ asistanından yardım alabilirsiniz. İkinci olarak, fonksiyonlarınızı haftanın klasöründe `ecg_measure.py` adlı bir script dosyası olarak kaydediniz. Script önce bir EKG'yi (sanal klinikten bir hastayı ya da bir PhysioNet kaydını) okumalı ve 12 derivasyonunu 3. uygulama durağındaki standart düzende çizmelidir. Ardından kalp hızını, PR, QRS, QT ve QTc değerlerini yazdırmalıdır. Scripti Jupyter Notebook'ta `%run ecg_measure.py` komutuyla ya da Anaconda Prompt penceresinde `python ecg_measure.py` komutuyla çalıştırınız. Üçüncü olarak, scripti kendi seçeceğiniz on sanal klinik hastasında çalıştırınız; bu hastaların en az ikisinde atriyal fibrilasyon ya da dal bloğu bulunmalıdır. Her ölçümü bir tabloda gerçek değerle karşılaştırınız. Dördüncü olarak, scripti 3. uygulama durağındaki PTB kaydında çalıştırınız ve MIT-BIH'in 100 numaralı kaydında kalp hızını ve kalp hızı değişkenliğini (ilk beş dakikanın SDNN ve RMSSD değerleri) bulunan atımlardan hesaplayarak raporlayınız. Son olarak, on hastanızın her biri için QTc'nin Bazett ve Fridericia formüllerine göre uzun olup olmadığına karar veriniz ve iki formülün farklı sonuç verdiği hastaları tartışınız.

**Nereye bakılacak?** Ders sayfasında "Vektör olarak kalp: On iki derivasyon, tek kaynak", "Aralıklar: PR, QRS ve QT", "QT'nin kalp hızına göre düzeltilmesi", "wfdb kütüphanesi ile EKG okuma ve işleme", "R-peak tespiti (NeuroKit2)", "HRV (kalp hızı değişkenliği) hesaplama", "12 derivasyon görselleştirme" ve "YZ asistanıyla çalışmak, 1. bölüm: Kod güvenlik kontrol listesi" bölümlerine bakınız. Etkileşimli labda B, C, D, E ve F bölümleri, Jupyter Notebook'ta ise 2. ve 3. uygulama duraklarının hazır uygulamaları, Alıştırma 2.2, 2.3 ve 3.1 ile Prompt 2.3, 3.1 ve 3.4 yardımcı olur.

**Promptlarla.** Proje, [prompt kütüphanesindeki](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/PROMPTLAR.md#haftal%C4%B1k-projenin-promptlar%C4%B1) dört promptla da yapılabilir; kütüphanede her adım için bir prompt bulunmaktadır. Her promptun tablosu, Jupyter Notebook'un sonundaki "Haftalık proje" bölümünde hazırlanır ve bu bölüm tek başına da açılabilir. Bir promptun testi sağlanmadan sonraki prompta geçilmemeli ve dört promptun tamamı YZ kullanım günlüğüne kaydedilmelidir. Testleri geçen kod `ecg_measure.py` scripti olarak kaydedilir.

**Örnek.** D1'de 0,9 mV, aVF'de −0,3 mV net QRS gerilimi olan bir hastada $H_y = -0{,}3/0{,}866 = -0{,}346$ ve frontal eksen $\operatorname{atan2}(-0{,}346;\ 0{,}9) = -21{,}0°$ bulunur. Bu değer normal sınırlar içindedir. Başka bir hastada −45°'lik bir eksen, sol eksen sapmasını gösterirdi.

**Ne teslim edilecek?** `ecg_measure.py` scripti ve [rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılmış, bir ya da iki sayfalık bir rapor teslim edilir. Raporda on hastanızın tablosu, iki gerçek kaydın sonuçları ve iki QT düzeltmesinin tartışması yer almalıdır. Rapora YZ kullanım günlüğünü (kullanılan araç, prompt, neyin denetlendiği ve neyin değiştirildiği) ve 1. haftanın alıştırmalarını tamamladığınız Jupyter Notebook'u ekleyiniz.

**Teslim.** Haftalık proje, 2. haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. E-postaya "Ne teslim edilecek?" başlığında sayılan öğeler ve etkileşimli labdan dışa aktarılan öğrenme günlüğü eklenir. Haftalık projeler değerlendirmenin yüzde 40'ını oluşturur ve sertifika için her birinden en az yüzde 70 almak gerekir (izlenceye bakınız).

## Öğrenme çıktıları

Haftanın sonunda katılımcıların Anaconda içinde Jupyter Notebook'u başlatabilmeleri, bir Jupyter Notebook'u açıp hücrelerini sırayla çalıştırabilmeleri ve kaydedebilmeleri beklenmektedir. Klinik değerlerle değişkenleri, listeleri, döngüleri, sözlükleri, koşulları ve fonksiyonları kullanabilmeli, pandas ile bir hasta tablosunu okuyup işleyebilmeli ve onu ortalama, standart sapma, medyan ve çeyrekler arası açıklıkla özetleyebilmelidirler. Matplotlib ile ilk kardiyolojik grafiği çizebilmeli ve Kaggle Heart Disease veri setiyle yapılan mini projeyi tamamlayabilmelidirler. Bir EKG'yi örneklerden oluşan bir tablo olarak ele alabilmeli, örnekleme frekansının ve çözünürlüğün etkisini açıklayabilmelidirler. On iki derivasyonu tek bir kalp vektörünün izdüşümleri olarak açıklayabilmeli, Einthoven yasasını uygulayabilmeli ve frontal QRS eksenini hesaplayabilmelidirler. PR, QRS ve QT aralıklarını elle ve bilgisayarla ölçebilmeli, QT'yi Bazett ve Fridericia formülleriyle düzeltebilmeli ve iki ölçüm yöntemini Bland-Altman analiziyle karşılaştırabilmelidirler. Ayrıca PhysioNet ve MIT-BIH veri setlerine erişebilmeli, bir kaydı wfdb kütüphanesiyle okuyup işleyebilmeli, R tepelerini NeuroKit2 ile bulabilmeli ve duyarlılığı ve pozitif öngörü değerini raporlayabilmelidirler. Normalden normale aralıkların standart sapmasını (SDNN) ve ardışık farklarının karelerinin ortalamasının karekökünü (RMSSD) hesaplayabilmeli ve 12 derivasyonu standart düzende görselleştirebilmelidirler. Son olarak, birimleri ve bir testi içeren bir prompt yazabilmeli ve bir YZ asistanının yazdığı kodu kod güvenlik kontrol listesiyle denetleyebilmelidirler.

## Oturumun eğitim akışı

Haftanın dört saatlik oturumu aşağıdaki plana göre işlenir. Plan, malzemelerin canlı bir oturumda nasıl bir araya geldiğini göstermek için paylaşılmaktadır.

| Süre | Etkinlik |
|---|---|
| 0:00-0:15 | Haftanın vakası VC-0317 tanıtılır ve eğitimin rotası anlatılır: Ana rotayı ders sayfası oluşturur, uygulama durakları Jupyter Notebook'ta üç bölümle çalışılır ve sanal klinik eğitim boyunca kullanılır. |
| 0:15-0:40 | İlk iki saat, Python'a giriş ve Jupyter Notebook ortamı: Anaconda ve Jupyter Notebook ortamı tanıtılır ve ilk kez kullanılır. Her katılımcı Jupyter Notebook'u Anaconda içinde başlatarak ya da Google Colab'da açarak 0. bölümü çalıştırır. |
| 0:40-1:05 | Değişkenler, listeler ve döngüler tıbbi örneklerle anlatılır; 1. uygulama durağının Python temellerindeki ilk hücreler ortak ekranda çalıştırılır. |
| 1:05-1:30 | Hasta tablosu pandas ile okunur ve işlenir; Matplotlib ile ilk kardiyolojik grafik çizilir. |
| 1:30-2:00 | Oturumun mini projesi, 1. uygulama durağı: Kaggle Heart Disease veri seti yüklenir, istatistiksel olarak özetlenir ve görselleştirilir. Katılımcılar kendi düzeylerine göre Python temelleri, promptlar ya da hazır uygulamayla çalışır. Veri hücresi bir kez de bilgisayar kaynağıyla, katılımcının kendi bilgisayarına indirdiği dosya üzerinde çalıştırılır. |
| 2:00-2:10 | Ara. |
| 2:10-2:50 | Son iki saat, EKG verisi ile çalışma: EKG bir veri olarak ele alınır. Etkileşimli labın A ve B bölümleriyle on iki derivasyonun tek bir kalp vektöründen nasıl oluştuğu, C bölümüyle aralıklar ve QT düzeltmesi çalışılır. Ardından 2. uygulama durağına geçilir. |
| 2:50-3:35 | PhysioNet ve MIT-BIH veri setlerine erişim, wfdb kütüphanesi ile EKG okuma ve işleme, NeuroKit2 ile R-peak tespiti, D bölümüyle HRV hesaplama ve 12 derivasyon görselleştirme çalışılır; E ve F bölümleriyle kod güvenlik kontrol listesi ele alınır. Ardından 3. uygulama durağına geçilir. |
| 3:35-3:50 | Haftalık proje tanıtılır: EKG'yi görselleştiren ve PR, QRS ve QT aralıklarını otomatik olarak hesaplayan bir script yazılacaktır. Haftanın makalesi ve sanal kliniğin ilk aşaması da kısaca ele alınır. |
| 3:50-4:00 | Sorular cevaplanır. |

## Kendi verinizle

Ders sayfası, haftanın yöntemlerini kendi verilerinize nasıl uygulayabileceğinizi anlatan bir bölümle sona ermektedir. Bu bölümde hangi sorunun hangi yönteme uyduğu, önce neyin denetlenmesi gerektiği, etik kurul onayı, Kişisel Verilerin Korunması Kanunu (KVKK) ve analizin nerede yapılacağı ele alınmaktadır. [Bölümü ders sayfasında okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#with-your-own-data).

## İsteğe bağlı araştırma ödevi

PubMed'de, 2023 ya da sonrasında yayımlanmış ve 12 derivasyonlu EKG için geliştirilmiş bir yapay zekâ modelini, modelin geliştirildiği hastanenin dışındaki bir hastanenin verileriyle sınayan bir çalışma bulunuz. Çalışmayı yarım sayfada özetleyiniz; özette hasta grubu, referans standart, başarım ölçütü ve çalışmanın bir sınırlılığı yer almalıdır. [Haftanın makalesindeki](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-paper-of-the-week) üç soru özetinize yön verebilir. Bu ödev notlandırılmaz; 2. haftadaki doğrulama tartışmasına hazırlık amacı taşır.

## Bu haftadan sonra sanal klinik

Sanal klinik 1. haftada açılır: 500 sentetik hastadan oluşan bir hasta kaydı ve her EKG'yi otomatik olarak ölçen bir EKG laboratuvarı kurulur. Bu aşamanın sonuçları ve otomatik ölçümün hataları, ders sayfasının [Sanal klinik, 1. aşama](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-virtual-clinic-stage-1-the-clinic-opens) bölümünde yer almaktadır.

## Gelecek hafta

**Hafta 2: Makine öğrenmesi temelleri.** Sanal klinik risk polikliniğini açar. UCI Heart Disease verisinde ve hasta kaydında koroner arter hastalığını öngören modeller kurulur ve bu modeller çapraz doğrulama ile alıcı işletim karakteristiği (ROC) analiziyle değerlendirilir. Ayrıntılar için [eğitimin planına](../../README.tr.md#on-bir-hafta) bakınız.

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
