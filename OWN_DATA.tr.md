# Kendi verilerinizle çalışmak

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](OWN_DATA.md)

Eğitimde sentetik hastalar ve açık araştırma verileri kullanılır; böylece her Jupyter Notebook herkes için çalışır ve gerçek cevaplar bilinir. Eğitimin asıl hedefi ise katılımcının kendi kliniğinin verileridir. Bu rehber, ders sayfalarındaki "Kendi verinizle" bölümlerinin hafta hafta anlattıklarını bir araya getirmektedir. Rehberde hangi sorunun hangi yönteme uyduğu, verilerin hastane sistemlerinden nasıl alındığı, yasanın ve etik kurulun neyi gerektirdiği ve analizin nerede yapılacağı anlatılır.

Rehber yol gösterir; hukuki görüş değildir. Her çalışmada son söz kurumun etik kuruluna, veri koruma sorumlusuna ve hukuk birimine aittir.

## 1. Veriden önce: Soru ve izinler

| Adım | Anlamı |
|---|---|
| Açık bir soru | Tek bir sonuç, tek bir hasta grubu ve tek bir karar anı belirlenir. Örneğin "Verilerimizde yapay zekâ ne bulur?" yerine "Düşük ejeksiyon fraksiyonlu kalp yetersizliği (HFrEF) olan hastalardan hangileri 12 ay içinde hastaneye yatar?" diye sorulur. |
| Yazılı bir plan | Soru, hastalar, değişkenler, planlanan analiz ve örneklem büyüklüğü, veriler görülmeden önce yazılır. Bir öngörü modelinin örneklem büyüklüğü olay sayısına bağlıdır [1]. |
| Etik kurul | Geriye dönük dosya taramaları dâhil, hasta verisiyle yapılan araştırmalar etik kurul onayı gerektirir. |
| Veri koruma | Sağlık verileri, Kişisel Verilerin Korunması Kanunu'na (KVKK) göre özel nitelikli kişisel verilerdir [2]. Bu verilerin nasıl işlenebileceğine kurum karar verir; başvurulacak yerler kurumun veri koruma sorumlusu ve hukuk birimidir. |
| Kurum | Hastane yönetiminin izni alınır; verilerin dışa aktarımı için bilgi işlem ya da klinik mühendislik biriminden destek istenir. |

## 2. Verileri hastane sistemlerinden dışa aktarmak

| Veri | Nerede bulunur? | Ne istenmeli? | Neler çıkarılmalı? |
|---|---|---|---|
| Hasta tabloları | Hastane bilgi yönetim sistemi (HBYS), bir çalışmanın kaydı | Her hasta için bir satır içeren bir Excel ya da CSV dosyası ve her sütunun birimini ve kodlamasını veren bir veri sözlüğü | Adlar, T.C. kimlik numaraları, dosya ve protokol numaraları, adresler ve telefon numaraları; tarihlerin yerini yaşlar ve süreler alır |
| EKG'ler | Elektrokardiyograf, EKG yönetim sistemi | PDF çıktıları yerine dijital biçimde ham sinyaller: XML (örneğin HL7 aECG), DICOM dalga biçimi, SCP-ECG ya da EDF | Her dosyanın başlığındaki ad ve kimlik numarası |
| Ekokardiyografi, kardiyak manyetik rezonans, koroner anjiyografi | Görüntü arşivleme ve iletişim sistemi (PACS) ya da cihaz | Ekran kayıtları yerine DICOM dosyaları; yöntem hareketi gerektiriyorsa sine kayıtları da istenir | DICOM başlığındaki kimlik bilgileri ve görüntünün üzerine işlenmiş yazılar, örneğin bir eko karesinin kenarındaki ad ve tarih |
| Yazılı raporlar | HBYS | Eko, kateterizasyon ya da epikriz raporlarının düz metni | Metnin içindeki adlar, tarihler, telefon numaraları ve yerler; otomatik anonimleştirme okunarak denetlenmelidir |
| Laboratuvar değerleri | Laboratuvar bilgi sistemi | Değerleri, birimleri ve referans aralıklarını içeren bir tablo | Tablolardaki gibi kimlik bilgileri; birimler laboratuvardan laboratuvara ve yıllar içinde değişebilir |

