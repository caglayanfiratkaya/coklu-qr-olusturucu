# Uygulamayı Başkalarıyla Paylaşma ve Çalıştırma Kılavuzu

Bu belge, hazırlanan QR Kod Oluşturucu uygulamasını başka bir bilgisayarda (arkadaşınızda, iş arkadaşınızda vb.) çalıştırmak için yapmanız gerekenleri anlatır.

## 1. Hangi Dosyaları Göndermelisiniz?

Programın çalışması için **tek bir dosya yeterlidir**:

- **`QR_Generator.exe`**: Bu dosya programın kendisidir. İçinde Python ve gerekli tüm kütüphaneler gömülüdür. 

**İsteğe Bağlı Dosyalar:**
- **`Dönüştürülecek.csv`**: Örnek olması açısından kendi Excel/CSV dosyanızı da gönderebilirsiniz.
- **`.env`**: Eğer renk ve ayarları siz yaptıysanız ve karşı tarafta da aynısı olsun istiyorsanız bu dosyayı da gönderebilirsiniz. Göndermezseniz program kendi "varsayılan" ayarlarıyla başlar.

## 2. Karşı Tarafın Yapması Gerekenler

Uygulamayı alan kişinin bilgisayarında **Python kurulu olmasına GEREK YOKTUR.** 

1.  Gönderdiğiniz `QR_Generator.exe` dosyasını (ve varsa CSV dosyasını) masaüstünde bir klasöre koysunlar.
2.  `QR_Generator.exe` dosyasına çift tıklayıp çalıştırsınlar.
3.  Açılan pencereden CSV dosyasını seçip "Oluştur" demeleri yeterlidir.

## 3. Sık Sorulan Sorular

**Soru: "Windows PC'nizi korudu" uyarısı çıkıyor?**
Cevap: Uygulama dijital imzalı olmadığı için Windows bu uyarıyı verebilir. 
- "Ek Bilgi" -> "Yine de Çalıştır" diyerek açabilirler. Bu tamamen güvenlidir.

**Soru: Ayarları nasıl değiştirecekler?**
Cevap: Program kapalıyken `.env` dosyasını Not Defteri ile açıp değiştirebilirler YA DA program içindeki renk seçici ve dosya seçicileri kullanarak ayarları değiştirip işlem yaptıklarında bu ayarlar otomatik kaydedilir.

**Soru: Program açılmıyor?**
Cevap: Genellikle virüs programları, bilinmeyen EXE dosyalarını engelleyebilir. Virüs programına "izin ver" demeleri gerekebilir.
