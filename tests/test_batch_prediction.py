from pathlib import Path

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from defect_detection.pipeline.prediction_pipeline import PredictionPipeline


def main():

    prediction_pipeline = PredictionPipeline()

    test_dir = Path(
        r"artifacts\data_ingestion\data\NEU-DET\validation\images"
    )

    results = []

    for class_dir in sorted(test_dir.iterdir()):

        if not class_dir.is_dir():
            continue

        actual_class = class_dir.name

        for image_path in class_dir.glob("*"):

            if image_path.suffix.lower() not in [
                ".jpg",
                ".jpeg",
                ".png",
                ".bmp",
            ]:
                continue

            prediction = prediction_pipeline.get_prediction(
                str(image_path)
            )

            results.append(
                {
                    "image": image_path.name,
                    "actual": actual_class,
                    "predicted": prediction["predicted_class"],
                    "confidence": prediction["confidence"],
                }
            )
    print(f"Number of predictions: {len(results)}")

    results_df = pd.DataFrame(results)

    print("\nFirst Five Predictions\n")
    print(results_df.head())

    print("\nAccuracy")
    print(
        accuracy_score(
            results_df["actual"],
            results_df["predicted"],
        )
    )

    print("\nClassification Report\n")
    print(
        classification_report(
            results_df["actual"],
            results_df["predicted"],
        )
    )

    print("\nConfusion Matrix\n")
    print(
        confusion_matrix(
            results_df["actual"],
            results_df["predicted"],
        )
    )
  

    output_dir = Path("artifacts/model_evaluation")
    output_dir.mkdir(parents=True, exist_ok=True)

    results_df.to_csv(
    output_dir / "prediction_results.csv",
    index=False
)

 

    print("\nPrediction results saved successfully.")

    sample_image = next(
        Path(
            r"artifacts\data_ingestion\data\NEU-DET\validation\images\crazing"
        ).glob("*")
    )

    prediction = prediction_pipeline.get_prediction(str(sample_image))

    print("\nSample Image:", sample_image.name)
    print("Prediction:", prediction["predicted_class"])
    print("Confidence:", prediction["confidence"])
    print("Probabilities:")

    for cls, prob in zip(
        prediction_pipeline.config.class_names,
        prediction["probabilities"]
    ):
        print(f"{cls:20} : {prob:.6f}")


if __name__ == "__main__":
    main()