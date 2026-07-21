import json
import pickle
import yaml
import sys

from pathlib import Path
from box import ConfigBox


from defect_detection.logger import logger
from defect_detection.exception import CustomException

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.
    """

    try:
        with open(path_to_yaml, "r", encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)

        if content is None:
            raise ValueError(f"The YAML file '{path_to_yaml}' is empty.")

        logger.info(f"Loaded YAML file: {path_to_yaml}")

        return ConfigBox(content)

    except Exception as e:
        logger.exception(f"Failed to read YAML file: {path_to_yaml}")
        raise CustomException(e, sys)
 
def create_directories(paths:list[Path],verbose:bool=True)->None:
    """
    Creates directories if they do not already exist.
    """
    try:
        for path in paths:
            path.mkdir(
                parents=True,
                exist_ok=True
            )
            if verbose:
                logger.info(f"Created directory: {path}")
    except Exception as e:
        logger.exception(f"failed to create directory: {path}")




def save_json(path:Path,data:dict)->None:
    try:
        with open(path,"w") as  file:
            json.dump(
                data,
                file,
                indent=4
            )
            logger.info(
            f"JSON saved at: {path}"
        )

    except Exception as e:
        logger.exception(f"failed to save json {path}")
        raise CustomException(e, sys)
    

def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as file:
            content=json.load(file)

        logger.info(
            f"JSON loaded from: {path}"
        )

        return ConfigBox(content)

    except Exception as e:
        logger.exception(f"failed to load json from {path}")
        raise CustomException(e, sys)
    

def save_binary(path: Path, data)->None:
    try:

        with open(path, "wb") as file:
            pickle.dump(data, file)

        logger.info(
            f"Binary file saved at: {path}"
        )

    except Exception as e:
        logger.exception(f"failed to save object in {path}")
        raise CustomException(e, sys)

def load_binary(path: Path):
    try:

        with open(path, "rb") as file:
            content = pickle.load(file)

        logger.info(
            f"Binary file loaded from: {path}"
        )

        return content

    except Exception as e:
        logger.exception(f"failed to load object from {path}")
        raise CustomException(e, sys)