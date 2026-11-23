# Kurulum

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](SETUP.md)

Eğitimin her Jupyter Notebook'u, aynı verilerle ve aynı sonuçlarla iki ortamda çalışabilmektedir. Bu ortamlardan tercih ettiğinizi kullanabilirsiniz; ortamı haftadan haftaya değiştirmek de mümkündür. Jupyter Notebook'taki her uygulama durağında kodu, hazır bir prompt (istem) yardımıyla bir yapay zekâ (YZ) asistanı yazabilir. Durağın Python temelleri bölümünde bu kodun nasıl yazılacağı öğretilir; hazır uygulama bölümünde ise eksiksiz program yer alır.

| | Google Colab | Kendi bilgisayarınızda Jupyter (Anaconda) |
|---|---|---|
| Neye ihtiyaç var? | Bir Google hesabı ve bir web tarayıcısı | Windows, macOS ya da Linux yüklü, yaklaşık 5 GB boş alanı olan bir bilgisayar |
| Kurulum | Yok | 1. haftadan önce bir kez, yaklaşık 20 dakika |
| Jupyter Notebook nasıl açılır? | Bir uygulama durağındaki, hafta sayfasındaki ya da eğitim sitesindeki **Colab'da aç** düğmesiyle | **Jupyter için indir** bağlantısıyla ya da ders klasörünün tamamıyla |
| Promptlar için YZ asistanı | Gemini yerleşiktir | Tarayıcıdaki herhangi bir asistan; Jupyter içinde Anaconda Assistant ya da Jupyter AI |
| Gerçek hasta verileri | Asla kullanılmaz | Yalnızca kurumun bir bilgisayarında ve kurumun kurallarına uygun olarak kullanılır |

## A seçeneği: Google Colab

1. Haftanın ders sayfasında bir uygulama durağındaki **Colab'da aç** düğmesine basınız. Hafta sayfasında ve eğitim sitesinde de aynı düğme bulunur.
2. Bir Google hesabıyla giriş yapınız ve değişikliklerinizin kaybolmaması için **Dosya → Drive'a kopya kaydet** (**File → Save a copy in Drive**) komutuyla kendi kopyanızı kaydediniz.
3. **0. bölümü** çalıştırınız. Bölümün başlangıç hücresi, `vclinic` ders paketini birkaç saniye içinde GitHub'dan indirir; haftanın veri dosyaları ise bir hücre bu dosyalara ilk kez ihtiyaç duyduğunda indirilir. Jupyter Notebook'un sonraki her bölümü kendi başlangıç hücresiyle açıldığı için bir bölüme doğrudan da başlanabilir.
4. Her uygulama durağının üç bölümünü sırayla çalışınız: **Python temelleri**, **Prompt ile uygulama** ve **Hazır uygulama**. Colab'ın YZ asistanı Gemini, pencerenin üstündeki düğmesiyle açılır.

Colab oturumları geçicidir: Bir oturumda oluşturulan dosyalar oturum sona erdiğinde silinir, Drive'a kaydedilen Jupyter Notebook ise korunur. Colab'da PyTorch dâhil eğitimin paketlerinin çoğu hazır olarak bulunmaktadır. İki EKG paketi, `wfdb` ve `neurokit2`, 1. haftanın Jupyter Notebook'unun 0. bölümünde kurulur.

## B seçeneği: Kendi bilgisayarınızda Jupyter

Aşağıdaki adımlarla, Python'u ve Jupyter'i birlikte getiren Anaconda kurulur ve ders klasörü indirilir. Adımlar yaklaşık 20 dakika sürer ve bir kez yapılır. Kendi kliniğinizin verileriyle daha sonra yapacağınız çalışmalarda da aynı ortam kullanılacaktır.

### 1. Anaconda'yı kurunuz

