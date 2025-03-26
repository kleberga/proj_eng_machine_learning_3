"""
Funções de preparação dos dados
"""

import mlflow
from sklearn.model_selection import train_test_split
import pandas as pd
import os

def formata_dados(base, description):
    # Aplicar transformações e limpeza necessárias
    mlflow.set_tracking_uri('http://localhost:5000')
    with mlflow.start_run(run_name="PreparacaoDados") as run:
        base.to_parquet('data_filtered_inicial.parquet', index=False)
        mlflow.log_artifact('data_filtered_inicial.parquet')
        mlflow.log_param("input_file_name", description)
        mlflow.log_param("description_before", "Contém os dados antes da remoçãos dos missings e de filtragem das variáveis a serem utilizadas.")
        mlflow.log_metric("initial_rows", len(base))
        mlflow.log_metric("initial_columns", len(base.columns))
        base.dropna(subset=['shot_made_flag'], inplace=True)
        base2 = base[['lat','lon','minutes_remaining','period','playoffs','shot_distance','shot_made_flag']]
        base2.to_parquet('data_filtered_final.parquet', index=False)
        mlflow.log_artifact('data_filtered_final.parquet')
        mlflow.log_metric("final_rows", len(base2))
        mlflow.log_metric("final_columns", len(base2.columns))
        mlflow.log_param("description_after", "Contém os dados após a remoção dos missings e de filtragem das variáveis.")
        mlflow.log_param("variables_filtered", "lat, lon, minutes_remaining, period, playoffs, shot_distance, shot_made_flag")
        os.remove('data_filtered_final.parquet')
        os.remove('data_filtered_inicial.parquet')
    return base2
    

def separa_base(base):
    mlflow.set_tracking_uri('http://localhost:5000')
    with mlflow.start_run(run_name="PreparacaoDados") as run:
        mlflow.log_param("description", "Separar a base em treinamento e teste")
        X = base.drop(columns=['shot_made_flag'])
        y = base['shot_made_flag']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10, stratify=y)
        base_train = pd.concat([X_train, y_train], axis=1)
        base_test = pd.concat([X_test, y_test], axis=1)
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("stratify", "yes")
        mlflow.log_param("random_state", 10)
        mlflow.log_metric("number_rows_train", len(base_train))
        mlflow.log_metric("number_rows_test", len(base_test))
        base_train.to_parquet('base_train.parquet', index=False)
        base_test.to_parquet('base_test.parquet', index=False)
        mlflow.log_artifact('base_train.parquet')
        mlflow.log_artifact('base_test.parquet')
        os.remove('base_train.parquet')
        os.remove('base_test.parquet')
        mlflow.end_run()
    return base_train, base_test
