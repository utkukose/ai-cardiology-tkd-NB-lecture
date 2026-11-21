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

### Hafta 1: Python ve kardiyoloji veri temelleri

Oturumun Python'a giriş ve Jupyter Notebook ortamına ayrılan ilk 2 saati, Anaconda ve Jupyter Notebook ortamının tanıtımını ve ilk kullanımını, tıbbi örneklerle değişkenleri, listeleri ve döngüleri, pandas ile hasta tablosu okuma ve işlemeyi ve Matplotlib ile ilk kardiyolojik grafiği kapsar. Son 2 saatte elektrokardiyogram (EKG) verisiyle çalışılır. Bu kısım PhysioNet ve MIT-BIH veri setlerine erişimi, wfdb kütüphanesi ile EKG okuma ve işlemeyi, NeuroKit2 ile R-peak tespitini, HRV (kalp hızı değişkenliği) hesaplamayı ve 12 derivasyon görselleştirmeyi kapsamaktadır. Aynı kısımda EKG bir veri olarak ele alınır ve aralıkları otomatik olarak ölçülür. **Oturumdaki mini proje:** UCI Heart Disease koleksiyonunun Cleveland verisinden alınan Kaggle Heart Disease veri setini yükleme, istatistiksel özet ve görselleştirme. **Haftalık proje:** EKG görselleştirme ve temel ölçümleri (PR, QRS, QT) otomatik hesaplayan script. **Veriler:** UCI Heart Disease (Cleveland), MIT-BIH Arrhythmia Database, PTB Diagnostic ECG Database. **Sanal kliniğin aşaması:** Hasta kaydı ve EKG laboratuvarı.

Malzemeler: [Hafta sayfası](tr/hafta-01/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/lab.html) · [Jupyter Notebook](tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb) · [Prompt kütüphanesi](tr/hafta-01/PROMPTLAR.md) · [PDF ders notu](tr/hafta-01/Hafta01_Ders_Notlari.pdf)

### Hafta 2: Makine öğrenmesi temelleri

Oturumun sınıflandırma ve regresyona ayrılan ilk 2 saati, scikit-learn ile modelleme pipeline'ını, lojistik regresyonla koroner arter hastalığı (KAH) riski tahminini, karar ağacı ve Random Forest karşılaştırmasını, çapraz doğrulamayı (cross-validation), alıcı işletim karakteristiği eğrisinin altındaki alanı (ROC-AUC) ve duyarlılık/özgüllük yorumunu kapsar. Kümeleme ve hasta segmentasyonuna ayrılan son 2 saat ise K-Means ile hasta alt gruplarını bulmayı, UMAP (Uniform Manifold Approximation and Projection) ve t-SNE (t-distributed Stochastic Neighbor Embedding) görselleştirmesini, Kaplan-Meier eğrisiyle sağkalım analizini (survival analysis) ve SMOTE (Synthetic Minority Over-sampling Technique) ile dengesiz veriyle başa çıkmayı kapsamaktadır. **Oturumdaki mini proje:** Cleveland Heart Disease veri seti ile KAH tahmin modeli, ROC eğrisi ve AUC analizi. **Haftalık proje:** HFpEF vs HFrEF hasta kümeleme + Kaplan-Meier sağkalım analizi. **Veriler:** UCI Heart Disease (Cleveland) ve sanal kliniğin izlem verilerini içeren hasta kaydı. **Sanal kliniğin aşaması:** Risk polikliniği.

Malzemeler: [Hafta sayfası](tr/hafta-02/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/lab.html) · [Jupyter Notebook](tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb) · [Prompt kütüphanesi](tr/hafta-02/PROMPTLAR.md) · [PDF ders notu](tr/hafta-02/Hafta02_Ders_Notlari.pdf)

### Hafta 3: Derin öğrenme ve CNN temelleri