Bilgisayarın işletim sistemine uygun Anaconda Distribution'ı [anaconda.com/download](https://www.anaconda.com/download) adresinden indiriniz ve varsayılan seçeneklerle kurunuz. Anaconda, Python ve Jupyter ile birlikte 1. haftanın gerektirdiği paketlerin çoğunu da kurar: NumPy, pandas, SciPy, Matplotlib ve Seaborn.

### 2. Ders klasörünü indiriniz

[Eğitimin GitHub sayfasında](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture) önce **Code** düğmesine, sonra **Download ZIP** seçeneğine tıklayınız ve dosyayı bir klasöre açınız. Klasörü OneDrive gibi bulutla eşitlenen bir yere değil, örneğin `Belgeler/dersler` gibi bir klasöre açmak dosyaların kilitlenmesini önler. git kullananlar aynı klasörü şu komutla oluşturabilir:

```bash
git clone https://github.com/utkukose/ai-cardiology-tkd-NB-lecture.git
```

### 3. Jupyter'i başlatınız

**Anaconda Navigator**'ı açınız, **JupyterLab**'i ya da **Jupyter Notebook**'u başlatınız ve soldaki dosya gezgininde ders klasörüne gidiniz. Bunun yerine Windows'ta **Anaconda Prompt**'u, macOS ve Linux'ta **Terminal**'i açınız, ders klasörüne gidiniz ve JupyterLab'i başlatınız:

```bash
cd ders/klasorunun/yolu/ai-cardiology-tkd-NB-lecture
jupyter lab
```

### 4. Bilgisayarı başlangıç Jupyter Notebook'uyla kontrol ediniz

`tr/baslangic/NB00_baslangic.ipynb` dosyasını açınız ve **Run → Run All Cells** ile bütün hücreleri çalıştırınız. Bu Jupyter Notebook'ta önce paketler kontrol edilir ve ders klasörü bulunur; ardından ilk EKG çizilir. Her şey çalışıyorsa son hücrede **1. haftaya hazırsınız** mesajı görünür.

### 5. Haftanın Jupyter Notebook'unu açınız

Haftanın klasöründeki Jupyter Notebook'u, örneğin `tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb` dosyasını açınız ve önce 0. bölümü çalıştırınız. Bölümün başlangıç hücresi ders klasörünü bulduktan sonra `vclinic` ders paketini ve haftanın paketlerini yüklemekte ve paketin sürümünü göstermektedir. **Kernel → Restart Kernel and Run All Cells** komutu ise Jupyter Notebook'u temiz bir durumdan başlayarak yeniden çalıştırır.

### 6. Sonraki haftaların paketleri

Jupyter Notebook'larda 3. haftadan itibaren eğitimin derin öğrenme paketi olan PyTorch kullanılmaktadır. Anaconda bu paketi içermediği için paket pip ile bir kez kurulmalıdır. Windows'ta Anaconda Prompt'ta, macOS'te Terminal'de şu komutu çalıştırınız:

```bash
pip install torch torchvision
```

Linux'ta varsayılan paket NVIDIA ekran kartları için kütüphaneler de içerir ve büyüktür. Eğitimin Jupyter Notebook'ları ekran kartı gerektirmediği için işlemciye yönelik daha küçük sürüm yeterlidir:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

Başka sistemler için uygun komut, [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/) adresindeki seçiciyle belirlenebilir. Kurulumdan sonra açık bir Jupyter Notebook'un çekirdeğini yeniden başlatınız. Colab'da PyTorch hazır gelir.

3. haftada ilk model, derin öğrenme için üst düzey bir arayüz olan Keras ile de kurulmaktadır. Keras Colab'da hazır olarak bulunur; başka ortamlarda ise `pip install keras` komutuyla kurulabilir. Jupyter Notebook Keras'ı PyTorch üzerinde çalıştırdığı için TensorFlow gerekmez. Keras kurulu değilse Jupyter Notebook yalnızca bu hücreyi atlar.

