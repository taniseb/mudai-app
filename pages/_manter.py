import streamlit as st

st.set_page_config(page_title="Mudaí - Aumentar", page_icon="arrow_upward")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    h1, h2, h3 { font-weight: 600 !important; text-align: center !important; color: #0a2d54 !important; }

    .main, .block-container { background-color: #fdf2e0 !important; }
    section[data-testid="stAppViewContainer"], [data-testid="stDecoration"] { background: #fdf2e0 !important; }

    .sub-pagina {
        background-color: #ffcaa8 !important;
        border: 2px solid #77a8af !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 20px 0 !important;
        text-align: center !important;
    }
</style>
""", unsafe_allow_html=True)

st.image("Mudai.png", width=360, use_container_width=True)
st.markdown("<h2>Manter a Frequência</h2>", unsafe_allow_html=True)

# IMAGEM
# VÍDEO MP4 (NÃO IMAGEM!)
st.video("manter.mp4", autoplay=True, muted=True, loop=True)

# TEXTO
st.markdown("""
<div class="sub-pagina">
<p><strong>Texto:</strong> Sua frequência está sendo mantida. Ideal para atividades de energia média.</p>
<p><strong>Dinâmica:</strong> Respire profundamente e visualize sua energia se mantendo, de forma uniforme e constante.</p>
</div>
""", unsafe_allow_html=True)

# ÁUDIO (só se existir)
st.audio("manter.ogg", format="audio/ogg")

col1, col2 = st.columns(2)
with col1:
    if st.button("Voltar"):
        st.switch_page("pages/_frequencia.py")
with col2:
    if st.button("Início"):
        st.switch_page("app.py")