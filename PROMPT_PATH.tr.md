# Prompt yolu

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [Python yolu](PYTHON_PATH.tr.md) · [Kendi verileriniz](OWN_DATA.tr.md) · [English](PROMPT_PATH.md)

Eğitimin tek bir ana rotası vardır: Her haftanın ders sayfası. Haftanın Jupyter defterinde ise iki uygulama yolu bulunur. Kod yazmayan, belki de hiç yapay zekâ (YZ) asistanı kullanmamış katılımcılar için hazırlanan yolda kodu, hazır bir prompt (istem), yani yazılı bir talimat ile bir YZ asistanı yazar; katılımcı kodu çalıştırır ve sonucu denetler. Her defterin 1. kısmını oluşturan bu yola **prompt yolu** denir. Defterin 2. kısmı olan **Python yolunda** ise aynı sonuçlara kod yazılarak ulaşılır ([PYTHON_PATH.tr.md](PYTHON_PATH.tr.md)). Yol, her uygulama durağında değiştirilebilir.

## Bir uygulama durağında ne olur?

Ders sayfasında her hafta iki ya da üç uygulama durağı bulunur. Durağın **Prompt yolu** düğmesi, defterin 1. kısmını aynı durağın başında, Google Colab'da ya da kendi bilgisayarınızdaki Jupyter'de açar. Bir durakta iki ile dört adım bulunur ve her adım aynı biçimde ilerler.

| Adım | Ne yapılır? |
|---|---|
| 1. Okuyun | Defterde adımın amacını okuyun. |
| 2. Veriyi hazırlayın | Promptun altındaki veri hücresini çalıştırın. Hücre, promptun tarif ettiği "veri" tablosunu hazırlar ve gösterir. |
| 3. Kopyalayın ve gönderin | Promptu kopyalayın ve bir YZ asistanına gönderin: Google Colab'daki Gemini ya da başka bir tarayıcı sekmesindeki ChatGPT, Claude, Copilot veya Gemini. |
| 4. Çalıştırın | Asistanın kodunu veri hücresinin altındaki hücreye yapıştırın ve çalıştırın. |
| 5. Denetleyin | Kontrol hücresini çalıştırın. Hücre *doğru* ya da *henüz değil* yazar ve "cevap" sonucunun değerini gösterir. |
| 6. Onarın | Kontrol *henüz değil* yazarsa onarım promptunu kodla birlikte gönderin. Sonuç yine yanlışsa doğru sonucu veren *Hazır kod* hücresini çalıştırın. |
| 7. Açıklatın ve kaydedin | Asistandan kodu sade bir dille açıklamasını isteyin; aracı, promptu ve neyin denetlendiğini YZ kullanım günlüğüne yazın. |

Her durak, o durağın verilerini yükleyen bir hazırlık hücresiyle başlar; böylece bir durağa başka bir gün de başlanabilir. Her adımın da, promptun tarif ettiği "veri" tablosunu hazırlayıp gösteren kendi veri hücresi vardır. Her adımın *Hazır kod* hücresi her zaman doğru sonucu verir; böylece hiçbir katılımcı bir adımda takılıp kalmaz ve sonraki adıma her zaman geçilebilir.

## Hangi asistan?

Python kodu yazabilen her asistan kullanılabilir; eğitimin promptları hepsiyle çalışır.

