import streamlit as st
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/batistajoao54/portifolio-desenvolvendo/main/deposito.csv")

df_ordem = df.sort_values(by= ['marca']).copy()


st.set_page_config(layout= 'wide')

st.title("CONTROLE DE ESTOQUE")

lista = list(df_ordem['marca'].unique())

st.write(lista)
#st.dataframe(df)

#por alguma razao nao conseguir trazer a lista de outra forma
marca = st.selectbox("MARCA", ["",'arte_de_brincar', 'beatriz_moda_infantil',
                                'bem_me_quero','bene_confeccoes',
                                'derick_baby','dona_flor',
                                'exito','marbelle',
                                'monza_baby','rainha_do_norte',
                                'suprersa_baby','valentinna_kids'])


df_marca = df[df['marca'] == marca]
botao = st.button("PESQUISAR")

if marca == "":
    st.markdown("## ESCOLHA UMA MARCA")

if marca != "":
    st.dataframe(df_marca, height=600)


