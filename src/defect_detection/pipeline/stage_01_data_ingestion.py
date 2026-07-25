from defect_detection import logger
from defect_detection.components.data_ingestion import DataIngestion
from defect_detection.config.configuration import ConfigurationManager


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")

        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(
            config=data_ingestion_config
        )

        data_ingestion.download_file()

        data_ingestion.extract_zipfile()

        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")