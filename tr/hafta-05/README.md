<div align="center">

# Hafta 5: Zaman serisi analizi ve EKG yapay zekâsı

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği

*EKG'den otomatik tanı: 12 derivasyon tam analiz*

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [Kurulum](../../SETUP.tr.md) · [English](../../en/week-05/README.md)

</div>

Hafta hakkında daha ayrıntılı bilgi için bu sayfayı okumaya devam ediniz. Haftaya doğrudan ders sayfasından devam etmek isterseniz bu bağlantıyı kullanınız: **[Haftanın ders sayfasını açınız](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html)**. Ders sayfası haftanın ana rotasıdır; sayfadaki kutular etkileşimli labı ve Jupyter Notebook'u ilgili yerde açmaktadır.

## Hafta hakkında

İlk iki saatte elektrokardiyogram (EKG) 1D CNN ve LSTM ile analiz edilir. EKG, 21.799 klinik kaydı içeren herkese açık PTB-XL veri setinin 12 derivasyonlu EKG'lerinde bir zaman serisi, yani sıralarıyla saklanan sayılardan oluşan on iki derivasyon olarak modellenir. Atriyal fibrilasyon (AF), önce bir kardiyoloğun yapacağı gibi RR aralıklarına dayanan bir kuralla tespit edilir. Ardından birkaç ritim etiketini aynı anda öğrenen tek boyutlu evrişimli bir ağ (1D CNN) kurulmakta; AF, ventriküler taşikardi (VT) ve supraventriküler taşikardiyi (SVT) birbirinden ayıran özellikler de EKG'de ve sentetik kayıtlarda izlenmektedir. RR aralıkları bir GRU ve bir LSTM ile dizi olarak okunur; mini projede ise PhysioNet 2020 Challenge'ın dokuz sınıfı çok etiketli sınıflandırmayla tespit edilir. Son iki saat gelişmiş EKG modellerine ve klinik entegrasyona ayrılmıştır: Akut miyokard enfarktüsünde (AMI) ST yükselmesi ve çökmesinin bir STEMI alarmı olarak otomatik tespiti, bir QTc uzaması risk algoritması, sanal kliniğin 24 saatlik sentetik kaydı üzerinde Holter analizi ve FDA/CE onaylı yapay zekâ (YZ) tabanlı EKG ürünlerine genel bir bakış. Hafta, bir YZ asistanının yazdığı bir zaman serisi işlem hattının denetlenmesiyle kapanır.

Oturum 4 saat sürer. Haftalık proje için yaklaşık 3 saat ayrılmalıdır.

## Haftanın vakası

PTB-XL'in 13913 numaralı kaydı, sinüs taşikardisi ve akut anterior ve lateral enfarktüsü olan 68 yaşında bir erkeğe aittir. Bir program kaydın 12.000 sayısından hangi ritmi bildirir, bir STEMI alarmı verir mi ve böyle bir alarm ne sıklıkla doğru çıkar?

## Malzemeler

| Malzeme | Aç | Ne işe yarar? |
|---|---|---|
| **Ders sayfası** | [Ders sayfasını aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html) | Haftanın konu anlatımını içeren bu sayfa yukarıdan aşağıya doğru okunmak üzere hazırlanmıştır. Sayfadaki kutular sizi uygulama duraklarına yönlendirir; sayfada kod ya da prompt (istem) bulunmamaktadır. |
| **Etkileşimli lab** | [Etkileşimli labı aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/lab.html) | Kod gerektirmeyen A-F bölümleri, ders sayfasında yeri geldiğinde açılmaktadır. F bölümü bir prompt atölyesidir. Öz değerlendirme ve öğrenme günlüğü de bu labda yer alır. |
| **Python Notebook** | [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb)<br>[Jupyter Notebook için indir (zip)](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/raw/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.zip) | Uygulama durakları burada çalışılır; her durakta Python temelleri, promptlar ve hazır bir uygulama bulunmaktadır. Python Notebook, Google Colab'da kurulum gerektirmeden ya da kendi bilgisayarınızdaki Jupyter Notebook'ta çalışabilir. Jupyter için zip dosyasını indiriniz, içindeki .ipynb dosyasını bir klasöre çıkarınız ve dosyayı Jupyter'de açınız. Her bölüm, bölümün kullandığı kurulumu ve veri çağrılarını yineleyen bir başlangıç hücresiyle açılır. |
| **Prompt kütüphanesi** | [PROMPTLAR.md](PROMPTLAR.md) | Uygulama duraklarının ve haftalık projenin bütün promptları, kodu onarmaya, açıklatmaya ve denetlemeye yönelik promptlarla birlikte burada toplanmıştır. GitHub'da her promptun yanında bir kopyalama düğmesi bulunur. |
| **PDF ders notu** | [Hafta05_Ders_Notlari.pdf](Hafta05_Ders_Notlari.pdf) | Ders sayfasının yazdırılabilir biçimidir. |

