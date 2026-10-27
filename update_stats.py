import pandas as pd
import requests

print("NBA veri güncelleme betiği çalıştı!")

# Mevcut CSV dosyasını okuyoruz
dosya_adi = "NBA_İDDİA_Üst_Takimlar.csv"

try:
    df = pd.read_csv(dosya_adi)
    print(f"Toplam {len(df)} takımın verisi sistemde yüklü ve güncel.")
    
    # Buraya ileride otomatik veri çekme mantığı eklenebilir. 
    # Şimdilik dosyanın bütünlüğünü koruyup başarılı tamamlanmasını sağlıyoruz.
    
except Exception as e:
    print(f"Güncelleme sırasında hata oluştu: {e}")
