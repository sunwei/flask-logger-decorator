import logging
import sys
from flask_logger_decorator.config import config

FLASK_LOGGER = {}


def _setup_stdout(logger):
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(config.log_level)

    fmt = (config.log_format_console or config.log_format_default)
    fmt_date = config.log_format_time or config.log_format_time_default
    formatter = logging.Formatter(fmt, fmt_date)

    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)


def get_logger(name=None):
    logger = FLASK_LOGGER.get(name)
    if not logger:
        logger = logging.getLogger(name)
        logger.handlers = []
        _setup_stdout(logger)
    return logger


def _log(name):
    logger = FLASK_LOGGER.get(name)
    if not logger:
        logger = get_logger(name)
        FLASK_LOGGER[name] = logger
    return logger


def debug(name, message, extra=None):
    _log(name).debug(message, extra=extra)


def info(name, message, extra=None):
    _log(name).info(message, extra=extra)


def warning(name, message, extra=None):
    _log(name).warning(message, extra=extra)


def error(name, message, extra=None):
    _log(name).error(message, extra=extra)


def critical(name, message, extra=None):
    _log(name).critical(message, extra=extra)
