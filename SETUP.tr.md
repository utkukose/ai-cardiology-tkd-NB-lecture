# Kurulum

**Python ile Yapay Zekâ Eğitimi: Kardiyologlar için Uygulamalı Eğitim Programı**<br>
Türk Kardiyoloji Derneği · İlk sürüm: Kasım 2026

[Eğitimin ana sayfası](README.tr.md) · [English](SETUP.md)

Eğitimin Jupyter defterleri, katılımcının kendi bilgisayarında Anaconda ile kurulan Jupyter'de çalışır. Aşağıdaki adımlar yaklaşık 20 dakika sürer ve 1. haftadan önce bir kez yapılır. Google Colab, Anaconda kurulamayan bilgisayarlar için yedek yoldur.

## 1. Anaconda'yı kurun

Bilgisayarın işletim sistemine uygun Anaconda Distribution'ı [anaconda.com/download](https://www.anaconda.com/download) adresinden indirin ve varsayılan seçeneklerle kurun. Anaconda, Python ve Jupyter ile birlikte 1. haftanın gerektirdiği NumPy, pandas, SciPy ve Matplotlib paketlerini de kurar.

## 2. Ders klasörünü indirin

[Eğitimin GitHub sayfasında](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture) önce **Code** düğmesine, sonra **Download ZIP** seçeneğine tıklayın ve dosyayı bir klasöre açın. Klasörü OneDrive gibi bulutla eşitlenen bir yere değil, örneğin `Belgeler/dersler` gibi bir klasöre açmak dosyaların kilitlenmesini önler. git kullananlar aynı klasörü şu komutla oluşturabilir:

```bash
git clone https://github.com/utkukose/ai-cardiology-tkd-NB-lecture.git
```

## 3. Jupyter'i başlatın

**Anaconda Navigator**'ı açın, **JupyterLab**'i ya da **Jupyter Notebook**'u başlatın ve soldaki dosya gezgininde ders klasörüne gidin. Bunun yerine Windows'ta **Anaconda Prompt**'u, macOS ve Linux'ta **Terminal**'i açın, ders klasörüne gidin ve JupyterLab'i başlatın:

```bash
cd ders/klasorunun/yolu/ai-cardiology-tkd-NB-lecture
jupyter lab
```

## 4. Bilgisayarı başlangıç defteriyle kontrol edin

`tr/baslangic/NB00_baslangic.ipynb` dosyasını açın ve **Run → Run All Cells** ile bütün hücreleri çalıştırın. Defter paketleri kontrol eder, ders klasörünü bulur, ilk EKG'yi çizer ve her şey çalışıyorsa **1. haftaya hazırsınız** yazar.

## 5. Haftanın defterini açın

Haftanın klasöründeki Jupyter defterini, örneğin `tr/hafta-01/NB01_python_ve_ekg_temelleri.ipynb` dosyasını açın ve önce Bölüm 0'ı çalıştırın. İlk hücre ders klasörünü bulur, ikinci hücre `vclinic` ders paketinin sürümünü yazar. **Kernel → Restart Kernel and Run All Cells** komutu defteri temiz bir durumdan başlayarak yeniden çalıştırır.

## 6. Sonraki haftaların paketleri

Defterler 3. haftadan itibaren eğitimin derin öğrenme paketi olan PyTorch'u kullanır. Anaconda bu paketi içermez; paket pip ile bir kez kurulur. Windows'ta Anaconda Prompt'ta, macOS'te Terminal'de şu komutu çalıştırın:

```bash
pip install torch torchvision
```

Linux'ta varsayılan paket NVIDIA ekran kartları için kütüphaneler de içerir ve büyüktür. Eğitimin defterleri ekran kartı gerektirmediği için işlemciye yönelik daha küçük sürüm yeterlidir:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

Başka sistemler için komutu [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/) adresindeki seçici verir. Kurulumdan sonra açık bir defterin çekirdeğini yeniden başlatın. Colab'da PyTorch hazır gelir.

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

