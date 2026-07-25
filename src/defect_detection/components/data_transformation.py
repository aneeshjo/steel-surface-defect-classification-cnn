import tensorflow as tf

from defect_detection import logger
from defect_detection.entity.config_entity import DataTransformationConfig
from defect_detection.entity.artifacts_entity import (
    DataTransformationArtifacts
)


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def create_datasets(self):

        logger.info("Creating TensorFlow training dataset...")

        train_dataset = tf.keras.utils.image_dataset_from_directory(
            directory=self.config.train_data_path,
            image_size=self.config.image_size,
            batch_size=self.config.batch_size,
            shuffle=self.config.train_shuffle,
            seed=self.config.seed,
        )

        logger.info("Creating TensorFlow validation dataset...")

        validation_dataset = tf.keras.utils.image_dataset_from_directory(
            directory=self.config.validation_data_path,
            image_size=self.config.image_size,
            batch_size=self.config.batch_size,
            shuffle=self.config.validation_shuffle,
        )

        logger.info("Datasets created successfully.")

        logger.info(f"Classes found : {train_dataset.class_names}")
        class_names = train_dataset.class_names

        artifacts = DataTransformationArtifacts(
            train_dataset=train_dataset,
            validation_dataset=validation_dataset,
            class_names=class_names,
            num_classes=len(class_names),
        )

        return artifacts