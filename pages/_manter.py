import streamlit as st

st.set_page_config(
    page_title="Mudaí - Manter",
    page_icon="wave",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { font-weight: 600 !important; text-align: center !important; color: #0a2d54 !important; }

    /* FUNDO BEGE 100% */
    .main, .block-container { background-color: #fdf2e0 !important; max-width: 900px !important; margin: 0 auto !important; padding: 2rem !important; }
    section[data-testid="stAppViewContainer"], [data-testid="stDecoration"] { background: #fdf2e0 !important; }

    /* Mudaí CENTRALIZADO */
    .logo-central {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 20px 0 !important;
    }

    /* TEXTO DA INSTRUÇÃO */
    .texto-instrucao {
        color: #ff751f !important;
        font-weight: bold !important;
        font-size: 18px !important;
        text-align: center !important;
        margin: 25px 0 !important;
    }

    /* SUB-PÁGINA */
    .sub-pagina {
        background-color: #ffcaa8 !important;
        border: 2px solid #77a8af !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 20px 0 !important;
        text-align: center !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }

    .sub-pagina p {
        color: #0a2d54 !important;
        font-size: 18px !important;
        line-height: 1.6 !important;
    }

    /* BOTÕES */
    .stButton > button {
        background: linear-gradient(145deg, #77a8af, #6bc0cd) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        height: 60px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
        transition: all 0.3s !important;
        margin: 10px 0 !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# Mudaí CENTRALIZADO
st.markdown('<div class="logo-central">', unsafe_allow_html=True)
st.image("Mudai.png", width=300)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2>Manter a Frequência</h2>", unsafe_allow_html=True)

# FRASE ADICIONADA
st.markdown('<p class="texto-instrucao">Clique no áudio antes de clicar no vídeo.</p>', unsafe_allow_html=True)

# ÁUDIO
st.audio("manter.ogg", format="audio/ogg")

# VÍDEO
st.video("manter.mp4", autoplay=True, muted=True, loop=True)

# TEXTO
st.markdown("""
<div class="sub-pagina">
<p><strong>Texto:</strong> Sua frequência está sendo mantida. Ideal para atividades de energia média.</p>
<p><strong>Dinâmica:</strong> Respire profundamente e visualize sua energia se mantendo, de forma uniforme e constante.</p>
</div>
""", unsafe_allow_html=True)

# BOTÕES
col1, col2 = st.columns(2)
with col1:
    if st.button("Voltar"):
        st.switch_page("pages/_frequencia.py")
with col2:
    if st.button("Início"):
        st.switch_page("app.py")
