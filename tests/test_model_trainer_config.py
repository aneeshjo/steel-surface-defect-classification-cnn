from defect_detection.components.model_trainer import ModelTrainer
from defect_detection.config.configuration import ConfigurationManager


config = ConfigurationManager()

trainer_config = config.get_model_trainer_config()

trainer = ModelTrainer(
    trainer_config
)

model = trainer.load_model()

model.summary()