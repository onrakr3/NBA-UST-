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

  st.dataframe(df_filtered, use_container_width=True)

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

    # Ev sahibinin seçtiği takım deplasman listesinden otomatik çıkarılır
    kalan_takimlar = [t for t in takimlar if t != ev_sahibi]

    with col2:
      deplasman = st.selectbox("✈️ Deplasman Takımı", kalan_takimlar, index=0)

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

      st.success("Analiz Başarıyla Tamamlandı! 🎯")

      mcol1, mcol2, mcol3 = st.columns(3)
      mcol1.metric("🏠 Ev Sahibi Beklenen Skor", f"{tahmini_ev:.1f}")
      mcol2.metric("✈️ Deplasman Beklenen Skor", f"{tahmini_dep:.1f}")
      mcol3.metric("📊 Tahmini Toplam Skor", f"{toplam_skor:.1f}")

      if toplam_skor > 230:
        st.markdown(
            "### 🔥 Sonuç: **KESİN ÜST!** (Yüksek tempo ve hücum gücü)"
        )
      elif toplam_skor > 220:
        st.markdown("### ⚡ Sonuç: **ÜST Olmaya Aday Maç**")
      else:
        st.markdown("### 🛡️ Sonuç: **Alt / Sınırda Mücadele**")
  else:
    st.warning("Yeterli takım verisi bulunamadı.")
