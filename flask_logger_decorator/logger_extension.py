import logging
from flask import g

from flask_logger_decorator.utils import generate_request_id
from flask_logger_decorator.parser import auto_parser
from flask_logger_decorator.config import config
from flask_logger_decorator.request_decorators import get_request_trace_info
from flask_logger_decorator.logger import debug


class LoggerExtension(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):   # pragma: no cover
            app.extensions = {}
        app.extensions['flask-logger-decorator-extended'] = self

        self._set_default_configuration_options(app)

    def _set_default_configuration_options(self, app):
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

            debug(config.request_log_name, get_request_trace_info())

        if config.log_all_requests is True:
            app.after_request(self._log_http_event)

    @staticmethod
    def _log_http_event(response):
        """
        It will create a log event as werkzeug but at the end of request holding the request-id

        Intended usage is a handler of Flask.after_request
        :return: The same response object
        """
        # logger.info(
        #     '{ip} - - "{method} {path} {status_code}"'.format(
        #         ip=request.remote_addr,
        #         method=request.method,
        #         path=request.path,
        #         status_code=response.status_code)
        # )
        print('todo...')
        return response
