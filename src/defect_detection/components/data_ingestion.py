import sys
import shutil

from pathlib import Path

from defect_detection.entity.config_entity import DataIngestionConfig
from defect_detection.logger import logger
from defect_detection.exception import CustomException

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        try:
            source_path=Path(self.config.source_url)
            destination_path=Path(self.config.local_data_file)

            if destination_path.exists():
                logger.info(
                    "Dataset already exists. Skipping copy."
                )
                return
            shutil.copy(
                src=source_path,
                dst=destination_path
            )
            logger.info(
            f"Dataset copied to {destination_path}"
        )

        except Exception as e:

            raise CustomException(e, sys)