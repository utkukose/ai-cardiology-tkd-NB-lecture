<div align="center">

# Hafta 2: Makine öğrenmesi temelleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği

*Risk faktörlerinden olasılığa, hastalardan fenogruplara*

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [Kurulum](../../SETUP.tr.md) · [English](../../en/week-02/README.md)

</div>

## Hafta hakkında

scikit-learn ile denetimli öğrenme: Cleveland verisinde koroner arter hastalığı için lojistik regresyon, karışıklık matrisi ve alıcı işletim karakteristiği (ROC) eğrisi, çapraz doğrulama ve veri sızıntısı, karar ağaçları ve rastgele ormanlar, nadir sonuçların tuzakları. Ardından denetimsiz öğrenme k-ortalamalarla kalp yetersizliği fenogruplarını bulur; Kaplan-Meier eğrileri ve log-rank testi bu grupların prognozunu karşılaştırır. Sanal klinik 2000 hastaya ulaşır ve risk polikliniğini açar.

Oturumda 4 saat, haftalık proje için yaklaşık 3 saat.

## Haftanın rotası

Ders sayfası haftanın ana rotasıdır. Kod ya da prompt (istem) içermez ve etkileşimli labla birlikte yukarıdan aşağıya okunur. Her uygulama durağında her katılımcı Jupyter defterindeki iki yoldan birini seçer: Kodu hazır promptlarla bir yapay zekâ (YZ) asistanının yazdığı, katılımcının ise çalıştırıp denetlediği **prompt yolu** (Kısım 1) ya da kodu katılımcının yazdığı **Python yolu** (Kısım 2). İki yol da aynı sonuçlara varır. Defter, kurulum gerektirmeyen Google Colab'da da kendi bilgisayarınızdaki Jupyter'de de çalışır ([kurulum](../../SETUP.tr.md)).

