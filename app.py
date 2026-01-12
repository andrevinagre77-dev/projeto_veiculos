import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Lendo os dados
df = pd.read_csv('vehicles_us.csv')

# Criar a coluna de fabricante (necessária para os gráficos)
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# 2. Título e Cabeçalho
st.header('Análise de Dados de Anúncios de Veículos')
st.write("Explore os dados e as tendências do mercado de veículos usados.")

# 3. --- NOVO: DATA VIEWER (O que faltava) ---
st.header('Visualizador de Dados')
# Caixa de seleção para mostrar os dados
show_data = st.checkbox('Incluir fabricantes com menos de 1000 anúncios', value=True)

if not show_data:
    # Filtrar fabricantes com muitos anúncios (como no vídeo)
    counts = df['manufacturer'].value_counts()
    df_filtered = df[df['manufacturer'].isin(counts[counts >= 1000].index)]
    st.write("Exibindo apenas fabricantes com mais de 1000 anúncios:")
    st.dataframe(df_filtered)
else:
    st.write("Exibindo todos os dados:")
    st.dataframe(df)

# 4. Gráfico de Histograma (Condição vs Ano)
st.write('### Histograma de Condição vs Ano do Modelo')
fig1 = px.histogram(df, x="model_year", color="condition", 
                   title="Distribuição da Condição pelo Ano do Modelo")
st.plotly_chart(fig1)

# 5. Comparação de Preço entre Fabricantes
st.write('### Comparar Distribuição de Preço entre Fabricantes')
list_manuf = sorted(df['manufacturer'].unique())

col1, col2 = st.columns(2)
with col1:
    manuf_1 = st.selectbox('Selecionar fabricante 1', list_manuf, index=list_manuf.index('chevrolet'))
with col2:
    manuf_2 = st.selectbox('Selecionar fabricante 2', list_manuf, index=list_manuf.index('hyundai'))

mask_filter = (df['manufacturer'] == manuf_1) | (df['manufacturer'] == manuf_2)
df_comp = df[mask_filter]

fig2 = px.histogram(df_comp, x="price", color="manufacturer", 
                   barmode='overlay', 
                   title=f"Distribuição de Preço: {manuf_1} vs {manuf_2}")
st.plotly_chart(fig2)

# 6. Gráfico de Tipos de Veículo por Fabricante
st.write('### Tipos de Veículo por Fabricante')
fig3 = px.histogram(df, x="manufacturer", color="type", 
                   title="Tipos de Veículo por Fabricante")
st.plotly_chart(fig3)