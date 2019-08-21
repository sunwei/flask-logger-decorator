import logging
from flask import g

from flask_logger_decorator.logger import Logger
from flask_logger_decorator.utils import generate_request_id
from flask_logger_decorator.parser import auto_parser
from flask_logger_decorator.config import config
from flask_logger_decorator.request_decorators import get_request_trace_info


FLASK_LOGGER = {}


def _log(name):
    logger = FLASK_LOGGER.get(name)
    if not logger:
        logger = Logger(name)
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


def exception(name, message, extra=None):
    _log(name).exception(message, extra=extra)


class LoggerManager(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):   # pragma: no cover
            app.extensions = {}
        app.extensions['flask-logger-decorator-extended'] = self

        self._set_default_configuration_options(app)

    @staticmethod
    def _set_default_configuration_options(app):
        app.config.setdefault('LOG_LEVEL', logging.DEBUG)
        app.config.setdefault('LOG_ALL_REQUESTS', True)
        app.config.setdefault('LOG_REQUEST_ID_G_OBJECT_ATTRIBUTE', 'flask_log_request_id')
        debug(config.request_log_name, "Init flask request logger...")

        @app.before_request
        def _persist_request_id():
            g_object_attr = config.log_request_id

            setattr(g, g_object_attr, auto_parser())
            if g.get(g_object_attr) is None:
                setattr(g, g_object_attr, generate_request_id())

        if config.log_all_requests is True:
            app.after_request(debug(config.request_log_name, get_request_trace_info()))
