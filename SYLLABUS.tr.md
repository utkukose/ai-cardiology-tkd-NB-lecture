# İzlence

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](SYLLABUS.md)

## Eğitim bilgileri

| Başlık | Ayrıntı |
|---|---|
| Düzenleyen | Türk Kardiyoloji Derneği |
| Eğitmen | Prof. Dr. Utku Köse, Süleyman Demirel Üniversitesi |
| Katılımcılar | Programlama deneyimi olan ya da olmayan kardiyologlar ve diğer uzman hekimler |
| Biçim | 11 hafta, haftada bir 4 saatlik oturum, toplam 44 saat; sürenin yaklaşık yüzde 80'i uygulamaya ayrılır |
| Malzemelerin dili | İngilizce ve Türkçe |
| Ortam | Katılımcının tercihine göre kurulum gerektirmeyen Google Colab ya da katılımcının kendi bilgisayarında Anaconda içinde çalışan Jupyter |
| Uygulamanın iki yolu | Kodu hazır prompt (istem) metinleriyle bir yapay zekâ (YZ) asistanının yazdığı prompt yolu ve kodu katılımcının yazdığı Python yolu; iki yol da aynı sonuçlara varır |
| Ön koşullar | Programlama deneyimi ve YZ konusunda ön bilgi gerekmez. Colab için bir Google hesabı ya da 1. haftadan önce kurulmuş bir Anaconda yeterlidir ([SETUP.tr.md](SETUP.tr.md)) |
| İletişim | utkukose@sdu.edu.tr, utkukose@gmail.com |

## Tanım

Program, kardiyologlara ve diğer uzman hekimlere kardiyoloji verilerini Python ile analiz etmeyi ve YZ modelleri kurmayı, doğrulamayı ve açıklamayı öğretmektedir. Eğitim, ilk haftalardaki tablolar ve sinyallerden görüntülere, metinlere ve veri füzyonuna doğru ilerler; açıklanabilir modeller, bir klinik karar destek sistemi prototipi ve bir final projesiyle sona erer. Sentetik hastalardan oluşan sanal bir kardiyoloji kliniği bütün haftalar boyunca kullanılır; her konuya açık erişimli gerçek veri setleri de eşlik eder. YZ asistanlarıyla kod yazmak, ilk haftadan başlayarak açık güvenlik kurallarıyla öğretilmektedir. Her alıştırma, asistana bir prompt yazılarak da çözülebilir.

