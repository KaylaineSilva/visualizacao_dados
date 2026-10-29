# Acontece no ICMC: Eventos e Palestras

## Sobre o projeto

Este projeto está sendo desenvolvido para a disciplina de **Visualização Computacional (SCC0252)**, do Instituto de Ciências Matemáticas e de Computação da Universidade de São Paulo (ICMC-USP).

A proposta é explorar os eventos e palestras divulgados pelo ICMC, buscando entender como essas atividades se distribuem entre diferentes áreas temáticas e ao longo do tempo.

Por meio de visualizações interativas, queremos identificar padrões na programação de acontecimentos, observar quais áreas concentram mais atividades e investigar como essa distribuição varia entre meses e anos.

## Questões de investigação

O projeto está organizado em torno de três perguntas principais:

**Q1 — Quais áreas temáticas concentram a maior quantidade de acontecimentos?**

A primeira questão busca identificar quais áreas possuem mais eventos e palestras. Para isso, utilizamos um gráfico de barras que apresenta a quantidade total de acontecimentos por área.

O gráfico permite selecionar múltiplos anos, facilitando a análise de diferentes períodos. Cada área possui uma cor própria, e, ao passar o mouse sobre uma barra, é possível visualizar separadamente as quantidades de eventos e palestras, além do total.

**Q2 — Em quais períodos do ano ocorrem mais acontecimentos?**

A segunda questão investiga a distribuição temporal dos acontecimentos, procurando identificar meses com maior ou menor concentração de atividades.

Utilizamos um gráfico de linhas que apresenta a quantidade de acontecimentos por mês. É possível selecionar diferentes anos para comparar suas distribuições e observar possíveis padrões ao longo do tempo.

**Q3 — Como a distribuição dos acontecimentos por área temática varia ao longo dos meses e anos?**

A terceira questão combina as dimensões exploradas anteriormente, permitindo analisar a distribuição mensal dos acontecimentos em cada área temática.

Para isso, utilizamos um mapa de calor (*heatmap*), no qual as linhas representam as áreas, as colunas representam os meses e a intensidade da cor indica a quantidade de acontecimentos.

O usuário pode selecionar o ano que deseja analisar. Além disso, cada célula apresenta a quantidade total de acontecimentos, e o recurso de passar o mouse permite consultar a quantidade de eventos e palestras separadamente.

## Conjunto de dados

Nesta etapa inicial, estamos utilizando **dados sintéticos** para desenvolver e testar as visualizações antes da coleta dos dados reais.

O conjunto de teste contém 1.300 registros fictícios, distribuídos entre 2022 e 2026, considerando inicialmente quatro áreas temáticas: Computação, Matemática, Estatística e Cultura.

Cada registro possui os seguintes atributos:

| Atributo | Descrição |
|---|---|
| `id` | Identificador do acontecimento |
| `titulo` | Título do evento ou palestra |
| `data` | Data de realização |
| `area` | Área temática |
| `tipo` | Classificação como Evento ou Palestra |

Os dados sintéticos são gerados pelo script `gerar_dados.py` e armazenados em um arquivo CSV.

Posteriormente, esses registros serão substituídos por dados reais coletados das páginas de divulgação de eventos e palestras do ICMC. Também será necessário padronizar as áreas temáticas e tratar possíveis inconsistências encontradas durante a coleta.

## Tecnologias utilizadas

O projeto está sendo desenvolvido em Python, utilizando as seguintes bibliotecas:

- **Pandas:** leitura, organização, filtragem e agrupamento dos dados.
- **Plotly:** construção dos gráficos interativos.
- **Streamlit:** desenvolvimento da interface e implementação dos filtros.

As visualizações seguem uma identidade visual baseada em fundo escuro e cores pastéis. Além da aparência, buscamos manter os gráficos simples e permitir que o usuário explore informações adicionais por meio das interações.

## Organização do código

O código foi separado para facilitar a manutenção e a inclusão de novas visualizações.

O arquivo `app.py` é responsável por montar a interface e apresentar os gráficos. O arquivo `funcoes.py` concentra as funções utilizadas para preparar e filtrar os dados de cada questão.

As implementações dos gráficos ficam no diretório `visualizacoes`, enquanto os dados de teste e o script responsável por gerá-los ficam em `dados/sintetico`.

Essa separação permite modificar uma visualização sem precisar alterar toda a aplicação.

## Como executar

Primeiro, crie e ative um ambiente virtual na raiz do projeto:

```bash
python -m venv .venv
source .venv/bin/activate
```

Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

Para iniciar a aplicação, execute:

```bash
streamlit run app.py
```

A interface poderá ser acessada pelo navegador, normalmente no endereço `http://localhost:8501`.

## Próximos passos

Com as visualizações iniciais implementadas, a próxima etapa será realizar a coleta dos dados reais de eventos e palestras, incluindo registros de anos anteriores.

Após a coleta, pretendemos avaliar a qualidade dos dados, revisar a classificação das áreas temáticas e adaptar as visualizações às características do conjunto obtido.

Também planejamos explorar novas formas de interação entre os gráficos, permitindo que seleções realizadas em uma visualização influenciem as demais. Dessa forma, será possível aprofundar a análise e investigar relações que não são tão evidentes ao observar cada gráfico isoladamente.

**Observação:** os resultados apresentados nesta etapa são apenas ilustrativos, pois foram obtidos a partir de dados sintéticos. As conclusões sobre a programação de eventos do ICMC serão elaboradas após a coleta e análise dos dados reais.