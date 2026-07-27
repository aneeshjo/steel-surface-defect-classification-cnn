from pathlib import Path
import tensorflow as tf

from defect_detection.entity.config_entity import PrepareBaseModelConfig
from defect_detection.entity.artifacts_entity import DataTransformationArtifacts
from defect_detection.logger import logger

class PrepareBaseModel:

    def __init__(
        self,
        config: PrepareBaseModelConfig
    ):
        self.config = config

    def build_model(
        self,
        transformation_artifacts: DataTransformationArtifacts
    ) -> tf.keras.Model:
        
        model = tf.keras.Sequential([
            tf.keras.layers.Input(
            shape=self.config.image_size
            ),

            tf.keras.layers.Conv2D(
                filters=32,
                kernel_size=(3,3),
                padding="same",
                activation="relu"
            ),

            tf.keras.layers.MaxPooling2D(
                pool_size=(2,2)
            ),

            tf.keras.layers.Conv2D(
                filters=64,
                kernel_size=(3,3),
                padding="same",
                activation="relu"
            ),

            tf.keras.layers.MaxPooling2D(
                pool_size=(2,2)
            ),
            tf.keras.layers.Conv2D(
                filters=128,
                kernel_size=(3,3),
                padding="same",
                activation="relu"
            ),

            tf.keras.layers.MaxPooling2D(
                pool_size=(2,2)
            ),
            tf.keras.layers.Flatten(),

            tf.keras.layers.Dense(
                256,
                activation="relu"
            ),

            tf.keras.layers.Dropout(
                self.config.dropout_rate
            ),

            tf.keras.layers.Dense(
                transformation_artifacts.num_classes,
                activation="softmax"
            )
        ])

        return model
    def compile_model(self,model:tf.keras.Model)-> tf.keras.Model:

        model.compile(
        
                    optimizer=tf.keras.optimizers.Adam(
                        learning_rate=self.config.learning_rate
                    ),
        
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        
                    metrics=[
                        "accuracy"
                    ]
                )
        return model
    def save_model(self,model:tf.keras.Model)->tf.keras.Model:
        model.save(
                    self.config.model_path
                ) 
        logger.info(
                    f"Model saved at: {self.config.model_path}"
                )
        
        return model
        
    def prepare_base_model(
    self,
    data_transformation_artifacts: DataTransformationArtifacts
    ):
        logger.info(
                    "Building custom CNN model..."
                )   
                
        
        model = self.build_model(
                transformation_artifacts=data_transformation_artifacts
                )
        logger.info(
            "Compiling CNN model..."
        )

        model = self.compile_model(
            model
        )

        logger.info(
            "Saving CNN model..."
        )

        self.save_model(
            model
        )

        return model