Eğitimin öğrenme çıktıları [eğitimin ana sayfasında](README.tr.md#eğitimin-öğrenme-çıktıları) yer alır; her hafta sayfası da o haftanın çıktılarını listeler.

## Haftalık plan

Her oturum dört saat sürer ve yaklaşık ikişer saatlik iki yarıdan oluşur. Her hafta ayrıca oturum içinde yapılan bir mini proje ve ev çalışması olarak verilen bir haftalık proje içerir. Plan, Türk Kardiyoloji Derneği'nin programını izler ve her hafta yayımlandıkça ayrıntılandırılır.

### Hafta 1: Python ve kardiyoloji verisinin temelleri

Oturumun ilk yarısında Anaconda içinde Jupyter, klinik örneklerle Python, pandas ile hasta tabloları ve Matplotlib ile ilk grafikler tanıtılır. İkinci yarıda elektrokardiyogram (EKG) veri olarak ele alınır; PhysioNet kayıtları, on iki derivasyon, R tepesi tespiti, kalp hızı değişkenliği ve aralıkların otomatik ölçümü işlenir. **Oturumdaki mini proje:** UCI Heart Disease veri setindeki Cleveland verisinin yüklenmesi, özetlenmesi ve görselleştirilmesi. **Haftalık proje:** PR, QRS ve QT aralıklarının otomatik ölçümü, frontal eksen ve iki QT düzeltmesi. **Veriler:** UCI Heart Disease (Cleveland), MIT-BIH Arrhythmia Database, PTB Diagnostic ECG Database. **Sanal kliniğin aşaması:** Hasta kaydı ve EKG laboratuvarı.

Malzemeler: [Hafta sayfası](tr/hafta-01/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/lab.html) · [Jupyter defteri](tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb) · [Prompt kütüphanesi](tr/hafta-01/PROMPTLAR.md) · [PDF ders notu](tr/hafta-01/Hafta01_Ders_Notlari.pdf)

### Hafta 2: Makine öğrenmesi temelleri

Oturumun ilk yarısında scikit-learn ile sınıflandırma ve regresyon modelleri kurulur. Koroner arter hastalığı riski için lojistik regresyon, karar ağaçları ve rastgele ormanlar kullanılır; çapraz doğrulama, alıcı işletim karakteristiği (ROC) eğrisi, duyarlılık ve özgüllük kavramları işlenir. İkinci yarıda k-ortalamalar yöntemiyle hasta alt grupları bulunur ve iki boyutta görselleştirilir; ardından Kaplan-Meier sağkalım analizi tanıtılır ve dengesiz veriler ele alınır. **Oturumdaki mini proje:** Cleveland verisinde koroner arter hastalığını öngören bir model ve bu modelin ROC eğrisi ile eğri altındaki alanı. **Haftalık proje:** Korunmuş ve düşük ejeksiyon fraksiyonlu kalp yetersizliğinin kümelenmesi ve Kaplan-Meier sağkalım analizi. **Veriler:** UCI Heart Disease (Cleveland) ve sanal kliniğin izlem verilerini içeren hasta kaydı. **Sanal kliniğin aşaması:** Risk polikliniği.

Malzemeler: [Hafta sayfası](tr/hafta-02/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/lab.html) · [Jupyter defteri](tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb) · [Prompt kütüphanesi](tr/hafta-02/PROMPTLAR.md) · [PDF ders notu](tr/hafta-02/Hafta02_Ders_Notlari.pdf)

### Hafta 3: Derin öğrenme ve evrişimli sinir ağları

Oturumun ilk yarısında yapay sinir ağları ve evrişimli sinir ağları (CNN) anlatılır: nöronlar, katmanlar, aktivasyon fonksiyonları, evrişim, havuzlama, dropout ve batch normalizasyonu. İkinci yarıda yaygın mimariler karşılaştırılır, kardiyak görüntülerle veri çoğaltma yapılır, karışıklık matrisi ve F1 skoru aşırı öğrenmeye dikkat edilerek yorumlanır. **Oturumdaki mini proje:** EchoNet-Dynamic'te normal ve anormal ekokardiyogramların sınıflandırılması (ejeksiyon fraksiyonu yüzde 50'nin altında olan videolar anormal sayılır). Bu proje, kişisel kaydı olan katılımcılar içindir. **Haftalık proje:** Kardiyak manyetik rezonans görüntülerinde dilate ve hipertrofik kardiyomiyopati sınıflandırması. **Veriler:** ACDC, açık kaynağından indirilen ve kalbi normal olan ya da DCM veya HCM'si bulunan 90 hastanın sine kardiyak manyetik rezonans incelemelerini içerir. EchoNet-Dynamic ise kişisel kayıtla edinilen ekokardiyografi videolarından oluşur. **Sanal kliniğin aşaması:** Görüntüleme laboratuvarı.

Malzemeler: [Hafta sayfası](tr/hafta-03/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/lab.html) · [Jupyter defteri](tr/hafta-03/NB03_derin_ogrenme_ve_evrisimli_aglar.ipynb) · [Prompt kütüphanesi](tr/hafta-03/PROMPTLAR.md) · [PDF ders notu](tr/hafta-03/Hafta03_Ders_Notlari.pdf)

### Hafta 4: Transfer öğrenme

Oturumun ilk yarısında milyonlarca fotoğrafla eğitilmiş ağlar kalp görüntülerine uyarlanır: EfficientNet-B0 ve ACDC'nin sine kardiyak manyetik rezonans incelemeleriyle öznitelik çıkarımı, ince ayar (fine-tuning) ve az sayıda etiketli hastayla öğrenme çalışılır. İkinci yarıda CAMUS ekokardiyogramlarında sol ventrikülün sınırları bir U-Net ile çizilir, hacimler ve ejeksiyon fraksiyonu biplan disk yöntemiyle hesaplanır, ölçümün uzmanla uyumu Bland-Altman analiziyle değerlendirilir ve otomatik bir ölçümün klinik doğrulaması planlanır. **Oturumdaki mini proje:** ImageNet üzerinde önceden eğitilmiş EfficientNet-B0 ile ACDC'nin kardiyomiyopati gruplarının, her gruptan 15 etiketli hastayla, öznitelik çıkarımı ve ince ayar yoluyla sınıflandırılması. **Haftalık proje:** Sol ventrikül segmentasyonu ve otomatik ejeksiyon fraksiyonu. **Veriler:** 3. haftadan tanıdık ACDC kullanılır. CAMUS, 500 hastanın apikal iki boşluk ve dört boşluk ekokardiyogramlarını uzman sınırlarıyla birlikte içerir; eğitim bu hastaların 300'ünü açık kaynağından indirir. EfficientNet-B0'ın ImageNet ağırlıkları da indirilir. **Sanal kliniğin aşaması:** Eko ölçümü: Otomatik ejeksiyon fraksiyonu.