## Çalışma yolu

Ders sayfası yukarıdan aşağıya doğru okunur; etkileşimli labın bölümleri de sayfada yeri geldikçe açılır. Uygulama duraklarında çalışma Jupyter Notebook'ta sürmektedir ve oradaki her durak üç bölümden oluşur. **Python temelleri** bölümünde durağın gerektirdiği Python bilgisi öğretilir. **Prompt ile uygulama** bölümünde kodu hazır promptlarla bir YZ asistanı yazar; katılımcının görevi bu kodu çalıştırmak ve sonucu denetlemektir. **Hazır uygulama** bölümünde ise durağın baştan sona çalışan programı yer almaktadır. Bölümleri bu sırayla izlemeniz önerilir; Python biliyorsanız promptlarla, yalnızca sonucu görmek istiyorsanız hazır uygulamayla başlayabilirsiniz. Her bölüm, bölümün kullandığı kurulumu ve veri çağrılarını yineleyen bir başlangıç hücresiyle açılır; bu sayede bölüm doğrudan açıldığında da çalışabilmektedir. Lab bölümlerinin ve Jupyter Notebook'taki durakların sonunda, sizi ders sayfasında okumanın devam ettiği yere geri götüren bir bağlantı bulunmaktadır. Nerede kaldığınızı bulamazsanız bu tabloya dönünüz. Oturuma katılanlar bu adımları oturum sırasında yapar. Tablodaki süreler, haftayı kendi başına izleyenler, örneğin bir oturumu kaçıranlar için verilmiştir.

