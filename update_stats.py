from datetime import datetime
from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd

print("Resmi NBA istatistikleri indiriliyor...")

# NBA API'den son sezon verilerini çekme
takim_istatistikleri = leaguedashteamstats.LeagueDashTeamStats(
    season='2025-26', measure_type_detailed_defense='Base'
)
df = takim_istatistikleri.get_data_frames()[0]

# Gerekli resmi sütunların seçilmesi
df = df[[
    'TEAM_NAME',
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
    'PLUS_MINUS',
]]

# Sütun adlarını Türkçe analize uygun hale getirelim
df.columns = [
    'Takim_adi',
    'Mac_Sayisi',
    'Attigi_Sayi',
    'Yedigi_Sayi',
    'Sut_Girisimi',
    'Uclu_Atis',
    'Uclu_Deneme',
    'Serbest_Atis',
    'Serbest_Deneme',
    'Hucum_Raund',
    'Savunma_Raund',
    'Toplam_Raund',
    Asist := 'Asist',
    'Top_Kaybi',
    'Top_Calma',
    'Blok',
    'Blok_Yeme',
    'Faul',
    'Alinan_Faul',
    'Averaj',
]

# CSV dosyasına kaydet
df.to_csv('NBA_İDDİA_Üst_Takimlar.csv', index=False)
print('Veriler başarıyla güncellendi ve kaydedildi!')
