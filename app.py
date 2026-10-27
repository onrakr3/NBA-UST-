import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="OverGrid | NBA İddaa Analiz Platformu",
    page_icon="🏀",
    layout="wide",
)

st.title("🔥 OverGrid: Profesyonel NBA Üst Analiz Platformu")
st.markdown(
    "Otomatik güncellenen resmi NBA verileriyle ÜST tahmin ve skor simülasyon"
    " sistemi."
)

# Dosya okuma
dosya_adi = "NBA_İDDİA_Üst_Takimlar.csv"

try:
  df = pd.read_csv(dosya_adi)
except Exception as e:
  st.error(f"Veri yüklenirken hata oluştu: {e}")
  st.stop()


# Akıllı Takım Logo Eşleştirme Fonksiyonu (İsme göre otomatik bulur)
def get_logo(takim_adi):
  if not isinstance(takim_adi, str):
    return None
  t = takim_adi.lower()
  if "atlanta" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/atl.png"
  elif "boston" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/bos.png"
  elif "brooklyn" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/bkn.png"
  elif "charlotte" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/cha.png"
  elif "chicago" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/chi.png"
  elif "cleveland" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/cle.png"
  elif "dallas" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/dal.png"
  elif "denver" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/den.png"
  elif "detroit" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/det.png"
  elif "golden" in t or "warriors" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/gs.png"
  elif "houston" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/hou.png"
  elif "indi
