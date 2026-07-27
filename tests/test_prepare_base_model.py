from defect_detection.components.prepare_base_model import PrepareBaseModel
from defect_detection.config.configuration import ConfigurationManager
from defect_detection.entity.artifacts_entity import DataTransformationArtifacts


def main():

    # Configuration
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()

    # Component
    prepare_base_model = PrepareBaseModel(
        config=prepare_base_model_config
    )

    # Dummy artifacts (only num_classes is used)
    transformation_artifacts = DataTransformationArtifacts(
        train_dataset=None,
        validation_dataset=None,
        class_names=[
            "crazing",
            "inclusion",
            "patches",
            "pitted_surface",
            "rolled_in_scale",
            "scratches"
        ],
        num_classes=6
    )

    model = prepare_base_model.prepare_base_model(
        transformation_artifacts
    )

    model.summary()


if __name__ == "__main__":
    main()