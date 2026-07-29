import json

import tensorflow as tf

from defect_detection.entity.config_entity import (
    ModelEvaluationConfig
)

from defect_detection.entity.artifacts_entity import (
    DataTransformationArtifacts
)

from defect_detection.logger import logger

class ModelEvaluation:

    def __init__(
        self,
        config: ModelEvaluationConfig
    ):

        self.config = config

    def load_model(self) -> tf.keras.Model:

        logger.info(
            "Loading trained CNN model..."
        )

        model = tf.keras.models.load_model(
            self.config.trained_model_path
        )

        logger.info(
            "Trained model loaded successfully."
        )

        return model

    def evaluate_model(
        self,
        model: tf.keras.Model,
        data_transformation_artifacts: DataTransformationArtifacts
    ) -> dict:

        logger.info(
            "Evaluating CNN model..."
        )

        loss, accuracy = model.evaluate(
            data_transformation_artifacts.validation_dataset,
            verbose=1
        )

        metrics = {
            "loss": float(loss),
            "accuracy": float(accuracy)
        }

        logger.info(
            f"Evaluation Results : {metrics}"
        )

        return metrics

    def save_metrics(
        self,
        metrics: dict
    ) -> None:

        logger.info(
            "Saving evaluation metrics..."
        )

        with open(
            self.config.metrics_file_path,
            "w"
        ) as file:

            json.dump(
                metrics,
                file,
                indent=4
            )

        logger.info(
            f"Metrics saved at: {self.config.metrics_file_path}"
        )

    def evaluate(
        self,
        data_transformation_artifacts: DataTransformationArtifacts
    ) -> dict:

        logger.info(
            "Loading trained model..."
        )

        model = self.load_model()

        metrics = self.evaluate_model(
            model=model,
            data_transformation_artifacts=data_transformation_artifacts
        )

        self.save_metrics(
            metrics=metrics
        )

        return metrics