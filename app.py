import streamlit as st
import pandas as pd
from datetime import datetime

# Sayfa Yapılandırması ve Geniş Mod
st.set_page_config(
    page_title="OverGrid | Profesyonel NBA Analiz Platformu",
    page_icon="🏀",
    layout="wide"
)

# Özel CSS İyileştirmeleri
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e2530;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Başlık Bölümü
st.title("🔥 OverGrid: Profesyonel NBA Analiz Platformu")
st.markdown("Güncel takım istatistikleriyle gelişmiş maç simülasyonu, skor tahminleri ve alt/üst barem analiz sistemi.")

# Veri Okuma
dosya_adi = "NBA_IDDİA_Üst_Takımlar.csv"

try:
    df = pd.read_csv(dosya_adi)
except Exception as e:
    st.error(f"Veri yüklenirken hata oluştu: {e}")
    st.stop()

# Akıllı Takım Logo Eşleştirme Fonksiyonu
def logoyu_al(takim_adi):
    if not isinstance(takim_adi, str):
        return ""
    T = takim_adi.lower()
    logos = {
        "toronto": "https://a.espncdn.com/i/teamlogos/nba/500/tor.png",
        "miami": "https://a.espncdn.com/i/teamlogos/nba/500/mia.png",
        "boston": "https://a.espncdn.com/i/teamlogos/nba/500/bos.png",
        "detroit": "https://a.espncdn.com/i/teamlogos/nba/500/det.png",
        "philadelphia": "https://a.espncdn.com/i/teamlogos/nba/500/phi.png",
        "phila": "https://a.espncdn.com/i/teamlogos/nba/500/phi.png",
        "new york": "https://a.espncdn.com/i/teamlogos/nba/500/nyk.png",
        "atlanta": "https://a.espncdn.com/i/teamlogos/nba/500/atl.png",
        "brooklyn": "https://a.espncdn.com/i/teamlogos/nba/500/bkn.png",
        "charlotte": "https://a.espncdn.com/i/teamlogos/nba/500/cha.png",
        "chicago": "https://a.espncdn.com/i/teamlogos/nba/500/chi.png",
        "dallas": "https://a.espncdn.com/i/teamlogos/nba/500/dal.png",
        "denver": "https://a.espncdn.com/i/teamlogos/nba/500/den.png",
        "golden state": "https://a.espncdn.com/i/teamlogos/nba/500/gs.png",
        "houston": "https://a.espncdn.com/i/teamlogos/nba/500/hou.png",
        "lakers": "https://a.espncdn.com/i/teamlogos/nba/500/lal.png",
        "clippers": "https://a.espncdn.com/i/teamlogos/nba/500/lac.png",
        "memphis": "https://a.espncdn.com/i/teamlogos/nba/500/mem.png",
        "milwaukee": "https://a.espncdn.com/i/teamlogos/nba/500/mil.png",
        "orlando": "https://a.espncdn.com/i/teamlogos/nba/500/orl.png",
        "phoenix": "https://a.espncdn.com/i/teamlogos/nba/500/phx.png",
        "portland": "https://a.espncdn.com/i/teamlogos/nba/500/por.png",
        "sacramento": "https://a.espncdn.com/i/teamlogos/nba/500/sac.png",
        "san antonio": "https://a.espncdn.com/i/teamlogos/nba/500/sas.png",
        "oklahoma": "https://a.espncdn.com/i/teamlogos/nba/500/okc.png",
        "indiana": "https://a.espncdn.com/i/teamlogos/nba/500/ind.png",
        "minnesota": "https://a.espncdn.com/i/teamlogos/nba/500/min.png",
        "new orleans": "https://a.espncdn.com/i/teamlogos/nba/500/nop.png",
        "utah": "https://a.espncdn.com/i/teamlogos/nba/500/uta.png",
        "washington": "https://a.espncdn.com/i/teamlogos/nba/500/wsh.png",
        "cleveland": "https://a.espncdn.com/i/teamlogos/nba/500/cle.png"
    }
    for anahtar, url in logos.items():
        if anahtar in T:
            return url
    return ""

# Sekmeler
tab1, tab2, tab3 = st.tabs(["📅 Günün Maçları", "📊 Takım İstatistikleri", "🏀 Maç Simülasyonu ve Barem Matrisi"])

