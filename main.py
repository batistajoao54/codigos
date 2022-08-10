#importando as bibliotecas que iremos usar para essa versão
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

#---------------------------------------------------------------------------

#configurando a pagina para que ela se auto preenchar na tela
st.set_page_config(layout='wide')

#--------------------------------------------------------------------------

#criando componentes do titulo e dos graficos
col_titulo, col_graficos = st.columns([1,1])

df_clientes = pd.read_csv('clientes.csv')
df_cidades = pd.read_csv('cidade.csv')
df_estado = df_clientes.groupby('ESTADO').count().reset_index()


with col_titulo:
  st.markdown("### CLIENTES/CIDADES")

  #separando os clientes

  lista_clientes = list(df_clientes['LOJA'].unique())
  lista_clientes.insert(0," ")

  pesquisa = st.selectbox("NOME DO CLIENTE",lista_clientes)

  df_pesquisa = df_clientes[df_clientes['LOJA'] == pesquisa]

  if pesquisa == ' ':
    st.markdown("##### Faça uma pesquisa")

  else:
    fig2 = ff.create_table(df_pesquisa,height_constant=10)
    st.plotly_chart(fig2,use_container_width=True)

#-----------------------------------------------------------------------------

#preenchendo os graficos
with col_graficos:
  st.markdown('### CLIENTES POR ESTADO')

  fig = px.bar(df_estado, x='ESTADO', y='LOJA', color='ESTADO', text_auto=True, )
  fig.update_xaxes(title='ESTADOS COM CLIENTES')
  fig.update_yaxes(title='QUANTIDADE DE CLIENTES')
  st.plotly_chart(fig,use_container_width=True)

#criando um grafico de mapa
butao = st.checkbox('MOSTRAR GRAFICO DE BARRA')

if butao == False:
  st.markdown("##### CLIENTES PELO BRASIL")

  fig_map = px.scatter_mapbox(
    df_cidades,
    lat='LAT',
    lon='LONG',
    hover_name='CIDADE',
    #hover_date=["ESTADO","CIDADE"],
    size='LOJA',
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=45,
    zoom=5.45,

  )

  fig_map.update_layout(mapbox_style='open-street-map')

  fig_map.update_layout(
    height=400,
    margin={
      'r': 0,
      't': 0,
      'l': 0,
      'b': 0
    }
  )

  st.plotly_chart(fig_map,use_container_width=True)

else:
  fig_barra = px.bar(df_cidades, x='CIDADE', y='LOJA', color='ESTADO', text_auto=True, )
  fig_barra.update_xaxes(title='CIDADES')
  fig_barra.update_yaxes(title='QUANTIDADE DE CLIENTES')

  st.plotly_chart(fig_barra,use_container_width=True)
