
# Imports
import pandas            as pd
import streamlit         as st
import joblib

from io                     import BytesIO
from pycaret.classification import *



@st.cache_data()
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Função para converter o df para excel
@st.cache_data()
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()  # Correção aqui
    processed_data = output.getvalue()
    return processed_data


# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(page_title = 'PyCaret', \
        layout="wide",
        initial_sidebar_state='expanded'
    )



    # Título principal da aplicação
    st.write("""## 📈 Escorando o modelo gerado no pycaret """)
    st.markdown("---")

    
    
    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Bank Credit Dataset", type = ['csv'])

    # Verifica se há conteúdo carregado na aplicação
    if (data_file_1 is not None):
        df_credit = pd.read_csv(data_file_1)
        df_credit = df_credit.sample(50000)

       # tentar com o pickle.load()
        model = joblib.load(r'Final lr Model 02Fev2024.pkl')
        predict = predict_model(model, data=df_credit)       


        # Mostrar as 20 primeiras linhas
        st.write("### Amostra das Previsões")
        st.dataframe(predict.head(20))
        st.write("##### Quantidade de linhas e colunas da tabela:") 
        predict.shape

        st.markdown("---")
        st.write("##### Faça download")
        df_xlsx = to_excel(predict)
        st.download_button(label='📥 Download',
                            data=df_xlsx ,
                            file_name= 'predict.xlsx')


if __name__ == '__main__':
	main()
    









