import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Visualizador de datos CSV")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    # Leer el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv(uploaded_file)
    
    # Mostrar el DataFrame
    st.write(df)
