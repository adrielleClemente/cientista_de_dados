import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_text

from sklearn.model_selection import cross_val_score
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

sns.set_theme(context='talk', style='ticks')

st.set_page_config(
     page_title="Análise de Dados",
     page_icon=":v:",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')


#plots
# fig, ax = plt.subplots(8,1,figsize=(10,70))
# renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
# st.write('## Gráficos ao longo do tempo')
# sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
# ax[1].tick_params(axis='x', rotation=45)
# sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
# ax[2].tick_params(axis='x', rotation=45)
# sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
# ax[3].tick_params(axis='x', rotation=45)
# sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
# ax[4].tick_params(axis='x', rotation=45)
# sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
# ax[5].tick_params(axis='x', rotation=45)
# sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
# ax[6].tick_params(axis='x', rotation=45)
# sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
# ax[7].tick_params(axis='x', rotation=45)
# sns.despine()
# st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,70))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)



st.write('---------------' )

st.write('### Renda por Tempo de Emprego (Renda < 25.000)')

df_renda_abaixo_10000 = renda[renda['renda'] < 25000]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='tempo_emprego', y='renda', data=df_renda_abaixo_10000, alpha=0.6)
plt.title('Renda por Tempo de Emprego (Renda < 25.000)')
plt.xlabel('Tempo de Emprego (anos)')
plt.ylabel('Renda')
plt.show()
st.pyplot(plt)

st.write('### Renda por Tempo de Emprego (Renda >= 25.000)')

df_renda_acima_10000 = renda[renda['renda'] >= 25000]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='tempo_emprego', y='renda', data=df_renda_acima_10000, alpha=0.6)
plt.title('Renda por Tempo de Emprego (Renda >= 25.000)')
plt.xlabel('Tempo de Emprego (anos)')
plt.ylabel('Renda')
plt.show()
st.pyplot(plt)

st.write('---------------' )

st.write('### Árvore de Decisão')

# Selecionando as variáveis de interesse
X = renda[['tempo_emprego']]  
y = renda['renda']

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeRegressor(max_depth=3, min_samples_split=10, min_samples_leaf=5)
modelo.fit(X_train, y_train)
plt.figure(figsize=(20,10))
plot_tree(modelo, filled=True)
plt.savefig('arvore_decisao.png')
plt.show()
st.pyplot(plt)


st.write('## Avaliação dos Resultados')

st.write('#### Previsões de renda com base nos anos trabalhados')

# Resultados das previsões
predictions = [
    ('Se Anos trabalhados <= 4.61', 'a previsão é 3682.46'),
    ('Se Anos trabalhados está entre 4.61 e 8.87', 'a previsão é 5192.17'),
    ('Se Anos trabalhados está entre 8.87 e 11.59', 'a previsão é 6870.45'),
    ('Se Anos trabalhados está entre 11.59 e 16.50', 'a previsão é 8959.83'),
    ('Se Anos trabalhados está entre 16.50 e 16.53', 'a previsão é 31647.28'),
    ('Se Anos trabalhados está entre 16.53 e 30.34', 'a previsão é 13047.72'),
    ('Se Anos trabalhados` está entre 30.34 e 30.60', 'a previsão é 68787.59'),
    ('Se Anos trabalhados > 30.60', 'a previsão é 27242.52')
]


# Exibição das previsões
for condition, prediction in predictions:
    st.write(f"{condition}, {prediction}")
