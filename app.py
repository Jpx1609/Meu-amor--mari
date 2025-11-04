import streamlit as st
from PIL import Image # Biblioteca para carregar imagens

# Configuração da página (opcional, mas legal)
st.set_page_config(page_title="Para Meu Amor", page_icon="💖")

# --- O MENU LATERAL ---
# O 'st.sidebar' cria um menu na lateral esquerda
st.sidebar.title("Nosso Cantinho 💖")
pagina_escolhida = st.sidebar.selectbox(
    "Escolha uma página:",
    ["Início", "Nossas Memórias", "Uma Carta para Você"]
)

# --- CONTEÚDO DA PÁGINA ---

if pagina_escolhida == "Início":
    # Página Inicial
    st.title("Bem-vinda, Meu Amor!")
    st.write("Este é um presentinho que fiz para você.")
    st.write("Espero que goste de relembrar nossos momentos.")
    
    # Tenta carregar uma foto de capa
    try:
        imagem_capa = Image.open("foto_capa.jpg") # Coloque uma foto principal aqui
        st.image(imagem_capa, caption="Nós <3")
    except FileNotFoundError:
        st.warning("Coloque uma 'foto_capa.jpg' na pasta do projeto.")

elif pagina_escolhida == "Nossas Memórias":
    # Página de Fotos
    st.header("Nossas Memórias Inesquecíveis")

    st.write("Aqui estão alguns dos nossos momentos...")

    # Foto 1
    try:
        foto1 = Image.open("foto1.jpg") # Coloque sua foto aqui
        st.image(foto1, caption="Lembra desse dia? Foi incrível!")
    except FileNotFoundError:
        st.error("Foto 'foto1.jpg' não encontrada.")

    st.write("---") # Linha divisória

    # Foto 2
    try:
        foto2 = Image.open("foto2.jpg") # Coloque outra foto aqui
        st.image(foto2, caption="Sempre rindo juntos.")
    except FileNotFoundError:
        st.error("Foto 'foto2.jpg' não encontrada.")

elif pagina_escolhida == "Uma Carta para Você":
    # Página de Texto
    st.header("De Coração Aberto...")
    
    st.write("""
    Aqui você pode escrever seu texto.
    
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat.
    
    Cada parágrafo pode ser uma nova linha.
    
    Com todo o meu amor,
    [Seu Nome]
    """)