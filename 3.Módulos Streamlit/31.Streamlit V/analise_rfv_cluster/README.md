# 📊 RFV Clustering  

Este repositório contém uma aplicação desenvolvida em **Streamlit** para segmentação de clientes utilizando **RFV (Recência, Frequência e Valor)** e **K-Means Clustering**.

O objetivo é agrupar clientes em clusters com base no comportamento de compras, permitindo a criação de estratégias de marketing mais eficazes.  

**Link no Render:** [analise-rfv-cluster](https://analise-rfv-cluster.onrender.com/)

## 🚀 Funcionalidades  
- **Cálculo de Recência (R):** Quantidade de dias desde a última compra.  
- **Cálculo de Frequência (F):** Número total de compras realizadas.  
- **Cálculo de Valor (V):** Valor total gasto no período analisado.  
- **Normalização dos Dados:** Aplicação do **StandardScaler** para padronizar os valores.  
- **Clusterização com K-Means:** Agrupamento dos clientes em clusters com base nas métricas RFV.  
- **Download dos Resultados:** Exportação dos dados segmentados em **CSV** ou **Excel**.  

## 🛠 Tecnologias Utilizadas  
- **Python** 🐍  
- **Pandas** 📊  
- **Streamlit** 🎛️  
- **Scikit-learn (K-Means, StandardScaler)** 🤖  
- **XlsxWriter** 📄  


## ▶️ Como Executar

1. **Instale as dependências:** `pip install -r requirements.txt`
2. **Execute a aplicação:** `streamlit run app_RFV_cluster.py`
