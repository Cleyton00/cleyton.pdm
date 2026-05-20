import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("2875404.png")
zap_base64 = get_base64_image("images (1).jpeg")

# =========================
# TOPO (imagem clicável)
# =========================
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="https://www.google.com" target="_blank">
                <img src="data:image/png;base64,{img_base64}" 
                     width="320" 
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# =========================
# LAYOUT PRINCIPAL
# =========================
col_left, col_right = st.columns([3,1])

with col_left:

    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Nome Cleyton Silva</b>
    </div>
    """, unsafe_allow_html=True)

    # subcolunas
    subcol1, subcol2 = st.columns([1,4])

    # IMAGEM
    with subcol1:
        st.image(
            "WhatsApp Image 2026-04-15 at 11.17.27 AM.png",
            width=250
        )

    # TEXTO
    with subcol2:
        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
        ">
            <b>Sobre Cleyton:</b><br><br>

            Olá, meu nome é Cleyton, sou da cidade de Gurinhém PB,
            tenho 18 anos e estou no terceiro ano do curso de
            Informática do IFPB Campus Itabaiana.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.link_button(
        "Acessar",
        "https://sites.google.com/academico.ifpb.edu.br/cleyton-alves-da-silva/in%C3%ADcio"
    )

with col_right:
    st.empty()

# ==================================================
# NOVA SEÇÃO - 3 LINKS COM IMAGENS
# ==================================================

st.markdown("""
    <hr style="margin-top:50px; margin-bottom:40px;">
    <h2 style='text-align:center;'>
        Meus Sites Favoritos
    </h2>
""", unsafe_allow_html=True)

link1, link2, link3 = st.columns(3)

# ================= LINK 1 =================
with link1:

    st.image("imagem1.png", width=250)

    st.markdown("""
        <div style="text-align:center; margin-top:10px;">
            <a href="https://site1.com" target="_blank">
                Clique para acessar o Site 1
            </a>
        </div>
    """, unsafe_allow_html=True)

# ================= LINK 2 =================
with link2:

    st.image("imagem2.png", width=250)

    st.markdown("""
        <div style="text-align:center; margin-top:10px;">
            <a href="https://site2.com" target="_blank">
                Clique para acessar o Site 2
            </a>
        </div>
    """, unsafe_allow_html=True)

# ================= LINK 3 =================
with link3:

    st.image("imagem3.png", width=250)

    st.markdown("""
        <div style="text-align:center; margin-top:10px;">
            <a href="https://site3.com" target="_blank">
                Clique para acessar o Site 3
            </a>
        </div>
    """, unsafe_allow_html=True)

# =========================
# WHATSAPP
# =========================
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://wa.me/5583987220076" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)
