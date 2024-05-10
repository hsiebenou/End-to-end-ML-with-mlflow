import json
import os
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from mlProject import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    read a yaml file and returns

    :param path_to_yaml:
    :return:
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    :param path_to_directories:
    :param verbose:
    :return:
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Create directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data

    :param path:
    :param data:
    :return:
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file data

    :param path:
    :return: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary data

    :param data:
    :param path:
    :return:
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data

    :param path:
    :return:
    """
    joblib.load(filename=path)
    logger.info(f"binary file load from: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    :param path:
    :return:
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"