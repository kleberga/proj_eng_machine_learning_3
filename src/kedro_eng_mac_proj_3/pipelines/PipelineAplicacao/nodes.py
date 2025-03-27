"""
Função para enviar uma base de dados para a API que está provisionando o modelo
"""

import json
import requests
import pandas as pd
from sklearn.metrics import f1_score
import mlflow
import os

def pipeline_aplicacao(base, url):
    mlflow.set_tracking_uri('http://localhost:5000')
    with mlflow.start_run(run_name="PipelineAplicacao") as run:
        mlflow.log_param("url_api", url)
        true_values = base['shot_made_flag']
        # Filtrar a coluna que não será usada no modelo
        base = base.drop(['shot_made_flag'], axis = 1)
        payload = json.dumps(
            {
                "dataframe_split": base.to_dict(orient="split"),
            }
        )
        response = requests.post(
            url=url,
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        response2 = response.json()
        f1 = f1_score(true_values.tolist(), response2['predictions'])
        mlflow.log_metric("f1_score", f1)
        response_df = pd.DataFrame(response2['predictions'], columns=["predictions"])
        response_df.to_parquet("predictions.parquet")
        mlflow.log_artifact("predictions.parquet")
        os.remove("predictions.parquet")
