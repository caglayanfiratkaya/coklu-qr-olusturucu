from PIL import Image

def convert_to_ico(png_file, ico_file):
    try:
        img = Image.open(png_file)
        # Boyutlandırma opsiyoneldir ama kaliteli bir ikon için farklı boyutlar eklemek iyidir
        img.save(ico_file, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
        print(f"Başarılı: {png_file} -> {ico_file}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    convert_to_ico("logo.png", "logo.ico")
