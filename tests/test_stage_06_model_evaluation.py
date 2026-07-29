from defect_detection.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline
)

from defect_detection.pipeline.stage_04_prepare_base_model import (
    PrepareBaseModelTrainingPipeline
)

from defect_detection.pipeline.stage_05_model_trainer import (
    ModelTrainingPipeline
)

from defect_detection.pipeline.stage_06_model_evaluation import (
    ModelEvaluationPipeline
)


def main():

    # Stage 03
    stage_03 = DataTransformationTrainingPipeline()

    data_transformation_artifacts = stage_03.main()

    # Stage 04
    stage_04 = PrepareBaseModelTrainingPipeline()

    stage_04.main(
        data_transformation_artifacts=data_transformation_artifacts
    )

    # Stage 05
    stage_05 = ModelTrainingPipeline()

    stage_05.main(
        data_transformation_artifacts=data_transformation_artifacts
    )

    # Stage 06
    stage_06 = ModelEvaluationPipeline()

    metrics = stage_06.main(
        data_transformation_artifacts=data_transformation_artifacts
    )

    print("\nEvaluation Metrics")
    print(metrics)


if __name__ == "__main__":
    main()