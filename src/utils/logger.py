import logging

from typing import NoReturn

from configuration import LoggerConfig


def init_logger(name: str, logger_config: LoggerConfig) -> NoReturn:
    logger = logging.getLogger(name)
    logger.setLevel(logger_config.level)
    __add_handlers(logger, logger_config)


def __add_handlers(logger: logging.Logger, logger_config: LoggerConfig) -> NoReturn:
    for handler in LOGGING_HANDLERS.values():
        logger.addHandler(handler(logger_config))


def __create_stream_handler(logger_config: LoggerConfig) -> logging.StreamHandler:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logger_config.level)
    stream_handler.setFormatter(logging.Formatter(logger_config.format))
    return stream_handler


LOGGING_HANDLERS = {
    'stream': __create_stream_handler
}
