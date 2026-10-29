
import pandas as pd
import streamlit as st

from visualizacoes.grafico_areas import grafico_areas
from visualizacoes.grafico_temporal import grafico_temporal
from funcoes import q1, q2

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