4. haftadan itibaren ekokardiyogramlardaki sınırlar için scikit-image paketi de kullanılmaktadır. Bu paket Anaconda'da ve Colab'da hazır olarak bulunur; başka bir Python ortamında `pip install scikit-image` komutuyla kurulabilir.

6. haftadan itibaren önceden eğitilmiş dil modelleri için Hugging Face'in transformers paketi de kullanılmaktadır. Paket, ilk kullanımda eğitimin küçük Türkçe modelinin tokenizer'ını ve ağırlıklarını (yaklaşık 19 MB) Hugging Face Hub'dan indirir. Bu paket Colab'da hazır olarak bulunur; başka ortamlarda `pip install transformers` komutuyla kurulabilir.

7. hafta yeni bir paket gerektirmemektedir. Haftanın Jupyter Notebook'u ilk kullanımda Vision Transformer ViT-B/16'nın ImageNet ağırlıklarını (yaklaşık 330 MB) torchvision aracılığıyla, ARCADE anjiyogramlarının darlık kümesini (yaklaşık 452 MB) ise Zenodo'dan indirir. Bu dosyaların ikisi de sonraki çalıştırmalar için bilgisayarda saklanır.

8. hafta yeni bir paket gerektirmez ve bu haftada hiçbir dosya indirilmez: Haftanın bütün verileri ders paketi tarafından bilgisayarda oluşturulmaktadır.

9. hafta yeni bir paket gerektirmemektedir. Haftanın Jupyter Notebook'unda 4. haftanın 300 CAMUS hastası kullanılır; yaklaşık 250 MB tutan bu veriler yalnızca bilgisayarda bulunmadıklarında yeniden indirilir. İsteğe bağlı shap paketi (`pip install shap` komutuyla kurulur), lojistik regresyonun Shapley değerlerini ikinci bir yolla hesaplamaktadır. Paket kurulu değilse Jupyter Notebook kapalı formu kullanır.

10. hafta tek bir yeni paket gerektirmektedir: Prototipin web arayüzü için Streamlit. Paket `pip install streamlit` komutuyla kurulur. 2. uygulama durağının hazır uygulaması, arayüzü haftanın klasörüne `app_af.py` dosyası olarak yazar. Arayüz, bu klasörde açılan Anaconda Prompt'ta `streamlit run app_af.py` komutuyla başlatılır ve tarayıcıda http://localhost:8501 adresinde görüntülenir. Jupyter Notebook ilk kullanımda MIT-BIH Atriyal Fibrilasyon Veri Tabanı'nın 25 kaydının başlık ve işaretleme dosyalarını ve bunlardan üçünün sinyal dosyalarını, yaklaşık 86 MB'lık bir indirmeyle PhysioNet'ten alır; bunun için üyelik gerekmez. Jupyter Notebook Colab'da da çalışır, ancak web arayüzü için katılımcının kendi bilgisayarı gereklidir.

11. hafta yeni bir paket gerektirmez ve bu haftada hiçbir dosya indirilmez: Haftanın çözümlü final projesinde kullanılan Cleveland verisi ders klasörüyle birlikte gelmektedir. Jupyter Notebook, kendi bulunduğu klasöre sonuçları, bir grafiği ve final projesinin araç takımını (`final_project/code/project_tools.py`) içeren `final_project` klasörünü yazar.

1. haftada EKG'ler, ne Anaconda'da ne de Colab'da hazır bulunan `wfdb` ve `neurokit2` paketleriyle okunup işlenmektedir. Bu paketler eksikse ve bilgisayar internete bağlıysa, 1. haftanın Jupyter Notebook'unun 0. bölümünde kurulur. Paketler kurulamazsa Jupyter Notebook'lar kendi içlerindeki yedek kodu kullanır. Paketler önceden de kurulabilir:

```bash
pip install wfdb neurokit2
```

PyTorch dâhil eğitimin bütün paketlerini içeren ayrı bir ortam, ders klasöründeki `environment.yml` dosyasından oluşturulabilir:

