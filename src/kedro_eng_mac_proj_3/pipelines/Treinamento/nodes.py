"""
Função para treinar modelos de classificação
"""

import mlflow
from pycaret.classification import *
from sklearn.metrics import log_loss
from sklearn.metrics import f1_score
import pickle
import os

def train_model(train, test, modelo, description, session_id):
    mlflow.set_tracking_uri('http://localhost:5000')
    with mlflow.start_run(run_name='Treinamento') as run:
        mlflow.log_param("description", description)
        mlflow.log_param("session_id", session_id)
        exp = ClassificationExperiment()
        print(session_id)
        exp.setup(data=train, target='shot_made_flag', session_id=session_id)
        res_model = exp.create_model(modelo)
        tuned_res = exp.tune_model(res_model, n_iter=100, optimize='F1', search_library='scikit-optimize')
        test_predictions = exp.predict_model(tuned_res, data=test)
        probabilities = test_predictions[['prediction_score']]
        true_labels = test_predictions['shot_made_flag']
        log_loss_value = log_loss(true_labels, probabilities)
        predicted_labels = test_predictions['prediction_label']
        f1 = f1_score(true_labels, predicted_labels)
        with open("model.pkl", "wb") as file:
            pickle.dump(tuned_res, file)
        mlflow.log_metric("log_loss_value", log_loss_value)
        mlflow.log_metric("f1_value", f1)
        mlflow.sklearn.log_model(tuned_res, "model")
        mlflow.log_artifact("model.pkl")
        os.remove("model.pkl")
    return tuned_res

