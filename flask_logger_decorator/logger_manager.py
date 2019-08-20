import logging

from flask_logger_decorator.logger import Logger
from flask_logger_decorator.utils import generate_request_id

from flask_logger_decorator.default_callbacks import (
    default_cloud_provider_callback
)

from flask_logger_decorator.exceptions import (
    LoggerCloudProviderError
)


class LoggerManager(object):

    def __init__(self, app=None):
        self._loggers = {}
        self._user_cloud_provider_callback = default_cloud_provider_callback

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):   # pragma: no cover
            app.extensions = {}
        app.extensions['flask-logger-decorator-extended'] = self

        self._set_default_configuration_options(app)
        self._set_error_handler_callbacks(app)

    def _set_error_handler_callbacks(self, app):
        @app.errorhandler(LoggerCloudProviderError)
        def handle_auth_error(e):
            return self._user_cloud_provider_callback(str(e))

    @staticmethod
    def _set_default_configuration_options(app):
        app.config.setdefault('LOG_LEVEL', logging.ERROR)
        app.config.setdefault('LOG_ALL_REQUESTS', True)

        @app.before_request
        def _persist_request_id():
            g_object_attr = app.config['LOG_REQUEST_ID_G_OBJECT_ATTRIBUTE']

            setattr(g, g_object_attr, self._request_id_parser())
            if g.get(g_object_attr) is None:
                if app.config['LOG_REQUEST_ID_GENERATE_IF_NOT_FOUND']:
                    setattr(g, g_object_attr, generate_request_id)

    def cloud_provider_loader(self, callback):
        self._user_cloud_provider_callback = callback
        return callback

    def _log(self, name):
        logger = self._loggers.get(name)

        if not logger:
            logger = Logger(name)
            self._loggers[name] = logger

        return logger

    def debug(self, name, message, extra=None):
        self._log(name).debug(message, extra=extra)

    def info(self, name, message, extra=None):
        self._log(name).info(message, extra=extra)

    def warning(self, name, message, extra=None):
        self._log(name).warning(message, extra=extra)

    def error(self, name, message, extra=None):
        self._log(name).error(message, extra=extra)

    def critical(self, name, message, extra=None):
        self._log(name).critical(message, extra=extra)

    def exception(self, name, message, extra=None):
        self._log(name).exception(message, extra=extra)

