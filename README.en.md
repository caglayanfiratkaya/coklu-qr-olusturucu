*Read this in other languages: [Türkçe](README.md) | **English***

---

# Bulk QR Code Generator

This Python program reads data (such as links, texts, serial numbers, etc.) from Excel or CSV files in bulk and automatically generates QR codes for each entry, saving them to your specified folder.

## Features

- **Bulk Processing:** Generate hundreds or thousands of QR codes from a single CSV file within seconds.
- **Customizable Colors:** Set the fill and background colors of the QR codes using HEX codes or English color names (`black`, `red`, `#3f6cab`).
- **Transparent Background:** Option to make the background transparent.
- **Dynamic Configuration:** It asks for your settings on first launch and saves them into an `.env` file. It automatically uses these settings in subsequent uses.

## Requirements

- Python 3.8 or higher
- Required Python libraries: `qrcode`, `python-dotenv`, `pandas` (If you are only going to use the .exe, you don't need these requirements.)

## Project Files (Scripts)

This project contains 3 Python files (`.py`). Their purposes are as follows:

1. **`qr_generator_app.py`**: This is the **main** file of the project. It contains the core code that opens the interface, reads the CSV/Excel file, and generates the QR codes. You run this file when executing from the source code.
2. **`exe_olustur.py`**: A developer tool that converts the project into an `.exe` (executable Windows application) format so it can run on computers without Python installed. It allows compiling the application with a single click.
3. **`convert_icon.py`**: A helper tool that converts the project's logo (`logo.png`) into `.ico` format (`logo.ico`) so it can be used as an icon in Windows applications.

## Installation and Usage

### Option 1: Executable File (Recommended)

If you have a compiled version (exe) of the program:

1. Double-click the **`QR_Generator.exe`** (or the compiled file suitable for your system) to run it.
2. On its first run, the program will ask you for some settings (CSV file name, colors, output folder, etc.).
3. These settings will be saved in the project directory as an `.env` file (might be hidden).
4. When the program finishes running, your QR codes will be ready in PNG format inside the `QR_Kodları` (or your specified) folder.

### Option 2: Running from Source Code

Steps for developers to run it directly via Python:

1. Clone the repository to your computer:
   ```bash
   git clone https://github.com/KULLANICI_ADINIZ/coklu-qr-olusturucu.git
   cd coklu-qr-olusturucu
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   *(If requirements.txt is missing, you can use: `pip install qrcode[pil] python-dotenv pandas`)*
4. Run the program:
   ```bash
   python qr_generator_app.py
   ```

## Settings (.env)

If you want to change the settings later, you can open the `.env` file with any text editor (e.g., Notepad) and edit it. If the file doesn't exist, you can review the `.env.example` file and rename it to `.env` to use it.

Example `.env` content:
```ini
GIRIS_CSV_ADI="Dönüştürülecek.csv"
CIKIS_KLASOR_ADI="QR_Kodları"
QR_DOLGU_RENGI="black"
QR_ARKA_PLAN_RENGI="white"
SEFFAF_ARKA_PLAN="False"
```

## Important Notes

- The **first row of your data file must be a header**. The program starts reading data from the second row onwards.
- Data is read from the **first column (Column A)** of the CSV file. The information you want to convert into QR codes must be placed in the first column.
- To avoid issues with Turkish characters or special characters, make sure you save your file in **CSV (Comma delimited) (UTF-8)** format when exporting from Excel.
