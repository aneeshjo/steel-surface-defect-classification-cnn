from defect_detection.pipeline.prediction_pipeline import PredictionPipeline


def main():

    image_path = "E:\Project_Works\ML_Projects\Deep Learning\CNN\Computer-Vision-Defect-Detection\samples\inclusion_242.jpg"   # Replace with your test image

    prediction_pipeline = PredictionPipeline()

    result = prediction_pipeline.get_prediction(
        image_path=image_path
    )

    print("\nPrediction Result")
    print("-" * 40)
    print(f"Predicted Class : {result['predicted_class']}")
    print(f"Confidence      : {result['confidence']:.2%}")

    print("\nClass Probabilities")

    for class_name, probability in zip(
        prediction_pipeline.config.class_names,
        result["probabilities"]
    ):
        print(f"{class_name:<20}: {probability:.4f}")


if __name__ == "__main__":
    main()