Malzemeler: [Hafta sayfası](tr/hafta-04/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-04/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-04/lab.html) · [Jupyter defteri](tr/hafta-04/NB04_transfer_ogrenme.ipynb) · [Prompt kütüphanesi](tr/hafta-04/PROMPTLAR.md) · [PDF ders notu](tr/hafta-04/Hafta04_Ders_Notlari.pdf)

### Hafta 5: Zaman serisi analizi ve EKG yapay zekâsı

Oturumun ilk yarısında EKG bir zaman serisi olarak modellenir: RR aralıklarına dayanan bir AF kuralı, tek boyutlu evrişimli ağlar, tekrarlayan ağlar ve PTB-XL'de altı ritim etiketinin çok etiketli sınıflandırması çalışılır. İkinci yarıda medyan atımda J noktasındaki ST sapması evrensel tanımın ölçütleriyle ölçülür, QT aralığı ölçülür, sanal kliniğin 24 saatlik bir Holter kaydı okunur ve düzenleyici onay almış EKG algoritmaları gözden geçirilir. **Oturumdaki mini proje:** PTB-XL'de altı ritim etiketi için tek boyutlu bir evrişimli ağ; eşikleri 9. katta seçilir ve ağ 10. katta RR aralıklarına dayanan bir kuralla karşılaştırılır. **Haftalık proje:** Bir STEMI alarmı: 12 derivasyonlu EKG'lerde ST sapmasının otomatik tespiti. **Veriler:** PhysioNet'ten indirilen dört kattaki 8.737 12 derivasyonlu EKG'siyle PTB-XL; sanal kliniğin sentetik 24 saatlik Holter kaydı ve EKG'leri. **Sanal kliniğin aşaması:** Ritim ve STEMI alarmı.

Malzemeler: [Hafta sayfası](tr/hafta-05/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/lab.html) · [Jupyter defteri](tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb) · [Prompt kütüphanesi](tr/hafta-05/PROMPTLAR.md) · [PDF ders notu](tr/hafta-05/Hafta05_Ders_Notlari.pdf)

### Hafta 6: Doğal dil işleme ve klinik metin madenciliği

Oturumun ilk yarısı metni token'lara ayırmayı (tokenization), kelime temsillerini ve Türkçe modeller dâhil Hugging Face Hub'daki önceden eğitilmiş dil modellerini kapsar. İkinci yarıda ilaç, tanı ve işlem gibi adlandırılmış varlıklar metinden çıkarılır, raporlar özetlenir ve büyük dil modellerinin klinik asistan olarak kullanımı tartışılır. **Oturumdaki mini proje:** Sentetik Türkçe epikrizlerden tanıların çıkarılması. **Haftalık proje:** Anjiyografi raporlarından darlık derecesini ve damarı çıkaran bir işlem hattı. **Veriler:** Sanal kliniğin Türkçe ve İngilizce sentetik raporları. **Sanal kliniğin aşaması:** Rapor arşivi: Klinik metin.

Malzemeler: [Hafta sayfası](tr/hafta-06/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-06/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-06/lab.html) · [Jupyter defteri](tr/hafta-06/NB06_klinik_metin_madenciligi.ipynb) · [Prompt kütüphanesi](tr/hafta-06/PROMPTLAR.md) · [PDF ders notu](tr/hafta-06/Hafta06_Ders_Notlari.pdf)

### Hafta 7: Vision Transformer modelleri

