# Análise exploratória da previsão de renda

Primeiramente, utiliza a análise bivariada para comparar e explorar os dados do dataframe. Em seguida, adota `tempo_emprego` para prever `renda`.

### Vídeo do Deploy

https://github.com/adrielleClemente/cientista_de_dados/assets/104394818/f3491880-754d-4f0b-8d33-6b6d67a6af92


## Dicionário de Dados
| Variável                | Descrição                                           | Tipo   |
| ----------------------- |:---------------------------------------------------:| ------:|
| data_ref                |  Data de referência                                 | object |
| id_cliente              |  ID do clinete                                      | int64  |
| sexo                    |  Sexo do cliente                                    | object |
| posse_de_veiculo        |  Se o cliente possui veículo                        | bool   |
| posse_de_imovel         |  Se o cliente possui imóvel                         | bool   |
| qtd_filhos              |  Quantidade filhos                                  | int64  |
| tipo_renda              |  Tipo de renda                                      | object |
| educacao                |  Nível de educação formal                           | object |
| estado_civil            |  Estado civíl                                       | object |
| tipo_residencia         |  Tipo de residência                                 | object |
| idade                   |  Idade do cliente                                   | int64  |
| tempo_emprego           |  Tempo de emprego                                   | float64|
| qt_pessoas_residencia   |  Quantidade de pessoas que moram na residência      | float64|
| renda                   |  Valor da renda                                     | float64|


## Árvore de Decisão
![arvore_decisao](https://github.com/adrielleClemente/cientista_de_dados/assets/104394818/384e9e00-f8c8-422e-bee5-bf3201be0c1e)

## Avaliação dos resultados
Aqui estão as previsões com base nas condições da árvore acima:

    Se anos trabalhados <= 4.61, a previsão é 3682.46.
    Se anos trabalhados está entre 4.61 e 8.87, a previsão é 5192.17.
    Se anos trabalhados está entre 8.87 e 11.59, a previsão é 6870.45.
    Se anos trabalhados está entre 11.59 e 16.50, a previsão é 8959.83.
    Se anos trabalhados está entre 16.50 e 16.53, a previsão é 31647.28.
    Se anos trabalhados está entre 16.53 e 30.34, a previsão é 13047.72.
    Se anos trabalhados está entre 30.34 e 30.60, a previsão é 68787.59.
    Se anos trabalhados > 30.60, a previsão é 27242.52.
