<div align="center">

# Hafta 2: Makine öğrenmesi temelleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği

*İstatistikten akıllı modellere: Kardiyoloji odaklı*

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [Kurulum](../../SETUP.tr.md) · [English](../../en/week-02/README.md)

</div>

Hafta hakkında daha ayrıntılı bilgi için bu sayfayı okumaya devam ediniz. Haftaya doğrudan ders sayfasından devam etmek isterseniz bu bağlantıyı kullanınız: **[Haftanın ders sayfasını açınız](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html)**. Ders sayfası haftanın ana rotasıdır; sayfadaki kutular etkileşimli labı ve Jupyter Notebook'u ilgili yerde açmaktadır.

## Hafta hakkında

İlk iki saatte scikit-learn ile denetimli modeller kurulur. Modelleme pipeline'ı ilk bir regresyon çizgisiyle tanıtılır ve Cleveland verisinde koroner arter hastalığı (KAH) için lojistik regresyon kurulur. Model çapraz doğrulama, alıcı işletim karakteristiği (ROC) eğrisi ve eğri altındaki alanla değerlendirilir; duyarlılığı ve özgüllüğü yorumlanır, ardından bir karar ağacı bir rastgele ormanla karşılaştırılır. Mini projede bir KAH tahmin modeli kurulur ve modelin ROC eğrisi ile AUC değeri incelenir. Son iki saatte dengesiz veri SMOTE ile ele alınır, kalp yetersizliği fenogrupları k-ortalamalar yöntemiyle bulunur, UMAP ve t-SNE haritalarında gösterilir ve prognozları Kaplan-Meier eğrileri ile log-rank testiyle karşılaştırılır. Sanal kliniğin hasta sayısı 2.000'e ulaşır ve klinikte risk polikliniği açılır.

Oturum 4 saat sürer. Haftalık proje için yaklaşık 3 saat ayrılmalıdır.

## Haftanın vakası

**VC-0246, 57 yaşında bir erkek hastadır.** Yeni açılan risk polikliniğine başvurmuştur. Sigara içmektedir ve tedavi altında hipertansiyonu vardır; LDL kolesterolü 170 mg/dL, HDL kolesterolü 36 mg/dL'dir. Efor testinde anjina ve 1,6 mm ST çökmesi gelişmiştir. Kliniğin bir sayıya, yani hastanın koroner arter hastalığı olasılığına ihtiyacı vardır; bu sayıya ne kadar güvenilebileceğini de bilmesi gerekir. [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html) bu vakayla açılır; sanal klinik soruyu son bölümde cevaplar.

## Malzemeler

| Malzeme | Aç | Ne işe yarar? |
|---|---|---|
| **Ders sayfası** | [Ders sayfasını aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html) | Haftanın konu anlatımını içeren bu sayfa yukarıdan aşağıya doğru okunmak üzere hazırlanmıştır. Sayfadaki kutular sizi uygulama duraklarına yönlendirir; sayfada kod ya da prompt (istem) bulunmamaktadır. |
| **Etkileşimli lab** | [Etkileşimli labı aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/lab.html) | Kod gerektirmeyen A-F bölümleri, ders sayfasında yeri geldiğinde açılmaktadır. F bölümü bir prompt atölyesidir. Öz değerlendirme ve öğrenme günlüğü de bu labda yer alır. |
| **Python Notebook** | [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb)<br>[Jupyter Notebook için indir (zip)](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/raw/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.zip) | Uygulama durakları burada çalışılır; her durakta Python temelleri, promptlar ve hazır bir uygulama bulunmaktadır. Python Notebook, Google Colab'da kurulum gerektirmeden ya da kendi bilgisayarınızdaki Jupyter Notebook'ta çalışabilir. Jupyter için zip dosyasını indiriniz, içindeki .ipynb dosyasını bir klasöre çıkarınız ve dosyayı Jupyter'de açınız. Her bölüm, bölümün kullandığı kurulumu ve veri çağrılarını yineleyen bir başlangıç hücresiyle açılır. |
| **Prompt kütüphanesi** | [PROMPTLAR.md](PROMPTLAR.md) | Uygulama duraklarının ve haftalık projenin bütün promptları, kodu onarmaya, açıklatmaya ve denetlemeye yönelik promptlarla birlikte burada toplanmıştır. GitHub'da her promptun yanında bir kopyalama düğmesi bulunur. |
| **PDF ders notu** | [Hafta02_Ders_Notlari.pdf](Hafta02_Ders_Notlari.pdf) | Ders sayfasının yazdırılabilir biçimidir. |

