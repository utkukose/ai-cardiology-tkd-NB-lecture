# Prompt yolu

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [Python yolu](PYTHON_PATH.tr.md) · [English](PROMPT_PATH.md)

Eğitim üç yoldan izlenebilir. Üç yol da aynı sonuçlara götürür ve sonuçlar her yolda aynı biçimde denetlenir. Katılımcı her alıştırmada yol değiştirebilir. Bu rehber, alıştırmaların bir yapay zekâ (YZ) asistanına yazılan prompt (istem) ile çözüldüğü yolu anlatmaktadır.

| Yol | Kimler için? | Bir alıştırma nasıl çözülür? |
|---|---|---|
| Temel yol | Programlamaya yeni başlayan katılımcılar | Python adımı ve alıştırmalar elle yazılır. Örnek çözümler katlanmış hücrelerde durur. |
| Prompt yolu | Görevi sözcüklerle anlatmayı tercih eden katılımcılar | Prompt kartıyla yazılmış bir prompt YZ asistanına gönderilir. Asistanın yazdığı kod çalıştırılır ve denetlenir. |
| İleri yol | Programlama bilen katılımcılar | *İleri yol* etiketli hücreler aynı deftere isteğe bağlı genişletmeler ekler. |

Prompt yolu Python'u atlamaz; öğrenmenin sırasını değiştirir. Katılımcı önce kodun tam olarak ne yapması gerektiğini ve sonucun nasıl denetleneceğini yazar. Ardından asistanın yazdığı kodu okur, çalıştırır ve açıklar. Kodu okumak ve açıklamak her alıştırmanın parçası olduğu için Python da bu yolda adım adım öğrenilmektedir.

## Prompt kartı

Eğitimdeki her prompt aynı yedi alandan oluşur.

| Alan | Ne belirtilir? |
|---|---|
| Rol | Asistanın üstleneceği rol; örneğin Python öğrenen bir kardiyoloğa yardım etmek |
| Bağlam | Kodun nerede çalışacağı ve neyin hazır olduğu: Jupyter defteri, içe aktarılmış paketler ve `vclinic` ders paketi |
| Veri | Değişken adları, birimler ve örnekleme frekansı |
| Görev | Varsa formülüyle birlikte tek ve açık bir görev |
| Kısıtlar | Kullanılacak paketler ve dosya okumak ya da paket kurmak gibi kaçınılacak işler |
| Çıktı | Değişken adı, yuvarlama ve cevabın biçimi. Alıştırmaların promptları kodun `teach.check` satırıyla bitmesini ister. |
| Test | Cevabı elle hesaplanabilen bir durum |

## Prompt döngüsü

Prompt yolundaki her alıştırma altı adımı izler.

| Adım | Ne yapılır? |
|---|---|
| 1. Tarif et | Alıştırmanın prompt kartını kopyalayın ya da kartı yedi alanıyla kendiniz yazın: rol, bağlam, veri, görev, kısıtlar, çıktı ve test. |
| 2. Gönder | Promptu bir YZ asistanına gönderin. |
| 3. Çalıştır | Asistanın kodunu alıştırmanın altındaki boş hücreye yapıştırın ve çalıştırın. |
| 4. Denetle | `teach.check` satırının yazdığı sonuca (*doğru* ya da *henüz değil*) ve promptun Test satırına bakın. Sonuç *henüz değil* ise kodu onarım promptuyla asistana geri gönderin. |
| 5. Açıkla | Asistandan kodu satır satır açıklamasını isteyin, ardından kodu bir kez de kendi sözcüklerinizle açıklayın. |
| 6. Kaydet | Aracı, promptu, neyin denetlendiğini ve neyin değiştirildiğini YZ kullanım günlüğüne yazın. |

Bir asistanın yazdığı kod, ancak sonucu bilinen bir cevapla karşılaştırılarak doğrulandığında ve her satırı açıklanabildiğinde kabul edilir.

## Promptlar nerede?

| Hafta | Prompt kütüphanesi | Prompt yolları | Prompt görevleri | Etkileşimli lab |
|---|---|---|---|---|
| 1 | [PROMPTLAR.md](tr/hafta-01/PROMPTLAR.md) | 13; her alıştırmanın altında bir tane | 9; her numaralı bölümün sonunda bir tane | F bölümü, prompt atölyesi |
| 2 | [PROMPTLAR.md](tr/hafta-02/PROMPTLAR.md) | 13; her alıştırmanın altında bir tane | 9; her numaralı bölümün sonunda bir tane | F bölümü, prompt atölyesi |
| 3-11 | Hazırlanıyor | | | |