Çalışma numaralarını hastalara bağlayan bir anahtar gerekiyorsa bu anahtar, verilerden ayrı olarak hastanede saklanır. Böyle bir anahtarı olan veriler anonim değil, takma adlandırılmış (pseudonymised) verilerdir ve kişisel veri olmayı sürdürür.

## 3. Hangi soruya hangi yöntem?

| Veri | Soru | Eğitimin yöntemleri | Hafta |
|---|---|---|---|
| Tablo | Hastada bir durum var mı ya da bir olay gelişecek mi? | Lojistik regresyon, karar ağaçları ve rastgele ormanlar, çapraz doğrulama | 2 |
| Tablo | Olaya kadar ne kadar zaman geçer? | Kaplan-Meier eğrileri, log-rank testi ve Cox regresyonu | 2 |
| Tablo | Hastalar arasında alt gruplar var mı? | Standartlaştırılmış değişkenlerle k-ortalamalar | 2 |
| EKG sinyali | Aralıklar, kalp hızı ve değişkenliği | Sinyal işleme, R tepesi tespiti | 1 |
| EKG sinyali | Ritim ve tanı, ST sapması | Tek boyutlu evrişimli ağlar ve tekrarlayan ağlar, aynı anda birden çok sınıf taşıyan etiketler | 5 |
| Ekokardiyografi, kardiyak manyetik rezonans | Görüntülerin sınıflandırılması | Evrişimli ağlar, önceden eğitilmiş ağlardan transfer öğrenme | 3, 4 |
| Ekokardiyografi, kardiyak manyetik rezonans | Hacimler ve ejeksiyon fraksiyonu gibi ölçümler | U-Net ile segmentasyon ve disk yöntemi | 4 |
| Koroner anjiyografi | Darlıkların saptanması | Evrişimli ağlar ve Vision Transformer modelleri | 7 |
| Yazılı raporlar | Bulguların çıkarılması | Doğal dil işleme | 6 |
| Birkaç veri türü birlikte | Birleşik bir risk | Veri füzyonu, eksik veri ve kalibrasyon | 8 |
| Her model | Model güvenilir ve açıklanabilir mi? | Açıklanabilir yapay zekâ (YZ), dağılım kayması ve yanlılık | 9 |
| Her model | Model hasta başında nasıl kullanılır? | Klinik karar destek sistemleri (CDSS) | 10 |

## 4. Ne kadar veri?

Tablolardan kurulan öngörü modellerinde olay sayısı hasta sayısından daha önemlidir; yayımlanmış yöntemler en küçük örneklem büyüklüğünü beklenen olay sayısından ve değişken sayısından hesaplar [1]. Görüntüler için sabit bir sayı yoktur. Bir ağı sıfırdan eğitmek çok sayıda etiketli görüntü gerektirir; önceden eğitilmiş ağlar ve 4. haftanın konusu olan transfer öğrenme bu ihtiyacı azaltır. Bir ön çalışmada başarımın eğitim görüntüsü sayısına karşı çizildiği öğrenme eğrisi, daha fazla verinin işe yarayıp yaramayacağını gösterir.

Her durumda verilerin bir bölümü ilk modelden önce test kümesi olarak ayrılır ve en sonda yalnızca bir kez kullanılır. Hasta bakımında kullanılması düşünülen bir model, başka bir hastanenin ya da başka bir cihazın verileriyle yeniden sınanır; buna dış doğrulama denir.

## 5. Hesap nerede yapılır ve YZ asistanları nasıl kullanılır?

Gerçek hastaların verileri kurumun bir bilgisayarında, Jupyter'de (Anaconda) analiz edilir; Google Colab gibi bulut tabanlı bir Jupyter Notebook'a ya da bir YZ sohbetine asla aktarılmaz. Böyle verileri taşıyan bir dizüstü bilgisayarın diski şifrelenmelidir.

Kodu hazır bir prompt (istem) ile bir YZ asistanına yazdırmak kişinin kendi verileriyle de işe yarar. Bunun tek bir kuralı vardır: Prompt verinin yapısını, yani sütunların adlarını, birimlerini, kodlarını ve örnekleme frekansını tarif eder; hiçbir zaman bir hastanın satırını içermez. Kodu önce aynı sütunlara sahip sentetik bir tabloda denemek, gerçek veride ise ancak bu denemeden geçtikten sonra çalıştırmak iyi bir alışkanlıktır; `vclinic` ders paketi böyle tablolar üretebilir. 6. haftada kullanılan ve kişinin kendi bilgisayarında çalışan önceden eğitilmiş dil modelleri, raporların metnini o bilgisayarın içinde tutar.

