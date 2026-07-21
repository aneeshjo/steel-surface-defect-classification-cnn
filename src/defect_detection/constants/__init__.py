from pathlib import Path

# ==========================================================
# Project Root
# ==========================================================
ROOT_DIR=Path.cwd()

# ==========================================================
# Configuration Files
# ==========================================================

CONFIG_FILE_PATH=Path("config/config.yaml")
PARAMS_FILE_PATH=Path("config/params.yaml")
SCHEMA_FILE_PATH=Path("config/schema.yaml")

# ==========================================================
# Default Directories
# ==========================================================

ARTIFACTS_DIR = Path("artifacts")

LOGS_DIR = Path("logs")

MODELS_DIR = Path("models")

REPORTS_DIR = Path("reports")

NOTEBOOKS_DIR = Path("notebooks")

DATA_DIR = Path("data")