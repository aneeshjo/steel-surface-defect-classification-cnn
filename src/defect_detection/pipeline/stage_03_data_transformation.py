from defect_detection import logger
from defect_detection.components.data_transformation import DataTransformation
from defect_detection.config.configuration import ConfigurationManager


STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")

        config = ConfigurationManager()

        data_transformation_config = (
            config.get_data_transformation_config()
        )

        data_transformation = DataTransformation(
            config=data_transformation_config
        )

        artifacts = data_transformation.create_datasets()

        logger.info(
            f"Number of Classes : {artifacts.num_classes}"
        )

        logger.info(
            f"Classes : {artifacts.class_names}"
        )

        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")

        return artifacts
if __name__ == "__main__":
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()