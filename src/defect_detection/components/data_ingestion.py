import sys
import shutil
import zipfile

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

            # Check whether the source dataset exists
            if not source_path.exists():
                raise FileNotFoundError(
                f"Source dataset not found: {source_path}"
            )

            # First-time copy
            if not destination_path.exists():
                shutil.copy2(source_path, destination_path)
                logger.info(
                    f"Dataset copied successfully to {destination_path}"
                )
                return
            
            # Compare modification times
            source_modified = source_path.stat().st_mtime
            destination_modified = destination_path.stat().st_mtime

            if source_modified > destination_modified:
                shutil.copy2(source_path, destination_path)
                logger.info(
                    "Source dataset has been updated. Destination dataset replaced."
                )
            else:
                logger.info(
                    "Destination dataset is already up-to-date. Skipping copy."
                )


        except Exception as e:

            raise CustomException(e, sys)
        
    def extract_zipfile(self):
        try:
            zip_filepath=self.config.local_data_file
            unzip_dir=self.config.unzip_dir
            # Ensure the ZIP file exists
            if not zip_filepath.exists():
                raise FileNotFoundError(
                    f"ZIP file not found: {zip_filepath}"
                )
            # Skip extraction only if directory exists and contains files
            if unzip_dir.exists() and any(unzip_dir.iterdir()):
                logger.info(
                    "Dataset already extracted. Skipping extraction."
                )
                return

            unzip_dir.mkdir(parents=True, exist_ok=True)

            with zipfile.ZipFile(zip_filepath, "r") as zip_ref:
                zip_ref.extractall(unzip_dir)

            logger.info(
                f"Dataset extracted successfully to {unzip_dir}"
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_ingestion(self):
        logger.info("Starting Data Ingestion...")

        self.download_file()

        self.extract_zipfile()

        logger.info("Data Ingestion completed successfully.")