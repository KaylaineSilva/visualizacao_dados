
import pandas as pd
import streamlit as st

def q1(df):
    df = df.copy()

    # Converter a coluna data
    df['data'] = pd.to_datetime(df['data'])

    # Extrair o ano
    df['ano'] = df['data'].dt.year

    anos = sorted(df['ano'].unique())

    # Filtro interativo
    anos_selecionados = st.multiselect(
        "Selecione os anos:",
        options=anos,
        default=anos,
        key="anos_q1"
    )

    df_filtrado = df[df['ano'].isin(anos_selecionados)]

    return df_filtrado


def q2(df):
    df = df.copy()

    # Converter a coluna data
    df['data'] = pd.to_datetime(df['data'])

    # Extrair ano e mês
    df['ano'] = df['data'].dt.year
    df['mes'] = df['data'].dt.month

    anos = sorted(df['ano'].unique())

    # Filtro interativo para comparar anos
    anos_selecionados = st.multiselect(
        "Selecione os anos para comparar:",
        options=anos,
        default=anos,
        key="anos_q2"
    )

    df_filtrado = df[df['ano'].isin(anos_selecionados)]

    return df_filtrado
