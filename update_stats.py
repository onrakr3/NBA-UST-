from datetime import datetime
from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd

print("NBA istatistikleri indiriliyor...")

# NBA API'den son sezon verilerini çekme
team_stats = leaguedashteamstats.LeagueDashTeamStats(
    season='2025-26', measure_type_detailed_defense='Advanced'
)
df = team_stats.get_data_frames()[0]

# Gerekli sütunları seçme ve resmi tam isimleri düzeltme
# (Artık kısaltma yerine tüm takımlar resmi ve tam adıyla yazılacak)
df = df[
    [
        'TEAM_NAME',
        'GP',
        'PTS',
        'FGM',
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
    ]
]

# Takım adlarını resmi ve eksiksiz formata sabitleme sözlüğü
isim_duzeltme = {
    'Phila': 'Philadelphia 76ers',
    'Philadelphia 76ers': 'Philadelphia 76ers',
    'New York': 'New York Knicks',
    'New York Knicks': 'New York Knicks',
    'Utah': 'Utah Jazz',
    'Utah Jazz': 'Utah Jazz',
    'Indiana': 'Indiana Pacers',
    'Indiana Pacers': 'Indiana Pacers',
    'Oklahoma City': 'Oklahoma City Thunder',
    'Oklahoma City Thunder': 'Oklahoma City Thunder',
}

# Eğer kısa gelen isimler varsa tam adıyla değiştir
df['TEAM_NAME'] = df['TEAM_NAME'].replace(isim_duzeltme)

# Sütun adlarını Türkçe ve anlaşılır hale getirme
df = df.rename(
    columns={
        'TEAM_NAME': 'Takim_adi',
        'GP': 'Oynanan_Mac',
        'PTS': 'Mac_Basina_Sayi',
    }
)

# Simülasyon ve analiz için örnek ev/deplasman sütunları türetme
df['Evinde_Attigi'] = df['Mac_Basina_Sayi'] + 2.5
df['Evinde_Yedigi'] = 112.0
df['Deplasman_Attigi'] = df['Mac_Basina_Sayi'] - 1.5
df['Deplasman_Yedigi'] = 115.0

# CSV dosyası olarak kaydetme
dosya_adi = 'NBA_İDDİA_Üst_Takimlar.csv'
df.to_csv(dosya_adi, index=False, encoding='utf-8-sig')

print(
    f'Veriler başarıyla güncellendi ve {dosya_adi} dosyasına kaydedildi!'
    f' Tarih: {datetime.now()}'
)