## 7. Ders klasörünü her hafta güncelleyin

Eğitim süresince depoya yeni haftalar eklenmektedir. git kullanılıyorsa ders klasöründe `git pull` komutu yeni dosyaları getirir. git kullanılmıyorsa ZIP dosyası yeniden indirilir. Üzerinde çalıştığınız defterlerin kopyalarını ayrı bir klasörde tutun; böylece bir güncelleme çalışmalarınızı silmez.

## Yapay zekâ asistanı (isteğe bağlı)

Yapay zekâ (YZ) asistanı yalnızca alıştırmaları asistana prompt (istem) yazarak çözenler, yani [prompt yolunu](PROMPT_PATH.tr.md) izleyenler için gereklidir; Python kodu yazabilen her asistan kullanılabilir. Anaconda'da Anaconda Assistant, Anaconda Toolbox ile birlikte gelir. Navigator'daki Anaconda Toolbox kutucuğundan ya da aşağıdaki komutla kurun. Ardından JupyterLab'de bir defter açın ve bir Anaconda hesabıyla oturum açın. Ücretsiz hesapta istek sayısı sınırlıdır.

```bash
conda install anaconda-toolbox
```

Jupyter AI, bir model sağlayıcısının uygulama programlama arayüzü (API) anahtarıyla ya da yerel bir modelle çalışan, JupyterLab için açık kaynaklı bir eklentidir. Google Colab'da Gemini yerleşik olarak bulunur. Bu seçenekler [PROMPT_PATH.tr.md](PROMPT_PATH.tr.md#yz-asistanları) dosyasının YZ asistanları bölümünde karşılaştırılmaktadır. Bu asistanların hiçbirine hasta verisi girilmez.

## Yedek yol olarak Google Colab

Her defterin bir **Open in Colab** rozeti vardır. Colab bir Google hesabı gerektirir ve tarayıcıda çalışır. **File → Save a copy in Drive** ile bir kopya kaydedin ve ders paketini ve veri dosyalarını GitHub'dan indiren Bölüm 0'ı çalıştırın. Colab oturumları geçicidir: Bir oturumda oluşturulan dosyalar, Drive'a kaydedilmedikçe ya da indirilmedikçe oturum bitince silinir.

Gerçek hasta verisi hiçbir zaman Colab'a ya da başka bir bulut hizmetine yüklenmez. Eğitim defterlerindeki bütün veriler ya sentetiktir ya da açık erişimlidir.

## Sık karşılaşılan sorunlar

| Sorun | Yapılacak |
|---|---|
| İnternet bağlantısı yokken `No module named 'vclinic'` hatası | Defteri ders klasörünün içinden açın. İlk hücre klasörü bulur ve indirme gerekmez. |
| `No module named 'torch'` hatası | PyTorch'u 6. adımda anlatıldığı gibi kurun, ardından çekirdeği yeniden başlatın. |
| Defter ders klasörünün dışında açıldı | İlk hücre ders paketini ve verileri defterin yanındaki `ai-cardiology-course` klasörüne indirir. Bunun için bir kez internet bağlantısı gerekir. |
| Hücreler sırasız çalıştırıldıktan sonra hata | **Kernel → Restart Kernel and Run All Cells** seçeneğini seçin ya da bölümün başındaki *Telafi* hücresini çalıştırın. |
| GitHub'daki defterde çıktı görünmüyor | GitHub defteri yalnızca görüntüler, çalıştırmaz. Defteri ders klasörüyle birlikte indirin ve Jupyter'de çalıştırın. |
| OneDrive klasöründe dosyalar kilitli ya da eksik | Ders klasörünü bulutla eşitlenmeyen bir klasöre taşıyın. |

---

*Prof. Dr. Utku Köse · Süleyman Demirel Üniversitesi · [utkukose.com](https://www.utkukose.com) · İçerik CC BY 4.0, kod MIT.*
