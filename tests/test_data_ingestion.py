from defect_detection.components.data_ingestion import DataIngestion
from defect_detection.config.configuration import ConfigurationManager

config = ConfigurationManager()

ingestion_config = config.get_data_ingestion_config()

ingestion = DataIngestion(ingestion_config)

ingestion.initiate_data_ingestion()