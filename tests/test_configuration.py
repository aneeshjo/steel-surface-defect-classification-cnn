from defect_detection.config.configuration import ConfigurationManager

config_manager = ConfigurationManager()

config = config_manager.get_data_ingestion_config()

print(config)