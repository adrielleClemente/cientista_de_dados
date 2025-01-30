# Tarefas Discursivas
**Assunto:** Combinação de Modelos I.

## Tarefa 1
#### 1. Monte um passo a passo para o Bagging

**Passos:**

1. Possuir um dataset.
2. Começando a amostragem com reposição gerando um novo dataframe com as mesmas quantidades de linhas, porém com reposição dos dados.
3. Assim, gera-se novas amostras com diferentes reposições.
4. Cria um modelo (ex. árvore de decisão) para cada conjunto de dados gerado (Base learners).
5. Usa-se os modelos para a fase de classificação.
6. A partir da classificação, faz um Aggregation (agregação) com as repostas dos modelos. A melhor classificação é agregada.

#### 2. Explique com suas palavras o Bagging

Bagging - Bootstrap Aggregating é uma técnica para melhorar a precisão de modelos de machine learning. Ele gera várias amostras do conjunto de dados inicial, estas amostragens usa reposição para selecionar aleatoriamente exemplos do conjunto original. Depois é criado um modelo para cada nova amostra, assim pode-se classificar as respostas desses modelos.

## Tarefa 2
#### 1. Monte um passo a passo para o algoritmo RF
**Passos:**

1. A partir do dataset cria-se novas amostras selecionando linhas e colunas aleatórias. (Bootstrap + Feature selection)
2. Gerar árvores de decisão para cada novo conjunto de dados.
3. Classificar cada árvore, passando o elemento de teste e encontrar o resultado predito para cada árvore.
4. Criar uma tabela de frequência e assim encontrar a melhor resposta.

#### 2. Explique com suas palavras o Random Forest
É um método de machine learning que se baseia em árvores de decisão. É robusto a overfitt, mas há casos em que podem ocasionar o overfitt.

#### 3. Qual a diferença entre Bagging e Random Forest?
A principal diferença é que depois da etapa do Bootstrap, enquanto com Bagging fazemos modelos a partir de cada nova amostragem, com o Random Forest criamos árvores de decisão.


## Tarefa 3
- Quais são os hyperparâmetros do RF?
- Pra que serve cada um deles?

1. **`n_estimators`**
   - **Função**: Define o número de árvores na floresta.

2. **`max_depth`**
   - **Função**: Define a profundidade máxima das árvores.

3. **`min_samples_split`**
   - **Função**: Define o número mínimo de amostras necessárias para dividir um nó.

4. **`min_samples_leaf`**
   - **Função**: Define o número mínimo de amostras que devem estar presentes em um nó folha.

5. **`max_features`**
   - **Função**: Define o número máximo de características consideradas para encontrar a melhor divisão.

6. **`bootstrap`**
   - **Função**: Define se as amostras são extraídas com reposição.

7. **`oob_score`**
   - **Função**: Define se a pontuação fora-da-bolsa (out-of-bag) deve ser usada para avaliar a precisão do modelo.

8. **`n_jobs`**
   - **Função**: Define o número de jobs a serem executados em paralelo.

9. **`random_state`**
   - **Função**: Define a semente usada pelo gerador de números aleatórios.

10. **`criterion`**
    - **Função**: Define a função usada para medir a qualidade de uma divisão (por exemplo, "gini" para o índice Gini ou "entropy" para a entropia).

**Fonte:** [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)