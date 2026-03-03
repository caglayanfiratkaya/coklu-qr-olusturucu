import PyInstaller.__main__
import os

print("EXE oluşturuluyor...")

# PyInstaller komut argümanları
args = [
    'qr_generator_app.py',     # Ana dosya
    '--onefile',               # Tek dosya EXE olsun
    '--name=QR_Generator',     # EXE adı
    '--hidden-import=dotenv',  # python-dotenv dahil et (bazen otomatik algılamaz)
    '--clean',                 # Önbelleği temizle
    '--noconsole',             # Konsol penceresini GİZLE (Pencere uygulaması)
    '--add-data=logo.ico;.',   # İkon dosyasını EXE içine göm (Runtime için)
    # '--noconfirm',           # Varolan dist klasörünü sormadan sil
]

# İkon varsa ekle (varsayılan: icon.ico)
if os.path.exists("logo.ico"):
    args.append('--icon=logo.ico')

PyInstaller.__main__.run(args)

print("\n-------------------------------------------")
print("BAŞARILI: EXE dosyası 'dist' klasöründe oluşturuldu.")
print("Ayarların çalışması için .env dosyasını EXE yanına koyabilir veya programın oluşturmasını bekleyebilirsiniz.")
