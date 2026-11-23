# Final projesi

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · Hafta 11

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [English](../../en/final-project/README.md)

## Amaç

Final projesinde, eğitimin yöntemleri katılımcının kendi klinik çalışmasından gelen bir soruya uygulanmaktadır. Katılımcı uçtan uca bir işlem hattı kurar: Bu hat bir klinik sorudan, verilerden, bir model ya da analizden, modelin kararlarının açıklamasından ve klinik değerlendirme için bir plandan oluşur. Proje, 11. haftanın oturumunda 5-7 dakikada sunulur ve değerlendirmenin yüzde 40'ını oluşturur. Proje tek başına ya da iki üç katılımcılık bir grupla yapılabilir.

## Seçenekler

Final projesi için yedi seçenek bulunmaktadır. A-F seçeneklerinde sentetik ya da açık veriler, G seçeneğinde ise katılımcının kurumuna ait veriler kullanılır. Tablonun son sütununda, başlangıç kodunu veren Jupyter Notebook'ların haftaları gösterilmiştir.

| Seçenek | Soru | Veriler | Başlangıç noktası |
|---|---|---|---|
| A. EKG | 12 derivasyonlu EKG'lerde bir ritim ya da iskemi sorusu | Sanal klinik, PTB-XL ya da PhysioNet/Computing in Cardiology Challenge 2020 | 1. ve 5. haftalar |
| B. Risk | Klinik değişkenlerle kurulan ve öngörülerini açıklayan bir risk modeli | Sanal klinik ya da UCI Heart Disease | 2. ve 9. haftalar |
| C. Görüntüleme | Ekokardiyogramların ya da kardiyak manyetik rezonans görüntülerinin sınıflandırılması ya da segmentasyonu | Sanal klinik ya da açık bir görüntüleme veri seti | 3., 4. ve 7. haftalar |
| D. Metin | Klinik raporlardan bilgi çıkarımı | Sanal kliniğin sentetik raporları | 6. hafta |
| E. Füzyon | Aynı hastaların farklı türdeki verilerini birleştiren bir model | Sanal klinik | 8. hafta |
| F. Karar desteği | Açıklamalar ve bir kullanıcı testi içeren bir klinik karar destek sistemi prototipi | Yukarıdakilerden herhangi biri | 9. ve 10. haftalar |
| G. Kendi sorusu | Katılımcının kliniğinden bir soru | Kurumun izniyle ve gerektiğinde etik kurul onayıyla kurum verileri | Herhangi bir hafta |

Kurum verileri yalnızca kurumun bir bilgisayarında, Kişisel Verilerin Korunması Kanunu'na (KVKK) uygun olarak işlenir. Bu veriler hiçbir zaman bulut tabanlı bir Jupyter Notebook'a ya da bir yapay zekâ (YZ) sohbetine aktarılmaz; raporda yalnızca toplu sonuçlar gösterilir.

## Ne teslim edilecek?

Teslim dört öğeden oluşur. Rapor dört ile altı sayfa arasındadır ve [rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılır. Raporda klinik soru, veriler ve kaynakları, yöntemler, belirsizlik ölçüsüyle birlikte sonuçlar, modelin açıklaması, sınırlılıklar ve klinik değerlendirme için bir plan yer alır. Rapor, "Klinik pratiğimde yapay zekâyı nasıl kullanacağım?" başlıklı yarım sayfalık kişisel bir eylem planıyla sona erer. Teslim edilen Jupyter Notebook ya da kod parçaları, rapordaki her sonucu yeniden üretebilmelidir. YZ kullanım günlüğünde bir YZ asistanının her kullanımı kaydedilir. Teslimin son öğesi ise sunumun slaytlarıdır.

## Önerilen ara aşamalar

| Hafta | Ara aşama |
|---|---|
| 6 | Seçeneğin belirlenmesi ve e-postayla gönderilen bir paragraflık öneri |
| 9 | Verilerin hazırlanması ve ilk sonuç |
| 10 | Modelin açıklaması ve sunumun taslağı |
| 11 | Oturumda sunum; rapor ve kod bir hafta içinde gönderilir |

## Değerlendirme ölçütleri

Jüri, projeyi aşağıdaki ölçütlerle 100 puan üzerinden değerlendirmektedir. Katılımcılar da sunumları değerlendirir ve jüri bu değerlendirmeyi de dikkate alır.

| Ölçüt | Puan |
|---|---|
| Klinik soru: Açık, önemli ve verilerle cevaplanabilir | 15 |
| Veriler: Kaynak, nitelik, hazırlık ve koruma | 15 |
| Yöntemler: Eğitimin yöntemlerinin doğru kullanımı ve sağlam bir doğrulama | 25 |
| Sonuçlar: Doğru, bir belirsizlik ölçüsüyle verilmiş ve bir referansla karşılaştırılmış | 15 |
| Açıklama ve sınırlılıklar: Modelin neyi kullandığı, nerede yanıldığı ve klinik değerlendirmenin neyi gerektirdiği | 15 |
| Sunum ve yeniden üretilebilirlik: Açık bir sunum, sonuçları yeniden üreten bir Jupyter Notebook ve eksiksiz bir YZ kullanım günlüğü | 15 |

## Başlangıç kodu

Her seçenek, seçenekler tablosunda adı geçen haftaların Jupyter Notebook'ları üzerine kurulur. [11. haftanın Jupyter Notebook'unda](../hafta-11/NB11_final_projesi_atolyesi.ipynb), B seçeneğine ait bir final projesi Cleveland verisi üzerinde, verilerin denetiminden raporun sonuç tablosuna kadar adım adım yürütülmektedir. Jupyter Notebook'un son bölümü, final projesinin araç takımını, yani `final_project/code/project_tools.py` modülünü yazar. Bu modülle 11. haftanın denetimleri her seçeneğin modeli için yapılabilir: Bir referansa göre kazancın bootstrap aralığı, kalibrasyon, eğitim verilerinde seçilen bir dışlama eşiği ve bütün hastalarda ve gruplarda Wilson aralıkları. Aynı bölümdeki tabloda ise her seçenek için başlanacak Jupyter Notebook'lar, sonuç, referans ve model belirtilmiştir. [11. haftanın ders sayfasında](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/ders.html) aynı proje adım adım izlenir; haftanın etkileşimli labında da sorunun formu, klinik değerlendirmenin planlayıcısı ve sunum için süre ölçerli değerlendirme ölçütleri yer alır.

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İlk sürüm: Kasım 2026 · İçerik CC BY 4.0, kod MIT.*
