
import pandas as pd
import plotly.express as px


cores_anos = {
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
        'eventos': 'Eventos',
        'palestra': 'Palestras',
        'palestras': 'Palestras'
    })

    # Contar acontecimentos por ano, mês e tipo
    contagem = (
        df.groupby(['ano', 'mes', 'tipo'])
        .size()
        .unstack(fill_value=0)
    )

    # Garantir que as colunas existam
    contagem = contagem.reindex(
        columns=['Eventos', 'Palestras'],
        fill_value=0
    )

    # Total de acontecimentos
    contagem['total'] = (
        contagem['Eventos'] + contagem['Palestras']
    )

    contagem = contagem.reset_index()

    # Converter ano para categoria
    contagem['ano'] = contagem['ano'].astype(str)

    # Criar gráfico de linhas
    fig = px.line(
        contagem,
        x='mes',
        y='total',
        color='ano',
        markers=True,
        custom_data=['Eventos', 'Palestras'],
        title='Distribuição mensal de acontecimentos',
        labels={
            'mes': 'Mês',
            'total': 'Quantidade de acontecimentos',
            'ano': 'Ano'
        },
        color_discrete_map=cores_anos,
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
        hovertemplate=(
            '<b>Ano: %{fullData.name}</b><br>'
            'Mês: %{x}<br>'
            'Total: %{y} acontecimentos<br>'
            'Eventos: %{customdata[0]}<br>'
            'Palestras: %{customdata[1]}'
            '<extra></extra>'
        )
    )

    return fig