Oturumun yapay sinir ağları ve CNN'ye ayrılan ilk 2 saati, nöron, katman ve aktivasyon fonksiyonunu tıbbi bir analojiyle, Keras Sequential API ile ilk modeli, görüntüde kenar ve desen bulan konvolüsyon (evrişim) işlemini ve pooling, dropout ve batch normalizasyonunu kapsar. Gelişmiş evrişimli sinir ağlarına (CNN) ve model değerlendirmeye ayrılan son 2 saat ise VGG16 ve ResNet50 mimarilerini kavramsal düzeyde, kardiyak görüntüler için görüntü augmentation'ını (veri çoğaltma), confusion matrix (karışıklık matrisi) ve F1-score yorumlamayı ve overfitting (aşırı öğrenme) tespitini ve önlenmesini kapsamaktadır. **Oturumdaki mini proje:** EchoNet-Dynamic veri setinden normal/anormal ekokardiyografi sınıflandırması (ejeksiyon fraksiyonu yüzde 50'nin altında olan videolar anormal sayılır); kişisel kaydı olan katılımcılar için. **Haftalık proje:** Kardiyak MRI ACDC veri seti: Dilate/hipertrofik KMP otomatik sınıflandırma. **Veriler:** ACDC, açık kaynağından indirilen ve kalbi normal olan ya da DCM veya HCM'si bulunan 90 hastanın sine kardiyak manyetik rezonans incelemelerini içerir. EchoNet-Dynamic ise kişisel kayıtla edinilen ekokardiyografi videolarından oluşur. **Sanal kliniğin aşaması:** Görüntüleme laboratuvarı.

Malzemeler: [Hafta sayfası](tr/hafta-03/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-03/lab.html) · [Jupyter Notebook](tr/hafta-03/NB03_derin_ogrenme_ve_evrisimli_aglar.ipynb) · [Prompt kütüphanesi](tr/hafta-03/PROMPTLAR.md) · [PDF ders notu](tr/hafta-03/Hafta03_Ders_Notlari.pdf)

### Hafta 4: Transfer learning: Hazır gücü kardiyolojiye uyarla

Oturumun transfer learning prensiplerine ayrılan ilk 2 saati, ImageNet ön eğitimli modelleri (EfficientNet, DenseNet), feature extraction (öznitelik çıkarımı) ile fine-tuning (ince ayar) arasındaki seçimi, son katmanların kardiyak hedefler için değiştirilmesini ve az veriyle yüksek başarıya ulaşmanın yollarını kapsar. Segmentasyon ve ölçüm otomasyonuna ayrılan son 2 saat ise kardiyak segmentasyon için U-Net mimarisini, sol ventrikül ejeksiyon fraksiyonunun (EF) Simpson yöntemiyle otomatik ölçümünü, pixel-wise (piksel düzeyinde) segmentasyon eğitimini ve klinik validasyon metodolojisini kapsamaktadır. **Oturumdaki mini proje:** EfficientNet-B0 ile az sayıda etiketli görüntüden KMP sınıflandırma: ACDC'nin sine kardiyak manyetik rezonans görüntülerinde gruplar, kardiyomiyopati etiketi taşımayan CAMUS ekokardiyogramlarında ise düşük ve normal EF. **Haftalık proje:** CAMUS veri seti ile sol ventrikül segmentasyonu + EF otomatik hesaplama. **Veriler:** 3. haftadan tanıdık ACDC kullanılır. CAMUS, 500 hastanın apikal iki boşluk ve dört boşluk ekokardiyogramlarını uzman sınırlarıyla birlikte içerir; eğitim bu hastaların 300'ünü açık kaynağından indirir. EfficientNet-B0'ın ImageNet ağırlıkları da indirilir. **Sanal kliniğin aşaması:** Eko ölçümü: Otomatik ejeksiyon fraksiyonu.

Malzemeler: [Hafta sayfası](tr/hafta-04/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-04/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-04/lab.html) · [Jupyter Notebook](tr/hafta-04/NB04_transfer_ogrenme.ipynb) · [Prompt kütüphanesi](tr/hafta-04/PROMPTLAR.md) · [PDF ders notu](tr/hafta-04/Hafta04_Ders_Notlari.pdf)

### Hafta 5: Zaman serisi analizi ve EKG yapay zekâsı

Oturumun 1D CNN ve LSTM ile EKG analizine ayrılan ilk 2 saati, EKG'nin zaman serisi olarak modellenmesini, AF, VT ve SVT gibi aritmilerin tespiti için tek boyutlu evrişimli ağları (1D CNN), temporal bağımlılıklar için LSTM'i ve çok etiketli (multi-label) sınıflandırmayı kapsar. Gelişmiş EKG modelleri ve klinik entegrasyona ayrılan son 2 saat ise akut miyokard enfarktüsünde (AMI) ST yükselmesi ve çökmesinin otomatik tespitini, bir QTc uzaması risk algoritmasını, yapay zekâyla uzun dönem izlem olarak Holter analizini ve FDA/CE onaylı yapay zekâ tabanlı EKG ürünlerine genel bir bakışı kapsamaktadır. **Oturumdaki mini proje:** PhysioNet 2020 Challenge: 12 derivasyon EKG'den 9 ritim bozukluğu tespiti. CPSC 2018'in dokuz sınıfı, Challenge'ın PTB-XL kısmında tek boyutlu bir evrişimli ağla öğrenilir ve her sınıfın 10. kattaki AUC değeri bildirilir. **Haftalık proje:** STEMI alarm sistemi: AMI EKG'lerinden ST deviasyonu otomatik tespiti (PTB-XL). **Veriler:** PhysioNet'ten indirilen dört kattaki 8.737 12 derivasyonlu EKG'siyle PTB-XL; sanal kliniğin sentetik 24 saatlik Holter kaydı ve EKG'leri. **Sanal kliniğin aşaması:** Ritim ve STEMI alarmı.

Malzemeler: [Hafta sayfası](tr/hafta-05/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-05/lab.html) · [Jupyter Notebook](tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb) · [Prompt kütüphanesi](tr/hafta-05/PROMPTLAR.md) · [PDF ders notu](tr/hafta-05/Hafta05_Ders_Notlari.pdf)

### Hafta 6: NLP ve klinik metin madenciliği

Oturumun NLP temelleri ve klinik metin işlemeye ayrılan ilk 2 saati, tokenizasyon ve lemmatizasyonu, TF-IDF ve word embedding kavramlarını, Hugging Face Hub üzerinden yüklenen BERT ve BioBERT modellerini ve BERTurk gibi Türkçe tıbbi dil modellerini kapsar. Gelişmiş klinik NLP uygulamalarına ayrılan son 2 saat ise ilaç, tanı ve prosedür için adlandırılmış varlık tanımayı (Named Entity Recognition, NER), radyoloji raporlarının otomatik özetlenmesini, klinik çalışmalara (trial) uygunluğun tespitini ve kavramsal olarak büyük dil modelleri (LLM) ile klinik asistanı kapsamaktadır. **Oturumdaki mini proje:** Sentetik Türkçe epikrizlerden tanı (STEMI, AF, KY) otomatik çıkarımı: NER pipeline. **Haftalık proje:** Kardiyak anjiyo raporu NLP pipeline: Stenoz derecesi + etkilenen damar otomatik çıkarımı. **Veriler:** Sanal kliniğin Türkçe ve İngilizce sentetik raporları. **Sanal kliniğin aşaması:** Rapor arşivi: Klinik metin.

Malzemeler: [Hafta sayfası](tr/hafta-06/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-06/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-06/lab.html) · [Jupyter Notebook](tr/hafta-06/NB06_klinik_metin_madenciligi.ipynb) · [Prompt kütüphanesi](tr/hafta-06/PROMPTLAR.md) · [PDF ders notu](tr/hafta-06/Hafta06_Ders_Notlari.pdf)

### Hafta 7: Vision Transformer (ViT): Görüntü işlemede yeni nesil

Oturumun attention mekanizması ve ViT mimarisine ayrılan ilk 2 saati, CNN'in sınırlarını ve global bağlam eksikliğini, görüntünün farklı bölgeleri arasındaki ilişki olarak self-attention'ı, görüntüyü 16 × 16 piksellik parçalara ayıran patch embedding'i ve PyTorch ile inşa edilen bir Vision Transformer'ın yanında Hugging Face üzerinden yüklenen hazır bir ViT modelini kapsar. Hibrit CNN-ViT ve medikal görüntülemeye ayrılan son 2 saat ise Swin Transformer'ın shifted window attention mekanizmasını, CNN backbone ve Transformer head'den oluşan hibrit mimariyi, stenoz tespiti için koroner anjiyografi analizini ve attention haritalarının klinik yorumuyla birlikte görselleştirilmesini kapsamaktadır. **Oturumdaki mini proje:** CIFAR-10 üzerinde mini ViT eğitimi; ardından EchoNet'e transfer uygulaması. EchoNet-Dynamic için kişisel kaydı olmayan katılımcılar CAMUS ekokardiyogramlarını kullanır. **Haftalık proje:** Koroner anjiyografi: Stenoz tespiti CNN vs ViT vs Hibrit karşılaştırması + attention haritaları. **Veriler:** Sanal kliniğin sentetik anjiyogramları; Zenodo'dan indirilen, darlıklarının sınırları çizilmiş 1.500 X ışınlı koroner anjiyogramıyla ARCADE; CAMUS ekokardiyogramları; Toronto Üniversitesinden on sınıflı 60.000 renkli fotoğrafla CIFAR-10; kişisel kayıtla EchoNet-Dynamic. **Sanal kliniğin aşaması:** Kateter laboratuvarı.

Malzemeler: [Hafta sayfası](tr/hafta-07/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-07/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-07/lab.html) · [Jupyter Notebook](tr/hafta-07/NB07_vision_transformer.ipynb) · [Prompt kütüphanesi](tr/hafta-07/PROMPTLAR.md) · [PDF ders notu](tr/hafta-07/Hafta07_Ders_Notlari.pdf)

### Hafta 8: Çok modlu yapay zekâ ve veri füzyonu

Oturumun multimodal AI prensiplerine ayrılan ilk 2 saati, erken füzyon, geç füzyon ve hibrit füzyon karşılaştırmasını, farklı veri tiplerinin tek modelde birleştirilmesini, attention tabanlı füzyon mekanizmalarını ve klinik gerçeklik olarak eksik veri yönetimini kapsar. Kardiyovasküler risk skorlama sistemine ayrılan son 2 saat ise SCORE2 ve Framingham'a alternatif bir yapay zekâ modelinin tasarımını, şüpheli AKS erken uyarı modelini, biyobelirteçlerin, klinik değişkenlerin ve görüntülemenin füzyonunu ve kalibrasyon ile güven aralıklarının önemini kapsamaktadır. **Oturumdaki mini proje:** EKG sinyali + ekokardiyografi + lab değerleri füzyon modeli ile KY risk sınıflandırması. **Haftalık proje:** Gerçek zamanlı MACE tahmin modeli: Triyaj senaryosu simülasyonu (MIMIC-IV sentetik). **Veriler:** Sanal kliniğin izlem verilerini içeren hasta kaydı ve iki hastanedeki göğüs ağrısı ünitesi: Aynı sentetik başvurulara ait klinik tablolar, triyaj notları, 12 derivasyonlu EKG'ler, troponin değerleri ve ekokardiyogramlar. **Sanal kliniğin aşaması:** Kalp ekibi: Veri füzyonu.

Malzemeler: [Hafta sayfası](tr/hafta-08/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-08/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-08/lab.html) · [Jupyter Notebook](tr/hafta-08/NB08_cok_modlu_yapay_zeka_ve_veri_fuzyonu.ipynb) · [Prompt kütüphanesi](tr/hafta-08/PROMPTLAR.md) · [PDF ders notu](tr/hafta-08/Hafta08_Ders_Notlari.pdf)

### Hafta 9: Model güvenilirliği ve açıklanabilir yapay zekâ (XAI)

Oturumun açıklanabilir AI yöntemlerine ayrılan ilk 2 saati, kara kutu problemini ve klinisyenin neden güvenmediğini, hangi özelliğin ne kadar katkı yaptığını gösteren SHAP değerlerini, yerel açıklamalarıyla LIME'ı ve CNN'in nereye baktığını gösteren Grad-CAM'i kapsar. AI güvenilirliği ve klinik validasyona ayrılan son 2 saat ise distribüsyon kaymasının (data drift) tuzaklarını, model kalibrasyonunu ve güven skorunu, cinsiyet, yaş ve etnik kökene göre önyargı (bias) tespitini ve GDPR ile Kişisel Verilerin Korunması Kanunu'nun (KVKK) çizdiği hukuki ve etik çerçeveyi kapsamaktadır. **Oturumdaki mini proje:** KAH tahmin modelinde SHAP: Hangi klinik faktör (LDL, yaş, EF?) modeli en çok etkiliyor? **Haftalık proje:** Grad-CAM ile ekokardiyografi modelinin 'nereye baktığını' görselleştirme ve uzman yorumuyla karşılaştırma. **Veriler:** 2. haftanın Cleveland verisi, LDL, yaş ve ejeksiyon fraksiyonunu içeren sanal klinik kayıt sistemi, 4. haftanın 300 CAMUS hastası ve sanal kliniğin iki hastanedeki göğüs ağrısı ünitesi. **Sanal kliniğin aşaması:** Kalite ve güvenlik kurulu: XAI.

Malzemeler: [Hafta sayfası](tr/hafta-09/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-09/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-09/lab.html) · [Jupyter Notebook](tr/hafta-09/NB09_guvenilirlik_ve_aciklanabilir_yapay_zeka.ipynb) · [Prompt kütüphanesi](tr/hafta-09/PROMPTLAR.md) · [PDF ders notu](tr/hafta-09/Hafta09_Ders_Notlari.pdf)

### Hafta 10: Klinik karar destek sistemleri (CDSS)

Oturumun CDSS tasarım prensiplerine ayrılan ilk 2 saati, klinik karar destek sisteminin (CDSS) ne olduğunu ve klinik iş akışına entegrasyonunu, Streamlit ile web arayüzü geliştirmeyi, HL7 FHIR standardına kavramsal bir girişi ve Flask ile FastAPI'yle gerçek zamanlı bir tahmin API'sini kapsar. Deployment ve yayımlamaya ayrılan son 2 saat ise model versiyonlama ve güncelleme stratejisini, klinik AI'da insan gözetimini (human-in-the-loop), FDA De Novo ve CE MDR süreçlerine girişi ve Kişisel Verilerin Korunması Kanunu (KVKK) kapsamında hasta rızasını ve veri gizliliğini kapsamaktadır. **Oturumdaki mini proje:** AF tespit CDSS: EKG yükle → model tahmin eder → SHAP açıklama gösterir → rapor üretir. **Haftalık proje:** Kullanıcı test oturumu: Geri bildirimlerle CDSS prototipini iyileştirme. **Veriler:** MIT-BIH Atriyal Fibrilasyon Veri Tabanı ve sanal kliniğin telemetri servisi; VC-0128'in bir saatlik EKG dosyasıyla birlikte. **Sanal kliniğin aşaması:** Yatak başında karar desteği.

Malzemeler: [Hafta sayfası](tr/hafta-10/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-10/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-10/lab.html) · [Jupyter Notebook](tr/hafta-10/NB10_klinik_karar_destegi.ipynb) · [Prompt kütüphanesi](tr/hafta-10/PROMPTLAR.md) · [PDF ders notu](tr/hafta-10/Hafta10_Ders_Notlari.pdf)

### Hafta 11: Final projesi ve mezuniyet

Oturumun final proje geliştirmeye ayrılan ilk 2 saati, problem seçimini, yani katılımcının kendi kliniğinden gerçek bir soruyu, veri hazırlığını ve model seçimini, model eğitimini, optimizasyonunu ve XAI entegrasyonunu ve klinik geçerlilik değerlendirme tasarımını kapsar. Sunum, kapanış ve gelecek tartışmalarına ayrılan son 2 saatte ise kişi başına 5–7 dakikalık final proje sunumları, jüri ve katılımcı değerlendirmesi, sertifika töreni ve kardiyoloji AI alanındaki kariyer yolları ve kaynaklar yer almaktadır. **Oturumdaki mini proje:** Kişisel/grup final projesi: Gerçek kardiyoloji problemi üzerinde uçtan uca AI pipeline. **Haftalık proje:** Final proje sunumu + "Klinik Pratiğimde AI Nasıl Kullanacağım?" kişisel eylem planı. **Veriler:** Her katılımcı kendi verilerini seçer (final projesi sayfasına bakın). **Sanal kliniğin aşaması:** Katılımcıların birimleri: Final projeleri.

Malzemeler: [Hafta sayfası](tr/hafta-11/README.md) · [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/ders.html) · [Etkileşimli lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/lab.html) · [Jupyter Notebook](tr/hafta-11/NB11_final_projesi_atolyesi.ipynb) · [Prompt kütüphanesi](tr/hafta-11/PROMPTLAR.md) · [PDF ders notu](tr/hafta-11/Hafta11_Ders_Notlari.pdf)

## Değerlendirme ve sertifika

| Bileşen | Ağırlık | Sertifika koşulu |
|---|---|---|
| Haftalık projeler (1-10. haftalar) | Yüzde 40 | Her projeden en az yüzde 70 |
| Final projesi (sunum ve kod) | Yüzde 40 | Jüri ve katılımcı değerlendirmesi |
| Katılım ve etkin öğrenme | Yüzde 20 | En az yüzde 80 devam |

Her haftalık proje 100 puan üzerinden değerlendirilir. Sanal kliniğin gerçek değerleriyle ya da bir referansla karşılaştırılarak doğrulanmış doğru sonuçlar 40 puandır. Öğretildiği biçimde uygulanmış ve açıklanmış yöntemler 20 puandır. Klinik anlamın ve sınırlılıkların tartışılması 20 puandır. YZ kullanım günlüğü, kod güvenlik kontrol listesinin kullanımı ve her sonucu yeniden üreten bir Jupyter Notebook son 20 puanı oluşturur. Final projesinin değerlendirme ölçütleri [final projesi sayfasında](tr/final-projesi/README.md) yer almaktadır.

## Haftalık projelerin teslimi

Haftalık projeler, bir sonraki haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. Konu satırı haftayı ve katılımcıyı belirtir, örneğin "TKD YZ, Hafta 1, Ad Soyad". E-posta, YZ kullanım günlüğünü içeren ve [rapor şablonuyla](tr/sablonlar/Rapor_Sablonu.docx) yazılmış raporu, tamamlanmış Jupyter Notebook'u ve etkileşimli labdan dışa aktarılan öğrenme günlüğünü içerir.

## Üretken yapay zekâ kullanım kuralları

Üretken YZ araçlarının kullanımına bu eğitimde izin verilir ve bu araçlar öğretimin bir parçasıdır. Dört kural geçerlidir. Birincisi, hiçbir prompta hasta verisi girmez: Gerçek hastaların adları, doğum tarihleri, protokol numaraları ya da kayıtları kullanılmaz. İkincisi, haftalık ya da final projesi için bir YZ aracının her kullanımı, araç, prompt, neyin kontrol edildiği ve neyin değiştirildiği bilgileriyle YZ kullanım günlüğüne kaydedilir. Üçüncüsü, katılımcı teslim ettiği kodun her satırından sorumludur ve onu açıklayabilmelidir. Bir asistanla yazılan kod, sonuçları kullanılmadan önce kod güvenlik kontrol listesiyle denetlenir. Dördüncüsü, raporlardaki yorum ve tartışma katılımcının kendisine aittir. Bir asistan dil konusunda yardımcı olabilir ve bu yardım da günlüğe kaydedilir. [Prompt yolu](PROMPT_PATH.tr.md) aynı kuralları her alıştırmaya uygular; bu yoldan gelen kod da elle yazılmış kod gibi değerlendirilir.

## Veri koruma ve etik

Eğitimde yalnızca sentetik veriler ve açık araştırma verileri kullanılır. Katılımcının kurumuna ait gerçek hasta verileri, final projesinde yalnızca kurumun izniyle ve gerektiğinde etik kurul onayıyla kullanılabilir. Bu veriler KVKK'ya uygun olarak katılımcının kendi bilgisayarında işlenir [1]. Hiçbir zaman bir bulut hizmetine ya da bir YZ sohbetine aktarılmaz. Sanal kliniğin sentetik hastaları öğretim malzemesidir ve klinik kullanım için değildir.

## Devam

Sertifika için oturumların en az yüzde 80'ine, yani 11 oturumun en az 9'una katılım gerekir. Bir oturumu kaçıran katılımcı, haftayı hafta sayfasındaki çalışma yolunu izleyerek tamamlar; bu yol her adım için bireysel çalışma süresini verir.

## Malzemeler ve ortam

Her hafta için ders sayfasına, etkileşimli laba, Jupyter Notebook'a, prompt kütüphanesine ve PDF ders notuna bağlantı veren bir hafta sayfası vardır. [SETUP.tr.md](SETUP.tr.md) Jupyter Notebook'ların çalıştığı iki ortamı, yani Google Colab'ı ve kişinin kendi bilgisayarındaki Jupyter'i anlatır; [başlangıç Jupyter Notebook'u](tr/baslangic/NB00_baslangic.ipynb) 1. haftadan önce iki yolun ilk adımlarını hazırlar. [DATASETS.tr.md](DATASETS.tr.md) veri setlerini lisanslarıyla, [PYTHON_PATH.tr.md](PYTHON_PATH.tr.md) ise haftaların Python adımlarını listeler. [PROMPT_PATH.tr.md](PROMPT_PATH.tr.md) prompt yolunu ve bu yolda kullanılabilecek YZ asistanlarını, [OWN_DATA.tr.md](OWN_DATA.tr.md) ise eğitimin yöntemlerinin kişinin kendi kliniğinin verilerine nasıl uygulanacağını anlatmaktadır.

## İletişim

İçerikle ilgili sorular oturumlarda ya da utkukose@sdu.edu.tr veya utkukose@gmail.com adresine e-postayla sorulabilir. Malzemelerdeki hatalar deponun [issues](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/issues) bölümünden bildirilebilir.

## Kaynaklar

1. Kişisel Verilerin Korunması Kanunu, Kanun No. 6698. (2016). *Resmî Gazete, 29677 (7 Nisan 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5
---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