Oturumun ilk yarısında dikkat mekanizması, öz dikkat ve görüntüyü yamalara bölen Vision Transformer anlatılır; önceden eğitilmiş bir Vision Transformer ekokardiyografi kareleri için kalite kapısı olarak kullanılır. İkinci yarıda sentetik ve gerçek koroner anjiyogramlarda darlık bulmak için evrişimli bir ağ, bir Vision Transformer ve hibrit bir model karşılaştırılır, dikkat haritaları klinik açıdan yorumlanır ve bir ağ yamalardan bütün anjiyogramlara taşınır. **Oturumdaki mini proje:** ARCADE yamalarında karşılaştırılan üç küçük ağ, iki prevalanstaki eşikleri ve hataları bir kardiyoloğun okuduğu, bütün anjiyogramlar için bir tespit modeli. **Haftalık proje:** Koroner anjiyogramlarda darlık tespiti: Evrişimli ağ, Vision Transformer ve hibrit modelin karşılaştırması. **Veriler:** Sanal kliniğin sentetik anjiyogramları; Zenodo'dan indirilen, darlıklarının sınırları çizilmiş 1.500 X ışınlı koroner anjiyogramıyla ARCADE; CAMUS ekokardiyogramları. **Sanal kliniğin aşaması:** Kateter laboratuvarı.

Malzemeler: [Hafta sayfası](tr/hafta-07/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-07/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-07/lab.html) · [Jupyter defteri](tr/hafta-07/NB07_goru_donusturuculeri.ipynb) · [Prompt kütüphanesi](tr/hafta-07/PROMPTLAR.md) · [PDF ders notu](tr/hafta-07/Hafta07_Ders_Notlari.pdf)

### Hafta 8: Çok modlu yapay zekâ ve veri füzyonu

Oturumun ilk yarısında aynı hastalara ait tabloların, sinyallerin, görüntülerin ve metinlerin erken, geç ve hibrit füzyonu, dikkat tabanlı füzyon ve eksik modalitelerin yönetimi karşılaştırılır. İkinci yarıda bir göğüs ağrısı ünitesi için troponini, klinik değişkenleri, ekokardiyogramı, EKG'yi ve triyaj notunu birleştiren bir risk modeli tasarlanır. Model HEART skoruyla karşılaştırılır; kalibrasyonu, güven aralıkları, ikinci bir hastaneye aktarımı ve taburculuk eşiği değerlendirilir. **Oturumdaki mini proje:** Kalp yetersizliği olayları için EKG, ekokardiyogram ve laboratuvar değerlerini birleştiren bir model ile kalibrasyonu iki hastanede, taburculuk eşiği ise HEART 0-3 ile karşılaştırılarak değerlendirilen bir göğüs ağrısı ünitesi risk modeli. **Haftalık proje:** Simüle edilmiş bir triyajda majör olumsuz kardiyovasküler olayların (MACE) öngörüsü. **Veriler:** Sanal kliniğin izlem verilerini içeren hasta kaydı ve iki hastanedeki göğüs ağrısı ünitesi: Aynı sentetik başvurulara ait klinik tablolar, triyaj notları, 12 derivasyonlu EKG'ler, troponin değerleri ve ekokardiyogramlar. **Sanal kliniğin aşaması:** Kalp ekibi: Veri füzyonu.

Malzemeler: [Hafta sayfası](tr/hafta-08/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-08/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-08/lab.html) · [Jupyter defteri](tr/hafta-08/NB08_cok_modlu_yapay_zeka_ve_veri_fuzyonu.ipynb) · [Prompt kütüphanesi](tr/hafta-08/PROMPTLAR.md) · [PDF ders notu](tr/hafta-08/Hafta08_Ders_Notlari.pdf)

### Hafta 9: Model güvenilirliği ve açıklanabilir yapay zekâ

Oturumun ilk yarısında modellerin kararları, açıklanabilir YZ (XAI) yöntemlerinden SHAP, LIME ve Grad-CAM ile açıklanır. İkinci yarıda veri kayması, kalibrasyon, cinsiyete ve yaşa bağlı yanlılık ve Kişisel Verilerin Korunması Kanunu (KVKK) dâhil klinik yapay zekânın hukuki ve etik çerçevesi incelenir. **Oturumdaki mini proje:** Koroner arter hastalığı modelinde en çok ağırlık taşıyan klinik etkenlerin SHAP ile açıklanması. **Haftalık proje:** Eko modelinin Grad-CAM haritalarının bir uzmanın değerlendirmesiyle karşılaştırılması. **Veriler:** 2. haftanın Cleveland verisi, 4. haftanın 300 CAMUS hastası ve sanal kliniğin iki hastanedeki göğüs ağrısı ünitesi. **Sanal kliniğin aşaması:** Kalite ve güvenlik kurulu: XAI.

