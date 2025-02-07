# Escorando o modelo gerado no pycaret
![Data_Pipeline](https://github.com/user-attachments/assets/8300df06-517c-4efa-9d77-76bb4fdc37fa)


## Regressão Logística (PyCaret)
Ao final da criação do modelo, ele foi salvo em um arquivo pkl e usado para fazer previsões de dados de um csv. Aplicação web finalizada no arquivo ``app_pycaret.py``

**1. Visão Geral do Projeto**

- Nome do Projeto: Escorando o modelo gerado no pycaret

- Objetivo: Treinar um modelo de regressão logística (logistic regression) usando o [PyCaret](https://pycaret.org/).

- Tecnologias: ``Python 3.11.11``, PyCaret, ``Streamlit 1.36``

**2. Dados Utilizados**

- Fonte dos Dados: Para treinar o modelo foi usado um dataset de credit scoring.

## Modelo
_Código completo no final do arquivo Mod38PyCaret.ipynb_

```python

from pycaret.classification import *

exp_clf101 = setup(data = df, target = 'mau', session_id=123)

lr = create_model('lr')

predict_model(lr)
```
| Model                 | Accuracy | AUC    | Recall | Prec.  | F1     | Kappa  | MCC    |
|-----------------------|----------|--------|--------|--------|--------|--------|--------|
| Logistic Regression  | 0.9217   | 0.7718 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

```python
# finalizando e salvando o modelo
final_lr = finalize_model(lr)

import pickle

arquivo = 'Final lr Model 02Fev2024.pkl'
pickle.dump(final_lr, open(arquivo, 'wb'))

```

## Demonstração do deploy realizado no streamlit







https://github.com/user-attachments/assets/4927301c-b6f8-4481-8125-52e687d5dcec



