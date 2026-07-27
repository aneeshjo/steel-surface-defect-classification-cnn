from dataclasses import dataclass
from pathlib import Path


# ==============================
# Data Ingestion
# ==============================

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


# ==============================
# Dataset Structure Configuration
# ==============================

@dataclass(frozen=True)
class DatasetStructureConfig:
    root_dir: str
    train_dir: str
    validation_dir: str
    images_dir: str
    annotations_dir: str


# ==============================
# Runtime Dataset Paths
# ==============================

@dataclass(frozen=True)
class DatasetPaths:
    dataset_root: Path

    train_dir: Path
    validation_dir: Path

    train_images: Path
    train_annotations: Path

    validation_images: Path
    validation_annotations: Path


# ==============================
# Data Validation Configuration
# ==============================

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    dataset_dir: Path
    validation_status_file: Path

    dataset_structure: DatasetStructureConfig

    expected_classes: list[str]
    allowed_image_extensions: list[str]
    allowed_annotation_extensions: list[str]

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path

    train_data_path: Path
    validation_data_path: Path

    image_size: tuple
    batch_size: int
    seed: int

    train_shuffle: bool
    validation_shuffle: bool

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    model_path: Path

    image_size: tuple

    learning_rate: float
    dropout_rate: float