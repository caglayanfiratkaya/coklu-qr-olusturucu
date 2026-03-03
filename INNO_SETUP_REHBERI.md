# 🚀 ÇOKLU QR OLUŞTURUCU - INNO SETUP KURULUM REHBERİ

Bu rehber, QR Generator uygulamanızı profesyonel bir kurulum dosyasına dönüştürmek için gereken **TÜM** adımları içerir.

---

## 📋 İÇİNDEKİLER

1. [Ön Hazırlık](#1-ön-hazırlık)
2. [Inno Setup Kurulumu](#2-inno-setup-kurulumu)
3. [Proje Dosyalarını Hazırlama](#3-proje-dosyalarını-hazırlama)
4. [EXE Boyutunu Küçültme](#4-exe-boyutunu-küçültme)
5. [Setup Dosyasını Oluşturma](#5-setup-dosyasını-oluşturma)
6. [Test ve Dağıtım](#6-test-ve-dağıtım)
7. [Sorun Giderme](#7-sorun-giderme)

---

## 1️⃣ ÖN HAZIRLIK

### Gerekli Yazılımlar
- ✅ Python 3.x (Zaten kurulu)
- ✅ PyInstaller (Zaten kurulu)
- ⬜ **Inno Setup** (İndireceğiz)
- ⬜ **UPX** (Opsiyonel, boyut küçültme için)

### Proje Klasör Yapısı (Şu Anki)
```
Çoklu QR Oluşturucu/
├── qr_generator_app.py       # Ana program
├── exe_olustur.py             # PyInstaller scripti
├── QR_Generator.spec          # PyInstaller config (OPTİMİZE EDİLDİ ✅)
├── logo.ico                   # Program ikonu
├── Dönüştürülecek.csv         # Örnek CSV
├── README.md                  # Genel dokümantasyon
├── .env                       # Ayarlar (varsa)
├── dist/                      # PyInstaller çıktısı (EXE burada)
├── build/                     # Geçici dosyalar
└── Setup/                     # YENİ OLUŞTURULDU ✅
    ├── InnoSetup/
    │   └── QR_Generator_Setup.iss  # Setup script
    ├── Output/                # Setup.exe buraya oluşacak
    └── Files/                 # Ek dosyalar (oluşturacağız)
```

---

## 2️⃣ INNO SETUP KURULUMU

### Adım 1: İndir
1. **Resmi Site:** https://jrsoftware.org/isdl.php
2. **İndir:** `innosetup-6.x.x.exe` (En son sürüm)
3. **Boyut:** ~5 MB

### Adım 2: Kurulum
1. İndirilen dosyayı çalıştırın
2. "Next" → "I accept" → "Next"
3. **Önemli:** "Install Inno Setup Preprocessor" seçeneğini işaretleyin
4. Kurulum konumu: `C:\Program Files (x86)\Inno Setup 6\`
5. "Install" → "Finish"

### Adım 3: Doğrulama
```powershell
# PowerShell'de test edin:
& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" /?
```
Çıktı: "Inno Setup Compiler Version..." görünmeli

---

## 3️⃣ PROJE DOSYALARINI HAZIRLAMA

### Adım 1: Ek Dosyaları Oluştur

**A) .env.sample Dosyası**

`Setup/Files/.env.sample` dosyası oluşturun:

```plaintext
GIRIS_CSV_ADI=Dönüştürülecek.csv
CIKIS_KLASOR_ADI=QR_Kodları
QR_DOLGU_RENGI=#3f6cab
QR_ARKA_PLAN_RENGI=white
SEFFAF_ARKA_PLAN=True
```

**B) KULLANIM_KILAVUZU.txt**

`Setup/Files/KULLANIM_KILAVUZU.txt` dosyası oluşturun:

```
═══════════════════════════════════════════════════════════
   ÇOKLU QR OLUŞTURUCU - KULLANIM KILAVUZU
═══════════════════════════════════════════════════════════

🎯 PROGRAM HAKKINDA
Bu program, Excel/CSV listesindeki verileri toplu olarak 
QR kodlarına dönüştürür.

📖 HIZLI BAŞLANGIÇ
1. Programı çalıştırın (QR_Generator.exe)
2. CSV dosyanızı seçin (veya varsayılan kullanın)
3. Ayarları yapılandırın (renkler, klasör vb.)
4. "QR KODLARI OLUŞTUR" butonuna tıklayın

⚙️ AYARLAR (.env dosyası)
Ayarları değiştirmek için kurulum klasöründeki .env 
dosyasını Not Defteri ile açın:

- GIRIS_CSV_ADI: QR koduna dönüştürülecek CSV dosyası
- CIKIS_KLASOR_ADI: QR kodlarının kaydedileceği klasör
- QR_DOLGU_RENGI: QR kodunun rengi (örn: #3f6cab)
- QR_ARKA_PLAN_RENGI: Arka plan rengi (örn: white)
- SEFFAF_ARKA_PLAN: True/False (şeffaflık)

📝 CSV FORMATI
CSV dosyanızın ilk satırı başlık olmalıdır:

QR
0758
1234
5678

💡 İPUÇLARI
- Türkçe karakter sorunu yaşarsanız CSV'yi UTF-8 olarak kaydedin
- QR kodları seçtiğiniz klasöre .png formatında kaydedilir
- Ayarlarınız her çalıştırmada saklanır

🆘 DESTEK
Sorun yaşarsanız: support@example.com
═══════════════════════════════════════════════════════════
```

### Adım 2: Klasör Yapısını Tamamla

PowerShell'de çalıştırın:

```powershell
# Files klasörünü oluştur (zaten var)
cd "C:\Users\caglayankaya\Desktop\python\Çoklu QR Oluşturucu"

# .env.sample oluştur
@"
GIRIS_CSV_ADI=Dönüştürülecek.csv
CIKIS_KLASOR_ADI=QR_Kodları
QR_DOLGU_RENGI=#3f6cab
QR_ARKA_PLAN_RENGI=white
SEFFAF_ARKA_PLAN=True
"@ | Out-File -FilePath "Setup\Files\.env.sample" -Encoding UTF8

# KULLANIM_KILAVUZU.txt buradan kopyalanabilir
# (Yukarıdaki içeriği kopyalayın)
```

---

## 4️⃣ EXE BOYUTUNU KÜÇÜLTME

### Adım 1: UPX Kurulumu (Opsiyonel ama Önerilen)

**A) UPX İndir**
1. https://github.com/upx/upx/releases/latest
2. `upx-4.x.x-win64.zip` dosyasını indirin
3. Zip'i açın, içindeki `upx.exe` dosyasını alın

**B) PATH'e Ekle**
```powershell
# C:\Tools\upx\ klasörüne kopyalayın
New-Item -Path "C:\Tools\upx" -ItemType Directory -Force
Copy-Item "C:\Users\KULLANICI\Downloads\upx.exe" "C:\Tools\upx\"

# PATH'e kalıcı olarak ekleyin (Yönetici PowerShell)
[Environment]::SetEnvironmentVariable("Path", 
    $env:Path + ";C:\Tools\upx", 
    [EnvironmentVariableTarget]::Machine)

# Yeni PowerShell açın ve test edin:
upx --version
```

### Adım 2: Optimize Edilmiş EXE Oluştur

QR_Generator.spec dosyası **zaten optimize edildi** ✅:
- ✅ `optimize=2` (Python bytecode optimizasyonu)
- ✅ `strip=True` (Debug sembolleri kaldırıldı)
- ✅ `excludes=[...]` (Gereksiz modüller çıkarıldı)
- ✅ `upx=True` (UPX sıkıştırma aktif)

**EXE'yi Yeniden Oluştur:**

```powershell
# Sanal ortamı aktifleştir
.\.venv\Scripts\Activate.ps1

# Eski dosyaları temizle
Remove-Item -Path "dist", "build" -Recurse -Force -ErrorAction SilentlyContinue

# Yeni EXE oluştur (optimize edilmiş spec ile)
pyinstaller QR_Generator.spec

# Boyutu kontrol et
Get-Item "dist\QR_Generator.exe" | Select-Object Name, @{Name="Size(MB)";Expression={[math]::Round($_.Length/1MB,2)}}
```

**Beklenen Boyut:**
- ❌ Optimizasyon öncesi: ~30-40 MB
- ✅ Optimizasyon sonrası: ~15-20 MB
- ✅ UPX ile: ~8-12 MB

---

## 5️⃣ SETUP DOSYASINI OLUŞTURMA

### Adım 1: Dosya Kontrolü

Aşağıdaki dosyaların olduğundan emin olun:

```powershell
# Kontrol scripti
$files = @(
    "dist\QR_Generator.exe",
    "logo.ico",
    "Dönüştürülecek.csv",
    "Setup\InnoSetup\QR_Generator_Setup.iss",
    "Setup\Files\.env.sample",
    "Setup\Files\KULLANIM_KILAVUZU.txt"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "✅ $file" -ForegroundColor Green
    } else {
        Write-Host "❌ $file - BULUNAMADI!" -ForegroundColor Red
    }
}
```

### Adım 2: Inno Setup Compiler'ı Çalıştır

**Yöntem 1: GUI ile (Önerilen)**

```powershell
# Inno Setup'ı aç
& "C:\Program Files (x86)\Inno Setup 6\Compil32.exe"
```

1. "File" → "Open" → `Setup\InnoSetup\QR_Generator_Setup.iss` seçin
2. **ÖNEMLİ:** Script'i inceleyin, dosya yolları doğru mu?
3. "Build" → "Compile" (veya F9 tuşu)
4. Derleme başarılı olursa: `Setup\Output\QR_Generator_Setup_v1.0.0.exe` oluşur

**Yöntem 2: Komut Satırı ile**

```powershell
# Direkt derle
& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "Setup\InnoSetup\QR_Generator_Setup.iss"
```

### Adım 3: Çıktıyı Kontrol Et

```powershell
# Setup dosyasını listele
Get-Item "Setup\Output\QR_Generator_Setup_v*.exe" | 
    Select-Object Name, 
                  @{Name="Size(MB)";Expression={[math]::Round($_.Length/1MB,2)}},
                  CreationTime
```

**Beklenen Çıktı:**
```
Name                              Size(MB) CreationTime
----                              -------- ------------
QR_Generator_Setup_v1.0.0.exe    12.5     2/2/2026 14:30:00
```

---

## 6️⃣ TEST VE DAĞITIM

### Test Aşaması

**A) Sanal Makine veya Başka Bilgisayarda Test**

1. `QR_Generator_Setup_v1.0.0.exe` dosyasını USB'ye kopyalayın
2. **Python YÜKLÜ OLMAYAN** bir bilgisayarda çalıştırın
3. Kurulum wizard'ını takip edin
4. Kurulum sonrası programı çalıştırın
5. Tüm özellikleri test edin:
   - CSV yükleme
   - QR oluşturma
   - Renk değiştirme
   - Klasör seçimi

**B) Test Listesi**

```
✅ Setup çalışıyor mu?
✅ Program kuruldu mu? (C:\Program Files\QR_Generator\)
✅ Masaüstü kısayolu oluştu mu?
✅ Başlat menüsünde görünüyor mu?
✅ Program açılıyor mu?
✅ CSV dosyası okunuyor mu?
✅ QR kodları oluşturuluyor mu?
✅ Ayarlar kaydediliyor mu? (.env)
✅ Kaldırma (Uninstall) çalışıyor mu?
```

### Dağıtım

**Tek Dosya:** `QR_Generator_Setup_v1.0.0.exe` (~12-15 MB)

**Paylaşma Yöntemleri:**
- 💾 USB bellek
- 📧 E-posta (boyut uygunsa)
- ☁️ Google Drive / OneDrive / Dropbox
- 🌐 Web sitesi (download linki)
- 📦 GitHub Releases

---

## 7️⃣ SORUN GİDERME

### Problem: "dist\QR_Generator.exe bulunamadı"

**Çözüm:**
```powershell
# EXE'yi oluştur
pyinstaller QR_Generator.spec
# Sonra tekrar deneyin
```

### Problem: "UPX çalışmıyor"

**Çözüm 1:** UPX'i devre dışı bırak
- `QR_Generator.spec` dosyasında `upx=True` → `upx=False`

**Çözüm 2:** UPX'i doğru kur
```powershell
# PATH'i kontrol et
$env:Path -split ';' | Select-String 'upx'

# UPX test
upx --version
```

### Problem: "Setup derlenirken hata"

**Çözüm:**
1. Inno Setup'ta "Tools" → "Show errors"
2. Hangi dosya bulunamıyor kontrol edin
3. Dosya yollarını düzeltin `.iss` dosyasında

### Problem: "Kurulum sonrası program açılmıyor"

**Olası Nedenler:**
- Antivirüs engelliyor → Antivirüs'e exception ekleyin
- .NET Framework eksik → Windows Update
- Visual C++ Redistributable eksik → Microsoft'tan indirin

### Problem: "EXE çok büyük"

**Ekstra Optimizasyonlar:**

1. **Pandas Yerine CSV Modülü Kullan** (İleri Seviye)
   - `qr_generator_app.py` içinde pandas yerine Python'un kendi `csv` modülünü kullanın
   - Boyut: ~50 MB azalır

2. **--onedir Kullan**
   - `QR_Generator.spec` içinde `EXE(... )` bölümünü değiştir
   - Boyut: %30 daha küçük (ama klasör olarak)

3. **Nuitka Kullan** (Alternatif)
   ```powershell
   pip install nuitka
   python -m nuitka --standalone --onefile --windows-disable-console qr_generator_app.py
   ```

---

## 📦 SON KONTROL LİSTESİ

Dağıtım öncesi:

```
✅ EXE oluşturuldu ve test edildi
✅ Setup dosyası oluşturuldu
✅ Başka bilgisayarda test edildi
✅ Tüm özellikler çalışıyor
✅ README/Kullanım kılavuzu hazır
✅ Versiyon numarası güncellendi
✅ Dosya boyutu kabul edilebilir
```

---

## 🎯 ÖZET: 5 ADIMDA SETUP OLUŞTUR

```powershell
# 1. Inno Setup'ı indir ve kur
Start-Process "https://jrsoftware.org/isdl.php"

# 2. EXE'yi oluştur
pyinstaller QR_Generator.spec

# 3. Gerekli dosyaları hazırla
# (Yukarıdaki .env.sample ve KULLANIM_KILAVUZU.txt)

# 4. Setup'ı derle
& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "Setup\InnoSetup\QR_Generator_Setup.iss"

# 5. Test et ve dağıt
Start-Process "Setup\Output\QR_Generator_Setup_v1.0.0.exe"
```

---

## 📞 DESTEK

Sorun yaşarsanız:
1. Bu rehberi tekrar okuyun
2. Hata mesajını kopyalayın
3. GitHub Issues'da sorun açın veya mail atın

**İyi Çalışmalar! 🚀**
