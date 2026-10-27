import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="OverGrid | NBA İddaa Analiz Platformu",
    page_icon="🏀",
    layout="wide",
)

st.title("🔥 OverGrid: Profesyonel NBA Üst Analiz Platformu")
st.markdown(
    "Resmi NBA verileriyle tam entegre ÜST tahmin ve iddia barem matrisi."
)

dosya_adi = "NBA_İDDİA_Üst_Takimlar.csv"

try:
  df = pd.read_csv(dosya_adi)
except Exception as e:
  st.error(f"Veri yüklenirken hata oluştu: {e}")
  st.stop()


# Orijinal NBA Takım İsimlerine Göre Kusursuz Logo Eşleştirme
def get_logo(takim_adi):
  if not isinstance(takim_adi, str):
    return None
  t = takim_adi.lower()
  if "hawks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/atl.png"
  elif "celtics" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/bos.png"
  elif "nets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/bkn.png"
  elif "hornets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/cha.png"
  elif "bulls" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/chi.png"
  elif "cavaliers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/cle.png"
  elif "mavericks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/dal.png"
  elif "nuggets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/den.png"
  elif "pistons" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/det.png"
  elif "warriors" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/gs.png"
  elif "rockets" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/hou.png"
  elif "pacers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/ind.png"
  elif "clippers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/lac.png"
  elif "lakers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/lal.png"
  elif "grizzlies" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mem.png"
  elif "heat" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mia.png"
  elif "bucks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mil.png"
  elif "timberwolves" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/min.png"
  elif "pelicans" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/no.png"
  elif "knicks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/nyk.png"
  elif "thunder" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/okc.png"
  elif "magic" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/orl.png"
  elif "76ers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/phi.png"
  elif "suns" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/phx.png"
  elif "blazers" in t or "trail blazers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/por.png"
  elif "kings" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/sac.png"
  elif "spurs" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/sas.png"
  elif "raptors" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/tor.png"
  elif "jazz" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/uta.png"
  elif "wizards" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/wsh.png"
  return None


df["Logo"] = df["Takim_adi"].apply(get_logo)

tab1, tab2 = st.tabs(
    ["📊 Genel Takım İstatistikleri", "🔥 Maç Eşleşmesi & Skor Tahmini"]
)

with tab1:
  st.subheader("Resmi NBA Takım Hücum ve Savunma Ortalamaları")
  st.markdown("Takımların resmi NBA verilerine göre hazırlanan ÜST tablosu.")

  arama = st.text_input(
      "🔍 Takım Ara", placeholder="Takım adı yazın (örn. Lakers, Celtics)..."
  )
  if arama:
    df_filtered = df[df["Takim_adi"].str.contains(arama, case=False, na=False)]
  else:
    df_filtered = df

  cols = ["Logo"] + [c for c in df_filtered.columns if c != "Logo"]
  df_filtered = df_filtered[cols]

  st.dataframe(
      df_filtered,
      column_config={
          "Logo": st.column_config.ImageColumn("Arma", help="Resmi Kulüp Arması")
      },
      use_container_width=True,
  )

with tab2:
  st.subheader("Maç Eşleşmesi ve Skor Tahmin Simülasyonu")
  st.markdown(
      "İki farklı NBA takımı seçerek tüm iddia baremlerine göre ÜST/ALT"
      " ihtimallerini inceleyin."
  )

  takimlar = df["Takim_adi"].tolist() if "Takim_adi" in df.columns else []

  if len(takimlar) >= 2:
    col1, col2 = st.columns(2)
    with col1:
      ev_sahibi = st.selectbox("🏠 Ev Sahibi Takım", takimlar, index=0)
      ev_logo = get_logo(ev_sahibi)
      if ev_logo:
        st.image(ev_logo, width=80)

    kalan_takimlar = [t for t in takimlar if t != ev_sahibi]

    with col2:
      deplasman = st.selectbox("✈️ Deplasman Takımı", kalan_takimlar, index=0)
      dep_logo = get_logo(deplasman)
      if dep_logo:
        st.image(dep_logo, width=80)

    if st.button("🚀 Kapsamlı Barem ve Olasılık Matrisi Üret", type="primary"):
      ev_row = df[df["Takim_adi"] == ev_sahibi].iloc[0]
      dep_row = df[df["Takim_adi"] == deplasman].iloc[0]

      ev_at = ev_row.get("Attigi_Sayi", 115)
      ev_ye = ev_row.get("Yedigi_Sayi", 112)
      dep_at = dep_row.get("Attigi_Sayi", 112)
      dep_ye = dep_row.get("Yedigi_Sayi", 115)

      tahmini_ev = (ev_at + dep_ye) / 2
      tahmini_dep = (dep_at + ev_ye) / 2
      toplam_skor = tahmini_ev + tahmini_dep

      st.success("Resmi NBA Analizi Başarıyla Tamamlandı! 🎯")

      mcol1, mcol2, mcol3 = st.columns(3)
      mcol1.metric("🏠 Ev Beklenen", f"{tahmini_ev:.1f}")
      mcol2.metric("✈️ Dep Beklenen", f"{tahmini_dep:.1f}")
      mcol3.metric("📊 Model Toplam Skor", f"{toplam_skor:.1f}")

      st.markdown("---")
      st.markdown("### 📈 Tüm İddaa Baremleri İçin ÜST / ALT Matrisi")

      merkez_tam = int(toplam_skor)
      barem_listesi = [float(merkez_tam + i) + 0.5 for i in range(-7, 8)]

      matrix_data = []
      for barem in barem_listesi:
        fark = toplam_skor - barem
        ust_yuzde = min(max(int(50 + (fark * 5)), 5), 95)
        alt_yuzde = 100 - ust_yuzde

        if ust_yuzde >= 75:
          tavsiye = "🔥 Çok Güçlü ÜST"
        elif ust_yuzde >= 55:
          tavsiye = "⚡ İdeal ÜST"
        elif ust_yuzde <= 25:
          tavsiye = "🛡️ Çok Güçlü ALT"
        elif ust_yuzde <= 45:
          tavsiye = "🧊 İdeal ALT"
        else:
          tavsiye = "⚖️ Sınırda / Riskli"

        matrix_data.append({
            "İddaa Baremi": f"{barem} ÜST / ALT",
            "ÜST İhtimali": f"%{ust_yuzde}",
            "ALT İhtimali": f"%{alt_yuzde}",
            "Analiz Tavsiyesi": tavsiye,
        })

      df_matrix = pd.DataFrame(matrix_data)
      st.dataframe(df_matrix, use_container_width=True)

  else:
    st.warning("Yeterli takım verisi bulunamadı.")
