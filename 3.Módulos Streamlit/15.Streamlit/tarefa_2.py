import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import streamlit as st


sns.set()

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    st.pyplot(fig=plt)
    return None

st.title('Análise SISNAC')

sinasc = pd.read_csv('SINASC_RO_2019.csv')

st.write('### Data Máxima')
sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC)
st.write(sinasc.DTNASC.max())

st.write('### Datas Únicas Ordenadas')

datas = sinasc.DTNASC.unique()

st.write(datas)

# sinasc.DTNASC.min()


# max_data = sinasc.DTNASC.max()[:7]
# print(max_data)

# os.makedirs('./output/figs/'+max_data, exist_ok=True)


plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'quantidade de nascimento','data de nascimento')
# plt.savefig('./output/figs/'+max_data+'/quantidade de nascimento.png')

plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
# plt.savefig('./output/figs/'+max_data+'/media idade mae por sexo.png')

plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
# plt.savefig('./output/figs/'+max_data+'/media peso bebe por sexo.png')

plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'apgar1 medio','gestacao','sort')
# plt.savefig('./output/figs/'+max_data+'/media apgar1 por escolaridade mae.png')

plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
# plt.savefig('./output/figs/'+max_data+'/media apgar1 por gestacao.png')

plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio','gestacao','sort')
# plt.savefig('./output/figs/'+max_data+'/media apgar5 por gestacao.png')