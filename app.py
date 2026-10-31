
import pandas as pd
import streamlit as st

from visualizacoes.grafico_areas import grafico_areas
from visualizacoes.grafico_temporal import grafico_temporal
from visualizacoes.heatmap import heatmap_areas_meses

from funcoes import q1, q2, q3

st.title("Acontece no ICMC: eventos e palestras")

st.markdown("""
O **Acontece no ICMC** é um projeto de visualização de dados
que busca explorar a distribuição dos eventos e palestras
divulgados pelo ICMC-USP ao longo do tempo.

A análise utiliza dados extraídos de e-mails de divulgação
coletados entre **26 de abril de 2021 e 26 de outubro de 2026**,
permitindo investigar quais áreas temáticas concentram mais
acontecimentos, identificar padrões temporais e comparar
a programação de diferentes anos.

Explore os gráficos abaixo utilizando os filtros interativos.
""")

# Carregar os dados
df = pd.read_csv("dados/reais/eventos.csv")

# Q1 - Distribuição por área
st.subheader("Q1 - Distribuição dos acontecimentos por área")

df_q1 = q1(df)
fig1 = grafico_areas(df_q1)

st.plotly_chart(fig1, width="stretch")

# Q2 - Distribuição temporal
st.subheader("Q2 - Distribuição temporal dos acontecimentos")

df_q2 = q2(df)
fig2 = grafico_temporal(df_q2)

st.plotly_chart(fig2, width="stretch")

#Q3 - Heatmap de acontecimentos por área e mês
st.header("Q3 - Distribuição temporal por área temática")
df_q3 = q3(df)
fig3 = heatmap_areas_meses(df_q3)

st.plotly_chart(fig3, width="stretch")