# Final projesi

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · Hafta 11

[Eğitimin ana sayfası](../../README.tr.md) · [İzlence](../../SYLLABUS.tr.md) · [English](../../en/final-project/README.md)

## Amaç

Final projesi, eğitimin yöntemlerini katılımcının kendi klinik çalışmasından gelen bir soruya uygular. Katılımcı uçtan uca bir işlem hattı kurar: Bu hat bir klinik sorudan, verilerden, bir model ya da analizden, modelin kararlarının açıklamasından ve klinik değerlendirme için bir plandan oluşur. Proje 11. haftanın oturumunda 5-7 dakikada sunulur ve değerlendirmenin yüzde 40'ını oluşturur. Proje tek başına ya da iki üç katılımcılık bir grupla yapılabilir.

## Seçenekler

Yedi seçenek vardır. A-F seçeneklerinde sentetik ya da açık veriler, G seçeneğinde ise katılımcının kurumuna ait veriler kullanılır. Son sütun, başlangıç kodunu veren Jupyter defterlerinin haftalarını gösterir.

| Seçenek | Soru | Veriler | Başlangıç noktası |
|---|---|---|---|
| A. EKG | 12 derivasyonlu EKG'lerde bir ritim ya da iskemi sorusu | Sanal klinik, PTB-XL ya da PhysioNet/Computing in Cardiology Challenge 2020 | 1. ve 5. haftalar |
| B. Risk | Klinik değişkenlerle kurulan ve öngörülerini açıklayan bir risk modeli | Sanal klinik ya da UCI Heart Disease | 2. ve 9. haftalar |
| C. Görüntüleme | Ekokardiyogramların ya da kardiyak manyetik rezonans görüntülerinin sınıflandırılması ya da segmentasyonu | Sanal klinik ya da açık bir görüntüleme veri seti | 3., 4. ve 7. haftalar |
| D. Metin | Klinik raporlardan bilgi çıkarımı | Sanal kliniğin sentetik raporları | 6. hafta |
| E. Füzyon | Aynı hastaların farklı türdeki verilerini birleştiren bir model | Sanal klinik | 8. hafta |
| F. Karar desteği | Açıklamalar ve bir kullanıcı testi içeren bir klinik karar destek sistemi prototipi | Yukarıdakilerden herhangi biri | 9. ve 10. haftalar |
| G. Kendi sorusu | Katılımcının kliniğinden bir soru | Kurumun izniyle ve gerektiğinde etik kurul onayıyla kurum verileri | Herhangi bir hafta |

Kurum verileri yalnızca katılımcının kendi bilgisayarında, Kişisel Verilerin Korunması Kanunu'na (KVKK) uygun olarak işlenir. Bu veriler hiçbir zaman bulut tabanlı bir deftere ya da bir yapay zekâ (YZ) sohbetine aktarılmaz; raporda yalnızca toplu sonuçlar gösterilir.

## Ne teslim edilecek?

Teslim dört öğeden oluşur. Rapor dört ile altı sayfa arasındadır ve [rapor şablonuyla](../sablonlar/Rapor_Sablonu.docx) yazılır. Raporda klinik soru, veriler ve kaynakları, yöntemler, belirsizlik ölçüsüyle birlikte sonuçlar, modelin açıklaması, sınırlılıklar ve klinik değerlendirme için bir plan yer alır. Rapor, "Klinik pratiğimde yapay zekâyı nasıl kullanacağım?" başlıklı yarım sayfalık kişisel bir eylem planıyla biter. Jupyter defteri ya da betikler, rapordaki her sonucu yeniden üretir. YZ kullanım günlüğü, bir YZ asistanının her kullanımını kaydeder. Sunumun slaytları teslimi tamamlar.

## Önerilen ara aşamalar

| Hafta | Ara aşama |
|---|---|
| 6 | Seçeneğin belirlenmesi ve e-postayla gönderilen bir paragraflık öneri |
| 9 | Verilerin hazırlanması ve ilk sonuç |
| 10 | Modelin açıklaması ve sunumun taslağı |
| 11 | Oturumda sunum; rapor ve kod bir hafta içinde gönderilir |

## Değerlendirme ölçütleri

Jüri projeyi aşağıdaki ölçütlerle 100 puan üzerinden değerlendirir. Katılımcılar da sunumları değerlendirir ve jüri bu değerlendirmeyi dikkate alır.

| Ölçüt | Puan |
|---|---|
| Klinik soru: Açık, önemli ve verilerle cevaplanabilir | 15 |
| Veriler: Kaynak, nitelik, hazırlık ve koruma | 15 |
| Yöntemler: Eğitimin yöntemlerinin doğru kullanımı ve sağlam bir doğrulama | 25 |
| Sonuçlar: Doğru, bir belirsizlik ölçüsüyle verilmiş ve bir referansla karşılaştırılmış | 15 |
| Açıklama ve sınırlılıklar: Modelin neyi kullandığı, nerede yanıldığı ve klinik değerlendirmenin neyi gerektirdiği | 15 |
| Sunum ve yeniden üretilebilirlik: Açık bir sunum, sonuçları yeniden üreten bir defter ve eksiksiz bir YZ kullanım günlüğü | 15 |

## Başlangıç kodu

Her seçenek, seçenekler tablosunda adı geçen haftaların Jupyter defterleri üzerine kurulur. [11. haftanın Jupyter defteri](../hafta-11/NB11_final_projesi_atolyesi.ipynb), B seçeneğine ait bir final projesini Cleveland verisi üzerinde verilerin denetiminden raporun sonuç tablosuna kadar götürür. Defterin son bölümü final projesinin araç takımını, yani `final_project/code/project_tools.py` modülünü yazar. Bu modül 11. haftanın denetimlerini her seçeneğin modeli için yapar: Bir referansa göre kazancın bootstrap aralığı, kalibrasyon, eğitim verilerinde seçilen bir dışlama eşiği ve bütün hastalarda ve gruplarda Wilson aralıkları. Aynı bölümdeki tablo her seçenek için başlanacak defterleri, sonucu, referansı ve modeli adlandırır. [11. haftanın ders sayfası](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/tr/hafta-11/ders.html) aynı projeyi adım adım izler; etkileşimli labında da sorunun formu, klinik değerlendirmenin planlayıcısı ve sunum için süre ölçerli değerlendirme ölçütleri yer alır.

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İlk sürüm: Kasım 2026 · İçerik CC BY 4.0, kod MIT.*
