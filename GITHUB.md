# GitHub'a Proje Yükleme Kılavuzu

Bu kılavuz, **Çoklu QR Oluşturucu** projesini kendi GitHub deponuza (repository) yüklemeniz için adım adım yönergeler içerir. İki farklı yöntemle yükleme yapabilirsiniz: **Git Komut Satırı (Terminal/CMD)** veya **GitHub Desktop** uygulaması.

---

## Ön Hazırlık

Hangi yöntemi kullanırsanız kullanın, önce GitHub web sitesinde boş bir depo (repository) oluşturmalısınız:

1. [github.com](https://github.com)'a giriş yapın.
2. Sağ üst köşedeki **+** ikonuna tıklayıp **New repository** (Yeni depo) seçeneğini seçin.
3. Deponuza bir isim verin (Örn: `coklu-qr-olusturucu`).
4. **Public** (Herkese Açık) veya **Private** (Gizli) seçiminizi yapın.
5. *Önemli:* "Add a README file" veya "Add .gitignore" seçeneklerini **İŞARETLEMEYİN**. Projenizde zaten bu dosyalar bulunmaktadır.
6. **Create repository** butonuna tıklayın ve açılan sayfadaki depo bağlantısını (URL) bir yere kopyalayın.

---

## Yöntem 1: Git Komut Satırı ile Yükleme (Kodlarla)

Bilgisayarınızda [Git](https://git-scm.com/downloads) yüklü ise, CMD (Komut İstemi), PowerShell veya Git Bash kullanarak projenizi GitHub'a gönderebilirsiniz.

Projenizin bulunduğu klasörde (`c:\Users\caglayankaya\Desktop\python\Çoklu QR Oluşturucu`) komut satırını açın ve sırasıyla aşağıdaki komutları çalıştırın:

1. **Git'i Projenizde Başlatın:**
   ```bash
   git init
   ```
   *Bu komut klasörde gizli bir `.git` klasörü oluşturarak git takibini başlatır.*

2. **Dosyaları Yükleme Öncesi Hazırlayın:**
   ```bash
   git add .
   ```
   *Bu komut klasördeki tüm dosyaları (hariç tutulanlar `.gitignore` dosyanızda belirlendiği için onlar otomatik olarak atlanacaktır) hazırlık aşamasına (staging) ekler.*

3. **İlk Versiyonunuzu Kaydedin (Commit):**
   ```bash
   git commit -m "İlk yükleme - Proje dosyaları eklendi"
   ```
   *Bu komut dosyalarınızı "İlk yükleme" notu ile kaydeder.*

4. **Ana Dalın (Branch) Adını Belirleyin:**
   ```bash
   git branch -M main
   ```
   *GitHub'ın yeni standardı olan `main` kelimesini ana depo dalı olarak kullanıyoruz.*

5. **GitHub'daki Deponuzu Bilgisayarınıza Tanıtın:**
   ```bash
   git remote add origin DEPO_URL_ADRESİNİZ
   ```
   *Örnek:* `git remote add origin https://github.com/KULLANICADI/coklu-qr-olusturucu.git`
   *(Buraya kopyaladığınız depo adresini yapıştırın)*

6. **Dosyalarınızı GitHub'a Gönderin (Push):**
   ```bash
   git push -u origin main
   ```
   *(Eğer tarayıcı açılıp GitHub girişi isterse onaylayın. Sonrasında dosyalarınız GitHub'a yüklenecektir.)*

---

## Yöntem 2: GitHub Desktop ile Yükleme (Uygulama İle)

Eğer kodlarla uğraşmak istemiyorsanız, GitHub'ın resmi masaüstü uygulaması [GitHub Desktop](https://desktop.github.com/)'ı indirip kurarak çok daha hızlı yükleme yapabilirsiniz.

1. **GitHub Desktop'ı Açın** ve hesabınıza giriş yapın.
2. Sol üst kısımdan **File** (Dosya) menüsüne tıklayın ve **Add local repository...** (Yerel depo ekle...) seçeneğine tıklayın.
3. Açılan pencerede **Choose...** butonuna tıklayın ve projenizin bulunduğu klasörü seçin (`Çoklu QR Oluşturucu`).
4. Eğer karşınıza *"This directory does not appear to be a Git repository"* (Bu dizin bir Git deposu gibi görünmüyor) uyarısı gelirse, altındaki mavi **create a repository** (yeni bir depo oluştur) yazısına tıklayın.
   - Açılan bölümde isim kısmını aynı bırakın.
   - **Git ignore** veya **License** seçeneklerini `None` olarak bırakın (Çünkü `.gitignore` ve `README.md` dosyamız zaten var).
   - **Create repository** butonuna tıklayın.
5. Projeniz GitHub Desktop içine eklendikten sonra, uygulamanın üst kısmında veya ortasında mavi bir **Publish repository** (Depoyu yayımla) butonu belirecektir. Bu butona tıklayın.
6. Sağ tarafta açılan panelde:
   - **Name:** Deponun GitHub üzerinde görünecek adını belirleyin (boşluksuz ve küçük harf önerilir, örn: `coklu-qr-olusturucu`).
   - **Keep this code private:** Kodların herkes tarafından görülmesini istemiyorsanız işaretli bırakın. Herkes görsün istiyorsanız (Açık kaynak) işareti kaldırın.
7. Son olarak alttaki **Publish repository** butonuna tıkladığınızda tüm projeniz (gereksiz dosyalar `.gitignore` sayesinde hariç tutularak) tek tıklamayla GitHub'a yüklenecektir!

Tebrikler, artık GitHub sayfanıza giderek projenizin başarıyla yüklendiğini görebilirsiniz.
