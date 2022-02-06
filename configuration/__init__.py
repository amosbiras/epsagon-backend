import os

from enum import Enum

from .base import LoggerConfig
from .db import MySQLConfig, Queries
from .util import load_yaml

CONFIGURATION_DIRECTORY_PATH: str = './etc/settings'


class ConfigurationPaths(str, Enum):
    LOGGER: str = os.path.join(CONFIGURATION_DIRECTORY_PATH, 'logger.yaml')
    DB: str = os.path.join(CONFIGURATION_DIRECTORY_PATH, 'mysql.yaml')
    QUERIES: str = os.path.join(CONFIGURATION_DIRECTORY_PATH, 'queries.yaml')
