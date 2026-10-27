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


# Akıllı Takım Logo Eşleştirme Fonksiyonu
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
  elif "indiana" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/ind.png"
  elif "clippers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/lac.png"
  elif "lakers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/lal.png"
  elif "memphis" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mem.png"
  elif "miami" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mia.png"
  elif "milwaukee" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/mil.png"
  elif "minnesota" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/min.png"
  elif "orleans" in t or "pelicans" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/no.png"
  elif "knicks" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/nyk.png"
  elif "oklahoma" in t or "thunder" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/okc.png"
  elif "orlando" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/orl.png"
  elif "philadelphia" in t or "76ers" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/phi.png"
  elif "phoenix" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/phx.png"
  elif "portland" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/por.png"
  elif "sacramento" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/sac.png"
  elif "san antonio" in t or "spurs" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/sas.png"
  elif "toronto" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/tor.png"
  elif "utah" in t or "jazz" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/uta.png"
  elif "washington" in t or "wizards" in t:
    return "https://a.espncdn.com/i/teamlogos/nba/500/wsh.png"
  return None


# DataFrame'e logo sütunu ekleme
df["Logo"] = df["Takim_adi"].apply(get_logo)

# Sekmeler oluşturma (Tabs)
tab1, tab2 = st.tabs(
    ["📊 Genel Takım İstatistikleri", "🔥 Maç Eşleşmesi & Skor Tahmini"]
)

with tab1:
  st.subheader("Takım Hücum ve Savunma Ortalamaları")
  st.markdown(
      "Takımların güncel performanslarına göre hazırlanan ÜST analiz tablosu."
  )

  # Arama kutusu
  arama = st.text_input(
      "🔍 Takım Ara", placeholder="Takım adı yazın (örn. Boston, Dallas)..."
  )
  if arama:
    df_filtered = df[df["Takim_adi"].str.contains(arama, case=False, na=False)]
  else:
    df_filtered = df


  # Renkli ÜST Potansiyeli Belirleme Fonksiyonu
  def potansiyel_hesapla(row):
    try:
      toplam = (row.get("Evinde_Attigi", 110) + row.get("Evinde_Yedigi", 110)) / 2
      if toplam > 118:
        return "🟢 Yüksek ÜST Potansiyeli"
      elif toplam > 112:
        return "🟡 Orta ÜST Potansiyeli"
      else:
        return "🔴 Düşük / Sınırda"
    except:
      return "⚪ Normal"


  if (
      "Evinde_Attigi" in df_filtered.columns
      and "Evinde_Yedigi" in df_filtered.columns
  ):
    df_filtered["ÜST_Durumu"] = df_filtered.apply(potansiyel_hesapla, axis=1)

  # Logonun tabloda en başta görünmesi için sütun düzenlemesi
  cols = ["Logo"] + [c for c in df_filtered.columns if c != "Logo"]
  df_filtered = df_filtered[cols]

  st.dataframe(
      df_filtered,
      column_config={
          "Logo": st.column_config.ImageColumn("Arma", help="Kulüp Arması")
      },
      use_container_width=True,
  )

with tab2:
  st.subheader("Maç Eşleşmesi ve Skor Tahmin Simülasyonu")
  st.markdown(
      "İki farklı takım seçerek bu maçın olası toplam skorunu ve ÜST"
      " ihtimalini hesaplayın."
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

    if st.button("🚀 Maçı Analiz Et ve Tahmin Üret", type="primary"):
      ev_row = df[df["Takim_adi"] == ev_sahibi].iloc[0]
      dep_row = df[df["Takim_adi"] == deplasman].iloc[0]

      ev_at = ev_row.get("Evinde_Attigi", 115)
      ev_ye = ev_row.get("Evinde_Yedigi", 112)
      dep_at = dep_row.get("Deplasman_Attigi", 112)
      dep_ye = dep_row.get("Deplasman_Yedigi", 115)

      tahmini_ev = (ev_at + dep_ye) / 2
      tahmini_dep = (dep_at + ev_ye) / 2
      toplam_skor = tahmini_ev + tahmini_dep

      baz_baraj = 226.5
      fark = toplam_skor - baz_baraj
      ust_olasilik = min(max(int(50 + (fark * 4.5)), 15), 95)

      st.success("Profesyonel Analiz Başarıyla Tamamlandı! 🎯")

      mcol1, mcol2, mcol3, mcol4 = st.columns(4)
      mcol1.metric("🏠 Ev Beklenen", f"{tahmini_ev:.1f}")
      mcol2.metric("✈️ Dep Beklenen", f"{tahmini_dep:.1f}")
      mcol3.metric("📊 Toplam Skor", f"{toplam_skor:.1f}")
      mcol4.metric("🔥 ÜST İhtimali", f"%{ust_olasilik}")

      st.write(f"**Maçın 226.5 ÜST Bitme Olasılığı (%{ust_olasilik})**")
      st.progress(ust_olasilik)

      if ust_olasilik >= 75:
        st.markdown(
            "### 🔥 Kesin Tavsiye: **BANKO ÜST!** \n*İki takımın da"
            " temposu ve savunma zaafları yüksek skor üretmeye çok uygun.*"
        )
      elif ust_olasilik >= 55:
        st.markdown(
            "### ⚡ Tavsiye: **ÜST Olmaya Aday** \n*Maçın hücum ağırlıklı"
            " geçmesi bekleniyor ancak sınırda kalabilir.*"
        )
      else:
        st.markdown(
            "### 🛡️ Tavsiye: **ALT veya Sınırda Mücadele** \n*Takımların"
            " savunma dirençleri bu maçta skoru baskılayabilir.*"
        )
  else:
    st.warning("Yeterli takım verisi bulunamadı.")
