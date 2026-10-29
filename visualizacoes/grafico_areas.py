# Quais áreas temáticas concentram o maior número de eventos?
'''
Para construir a visualização para esta pergunta são feitas três operações
1) Agrupa os eventos de acordo com a área temática.
2) Conta quantos eventos existem em cada área.
3) Constrói um gráfico de barras interativo com Plotly.
''' 

import pandas as pd
import plotly.express as px

def grafico_areas(df):
    contagem = (
        df.groupby("area")
        .size()
        .reset_index(name="quantidade")
        .sort_values("quantidade", ascending=False)
    )

    fig = px.bar(
        contagem,
        x="area",
        y="quantidade",
        title="Quantidade de eventos por área",
        labels={
            "area": "Área temática",
            "quantidade": "Número de eventos"
        }
    )

    return fig
