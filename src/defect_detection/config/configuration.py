import sys
from pathlib import Path

from defect_detection.constants import (
    CONFIG_FILE_PATH,
    SCHEMA_FILE_PATH,
    PARAMS_FILE_PATH
)
from defect_detection.entity.config_entity import (
    DataIngestionConfig,
    DatasetStructureConfig,
    DataValidationConfig,
    DataTransformationConfig
)
from defect_detection.utils.common import (
    read_yaml,
    create_directories
)


class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,schema_filepath=SCHEMA_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self._config=read_yaml(config_filepath)
        self._schema=read_yaml(schema_filepath)
        self._params=read_yaml(params_filepath)
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
    
    def get_data_validation_config(self) -> DataValidationConfig:

        config = self._config.data_validation
        schema = self._schema

        create_directories([Path(config.root_dir)])

        dataset_structure = DatasetStructureConfig(
            root_dir=schema.DATASET_STRUCTURE.ROOT_DIR,
            train_dir=schema.DATASET_STRUCTURE.TRAIN_DIR,
            validation_dir=schema.DATASET_STRUCTURE.VALIDATION_DIR,
            images_dir=schema.DATASET_STRUCTURE.IMAGES_DIR,
            annotations_dir=schema.DATASET_STRUCTURE.ANNOTATIONS_DIR,
        )

        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            dataset_dir=Path(config.dataset_dir),
            validation_status_file=Path(config.validation_status_file),

            dataset_structure=dataset_structure,

            expected_classes=list(schema.EXPECTED_CLASSES),
            allowed_image_extensions=list(schema.ALLOWED_IMAGE_EXTENSIONS),
            allowed_annotation_extensions=list(
                schema.ALLOWED_ANNOTATION_EXTENSIONS
            )
        )
    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self._config.data_transformation
        params = self._params

        create_directories([Path(config.root_dir)])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),

            train_data_path=Path(config.train_data_path),
            validation_data_path=Path(config.validation_data_path),

            image_size=tuple(params.IMAGE_SIZE),
            batch_size=params.BATCH_SIZE,
            seed=params.SEED,

            train_shuffle=params.TRAIN_SHUFFLE,
            validation_shuffle=params.VALIDATION_SHUFFLE,
        )

        return data_transformation_config