| Asistan | Nerede çalışır? | Bilinmesi gerekenler |
|---|---|---|
| [Colab'da Gemini](https://developers.googleblog.com/en/new-ai-first-google-colab-now-available-to-everyone/) | Google Colab | Colab'ın içinde bulunur ve pencerenin üstündeki düğmesiyle açılır. Bir açıklamadan yola çıkarak kod yazar ve hataları açıklar. Özellikler hesaba ve bölgeye göre farklılık gösterebilir. |
| ChatGPT, Claude, Copilot ya da Gemini gibi bir sohbet asistanı | Web tarayıcısının ikinci bir sekmesi | Prompt sohbete yapıştırılır, kod da deftere geri kopyalanır. |
| [Anaconda Assistant](https://docs.anaconda.com/anaconda-notebooks/local-assistant) | Anaconda Toolbox aracılığıyla Anaconda'daki JupyterLab (`conda install anaconda-toolbox`) | Bir Anaconda hesabı gerektirir. Ücretsiz hesapta istek sayısı sınırlıdır. |
| [Jupyter AI](https://jupyter-ai.readthedocs.io/en/latest/) | Anaconda'daki JupyterLab | Sohbet paneli olan açık kaynaklı bir eklentidir. Bir model sağlayıcısının uygulama programlama arayüzü (API) anahtarını ya da yerel bir modeli gerektirir. Sağlayıcılar kullanım için ücret alabilir. |

Eğitim bu araçların hiçbirine bağlı değildir. Asistanlar sık değiştiği için her aracın kurulumu kendi belgelerini izler.

## Prompt kartı

Eğitimdeki her prompt aynı yedi alandan oluşur; bu alanları okumak, bir asistana iyi bir istek yazmayı öğretir. Promptlar klinik bir dille yazılır. Bir promptta koddan yalnızca iki ad geçer: Her adımın veri hücresinin hazırlayıp gösterdiği "veri" tablosu ve sonucun kontrol için saklandığı "cevap" adı. Kodun hiçbir paketinin, fonksiyonunun ya da ayarının adı geçmez.

| Alan | Ne belirtilir? |
|---|---|
| Rol | Asistanın kime yardım ettiği ve kodunun nerede çalışacağı: Kod yazmayan bir kardiyolog ve bir Jupyter defteri |
| Bağlam | Adımın klinik sorusu |
| Veri | "veri" tablosu: Satırları, sütunları ve birimleri; sinyallerde saniyedeki örnek sayısı |
| Görev | Formülü ya da kuralıyla birlikte tek ve açık bir görev |
| Kısıtlar | Kodun yapmaması gerekenler: Başka veri kullanmak, dosya okumak, bir şey indirmek ya da program kurmak |
| Çıktı | Neyin yazdırılacağı ya da çizileceği; sonucun "cevap" adıyla saklanması |
| Test | Sonucun denetlenebilmesi için cevabı bilinen bir durum ya da makul bir aralık |

Bir asistan, hata vermeden çalışan ama yanlış bir sayı üreten kod yazabilir. Bu yüzden prompt yolunun en önemli parçası her adımın kontrolüdür.

## Promptlar nerede?

| Hafta | Prompt kütüphanesi | Prompt yolu | Etkileşimli lab |
|---|---|---|---|
| 1 | [PROMPTLAR.md](tr/hafta-01/PROMPTLAR.md) | 3 durak, 10 adım | F bölümü, prompt atölyesi |
| 2 | [PROMPTLAR.md](tr/hafta-02/PROMPTLAR.md) | 3 durak, 9 adım | F bölümü, prompt atölyesi |
| 3 | [PROMPTLAR.md](tr/hafta-03/PROMPTLAR.md) | 3 durak, 10 adım | F bölümü, prompt atölyesi |
| 4 | [PROMPTLAR.md](tr/hafta-04/PROMPTLAR.md) | 3 durak, 9 adım | F bölümü, prompt atölyesi |
| 5 | [PROMPTLAR.md](tr/hafta-05/PROMPTLAR.md) | 3 durak, 11 adım | F bölümü, prompt atölyesi |
| 6 | [PROMPTLAR.md](tr/hafta-06/PROMPTLAR.md) | 3 durak, 10 adım | F bölümü, prompt atölyesi |
| 7 | [PROMPTLAR.md](tr/hafta-07/PROMPTLAR.md) | 3 durak, 10 adım | F bölümü, prompt atölyesi |
| 8 | [PROMPTLAR.md](tr/hafta-08/PROMPTLAR.md) | 3 durak, 11 adım | F bölümü, prompt atölyesi |
| 9 | [PROMPTLAR.md](tr/hafta-09/PROMPTLAR.md) | 3 durak, 12 adım | F bölümü, prompt atölyesi |
| 10 | [PROMPTLAR.md](tr/hafta-10/PROMPTLAR.md) | 3 durak, 9 adım | F bölümü, prompt atölyesi |
| 11 | [PROMPTLAR.md](tr/hafta-11/PROMPTLAR.md) | 3 durak, 9 adım | F bölümü, prompt atölyesi |

Haftanın prompt kütüphanesi, 1. kısmın bütün promptlarını GitHub'da birer kopyalama düğmesiyle, kodu onarmak için promptları ve haftalık projenin prompt yolunu içerir. Etkileşimli labın F bölümünde prompt kartı, bir kalite göstergesi ve bir mahremiyet denetimiyle çalışılır.

## Mahremiyet

Hiçbir prompta hasta verisi girmez. Buna adlar, doğum tarihleri, T.C. kimlik numaraları, hastane ve protokol numaraları, yatış tarihleri, hasta dosyalarından alınan serbest metinler ve kimlik bilgisi taşıyan görüntüler dâhildir. Eğitimin promptları verinin yapısını, yani sütun adlarını, birimleri ve örnekleme frekansını tarif eder; hiçbir zaman gerçek bir hastayı tarif etmez. Gerçek hasta verileri kurumun bir bilgisayarında, kurumun kurallarına ve Kişisel Verilerin Korunması Kanunu'na (KVKK) uygun olarak kalır [1]. [OWN_DATA.tr.md](OWN_DATA.tr.md), prompt yolunun kişinin kendi verileriyle nasıl kullanılacağını anlatır: Prompt sütunları tarif eder, veriler bilgisayardan hiç çıkmaz.

## YZ kullanım günlüğü ve değerlendirme

Prompt yolundan gelen kod, elle yazılmış kodla aynı biçimde değerlendirilir. Haftalık proje, [izlencede](SYLLABUS.tr.md#değerlendirme-ve-sertifika) anlatıldığı gibi sonuçları, yöntemleri ve bunların açıklaması, tartışması ve kayıtları üzerinden puanlanır. Her haftalık projeye, bir asistanın her kullanımı için bir satır içeren bir YZ kullanım günlüğü eklenir. Her satırda araç, prompt, neyin denetlendiği ve neyin değiştirildiği yazılır.

## Kaynaklar

1. Kişisel Verilerin Korunması Kanunu, Kanun No. 6698. (2016). *Resmî Gazete, 29677 (7 Nisan 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
