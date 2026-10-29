from datetime import datetime
from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd

print("Resmi NBA istatistikleri ve konferans bilgileri indiriliyor...")

# Resmi NBA API'den 2025-26 sezonu temel istatistikleri çekme
takim_istatistikleri = leaguedashteamstats.LeagueDashTeamStats(
    season='2025-26', measure_type_detailed_defense='Base'
)
df = takim_istatistikleri.get_data_frames()[0]

# Doğu ve Batı konferansı takımlarının otomatik eşleştirme sözlüğü
konferans_haritasi = {
    "Boston Celtics": "East", "Brooklyn Nets": "East", "New York Knicks": "East", 
    "Philadelphia 76ers": "East", "Toronto Raptors": "East", "Chicago Bulls": "East", 
    "Cleveland Cavaliers": "East", "Detroit Pistons": "East", "Indiana Pacers": "East", 
    "Milwaukee Bucks": "East", "Atlanta Hawks": "East", "Charlotte Hornets": "East", 
    "Miami Heat": "East", "Orlando Magic": "East", "Washington Wizards": "East",
    "Denver Nuggets": "West", "Minnesota Timberwolves": "West", "Oklahoma City Thunder": "West", 
    "Portland Trail Blazers": "West", "Utah Jazz": "West", "Golden State Warriors": "West", 
    "Los Angeles Clippers": "West", "Los Angeles Lakers": "West", "Phoenix Suns": "West", 
    "Sacramento Kings": "West", "Dallas Mavericks": "West", "Houston Rockets": "West", 
    "Memphis Grizzlies": "West", "New Orleans Pelicans": "West", "San Antonio Spurs": "West"
}

# Eğer API'den CONFERENCE sütunu gelmezse veya eksikse sözlükten tamamlayalım
if 'CONFERENCE' not in df.columns:
    df['CONFERENCE'] = df['TEAM_NAME'].map(konferans_haritasi).fillna("Unknown")

# İstenen sütun listesi (Conference bilgisi başa eklendi)
secilen_sutunlar = [
    'TEAM_NAME',
    'CONFERENCE',
    'GP',
    'PTS',
    'OPP_PTS',
    'FGA',
    'FG3M',
    'FG3A',
    'FTM',
    'FTA',
    'OREB',
    'DREB',
    'REB',
    'AST',
    'TOV',
    'STL',
    'BLK',
    'BLKA',
    'PF',
    'PFD',
    'PLUS_MINUS'
]

# Tabloyu filtreleme ve düzenleme
df_final = df[secilen_sutunlar].copy()

# CSV dosyası olarak kaydetme
dosya_adi = "NBA_IDDİA_Üst_Takımlar.csv"
df_final.to_csv(dosya_adi, index=False)

print(f"İşlem tamam! Veriler '{dosya_adi}' dosyasına başarıyla kaydedildi.")
