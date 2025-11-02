import streamlit as st

st.set_page_config(page_title="Mudaí", page_icon="wave", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { font-weight: 600 !important; text-align: center !important; color: #0a2d54 !important; }

    .main, .block-container { background-color: #fdf2e0 !important; max-width: 900px !important; margin: 0 auto !important; padding: 2rem !important; }
    section[data-testid="stAppViewContainer"], [data-testid="stDecoration"] { background: #fdf2e0 !important; }

    .stButton > button {
        background: linear-gradient(145deg, #77a8af, #6bc0cd) !important;
        color: white !important;
        border: none !important;
        border-radius: 30px !important;
        height: 120px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15) !important;
        transition: all 0.3s !important;
        margin: 15px 0 !important;
    }
    .stButton > button:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 12px 25px rgba(0,0,0,0.2) !important;
    }

    .texto-explicativo {
        background-color: #ffcaa8 !important;
        border-radius: 20px !important;
        padding: 25px !important;
        margin: 30px 0 !important;
        text-align: center !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

st.image("Mudai.png", width=300)
st.markdown("<h2>Escolha seu caminho:</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Questionário", width="stretch"):
        st.switch_page("pages/_questionario.py")
with col2:
    if st.button("Frequência", width="stretch"):
        st.switch_page("pages/_frequencia.py")

st.markdown("""
<div class="texto-explicativo">
<h3>Por que trabalhar a frequência?</h3>
<p>A sua frequência vibracional define como você se sente. Você pode <strong>aumentar</strong>, <strong>diminuir</strong> ou <strong>manter</strong> sua energia.</p>
</div>
""", unsafe_allow_html=True)