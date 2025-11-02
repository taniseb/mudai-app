import streamlit as st
import urllib.parse
st.set_page_config(page_title="Mudaí - Frequência", page_icon="wave", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { font-weight: 600 !important; text-align: center !important; color: #0a2d54 !important; }

    .main, .block-container { background-color: #fdf2e0 !important; max-width: 900px !important; margin: 0 auto !important; padding: 2rem !important; }
    section[data-testid="stAppViewContainer"], [data-testid="stDecoration"] { background: #fdf2e0 !important; }

    .freq-btn {
        background: #ffcaa8 !important;
        color: #0a2d54 !important;
        border: 2px solid #77a8af !important;
        border-radius: 30px !important;
        height: 80px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        margin: 15px 0 !important;
    }
    .freq-btn:hover {
        background: #77a8af !important;
        color: white !important;
        transform: translateX(10px) !important;
    }

    .audio-inicial {
        background-color: #ffcaa8 !important;
        border: 2px solid #77a8af !important;
        border-radius: 20px !important;
        padding: 20px !important;
        margin: 30px 0 !important;
        text-align: center !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# Estado
if 'audio_ouvido' not in st.session_state:
    st.session_state.audio_ouvido = False

st.image("Mudai.png", width=300)
st.markdown("<h2>Escolha o que deseja fazer com sua frequência</h2>", unsafe_allow_html=True)

# GIF ANTES DO ÁUDIO
st.image("inicio.gif", use_container_width=True)

# ÁUDIO INICIAL
st.markdown("""
<div class="audio-inicial">
<p><strong>Ouça o áudio antes de escolher:</strong></p>
</div>
""", unsafe_allow_html=True)

audio_played = st.audio("audio_inicial.ogg", format="audio/ogg")

if audio_played:
    st.session_state.audio_ouvido = True

if st.session_state.audio_ouvido:
    if st.button("Aumentar", key="aum", width="stretch"):
        st.switch_page("pages/_aumentar.py")
    if st.button("Manter", key="man", width="stretch"):
        st.switch_page("pages/_manter.py")
    if st.button("Reduzir", key="red", width="stretch"):
        st.switch_page("pages/_diminuir.py")
else:
    st.info("Toque o áudio acima para liberar as opções.")