# Documentação da Aplicação
`app_streamlit_II.py`

## Descrição Geral

Este script é uma aplicação Streamlit que realiza uma análise exploratória de dados de _telemarketing_. A aplicação permite carregar um arquivo de dados, aplicar filtros interativos e visualizar gráficos comparativos. As funcionalidades incluem:

- Carregamento de arquivos CSV ou Excel.
- Filtros interativos para selecionar subconjuntos dos dados.
- Visualização de gráficos de barras ou pizza para comparar proporções.
- Download dos dados filtrados em formato Excel.

A aplicação foi desenvolvida para demonstrar o uso de bibliotecas como `pandas`, `seaborn`, `matplotlib` e `streamlit` para análise de dados de telemarketing.


## Requisitos

Para executar esta aplicação, você precisará de:

- Python 3.7 ou superior.
- Bibliotecas instaladas: `streamlit`, `pandas`, `seaborn`, `matplotlib`, `Pillow`, `xlsxwriter`.

Instale as dependências com:
``pip install streamlit pandas seaborn matplotlib Pillow xlsxwriter``

## Como Executar
- Salve o código no arquivo app_streamlit_II.py.
- No terminal, execute:
`streamlit run app_streamlit_II.py`

---

Esta aplicação faz **deploy** com o streamlit para análise exploratória de dados de telemarketing, permitindo a visualização de tendências e proporções de forma interativa. Ela pode ser adaptada para outros conjuntos de dados ou expandida com novas funcionalidades.