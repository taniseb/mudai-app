import streamlit as st
import base64

st.set_page_config(page_title="Mudaí", page_icon="wave", layout="centered")

# CSS agressivo para centralizar TUDO
st.markdown("""
<style>
    .main, .block-container { background-color: #fdf2e0 !important; }
    
    /* Centraliza o container da imagem/link */
    .logo-box {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 0 auto 30px auto !important;
    }
    
    /* Remove margens extras do Streamlit */
    [data-testid="stVerticalBlock"] > div:first-child {
        text-align: center !important;
    }
</style>
""", unsafe_allow_html=True)

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

try:
    img = get_base64("Mudai.png")
    # Link HTML com classe customizada
    st.markdown(f'<div class="logo-box"><a href="/" target="_self"><img src="data:image/png;base64,{img}" width="250"></a></div>', unsafe_allow_html=True)
except:
    st.error("Logo não encontrada")

# Conteúdo da página
st.video("mudai_mobile/assets/audio_inicial.mp4", autoplay=True, muted=True, loop=True)
st.markdown("<h3 style='text-align:center;'>Como você quer se sentir?</h3>", unsafe_allow_html=True)

if st.button("Dar um gás! 🔥", use_container_width=True): st.switch_page("pages/_aumentar.py")
if st.button("Ficar no centro 🎯", use_container_width=True): st.switch_page("pages/_manter.py")
if st.button("Desacelerar... 💆", use_container_width=True): st.switch_page("pages/_diminuir.py")


st.markdown("""
<div style="text-align: center; color: #0a2d54; padding: 40px 20px 20px 20px; font-size: 13px; line-height: 1.4;">
    Projeto para o curso de Master PNL, desenvolvido por Tanisé Brandão e elaborado em Novembro de 2025, por Carolina Nóbrega, Càtia Nyland, Emersonn Adolfato e Tanisé Brandão
</div>
""", unsafe_allow_html=True)
