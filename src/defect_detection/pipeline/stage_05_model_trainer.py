from defect_detection import logger

from defect_detection.components.model_trainer import (
    ModelTrainer
)

from defect_detection.config.configuration import (
    ConfigurationManager
)

from defect_detection.entity.artifacts_entity import (
    DataTransformationArtifacts
)


STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(
        self,
        data_transformation_artifacts: DataTransformationArtifacts
    ):

        logger.info(
            f">>>>>> {STAGE_NAME} Started <<<<<<"
        )

        config = ConfigurationManager()

        model_trainer_config = (
            config.get_model_trainer_config()
        )

        model_trainer = ModelTrainer(
            config=model_trainer_config
        )

        model = model_trainer.train(
            data_transformation_artifacts=data_transformation_artifacts
        )

        logger.info(
            f">>>>>> {STAGE_NAME} Completed <<<<<<"
        )

        return model