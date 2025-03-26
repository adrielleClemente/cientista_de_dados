# Concessão de Crédito

No projeto é utilizado a **metodologia CRISP-DM** com as seguintes etapas:

### Etapa 1 CRISP - DM: Entendimento do negócio

Como primeira etapa do CRISP-DM, vamos entender do que se trata o negócio, e quais os objetivos. Nessa etapa também se avalia a situação da empresa/segmento/assunto de modo a se entender o tamanho do público, relevância, problemas presentes e todos os detalhes do processo gerador do fenômeno em questão, e portanto dos dados.

### Etapa 2 Crisp-DM: Entendimento dos dados

A segunda etapa é o entendimento dos dados. Foram fornecidas 15 variáveis mais a variável resposta. O significado de cada uma dessas variáveis se encontra na tabela.

#### Dicionário dos Dados
| Variable Name         | Description                                                | Tipo    |
| --------------------- | ---------------------------------------------------------- | ------- |
| sexo                  | M = 'Masculino'; F = 'Feminino'                            | M/F     |
| posse_de_veiculo      | Y = 'possui'; N = 'não possui'                             | Y/N     |
| posse_de_imovel       | Y = 'possui'; N = 'não possui'                             | Y/N     |
| qtd_filhos            | Quantidade de filhos                                       | inteiro |
| tipo_renda            | Tipo de renda (ex: assaliariado, autônomo etc)             | texto   |
| educacao              | Nível de educação (ex: secundário, superior etc)           | texto   |
| estado_civil          | Estado civil (ex: solteiro, casado etc)                    | texto   |
| tipo_residencia       | tipo de residência (ex: casa/apartamento, com os pais etc) | texto   |
| idade                 | idade em anos                                              | inteiro |
| tempo de emprego      | tempo de emprego em anos                                   | inteiro |
| possui_celular        | Indica se possui celular (1 = sim, 0 = não)                | binária |
| possui_fone_comercial | Indica se possui telefone comercial (1 = sim, 0 = não)     | binária |
| possui_fone           | Indica se possui telefone (1 = sim, 0 = não)               | binária |
| possui_email          | Indica se possui e-mail (1 = sim, 0 = não)                 | binária |
| qt_pessoas_residencia | quantidade de pessoas na residência                        | inteiro |
| **mau**               | indicadora de mau pagador (True = mau, False = bom)        | binária |


**Entendimento dos dados - Univariada**
```python
print(df['mau'].value_counts())
print("\nTaxa de inadimplentes:")
print(df['mau'].mean())

# output
False    16260
True       390

Taxa de inadimplentes:
0.023423423423423424
```

```python
var = 'mau'
grafico_barras = df[var].value_counts().plot.bar()
```
![image](https://github.com/user-attachments/assets/aacdfc09-0ca5-488a-abf6-97b0233785f6)


### Etapa 3 Crisp-DM: Preparação dos dados

Nessa etapa realizamos tipicamente as seguintes operações com os dados:

- Seleção Neste caso, os dados já estão pré-selecionados
- Limpeza Precisaremos identificar e tratar dados faltantes
- Construção Neste primeiro exercício não faremos construção de novas variáveis
- Integração Temos apenas uma fonte de dados, não é necessário agregação
- Formatação Os dados já se encontram em formatos úteis

Os dados já estão pré-selecionados, construídos e integrados, mas há dados faltantes que foram eliminados.

### Etapa 4 Crisp-DM: Modelagem

Nessa etapa que realizaremos a construção do modelo. Os passos típicos são:

- Selecionar a técnica de modelagem Utilizaremos a técnica de floresta aleatória (random forest), pois é uma técnica bastante versátil e robusta que captura bem padrões complexos nos dados, relativamente fácil de se usar e que costuma produzir excelentes resultados para uma classificação como estas. Vamos ver esse algoritmo em detalhes mais adiante no curso, mas pense nele por enquanto como uma regra complexa baseada nas variáveis explicativas que classifica o indivíduo como inadimplente ou não. Mais adiante no curso vamos extrair mais dessa técnica.
- Desenho do teste Antes de rodar o modelo precisamos construir um desenho do teste que será realizado. Para desenvolver um modelo como este, é considerado uma boa prática dividir a base em duas, uma chamada treinamento, onde o algoritmo 'aprende', e outra chamada teste, onde o algoritmo é avaliado. Essa prática fornece uma métrica de avaliação mais fidedigna do algoritmo, falaremos mais detalhes em lições futuras.
- Avaliação do modelo Faremos a avaliação do nosso modelo através do percentual de acerto, avaliando a classificação do modelo (inadimplente e não inadimplente) e comparando com o estado real armazenado na variável resposta (AtrasoRelevante2anos). Esse percentual de acerto é frequentemente chamado de acurácia (obs: nunca usar assertividade... assertivo não é aquele que acerta, e sim "adj.: em que o locutor declara algo, positivo ou negativo, do qual assume inteiramente a validade; declarativo." aCertivo está errado;)

**Rodando o Modelo**
```python
clf = RandomForestClassifier(n_estimators=3)
clf.fit(x_train,y_train)
```

### Etapa 5 Crisp-DM: Avaliação dos resultados

A etapa final do CRISP. Neste caso, a nossa avaliação termina com a acurácia. Mas em problemas futuros aprofundaremos mais - a ideia seria avaliar o impacto do uso do modelo no negócio, ou seja, o quanto o resultado financeiro melhora em detrimento da utilização do modelo.

### Etapa 6 Crisp-DM: Implantação

Nessa etapa colocamos em uso o modelo desenvolvido, normalmente implementando o modelo desenvolvido em um motor de crédito que toma as decisões com algum nível de automação - tipicamente aprovando automaticamente clientes muito bons, negando automaticamente clientes muito ruins, e enviando os intermediários para análise manual.
