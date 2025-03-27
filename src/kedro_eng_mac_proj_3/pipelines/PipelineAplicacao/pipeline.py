"""
This is a boilerplate pipeline 'PipelineAplicacao'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.pipeline_aplicacao,
            inputs=["data_filtered_prod", "params:url_api"],
            outputs=None
        )
    ])
