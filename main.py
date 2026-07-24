from defect_detection import logger
from defect_detection.exception import CustomException

from defect_detection.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from defect_detection.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from defect_detection.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)


if __name__ == "__main__":

    try:

        DataIngestionTrainingPipeline().main()

        DataValidationTrainingPipeline().main()

        DataTransformationTrainingPipeline().main()

    except Exception as e:
        logger.exception(e)
        raise CustomException(e)