## Çalışma yolu

Ders sayfası yukarıdan aşağıya doğru okunur; etkileşimli labın bölümleri de sayfada yeri geldikçe açılır. Uygulama duraklarında çalışma Jupyter Notebook'ta sürmektedir ve oradaki her durak üç bölümden oluşur. **Python temelleri** bölümünde durağın gerektirdiği Python bilgisi öğretilir. **Prompt ile uygulama** bölümünde kodu hazır promptlarla bir yapay zekâ (YZ) asistanı yazar; katılımcının görevi bu kodu çalıştırmak ve sonucu denetlemektir. **Hazır uygulama** bölümünde ise durağın baştan sona çalışan programı yer almaktadır. Bölümleri bu sırayla izlemeniz önerilir; Python biliyorsanız promptlarla, yalnızca sonucu görmek istiyorsanız hazır uygulamayla başlayabilirsiniz. Her bölüm, bölümün kullandığı kurulumu ve veri çağrılarını yineleyen bir başlangıç hücresiyle açılır; bu sayede bölüm doğrudan açıldığında da çalışabilmektedir. Lab bölümlerinin ve Jupyter Notebook'taki durakların sonunda, sizi ders sayfasında okumanın devam ettiği yere geri götüren bir bağlantı bulunmaktadır. Nerede kaldığınızı bulamazsanız bu tabloya dönünüz. Oturuma katılanlar bu adımları oturum sırasında yapar. Tablodaki süreler, haftayı kendi başına izleyenler, örneğin bir oturumu kaçıranlar için verilmiştir.

