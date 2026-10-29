# Quais áreas temáticas concentram o maior número de eventos?
'''
Para construir a visualização para esta pergunta são feitas três operações
1) Agrupa os eventos de acordo com a área temática.
2) Conta quantos eventos existem em cada área.
3) Constrói um gráfico de barras interativo com Plotly.
''' 

import pandas as pd
import plotly.express as px

CORES_AREAS = {
    "Computação": "#A8DADC",
    "Matemática": "#CDB4DB",
    "Estatística": "#FFCAD4",
    "Cultura": "#FFE5B4"
}

def grafico_areas(df):
    contagem = df.pivot_table(
        index="area",
        columns="tipo",
        values="id",
        aggfunc="count",
        fill_value=0
    ).reindex(
        columns=["Evento", "Palestra"],
        fill_value=0
    ).reset_index()

    contagem["total"] = (
        contagem["Evento"] + contagem["Palestra"]
    )

    contagem = contagem.sort_values(
        "total",
        ascending=False
    )

    fig = px.bar(
        contagem,
        x="area",
        y="total",
        color="area",
        color_discrete_map=CORES_AREAS,
        text="total",
        custom_data=["Evento", "Palestra"],
        title="Distribuição de acontecimentos por área temática"
    )

    fig.update_traces(
        textposition="outside",
        marker_line_width=0,
        hovertemplate=(
            "<b>%{x}</b><br><br>"
            "Eventos: %{customdata[0]}<br>"
            "Palestras: %{customdata[1]}<br>"
            "Total: %{y}"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#000000",
        plot_bgcolor="#000000",
        font_color="#FFFFFF",
        showlegend=False,
        title_x=0.0,
        title_y=0.95,
        bargap=0.35,
        xaxis_title=None,
        yaxis_title="Quantidade de acontecimentos",
        hoverlabel=dict(
            bgcolor="#1E1E1E",
            font_color="#FFFFFF",
            bordercolor="#CDB4DB"
        )
    )

    return fig
