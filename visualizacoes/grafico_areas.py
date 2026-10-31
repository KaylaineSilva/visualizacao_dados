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
    "Matemática e Estatística": "#CDB4DB",
    "Geral / Outros": "#B8BEC8",
    "Inteligência Artificial e Ciência de Dados": "#A8DADC",
    "Computação e Tecnologia": "#A9C5F5",
    "Educação e Licenciatura": "#B9DDAA",
    "Institucional, Cultura e Sociedade": "#FFCAD4",
    "Inovação, Negócios e Carreira": "#FFE5B4"
}

def grafico_areas(df):
    contagem = (
        df.groupby(["area", "tipo"])
        .size()
        .unstack(fill_value=0)
        .reindex(
            columns=["evento", "palestra", "evento_externo"],
            fill_value=0
        )
        .reset_index()
    )

    contagem["total"] = (
        contagem["evento"] + contagem["palestra"] + contagem["evento_externo"]
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
        custom_data=["evento", "palestra", "evento_externo"],
        title="Distribuição de acontecimentos por área temática"
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br><br>"
            "Eventos: %{customdata[0]}<br>"
            "Palestras: %{customdata[1]}<br>"
            "Eventos externos: %{customdata[2]}<br>"
            "<b>Total: %{y}</b>"
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
        title_y=1,
        bargap=0.35,
        xaxis_title=None,
        yaxis_title="Quantidade de acontecimentos",
        hoverlabel=dict(
            bgcolor="#1E1E1E",
            font_color="#FFFFFF",
            bordercolor="#CDB4DB"
        ),
        width=1200,    
        height=650,    
        margin=dict(
            l=40,
            r=40,
            t=60,
            b=130
        )
    )

    return fig
