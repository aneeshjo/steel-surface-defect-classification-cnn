import sys
from pathlib import Path

from defect_detection.constants import (
    CONFIG_FILE_PATH
)
from defect_detection.entity.config_entity import (
    DataIngestionConfig
)
from defect_detection.utils.common import (
    read_yaml,
    create_directories
)


class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH):
        self._config=read_yaml(config_filepath)
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