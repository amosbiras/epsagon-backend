from src.utils import init_logger
from configuration import LoggerConfig, load_yaml, ConfigurationPaths

init_logger(name=__name__, logger_config=LoggerConfig(**load_yaml(ConfigurationPaths.LOGGER)))
