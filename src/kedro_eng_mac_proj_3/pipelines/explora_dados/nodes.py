"""
Funções de carga e exploração dos dados
"""

import requests
import pandas as pd
import os
import mlflow

def download_data(caminho_salvo, url_arquivo, descricao):
    mlflow.set_tracking_uri('http://localhost:5000')
    with mlflow.start_run(run_name="CargaDados") as run:
        mlflow.log_param("description", descricao)
        if(os.path.exists(caminho_salvo)):
            mlflow.log_param("file_path", caminho_salvo)
            mlflow.log_artifact(caminho_salvo)
            print("Usando dados já salvos...")
            df = pd.read_parquet(caminho_salvo)
        else:
            mlflow.log_param("file_path", url_arquivo)
            print("Baixando dados do repositório...")
            resp = requests.get(url_arquivo)
            with open("file.parquet", "wb") as file:
                file.write(resp.content)
            df = pd.read_parquet("file.parquet")
            mlflow.log_artifact("file.parquet")
        mlflow.log_metric("file_rows", len(df))
        mlflow.log_metric("file_columns", len(df.columns))
        mlflow.end_run()
    return df


def descricao_dados(base, descricao):
    mlflow.set_tracking_uri('http://localhost:5000')
    with mlflow.start_run(run_name="ExploraDados") as run:
        mlflow.log_param("description", descricao)
        # criar um dataframe de nomes das colunas
        base_var_df = pd.DataFrame(base.columns.tolist(), columns=["Nome das variáveis"])
        mlflow.log_param("names_columns", base.columns.tolist())
        # inserir no dataframe os tipos das colunas
        base_var_df["Tipo"] = base.dtypes.tolist()
        # inserir no dataframe a quantidade de missing values
        base_var_df["Nr. de missing values"] = base.isnull().sum().tolist()
        # inserir no dataframe a quantidade de observacoes
        base_var_df["Nr. de observações"] = base.count().tolist()
        filtered_mis = base_var_df[base_var_df["Nr. de missing values"] > 0]["Nome das variáveis"].tolist()
        if(len(filtered_mis)>0):
            mlflow.log_param("columns_with_missing_values", filtered_mis)
        else:
            mlflow.log_param("columns_with_missing_values", "Não há colunas com missing values")
        base_var_df.to_excel('explora_dados.xlsx', index=False)
        mlflow.log_artifact('explora_dados.xlsx')
        os.remove('explora_dados.xlsx')
        mlflow.end_run()
    return base_var_df