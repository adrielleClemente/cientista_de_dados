# Regressão Logística - OOT
Neste projeto, estamos construindo um _credit scoring_ para cartão de crédito, em um desenho amostral com 15 safras, e utilizando 12 meses de performance.

**Descritiva Univariada**
```python
print('numero de linhas: {0} \nnúmero de colunas: {1}'.format(df.shape[0], df.shape[1]))

# Output
# numero de linhas: 750000 
# número de colunas: 15
```

## Amostragem
Separação dos três últimos meses como safras de **validação out of time (oot)**.
```python
ultimos_meses = df['data_ref'].sort_values().unique()[-3:]

df_oot = df[df['data_ref'].isin(ultimos_meses)]

df_treino = df[~df['data_ref'].isin(ultimos_meses)]

print("Base de treino:", df_treino.shape)
print("Base de validação:", df_oot.shape)

# Output
# Base de treino: (600000, 15)
# Base de validação: (150000, 15
```

## Modelo de Regressão Logística
Depois da análise descritiva bivariada de cada variável discreta e contínua, foi possível o desenvolvimento do modelo:
```python
formula = 'mau ~ ' + ' + '.join([col for col in df.columns if col not in ['data_ref', 'index', 'mau']])
rl = smf.glm(formula, data=df_treino, family=sm.families.Binomial()).fit()
```

## Avaliação do modelo

**Modelo na base df_treino:**
- Acurácia: 54.1%
- AUC: 77.5%
- GINI: 55.0%
- KS: 41.4%

**Modelo com colunas categorizadas:**
- Acurácia: 54.1%
- AUC: 77.5%
- GINI: 55.0%
- KS: 41.4%

**Modelo na base df_oot:**
- Acurácia: 59.5%
- AUC: 78.0%
- GINI: 55.9%
- KS: 41.8%

Durante os ajustes do modelo em vários teste não houve mudanças nos valores do IV das covariáveis. Para os outliers, categorizei renda e tempo_emprego para tentar amenizar o impacto das colunas no modelo, mas essa técnica não trouxe diferençaa nas métricas finais.

O modelo se manteve estável entre as bases de df_treino e df_oot, com métricas muito próximas, indicando boa generalização. O desempenho um pouco superior na base oot sugere um ajuste melhor ao conjunto de validação, mas acredito que não muito significativo.


