# Python yolu

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](PYTHON_PATH.md)

Python yolu, her Jupyter Notebook'un kodu kendisi yazmayı öğrenmek isteyen katılımcılar için hazırlanmış 2. kısmıdır. Eğitim programlama deneyimi gerektirmez. 2. kısım, haftanın gerektirdiği dil bilgisini öğreten bir Python adımıyla başlar; *Python notu* hücreleri de her yeni yapıyı ilk geçtiği yerde açıklar. Numaralı bölümler, ders sayfasındaki uygulama duraklarının sonuçlarına cevabı hemen kontrol edilen alıştırmalarla ulaşır. Aşağıdaki tablo haftaların Python adımlarını göstermektedir; sonraki haftaların adımlarının bağlantıları her hafta yayımlandığında eklenir.

1. haftadan önce [başlangıç Jupyter Notebook'u](tr/baslangic/NB00_baslangic.ipynb) bilgisayarı denetler; hücreleri, değerleri, yazdırmayı ve ilk grafiği tanıtır.

Kod yazmak istemeyen katılımcılar için aynı Jupyter Notebook'un 1. kısmında kodu, hazır bir prompt (istem) ile bir yapay zekâ (YZ) asistanı yazar. Bu yola [prompt yolu](PROMPT_PATH.tr.md) denir. İki yol da aynı sonuçlara varır ve yol her uygulama durağında değiştirilebilir.

| Hafta | Python adımı | Konular | Jupyter Notebook |
|---|---|---|---|
| 1 | Python adımı 1: Tıbbi örneklerle değişkenler, listeler ve döngüler; sözlükler, koşullar ve fonksiyonlar | Değişkenler ve türler, klinik değerlerle aritmetik işlemler, listeler ve indeksleme, sözlükler, if ve else, for döngüleri, argüman alan ve değer döndüren fonksiyonlar, NumPy dizileri, pandas DataFrame'leri ve Matplotlib grafikleri | [NB01_python_ve_ekg_temelleri.ipynb](tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb) |
| 2 | Python adımı 2: Veriyi modele hazırlamak | Sütun ve satır seçme, eksik değerler, kukla değişkenler, veriyi hastaya göre bölme, scikit-learn'ün fit ve predict kalıbı, işlem hatları | [NB02_makine_ogrenmesi_temelleri.ipynb](tr/hafta-02/NB02_makine_ogrenmesi_temelleri.ipynb) |
| 3 | Python adımı 3: Görüntüleri dizi olarak işlemek | İki ve üç boyutlu diziler, dilimleme, normalizasyon, görüntü yükleme, bir sinir ağının eğitim döngüsü | [NB03_derin_ogrenme_ve_evrisimli_aglar.ipynb](tr/hafta-03/NB03_derin_ogrenme_ve_evrisimli_aglar.ipynb) |
| 4 | Python adımı 4: Eğitilmiş modelleri yeniden kullanmak | Önceden eğitilmiş ağırlıkları yükleme, katmanları dondurma, dizi olarak maskeler, alan ve hacim ölçen fonksiyonlar | [NB04_transfer_ogrenme.ipynb](tr/hafta-04/NB04_transfer_ogrenme.ipynb) |
| 5 | Python adımı 5: Sinyalleri toplu işlemek | Bir sinyalin pencereleri, çok sayıda kayıttan oluşan diziler, birden fazla sınıfı olan etiketler, büyük bir veri setini adım adım okuma | [NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb](tr/hafta-05/NB05_zaman_serisi_ve_ekg_yapay_zekasi.ipynb) |
| 6 | Python adımı 6: Metinle çalışmak | Karakter dizileri (string) ve metotları, düzenli ifadeler, token'lar, Hugging Face Hub'dan önceden eğitilmiş bir modeli çağırma | [NB06_klinik_metin_madenciligi.ipynb](tr/hafta-06/NB06_klinik_metin_madenciligi.ipynb) |
| 7 | Python adımı 7: Sınıflar ve modüller | Küçük bir sınıfı okuma ve yazma, modüllerden kod içe aktarma, bir modeli parçalardan kurma | [NB07_vision_transformer.ipynb](tr/hafta-07/NB07_vision_transformer.ipynb) |
| 8 | Python adımı 8: Verileri birleştirmek | Tabloları birleştirme, bir hastanın sinyallerini ve görüntülerini hizalama, eksik parçalarla başa çıkma | [NB08_cok_modlu_yapay_zeka_ve_veri_fuzyonu.ipynb](tr/hafta-08/NB08_cok_modlu_yapay_zeka_ve_veri_fuzyonu.ipynb) |
| 9 | Python adımı 9: Bir modeli kodla açıklamak | itertools ile değişken grupları ve sıraları, anahtarları demet olan sözlükler, Shapley formülünün faktöriyelleri, başka fonksiyonlara verilen fonksiyonlar, katkı grafikleri | [NB09_guvenilirlik_ve_aciklanabilir_yapay_zeka.ipynb](tr/hafta-09/NB09_guvenilirlik_ve_aciklanabilir_yapay_zeka.ipynb) |
| 10 | Python adımı 10: Jupyter Notebook'tan uygulamaya | Betikler, Streamlit ile küçük bir web arayüzü, bir modeli kaydetme ve yükleme | [NB10_klinik_karar_destegi.ipynb](tr/hafta-10/NB10_klinik_karar_destegi.ipynb) |
| 11 | Python adımı 11: Katılımcının kendi projesi | Bir proje klasörünü düzenleme, kodu belgeleme, sonuçları yeniden üretilebilir kılma | [NB11_final_projesi_atolyesi.ipynb](tr/hafta-11/NB11_final_projesi_atolyesi.ipynb) |

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
