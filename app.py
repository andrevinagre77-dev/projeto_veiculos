import streamlit as st
import pandas as pd
import plotly_express as px

# Configuração da página
st.set_page_config(page_title="Car Sales Dashboard", layout="wide")

st.header('Análise de Anúncios de Veículos')

# Função para carregar e limpar (mesma lógica do EDA)
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
    df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
    df['odometer'] = df.groupby('model_year')['odometer'].transform(lambda x: x.fillna(x.median()))
    return df.dropna(subset=['model_year', 'odometer'])

df = load_data()

# 1. Tabela de Dados (Como no vídeo)
st.subheader('Explorar Base de Dados')
st.dataframe(df, use_container_width=True)

# 2. Seção de Gráficos com Checkboxes
st.subheader('Análise Visual')

# Checkbox para Histograma
build_histogram = st.checkbox('Criar histograma de anos dos modelos')
if build_histogram:
    st.write('Criando um histograma para a coluna model_year')
    fig = px.histogram(df, x="model_year", color="condition")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para Gráfico de Dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão Preço vs KM')
if build_scatter:
    st.write('Analisando a relação entre preço e quilometragem')
    fig_scatter = px.scatter(df, x="odometer", y="price", color="type", opacity=0.5)
    st.plotly_chart(fig_scatter, use_container_width=True)