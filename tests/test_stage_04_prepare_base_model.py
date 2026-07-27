from defect_detection.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline
)

from defect_detection.pipeline.stage_04_prepare_base_model import (
    PrepareBaseModelTrainingPipeline
)


def main():

    # Stage 03
    stage_03 = DataTransformationTrainingPipeline()

    transformation_artifacts = stage_03.main()

    # Stage 04
    stage_04 = PrepareBaseModelTrainingPipeline()

    model = stage_04.main(
        transformation_artifacts
    )

    model.summary()


if __name__ == "__main__":
    main()