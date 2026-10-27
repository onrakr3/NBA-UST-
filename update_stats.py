from datetime import datetime
from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd

print("Resmi NBA istatistikleri ve konferans bilgileri indiriliyor...")

takim_istatistikleri = leaguedashteamstats.LeagueDashTeamStats(
    season='2025-26', measure_type_detailed_defense='Base'
)
df = takim_istatistikleri.get_data_frames()[0]

# Gerekli sütunlara Conference (Konferans) bilgisini de ekliyoruz
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

# Not: nba_api varsayılan olarak konferans bilgisini de barındırır,
# ancak direkt eklemek için tablodan alabiliriz. Eğer direkt gelmezse
# takım adına göre Doğu/Batı haritalaması da yapabiliriz.