| Adım | Ne yapılır? | Süre |
|---|---|---|
| 1 | Haftanın vakasını ve ders sayfasının ilk iki saatini 1. uygulama durağına kadar [okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html) (zaman serisi olarak EKG, AF, VT ve SVT için 1D CNN, LSTM, çok etiketli sınıflandırma ve mini proje); etkileşimli labın A, B ve C bölümlerini yapınız ve bilgi kontrolü sorularını cevaplayınız | 1 saat 10 dakika |
| 2 | **[1. uygulama durağı: Mini proje: Ritim, bir kuraldan PhysioNet 2020 Challenge'ın dokuz sınıfına](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#stop-1)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-1-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-1-prompt) ([promptlar](PROMPTLAR.md#durak-1-mini-proje-ritim-bir-kuraldan-physionet-2020-challenge%C4%B1n-dokuz-s%C4%B1n%C4%B1f%C4%B1na)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-1-app) | 1 saat 50 dakika |
| 3 | 2. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#last-two-hours-advanced-ecg-models-and-clinical-integration) (3B sahneyle AMI'de ST yükselmesi ve çökmesinin otomatik tespiti, otomatik ST ölçümü); etkileşimli labın D bölümünü yapınız | 40 dakika |
| 4 | **[2. uygulama durağı: ST yükselmesi: Medyan atım, J noktası ve alarm](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#stop-2)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-2-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-2-prompt) ([promptlar](PROMPTLAR.md#durak-2-st-y%C3%BCkselmesi-medyan-at%C4%B1m-j-noktas%C4%B1-ve-alarm)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-2-app) | 50 dakika |
| 5 | 3. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#qt-prolongation-and-its-risk) (QTc uzaması risk algoritması ve Holter analizi); Holter kaydının animasyonunu inceleyiniz | 35 dakika |
| 6 | **[3. uygulama durağı: Uzun süreli izlem: Pencereler, AF yükü ve yanlış alarmlar](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#stop-3)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-3-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-3-prompt) ([promptlar](PROMPTLAR.md#durak-3-uzun-s%C3%BCreli-izlem-pencereler-af-y%C3%BCk%C3%BC-ve-yanl%C4%B1%C5%9F-alarmlar)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=stop-3-app) | 45 dakika |
| 7 | FDA/CE onaylı EKG ürünlerine genel bakışı, zaman serisi işlem hattı denetimini, haftanın makalesini, sanal kliniğin bu haftaki aşamasını ve "Kendi verinizle" bölümünü [okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#ecg-algorithms-with-regulatory-approval); etkileşimli labın E ve F bölümlerini yapınız ve Jupyter Notebook'ta uygulama duraklarından sonra gelen bölümü çalışınız | 55 dakika |
| 8 | [Etkileşimli labın](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/lab.html) "Kendini sına" sekmesindeki öz değerlendirmeyi yapınız, yansıtma yazınızı yazınız ve öğrenme günlüğünü dışa aktarınız | 20 dakika |
| | **Haftalık proje dışında toplam** | **7 saat 5 dakika** |
| 9 | [Haftalık projeyi](#haftal%C4%B1k-proje) tamamlayınız<br>[Promptlar](PROMPTLAR.md#haftal%C4%B1k-projenin-promptlar%C4%B1) · [Jupyter Notebook'ta haftalık proje](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb#scrollTo=project) | 3 saat |

<table>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_b_bolumu_rr_kurali.png" alt="Etkileşimli lab, B bölümü: Test katındaki değişim katsayıları, AF kuralının eşiği, alarmlar, duyarlılık, özgüllük ve pozitif öngörü değeri; altta ventriküler erken vurulu bir kaydın RR aralıkları görülmektedir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_12_derivasyonlu_vaka.png" alt="Jupyter Notebook, «Durak 1 · Hazır uygulama»: PTB-XL'den haftanın vakasının 12 derivasyonlu EKG'si." width="100%"></td></tr>
<tr><td>Etkileşimli lab, B bölümü: Test katındaki değişim katsayıları, AF kuralının eşiği, alarmlar, duyarlılık, özgüllük ve pozitif öngörü değeri; altta ventriküler erken vurulu bir kaydın RR aralıkları görülmektedir.</td><td>Jupyter Notebook, «Durak 1 · Hazır uygulama»: PTB-XL'den haftanın vakasının 12 derivasyonlu EKG'si.</td></tr>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_d_bolumu_st.png" alt="Etkileşimli lab, D bölümü: Vakanın on iki derivasyonunun medyan atımları PR düzeyi ve J noktasıyla birlikte çizilir; panel STEMI alarmının kararını verir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/ders_holter_pencereleri.png" alt="Ders sayfası: Sanal kliniğin 24 saatlik Holter kaydının pencereleri, alarmın eşiği ve yanlış alarmları." width="100%"></td></tr>
<tr><td>Etkileşimli lab, D bölümü: Vakanın on iki derivasyonunun medyan atımları PR düzeyi ve J noktasıyla birlikte çizilir; panel STEMI alarmının kararını verir.</td><td>Ders sayfası: Sanal kliniğin 24 saatlik Holter kaydının pencereleri, alarmın eşiği ve yanlış alarmları.</td></tr>
</table>

## Haftalık proje

**Proje.** STEMI alarm sistemi: AMI EKG'lerinden ST deviasyonu otomatik tespiti (PTB-XL).

**Ne yapılacak?** PTB-XL'in 12 derivasyonlu EKG'lerinde otomatik bir STEMI alarmı kurunuz ve bu alarmı bir göğüs ağrısı biriminin yapacağı gibi değerlendiriniz. Önce 9. ve 10. katlardaki her kaydın medyan atımında on iki derivasyonun J noktasındaki ST sapmasını ölçünüz. İkinci adımda evrensel tanımın ölçütlerini uygulayınız: V2 ve V3 için cinsiyete ve yaşa göre eşikleri, öteki derivasyonlar için 1 mm'yi ve üç derivasyon grubunu kullanınız; bir gruptaki iki derivasyon eşiğine ulaştığında alarm çalar. Üçüncü adımda alarmı iki kattaki akut miyokard enfarktüsleriyle, yani enfarktüs evresi Stadium I ya da Stadium I-II olan kayıtlarla karşılaştırınız. Duyarlılığı, özgüllüğü ve pozitif öngörü değerini bildiriniz; yanlış alarmları da kayıtların ifadelerine göre, örneğin sol dal bloğu, sol ventrikül hipertrofisi ve normal EKG olarak sayınız. Son olarak gözden kaçan üç enfarktüsü ve ST yükselmesi en büyük üç yanlış alarmı medyan atımlarıyla gösteriniz. Alarmın bir acil serviste çalışabilmesi için nelere ihtiyaç duyacağını da yarım sayfada yazınız.

**Nereye bakılacak?** Ders: "ST-yükselmesi/depresyonu otomatik tespiti (AMI)" bölümü ve bu bölümün "ST yükselmesi ve çökmesi: Evrensel tanımın ölçütleri" ve "ST segmentini otomatik ölçmek: Medyan atım ve J noktası" alt bölümleri. Etkileşimli lab: D bölümü. Jupyter Notebook: 2. uygulama durağının hazır uygulaması.

**Promptlarla.** Proje, [prompt kütüphanesindeki](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-05/PROMPTLAR.md#haftal%C4%B1k-projenin-promptlar%C4%B1) dört promptla da yapılabilir; kütüphanede her adım için bir prompt bulunmaktadır. Her promptun tablosu, Jupyter Notebook'un sonundaki "Haftalık proje" bölümünde hazırlanır ve bu bölüm tek başına da açılabilir. Bir promptun testi sağlanmadan sonraki prompta geçilmemeli ve her prompt YZ kullanım günlüğüne kaydedilmelidir.

**Örnek.** Alarmın 40 akut enfarktüsün 30'unda ve öteki 4.000 kaydın 60'ında çaldığını varsayınız. Duyarlılık $30/40 = 0{,}75$, özgüllük $(4000 - 60)/4000 = 3940/4000 = 0{,}985$, pozitif öngörü değeri ise $30/(30 + 60) = 0{,}333$ olur. Alarm enfarktüsü olmayan kayıtların yüzde 98,5'inde doğru karar verdiği hâlde her üç alarmdan ikisi yanlıştır.

**Ne teslim edilecek?** [Rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılmış, bir ya da iki sayfalık bir rapor teslim edilir. Raporda duyarlılık, özgüllük ve pozitif öngörü değeri tablosu, yanlış alarmların ifadelere göre sayımı, altı medyan atımın şekli ve alarmın neye ihtiyaç duyacağını anlatan yarım sayfa yer almalıdır. Rapora YZ kullanım günlüğünü (kullanılan araç, prompt, neyin denetlendiği ve neyin değiştirildiği) ve çıktılarıyla birlikte Jupyter Notebook'u ekleyiniz. PTB-XL EKG'leri içeren şekiller "PTB-XL, CC BY 4.0" kaynak bilgisini taşımalıdır.

**Teslim.** Haftalık proje, 6. haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. E-postaya "Ne teslim edilecek?" başlığında sayılan öğeler ve etkileşimli labdan dışa aktarılan öğrenme günlüğü eklenir. Haftalık projeler değerlendirmenin yüzde 40'ını oluşturur; değerlendirme ölçütleri izlencede yer almaktadır.

## Öğrenme çıktıları

Haftanın sonunda katılımcıların bir EKG'yi zaman serisi olarak modelleyebilmeleri, örnekleme frekansını ve etiketlerini açıklayabilmeleri ve bir hastanın kayıtlarını tek bir kümede tutabilmeleri beklenmektedir. AF'yi RR aralıklarına dayanan bir kuralla tespit edebilmeli, tek boyutlu evrişimi ve alıcı alanını açıklayabilmeli ve AF, VT ile SVT'yi RR aralıklarının düzeni, QRS kompleksinin genişliği ve P dalgalarıyla birbirinden ayırabilmelidirler. LSTM ve GRU kapılarının temporal bağımlılıkları nasıl yakaladığını açıklayabilmeli ve çok etiketli bir ağı, PhysioNet 2020 Challenge'ın dokuz sınıfında olduğu gibi, eşikleri bir doğrulama kümesinde seçilmiş olarak etiket etiket değerlendirebilmelidirler. Son olarak ST segmentini bir medyan atımda ölçebilmeli, evrensel tanımın ST yükselmesi ölçütlerini bir alarm olarak uygulayıp yanlış alarmlarını değerlendirebilmeli, bir QTc uzaması risk skoru hesaplayabilmeli, 24 saatlik bir kaydı pencereler hâlinde okuyabilmeli ve bir EKG ürününün onayının neyi kapsadığını söyleyebilmelidirler.

## Oturumun eğitim akışı

Haftanın dört saatlik oturumu aşağıdaki plana göre işlenir. Plan, malzemelerin canlı bir oturumda nasıl bir araya geldiğini göstermek için paylaşılmaktadır.

| Süre | Etkinlik |
|---|---|
| 0:00-0:15 | Haftanın vakası tanıtılır ve haftanın rotası anlatılır. Her katılımcı Jupyter Notebook'u Google Colab'da ya da Jupyter'de açarak 0. bölümü çalıştırır. Bu bölüm, PTB-XL'in dört katındaki 100 Hz'lik 12 derivasyonlu EKG'leri (yaklaşık 216 MB) PhysioNet'ten indirir. |
| 0:15-0:55 | İlk iki saat, 1D CNN ve LSTM ile EKG analizi: EKG bir zaman serisi olarak modellenir; B bölümüyle RR aralıklarına dayanan bir AF kuralı, A bölümüyle tek boyutlu evrişim çalışılır. Ardından EKG'de ve ağda AF, VT ve SVT, LSTM ve GRU ile etkileşimli labın C bölümüyle çok etiketli sınıflandırma anlatılır. |
| 0:55-1:45 | Oturumun mini projesi olan 1. uygulama durağında katılımcılar Jupyter Notebook'ta, promptlarla ya da Python ile, PhysioNet 2020 Challenge'ın dokuz sınıfı üzerinde çalışır. Tek boyutlu bir ağ PTB-XL'in ritim etiketlerini yaklaşık iki dakikada öğrenir; eşikleri 9. katta seçilir ve ağ 10. katta kuralla karşılaştırılır. Durağın hazır uygulaması ardından ağı Challenge'ın dokuz sınıfı için eğitir. |
| 1:45-2:00 | Ara. |
| 2:00-2:35 | Son iki saat, gelişmiş EKG modelleri ve klinik entegrasyon: AMI'de ST yükselmesi ve çökmesinin otomatik tespiti 3B sahne, evrensel tanımın ölçütleri ve D bölümüyle medyan atım ve J noktası üzerinden çalışılır. Ardından 2. uygulama durağında vakanın ST sapması ve test katındaki alarm hesaplanır. |
| 2:35-3:20 | QTc uzaması risk algoritması ve sanal kliniğin 24 saatlik kaydıyla Holter analizi anlatılır. 3. uygulama durağında dört yatan hastanın risk skoru, pencereler, AF yükü ve bir günün yanlış alarmları çalışılır. |
| 3:20-4:00 | FDA/CE onaylı EKG yapay zekâ ürünlerine genel bir bakış sunulur; etkileşimli labın E ve F bölümleriyle bir zaman serisi işlem hattının denetimi çalışılır. Ardından haftanın makalesi, sanal kliniğin ritim ve STEMI alarmı, "Kendi verinizle" bölümü ve haftalık proje ele alınır. |

## Kendi verinizle

Ders sayfası, haftanın yöntemlerini kendi verilerinize nasıl uygulayabileceğinizi anlatan bir bölümle sona ermektedir. Bu bölümde hangi sorunun hangi yönteme uyduğu, önce neyin denetlenmesi gerektiği, etik kurul onayı, Kişisel Verilerin Korunması Kanunu (KVKK) ve analizin nerede yapılacağı ele alınmaktadır. [Bölümü ders sayfasında okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#with-your-own-data).

## İsteğe bağlı araştırma ödevi

PubMed'de, 2020 ya da sonrasında yayımlanmış ve atriyal fibrilasyonu ya da akut miyokard enfarktüsünü EKG'lerde otomatik olarak tespit edip algoritmayı kardiyologlarla karşılaştıran bir çalışma bulunuz. Çalışmayı yarım sayfada özetleyiniz. Özette hastalar, hastaneler ve cihazlar, referansın nasıl ve kaç okuyucu tarafından verildiği, duyarlılık, özgüllük ve pozitif öngörü değeri, test kümesindeki prevalans ve testin başka bir hastanede yapılıp yapılmadığı yer almalıdır. [Haftanın makalesindeki](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#the-paper-of-the-week) üç soru özete yol gösterebilir. Ödev notlandırılmaz; haftalık projedeki yarım sayfalık metne hazırlık niteliğindedir.

## Bu haftadan sonra sanal klinik

5. haftada sanal kliniğe bir ritim ve STEMI alarmı eklenir. Kliniğin 500 hastasının istirahat EKG'leri, PTB-XL ile eğitilmiş tek boyutlu bir ağ ve ST yükselmesi ölçütleriyle okunmaktadır. Bir hastanın 24 saatlik sentetik Holter kaydı ise uzun süreli izlemdeki pencereleri ve yanlış alarmları gösterir. Sonuçlar ders sayfasının [Sanal klinik, 5. aşama](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html#the-virtual-clinic-stage-5-rhythm-and-stemi-alarm) bölümünde yer almaktadır.

## Gelecek hafta

**Hafta 6: NLP ve klinik metin madenciliği.** Kliniğin raporları veriye dönüştürülür: Türkçe ve İngilizce metinlerden tanılar, ilaçlar ve darlık derecesi; token'lar, kelime temsilleri ve önceden eğitilmiş dil modelleri yardımıyla çıkarılmaktadır. Ayrıntılar için [eğitimin planına](../../README.tr.md#on-bir-hafta) bakabilirsiniz.

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
