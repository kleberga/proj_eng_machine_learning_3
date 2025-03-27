# Projeto da disciplina Engenharia de Machine Learning [25E1_3]

## Questão 1

Aluno: Kleber Giovelli Abitante

Repositório: https://github.com/kleberga/proj_eng_machine_learning_3

## Questão 2

A figura abaixo mostra os arquivos originais (baixados do site) na pasta *01_raw* do projeto:

**Figura 1** - Arquivos na pasta *01_raw*.

![Arquivos na pasta raw](raw.PNG)

A imagem a seguir mostra as etapas necessárias para conclusão deste projeto.

**Figura 2** - Diagrama das etapas necessárias para o projeto.

![Diagrama](diagrama_2.png)

## Questão 3

- **Streamlit**: é uma ferramenta para construir aplicações baseadas na web para machine learning e ciência de dandos. Ela permite criar dashboards interativos, utilizar outras bibliotecas, como Matplotlib, para visualizar os dados e adicionar botões e menus que permitam ao usuário interagir com a aplicação. Além disso, a aplicação pode auxiliar a monitorar e gerenciar a saúde dos modelos;
- **MLFlow**: permite o rastreamento de experimentos de machine learning, registro e controle de versões dos modelos e provisionamento (deployment) em plataformas na nuvem, em contêineres Docker ou em REST APIs;
- **PyCaret**: é uma biblioteca que possui funções que automatizam o pré-processamento, treinamento e avaliação de modelos de machine learning. Ela permite buscar os melhores hiperparâmetros e comparar modelos de forma fácil e com a utilização de poucas funções. Pode ser utilizada também na atualização de modelos; e
- **Scikit-Learn**: é uma ferramenta que possui funções para criação e implementação de modelos de machine learning. Permite pré-processamento de dados, busca pelos melhores hiperparâmetros, seleção de features, treinamento, avaliação e atualização de modelos.

## Questão 4

Os artefatos que serão criados no projeto são:

- **diagrama_2.png**: diagrama contendo todas as etapas necessárias do projeto;
- **dataset_kobe_dev.parquet**: base de dados, que contém os arremessos de Kobe Bryant, a ser utilizada para treinamento dos modelos. A base contém 25 colunas e 24.271 linhas. As colunas da base de dados são:
  1. *action_type*: tipos de arremessos, de forma mais detalhada, totalizado 57 diferentes tipos;
  2. *combined_shot_type*: tipos de arremessos, de forma mais geral, totalizado 6 diferentes tipos;
  3. *game_event_id*: identificador único de cada evento;
  4. *game_id*: identificador único de cada jogo;
  5. *lat*: latitude do estádio em que o jogo foi realizado;
  6. *lon*: longitude do estádio em que o jogo foi realizado;
  7. *loc_x*: localização do arremesso no eixo-x (-250 = canto inferior direito da quadra até 250 = canto superior direito da quadra, em que a cesta está no centro direito);
  8. *loc_y*: localização do arremesso no eixo-y (-40 = lado direito até 900 = lado esquerdo, em que a cesta está no centro direito);
  9. *minutes_remaining*: minutos faltando para terminar um período do jogo (máximo de 12);
  10. *period*: período do jogo (em geral, há no máximo 4, mas em caso de empate, ocorrerão períodos adicionais);
  11. *playoffs*: marcação se o jogo não ocorreu nos playoffs (0) ou ocorreu em playoffs (1);
  12. *season*: temporada da NBA;
  13. *seconds_remaining*: segundos faltando em um período;
  14. *shot_distance*: distância (em metros) do arremesso em relação à cesta;
  15. *shot_type*: pontos que poderiam ser obtidos no arremesso (2 ou 3 pontos);
  16. *shot_zone_area*: área da quadra de basquete de onde o arremesso foi executado (BC, C, LC, L, RC, R);
  17. *shot_zone_basic*: zona da quadra de basquete de onde o arremesso foi executado (7 diferentes áreas);
  18. *shot_zone_range*: intervalo (em metros) de onde o arremesso foi executado (<8, 8-16, 16-24, 24+, fundo da quadra);
  19. *team_id*: código identificador do time de Kobe Bryant (Los Angeles Lakers - LA) (mesmo código em toda a base de dados);
  20. *team_name*: nome do time (LA) (mesmo nome em toda a base de dados);
  21. *game_date*: data em que o jogo ocorreu
  22. *matchup*: equipes que disputaram a partida (LA versus outra equipe);
  23. *opponent*: equipe adversária de LA na partida;
  24. *shot_made_flag*: marcação se o arremesso teve sucesso (1) ou não (0); e
  25. *shot_id*: identificador único de cada arremesso.
- **dataset_kobe_prod.parquet**: base de dados, que contém os arremessos de Kobe Bryant, a ser utilizada com o modelo final no ambiente de produção. A base contém 25 colunas e 6.426 linhas. As colunas da base de dados são as mesmas da base anterior;
- **df_explorado_dev.xlsx**: base de dados contendo os nomes das colunas, o tipo de cada coluna, a quantidade valores faltantes em cada coluna e o número total de observações de cada coluna da base de desenvolvimento de modelos;
- **df_explorado_prod.xlsx**: base de dados contendo os nomes das colunas, o tipo de cada coluna, a quantidade valores faltantes em cada coluna e o número total de observações de cada coluna da base a ser utilizada com o modelo final no ambiente de produção;
- **data_filtered_dev.parquet**: base de dados com exclusão das linhas com valores faltantes e contendo apenas as colunas a serem utilizadas no treinamento dos modelos. A base contém 7 colunas e 20.285 linhas. As colunas são:
  1. *lat*;
  2. *lon*;
  3. *minutes_remaining*;
  4. *period*;
  5. *playoffs*;
  6. *shot_distance*; e
  7. *shot_made_flag*.
