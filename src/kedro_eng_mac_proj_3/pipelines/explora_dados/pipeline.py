"""
Pipeline de carga e exploração de dados
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.download_data,
            inputs=["params:dev_caminho_salvo", "params:dev_url", "params:dev_descricao"],
            outputs="df_dev"
        ),
        node(
            nodes.download_data,
            inputs=["params:prod_caminho_salvo", "params:prod_url", "params:prod_descricao"],
            outputs="df_prod"
        ),
        node(
            nodes.descricao_dados,
            inputs=["df_dev","params:dev_descricao_explor"],
            outputs="df_explorado_dev"
        ),
        node(
            nodes.descricao_dados,
            inputs=["df_prod", "params:prod_descricao_explor"],
            outputs="df_explorado_prod"
        )
    ])
