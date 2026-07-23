from pathlib import Path
import sys

from PIL import Image

from defect_detection.entity.config_entity import DataValidationConfig,DatasetPaths
from defect_detection.logger import logger
from defect_detection.exception import CustomException

class DataValidation:

    def __init__(
        self,
        config: DataValidationConfig
    ):

        self.config = config
        self.validation_errors = []

    def _get_dataset_paths(self) -> DatasetPaths:

        dataset_root = (
            self.config.dataset_dir /
            self.config.dataset_structure.root_dir
        )

        train_dir = (
            dataset_root /
            self.config.dataset_structure.train_dir
        )

        validation_dir = (
            dataset_root /
            self.config.dataset_structure.validation_dir
        )

        paths = DatasetPaths(
            dataset_root=dataset_root,

            train_dir=train_dir,
            validation_dir=validation_dir,

            train_images=(
                train_dir /
                self.config.dataset_structure.images_dir
            ),

            train_annotations=(
                train_dir /
                self.config.dataset_structure.annotations_dir
            ),

            validation_images=(
                validation_dir /
                self.config.dataset_structure.images_dir
            ),

            validation_annotations=(
                validation_dir /
                self.config.dataset_structure.annotations_dir
            )
        )

        return paths

    def validate_dataset_root(self) -> bool:

        paths = self._get_dataset_paths()

        if not paths.dataset_root.exists():

            self.validation_errors.append(
                f"Dataset root not found: {paths.dataset_root}"
            )

            return False

        logger.info("Dataset root validation passed.")

        return True
    
    def validate_split_directories(self) -> bool:

        paths = self._get_dataset_paths()

        if not paths.train_dir.exists():

            self.validation_errors.append(
                f"Missing directory: {paths.train_dir}"
            )

        if not paths.validation_dir.exists():

            self.validation_errors.append(
                f"Missing directory: {paths.validation_dir}"
            )

        if self.validation_errors:
            return False

        logger.info("Split directory validation passed.")

        return True
    
        
    def validate_images_and_annotations_directories(self) -> bool:

        paths = self._get_dataset_paths()

        directories = {
            "Train Images": paths.train_images,
            "Train Annotations": paths.train_annotations,
            "Validation Images": paths.validation_images,
            "Validation Annotations": paths.validation_annotations,
        }

        for name, directory in directories.items():

            if not directory.exists():

                self.validation_errors.append(
                    f"{name} directory not found: {directory}"
                )

        if self.validation_errors:
            return False

        logger.info(
            "Images and annotations directory validation passed."
        )

        return True
    
    def validate_class_folders(self) -> bool:

        paths = self._get_dataset_paths()

        image_directories = {
            "Train": paths.train_images,
            "Validation": paths.validation_images,
        }

        for split_name, image_dir in image_directories.items():

            for class_name in self.config.expected_classes:

                class_path = image_dir / class_name

                if not class_path.exists():

                    self.validation_errors.append(
                        f"{split_name}: Missing class folder '{class_name}' ({class_path})"
                    )

        if self.validation_errors:
            return False

        logger.info("Class folder validation passed.")

        return True
    
    def validate_image_files(self) -> bool:

        paths = self._get_dataset_paths()

        image_directories = {
            "Train": paths.train_images,
            "Validation": paths.validation_images,
        }

        for split_name, image_dir in image_directories.items():

            for class_name in self.config.expected_classes:

                class_dir = image_dir / class_name

                image_files = [
                    file
                    for file in class_dir.iterdir()
                    if file.is_file()
                ]

                if not image_files:

                    self.validation_errors.append(
                        f"{split_name}: '{class_name}' contains no images."
                    )

                    continue

                for image in image_files:

                    if image.suffix.lower() not in self.config.allowed_image_extensions:

                        self.validation_errors.append(
                            f"{split_name}: {image.name} has unsupported extension '{image.suffix}'."
                        )

        if self.validation_errors:
            return False

        logger.info("Image file validation passed.")

        return True

    def validate_image_integrity(self) -> bool:
        paths = self._get_dataset_paths()
        image_directories = {
            "Train": paths.train_images,
            "Validation": paths.validation_images,
        }

        for split_name, image_dir in image_directories.items():

            for class_name in self.config.expected_classes:
                class_dir = image_dir / class_name

                image_files = [
                    file
                    for file in class_dir.iterdir()
                    if file.is_file()
                ]
                for image_path in image_files:
                    try:

                        with Image.open(image_path) as image:

                            image.verify()

                    except Exception:

                        self.validation_errors.append(
                            f"{split_name}: Corrupted image: {image_path}"
                        )
        if self.validation_errors:
            return False

        logger.info("Image integrity validation passed.")

        return True

    def validate_annotation_files(self) -> bool:

        paths = self._get_dataset_paths()

        directory_pairs = {
            "Train": (
                paths.train_images,
                paths.train_annotations,
            ),
            "Validation": (
                paths.validation_images,
                paths.validation_annotations,
            ),
        }

        for split_name, (image_root, annotation_root) in directory_pairs.items():

            for class_name in self.config.expected_classes:

                image_dir = image_root / class_name
                annotation_dir = annotation_root / class_name

                # Validate annotation directory
                if not annotation_dir.exists():

                    self.validation_errors.append(
                        f"{split_name}: Missing annotation directory: {annotation_dir}"
                    )
                    continue

                # Collect image names (without extension)
                image_names = {
                    image.stem
                    for image in image_dir.iterdir()
                    if image.is_file()
                }

                # Collect annotation names (without extension)
                annotation_names = set()

                for annotation in annotation_dir.iterdir():

                    if not annotation.is_file():
                        continue

                    # Validate annotation extension
                    if (
                        annotation.suffix.lower()
                        not in self.config.allowed_annotation_extensions
                    ):

                        self.validation_errors.append(
                            f"{split_name}: Unsupported annotation file "
                            f"'{annotation.name}'"
                        )
                        continue

                    annotation_names.add(annotation.stem)

                # Missing XML
                missing_annotations = image_names - annotation_names

                for image_name in sorted(missing_annotations):

                    self.validation_errors.append(
                        f"{split_name}: Missing annotation for image "
                        f"'{image_name}'"
                    )

                # Extra XML
                extra_annotations = annotation_names - image_names

                for annotation_name in sorted(extra_annotations):

                    self.validation_errors.append(
                        f"{split_name}: Extra annotation "
                        f"'{annotation_name}.xml'"
                    )

        if self.validation_errors:
            return False

        logger.info(
            "Annotation validation passed."
        )

        return True





    
    def initiate_data_validation(self) -> bool:

        self.validation_errors.clear()

        logger.info("Starting Data Validation...")

        if not self.validate_dataset_root():
            return False

        if not self.validate_split_directories():
            return False

        if not self.validate_images_and_annotations_directories():
            return False
        if not self.validate_class_folders():
            return False
        if not self.validate_image_files():
            return False
        if not self.validate_image_integrity():
            return False
        if not self.validate_annotation_files():
            return False

        logger.info(
            "Data Validation completed successfully."
        )

        return True