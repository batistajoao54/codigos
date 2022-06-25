import streamlit as st
import pandas as pd


st.title("Estou AQUI")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file != "":
  df = pd.read_csv(uploaded_file)

  st.dataframe(df)

else:
  st.write("carregue um arquivo")