with tab1:
    st.subheader("📅 Günün NBA Maç Programı")
    st.markdown(f"Bugünün Tarihi: **{datetime.now().strftime('%d.%m.%Y')}** - Karşılaşmaları inceleyip tek tıkla simülasyona aktarabilirsiniz.")
    
    bugunun_maclari = [
        {"ev": "New orleans", "dep": "Sacramento", "saat": "03:00"},
        {"ev": "Atlanta", "dep": "Cleveland", "saat": "03:00"},
        {"ev": "Portland", "dep": "Memphis", "saat": "03:30"},
        {"ev": "Toronto", "dep": "Phoenix", "saat": "02:30"}
    ]
    
    st.markdown("---")
    for idx, mac in enumerate(bugunun_maclari):
        c1, c2, c3 = st.columns([3, 2, 2])
        with c1:
            st.markdown(f"#### 🏀 {mac['ev']} vs {mac['dep']}")
        with c2:
            st.markdown(f"⏰ **Saat:** `{mac['saat']}`")
        with c3:
            if st.button(f"Analiz Et #{idx+1}", key=f"btn_mac_{idx}"):
                st.session_state['secilen_ev'] = mac['ev']
                st.session_state['secilen_dep'] = mac['dep']
                st.success("Takımlar seçildi! Lütfen 'Maç Simülasyonu' sekmesine geçin.")
        st.markdown("---")

with tab2:
    st.subheader("Takım Performans Tablosu")
    arama = st.text_input("🔍 Takım Ara", "")
    if arama:
        filtrelenmis_df = df[df['TEAM_NAME'].str.contains(arama, case=False, na=False)]
    else:
        filtrelenmis_df = df
    st.dataframe(filtrelenmis_df, use_container_width=True)

with tab3:
    st.subheader("Karşılaşma Simülasyonu & Barem Matrisi")
    
    takimlar = df['TEAM_NAME'].tolist() if 'TEAM_NAME' in df.columns else []
    
    secilen_ev_isimi = st.session_state.get('secilen_ev', "")
    secilen_dep_isimi = st.session_state.get('secilen_dep', "")
    
    default_ev_idx = 0
    default_dep_idx = 1 if len(takimlar) > 1 else 0
    
    if secilen_ev_isimi:
        for i, t in enumerate(takimlar):
            if secilen_ev_isimi.lower() in t.lower():
                default_ev_idx = i
                break
                
    if secilen_dep_isimi:
        for i, t in enumerate(takimlar):
            if secilen_dep_isimi.lower() in t.lower():
                default_dep_idx = i
                break

    col1, col2 = st.columns(2)
    with col1:
        ev_sahibi = st.selectbox("Ev Sahibi Takım", takimlar, index=default_ev_idx)
        if logoyu_al(ev_sahibi):
            st.image(logoyu_al(ev_sahibi), width=90)
        
    with col2:
        deplasman = st.selectbox("Deplasman Takımı", takimlar, index=default_dep_idx)
        if logoyu_al(deplasman):
            st.image(logoyu_al(deplasman), width=90)
        
    st.markdown("---")
    
    if st.button("🚀 Matris Üret ve Analiz Et", type="primary", use_container_width=True):
        st.success("Maç analizi ve olasılık matrisi başarıyla oluşturuldu!")
        
        ev_verisi = df[df['TEAM_NAME'] == ev_sahibi]
        dep_verisi = df[df['TEAM_NAME'] == deplasman]
        
        ev_ort = ev_verisi['PTS'].values[0] if not ev_verisi.empty and 'PTS' in ev_verisi.columns else 115.0
        dep_ort = dep_verisi['PTS'].values[0] if not dep_verisi.empty and 'PTS' in dep_verisi.columns else 112.0
        
        toplam_skor = ev_ort + dep_ort
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label=f"🏠 {ev_sahibi} Beklenen Skor", value=f"{ev_ort:.1f}")
        with m2:
            st.metric(label=f"✈️ {deplasman} Beklenen Skor", value=f"{dep_ort:.1f}")
        with m3:
            st.metric(label="🎯 Toplam Barem", value=f"{toplam_skor:.1f}")
        
        st.markdown("### 📈 Alt / Üst Olasılık Matrisi")
        baz_barem = round(toplam_skor * 2) / 2 - 4
        
        tablo_verisi = []
        for i in range(10):
            barem = baz_barem + (i * 1.0)
            ust_oran = max(5, min(95, int(50 + (toplam_skor - barem) * 12)))
            alt_oran = 100 - ust_oran
            
            if ust_oran >= 75:
                durum = "🔥 Güçlü ÜST"
            elif alt_oran >= 75:
                durum = "🛡️ Güçlü ALT"
            else:
                durum = "⚠️ Riskli"
                
            tablo_verisi.append({
                "Barem": barem,
                "ÜST (%)": f"%{ust_oran}",
                "Durum": durum,
                "ALT (%)": f"%{alt_oran}"
            })
            
        st.table(pd.DataFrame(tablo_verisi))
