import tensorflow as tf

from defect_detection.entity.config_entity import ModelTrainerConfig
from defect_detection.entity.artifacts_entity import DataTransformationArtifacts
from defect_detection.logger import logger


class ModelTrainer:

    def __init__(
        self,
        config: ModelTrainerConfig
    ):
        self.config = config

    def load_model(self) -> tf.keras.Model:

        logger.info(
            "Loading base CNN model..."
        )

        model = tf.keras.models.load_model(
            self.config.base_model_path
        )

        return model

    def train_model(
        self,
        model: tf.keras.Model,
        data_transformation_artifacts: DataTransformationArtifacts
    ) -> tf.keras.Model:

        logger.info(
            "Training CNN model..."
        )

        model.fit(
            data_transformation_artifacts.train_dataset,
            validation_data=data_transformation_artifacts.validation_dataset,
            epochs=self.config.epochs
        )

        logger.info(
            "Model training completed."
        )

        return model

    def save_model(
        self,
        model: tf.keras.Model
    ) -> None:

        logger.info(
            "Saving trained CNN model..."
        )

        model.save(
            self.config.trained_model_path
        )

        logger.info(
            f"Trained model saved at: {self.config.trained_model_path}"
        )

    def train(
        self,
        data_transformation_artifacts: DataTransformationArtifacts
    ) -> tf.keras.Model:

        logger.info(
            "Loading base model..."
        )

        model = self.load_model()

        model = self.train_model(
            model=model,
            data_transformation_artifacts=data_transformation_artifacts
        )

        self.save_model(
            model=model
        )

        return model
