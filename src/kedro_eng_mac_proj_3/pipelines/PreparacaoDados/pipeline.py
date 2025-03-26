"""
Pipeline de preparação dos dados
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.formata_dados,
            inputs=["df_dev", "params:dev_description"],
            outputs="data_filtered_dev",
            tags=["filter_data"]
        ),
        node(
            nodes.formata_dados,
            inputs=["df_prod","params:prod_description"],
            outputs="data_filtered_prod",
            tags=["filter_data"]
        ),
        node(
            nodes.separa_base,
            inputs="data_filtered_dev",
            outputs=["base_train", "base_test"],
            tags=["split_data"]
        )
    ])