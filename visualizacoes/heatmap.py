
import pandas as pd
import plotly.graph_objects as go

MESES = [
    "Jan", "Fev", "Mar", "Abr",
    "Mai", "Jun", "Jul", "Ago",
    "Set", "Out", "Nov", "Dez"
]


def heatmap_areas_meses(df):
    df = df.copy()
    df["data"] = pd.to_datetime(df["data"])
    df["mes"] = df["data"].dt.month

    areas = sorted(df["area"].dropna().unique().tolist())

    # Contar os acontecimentos por área, mês e tipo
    contagem = (
        df.groupby(["area", "mes", "tipo"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=["Evento", "Palestra"], fill_value=0)
    )

    # Garantir todos os meses e áreas, mesmo sem registros
    indice = pd.MultiIndex.from_product(
        [areas, range(1, 13)],
        names=["area", "mes"]
    )

    contagem = contagem.reindex(indice, fill_value=0)
    contagem["total"] = (
        contagem["Evento"] + contagem["Palestra"]
    )

    # Matrizes para o heatmap e o hover
    total = contagem["total"].to_numpy().reshape(len(areas), 12)
    eventos = contagem["Evento"].to_numpy().reshape(len(areas), 12)
    palestras = contagem["Palestra"].to_numpy().reshape(len(areas), 12)

    customdata = [
        [
            [int(eventos[i, j]), int(palestras[i, j])]
            for j in range(12)
        ]
        for i in range(len(areas))
    ]

    fig = go.Figure(
        data=go.Heatmap(
            text=total,
            texttemplate="%{text}",
            textfont=dict(
                size=14,
                color="#FFFFFF"
            ),
            z=total,
            x=MESES,
            y=areas,
            customdata=customdata,
            colorscale=[
                [0, "#DFC8EE"],
                [0.25, "#AD8CC6"],
                [0.5, "#795A94"],
                [0.75, "#49355F"],
                [1, "#211A30"]
            ],
            colorbar=dict(
                title=dict(text="Quantidade")
            ),
            hovertemplate=(
                "<b>%{y} — %{x}</b><br><br>"
                "Eventos: %{customdata[0]}<br>"
                "Palestras: %{customdata[1]}<br>"
                "Total: %{z}"
                "<extra></extra>"
            ),
            xgap=3,
            ygap=3
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#000000",
        plot_bgcolor="#000000",
        font_color="#FFFFFF",

        xaxis_title="Mês",
        yaxis_title="Área temática",

        yaxis=dict(autorange="reversed"),

        height=350,
        autosize=True,

        margin=dict(l=10, r=10, t=20, b=40)
    )

    return fig
