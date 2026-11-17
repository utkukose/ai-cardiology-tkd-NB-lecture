<div align="center">

# Hafta 1: Python ve kardiyoloji veri temelleri

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği

*Programlamaya sıfırdan başlayıp klinik veri analizine*

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [Kurulum](../../SETUP.tr.md) · [English](../../en/week-01/README.md)

</div>

## Hafta hakkında

Sıfırdan Python, pandas ile hasta tabloları, veri olarak elektrokardiyogram (EKG), tek bir kalp vektörünün izdüşümleri olarak on iki derivasyon, QT düzeltmesiyle birlikte otomatik PR, QRS ve QT ölçümü, gerçek PhysioNet kayıtlarında atım tespiti ve kalp hızı değişkenliği ile bir yapay zekâ (YZ) asistanıyla kod yazmanın ilk kuralları.

Oturumda 4 saat, haftalık proje için yaklaşık 3 saat.

## Haftanın rotası

Ders sayfası haftanın ana rotasıdır. Kod ya da prompt (istem) içermez ve etkileşimli labla birlikte yukarıdan aşağıya okunur. Her uygulama durağında her katılımcı Jupyter defterindeki iki yoldan birini seçer: Kodu hazır promptlarla bir yapay zekâ (YZ) asistanının yazdığı, katılımcının ise çalıştırıp denetlediği **prompt yolu** (Kısım 1) ya da kodu katılımcının yazdığı **Python yolu** (Kısım 2). İki yol da aynı sonuçlara varır. Defter, kurulum gerektirmeyen Google Colab'da da kendi bilgisayarınızdaki Jupyter'de de çalışır ([kurulum](../../SETUP.tr.md)).

