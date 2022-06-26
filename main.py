#importando as bibliotecas que iremos usar para essa versão
import streamlit as st
import pandas as pd

#---------------------------------------------------------------------------

#configurando a pagina para que ela se auto preenchar na tela
st.set_page_config(layout='wide')

#--------------------------------------------------------------------------

#criando componentes do titulo e do carregamento de dados
col_titulo, col_dados = st.columns([2,1])

with col_titulo:
  st.title("Controle de distribuição de sacolas")

with col_dados:
  dados = st.file_uploader("Add dados")
#-----------------------------------------------------------------------------

#configurando os modos de pesquisas
pesquisa = st.radio('MODO DA PESQUISA', ('','NOME','MARCA','OS'))

#-------------------------------------------------------------------------------

#configurando as pesquisas por Nome
if pesquisa == "NOME":
  col_nome,col_marca,col_os = st.columns(3)
  df = pd.read_csv(dados)

  lista_nome = list(df['pessoa'].unique())
  lista_nome.insert(0,'')
  with col_nome:
    nome = st.selectbox("Nome",lista_nome)
    df_nome = df[df['pessoa'] == nome]


  lista_marca = list(df_nome['marca'].unique())
  #lista_marca.insert(0, '')
  with col_marca:
    marca = st.selectbox('MARCA',lista_marca)
    df_marca = df_nome[df_nome['marca'] == marca]


  lista_os = list(df_marca['os'].unique())
  #lista_os.insert(0, '')
  with col_os:
    os = st.selectbox('OS',lista_os)
    df_os = df_marca[df_marca['os'] == os]

  st.table(df_os)



#---------------------------------------------------------------------------------


#df = pd.read_csv(dados)
#st.table(df)