Jupyter defterinde *prompt yolu*, bir alıştırmanın hemen altındaki katlanmış hücredir; bu hücrede alıştırmanın prompt kartı kopyalanmaya hazır durur. Her numaralı bölüm bir *prompt göreviyle* biter. Prompt görevinde hazır kod yoktur; sonucun doğru olup olmadığını görevin altındaki beklenen sonuç gösterir. Haftanın prompt kütüphanesi bütün promptları, kodu açıklatmak, onarmak ve sınamak için dört hazır kalıbı ve haftalık projenin prompt yolunu bir araya getirir. Etkileşimli labın F bölümünde prompt kartı, bir kalite göstergesi ve bir mahremiyet denetimi eşliğinde yazılır.

## YZ asistanları

Python kodu yazabilen her asistan kullanılabilir; eğitimin promptları hepsiyle çalışır. Aşağıdaki üç asistan doğrudan eğitimin defter ortamlarında çalışmaktadır.

| Asistan | Nerede çalışır? | Bilinmesi gerekenler |
|---|---|---|
| [Jupyter AI](https://jupyter-ai.readthedocs.io/en/latest/) | Anaconda içindeki JupyterLab | Sohbet paneli ve `%%ai` sihirli komutu sunan açık kaynaklı bir eklentidir. Bir model sağlayıcısının uygulama programlama arayüzü (API) anahtarıyla ya da örneğin Ollama üzerinden çalışan yerel bir modelle kullanılır. Sağlayıcılar kullanım için ücret alabilir. |
| [Anaconda Assistant](https://docs.anaconda.com/anaconda-notebooks/local-assistant) | Anaconda içindeki JupyterLab; Anaconda Toolbox ile gelir (`conda install anaconda-toolbox`) | Bir Anaconda hesabı gerektirir. Ücretsiz hesapta istek sayısı sınırlıdır. |
| [Colab'daki Gemini](https://developers.googleblog.com/en/new-ai-first-google-colab-now-available-to-everyone/) | Eğitimin yedek ortamı olan Google Colab | Colab'a yerleşiktir. Bir tariften kod yazar ve hataları açıklar. Özellikler hesaba ve bölgeye göre değişebilir. |
| Genel bir sohbet asistanı | Web tarayıcısı | Prompt sohbete yapıştırılır, asistanın yazdığı kod deftere kopyalanır. |

Eğitim bu araçların hiçbirine bağlı değildir. Asistanlar sık değiştiği için her aracın kurulumunda kendi belgeleri izlenmelidir.

## Mahremiyet

Hiçbir prompta hasta verisi yazılmaz. Adlar, doğum tarihleri, T.C. kimlik numaraları, hastane ve protokol numaraları, yatış tarihleri, tıbbi kayıtlardan alınmış serbest metinler ve kimlik bilgisi taşıyan görüntüler de buna dâhildir. Eğitimin promptları sütun adları, birimler ve örnekleme frekansı gibi verinin yapısını tarif eder; hiçbir zaman gerçek bir hastayı tarif etmez. Gerçek hasta verileri, kurumun kurallarına ve Kişisel Verilerin Korunması Kanunu'na (KVKK) uygun olarak katılımcının kendi bilgisayarında kalır [1]. Yerel bir model promptun metnini bilgisayarın dışına çıkarmaz; yine de bu kural her araç için geçerlidir. Etkileşimli labın F bölümündeki mahremiyet denetimi, tarih ve uzun numara gibi yaygın tanımlayıcılar için uyarı verir. Denetim yalnızca yaygın örüntüleri yakalayabilir; sorumluluk katılımcıdadır.

## YZ kullanım günlüğü ve değerlendirme

Prompt yolundan gelen kod, elle yazılmış kodla aynı biçimde değerlendirilir. Haftalık proje, [izlencede](SYLLABUS.tr.md) anlatıldığı gibi sonuçlarına, yöntemlerine ve bunların açıklamasına, tartışmasına ve kayıtlarına göre puanlanır; kodun nasıl yazıldığı puanı değiştirmez. Her haftalık projeye, asistanın her kullanımı için bir satır içeren bir YZ kullanım günlüğü eklenir: araç, prompt, neyin denetlendiği ve neyin değiştirildiği. Etkileşimli labın prompt atölyesinde kaydedilen promptlar da haftanın öğrenme günlüğüne eklenir.

## Kaynaklar

1. Kişisel Verilerin Korunması Kanunu, Kanun No. 6698. (2016). *Resmî Gazete, 29677 (7 Nisan 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
