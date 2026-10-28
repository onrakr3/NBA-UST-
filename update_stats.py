import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams

print("NBA istatistikleri indiriliyor...")

# NBA API'den son sezonda çekilme (2025-26 sezonu)
takim_istatistikleri = leaguedashteamstats.LeagueDashTeamStats(
    season='2025-26',
    measure_type_detailed_defense='Base'
)
df = takim_istatistikleri.get_data_frames()[0]

# Gerekli sütunların seçilmesi
columns_to_keep = [
    'TEAM_NAME', 'GP', 'PTS', 'FGM', 'FGA', 'FG_PCT',
    'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
    'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK',
    'PF', 'PLUS_MINUS'
]

# Mevcut sütunlara göre filtreleme
df = df[[col for col in columns_to_keep if col in df.columns]]

# CSV dosyasına kaydetme
df.to_csv('NBA_IDDİA_Üst_Takımlar.csv', index=False)
print("Veriler başarıyla güncellendi ve kaydedildi!")
