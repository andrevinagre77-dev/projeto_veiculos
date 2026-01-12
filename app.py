import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo os dados
df = pd.read_csv('vehicles_us.csv')

# Título do Dashboard
st.header('Análise de Dados de Anúncios de Veículos')

# --- Secção 1: Histograma de Condição vs Ano do Modelo ---
st.write('### Histograma de Condição vs Ano do Modelo')
# Criando o gráfico igual à foto f2aecb.jpg
fig1 = px.histogram(df, x="model_year", color="condition", 
                   title="Distribuição da Condição pelo Ano do Modelo")
st.plotly_chart(fig1)

# --- Secção 2: Comparação de Preço entre Fabricantes ---
st.write('### Comparar Distribuição de Preço entre Fabricantes')

# Extrair o fabricante (primeira palavra do modelo)
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
list_manuf = sorted(df['manufacturer'].unique())

# Criar os seletores (como na foto f2b173.jpg)
col1, col2 = st.columns(2)
with col1:
    manuf_1 = st.selectbox('Selecionar fabricante 1', list_manuf, index=list_manuf.index('chevrolet'))
with col2:
    manuf_2 = st.selectbox('Selecionar fabricante 2', list_manuf, index=list_manuf.index('hyundai'))

# Filtrar dados para os dois fabricantes escolhidos
mask_filter = (df['manufacturer'] == manuf_1) | (df['manufacturer'] == manuf_2)
df_comp = df[mask_filter]

# Gráfico de Histograma Comparativo
fig2 = px.histogram(df_comp, x="price", color="manufacturer", 
                   barmode='overlay', 
                   title=f"Distribuição de Preço: {manuf_1} vs {manuf_2}")
st.plotly_chart(fig2)

# --- Secção 3: Tipos de Veículo por Fabricante ---
st.write('### Tipos de Veículo por Fabricante')
# Gráfico de barras empilhadas (como na foto f2ae8d.jpg)
fig3 = px.histogram(df, x="manufacturer", color="type", 
                   title="Tipos de Veículo por Fabricante")
st.plotly_chart(fig3)