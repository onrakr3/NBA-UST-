import pandas as pd
import streamlit as st

st.set_page_config(page_title="OverGrid NBA", page_icon="🏀", layout="wide")

st.title("OverGrid: Profesyonel NBA Analiz Platformu")

dosya_adi = "NBA_İDDİA_Üst_Takimlar.csv"

try:
  df = pd.read_csv(dosya_adi)
except Exception as e:
  st.error(f"Hata: {e}")
  st.stop()


def get_logo(takim):
  if not isinstance(takim, str):
    return None
  t = takim.lower()
  if "atlanta" in t or "hawks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/atl.png"
  elif "boston" in t or "celtics" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/bos.png"
  elif "brooklyn" in t or "nets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/bkn.png"
  elif "charlotte" in t or "hornets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/cha.png"
  elif "chicago" in t or "bulls" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/chi.png"
  elif "cleveland" in t or "cavaliers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/cle.png"
  elif "dallas" in t or "mavericks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/dal.png"
  elif "denver" in t or "nuggets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/den.png"
  elif "detroit" in t or "pistons" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/det.png"
  elif "golden" in t or "warriors" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/gs.png"
  elif "houston" in t or "rockets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/hou.png"
  elif "indiana" in t or "pacers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/ind.png"
  elif "clippers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/lac.png"
  elif "lakers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/lal.png"
  elif "memphis" in t or "grizzlies" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mem.png"
  elif "miami" in t or "heat" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mia.png"
  elif "milwaukee" in t or "bucks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mil.png"
  elif "minnesota" in t or "timberwolves" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/min.png"
  elif "orleans" in t or "pelicans" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/no.png"
  elif "knicks" in t or "new york" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/nyk.png"
  elif "oklahoma" in t or "thunder" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/okc.png"
  elif "orlando" in t or "magic" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/orl.png"
  elif (
      "philadelphia" in t or "76ers" in t or "phila" in t or "phıladelphia" in t
  ):
    return "https://a.espncdn.com/i/teamlogos/nba/500/phi.png"
  elif "phoenix" in t or "suns" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/phx.png"
  elif "portland" in t or "blazers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/por.png"
  elif "sacramento" in t or "kings" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/sac.png"
  elif "san antonio" in t or "spurs" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/sas.png"
  elif "toronto" in t or "raptors" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/tor.png"
  elif "utah" in t or "jazz" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/uta.png"
  elif "washington" in t or "wizards" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/wsh.png"
  return None


df["Logo"] = df["Takim_adi"].apply(get_logo)

dogu_anahtarlari = [
    "boston",
    "celtics",
    "brooklyn",
    "nets",
    "new york",
    "knicks",
    "philadelphia",
    "76ers",
    "phila",
    "toronto",
    "raptors",
    "chicago",
    "bulls",
    "cleveland",
    "cavaliers",
    "detroit",
    "pistons",
    "indiana",
    "pacers",
    "milwaukee",
    "bucks",
    "atlanta",
    "hawks",
    "charlotte",
    "hornets",
    "miami",
    "heat",
    "orlando",
    "magic",
    "washington",
    "wizards",
]


def konferans_belirle(takim):
  if not isinstance(takim, str):
    return "Batı Konferansı"
  t = takim.lower()
  if any(d in t for d in dogu_anahtarlari):
    return "Doğu Konferansı"
  return "Batı Konferansı"


df["Konferans"] = df["Takim_adi"].apply(konferans_belirle)

tab1, tab2 = st.tabs(["Konferanslar", "Maç Simülasyonu"])

with tab1:
  st.subheader("Doğu Konferansı")
  df_dogu = df[df["Konferans"] == "Doğu Konferansı"]
  cols = ["Logo"] + [c for c in df_dogu.columns if c != "Logo"]
  st.dataframe(
      df_dogu[cols],
      column_config={"Logo": st.column_config.ImageColumn("Arma")},
      use_container_width=True,
  )

  st.subheader("Batı Konferansı")
  df_bati = df[df["Konferans"] == "Batı Konferansı"]
  cols_bati = ["Logo"] + [c for c in df_bati.columns if c != "Logo"]
  st.dataframe(
      df_bati[cols_bati],
      column_config={"Logo": st.column_config.ImageColumn("Arma")},
      use_container_width=True,
  )

with tab2:
  st.subheader("Maç Simülasyonu")
  takimlar = df["Takim_adi"].tolist() if "Takim_adi" in df.columns else []

  if len(takimlar) >= 2:
    col1, col2 = st.columns(2)
    with col1:
      ev_sahibi = st.selectbox("Ev Sahibi", takimlar, index=0)
      if ev_logo := get_logo(ev_sahibi):
        st.image(ev_logo, width=80)

    kalan_takimlar = [t for t in takimlar if t != ev_sahibi]

    with col2:
      deplasman = st.selectbox("Deplasman", kalan_takimlar, index=0)
      if dep_logo := get_logo(deplasman):
        st.image(dep_logo, width=80)

    if st.button("Matris Üret", type="primary"):
      ev_row = df[df["Takim_adi"] == ev_sahibi].iloc[0]
      dep_row = df[df["Takim_adi"] == deplasman].iloc[0]

      ev_at = ev_row.get("Attigi_Sayi", ev_row.get("Evinde_Attigi", 115))
      ev_ye = ev_row.get("Yedigi_Sayi", ev_row.get("Evinde_Yedigi", 112))
      dep_at = dep_row.get("Attigi_Sayi", dep_row.get("Deplasman_Attigi", 112))
      dep_ye = dep_row.get("Yedigi_Sayi", dep_row.get("Deplasman_Yedigi", 115))

      tahmini_ev = (ev_at + dep_ye) / 2
      tahmini_dep = (dep_at + ev_ye) / 2
      toplam_skor = tahmini_ev + tahmini_dep

      st.success("Analiz Tamamlandı!")

      mcol1, mcol2, mcol3 = st.columns(3)
      mcol1.metric("Ev", f"{tahmini_ev:.1f}")
      mcol2.metric("Dep", f"{tahmini_dep:.1f}")
      mcol3.metric("Toplam", f"{toplam_skor:.1f}")

      merkez_tam = int(toplam_skor)
      barem_listesi = [float(merkez_tam + i) + 0.5 for i in range(-7, 8)]

      matrix_data = []
      for barem in barem_listesi:
        fark = toplam_skor - barem
        ust_yuzde = min(max(int(50 + (fark * 5)), 5), 95)
        alt_yuzde = 100 - ust_yuzde

        tavsiye = (
            "Güçlü ÜST"
            if ust_yuzde >= 75
            else "Güçlü ALT"
            if ust_yuzde <= 25
            else "Riskli"
        )

        matrix_data.append({
            "Barem": f"{barem}",
            "ÜST": f"%{ust_yuzde}",
            "ALT": f"%{alt_yuzde}",
            "Durum": tavsiye,
        })

      st.dataframe(pd.DataFrame(matrix_data), use_container_width=True)

  else:
    st.warning("Yeterli takım verisi bulunamadı.")
