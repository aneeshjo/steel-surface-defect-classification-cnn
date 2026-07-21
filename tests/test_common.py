from pathlib import Path

from defect_detection.utils.common import (
    create_directories,
    read_yaml,
)

from defect_detection.constants import CONFIG_FILE_PATH

create_directories(
    [
        Path("artifacts/test"),
        Path("artifacts/sample")
    ]
)

config = read_yaml(CONFIG_FILE_PATH)

print(config)