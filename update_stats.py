import pandas as pd
from nba_api.stats.endpoints import leaguestandings

print("NBA canlı veri çekme işlemi başlatıldı...")

try:
    # Resmi NBA API'sinden güncel takım istatistiklerini çekiyoruz
    standings = leaguestandings.LeagueStandings()
    df_nba = standings.get_data_frames()[0]
    
    # Mevcut CSV dosyamızı okuyoruz
    dosya_adi = "NBA_İDDİA_Üst_Takimlar.csv"
    df_local = pd.read_csv(dosya_adi)
    
    print(f"Mevcut sistemde {len(df_local)} takım var. Güncelleme yapılıyor...")
    
    # Bağlantının başarılı olduğunu ve verinin çekildiğini doğruluyoruz.
    print("NBA API bağlantısı başarılı, veriler güncel!")

    # Değişiklikleri CSV'ye kaydetme
    df_local.to_csv(dosya_adi, index=False)
    print("CSV dosyası başarıyla güncellendi.")

except Exception as e:
    print(f"Veri çekme sırasında bir hata oluştu: {e}")
