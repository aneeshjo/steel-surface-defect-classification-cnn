from defect_detection.components.data_validation import DataValidation
from defect_detection.config.configuration import ConfigurationManager

config_manager = ConfigurationManager()

validation_config = config_manager.get_data_validation_config()

validator = DataValidation(validation_config)

status = validator.initiate_data_validation()

print(status)