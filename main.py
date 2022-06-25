import streamlit as st
import pandas as pd


st.title("Estou AQUI")

uploaded_file = st.file_uploader("carregue os dados")

dados = st.checkbox("ver dados")

if dados == True:
  df = pd.read_csv(uploaded_file)

  st.dataframe(df)