Malzemeler: [Hafta sayfası](tr/hafta-09/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-09/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-09/lab.html) · [Jupyter defteri](tr/hafta-09/NB09_guvenilirlik_ve_aciklanabilir_yapay_zeka.ipynb) · [Prompt kütüphanesi](tr/hafta-09/PROMPTLAR.md) · [PDF ders notu](tr/hafta-09/Hafta09_Ders_Notlari.pdf)

### Hafta 10: Klinik karar destek sistemleri

Oturumun ilk yarısında klinik iş akışına uygun bir klinik karar destek sistemi (KKDS) tasarlanır, web arayüzü Streamlit ile kurulur ve HL7 FHIR ile tahmin servisleri tanıtılır. İkinci yarı sürüm yönetimini, insan gözetimini, tıbbi cihaz yazılımlarının düzenleyici süreçlerini ve hasta onamını kapsar. **Oturumdaki mini proje:** Atriyal fibrilasyon için bir karar destek prototipi: EKG yükleme, tahmin, açıklama ve rapor. **Haftalık proje:** Karar destek prototipinin kullanıcı testi ve iyileştirilmesi. **Veriler:** Sanal kliniğin EKG'leri ve MIT-BIH Atriyal Fibrilasyon Veri Tabanı. **Sanal kliniğin aşaması:** Yatak başında karar desteği.

Malzemeler: [Hafta sayfası](tr/hafta-10/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-10/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-10/lab.html) · [Jupyter defteri](tr/hafta-10/NB10_klinik_karar_destegi.ipynb) · [Prompt kütüphanesi](tr/hafta-10/PROMPTLAR.md) · [PDF ders notu](tr/hafta-10/Hafta10_Ders_Notlari.pdf)

### Hafta 11: Final projesi ve sertifika

Oturumun ilk yarısı final projeleri üzerine bir atölyedir; bu atölyede sorunun, verinin, modelin, modelin açıklamasının ve klinik değerlendirmenin tasarımı üzerinde çalışılır. İkinci yarıda final projeleri sunulur ve değerlendirilir; program sertifikalarla kapanır. **Oturumdaki mini proje:** Final projesi üzerinde çalışma. **Haftalık proje:** Final projesi: Katılımcının kendi kliniğinden bir soru için uçtan uca bir YZ işlem hattı ve kişisel eylem planı. **Veriler:** Her katılımcı kendi verilerini seçer (final projesi sayfasına bakın). **Sanal kliniğin aşaması:** Katılımcıların birimleri: Final projeleri.

Malzemeler: [Hafta sayfası](tr/hafta-11/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/lab.html) · [Jupyter defteri](tr/hafta-11/NB11_final_projesi_atolyesi.ipynb) · [Prompt kütüphanesi](tr/hafta-11/PROMPTLAR.md) · [PDF ders notu](tr/hafta-11/Hafta11_Ders_Notlari.pdf)

## Değerlendirme ve sertifika

| Bileşen | Ağırlık | Sertifika koşulu |
|---|---|---|
| Haftalık projeler (1-10. haftalar) | Yüzde 40 | Her projeden en az yüzde 70 |
| Final projesi (sunum ve kod) | Yüzde 40 | Jüri ve katılımcı değerlendirmesi |
| Katılım ve etkin öğrenme | Yüzde 20 | En az yüzde 80 devam |

Her haftalık proje 100 puan üzerinden değerlendirilir. Sanal kliniğin gerçek değerleriyle ya da bir referansla karşılaştırılarak doğrulanmış doğru sonuçlar 40 puandır. Öğretildiği biçimde uygulanmış ve açıklanmış yöntemler 20 puandır. Klinik anlamın ve sınırlılıkların tartışılması 20 puandır. YZ kullanım günlüğü, kod güvenlik kontrol listesinin kullanımı ve her sonucu yeniden üreten bir defter son 20 puanı oluşturur. Final projesinin değerlendirme ölçütleri [final projesi sayfasında](tr/final-projesi/README.md) yer almaktadır.

