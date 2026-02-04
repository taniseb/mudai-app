import streamlit as st
import base64

st.set_page_config(page_title="Mudaí - Quiz", page_icon="✨", layout="centered")

def get_base64(path):
    try:
        with open(path, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return None

# CSS COM SELETORES GLOBAIS PARA FORÇAR O TAMANHO
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    .main, .block-container { background-color: #fdf2e0 !important; }
    
    .header-logo { display: flex; justify-content: center; width: 100%; margin-bottom: 30px; }
    
    .question-card { 
        background: white; 
        padding: 40px; 
        border-radius: 25px; 
        text-align: center; 
        margin-bottom: 40px; 
        font-size: 26px; 
        font-weight: 700; 
        color: #0a2d54; 
    }

    /* REMOVENDO CAIXAS E FORÇANDO EMOJIS GIGANTES */
    /* Este seletor pega qualquer botão dentro de uma coluna e o torna invisível */
    div[data-testid="column"] button {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: inherit !important;
        padding: 0 !important;
        height: auto !important;
        width: 100% !important;
    }

    /* Este seletor ataca o texto (emoji) dentro de qualquer botão em colunas */
    div[data-testid="column"] button p, 
    div[data-testid="column"] button span,
    div[data-testid="column"] button div {
        font-size: 120px !important; 
        line-height: 1 !important;
        display: block !important;
        margin: 0 !important;
    }

    /* Estilos de resultado e botões de ação */
    .result-card { background: white; padding: 60px 30px; border-radius: 25px; text-align: center; border: 2px solid #ffcaa8; margin-bottom: 40px; }
    .stButton > button:not([key^="emo_"]) { border-radius: 15px !important; height: 75px !important; font-size: 18px !important; font-weight: 600 !important; border: 2px solid #ffcaa8 !important; }
    
    .footer { 
        text-align: center; 
        color: #0a2d54; 
        padding: 40px 20px 20px 20px; 
        font-size: 13px; 
        line-height: 1.4; 
    }
</style>
""", unsafe_allow_html=True)

if 'passo' not in st.session_state: st.session_state.passo = 0
if 'pontos' not in st.session_state: st.session_state.pontos = 0

img_data = get_base64("Mudai.png")
if img_data:
    st.markdown(f'<div class="header-logo"><a href="/" target="_self"><img src="data:image/png;base64,{img_data}" width="240"></a></div>', unsafe_allow_html=True)

perguntas = ["Como está seu nível de disposição agora? ⚡", "Você sente que sua mente está calma? 🧠", "Como você avalia seu humor neste momento? 😊", "Sente que seu corpo está leve e sem tensões? 🍃", "O quanto você se sente pronto(a) para agir agora? 🚀", "Como está seu nível de foco atual? 🎯"]

if st.session_state.passo < len(perguntas):
    st.markdown(f"<div class='question-card'>{perguntas[st.session_state.passo]}</div>", unsafe_allow_html=True)
    cols = st.columns(5)
    emojis = ["😩", "😕", "😐", "🙂", "🤩"]
    for i, emoji in enumerate(emojis):
        with cols[i]:
            if st.button(emoji, key=f"emo_{st.session_state.passo}_{i}"):
                st.session_state.pontos += (i + 1)
                st.session_state.passo += 1
                st.rerun()
else:
    total = st.session_state.pontos
    if total < 15: res, rota, frase = "Dar um gás! 🔥", "pages/_aumentar.py", "Sua energia está pedindo movimento."
    elif total < 28: res, rota, frase = "Ficar no centro 🎯", "pages/_manter.py", "Você está em um excelente equilíbrio."
    else: res, rota, frase = "Desacelerar... 💆", "pages/_diminuir.py", "Sua vibração está altíssima! Que tal relaxar um pouco?"
    
    st.markdown(f"<div class='result-card'><h1>{frase}</h1></div>", unsafe_allow_html=True)
    if st.button(f"Entrar agora em: {res}", use_container_width=True): st.switch_page(rota)
    if st.button("Escolher sua mudança ✨", use_container_width=True): st.switch_page("pages/_frequencia.py")
    if st.button("Refazer Teste 🔄", use_container_width=True):
        st.session_state.passo = 0; st.session_state.pontos = 0; st.rerun()

st.markdown("""
<div class="footer">
    Projeto para o curso de Master PNL, desenvolvido por Tanisé Brandão e elaborado em Novembro de 2025, por Carolina Nóbrega, Càtia Nyland, Emersonn Adolfato e Tanisé Brandão
</div>
""", unsafe_allow_html=True)
