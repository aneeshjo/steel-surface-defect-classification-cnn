from dataclasses import dataclass
import tensorflow as tf


@dataclass(frozen=True)
class DataTransformationArtifacts:
    train_dataset: tf.data.Dataset
    validation_dataset: tf.data.Dataset
    class_names: list[str]