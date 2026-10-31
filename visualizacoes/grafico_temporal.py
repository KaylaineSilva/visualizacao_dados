
import pandas as pd
import plotly.express as px


cores_anos = {
    "2021": "#FFCAD4",
    "2022": "#142A98",
    "2023": "#800020",
    "2024": "#B8860B",
    "2025": "#4BD2D4",
    "2026": "#6617D4"
}


def grafico_temporal(df):
    df = df.copy()

    # Padronizar as categorias
    df['tipo'] = df['tipo'].str.strip().str.lower()

    df['tipo'] = df['tipo'].replace({
        'evento': 'Eventos',
        'palestra': 'Palestras',
        'evento_externo': 'Eventos externos'
    })

    # Contar acontecimentos por ano, mês e tipo
    contagem = (
        df.groupby(['ano', 'mes', 'tipo'])
        .size()
        .unstack(fill_value=0)
    )

    # Garantir que todas as categorias existam
    contagem = contagem.reindex(
        columns=[
            'Eventos',
            'Palestras',
            'Eventos externos'
        ],
        fill_value=0
    )

    # Calcular o total
    contagem['total'] = (
        contagem['Eventos']
        + contagem['Palestras']
        + contagem['Eventos externos']
    )

    contagem = contagem.reset_index()

    # Garantir todos os meses para os anos selecionados
    anos = sorted(df['ano'].dropna().unique())

    indice = pd.MultiIndex.from_product(
        [anos, range(1, 13)],
        names=['ano', 'mes']
    )

    contagem = (
        contagem.set_index(['ano', 'mes'])
        .reindex(indice, fill_value=0)
        .reset_index()
    )

    # Converter ano para categoria
    contagem['ano'] = contagem['ano'].astype(str)

    # Criar gráfico de linhas
    fig = px.line(
        contagem,
        x='mes',
        y='total',
        color='ano',
        markers=True,
        custom_data=[
            'Eventos',
            'Palestras',
            'Eventos externos'
        ],
        title='Distribuição mensal de acontecimentos',
        labels={
            'mes': 'Mês',
            'total': 'Quantidade de acontecimentos',
            'ano': 'Ano'
        },
        color_discrete_map=cores_anos
    )

    fig.update_xaxes(
        tickmode='array',
        tickvals=list(range(1, 13)),
        ticktext=[
            'Jan', 'Fev', 'Mar', 'Abr',
            'Mai', 'Jun', 'Jul', 'Ago',
            'Set', 'Out', 'Nov', 'Dez'
        ]
    )

    fig.update_yaxes(rangemode='tozero')

    fig.update_traces(
        line=dict(width=2),
        marker=dict(size=5),
        hovertemplate=(
            "<b>%{fullData.name}</b>: %{y} acontecimentos"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#1E1E1E",
            font_color="#FFFFFF",
            font_size=12
        )
    )

    return fig
