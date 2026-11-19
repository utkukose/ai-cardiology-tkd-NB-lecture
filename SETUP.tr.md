# Kurulum

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](SETUP.md)

Eğitimin her Jupyter defteri, aynı verilerle ve aynı sonuçlarla iki ortamda çalışır. Hangisini tercih ederseniz onu kullanın; haftadan haftaya değiştirmek de mümkündür. Defterin 1. kısmında kodu, hazır bir prompt (istem) ile bir yapay zekâ (YZ) asistanı yazar; 2. kısmında ise kodu katılımcı Python ile yazar.

| | Google Colab | Kendi bilgisayarınızda Jupyter (Anaconda) |
|---|---|---|
| Neye ihtiyaç var? | Bir Google hesabı ve bir web tarayıcısı | Windows, macOS ya da Linux yüklü, yaklaşık 5 GB boş alanı olan bir bilgisayar |
| Kurulum | Yok | 1. haftadan önce bir kez, yaklaşık 20 dakika |
| Defter nasıl açılır? | Bir uygulama durağındaki, hafta sayfasındaki ya da eğitim sitesindeki **Colab'da aç** düğmesiyle | **Jupyter için indir** bağlantısıyla ya da ders klasörünün tamamıyla |
| Prompt yolu için YZ asistanı | Gemini yerleşiktir | Tarayıcıdaki herhangi bir asistan; Jupyter içinde Anaconda Assistant ya da Jupyter AI |
| Gerçek hasta verileri | Asla kullanılmaz | Yalnızca kurumun bir bilgisayarında ve kurumun kurallarına uygun olarak kullanılır |

## A seçeneği: Google Colab

1. Haftanın ders sayfasında bir uygulama durağındaki **Colab'da aç** düğmesine basın. Hafta sayfasında ve eğitim sitesinde de aynı düğme bulunur.
2. Bir Google hesabıyla giriş yapın ve değişikliklerinizin kaybolmaması için **Dosya → Drive'a kopya kaydet** (**File → Save a copy in Drive**) komutuyla kendi kopyanızı kaydedin.
3. **0. bölümü** çalıştırın. İlk hücresi `vclinic` ders paketini ve haftanın veri dosyalarını birkaç saniyede GitHub'dan indirir.
4. **Kısım 1, prompt yolu** ya da **Kısım 2, Python yolu** ile devam edin. Colab'ın YZ asistanı Gemini, pencerenin üstündeki düğmesiyle açılır.

Colab oturumları geçicidir: Bir oturumda oluşturulan dosyalar oturum bitince silinir; Drive'a kaydedilen defter ise kalır. Colab, PyTorch dâhil eğitimin paketlerini zaten içerir.

## B seçeneği: Kendi bilgisayarınızda Jupyter

Aşağıdaki adımlarla, Python'u ve Jupyter'i birlikte getiren Anaconda kurulur ve ders klasörü indirilir. Adımlar yaklaşık 20 dakika sürer ve bir kez yapılır. Kendi kliniğinizin verileriyle daha sonra yapacağınız çalışmaların ortamı da budur.

### 1. Anaconda'yı kurun

Bilgisayarın işletim sistemine uygun Anaconda Distribution'ı [anaconda.com/download](https://www.anaconda.com/download) adresinden indirin ve varsayılan seçeneklerle kurun. Anaconda, Python ve Jupyter ile birlikte 1. haftanın gerektirdiği NumPy, pandas, SciPy ve Matplotlib paketlerini de kurar.

### 2. Ders klasörünü indirin

[Eğitimin GitHub sayfasında](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture) önce **Code** düğmesine, sonra **Download ZIP** seçeneğine tıklayın ve dosyayı bir klasöre açın. Klasörü OneDrive gibi bulutla eşitlenen bir yere değil, örneğin `Belgeler/dersler` gibi bir klasöre açmak dosyaların kilitlenmesini önler. git kullananlar aynı klasörü şu komutla oluşturabilir:

```bash
git clone https://github.com/utkukose/ai-cardiology-tkd-NB-lecture.git
```

### 3. Jupyter'i başlatın

**Anaconda Navigator**'ı açın, **JupyterLab**'i ya da **Jupyter Notebook**'u başlatın ve soldaki dosya gezgininde ders klasörüne gidin. Bunun yerine Windows'ta **Anaconda Prompt**'u, macOS ve Linux'ta **Terminal**'i açın, ders klasörüne gidin ve JupyterLab'i başlatın:

```bash
cd ders/klasorunun/yolu/ai-cardiology-tkd-NB-lecture
jupyter lab
```

### 4. Bilgisayarı başlangıç defteriyle kontrol edin

`tr/baslangic/NB00_baslangic.ipynb` dosyasını açın ve **Run → Run All Cells** ile bütün hücreleri çalıştırın. Defter paketleri kontrol eder, ders klasörünü bulur, ilk EKG'yi çizer ve her şey çalışıyorsa **1. haftaya hazırsınız** yazar.

### 5. Haftanın defterini açın

Haftanın klasöründeki Jupyter defterini, örneğin `tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb` dosyasını açın ve önce 0. bölümü çalıştırın. İlk hücre ders klasörünü bulur, ikinci hücre `vclinic` ders paketinin sürümünü yazar. **Kernel → Restart Kernel and Run All Cells** komutu defteri temiz bir durumdan başlayarak yeniden çalıştırır.

### 6. Sonraki haftaların paketleri

Defterler 3. haftadan itibaren eğitimin derin öğrenme paketi olan PyTorch'u kullanır. Anaconda bu paketi içermez; paket pip ile bir kez kurulur. Windows'ta Anaconda Prompt'ta, macOS'te Terminal'de şu komutu çalıştırın:

