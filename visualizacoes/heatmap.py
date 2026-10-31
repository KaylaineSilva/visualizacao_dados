
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
        .reindex(columns=["evento", "palestra", "evento_externo"], fill_value=0)
    )

    # Garantir todos os meses e áreas, mesmo sem registros
    indice = pd.MultiIndex.from_product(
        [areas, range(1, 13)],
        names=["area", "mes"]
    )

    contagem = contagem.reindex(indice, fill_value=0)
    contagem["total"] = (
        contagem["evento"] + contagem["palestra"] + contagem["evento_externo"]
    )

    #matrizes para o hover
    total = contagem["total"].to_numpy().reshape(len(areas), 12)
    eventos = contagem["evento"].to_numpy().reshape(len(areas), 12)
    palestras = contagem["palestra"].to_numpy().reshape(len(areas), 12)
    externos = contagem["evento_externo"].to_numpy().reshape(len(areas), 12)

    customdata = [
        [
            [
                int(eventos[i, j]),
                int(palestras[i, j]),
                int(externos[i, j])
            ]
            for j in range(12)
        ]
        for i in range(len(areas))
    ]

    fig = go.Figure(
        data=go.Heatmap(
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
                "Eventos externos: %{customdata[2]}<br>"
                "<b>Total: %{z}</b>"
                "<extra></extra>"
            ),
            xgap=3,
            ygap=3
        )
    )

    # Cor do texto de acordo com a intensidade da célula
    valor_maximo = total.max()

    for i, area in enumerate(areas):
        for j, mes in enumerate(MESES):
            valor = int(total[i, j])

            # Valores baixos têm fundo claro -> texto preto
            # Valores altos têm fundo escuro -> texto branco
            proporcao = valor / valor_maximo if valor_maximo > 0 else 0

            cor_texto = "#000000" if proporcao < 0.5 else "#FFFFFF"

            fig.add_annotation(
                x=mes,
                y=area,
                text=str(valor),
                showarrow=False,
                font=dict(
                    color=cor_texto,
                    size=14
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
