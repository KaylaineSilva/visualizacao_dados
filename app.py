
import pandas as pd
import streamlit as st

from visualizacoes.grafico_areas import grafico_areas
from visualizacoes.grafico_temporal import grafico_temporal
from visualizacoes.heatmap import heatmap_areas_meses

from funcoes import q1, q2, q3

st.title("Acontece no ICMC: eventos e palestras")

# Carregar os dados
df = pd.read_csv("dados/sintetico/eventos_exemplo.csv")

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