|  | Ana rota: ders sayfası ve etkileşimli lab | Uygulama durağı: yolunuzu seçin |
|---|---|---|
| 1 | [Uygulamanın iki yolu: Prompt ve Python](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#two-paths-of-practice), [Sanal kardiyoloji kliniği, eğitimin projesi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-virtual-cardiology-clinic-the-project-of-the-course), [pandas ile hasta tabloları](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#patient-tables-with-pandas) | **[Durak 1: Hasta tabloları](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-1)**<br>Prompt yolu: Kısım 1, Durak 1<br>Python yolu: Kısım 2, Python adımı 1, 1. ve 2. bölümler |
| 2 | [Veri olarak EKG](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-ecg-as-data), [Bir vektör olarak kalp: On iki derivasyon, tek kaynak](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-heart-as-a-vector-twelve-leads-one-source), [Aralıklar: PR, QRS ve QT](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#intervals-pr-qrs-and-qt), [QT'nin kalp hızına göre düzeltilmesi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#correcting-the-qt-for-heart-rate) | **[Durak 2: Veri olarak EKG](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-2)**<br>Prompt yolu: Kısım 1, Durak 2<br>Python yolu: Kısım 2, 3-5. bölümler |
| 3 | [Her atımı bulmak: R tepesi tespiti](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#finding-every-beat-r-peak-detection), [Kalp hızı değişkenliği](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#heart-rate-variability), [Gerçek veri: PhysioNet kayıtları](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#real-data-physionet-records), [YZ asistanıyla çalışmak, 1. bölüm: Kod güvenlik kontrol listesi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#ai-pair-programming-part-1-the-code-safety-checklist) | **[Durak 3: Gerçek kayıtlar ve denetlenecek bir fonksiyon](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#stop-3)**<br>Prompt yolu: Kısım 1, Durak 3<br>Python yolu: Kısım 2, 6-9. bölümler |
|  | [Haftanın makalesi](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-paper-of-the-week), [Sanal klinik, 1. aşama: Klinik açılıyor](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-virtual-clinic-stage-1-the-clinic-opens) | Kendi verinizle bölümü, haftanın makalesi ve sanal klinik |

## Malzemeler

| Malzeme | Aç | İçeriği |
|---|---|---|
| **Ders sayfası (ana rota)** | [Ders sayfasını aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) | Vaka, uygulamanın iki yolu, çözümlü örnekleriyle kavramlar, kalp döngüsünün üç boyutlu (3B) sahnesi, iki animasyon, bilgi kontrolleri, üç uygulama durağı, kendi verinizle bölümü, tekrar kartları ve kaynaklar. Kod ve prompt içermez. |
| **Etkileşimli lab** | [Etkileşimli labı aç](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/lab.html) | F bölümündeki prompt atölyesi dâhil kod gerektirmeyen A-F bölümleri, öz değerlendirme, yansıtma ve dışa aktarılabilen öğrenme günlüğü |
| **Jupyter defteri** | [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb)<br>[Jupyter için indir](NB01_python_ve_ekg_temelleri.ipynb) | Kısım 1, prompt yolu: her biri hazır bir prompt, YZ asistanının kodu için bir hücre, otomatik bir kontrol ve hazır kod içeren on adımlı üç durak. Kısım 2, Python yolu: Python adımı 1, A-J alıştırmalarıyla 1-10. bölümler, bir uygulama anahtarı ve dört alanın uygulama görevleri. |
| **Prompt kütüphanesi** | [PROMPTLAR.md](PROMPTLAR.md) | Prompt yolunun bütün promptları (GitHub'da her birinin yanında kopyalama düğmesi bulunur), kodu onarmak için promptlar ve haftalık projenin prompt yolu |
| **PDF ders notu** | [Hafta01_Ders_Notlari.pdf](Hafta01_Ders_Notlari.pdf) | Uygulama duraklarıyla ve kendi verinizle bölümüyle birlikte ders sayfasının yazdırılabilir biçimi |

<table>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_b_bolumu_kalp_vektoru.png" alt="Etkileşimli lab, B bölümü: VC-0317'nin kalp vektörü 3B bir gövdenin içinde ve on iki derivasyondaki izdüşümleri." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_12_derivasyonlu_ekg.png" alt="Jupyter defteri, Python yolu, 4. bölüm: VC-0317'nin 12 derivasyonlu EKG'si." width="100%"></td></tr>
<tr><td>Etkileşimli lab, B bölümü: VC-0317'nin kalp vektörü 3B bir gövdenin içinde ve on iki derivasyondaki izdüşümleri.</td><td>Jupyter defteri, Python yolu, 4. bölüm: VC-0317'nin 12 derivasyonlu EKG'si.</td></tr>
<tr><td width="50%"><img src="ekran-goruntuleri/lab_f_bolumu_prompt_atolyesi.png" alt="Etkileşimli lab, F bölümü: prompt kartının yedi alanı, bir nitelik göstergesi ve bir mahremiyet denetimiyle prompt atölyesi." width="100%"></td><td width="50%"><img src="ekran-goruntuleri/defter_prompt_yolu.png" alt="Jupyter defteri, prompt yolu, 2. durak: hazır bir prompt, bir YZ asistanının kodu ve eğitimin kontrolü." width="100%"></td></tr>
<tr><td>Etkileşimli lab, F bölümü: prompt kartının yedi alanı, bir nitelik göstergesi ve bir mahremiyet denetimiyle prompt atölyesi.</td><td>Jupyter defteri, prompt yolu, 2. durak: hazır bir prompt, bir YZ asistanının kodu ve eğitimin kontrolü.</td></tr>
</table>

## Haftanın vakası

**VC-0317, 67 yaşında, kadın**, ilaç tedavisindeki bir değişiklikten sonra başlayan çarpıntıyla polikliniğe başvuruyor. EKG'sinin otomatik raporu düzeltilmiş QT'yi (QTc) 465 ms olarak veriyor ve uzamış diye işaretliyor. [Ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html) bu vakayla açılmakta, klinik de soruyu son bölümde kendi ölçümleriyle cevaplamaktadır.

## Öğrenme çıktıları

Hafta sonunda katılımcıların bir klinik tabloyu pandas ile yükleyip ortalama, standart sapma, ortanca ve çeyrekler arası açıklıkla özetleyebilmeleri beklenmektedir. Bir EKG'yi örneklerden oluşan bir tablo olarak ele alabilmeli, örnek sayısı ile zaman arasında dönüşüm yapabilmeli, örnekleme frekansının ve çözünürlüğün etkisini açıklayabilmelidirler. On iki derivasyonu tek bir kalp vektörünün izdüşümleri olarak açıklayabilmeli, Einthoven yasasını uygulayabilmeli ve frontal QRS eksenini hesaplayabilmelidirler. PR, QRS ve QT aralıklarını elle ve bilgisayarla ölçebilmeli, QT'yi Bazett ve Fridericia formülleriyle düzeltebilmeli ve iki ölçüm yöntemini Bland-Altman analiziyle karşılaştırabilmelidirler. Ayrıca R tepelerini bulabilmeli, duyarlılığı ve pozitif öngörü değerini raporlayabilmeli, normalden normale aralıkların standart sapmasını (SDNN) ve ardışık farklarının karelerinin ortalamasının karekökünü (RMSSD) hesaplayabilmelidirler. Son olarak birimleri ve bir testi içeren bir prompt yazabilmeli ve bir YZ asistanının yazdığı kodu kod güvenlik kontrol listesiyle denetleyebilmelidirler. Python'da katılımcıların değişkenleri, listeleri, sözlükleri, kararları, döngüleri, fonksiyonları, NumPy dizilerini ve pandas DataFrame'lerini kullanabilmeleri beklenmektedir.

## Çalışma yolu

Oturuma katılanlar ana rotayı ve uygulama duraklarını oturumda tamamlar. Haftayı kendi başına izleyenler, örneğin bir oturumu kaçıranlar, aşağıdaki sürelerle plan yapabilir.

| Adım | Etkinlik | Prompt yolu | Python yolu |
|---|---|---|---|
| 1 | Haftanın vakasını ve ders sayfasını, uygulamanın iki yolu ve sanal klinik dâhil, 1. uygulama durağına kadar okuyun | 40 dakika | 40 dakika |
| 2 | 1. uygulama durağı: Prompt yolunda Kısım 1, Durak 1; Python yolunda Python adımı 1 ile 1. ve 2. bölümler | 30 dakika | 1 saat 15 dakika |
| 3 | 2. uygulama durağına kadar okumayı sürdürün; etkileşimli labın A-C bölümlerini ve bilgi kontrollerini yapın | 1 saat | 1 saat |
| 4 | 2. uygulama durağı: Kısım 1, Durak 2 ya da 3-5. bölümler | 30 dakika | 1 saat |
| 5 | 3. uygulama durağına kadar okumayı sürdürün; etkileşimli labın D-F bölümlerini yapın | 45 dakika | 45 dakika |
| 6 | 3. uygulama durağı: Kısım 1, Durak 3 ya da 6-9. bölümler | 35 dakika | 1 saat |
| 7 | Haftanın makalesini, sanal kliniğin aşamasını ve kendi verinizle bölümünü okuyun | 30 dakika | 30 dakika |
| 8 | Etkileşimli labdaki öz değerlendirmeyi yapın (sekme: Kendini sına), yansıtmayı yazın ve öğrenme günlüğünü dışa aktarın | 20 dakika | 20 dakika |
| | **Haftalık proje dışında toplam** | **4 saat 50 dakika** | **6 saat 30 dakika** |
| 9 | Haftalık projeyi iki yoldan biriyle tamamlayın | 3 saat | 3 saat |

## Oturumun eğitim akışı

Haftanın dört saatlik oturumu aşağıdaki plana göre işlenir. Plan, malzemelerin canlı bir oturumda nasıl bir araya geldiğini göstermek için paylaşılmaktadır.

| Süre | Etkinlik |
|---|---|
| 0:00-0:20 | Haftanın vakası VC-0317 ve eğitimin rotası: ana rota olarak ders sayfası, uygulamanın iki yolu ve sanal klinik. Her katılımcı defteri Google Colab'da ya da Jupyter'de açar ve 0. bölümü çalıştırır. |
| 0:20-1:00 | Ana rota: hasta tabloları. İki grupta 1. uygulama durağı: prompt yolu ve Python yolu; Python grubu Python adımı 1 ile başlar. |
| 1:00-1:50 | Ana rota: veri olarak EKG, etkileşimli labın A ve B bölümleriyle tek kalp vektöründen on iki derivasyon, C bölümüyle aralıklar ve QT düzeltmesi. 2. uygulama durağı. |
| 1:50-2:05 | Ara. |
| 2:05-3:05 | Ana rota: her atımı bulmak, D bölümüyle kalp hızı değişkenliği, gerçek PhysioNet kayıtları ve E ile F bölümleriyle kod güvenlik kontrol listesi. 3. uygulama durağı. |
| 3:05-3:40 | Haftanın makalesi, sanal kliniğin ilk aşaması ve kendi verinizle bölümü. |
| 3:40-4:00 | Haftalık proje ve sorular. |

## Haftalık proje

**Ne yapılacak?** Önce Jupyter defterinin 5. bölümündeki `measure_ecg` fonksiyonunu alın ve dilerseniz bir YZ asistanının yardımıyla, D1 ve aVF derivasyonlarının net QRS gerilimlerinden frontal QRS eksenini de döndürecek biçimde genişletin. İkinci olarak fonksiyonu, en az ikisinde atriyal fibrilasyon ya da dal bloğu bulunan, seçtiğiniz on sanal klinik hastasında çalıştırın ve her değeri bir tabloda gerçek değerle karşılaştırın. Üçüncü olarak fonksiyonu 8. bölümdeki PTB kaydında çalıştırın ve MIT-BIH 100 numaralı kaydın kalp hızını bulunan atımlardan hesaplayıp raporlayın. Son olarak on hastanızın her biri için QTc'nin Bazett ve Fridericia formüllerine göre uzamış olup olmadığına karar verin ve iki formülün farklı sonuç verdiği hastaları tartışın.

**Nereye bakılacak?** Ders: "Bir vektör olarak kalp: On iki derivasyon, tek kaynak", "Aralıklar: PR, QRS ve QT", "QT'nin kalp hızına göre düzeltilmesi" ve "YZ ile eşli kodlama, bölüm 1: Kod güvenlik kontrol listesi" bölümleri. Etkileşimli lab: B, C, E ve F bölümleri. Jupyter defteri: 4, 5, 8 ve 9. bölümler ile E, F ve J alıştırmaları.

**Prompt yolu.** Proje, her adım için bir prompt olmak üzere [prompt kütüphanesindeki](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/tr/hafta-01/PROMPTLAR.md#haftal%C4%B1k-projenin-prompt-yolu) dört promptla da kurulabilir. Bir promptun testi sağlanmadan sonraki prompt gönderilmez; dört promptun tamamı YZ kullanım günlüğüne yazılır.

**Örnek.** D1'de 0,9 mV, aVF'de −0,3 mV net QRS gerilimi olan bir hastada $H_y = -0{,}3/0{,}866 = -0{,}346$ ve frontal eksen $\operatorname{atan2}(-0{,}346;\ 0{,}9) = -21{,}0°$ olur; bu normal sınırlar içindedir. Başka bir hastada −45°'lik bir eksen sol eksen sapmasını gösterirdi.

**Ne teslim edilecek?** [Rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılmış, bir-iki sayfalık bir rapor: on hastanızın tablosu, iki gerçek kaydın sonuçları ve iki QT düzeltmesinin tartışması. Rapora YZ kullanım günlüğünü (araç, prompt, neyin denetlendiği, neyin değiştirildiği) ve 1. hafta alıştırmaları tamamlanmış Jupyter defterini ekleyin.

**Teslim.** Haftalık proje, 2. haftanın oturumundan önce utkukose@sdu.edu.tr ya da utkukose@gmail.com adresine e-postayla gönderilir. E-postaya "Ne teslim edilecek?" başlığında sayılan öğeler ve etkileşimli labdan dışa aktarılan öğrenme günlüğü eklenir. Haftalık projeler değerlendirmenin yüzde 40'ını oluşturur ve sertifika için her birinden en az yüzde 70 almak gerekir (izlenceye bakın).

## Kendi verinizle

Ders sayfası, haftanın yöntemlerini kendi verinize uygulamayı anlatan bir bölümle biter: hangi sorunun hangi yönteme uyduğu, önce neyin denetleneceği, etik kurul onayı, Kişisel Verilerin Korunması Kanunu (KVKK) ve hesabın nerede yapılacağı. [Ders sayfasında okuyun](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#with-your-own-data).

## İsteğe bağlı araştırma ödevi

PubMed'de, 12 derivasyonlu EKG için geliştirilmiş bir yapay zekâ modelini, modelin geliştirildiği hastane dışındaki bir hastanenin verileriyle sınayan ve 2023 ya da sonrasında yayımlanmış bir çalışma bulun. Çalışmayı yarım sayfada özetleyin: hasta grubu, referans standart, başarım ölçütü ve bir sınırlılık. [Haftanın makalesindeki](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-paper-of-the-week) üç soru özete yön verebilir. Ödeve not verilmez; ödev, 2. haftadaki doğrulama tartışmasına hazırlıktır.

## Bu haftadan sonra sanal klinik

Sanal klinik 1. haftada, 500 sentetik hastadan oluşan bir kayıt ve her kaydı otomatik olarak ölçen bir EKG laboratuvarıyla açılır. Bu aşamanın sonuçları, otomatik ölçümün hatalarıyla birlikte, ders sayfasının [Sanal klinik, 1. aşama](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-01/ders.html#the-virtual-clinic-stage-1-the-clinic-opens) bölümündedir.

## Gelecek hafta

**Hafta 2: Makine öğrenmesi temelleri.** Sanal klinik risk polikliniğini açar: UCI Heart Disease verisinde ve hasta kaydında koroner arter hastalığını öngören modeller, çapraz doğrulama ve alıcı işletim karakteristiği (ROC) analiziyle. [Eğitimin planına](../../README.tr.md#on-bir-hafta) bakın.

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
