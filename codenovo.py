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
# SEÇÃO - SITES PARCEIROS
# ==================================================
st.markdown("""
    <hr style="margin-top:50px; margin-bottom:30px;">

    <h2 style='
        text-align:center;
        font-size:38px;
        color:#333;
        margin-bottom:40px;
    '>
        Sites Parceiros
    </h2>
""", unsafe_allow_html=True)

link1, link2, link3 = st.columns(3)

# ================= LINK 1 =================
with link1:

    st.markdown("""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{}"
                 style="
                    width:250px;
                    height:180px;
                    object-fit:cover;
                    border-radius:12px;
                 ">
        </div>
    """.format(get_base64_image("image_ifood.png")),
    unsafe_allow_html=True)

    st.markdown("""
        <h3 style="text-align:center; margin-top:15px;">
            iFood
        </h3>

        <p style="
            text-align:justify;
            font-size:16px;
            line-height:1.6;
        ">
            O iFood é uma plataforma de delivery que conecta
            restaurantes, mercados e consumidores, permitindo
            pedidos online de forma rápida e prática.
        </p>

        <div style="text-align:center; margin-top:15px;">
            <a href="https://portal.ifood.com.br/login"
               target="_blank"
               style="
                    font-size:20px;
                    text-decoration:none;
                    font-weight:bold;
               ">
                Acessar iFood
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= LINK 2 =================
with link2:

    st.markdown("""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{}"
                 style="
                    width:250px;
                    height:180px;
                    object-fit:cover;
                    border-radius:12px;
                 ">
        </div>
    """.format(get_base64_image("image_facebook.jpg")),
    unsafe_allow_html=True)

    st.markdown("""
        <h3 style="text-align:center; margin-top:15px;">
            Facebook
        </h3>

        <p style="
            text-align:justify;
            font-size:16px;
            line-height:1.6;
        ">
            O Facebook é uma rede social utilizada para compartilhar
            fotos, vídeos, notícias e interagir com pessoas do mundo todo.
        </p>

        <div style="text-align:center; margin-top:15px;">
            <a href="https://www.facebook.com/?locale=pt_BR"
               target="_blank"
               style="
                    font-size:20px;
                    text-decoration:none;
                    font-weight:bold;
               ">
                Acessar Facebook
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= LINK 3 =================
with link3:


    st.markdown("""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{}"
                 style="
                    width:250px;
                    height:180px;
                    object-fit:cover;
                    border-radius:12px;
                 ">
        </div>
    """.format(get_base64_image("image_netflix.jpg")),
    unsafe_allow_html=True)

    st.markdown("""
        <h3 style="text-align:center; margin-top:15px;">
            Netflix
        </h3>

        <p style="
            text-align:justify;
            font-size:16px;
            line-height:1.6;
        ">
            A Netflix é uma plataforma de streaming que oferece
            filmes, séries, documentários e conteúdos exclusivos
            para entretenimento online.
        </p>

        <div style="text-align:center; margin-top:15px;">
            <a href="https://www.netflix.com/br/"
               target="_blank"
               style="
                    font-size:20px;
                    text-decoration:none;
                    font-weight:bold;
               ">
                Acessar Netflix
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

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
