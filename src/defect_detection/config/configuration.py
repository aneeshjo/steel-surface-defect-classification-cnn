import sys
from pathlib import Path

from defect_detection.constants import (
    CONFIG_FILE_PATH,
    SCHEMA_FILE_PATH
)
from defect_detection.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig
)
from defect_detection.utils.common import (
    read_yaml,
    create_directories
)


class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,schema_filepath=SCHEMA_FILE_PATH):
        self._config=read_yaml(config_filepath)
        self._schema=read_yaml(schema_filepath)
        create_directories([Path(self._config.artifacts_root)])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self._config.data_ingestion
        create_directories([Path(config.root_dir)])

        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
    
    def get_data_validation_config(self)->DataValidationConfig:
        config=self._config.data_validation
        schema=self._schema
        create_directories(
            [
                Path(config.root_dir)
            ]
        )
        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            dataset_dir=Path(config.dataset_dir),
            validation_status_file=Path(config.validation_status_file),
            expected_classes=list(schema.EXPECTED_CLASSES),
            allowed_image_extensions=list(schema.ALLOWED_IMAGE_EXTENSIONS)
        )

