import streamlit as st
import base64

st.set_page_config(page_title="Mudaí", page_icon="wave", layout="centered")

def get_base64(path):
    try:
        with open(path, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

img_b64 = get_base64("Mudai.png")

# Usando chaves duplas {{ }} para o CSS não quebrar o Python
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * {{ font-family: 'Montserrat', sans-serif !important; }}
    .main, .block-container {{ background-color: #fdf2e0 !important; }}
    
    .logo-container {{
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 20px;
    }}
    
    .centered-title {{
        text-align: center !important;
        color: #0a2d54;
        width: 100%;
    }}

    .stButton > button {{
        border-radius: 20px;
        height: 80px !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        background-color: white !important;
        border: 1px solid #77a8af !important;
    }}

    .footer {{ 
        text-align: center; 
        color: #0a2d54; 
        padding: 60px 20px 20px 20px; 
        font-size: 13px; 
        line-height: 1.4;
    }}
</style>

<div class="logo-container">
    <img src="data:image/png;base64,{img_b64}" width="320">
</div>
<h2 class="centered-title">Como você quer se sentir agora?</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Fazer o Teste 📝", use_container_width=True): st.switch_page("pages/_questionario.py")
with col2:
    if st.button("Escolher sua mudança ✨", use_container_width=True): st.switch_page("pages/_frequencia.py")

st.markdown('<div class="footer">Projeto para o curso de Master PNL, desenvolvido por Tanisé Brandão e elaborado em Novembro de 2025, por Carolina Nóbrega, Càtia Nyland, Emersonn Adolfato e Tanisé Brandão</div>', unsafe_allow_html=True)