| Adım | Ne yapılır? | Süre |
|---|---|---|
| 1 | Haftanın vakasını ve ders sayfasının ilk iki saatini 1. uygulama durağına, yani mini projeye kadar [okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html); etkileşimli labın A ve B bölümlerini yapınız ve bilgi kontrolü sorularını cevaplayınız | 1 saat 10 dakika |
| 2 | **[1. uygulama durağı: Mini proje: KAH tahmin modeli, ROC eğrisi ve AUC](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-1)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-1-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-1-prompt) ([promptlar](PROMPTLAR.md#durak-1-mini-proje-kah-tahmin-modeli-roc-e%C4%9Frisi-ve-auc)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-1-app) | 1 saat 15 dakika |
| 3 | 2. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#decision-trees-and-random-forests) (karar ağacı ve rastgele orman karşılaştırması, SMOTE ile dengesiz veri) | 35 dakika |
| 4 | **[2. uygulama durağı: Bir modeli dürüstçe sınamak](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-2)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-2-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-2-prompt) ([promptlar](PROMPTLAR.md#durak-2-bir-modeli-d%C3%BCr%C3%BCst%C3%A7e-s%C4%B1namak)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-2-app) | 1 saat 5 dakika |
| 5 | 3. uygulama durağına kadar [okumayı sürdürün](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#unsupervised-learning-k-means-and-phenogroups) (k-ortalamalar, UMAP ve t-SNE haritaları, Kaplan-Meier eğrisi) ve etkileşimli labın C, D, E ve F bölümlerini yapınız | 55 dakika |
| 6 | **[3. uygulama durağı: Alt gruplar, sağkalım ve denetlenecek bir model](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-3)**<br>[Python temelleri](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-3-basics) · [Prompt ile uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-3-prompt) ([promptlar](PROMPTLAR.md#durak-3-alt-gruplar-sa%C4%9Fkal%C4%B1m-ve-denetlenecek-bir-model)) · [Hazır uygulama](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=stop-3-app) | 55 dakika |
| 7 | Haftanın makalesini, sanal kliniğin bu haftaki aşamasını ve "Kendi verinizle" bölümünü [okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#the-paper-of-the-week) | 30 dakika |
| 8 | [Etkileşimli labın](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/lab.html) "Kendini sına" sekmesindeki öz değerlendirmeyi yapınız, yansıtma yazınızı yazınız ve öğrenme günlüğünü dışa aktarınız | 20 dakika |
| | **Haftalık proje dışında toplam** | **6 saat 45 dakika** |
| 9 | [Haftalık projeyi](#haftal%C4%B1k-proje) tamamlayınız<br>[Promptlar](PROMPTLAR.md#haftal%C4%B1k-projenin-promptlar%C4%B1) · [Jupyter Notebook'ta haftalık proje](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb#scrollTo=project) | 3 saat |

<table>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_c_bolumu_k_ortalamalar_3b.png" alt="Etkileşimli lab, C bölümü: Kalp yetersizliği olan hastalar üç boyutta, adım adım k-ortalamalar yöntemiyle kümelenir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_kaplan_meier.png" alt="Jupyter Notebook, «Durak 3 · Hazır uygulama»: Üç kümenin ve HFrEF ile HFpEF gruplarının Kaplan-Meier eğrileri çizilir." width="100%"></td></tr>
<tr><td>Etkileşimli lab, C bölümü: Kalp yetersizliği olan hastalar üç boyutta, adım adım k-ortalamalar yöntemiyle kümelenir.</td><td>Jupyter Notebook, «Durak 3 · Hazır uygulama»: Üç kümenin ve HFrEF ile HFpEF gruplarının Kaplan-Meier eğrileri çizilir.</td></tr>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_b_bolumu_esik.png" alt="Etkileşimli lab, B bölümü: Koroner arter hastalığı modelinin eşiği değiştirilir; karışıklık matrisi ve ROC eğrisi buna göre güncellenir." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/lab_f_bolumu_prompt_atolyesi.png" alt="Etkileşimli lab, F bölümü: Prompt atölyesinde prompt kartının yedi alanı doldurulur; bir kalite göstergesi ve hasta verisi uyarısı yazılanı değerlendirir." width="100%"></td></tr>
<tr><td>Etkileşimli lab, B bölümü: Koroner arter hastalığı modelinin eşiği değiştirilir; karışıklık matrisi ve ROC eğrisi buna göre güncellenir.</td><td>Etkileşimli lab, F bölümü: Prompt atölyesinde prompt kartının yedi alanı doldurulur; bir kalite göstergesi ve hasta verisi uyarısı yazılanı değerlendirir.</td></tr>
</table>

## Haftalık proje

**Proje.** HFpEF vs HFrEF hasta kümeleme + Kaplan-Meier sağkalım analizi.

**Ne yapılacak?** Sanal kliniğin kaydındaki kalp yetersizliği fenogruplarını bulunuz ve prognozlarını karşılaştırınız. Önce HFrEF ya da HFpEF tanısı olan hastaları dokuz standartlaştırılmış değişkenle ve k = 2-6 için k-ortalamalar yöntemiyle kümeleyiniz; k değerini siluet değerine ve klinik anlama bakarak seçiniz. Ardından her kümeyi bir tabloda tanımlayınız ve kümeye kısa bir klinik ad veriniz. Sonra kümelerin ve HFrEF ile HFpEF gruplarının Kaplan-Meier eğrilerini çiziniz ve eğrileri log-rank testiyle karşılaştırınız. Daha sonra kümeleri, dersin kayda gizlediği fenogruplarla bir çapraz tablo ve düzeltilmiş Rand indeksi yardımıyla karşılaştırınız. Son olarak kümelemenin, tek başına ejeksiyon fraksiyonunun kaçırdığı hangi bilgiyi ortaya çıkardığını yazınız.

**Nereye bakılacak?** Ders sayfasında "K-Means ile hasta alt gruplarını bulma", "UMAP / t-SNE görselleştirmesi", "Survival analysis (sağkalım analizi): Kaplan-Meier eğrisi" ve "Haftanın makalesi" bölümlerine bakınız. Etkileşimli labda C, D ve F bölümleri, Jupyter Notebook'ta ise 3. uygulama durağının hazır uygulaması yardımcı olur.

**Promptlarla.** Proje, [prompt kütüphanesindeki](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/PROMPTLAR.md#haftal%C4%B1k-projenin-promptlar%C4%B1) dört promptla da yapılabilir; kütüphanede her adım için bir prompt bulunmaktadır. Her promptun tablosu, Jupyter Notebook'un sonundaki "Haftalık proje" bölümünde hazırlanır ve bu bölüm tek başına da açılabilir. Bir promptun testi sağlanmadan sonraki prompta geçilmemeli ve her prompt YZ kullanım günlüğüne kaydedilmelidir.

**Örnek.** 5. ayda risk altındaki üç hastadan birinde olay görülürse çarpan $1 - 1/3 = 0{,}667$ olur. 5. aydan önceki sağkalım 0,800 ise eğri $0{,}800 \times 0{,}667 = 0{,}533$ değerine iner. Bir kümenin Kaplan-Meier eğrisindeki her basamak aynı yolla hesaplanır.

**Ne teslim edilecek?** [Rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılmış, bir ya da iki sayfalık bir rapor teslim edilir. Raporda kümelerin tablosu, Kaplan-Meier şekli, iki log-rank testi ve gizli fenogruplarla karşılaştırma yer almalıdır. Rapora YZ kullanım günlüğünü (kullanılan araç, prompt, neyin denetlendiği ve neyin değiştirildiği) ve çıktılarıyla birlikte Jupyter Notebook'u ekleyiniz.

**Teslim.** Haftalık proje, 3. haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. E-postaya "Ne teslim edilecek?" başlığında sayılan öğeler ve etkileşimli labdan dışa aktarılan öğrenme günlüğü eklenir. Haftalık projeler değerlendirmenin yüzde 40'ını oluşturur; değerlendirme ölçütleri izlencede yer almaktadır.

## Öğrenme çıktıları

Haftanın sonunda katılımcıların bir klinik tabloyu modele hazırlayabilmeleri, scikit-learn ile bir modelleme pipeline'ı kurabilmeleri, doğrusal ve lojistik regresyon modellerini eğitip sonuçlarını okuyabilmeleri beklenmektedir. Bir modelin başarımını karışıklık matrisi, duyarlılık, özgüllük, öngörü değerleri, ROC eğrisi ve eğri altındaki alanla ölçebilmeli, duyarlılık ile özgüllüğü bir hastalığı dışlama ya da doğrulama açısından yorumlayabilmeli ve başarımı test hastalarından bilgi sızdırmadan çapraz doğrulamayla kestirebilmelidirler. Bir karar ağacını rastgele bir ormanla karşılaştırabilmeli, nadir sonuçlarda doğruluğun neden yanılttığını ve SMOTE ile sınıf ağırlıklarının olasılıkları nasıl değiştirdiğini açıklayabilmelidirler. Son olarak k-ortalamalar yöntemiyle hasta alt gruplarını bulabilmeli, bu grupları bir t-SNE ya da UMAP haritasında gösterebilmeli, prognozlarını Kaplan-Meier eğrileri ve log-rank testiyle karşılaştırabilmeli ve bir YZ asistanının kurduğu modeli dört soruyla denetleyebilmelidirler.

## Oturumun eğitim akışı

Haftanın dört saatlik oturumu aşağıdaki plana göre işlenir. Plan, malzemelerin canlı bir oturumda nasıl bir araya geldiğini göstermek için paylaşılmaktadır.

| Süre | Etkinlik |
|---|---|
| 0:00-0:15 | Haftanın vakası VC-0246 tanıtılır ve haftanın rotası anlatılır. Her katılımcı Jupyter Notebook'u Google Colab'da ya da Jupyter'de açarak 0. bölümü çalıştırır. |
| 0:15-0:45 | İlk iki saat, sınıflandırma ve regresyon: Makine öğrenmesinin temel fikirleri, scikit-learn ile modelleme pipeline'ı ve ilk regresyon çizgisi anlatılır; etkileşimli labın A bölümüyle KAH riski için lojistik regresyon çalışılır. |
| 0:45-1:15 | Çapraz doğrulama, ROC-AUC ve duyarlılık ile özgüllüğün yorumu etkileşimli labın B bölümüyle çalışılır. |
| 1:15-1:45 | Mini proje, 1. uygulama durağı: Her katılımcı Jupyter Notebook'ta, promptlarla ya da Python ile, Cleveland verisinde bir KAH tahmin modeli kurar ve modelin ROC eğrisini ve AUC değerini inceler. Durağın sonunda katılımcıların test kümesindeki AUC değerleri karşılaştırılır. |
| 1:45-2:00 | Karar ağacı ve rastgele orman karşılaştırılır. |
| 2:00-2:10 | Ara. |
| 2:10-2:40 | Son iki saat, kümeleme ve hasta segmentasyonu: SMOTE ile dengesiz veriyle başa çıkma anlatılır. Ardından 2. uygulama durağına geçilir. |
| 2:40-3:20 | C bölümüyle k-ortalamalar yöntemiyle hasta alt grupları bulunur, UMAP ve t-SNE haritaları incelenir, D bölümüyle Kaplan-Meier eğrisi, E ve F bölümleriyle bir modelin denetlenmesi çalışılır. Ardından 3. uygulama durağına geçilir. |
| 3:20-3:45 | Haftanın makalesi, sanal kliniğin risk polikliniği ve "Kendi verinizle" bölümü ele alınır. |
| 3:45-4:00 | Haftalık proje tanıtılır ve sorular cevaplanır. |

## Kendi verinizle

Ders sayfası, haftanın yöntemlerini kendi verilerinize nasıl uygulayabileceğinizi anlatan bir bölümle sona ermektedir. Bu bölümde hangi sorunun hangi yönteme uyduğu, önce neyin denetlenmesi gerektiği, etik kurul onayı, Kişisel Verilerin Korunması Kanunu (KVKK) ve analizin nerede yapılacağı ele alınmaktadır. [Bölümü ders sayfasında okuyunuz](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#with-your-own-data).

## İsteğe bağlı araştırma ödevi

PubMed'de, 2020 ya da sonrasında yayımlanmış ve kalp yetersizliği hastalarının prognozu için bir makine öğrenmesi modeli geliştiren ya da doğrulayan bir çalışma bulunuz. Çalışmayı yarım sayfada özetleyiniz; özette hasta grubu, sonuç ve izlem süresi, model, modelin nasıl doğrulandığı ve çalışmanın bir sınırlılığı yer almalıdır. [Haftanın makalesindeki](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#the-paper-of-the-week) üç soru özetinize yol gösterebilir. Bu ödev notlandırılmaz; 3. haftadaki dış doğrulama tartışmasına hazırlık amacı taşır.

## Bu haftadan sonra sanal klinik

2. haftada sanal kliniğin hasta sayısı, beş yıllık izlem verisiyle birlikte 2.000'e ulaşır ve klinikte risk polikliniği açılır. Kliniğin koroner arter hastalığı modeli, kaydı üreten gerçek etkilerle karşılaştırılır; kalp yetersizliği olan hastalar da prognozu birbirinden farklı fenogruplara ayrılır. Sonuçlar, ders sayfasının [Sanal klinik, 2. aşama](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#the-virtual-clinic-stage-2-the-risk-outpatient-clinic-opens) bölümünde yer almaktadır.

## Gelecek hafta

**Hafta 3: Derin öğrenme ve evrişimli sinir ağları.** Sanal klinikte görüntüleme laboratuvarı açılır. Sinir ağlarının görüntülerden nasıl öğrendiği anlatılır; evrişimli bir ağ da ACDC'nin sine kardiyak manyetik rezonans incelemelerini normal kalp, dilate kardiyomiyopati ve hipertrofik kardiyomiyopati olarak sınıflandırır. Karışıklık matrisi ve F1 skoru, aşırı öğrenmeye dikkat edilerek yorumlanır. ACDC verisi, Jupyter Notebook tarafından otomatik olarak indirilmektedir. Oturumun mini projesi, Stanford AIMI'de kişisel kayıt gerektiren EchoNet-Dynamic'i kullanmaktadır; projeyi kendisi çalıştırmak isteyen katılımcılar oturumdan önce kaydolabilir ([DATASETS.tr.md](../../DATASETS.tr.md#3-haftanın-veri-setleri)). Ayrıntılar için [eğitimin planına](../../README.tr.md#on-bir-hafta) bakınız.

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
