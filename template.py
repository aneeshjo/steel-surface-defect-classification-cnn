from pathlib import Path
import logging

# ==========================================================
# Logging Configuration
# ==========================================================
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

# ==========================================================
# Project Name (Change only this for new projects)
# ==========================================================
project_name = "defect_detection"

# ==========================================================
# Files & Folder Structure
# ==========================================================
list_of_files = [

    # ---------------- GitHub ----------------
    ".github/workflows/.gitkeep",

    # ---------------- Source ----------------
    f"src/{project_name}/__init__.py",

    # Components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/prepare_base_model.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",

    # Configuration
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    # Constants
    f"src/{project_name}/constants/__init__.py",

    # Entity
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    # Pipeline
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_prepare_base_model.py",
    f"src/{project_name}/pipeline/stage_05_model_trainer.py",
    f"src/{project_name}/pipeline/stage_06_model_evaluation.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",

    # Utilities
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/image_utils.py",
    f"src/{project_name}/utils/visualization.py",

    # Logger & Exception
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",

    # ---------------- Config ----------------
    "config/config.yaml",
    "config/params.yaml",
    "config/schema.yaml",

    # ---------------- Data ----------------
    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",

    # ---------------- Artifacts ----------------
    "artifacts/.gitkeep",

    # ---------------- Logs ----------------
    "logs/.gitkeep",

    # ---------------- Models ----------------
    "models/.gitkeep",

    # ---------------- MLflow ----------------
    "mlruns/.gitkeep",

    # ---------------- Reports ----------------
    "reports/figures/.gitkeep",
    "reports/metrics/.gitkeep",

    # ---------------- Notebooks ----------------
    "notebooks/.gitkeep",

    # ---------------- Research ----------------
    "research/.gitkeep",

    # ---------------- Static ----------------
    "static/css/.gitkeep",
    "static/js/.gitkeep",
    "static/images/.gitkeep",

    # ---------------- Templates ----------------
    "templates/index.html",

    # ---------------- Tests ----------------
    "tests/__init__.py",
    "tests/test_config.py",
    "tests/test_data_ingestion.py",
    "tests/test_model.py",
    "tests/test_prediction.py",

    # ---------------- Root Files ----------------
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "Dockerfile",
    "docker-compose.yml",
    ".env.example",
    ".gitignore",
    "README.md",
    "LICENSE"
]

# ==========================================================
# Create Files & Directories
# ==========================================================
for filepath in list_of_files:

    filepath = Path(filepath)

    filedir = filepath.parent

    if filedir != Path(""):

        filedir.mkdir(
            parents=True,
            exist_ok=True
        )

        logging.info(f"Ensured directory exists: {filedir}")

    if not filepath.exists():

        filepath.touch(exist_ok=True)

        logging.info(f"Created file: {filepath}")

    else:

        logging.info(f"Already exists: {filepath}")

logging.info("=" * 60)
logging.info("Project structure created successfully.")
logging.info("=" * 60)