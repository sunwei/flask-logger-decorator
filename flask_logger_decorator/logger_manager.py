from flask_logger_decorator.logger import Logger

FLASK_LOGGER = {}


def _log(name):
    logger = FLASK_LOGGER.get(name)
    if not logger:
        the_logger = Logger(name)
        FLASK_LOGGER[name] = the_logger.logger
        logger = FLASK_LOGGER[name]
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


def exception(name, message, extra=None):
    _log(name).exception(message, extra=extra)