- **data_filtered_prod.parquet**: base de dados com exclusão das linhas com valores faltantes e contendo apenas as colunas a serem utilizadas com o modelo final no ambiente de produção. A base contém 7 colunas e 5.412 linhas. As colunas são as mesmas da base anterior.
- **base_test.parquet**: representa 20% dos dados da base "data_filtered_dev.parquet", a ser usada para testar os modelos. A divisão foi realizada de modo aleatório e com estratificação pela variável *shot_made_flag*;
- **base_train.parquet**: representa 80% dos dados da base "data_filtered_dev.parquet", a ser usada para treinar os modelos. A divisão foi realizada de modo aleatório e com estratificação pela variável *shot_made_flag*;
- **model_dt.pkl**: modelo de árvore de decisão criado com a base de treinamento. O modelo é salvo com controle de versão;
- **model_lr.pkl**: modelo de regressão logística criado com a base de treinamento. O modelo é salvo com controle de versão;
- **modelo final registrado**: modelo final registrado no MLFlow;
- **pipeline de aplicação**: pipeline para provisionamento do modelo final escolhido para ser aplicado na base de produção; e
- **dashboard**: dashboard para monitorar o modelo em produção.

## Questão 5

A imagem abaixo mostra o pipeline do MLFlow com o nome "PreparacaoDados" para a base de desenvolvimento. Este pipeline remove os valores faltantes e filtra apenas as variáveis a serem utilizadas nos modelos.

**Figura 3** - Imagem do pipeline de processamento de dados com o MLFlow, rodada (run) com o nome "PreparacaoDados" para manipulação da base de desenvolvimento.

![Pipeline de "PreparacaoDados" para a base de desenvolvimento](preparacaoDados_1.PNG)

A imagem a seguir mostra o pipeline do MLFlow com o nome "PreparacaoDados" para a base de produção, o qual também remove os valores faltantes e filtra apenas as variáveis a serem utilizadas nos modelos.

**Figura 4** - Imagem do pipeline de processamento de dados com o MLFlow, rodada (run) com o nome "PreparacaoDados" para manipulação da base de produção.

![Pipeline de "PreparacaoDados" para a base de produção](preparacaoDados_2.PNG)

A imagem a seguir mostra os arquivos filtrados e com eliminação de valores faltantes salvos na pasta *02_intermediate*.

**Figura 5** - Imagem dos arquivos filtrados.

![Imagem dos arquivos filtrados](preparacaoDados_5.PNG)

A imagem a seguir mostra o pipeline do MLFlow com o nome "PreparacaoDados" para separar as bases em treinamento e teste.

**Figura 6** - Imagem do pipeline de processamento de dados com o MLFlow, rodada (run) com o nome "PreparacaoDados" para separar a base em treinamento e teste.

![Pipeline de "PreparacaoDados" para separar a base em treinamento e teste](preparacaoDados_3.PNG)

A imagem a seguir mostra os arquivos de treinamento e de teste, após a separação em 80% para treinamento e o restante para teste.

**Figura 7** - Base de treinamento e de teste após a separação.

![Bases de treinamento e teste](preparacaoDados_4.PNG)

## Questão 6

A imagem a seguir apresentar o pipeline do MLFlow com o nome "Treinamento" do modelo de árvore de decisão, juntamente com as métricas de *log loss* e *F1 score*.

**Figura 8** - Imagem do pipeline de processamento de dados com o MLFlow, rodada (run) com o nome "Treinamento" do modelo de árvore de decisão.

![Pipeline de "Treinamento" da árvore de decisão](treinamento_1.PNG)

A próxima imagem mostra o artefato referente ao modelo de árvore de decisão.

**Figura 9** - Artefato do modelo de árvore de decisão:

![Artefato do modelo de árvore de decisão](treinamento_11.PNG)

A imagem a seguir apresenta o pipeline do MLFlow com o nome "Treinamento" do modelo de regressão logística, juntamente com as métricas de *log loss* e *F1 score*.

**Figura 10** - Imagem do pipeline de processamento de dados com o MLFlow, rodada (run) com o nome "Treinamento" do modelo de regressão logística.

![Pipeline de "Treinamento" da regressão logística](treinamento_2.PNG)

A imagem a seguir mostra o artefato da regressão logística.

**Figura 11** - Artefato do modelo de regressão logística:

![Artefato de modelo de regressão logística](treinamento_21.PNG)

O modelo escolhido para finalização foi a **regressão logística**, pois apresentou o maior valor de *F1 score* e o menor valor de *log loss*, em relação à árvore de decisão.

## Questão 7

A imagem a seguir mostra a inicialização do MLFlow server:

**Figura 12** - Inicialização do MLFlow server.

![Inicialização do MLFlow server](iniciar_server.PNG)

A próxima imagem mostra a inicialização da API local do modelo escolhido ("regressão logística") usando o MLFlow

**Figura 13** - Inicialização do MLFlow server.

![Inicialização do MLFlow server](iniciar_server.PNG)