## Haftalık projelerin teslimi

Haftalık projeler, bir sonraki haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. Konu satırı haftayı ve katılımcıyı belirtir, örneğin "TKD YZ, Hafta 1, Ad Soyad". E-posta, YZ kullanım günlüğünü içeren ve [rapor şablonuyla](tr/sablonlar/Rapor_Sablonu.docx) yazılmış raporu, tamamlanmış Jupyter defterini ve etkileşimli labdan dışa aktarılan öğrenme günlüğünü içerir.

## Üretken yapay zekâ kullanım kuralları

Üretken YZ araçlarının kullanımına bu eğitimde izin verilir ve bu araçlar öğretimin bir parçasıdır. Dört kural geçerlidir. Birincisi, hiçbir prompta hasta verisi girmez: Gerçek hastaların adları, doğum tarihleri, protokol numaraları ya da kayıtları kullanılmaz. İkincisi, haftalık ya da final projesi için bir YZ aracının her kullanımı, araç, prompt, neyin kontrol edildiği ve neyin değiştirildiği bilgileriyle YZ kullanım günlüğüne kaydedilir. Üçüncüsü, katılımcı teslim ettiği kodun her satırından sorumludur ve onu açıklayabilmelidir. Bir asistanla yazılan kod, sonuçları kullanılmadan önce kod güvenlik kontrol listesiyle denetlenir. Dördüncüsü, raporlardaki yorum ve tartışma katılımcının kendisine aittir. Bir asistan dil konusunda yardımcı olabilir ve bu yardım da günlüğe kaydedilir. [Prompt yolu](PROMPT_PATH.tr.md) aynı kuralları her alıştırmaya uygular; bu yoldan gelen kod da elle yazılmış kod gibi değerlendirilir.

## Veri koruma ve etik

Eğitimde yalnızca sentetik veriler ve açık araştırma verileri kullanılır. Katılımcının kurumuna ait gerçek hasta verileri, final projesinde yalnızca kurumun izniyle ve gerektiğinde etik kurul onayıyla kullanılabilir. Bu veriler KVKK'ya uygun olarak katılımcının kendi bilgisayarında işlenir [1]. Hiçbir zaman bir bulut hizmetine ya da bir YZ sohbetine aktarılmaz. Sanal kliniğin sentetik hastaları öğretim malzemesidir ve klinik kullanım için değildir.

## Devam

Sertifika için oturumların en az yüzde 80'ine, yani 11 oturumun en az 9'una katılım gerekir. Bir oturumu kaçıran katılımcı, haftayı hafta sayfasındaki çalışma yolunu izleyerek tamamlar; bu yol her adım için bireysel çalışma süresini verir.

## Malzemeler ve ortam

Her hafta için ders sayfasına, etkileşimli laba, Jupyter defterine, prompt kütüphanesine ve PDF ders notuna bağlantı veren bir hafta sayfası vardır. [SETUP.tr.md](SETUP.tr.md) defterlerin çalıştığı iki ortamı, yani Google Colab'ı ve kişinin kendi bilgisayarındaki Jupyter'i anlatır; [başlangıç defteri](tr/baslangic/NB00_baslangic.ipynb) 1. haftadan önce iki yolun ilk adımlarını hazırlar. [DATASETS.tr.md](DATASETS.tr.md) veri setlerini lisanslarıyla, [PYTHON_PATH.tr.md](PYTHON_PATH.tr.md) ise haftaların Python adımlarını listeler. [PROMPT_PATH.tr.md](PROMPT_PATH.tr.md) prompt yolunu ve bu yolda kullanılabilecek YZ asistanlarını, [OWN_DATA.tr.md](OWN_DATA.tr.md) ise eğitimin yöntemlerinin kişinin kendi kliniğinin verilerine nasıl uygulanacağını anlatmaktadır.

## İletişim

İçerikle ilgili sorular oturumlarda ya da utkukose@sdu.edu.tr veya utkukose@gmail.com adresine e-postayla sorulabilir. Malzemelerdeki hatalar deponun [issues](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/issues) bölümünden bildirilebilir.

## Kaynaklar

1. Kişisel Verilerin Korunması Kanunu, Kanun No. 6698. (2016). *Resmî Gazete, 29677 (7 Nisan 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5
---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
