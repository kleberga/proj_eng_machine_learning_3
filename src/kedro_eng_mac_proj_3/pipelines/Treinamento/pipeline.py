"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                nodes.train_model,
                inputs=["base_train", "base_test", "params:lr_model", "params:lr_descriptions", "params:lr_session_id"],
                outputs='model_lr',
                tags=["train_logistic_regression"]
        ),
                node(
                nodes.train_model,
                inputs=["base_train", "base_test", "params:dt_model", "params:dt_descriptions", "params:dt_session_id"],
                outputs='model_dt',
                tags=["train_decision_tree"]
        ),
    ])