|  | Ana rota: ders sayfası ve etkileşimli lab | Uygulama durağı: yolunuzu seçin |
|---|---|---|
| 1 | [Bir sayfada makine öğrenmesi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#machine-learning-in-one-page), [Lojistik regresyon: Risk faktörlerinden bir olasılığa](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#logistic-regression-from-risk-factors-to-a-probability), [Bir modeli ölçmek: Karışıklık matrisi ve ROC eğrisi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#measuring-a-model-confusion-matrix-and-roc-curve) | **[Durak 1: İlk risk modeli](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-1)**<br>Prompt yolu: Kısım 1, Durak 1<br>Python yolu: Kısım 2, Python adımı 2, 1. ve 2. bölümler |
| 2 | [Eğitim ve test: Çapraz doğrulama ve veri sızıntısı](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#training-and-testing-cross-validation-and-data-leakage), [Karar ağaçları ve rastgele ormanlar](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#decision-trees-and-random-forests), [Nadir sonuçlar: Dengesiz veri](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#rare-outcomes-imbalanced-data) | **[Durak 2: Bir modeli dürüstçe sınamak](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-2)**<br>Prompt yolu: Kısım 1, Durak 2<br>Python yolu: Kısım 2, 3-6. bölümler |
| 3 | [Denetimsiz öğrenme: k-ortalamalar ve fenogruplar](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#unsupervised-learning-k-means-and-phenogroups), [Sağkalım analizi: Kaplan-Meier ve log-rank testi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#survival-analysis-kaplan-meier-and-the-log-rank-test), [YZ asistanıyla çalışmak, 2. bölüm: Bir modeli denetlemek](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#ai-pair-programming-part-2-reviewing-a-model-built-by-an-assistant) | **[Durak 3: Alt gruplar, sağkalım ve denetlenecek bir model](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#stop-3)**<br>Prompt yolu: Kısım 1, Durak 3<br>Python yolu: Kısım 2, 7-9. bölümler |
|  | [Haftanın makalesi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#the-paper-of-the-week), [Sanal klinik, 2. aşama: Risk polikliniği açılıyor](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#the-virtual-clinic-stage-2-the-risk-outpatient-clinic-opens) | Kendi verinizle bölümü, haftanın makalesi ve sanal klinik |

## Malzemeler

| Malzeme | Aç | İçeriği |
|---|---|---|
| **Ders sayfası (ana rota)** | [Ders sayfasını aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html) | Vaka, çözümlü örnekleriyle kavramlar, k-ortalamaların üç boyutlu (3B) sahnesi, iki animasyon, bilgi kontrolleri, üç uygulama durağı, kendi verinizle bölümü, tekrar kartları ve kaynaklar. Kod ve prompt içermez. |
| **Etkileşimli lab** | [Etkileşimli labı aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/lab.html) | F bölümündeki prompt atölyesi dâhil kod gerektirmeyen A-F bölümleri, öz değerlendirme, yansıtma ve dışa aktarılabilen öğrenme günlüğü |
| **Jupyter defteri** | [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb)<br>[Jupyter için indir](NB02_makine_ogrenmesi_temelleri.ipynb) | Kısım 1, prompt yolu: her biri hazır bir prompt, YZ asistanının kodu için bir hücre, otomatik bir kontrol ve hazır kod içeren dokuz adımlı üç durak. Kısım 2, Python yolu: Python adımı 2, A-J alıştırmalarıyla 1-10. bölümler, bir uygulama anahtarı ve yedi alanın uygulama görevleri. |
| **Prompt kütüphanesi** | [PROMPTLAR.md](PROMPTLAR.md) | Prompt yolunun bütün promptları (GitHub'da her birinin yanında kopyalama düğmesi bulunur), kodu onarmak için promptlar ve haftalık projenin prompt yolu |
| **PDF ders notu** | [Hafta02_Ders_Notlari.pdf](Hafta02_Ders_Notlari.pdf) | Uygulama duraklarıyla ve kendi verinizle bölümüyle birlikte ders sayfasının yazdırılabilir biçimi |

<table>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_c_bolumu_k_ortalamalar_3b.png" alt="Etkileşimli lab, C bölümü: kalp yetersizliği olan hastalarda adım adım üç boyutlu k-ortalamalar." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_kaplan_meier.png" alt="Jupyter defteri, 8. bölüm: üç kümenin ve HFrEF ile HFpEF'nin Kaplan-Meier eğrileri." width="100%"></td></tr>
<tr><td>Etkileşimli lab, C bölümü: kalp yetersizliği olan hastalarda adım adım üç boyutlu k-ortalamalar.</td><td>Jupyter defteri, 8. bölüm: üç kümenin ve HFrEF ile HFpEF'nin Kaplan-Meier eğrileri.</td></tr>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_b_bolumu_esik.png" alt="Etkileşimli lab, B bölümü: koroner arter hastalığı modelinin eşiği, karışıklık matrisi ve ROC eğrisi." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/lab_f_bolumu_prompt_atolyesi.png" alt="Etkileşimli lab, F bölümü: prompt atölyesi. Prompt kartının yedi alanı, kalite göstergesi ve hasta verisi uyarısı." width="100%"></td></tr>
<tr><td>Etkileşimli lab, B bölümü: koroner arter hastalığı modelinin eşiği, karışıklık matrisi ve ROC eğrisi.</td><td>Etkileşimli lab, F bölümü: prompt atölyesi. Prompt kartının yedi alanı, kalite göstergesi ve hasta verisi uyarısı.</td></tr>
</table>

## Haftanın vakası

**VC-0246, 57 yaşında, erkek**, yeni açılan risk polikliniğine başvurur. Sigara içmektedir, tedavi altında hipertansiyonu vardır; LDL kolesterolü 170 mg/dL, HDL kolesterolü 36 mg/dL'dir. Efor testinde angina ve 1,6 mm ST çökmesi gelişmiştir. Kliniğin bir sayıya, yani hastanın koroner arter hastalığı olasılığına ihtiyacı vardır; bu sayıya ne kadar güvenilebileceğini de bilmesi gerekir. [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html) onun vakasıyla açılır; klinik soruyu son bölümde cevaplar.

## Öğrenme çıktıları

Hafta sonunda katılımcıların bir klinik tabloyu modele hazırlayabilmeleri ve scikit-learn ile bir lojistik regresyonu uydurup okuyabilmeleri ve kullanabilmeleri beklenmektedir. Bir modeli karışıklık matrisi, duyarlılık, özgüllük, öngörü değerleri, ROC eğrisi ve eğri altındaki alanla ölçebilmeli; test hastalarından bilgi sızdırmadan performansını çapraz doğrulamayla kestirebilmelidirler. Bir karar ağacını rastgele bir ormanla karşılaştırabilmeli, nadir sonuçlarda doğruluğun neden yanılttığını ve pozitif öngörü değerinin prevalansa nasıl bağlı olduğunu açıklayabilmelidirler. Son olarak k-ortalamalarla hasta alt gruplarını bulabilmeli, bu grupların prognozunu Kaplan-Meier eğrileri ve log-rank testiyle karşılaştırabilmeli ve bir YZ asistanının kurduğu modeli dört soruyla denetleyebilmelidirler.

## Çalışma yolu

Oturuma katılanlar ana rotayı ve uygulama duraklarını oturumda tamamlar. Haftayı kendi başına izleyenler, örneğin bir oturumu kaçıranlar, aşağıdaki sürelerle plan yapabilir.

| Adım | Etkinlik | Prompt yolu | Python yolu |
|---|---|---|---|
| 1 | Haftanın vakasını ve ders sayfasını 1. uygulama durağına kadar okuyun; etkileşimli labın A ve B bölümlerini ve bilgi kontrollerini yapın | 55 dakika | 55 dakika |
| 2 | 1. uygulama durağı: Prompt yolunda Kısım 1, Durak 1; Python yolunda Python adımı 2 ile 1. ve 2. bölümler | 30 dakika | 1 saat 10 dakika |
| 3 | 2. uygulama durağına kadar okumayı sürdürün: çapraz doğrulama, ağaçlar ve ormanlar, nadir sonuçlar | 35 dakika | 35 dakika |
| 4 | 2. uygulama durağı: Kısım 1, Durak 2 ya da 3-6. bölümler | 30 dakika | 1 saat |
| 5 | 3. uygulama durağına kadar okumayı sürdürün; etkileşimli labın C-F bölümlerini yapın | 50 dakika | 50 dakika |
| 6 | 3. uygulama durağı: Kısım 1, Durak 3 ya da 7-9. bölümler | 30 dakika | 50 dakika |
| 7 | Haftanın makalesini, sanal kliniğin aşamasını ve kendi verinizle bölümünü okuyun | 30 dakika | 30 dakika |
| 8 | Etkileşimli labdaki öz değerlendirmeyi yapın (sekme: Kendini sına), yansıtmayı yazın ve öğrenme günlüğünü dışa aktarın | 20 dakika | 20 dakika |
| | **Haftalık proje dışında toplam** | **4 saat 40 dakika** | **6 saat 10 dakika** |
| 9 | Haftalık projeyi iki yoldan biriyle tamamlayın | 3 saat | 3 saat |

## Oturumun eğitim akışı

Haftanın dört saatlik oturumu aşağıdaki plana göre işlenir. Plan, malzemelerin canlı bir oturumda nasıl bir araya geldiğini göstermek için paylaşılmaktadır.

| Süre | Etkinlik |
|---|---|
| 0:00-0:15 | Haftanın vakası VC-0246 ve haftanın rotası. Her katılımcı defteri Google Colab'da ya da Jupyter'de açar ve 0. bölümü çalıştırır. |
| 0:15-0:55 | Ana rota: tek sayfada makine öğrenmesi, etkileşimli labın A bölümüyle lojistik regresyon, B bölümüyle karışıklık matrisi ve ROC eğrisi. |
| 0:55-1:35 | İki grupta 1. uygulama durağı: prompt yolu ve Python yolu. Sonunda iki grup test AUC değerlerini karşılaştırır. |
| 1:35-1:50 | Ara. |
| 1:50-2:30 | Ana rota: çapraz doğrulama ve veri sızıntısı, ağaçlar ve ormanlar, nadir sonuçlar. 2. uygulama durağı. |
| 2:30-3:20 | Ana rota: C bölümüyle üç boyutta k-ortalamalar, D bölümüyle elle Kaplan-Meier, E ve F bölümleriyle bir modeli denetlemek. 3. uygulama durağı. |
| 3:20-3:45 | Haftanın makalesi, sanal kliniğin risk polikliniği ve kendi verinizle bölümü. |
| 3:45-4:00 | Haftalık proje ve sorular. |

## Haftalık proje

**Ne yapılacak?** Sanal kliniğin kaydındaki kalp yetersizliği fenogruplarını bulun ve prognozlarını karşılaştırın. Önce HFrEF ya da HFpEF olan hastaları dokuz standartlaştırılmış değişkenle, k = 2-6 için k-ortalamalarla kümeleyin; k değerini siluet değeri ve klinik anlamla seçin. İkinci olarak her kümeyi bir tabloda tanımlayın ve kısa bir klinik adla adlandırın. Üçüncü olarak kümelerin ve HFrEF ile HFpEF'nin Kaplan-Meier eğrilerini çizin ve log-rank testiyle karşılaştırın. Dördüncü olarak kümeleri dersin kayda gizlediği fenogruplarla bir çapraz tablo ve düzeltilmiş Rand indeksiyle karşılaştırın. Ardından kümelemenin, tek başına ejeksiyon fraksiyonunun kaçırdığı neyi bulduğunu yazın.

**Nereye bakılacak?** Ders: "Denetimsiz öğrenme: k-ortalamalar ve fenogruplar", "Sağkalım analizi: Kaplan-Meier ve log-rank testi" ve "Haftanın makalesi" bölümleri. Etkileşimli lab: C, D ve F bölümleri. Jupyter defteri: 7. ve 8. bölümler.

**Prompt yolu.** Proje, her adım için bir prompt olmak üzere [prompt kütüphanesindeki](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-02/PROMPTLAR.md#haftal%C4%B1k-projenin-prompt-yolu) dört promptla da kurulabilir. Bir promptun testi sağlanmadan sonraki prompta geçilmez.

**Örnek.** 5. ayda risk altındaki üç hastadan birinde olay görülürse çarpan $1 - 1/3 = 0{,}667$ olur. 5. aydan önceki sağkalım 0,800 ise eğri $0{,}800 \times 0{,}667 = 0{,}533$ değerine iner. Bir kümenin Kaplan-Meier eğrisindeki her basamak aynı yolla hesaplanır.

**Ne teslim edilecek?** [Rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılmış, bir-iki sayfalık bir rapor: kümelerin tablosu, Kaplan-Meier şekli, iki log-rank testi ve gizli fenogruplarla karşılaştırma. Rapora YZ kullanım günlüğünü (araç, prompt, neyin denetlendiği, neyin değiştirildiği) ve çıktılarıyla birlikte Jupyter defterini ekleyin.

**Teslim.** Haftalık proje, 3. haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. E-postaya "Ne teslim edilecek?" başlığında sayılan öğeler ve etkileşimli labdan dışa aktarılan öğrenme günlüğü eklenir. Haftalık projeler değerlendirmenin yüzde 40'ını oluşturur; değerlendirme ölçütleri izlencede yer almaktadır.

## Kendi verinizle

Ders sayfası, haftanın yöntemlerini kendi verinize uygulamayı anlatan bir bölümle biter: hangi sorunun hangi yönteme uyduğu, önce neyin denetleneceği, etik kurul onayı, Kişisel Verilerin Korunması Kanunu (KVKK) ve hesabın nerede yapılacağı. [Ders sayfasında okuyun](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#with-your-own-data).

## İsteğe bağlı araştırma ödevi

PubMed'de, 2020 ya da sonrasında yayımlanmış ve kalp yetersizliği hastalarının prognozu için bir makine öğrenmesi modeli geliştiren ya da doğrulayan bir çalışma bulun. Çalışmayı yarım sayfada özetleyin: hasta grubu, sonuç ve izlem süresi, model, modelin nasıl doğrulandığı ve bir kısıtlılık. [Haftanın makalesindeki](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#the-paper-of-the-week) üç soru özete yol gösterebilir. Ödev notlandırılmaz; 3. haftadaki dış doğrulama tartışmasına hazırlık niteliğindedir.

## Bu haftadan sonra sanal klinik

Sanal klinik 2. haftada beş yıllık izlem verisi olan 2000 hastaya ulaşır ve risk polikliniğini açar. Kliniğin koroner arter hastalığı modeli, kaydı üreten gerçek etkilerle karşılaştırılır; kalp yetersizliği olan hastaları da prognozu farklı fenogruplara ayrılır. Sonuçlar ders sayfasının [Sanal klinik, 2. aşama](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-02/ders.html#the-virtual-clinic-stage-2-the-risk-outpatient-clinic-opens) bölümündedir.

## Gelecek hafta

**Hafta 3: Derin öğrenme ve evrişimli sinir ağları.** Sanal klinik görüntüleme laboratuvarını açar: Sinir ağları görüntülerden öğrenir, evrişimli bir ağ ACDC'nin sine kardiyak manyetik rezonans incelemelerini normal kalp, dilate ve hipertrofik kardiyomiyopati olarak sınıflandırır; karışıklık matrisi ve F1 skoru aşırı öğrenmeye dikkat edilerek okunur. Defter ACDC'yi kendisi indirir. Oturumun mini projesi, Stanford AIMI'de kişisel kayıt gerektiren EchoNet-Dynamic'i kullanır; projeyi kendisi çalıştırmak isteyen katılımcılar oturumdan önce kaydolabilir ([DATASETS.tr.md](../../DATASETS.tr.md#3-haftanın-veri-setleri)). [Eğitimin planına](../../README.tr.md#on-bir-hafta) bakın.

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