```bash
pip install torch torchvision
```

Linux'ta varsayılan paket NVIDIA ekran kartları için kütüphaneler de içerir ve büyüktür. Eğitimin defterleri ekran kartı gerektirmediği için işlemciye yönelik daha küçük sürüm yeterlidir:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

Başka sistemler için komutu [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/) adresindeki seçici verir. Kurulumdan sonra açık bir defterin çekirdeğini yeniden başlatın. Colab'da PyTorch hazır gelir.

Defterler 4. haftadan itibaren ekokardiyogramlardaki sınırlar için scikit-image paketini de kullanır. Anaconda ve Colab bu paketi içerir; başka bir Python ortamında `pip install scikit-image` komutuyla kurulur.

Defterler 6. haftadan itibaren önceden eğitilmiş dil modelleri için Hugging Face'in transformers paketini de kullanır. Paket ilk kullanımda eğitimin küçük Türkçe modelinin belirteçleyicisini ve ağırlıklarını (yaklaşık 19 MB) Hugging Face Hub'dan indirir. Colab bu paketi içerir; başka ortamlarda `pip install transformers` komutuyla kurulur.

7. hafta yeni bir paket gerektirmez. Haftanın defteri ilk kullanımda görü dönüştürücüsü ViT-B/16'nın ImageNet ağırlıklarını (yaklaşık 330 MB) torchvision aracılığıyla, ARCADE anjiyogramlarının darlık kümesini (yaklaşık 452 MB) ise Zenodo'dan indirir; ikisi de sonraki çalıştırmalar için bilgisayarda saklanır.

Defterler, `wfdb` ve `neurokit2` paketleri kuruluysa bu paketleri, kurulu değilse kendi içlerindeki yedek kodu kullanır. Paketleri kurmak için şu komutu çalıştırın:

```bash
pip install wfdb neurokit2
```

PyTorch dâhil eğitimin bütün paketlerini içeren ayrı bir ortam, ders klasöründeki `environment.yml` dosyasından oluşturulabilir:

```bash
conda env create -f environment.yml
conda activate ai-cardiology
jupyter lab
```

### 7. Ders klasörünü her hafta güncelleyin

Eğitim süresince depoya yeni haftalar eklenmektedir. git kullanılıyorsa ders klasöründe `git pull` komutu yeni dosyaları getirir. git kullanılmıyorsa ZIP dosyası yeniden indirilir. Üzerinde çalıştığınız defterlerin kopyalarını ayrı bir klasörde tutun; böylece bir güncelleme çalışmalarınızı silmez.

## Yapay zekâ asistanı (isteğe bağlı)

YZ asistanı yalnızca alıştırmaları asistana prompt yazarak çözenler, yani [prompt yolunu](PROMPT_PATH.tr.md) izleyenler için gereklidir; Python kodu yazabilen her asistan kullanılabilir. Anaconda'da Anaconda Assistant, Anaconda Toolbox ile birlikte gelir. Anaconda Toolbox'ı Navigator'daki kutucuğundan ya da aşağıdaki komutla kurun. Ardından JupyterLab'de bir defter açın ve bir Anaconda hesabıyla oturum açın. Ücretsiz hesapta istek sayısı sınırlıdır.

```bash
conda install anaconda-toolbox
```

Jupyter AI, bir model sağlayıcısının uygulama programlama arayüzü (API) anahtarıyla ya da yerel bir modelle çalışan, JupyterLab için açık kaynaklı bir eklentidir. Google Colab'da Gemini yerleşik olarak bulunur. Bu seçenekler [PROMPT_PATH.tr.md](PROMPT_PATH.tr.md#hangi-asistan) dosyasının YZ asistanları bölümünde karşılaştırılmaktadır. Bu asistanların hiçbirine hasta verisi girilmez.

Gerçek hasta verisi hiçbir zaman Colab'a ya da başka bir bulut hizmetine yüklenmez. Eğitim defterlerindeki bütün veriler ya sentetiktir ya da açık erişimlidir.

## Sık karşılaşılan sorunlar

| Sorun | Yapılacak |
|---|---|
| İnternet bağlantısı yokken `No module named 'vclinic'` hatası | Defteri ders klasörünün içinden açın. İlk hücre klasörü bulur ve indirme gerekmez. |
| `No module named 'torch'` hatası | PyTorch'u 6. adımda anlatıldığı gibi kurun, ardından çekirdeği yeniden başlatın. |
| `No module named 'skimage'` hatası | scikit-image paketini `pip install scikit-image` komutuyla kurun, ardından çekirdeği yeniden başlatın. |
| `No module named 'transformers'` hatası | transformers paketini `pip install transformers` komutuyla kurun, ardından çekirdeği yeniden başlatın. |
| Defter ders klasörünün dışında açıldı | İlk hücre ders paketini ve verileri defterin yanındaki `ai-cardiology-course` klasörüne indirir. Bunun için bir kez internet bağlantısı gerekir. |
| Hücreler sırasız çalıştırıldıktan sonra hata | **Kernel → Restart Kernel and Run All Cells** seçeneğini seçin ya da bölümün başındaki *Telafi* hücresini çalıştırın. |
| GitHub'daki defterde çıktı görünmüyor | GitHub defteri yalnızca görüntüler, çalıştırmaz. Defteri ders klasörüyle birlikte indirin ve Jupyter'de çalıştırın. |
| OneDrive klasöründe dosyalar kilitli ya da eksik | Ders klasörünü bulutla eşitlenmeyen bir klasöre taşıyın. |

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
