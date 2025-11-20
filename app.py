# python -m streamlit run app.py
import streamlit as st
from PIL import Image, ImageOps

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Para Meu Amor, Mari", 
    page_icon="💖",
    layout="centered" # Deixa o conteúdo centralizado, fica mais bonito
)

# --- SEÇÃO 1: ABERTURA E TEXTO PRINCIPAL ---
st.title("Oi, Meu Amor! ❤️")

st.write("""
Estava reelembrando como foi há 1 ano atrás... 
Lembrei do nervosismo, do planejamento, do Sol... Lembrei do seu sorriso lindo. 
Eu sou muito grato por ter você na minha vida, pode ter certeza que você é minha 
melhor escolha e a dupla perfeita para as próximas conquistas.
""")

st.write("""
Fico muito feliz por termos chegado até aqui juntos, eu te amo demais, amor da minha vida. 
Amo seus trejeitos, seu sorriso, sua inteligência, seu cheiro e suas falas.
""")

st.write("Pensei em fazer essa página para te mostrar o quanto você é especial para mim. Espero que goste! 💖")

# Foto de Capa (Açaí)
try:
    # Adicionei o use_column_width=True para a foto ajustar na tela do celular
    imagem_capa = Image.open("fotos/acai.jpg") 
    st.image(imagem_capa, caption="Nós <3", use_container_width=True) 
except FileNotFoundError:
    st.warning("⚠️ A imagem 'fotos/acai.jpg' não foi encontrada.")

st.divider() # Cria uma linha divisória visual elegante

# --- SEÇÃO 2: GALERIA DE MEMÓRIAS ---
st.header("Nossas Memórias Inesquecíveis 📸")
st.write("Aqui estão alguns dos nossos momentos...")

# Para as fotos ficarem lado a lado no PC e uma embaixo da outra no celular, 
# podemos usar colunas (opcional, mas fica bonito):
col1, col2 = st.columns(2)

with col1:
    try:
        foto1 = Image.open("foto1.jpg")
        st.image(foto1, caption="Lembra desse dia? Foi incrível!", use_container_width=True)
    except FileNotFoundError:
        st.info("Coloque a 'foto1.jpg' na pasta.")

with col2:
    try:
        foto2 = Image.open("foto2.jpg")
        st.image(foto2, caption="Sempre rindo juntos.", use_container_width=True)
    except FileNotFoundError:
        st.info("Coloque a 'foto2.jpg' na pasta.")

st.divider() # Outra linha divisória

# --- SEÇÃO 3: CARTA FINAL ---
st.header("De Coração Aberto... 💌")

# DICA: Substitua o texto abaixo pela sua carta real
st.write("""
Aqui você escreve o restante da sua carta para a Mari...

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

Cada parágrafo pode ser uma nova linha.

Com todo o meu amor,
[Seu Nome]
""")

# Um botãozinho final só de charme (não faz nada, só solta balões)
if st.button("Clique aqui para receber meu amor"):
    st.balloons()
    st.toast('Eu te amo muito! ❤️')