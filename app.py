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
st.title("Oi, Meu Amor! ")

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

st.write("Pensei em fazer essa página para guardar os nossos momentos especiais. Espero que goste! 💖")
st.divider() # Cria uma linha divisória visual elegante

# --- SEÇÃO 2: GALERIA DE MEMÓRIAS ---
st.header("Nossa história em fotos📸")


# Para as fotos ficarem lado a lado no PC e uma embaixo da outra no celular, 
# podemos usar colunas (opcional, mas fica bonito):
col1, col2 = st.columns(2)

with col1:
    try:
        foto1 = Image.open("fotos/dozeCort.jpg")
        st.image(foto1, caption="Doze Ginkeria Agradece!", use_container_width=True)
        foto3 = Image.open("fotos/linda_ham.jpg")
        st.image(foto3, caption="Bonitinha no dia das crianças, a gente conseguiu pegar o uber com 1% de bateria", use_container_width=True)
        foto5 = Image.open("fotos/namoro.jpg")
        foto5 = ImageOps.exif_transpose(foto5)  
        st.image(foto5, caption="Aqui o Sol abriu", use_container_width=True)
        foto7 = Image.open("fotos/poster.jpg")
        foto7 = ImageOps.exif_transpose(foto7)
        st.image(foto7, caption="Para de me olhar assim cara", use_container_width=True)
        foto9 = Image.open("fotos/lindosjuntos.jpg")
        st.image(foto9, caption="Bonitos juntos", use_container_width=True)
        foto11 = Image.open("fotos/flamengo.jpg")
        foto11 = ImageOps.exif_transpose(foto11)
        st.image(foto11, caption="Você será Flamengo...", use_container_width=True)
        foto13 = Image.open("fotos/protecaodetela.jpg")
        foto13 = ImageOps.exif_transpose(foto13)
        st.image(foto13, caption="Achei mt engraçado quando vc viu essa foto como proteção de tela", use_container_width=True)
        
    except FileNotFoundError:
        st.info("Coloque a 'foto1.jpg' na pasta.")

with col2:
    try:
        foto2 = Image.open("fotos/insta_primeiraft.jpg")
        st.image(foto2, caption="Aqui foi quando eu fiquei abobado, gosto desse print inteiro", use_container_width=True)
        foto4 = Image.open("fotos/fest_kauan.jpg")
        st.image(foto4, caption="Olha eles de casalzinho", use_container_width=True)
        foto6 = Image.open("fotos/pics.jpg")
        foto6 = ImageOps.exif_transpose(foto6)  
        st.image(foto6, caption="Meio que essa página é tipo isso", use_container_width=True)
        foto8 = Image.open("fotos/lindadnv.jpg")
        foto8 = ImageOps.exif_transpose(foto8) 
        st.image(foto8, caption="Minha Linda", use_container_width=True)
        foto10 = Image.open("fotos/vidaleve.jpg")
        foto10 = ImageOps.exif_transpose(foto10) 
        st.image(foto10, caption="Vidinha boa", use_container_width=True)
    except FileNotFoundError:
        st.info("Coloque a 'foto2.jpg' na pasta.")

st.divider() # Outra linha divisória

st.header("TE AMOOO MUITO!!! ❤️❤️❤️ ")



if st.button("Clique aqui para receber meu amor"):
    st.balloons()
    st.toast('Eu te amo muito! ❤️')