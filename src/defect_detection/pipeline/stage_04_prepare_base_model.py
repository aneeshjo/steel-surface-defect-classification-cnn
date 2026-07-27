from defect_detection import logger

from defect_detection.components.prepare_base_model import (
    PrepareBaseModel
)

from defect_detection.config.configuration import (
    ConfigurationManager
)

from defect_detection.entity.artifacts_entity import (
    DataTransformationArtifacts
)

STAGE_NAME = "Prepare Base Model Stage"


class PrepareBaseModelTrainingPipeline:

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

        prepare_base_model_config = (
            config.get_prepare_base_model_config()
        )

        prepare_base_model = PrepareBaseModel(
            config=prepare_base_model_config
        )

        model = prepare_base_model.prepare_base_model(
            data_transformation_artifacts=data_transformation_artifacts
        )

        logger.info(
            f"Model saved at : {prepare_base_model_config.model_path}"
        )

        logger.info(
            f">>>>>> {STAGE_NAME} Completed <<<<<<"
        )

        return model