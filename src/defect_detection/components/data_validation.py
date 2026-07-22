from pathlib import Path
import sys

from defect_detection.entity.config_entity import DataValidationConfig
from defect_detection.logger import logger
from defect_detection.exception import CustomException

class DataValidation:

    def __init__(
        self,
        config: DataValidationConfig
    ):

        self.config = config
        self.validation_errors = []

    def validate_dataset_directory(self):

        dataset_dir = self.config.dataset_dir

        if not dataset_dir.exists():

            self.validation_errors.append(
                f"Dataset directory not found: {dataset_dir}"
            )

            return False

        logger.info(
            "Dataset directory validation passed."
        )

        return True
    
    def initiate_data_validation(self):

        logger.info(
            "Starting Data Validation..."
        )

        if not self.validate_dataset_directory():

            logger.error(
                "Dataset directory validation failed."
            )

            return False

        logger.info(
            "Data Validation completed successfully."
        )

        return True
