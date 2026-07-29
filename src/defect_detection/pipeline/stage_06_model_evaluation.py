from defect_detection.logger import logger

from defect_detection.config.configuration import (
    ConfigurationManager
)

from defect_detection.components.model_evaluation import (
    ModelEvaluation
)

from defect_detection.entity.artifacts_entity import (
    DataTransformationArtifacts
)


STAGE_NAME = "Model Evaluation Stage"


class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(
        self,
        data_transformation_artifacts: DataTransformationArtifacts
    ) -> dict:

        logger.info(
            f">>>>>> {STAGE_NAME} Started <<<<<<"
        )

        config = ConfigurationManager()

        model_evaluation_config = (
            config.get_model_evaluation_config()
        )

        model_evaluation = ModelEvaluation(
            config=model_evaluation_config
        )

        metrics = model_evaluation.evaluate(
            data_transformation_artifacts=data_transformation_artifacts
        )

        logger.info(
            f">>>>>> {STAGE_NAME} Completed <<<<<<"
        )

        return metrics