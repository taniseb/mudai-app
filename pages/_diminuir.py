import streamlit as st
import base64

st.set_page_config(page_title="Mudaí - Desacelerar", page_icon="💆")

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

try:
    img = get_base64("Mudai.png")
    st.markdown(f'''
        <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
            <a href="/" target="_self">
                <img src="data:image/png;base64,{img}" width="200">
            </a>
        </div>
    ''', unsafe_allow_html=True)
except:
    st.error("Logo não encontrada.")

st.markdown("<style>.main, .block-container { background-color: #fdf2e0 !important; }</style>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>Desacelerar... 💆</h2>", unsafe_allow_html=True)
st.video("mudai_mobile/assets/diminuir_.mp4", autoplay=True, muted=True, loop=True)
st.markdown('<div style="background-color:#f3e5f5; padding:25px; border-radius:15px; border-left:8px solid #7b1fa2; font-size:20px; color:#0a2d54; margin-bottom: 80px; margin-top: 20px; text-align: center;"><strong>Hora de baixar o ritmo.</strong> Ideal para relaxar ou meditar.</div>', unsafe_allow_html=True)
if st.button("Voltar"): st.switch_page("pages/_frequencia.py")

st.markdown("""
<div style="text-align: center; color: #0a2d54; padding: 40px 20px 20px 20px; font-size: 13px; line-height: 1.4;">
    Projeto para o curso de Master PNL, desenvolvido por Tanisé Brandão e elaborado em Novembro de 2025, por Carolina Nóbrega, Càtia Nyland, Emersonn Adolfato e Tanisé Brandão
</div>
""", unsafe_allow_html=True)
