import streamlit as st

st.set_page_config(page_title="Mudaí - Frequência", page_icon="wave")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { font-weight: 600 !important; text-align: center !important; color: #0a2d54 !important; }

    .main, .block-container { background-color: #fdf2e0 !important; }
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
        transition: all 0.3s !important;
    }
    .freq-btn:hover {
        background: #77a8af !important;
        color: white !important;
        transform: translateX(10px) !important;
    }
</style>
""", unsafe_allow_html=True)

st.image("Mudai.png", width=360, use_container_width=True)
# VÍDEO MP4 (NÃO IMAGEM!)
st.video("frequencia.mp4", autoplay=True, muted=True, loop=True)
#ÁUDIO (se tiver)

st.markdown("<h3>Primeiro, ouça esse áudio para ir entrando no estado...</h3>", unsafe_allow_html=True)
st.audio("audio_inicial.ogg", format="audio/ogg")

st.markdown("<h2>Escolha o que deseja fazer com sua frequência</h2>", unsafe_allow_html=True)

if st.button("Aumentar", key="aum", use_container_width=True):
    st.switch_page("pages/_aumentar.py")
if st.button("Manter", key="man", use_container_width=True):
    st.switch_page("pages/_manter.py")
if st.button("Diminuir", key="dim", use_container_width=True):
    st.switch_page("pages/_diminuir.py")
