import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from PIL import Image

# Título de la aplicación
st.title("Visualizador de datos CSV")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    # Leer el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv(uploaded_file)
    
    # Mostrar el DataFrame
    st.write(df)

lottie_coding = load_lottieurl("https://lottie.host/aa4d3448-0f1f-4030-a0b0-3f4f9e6ff0a1/wIUZV63gdS.json")
imagen_random = Image.open("https://www.metodobenozzi.com/wp-content/uploads/2022/12/Cuando-aparece-la-retinopatia-diabetica.jpg")

with st.container():
  st.subheader("Proyecto Final Machine Learning")
  st.title("Introducción a Machine Learning")
  st.write("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  st.write("[Ingrese aquí para más información](https://www.google.com/search?sca_esv=8b4a0b2f1f186285&q=retinopatia+diabetica&uds=ADvngMgFHG_01LTdfHIz9eKL6nE3j859i-msPDi-BHHMTzcmf58F_D4VMZdnrvvUbblvR4kVqgWzxEkQYzVTw484LYv2QC8Ti3LyXFHhcgW8ZPrSTrjt3szgiEqSHUoVMSC5fUp2zY8vNLomAfCIaDIyrxPScbb-5Q7togzdv8v5Yul5diyy9j71ZfsKSObEthRptwO0BEqcdoac_S6xmMwxBna_AA6B0SNw16K-AqHAljpNF6iwkaRyjJSzI6grmT8RneNH4TUVzwFVij0FsGmF_Nfg2EmETYp-bNF810ao6Ng3rs16TwIjagA20WcefKIcKA0BAhZ8sDobPLk7ePYotpNAy6P1Ew&udm=2&prmd=ivsnmbtz&sa=X&ved=2ahUKEwi78r6tyNSGAxX2pZUCHbjuAvYQtKgLegQICxAB&biw=767&bih=703&dpr=1.25#vhid=DQKpNF5IHdnmpM&vssid=mosaic)")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("Introducción")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do")
    st.write("[Youtube >](https://www.youtube.com)")
  
  with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
