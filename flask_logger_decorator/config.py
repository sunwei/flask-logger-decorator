from flask import current_app


class _Config(object):

    @property
    def request_log_name(self):
        return 'flask-request-logger'

    @property
    def log_level(self):
        return current_app.config.get('LOG_LEVEL')

    @property
    def log_format_console(self):
        return current_app.config.get('LOG_FORMAT_CONSOLE')

    @property
    def log_format_default(self):
        return '%(asctime)s %(name)10s %(levelname)10s: %(message)10s'

    @property
    def log_format_time(self):
        return current_app.config.get('LOG_FORMAT_TIME')

    @property
    def log_request_id(self):
        return current_app.config.get('LOG_REQUEST_ID_G_OBJECT_ATTRIBUTE')

    @property
    def log_all_requests(self):
        return current_app.config.get('LOG_ALL_REQUESTS')

    @property
    def log_format_time_default(self):
        return '%Y-%m-%dT%T'


config = _Config()
