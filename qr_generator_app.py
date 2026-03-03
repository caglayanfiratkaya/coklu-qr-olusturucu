import os
import sys
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import tkinter.ttk as ttk

# Gerekli kütüphaneleri kontrol et ve yükle
def install_requirements():
    if getattr(sys, 'frozen', False):
        return

    required_packages = ['pandas', 'qrcode', 'pillow', 'python-dotenv']
    for package in required_packages:
        try:
            if package == 'python-dotenv':
                __import__('dotenv')
            else:
                __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_requirements()

import pandas as pd
import qrcode
from PIL import Image, ImageTk
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Tüm ayarları SADECE .env'den al
DEFAULT_FILL_COLOR = os.getenv("QR_DOLGU_RENGI", "#3f6cab")
DEFAULT_BACK_COLOR = os.getenv("QR_ARKA_PLAN_RENGI", "#ffffff")
DEFAULT_TRANSPARENT = os.getenv("SEFFAF_ARKA_PLAN", "True").lower() == "true"
BUTTON_COLOR = "#4CAF50"  # Yeşil buton rengi
BUTTON_HOVER_COLOR = "#45a049"  # Hover efekti

# Varsayılan Global Ayarlar
DEFAULT_CONFIG = {
    "GIRIS_CSV_ADI": "Dönüştürülecek.csv",
    "CIKIS_KLASOR_ADI": "QR_Kodları",
    "QR_DOLGU_RENGI": DEFAULT_FILL_COLOR,
    "QR_ARKA_PLAN_RENGI": DEFAULT_BACK_COLOR,
    "SEFFAF_ARKA_PLAN": "False"
}

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Çoklu QR Oluşturucu")
        self.root.geometry("380x220")
        self.root.resizable(True, True)  # Genişlik ve yükseklik değiştirilebilir
        self.root.minsize(450, 250)  # Minimum boyut

        try:
            from ctypes import windll
            myappid = 'qr_generator.app.v1.0' 
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass

        icon_path = resource_path("logo.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        # Değişkenler - .env'den gelen değerlerle başlat
        self.csv_path_var = tk.StringVar(value=os.getenv("GIRIS_CSV_ADI", ""))
        self.output_dir_var = tk.StringVar(value=os.getenv("CIKIS_KLASOR_ADI", ""))
        self.fill_color_var = tk.StringVar(value=DEFAULT_FILL_COLOR)
        self.back_color_var = tk.StringVar(value=DEFAULT_BACK_COLOR)
        self.is_transparent_var = tk.BooleanVar(value=DEFAULT_TRANSPARENT)

        self.create_widgets()
        
        # Sadece QR rengini güncelle
        self.update_color_button('fill')

    def load_config(self):
        # Bu fonksiyon artık kullanılmıyor - .env direkt okunuyor
        pass

    def save_config(self):
        env_path = os.path.join(os.getcwd(), '.env')
        
        # Arka plan rengini al ve beyazsa workaround uygula
        back_color = self.back_color_var.get()
        if back_color.lower() == "#ffffff":
            back_color = "#fffffe"  # Windows colorchooser bug workaround
        
        config = {
            "GIRIS_CSV_ADI": self.csv_path_var.get(),
            "CIKIS_KLASOR_ADI": self.output_dir_var.get(),
            "QR_DOLGU_RENGI": self.fill_color_var.get(),
            "QR_ARKA_PLAN_RENGI": back_color,
            "SEFFAF_ARKA_PLAN": str(self.is_transparent_var.get())
        }
        
        try:
            with open(env_path, 'w', encoding='utf-8') as f:
                for key, value in config.items():
                    f.write(f"{key}={value}\n")
        except Exception:
            pass

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Başlık
        header_label = ttk.Label(main_frame, text="QR Kod Oluşturucu", font=("Segoe UI", 12, "bold"))
        header_label.pack(pady=(0, 8))

        # Dosya Ayarları
        file_frame = ttk.LabelFrame(main_frame, text="Dosya Ayarları", padding="6")
        file_frame.pack(fill=tk.X, pady=(0, 6))

        ttk.Label(file_frame, text="Giriş CSV:").grid(row=0, column=0, sticky="w", pady=2)
        ttk.Entry(file_frame, textvariable=self.csv_path_var, width=44).grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(file_frame, text="Seç", command=self.browse_csv, width=5).grid(row=0, column=2)

        ttk.Label(file_frame, text="Çıktı Klasörü:").grid(row=1, column=0, sticky="w", pady=2)
        ttk.Entry(file_frame, textvariable=self.output_dir_var, width=44).grid(row=1, column=1, padx=5, pady=2)
        ttk.Button(file_frame, text="Seç", command=self.browse_folder, width=5).grid(row=1, column=2)

        # Görünüm Ayarları
        style_frame = ttk.LabelFrame(main_frame, text="Görünüm Ayarları", padding="6")
        style_frame.pack(fill=tk.X, pady=(0, 8))

        ttk.Label(style_frame, text="QR Rengi:").grid(row=0, column=0, sticky="w", pady=2)
        self.fill_color_swatch = tk.Label(style_frame, bg=self.fill_color_var.get(), width=3, 
                                         relief=tk.RAISED, borderwidth=1, cursor="hand2")
        self.fill_color_swatch.grid(row=0, column=1, padx=5, pady=2)
        self.fill_color_swatch.bind("<Button-1>", lambda e: self.pick_color('fill'))
        fill_entry = ttk.Entry(style_frame, textvariable=self.fill_color_var, width=12)
        fill_entry.grid(row=0, column=2, padx=5, pady=2)
        fill_entry.bind('<FocusOut>', lambda e: self.update_color_button('fill'))
        fill_entry.bind('<Return>', lambda e: self.update_color_button('fill'))

        # İşlem Butonu
        self.start_btn = tk.Button(main_frame, text="QR KODLARI OLUŞTUR", 
                                   bg=BUTTON_COLOR, fg="white", 
                                   font=("Segoe UI", 10, "bold"), 
                                   command=self.start_thread, 
                                   relief=tk.FLAT, 
                                   pady=6, 
                                   cursor="hand2",
                                   activebackground=BUTTON_HOVER_COLOR)
        self.start_btn.pack(fill=tk.X)

    def browse_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV Dosyaları", "*.csv"), ("Tüm Dosyalar", "*.*")])
        if filename:
            self.csv_path_var.set(filename)

    def browse_folder(self):
        foldername = filedialog.askdirectory()
        if foldername:
            self.output_dir_var.set(foldername)

    def pick_color(self, type_):
        """Renk paletini açar ve donma/yanlış renk sorununu gidermek için tasarlandı."""
        var = self.fill_color_var if type_ == 'fill' else self.back_color_var
        initial = var.get().strip()
        
        if not initial.startswith('#') or len(initial) != 7:
            initial = DEFAULT_FILL_COLOR if type_ == 'fill' else DEFAULT_BACK_COLOR

        # Arayüzü tazele
    def pick_color(self, type_):
        """Her iki paleti de aynı basit ve hatasız mantıkla çalıştırır."""
        var = self.fill_color_var if type_ == 'fill' else self.back_color_var
        initial = var.get()
        
        print(f"\n{'='*50}")
        print(f"PALET AÇILIYOR: {type_}")
    def pick_color(self, type_):
        """QR dolgu rengini seç"""
        var = self.fill_color_var
        initial = var.get()
        
        color = colorchooser.askcolor(color=initial, title="Renk Seç")
        
        if color and color[1]:
            var.set(color[1])
            self.update_color_button('fill')
            self.save_config()

    def update_color_button(self, type_):
        """Arayüzdeki küçük renkli kareyi (swatch) günceller."""
        try:
            color = self.fill_color_var.get().strip()
            if not color.startswith('#') or len(color) != 7:
                return

            self.root.winfo_rgb(color)
            self.fill_color_swatch.config(bg=color)
        except:
            pass

    def start_thread(self):
        self.save_config()
        self.start_btn.config(state='disabled', text="İşleniyor...")
        threading.Thread(target=self.generate_process, daemon=True).start()

    def generate_process(self):
        try:
            self.generate_qrs()
            messagebox.showinfo("Tamamlandı", "QR Kodları başarıyla oluşturuldu!")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu:\n{e}")
        finally:
            self.root.after(0, lambda: self.start_btn.config(state='normal', text="QR KODLARI OLUŞTUR"))

    def clean_filename(self, filename):
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename

    def generate_qrs(self):
        csv_path = self.csv_path_var.get().strip()
        output_dir = self.output_dir_var.get().strip()
        fill_color = self.fill_color_var.get().strip()
        back_color = self.back_color_var.get().strip()
        is_transparent = self.is_transparent_var.get()

        if not csv_path or not output_dir:
            raise ValueError("Lütfen dosya ve klasör seçimlerini yapın.")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        df = pd.read_csv(csv_path, dtype=str, keep_default_na=False, na_filter=False)
        col_name = df.columns[0]
        data_list = df[col_name].dropna().tolist()

        for item in data_list:
            item = item.strip()
            if not item: continue
            
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(item)
            qr.make(fit=True)

            img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")
            
            if is_transparent:
                back_rgb = tuple(int(back_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                datas = img.getdata()
                new_data = []
                for pixel in datas:
                    # Toleransı 20'ye çıkardım (tam olmayan beyazlar için)
                    if all(abs(pixel[i] - back_rgb[i]) < 20 for i in range(3)):
                        new_data.append((255, 255, 255, 0))
                    else:
                        new_data.append(pixel)
                img.putdata(new_data)

            filename = self.clean_filename(item) + ".png"
            img.save(os.path.join(output_dir, filename))

if __name__ == "__main__":
    root = tk.Tk()
    app = QRGeneratorApp(root)
    root.mainloop()