import streamlit as st
import urllib.parse  # ← IMPORTANTE

st.set_page_config(page_title="Mudaí - Questionário", page_icon="question", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { font-weight: 600 !important; text-align: center !important; color: #0a2d54 !important; }

    .main, .block-container { background-color: #fdf2e0 !important; max-width: 900px !important; margin: 0 auto !important; padding: 2rem !important; }
    section[data-testid="stAppViewContainer"], [data-testid="stDecoration"] { background: #fdf2e0 !important; }

    .pergunta {
        background-color: #ffcaa8 !important;
        border: 2px solid #77a8af !important;
        border-radius: 20px !important;
        padding: 25px !important;
        margin: 20px 0 !important;
        text-align: center !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }

    .stSlider > div > div > div > div {
        background: linear-gradient(to right, #ff6b6b, #feca57, #48dbfb, #1dd1a1) !important;
    }

    .proxima-btn {
        background: linear-gradient(145deg, #ff751f, #ff9a5e) !important;
        color: white !important;
        border-radius: 30px !important;
        height: 70px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        margin-top: 30px !important;
    }

    .resultado {
        background-color: #ffcaa8 !important;
        border: 2px solid #77a8af !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 20px 0 !important;
        text-align: center !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# Estado
if 'passo_quiz' not in st.session_state: st.session_state.passo_quiz = 1
if 'pontos_quiz' not in st.session_state: st.session_state.pontos_quiz = 0

# LOGO
st.image("Mudai.png", width=300)  # ← CORRETO (sem ../)

st.markdown("<h2>Quiz: Avalie sua Vibração Atual</h2>", unsafe_allow_html=True)

perguntas = [
    ("Como está sua energia física agora?", "Cansado(a), pesado(a)", "Leve, disposto(a)"),
    ("Como está seu foco mental?", "Confuso, disperso", "Claro e criativo"),
    ("Como está sua respiração?", "Curta e rápida", "Profunda e fluida"),
    ("Como está sua voz interna?", "Crítica ou acelerada", "Calma e encorajadora"),
    ("O que você sente no corpo agora?", "Tensão, aperto, peso", "Leveza, conforto, expansão"),
    ("Seus pensamentos estão mais voltados para:", "Passado ou preocupação", "Futuro com possibilidades e gratidão")
]

if st.session_state.passo_quiz <= 6:
    st.progress(st.session_state.passo_quiz / 6)
    st.markdown(f"**Pergunta {st.session_state.passo_quiz}/6**")

    p, neg, pos = perguntas[st.session_state.passo_quiz - 1]
    st.markdown(f"<div class='pergunta'><h3>{p}</h3></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.markdown(f"<p style='text-align:right;'><strong>😴 {neg}</strong></p>", unsafe_allow_html=True)
    with col2:
        value = st.slider("", 1, 5, 3, key=f"s{st.session_state.passo_quiz}")
    with col3:
        st.markdown(f"<p style='text-align:left;'><strong>☀️ {pos}</strong></p>", unsafe_allow_html=True)

    if st.button("Próxima", key=f"n{st.session_state.passo_quiz}", width="stretch"):
        st.session_state.pontos_quiz += value
        st.session_state.passo_quiz += 1
        st.rerun()
else:
    total = st.session_state.pontos_quiz
    st.markdown("### ☀️ Seu Resultado!")

    if total <= 14:
        st.markdown("**🔻 Baixa vibração**")
        st.session_state.estado = "baixa_vibracao"
        frase = ("Sua frequência está baixa. Se você pretende se dedicar a atividades que exigem energia, "
                 "considere aumentar sua vibração. Caso contrário, está tudo bem.")
    elif total <= 22:
        st.markdown("**⚖️ Neutro**")
        st.session_state.estado = "neutro"
        frase = ("Sua frequência está estável. Se deseja mais foco ou criatividade, considere aumentar. "
                 "Se está confortável, pode manter.")
    else:
        st.markdown("**🌟 Alta vibração!**")
        st.session_state.estado = "alta_vibracao"
        frase = ("Sua frequência está alta! Ótimo para atividades físicas, criativas ou de alta performance. "
                 "Se quiser relaxar, considere reduzir.")

    st.markdown(f"<div class='resultado'><p>{frase}</p><p><strong>Total: {total}/30</strong></p></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Compartilhar"):
            url = f"https://web.whatsapp.com/send?text={urllib.parse.quote(frase)}"
            st.markdown(f"[WhatsApp]({url})")
    with col2:
        if st.button("Frequência"):
            st.switch_page("pages/_frequencia.py")
    with col3:
        if st.button("Refazer"):
            st.session_state.passo_quiz = 1
            st.session_state.pontos_quiz = 0
            st.rerun()

st.markdown("""
<div style="text-align:center;font-size:11px;color:#0a2d54;margin-top:60px;padding:15px;border-top:1px solid #77a8af;">
Projeto para o curso de Master PNL, elaborado em Novembro de 2025, por Carolina Nóbrega, Càtia Nyland, Emersonn Adolfato e Tanisé Brandão
</div>
""", unsafe_allow_html=True)