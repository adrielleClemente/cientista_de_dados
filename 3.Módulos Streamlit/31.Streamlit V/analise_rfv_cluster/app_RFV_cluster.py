# Imports
import pandas                as pd
import streamlit             as st

from   sklearn.cluster       import KMeans
from   sklearn.preprocessing import StandardScaler
from   datetime              import datetime
from   io                    import BytesIO

@st.cache_data()
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

@st.cache_data()
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(
        page_title='RFV Clustering',
        layout="wide",
        initial_sidebar_state='expanded'
    )

    # Título principal da aplicação
    st.write("""# RFV Clustering

    Essa aplicação utiliza o método RFV (Recência, Frequência, Valor) para segmentar clientes por meio de clusterização.
    O objetivo é agrupar clientes em clusters semelhantes para criar ações de marketing direcionadas.

    Para cada cliente, calculamos as métricas a seguir:
    - **Recência (R):** Quantidade de dias desde a última compra.
    - **Frequência (F):** Quantidade total de compras no período.
    - **Valor (V):** Total gasto no período.
    """)
    st.markdown("---")

    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Bank marketing data", type=['csv', 'xlsx'])

    # Número de clusters definido pelo usuário
    num_clusters = st.sidebar.slider("Escolha o número de clusters", min_value=2, max_value=10, value=4)

    # Verifica se há conteúdo carregado na aplicação
    if (data_file_1 is not None):
        df_compras = pd.read_csv(data_file_1, parse_dates=['DiaCompra'])

        # st.write('## Recência (R)')
        
        dia_atual = df_compras['DiaCompra'].max()
        st.write('Dia máximo na base de dados: ', dia_atual)

        df_recencia = df_compras.groupby(by='ID_cliente', as_index=False)['DiaCompra'].max()
        df_recencia.columns = ['ID_cliente', 'DiaUltimaCompra']
        df_recencia['Recencia'] = df_recencia['DiaUltimaCompra'].apply(lambda x: (dia_atual - x).days)
        df_recencia.drop('DiaUltimaCompra', axis=1, inplace=True)

        # st.write('## Frequência (F)')
        df_frequencia = df_compras[['ID_cliente', 'CodigoCompra']].groupby('ID_cliente').count().reset_index()
        df_frequencia.columns = ['ID_cliente', 'Frequencia']

        # st.write('## Valor (V)')
        df_valor = df_compras[['ID_cliente', 'ValorTotal']].groupby('ID_cliente').sum().reset_index()
        df_valor.columns = ['ID_cliente', 'Valor']

        st.write('## Tabela RFV Final')
        df_RF = df_recencia.merge(df_frequencia, on='ID_cliente')
        df_RFV = df_RF.merge(df_valor, on='ID_cliente')
        df_RFV.set_index('ID_cliente', inplace=True)
        st.write(df_RFV.head(20))

        st.write('## Clusterização utilizando K-Means')

        # Normalizar os dados
        scaler = StandardScaler()
        rfv_scaled = scaler.fit_transform(df_RFV)

        # Aplicar K-Means
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        df_RFV['Cluster'] = kmeans.fit_predict(rfv_scaled)

        st.write(f"### Clusters formados ({num_clusters} clusters)")
        st.write(df_RFV.groupby('Cluster').mean())

        # Visualizar os dados com clusters atribuídos
        st.write('## Tabela RFV com Clusters')
        st.write(df_RFV.head(20))

        # Baixar a tabela com os clusters
        df_xlsx = to_excel(df_RFV)
        st.download_button(
            label='📥 Download',
            data=df_xlsx,
            file_name='RFV_Clusters_.xlsx'
        )

if __name__ == '__main__':
    main()


