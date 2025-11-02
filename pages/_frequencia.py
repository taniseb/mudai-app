import streamlit as st


st.set_page_config(page_title="Mudaí", page_icon="wave", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { font-weight: 600 !important; text-align: center !important; color: #0a2d54 !important; }

    .main, .block-container { background-color: #fdf2e0 !important; max-width: 900px !important; margin: 0 auto !important; padding: 2rem !important; }
    section[data-testid="stAppViewContainer"], [data-testid="stDecoration"] { background: #fdf2e0 !important; }

    /* MUDaí CENTRALIZADO */
    .logo-central {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 20px 0 !important;
    }

    .stButton > button { /* seus estilos */ }
</style>
""", unsafe_allow_html=True)

# MUDaí CENTRALIZADO
st.markdown('<div class="logo-central">', unsafe_allow_html=True)
st.image("Mudai.png", width=300)
st.markdown('</div>', unsafe_allow_html=True)
# VÍDEO MP4 (NÃO IMAGEM!)
st.video("frequencia.mp4", autoplay=True, muted=True, loop=True)
#ÁUDIO (se tiver)

st.markdown("<h3>Primeiro, ouça esse áudio para ir entrando no estado...(clique no áudio antes de clicar no vídeo acima)</h3>", unsafe_allow_html=True)
st.audio("audio_inicial.ogg", format="audio/ogg")

st.markdown("<h2>Escolha o que deseja fazer com sua frequência</h2>", unsafe_allow_html=True)

if st.button("Aumentar", key="aum", use_container_width=True):
    st.switch_page("pages/_aumentar.py")
if st.button("Manter", key="man", use_container_width=True):
    st.switch_page("pages/_manter.py")
if st.button("Diminuir", key="dim", use_container_width=True):
    st.switch_page("pages/_diminuir.py")
