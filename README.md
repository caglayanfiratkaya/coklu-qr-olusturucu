# Çoklu QR Kod Oluşturucu

Bu Python programı, Excel veya CSV formatındaki listelerde yer alan verileri (örneğin bağlantılar, metinler, seri numaraları vb.) toplu olarak okur ve her biri için otomatik olarak QR kodları oluşturarak belirlediğiniz klasöre kaydeder.

## Özellikler

- **Toplu İşlem:** Tek bir CSV dosyasından yüzlerce veya binlerce QR kodunu saniyeler içinde oluşturma.
- **Özelleştirilebilir Renkler:** QR kodunun dolgu rengini ve arka plan rengini HEX kodlarıyla veya İngilizce renk isimleriyle (`black`, `red`, `#3f6cab`) belirleyebilme.
- **Şeffaf Arka Plan:** İsteğe bağlı olarak arka planı şeffaf (transparent) yapabilme.
- **Dinamik Yapılandırma:** İlk açılışta ayarları sorar ve bir `.env` dosyasına kaydeder. Sonraki kullanımlarda otomatik olarak bu ayarları kullanır.

## Gereksinimler

- Python 3.8 veya üzeri
- Gerekli Python kütüphaneleri: `qrcode`, `python-dotenv`, `pandas` (Eğer sadece .exe kullanacaksanız gereksinimlere ihtiyacınız yoktur.)

## Proje Dosyaları (Scriptler)

Bu projede 3 adet Python dosyası (`.py`) bulunmaktadır. Her birinin görevi şöyledir:

1. **`qr_generator_app.py`**: Projenin **ana** dosyasıdır. Arayüzü açan, CSV/Excel dosyasını okuyan ve QR kodlarını oluşturan temel kodları barındırır. Kaynak koddan çalıştırırken bu dosyayı başlatırsınız.
2. **`exe_olustur.py`**: Projeyi Python yüklü olmayan bilgisayarlarda da çalışabilmesi için `.exe` (çalıştırılabilir Windows uygulaması) formatına dönüştüren geliştirici aracıdır. Tek tıklamayla uygulamanın derlenmesini sağlar.
3. **`convert_icon.py`**: Projenin logosunu (`logo.png`), Windows uygulamalarında ikon olarak kullanılabilmesi için `.ico` formatına (`logo.ico`) çeviren yardımcı bir araçtır.
## Kurulum ve Kullanım

### Seçenek 1: Çalıştırılabilir Dosya (Önerilen)

Eğer programın derlenmiş bir sürümüne (exe) sahipseniz:

1. **`QR_Generator.exe`** (veya sisteminize uygun derlenmiş dosya) dosyesini çift tıklayarak çalıştırın.
2. İlk çalıştırılmasında program size bazı ayarları (CSV dosya adı, renkler, klasör vb.) soracaktır.
3. Bu ayarlar proje dizininde `.env` (gizli dosya olabilir) adı altında kaydedilir.
4. Program çalışmasını tamamladığında `QR_Kodları` (veya belirttiğiniz klasör) içinde QR kodlarınız PNG formatında hazır olacaktır.

### Seçenek 2: Kaynak Koddan Çalıştırma

Geliştiriciler için doğrudan Python üzerinden çalıştırma adımları:

1. Depoyu bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/KULLANICI_ADINIZ/coklu-qr-olusturucu.git
   cd coklu-qr-olusturucu
   ```
2. Sanal bir ortam oluşturun ve aktif edin (isteğe bağlı ama önerilir):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
   *(Eğer requirements.txt yoksa: `pip install qrcode[pil] python-dotenv pandas` kullanabilirsiniz)*
4. Programı çalıştırın:
   ```bash
   python qr_generator_app.py
   ```

## Ayarlar (.env)

Ayarları sonradan değiştirmek isterseniz `.env` dosyasını herhangi bir metin düzenleyici (Örn: Not Defteri) ile açıp düzenleyebilirsiniz. Eğer dosya yoksa `.env.example` dosyasını inceleyebilir ve adını `.env` yaparak kullanabilirsiniz.

Örnek `.env` içeriği:
```ini
GIRIS_CSV_ADI="Dönüştürülecek.csv"
CIKIS_KLASOR_ADI="QR_Kodları"
QR_DOLGU_RENGI="black"
QR_ARKA_PLAN_RENGI="white"
SEFFAF_ARKA_PLAN="False"
```

## Önemli Notlar

- Okunacak veri dosyanızın **ilk satırı başlık (header)** olmalıdır. Program verileri ikinci satırdan itibaren okumaya başlar.
- Veriler CSV dosyasının **ilk sütunundan (A sütunu)** okunur. Karekoda dönüşmesini istediğiniz bilgiler ilk sütunda yer almalıdır.
- Türkçe karakter veya özel karakter sorunları yaşamamak için Excel'den dışa aktarım yaparken dosyanızı **CSV (Virgülle Ayrılmış) (UTF-8)** formatında kaydettiğinizden emin olun.
