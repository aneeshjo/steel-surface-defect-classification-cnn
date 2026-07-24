from defect_detection import logger
from defect_detection.components.data_validation import DataValidation
from defect_detection.config.configuration import ConfigurationManager


STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")

        config = ConfigurationManager()

        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(
            config=data_validation_config
        )

        validation_status = data_validation.initiate_data_validation()

        if validation_status:
            logger.info("Dataset validation completed successfully.")
        else:
            logger.warning("Dataset validation failed.")

        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")