import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="NBA ÜST Tahmin Sistemi", layout="wide")
st.title("🏀 NBA İddaa ÜST Tahmin ve Analiz Sistemi")
st.markdown("Mevcut takım ortalamaları ve istatistiklerine dayanarak otomatik ÜST analiz motoru.")

@st.cache_data
def load_data():
    df = pd.read_csv('NBA_İDDİA_Üst_Takimlar.csv', encoding='utf-8')
    df.columns = df.columns.str.strip()
    return df

try:
    takimlar = load_data()
except Exception as e:
    st.error(f"Veri yüklenirken hata oluştu: {e}")
    st.stop()

st.sidebar.header("Maç Simülasyonu")
takim_listesi = sorted(takimlar['Takim_adi'].unique())
ev_sahibi = st.sidebar.selectbox("Ev Sahibi Takım", takim_listesi, index=0)
deplasman = st.sidebar.selectbox("Deplasman Takımı", takim_listesi, index=1)
iddaa_baremi = st.sidebar.number_input("İddaa Açılış Baremi (Toplam Sayı)", min_value=180.0, max_value=260.0, value=225.5, step=0.5)

if ev_sahibi == deplasman:
    st.sidebar.warning("Ev sahibi ve deplasman aynı olamaz!")
else:
    ev_row = takimlar[takimlar['Takim_adi'] == ev_sahibi].iloc[0]
    dep_row = takimlar[takimlar['Takim_adi'] == deplasman].iloc[0]
    
    ev_attigi = (ev_row['Evinde_Attigi'] + dep_row['Deplasmanda_Yedigi']) / 2
    dep_attigi = (dep_row['Deplasmanda_Attigi'] + ev_row['Evinde_Yedigi']) / 2
    toplam_beklenen = ev_attigi + dep_attigi

    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label=f"🏠 {ev_sahibi} Beklenen", value=f"{ev_attigi:.2f} sayı")
    with col2:
        st.metric(label=f"✈️ {deplasman} Beklenen", value=f"{dep_attigi:.2f} sayı")
    with col3:
        delta_val = f"{toplam_beklenen - iddaa_baremi:+.2f}"
        st.metric(label="📊 Toplam Beklenen Skor", value=f"{toplam_beklenen:.2f}", delta=delta_val)

    st.subheader("🎯 Tahmin ve Analiz Sonucu")
    if toplam_beklenen > iddaa_baremi:
        st.success(f"**Tahmin: ÜST** | Model Öngörüsü ({toplam_beklenen:.1f}), İddaa Baremi ({iddaa_baremi}) üzerindedir.")
    else:
        st.warning(f"**Tahmin: ALT / Riskli** | Model Öngörüsü ({toplam_beklenen:.1f}), İddaa Baremi ({iddaa_baremi}) altında kalıyor.")

st.divider()
st.subheader("📋 Tüm Takım İstatistikleri Arşivi")
st.dataframe(takimlar, use_container_width=True)
