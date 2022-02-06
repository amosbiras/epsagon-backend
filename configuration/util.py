import yaml

from typing import Dict


def load_yaml(file_path: str) -> Dict:
    with open(file_path, mode='rt', encoding='UTF-8') as yaml_file:
        return yaml.safe_load(yaml_file)
