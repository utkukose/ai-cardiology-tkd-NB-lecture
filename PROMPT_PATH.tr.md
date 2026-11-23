# Promptlarla çalışmak

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [Python temelleri](PYTHON_PATH.tr.md) · [Kendi verileriniz](OWN_DATA.tr.md) · [English](PROMPT_PATH.md)

Eğitimin tek bir ana rotası bulunmaktadır: Her haftanın ders sayfası. Sayfadaki uygulama duraklarında çalışma, haftanın Jupyter Notebook'unda sürdürülür. Burada kodu, hazır bir prompt (istem), yani yazılı bir talimat yardımıyla bir yapay zekâ (YZ) asistanı yazabilir; katılımcının görevi bu kodu çalıştırmak ve sonucu denetlemektir. Bu rehber, kod yazmayan ve belki de daha önce hiç YZ asistanı kullanmamış katılımcılar için hazırlanan bu çalışma biçimini anlatmaktadır. Jupyter Notebook'ta her durak **Python temelleri**, **Prompt ile uygulama** ve **Hazır uygulama** olmak üzere üç bölümden oluşur; promptlar «Prompt ile uygulama» bölümünde yer almaktadır. Aynı durağın Python temelleri bölümünde böyle bir kodun nasıl yazılacağı öğretilir ([PYTHON_PATH.tr.md](PYTHON_PATH.tr.md)); hazır uygulama bölümünde ise durağın eksiksiz programı gösterilir.

## Bir uygulama durağında ne olur?

Ders sayfasında her hafta iki ya da üç uygulama durağı bulunmaktadır. Durağın **2 · Prompt ile uygulama** düğmesi, Jupyter Notebook'u Google Colab'da bu bölümün başından açar. Kendi bilgisayarınızdaki Jupyter'de ise «Durak N · Prompt ile uygulama» başlığını içindekiler panelinde bulabilirsiniz. Bir durakta üç ile beş arasında prompt yer alır ve her promptla aynı biçimde çalışılır.

| Adım | Ne yapılır? |
|---|---|
| 1. Okuyunuz | Jupyter Notebook'ta promptun amacını okuyunuz. |
| 2. Veriyi hazırlayınız | Bölümün başlangıç hücresini bir kez, ardından promptun altındaki veri hücresini çalıştırınız. Veri hücresi, promptun tarif ettiği "veri" tablosunu hazırlayıp göstermektedir. |
| 3. Kopyalayınız ve gönderiniz | Promptu kopyalayınız ve bir YZ asistanına gönderiniz: Google Colab'daki Gemini ya da başka bir tarayıcı sekmesindeki ChatGPT, Claude, Copilot veya Gemini. |
| 4. Çalıştırınız | Asistanın verdiği kodu veri hücresinin altındaki hücreye yapıştırınız ve çalıştırınız. |
| 5. Denetleyiniz | Kontrol hücresini çalıştırınız. Hücre sonucu *doğru* ya da *henüz değil* biçiminde bildirmekte ve "cevap" sonucunun değerini göstermektedir. |
| 6. Onarınız | Kontrol hücresi *henüz değil* sonucunu verirse onarım promptunu kodla birlikte gönderiniz. Sonuç yine yanlışsa, doğru sonucu veren *Hazır kod* hücresini çalıştırınız. |
| 7. Açıklatınız ve kaydediniz | Asistandan kodu sade bir dille açıklamasını isteyiniz; kullandığınız aracı, promptu ve neyin denetlendiğini YZ kullanım günlüğüne yazınız. |

Bölüm, kullandığı kurulumu ve veri çağrılarını yineleyen bir başlangıç hücresiyle açılır; bu sayede bölüme başka bir gün de başlanabilmektedir. Her promptun ayrıca, promptun tarif ettiği "veri" tablosunu hazırlayıp gösteren kendi veri hücresi bulunur. Her promptun *Hazır kod* hücresi her zaman doğru sonucu vermektedir; böylece hiçbir katılımcı takılıp kalmadan sonraki prompta geçebilir. Ardından gelen «Hazır uygulama» bölümünde ise durağın eksiksiz programı yer alır.

