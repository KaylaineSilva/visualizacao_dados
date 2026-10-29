import pandas as pd
import streamlit as st

from visualizacoes.grafico_areas import grafico_areas

st.title("Eventos Acadêmicos e Culturais do ICMC")

df = pd.read_csv("dados/sintetico/eventos_exemplo.csv")

st.subheader("Distribuição dos eventos por área")

fig = grafico_areas(df)

st.plotly_chart(fig, width="stretch")
