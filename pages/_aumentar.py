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
st.markdown("<h2>Aumentar Frequência</h2>", unsafe_allow_html=True)

# VÍDEO MP4 (NÃO IMAGEM!)
st.video("aumentar.mp4", autoplay=True, muted=True, loop=True)

st.markdown("""
<div class="sub-pagina">
<p><strong>Texto:</strong> Sua frequência está aumentando. Ideal para atividades de alta energia.</p>
<p><strong>Dinâmica:</strong> Respire profundamente e visualize sua energia subindo.</p>
</div>
""", unsafe_allow_html=True)

#ÁUDIO (se tiver)
st.audio("aumentar.ogg", format="audio/ogg")

col1, col2 = st.columns(2)
with col1:
    if st.button("Voltar"):
        st.switch_page("pages/_frequencia.py")
with col2:
    if st.button("Início"):
        st.switch_page("app.py")