## Hangi asistan?

Python kodu yazabilen her asistan kullanılabilir; eğitimin promptları bu asistanların hepsiyle çalışacak biçimde hazırlanmıştır.

| Asistan | Nerede çalışır? | Bilinmesi gerekenler |
|---|---|---|
| [Colab'da Gemini](https://developers.googleblog.com/en/new-ai-first-google-colab-now-available-to-everyone/) | Google Colab | Colab'ın içinde bulunur ve pencerenin üstündeki düğmesiyle açılır. Bir açıklamadan yola çıkarak kod yazabilir ve hataları açıklayabilir. Özellikler hesaba ve bölgeye göre farklılık gösterebilir. |
| ChatGPT, Claude, Copilot ya da Gemini gibi bir sohbet asistanı | Web tarayıcısının ikinci bir sekmesi | Prompt sohbete yapıştırılır; asistanın verdiği kod da Jupyter Notebook'a geri kopyalanır. |
| [Anaconda Assistant](https://docs.anaconda.com/anaconda-notebooks/local-assistant) | Anaconda Toolbox aracılığıyla Anaconda'daki JupyterLab (`conda install anaconda-toolbox`) | Bir Anaconda hesabı gerektirmektedir. Ücretsiz hesapta istek sayısı sınırlıdır. |
| [Jupyter AI](https://jupyter-ai.readthedocs.io/en/latest/) | Anaconda'daki JupyterLab | Sohbet paneli olan açık kaynaklı bir eklentidir. Bir model sağlayıcısının uygulama programlama arayüzü (API) anahtarını ya da yerel bir modeli gerektirir. Sağlayıcılar kullanım için ücret alabilir. |

Eğitim bu araçların hiçbirine bağlı değildir. Asistanlar sık değiştiği için her aracın kurulumunda o aracın kendi belgeleri izlenmelidir.

## Prompt kartı

Eğitimdeki her prompt aynı yedi alandan oluşmaktadır; bu alanları incelemek, bir asistana iyi bir istek yazmayı da öğretir. Promptlar klinik bir dille yazılmıştır. Bir promptta koddan yalnızca iki ad geçer: Her promptun veri hücresinde hazırlanıp gösterilen "veri" tablosu ve sonucun kontrol için saklandığı "cevap" adı. Promptlarda kodun hiçbir paketinin, fonksiyonunun ya da ayarının adı geçmemektedir.

| Alan | Ne belirtilir? |
|---|---|
| Rol | Asistanın kime yardım ettiği ve kodunun nerede çalışacağı: Kod yazmayan bir kardiyolog ve bir Jupyter Notebook |
| Bağlam | Promptun klinik sorusu |
| Veri | "veri" tablosu: Satırları, sütunları ve birimleri; sinyallerde saniyedeki örnek sayısı |
| Görev | Formülü ya da kuralıyla birlikte tek ve açık bir görev |
| Kısıtlar | Kodun yapmaması gerekenler: Başka veri kullanmak, dosya okumak, bir şey indirmek ya da program kurmak |
| Çıktı | Neyin yazdırılacağı ya da çizileceği; sonucun "cevap" adıyla saklanması |
| Test | Sonucun denetlenebilmesi için cevabı bilinen bir durum ya da makul bir aralık |

Bir asistan, hata vermeden çalışan ama yanlış bir sayı üreten kod yazabilir. Bu nedenle promptlarla çalışmanın en önemli parçası, her promptun sonucunun denetlenmesidir.

## Promptlar nerede?

| Hafta | Prompt kütüphanesi | Jupyter Notebook'taki promptlar | Etkileşimli lab |
|---|---|---|---|
| 1 | [PROMPTLAR.md](tr/hafta-01/PROMPTLAR.md) | 3 durakta 10 prompt | F bölümü, prompt atölyesi |
| 2 | [PROMPTLAR.md](tr/hafta-02/PROMPTLAR.md) | 3 durakta 9 prompt | F bölümü, prompt atölyesi |
| 3 | [PROMPTLAR.md](tr/hafta-03/PROMPTLAR.md) | 3 durakta 10 prompt | F bölümü, prompt atölyesi |
| 4 | [PROMPTLAR.md](tr/hafta-04/PROMPTLAR.md) | 3 durakta 9 prompt | F bölümü, prompt atölyesi |
| 5 | [PROMPTLAR.md](tr/hafta-05/PROMPTLAR.md) | 3 durakta 11 prompt | F bölümü, prompt atölyesi |
| 6 | [PROMPTLAR.md](tr/hafta-06/PROMPTLAR.md) | 3 durakta 11 prompt | F bölümü, prompt atölyesi |
| 7 | [PROMPTLAR.md](tr/hafta-07/PROMPTLAR.md) | 3 durakta 11 prompt | F bölümü, prompt atölyesi |
| 8 | [PROMPTLAR.md](tr/hafta-08/PROMPTLAR.md) | 3 durakta 11 prompt | F bölümü, prompt atölyesi |
| 9 | [PROMPTLAR.md](tr/hafta-09/PROMPTLAR.md) | 3 durakta 13 prompt | F bölümü, prompt atölyesi |
| 10 | [PROMPTLAR.md](tr/hafta-10/PROMPTLAR.md) | 3 durakta 10 prompt | F bölümü, prompt atölyesi |
| 11 | [PROMPTLAR.md](tr/hafta-11/PROMPTLAR.md) | 3 durakta 9 prompt | F bölümü, prompt atölyesi |

Haftanın prompt kütüphanesinde uygulama duraklarının bütün promptları, GitHub'da her birinin yanında bir kopyalama düğmesiyle birlikte yer almaktadır. Kütüphanede ayrıca kodu onarmaya yönelik promptlar ve haftalık projenin promptları bulunur. Etkileşimli labın F bölümünde ise prompt kartı, bir kalite göstergesi ve bir mahremiyet denetimiyle birlikte çalışılır.

## Mahremiyet

Hiçbir prompta hasta verisi konmamalıdır. Buna adlar, doğum tarihleri, T.C. kimlik numaraları, hastane ve protokol numaraları, yatış tarihleri, hasta dosyalarından alınan serbest metinler ve kimlik bilgisi taşıyan görüntüler dâhildir. Eğitimin promptlarında verinin yapısı, yani sütun adları, birimler ve örnekleme frekansı tarif edilmektedir; promptlar hiçbir zaman gerçek bir hastayı tarif etmez. Gerçek hasta verileri, kurumun bir bilgisayarında, kurumun kurallarına ve Kişisel Verilerin Korunması Kanunu'na (KVKK) uygun olarak işlenmelidir [1]. Promptların kişinin kendi verileriyle nasıl kullanılabileceği [OWN_DATA.tr.md](OWN_DATA.tr.md) belgesinde anlatılmaktadır: Prompt yalnızca sütunları tarif eder, veriler ise bilgisayardan hiç çıkmaz.

## YZ kullanım günlüğü ve değerlendirme

Promptlarla yazılan kod, elle yazılmış kodla aynı biçimde değerlendirilmektedir. Haftalık proje, [izlencede](SYLLABUS.tr.md#değerlendirme-ve-sertifika) anlatıldığı gibi sonuçları, yöntemleri ve bunların açıklaması, tartışması ve kayıtları üzerinden puanlanır. Her haftalık projeye, bir asistanın her kullanımı için bir satır içeren bir YZ kullanım günlüğü eklenir. Her satırda araç, prompt, neyin denetlendiği ve neyin değiştirildiği yazılır.

## Kaynaklar

1. Kişisel Verilerin Korunması Kanunu, Kanun No. 6698. (2016). *Resmî Gazete, 29677 (7 Nisan 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