## 6. Raporlama ve klinik kullanıma geçiş

Bir öngörü modeli geliştiren ya da sınayan çalışma, modeli TRIPOD+AI kontrol listesiyle raporlar [3]. Hasta bakımında kullanılacak bir model ise bir çalışmadan farklı bir konudur. Hastaların tanısı ya da tedavisi için tasarlanan bir yazılım, Avrupa Birliği mevzuatıyla uyumlu Tıbbi Cihaz Yönetmeliği kapsamında bir tıbbi cihaz olabilir [4]. Böyle bir yazılım, kullanıma sunulmadan önce yönetmeliğin öngördüğü uygunluk değerlendirmesinden geçmelidir. Bu yüzden eğitimin ya da bir çalışmanın modeli, bu süreçten geçmeden hastalara ilişkin kararlarda asla kullanılmaz.

## 7. Kimden yardım alınır?

| Soru | Başvurulacak yer |
|---|---|
| Örneklem büyüklüğü, çalışma tasarımı, istatistik | Kurumun bir biyoistatistikçisi |
| Etik kurul onayı | Kurumun etik kurulu |
| KVKK ve veri güvenliği | Kurumun veri koruma sorumlusu ve hukuk birimi |
| Hastane sistemlerinden ve cihazlardan dışa aktarım | Bilgi işlem ya da klinik mühendislik birimi |
| Eğitimin final projesi | Eğitimin eğitmeni |

## Kısa bir kontrol listesi

1. Tek ve açık bir soru ile örneklem büyüklüğünü içeren yazılı bir plan.
2. Etik kurul onayı ve kurumun izni.
3. Bir veri sözlüğüyle birlikte kimlik bilgilerinden arındırılmış bir dışa aktarım.
4. Kurumun bir bilgisayarında bir hesap ortamı.
5. Kalite denetimi: Birimler, değer aralıkları, kodlar, tekrarlanan kayıtlar ve eksik değerler.
6. İlk modelden önce ayrılmış bir test kümesi.
7. Sınırlılıklarıyla birlikte TRIPOD+AI'ye uyan bir rapor.

## Kaynaklar

1. Riley, R. D., Ensor, J., Snell, K. I. E., Harrell, F. E., Jr., Martin, G. P., Reitsma, J. B., Moons, K. G. M., Collins, G., & van Smeden, M. (2020). Calculating the sample size required for developing a clinical prediction model. *BMJ, 368*, m441. https://doi.org/10.1136/bmj.m441
2. Kişisel Verilerin Korunması Kanunu, Kanun No. 6698. (2016). *Resmî Gazete, 29677 (7 Nisan 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5
3. Collins, G. S., Moons, K. G. M., Dhiman, P., Riley, R. D., Beam, A. L., Van Calster, B., Ghassemi, M., Liu, X., Reitsma, J. B., van Smeden, M., Boulesteix, A.-L., Camaradou, J. C., Celi, L. A., Denaxas, S., Denniston, A. K., Glocker, B., Golub, R. M., Harvey, H., Heinze, G., Hoffman, M. M., Kengne, A. P., Lam, E., Lee, N., Loder, E. W., Maier-Hein, L., Mateen, B. A., McCradden, M. D., Oakden-Rayner, L., Ordish, J., Parnell, R., Rose, S., Singh, K., Wynants, L., & Logullo, P. (2024). TRIPOD+AI statement: Updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ, 385*, e078378. https://doi.org/10.1136/bmj-2023-078378
4. Tıbbi Cihaz Yönetmeliği, Türkiye İlaç ve Tıbbi Cihaz Kurumu. (2021). *Resmî Gazete, 31499 (Mükerrer) (2 Haziran 2021)*. https://titck.gov.tr/storage/Archive/2021/contentFile/T%C4%B1bbi%20Cihaz%20Y%C3%B6netmeli%C4%9Fi_91969c4b-58b3-48cb-adfb-03c2cacd5632.pdf

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