```bash
conda env create -f environment.yml
conda activate ai-cardiology
jupyter lab
```

### 7. Ders klasörünü her hafta güncelleyiniz

Eğitim süresince depoya yeni haftalar eklenmektedir. git kullanılıyorsa yeni dosyalar, ders klasöründe çalıştırılan `git pull` komutuyla alınabilir; git kullanılmıyorsa ZIP dosyası yeniden indirilmelidir. Üzerinde çalıştığınız Jupyter Notebook'ların kopyalarını ayrı bir klasörde tutunuz; böylece bir güncelleme çalışmalarınızın silinmesine yol açmaz.

## Yapay zekâ asistanı (isteğe bağlı)

YZ asistanı yalnızca uygulama duraklarının [promptlarıyla](PROMPT_PATH.tr.md) çalışanlar için gereklidir; Python kodu yazabilen her asistan kullanılabilir. Anaconda'da Anaconda Assistant, Anaconda Toolbox ile birlikte gelir. Anaconda Toolbox'ı Navigator'daki kutucuğundan ya da aşağıdaki komutla kurunuz. Ardından JupyterLab'de bir Jupyter Notebook açınız ve bir Anaconda hesabıyla oturum açınız. Ücretsiz hesapta istek sayısı sınırlıdır.

```bash
conda install anaconda-toolbox
```

Jupyter AI, bir model sağlayıcısının uygulama programlama arayüzü (API) anahtarıyla ya da yerel bir modelle çalışan, JupyterLab için açık kaynaklı bir eklentidir. Google Colab'da Gemini yerleşik olarak bulunur. Bu seçenekler [PROMPT_PATH.tr.md](PROMPT_PATH.tr.md#hangi-asistan) dosyasının YZ asistanları bölümünde karşılaştırılmaktadır. Bu asistanların hiçbirine hasta verisi girilmez.

Gerçek hasta verisi hiçbir zaman Colab'a ya da başka bir bulut hizmetine yüklenmez. Eğitimin Jupyter Notebook'larındaki bütün veriler ya sentetiktir ya da açık erişimlidir.

## Sık karşılaşılan sorunlar

| Sorun | Yapılacak |
|---|---|
| İnternet bağlantısı yokken `No module named 'vclinic'` hatası | Jupyter Notebook'u ders klasörünün içinden açınız. Başlangıç hücresi klasörü bulur ve indirme gerekmez. |
| `No module named 'torch'` hatası | PyTorch'u 6. adımda anlatıldığı gibi kurunuz, ardından çekirdeği yeniden başlatınız. |
| `No module named 'skimage'` hatası | scikit-image paketini `pip install scikit-image` komutuyla kurunuz, ardından çekirdeği yeniden başlatınız. |
| `No module named 'transformers'` hatası | transformers paketini `pip install transformers` komutuyla kurunuz, ardından çekirdeği yeniden başlatınız. |
| Jupyter Notebook ders klasörünün dışında açıldı | Başlangıç hücresi ders paketini Jupyter Notebook'un yanındaki `ai-cardiology-course` klasörüne indirir; veri dosyaları ise ilk gerektiklerinde indirilir. Bunun için bir kez internet bağlantısı gerekmektedir. |
| Hücreler sırasız çalıştırıldıktan sonra hata | **Kernel → Restart Kernel and Run All Cells** seçeneğini seçiniz ya da bölümün başındaki başlangıç hücresini çalıştırınız. |
| GitHub'daki Jupyter Notebook'ta çıktı görünmüyor | GitHub, Jupyter Notebook'u yalnızca görüntüler, çalıştırmaz. Jupyter Notebook'u ders klasörüyle birlikte indiriniz ve Jupyter'de çalıştırınız. |
| OneDrive klasöründe dosyalar kilitli ya da eksik | Ders klasörünü bulutla eşitlenmeyen bir klasöre taşıyınız. |

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
