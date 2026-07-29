import numpy as np
import tensorflow as tf

from PIL import Image

from defect_detection.config.configuration import ConfigurationManager


class PredictionPipeline:

    def __init__(self):

        config_manager = ConfigurationManager()

        self.config = config_manager.get_prediction_config()

        self.load_model()

    def load_model(self) -> None:
        """
        Load the trained CNN model.
        """

        self.model = tf.keras.models.load_model(
            self.config.trained_model_path
        )

    def preprocess_image(
        self,
        image_path: str
    ) -> np.ndarray:
        """
        Preprocess an input image before prediction.

        Steps:
        1. Open image
        2. Convert to RGB
        3. Resize
        4. Convert to NumPy array
        5. Normalize
        6. Add batch dimension
        """

        image = Image.open(image_path)

        image = image.convert("RGB")

        image = image.resize(
            tuple(self.config.image_size[:2])
        )

        image = np.array(image)

        image = image.astype(np.float32) / 255.0

        image = np.expand_dims(
            image,
            axis=0
        )

        return image

    def predict(
        self,
        image_path: str
    ) -> np.ndarray:
        """
        Perform prediction on an image.
        """

        image = self.preprocess_image(
            image_path=image_path
        )

        predictions = self.model.predict(
            image,
            verbose=0
        )

        return predictions

    def get_prediction(
        self,
        image_path: str
    ) -> dict:
        """
        Return predicted class, confidence,
        and probability distribution.
        """

        predictions = self.predict(
            image_path=image_path
        )

        predicted_index = int(
            np.argmax(predictions[0])
        )

        confidence = float(
            np.max(predictions[0])
        )

        predicted_class = self.config.class_names[
            predicted_index
        ]

        return {
            "predicted_class": predicted_class,
            "confidence": confidence,
            "probabilities": predictions[0].tolist()
        }