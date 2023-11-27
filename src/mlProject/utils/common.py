from math import log
import os
import json
from click import BadParameter
import joblib
from box import BoxError, ConfigBox
from box.exceptions import BoxValueError
import yaml

from mlProject import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
        Reads yaml file and returns

        Args:
            path_to_yaml (str): path like input

        Raises:
            ValeError: If yaml file is empty
            e: empty file

        Returns:
            ConfigBox: ConfigBox Type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded Sucessfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose:True):
    """
        Creates list of directories

        Args:
            path_to_directories (list): list of path of directories
            ingnore_log (bool, optional): if multiple directories are created. Default to false.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data

    Args:
        data (Any): data to be saved in json file
        path (path): path to json file
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at : {path}")


@ensure_annotations
def load_json(path: Path, data: dict) -> ConfigBox:
    """
    Load json data

    Args:
        path (path): path to json file

    Returns:
        ConfigBox: data as class attributes instead if dict
    """
    with open(path, 'w') as f:
        content = json.load(f)

    logger.info(f"json file loaded at : {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file

    Args:
        data (Any): data to be saved as binary
        path (path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at : {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file

    Args:
        path (path): path to binary file

    Return:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file saved at : {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB

    Args:
        path (Path): Path of the file

    Returns: 
    str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"