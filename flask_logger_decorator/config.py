from flask import current_app


class _Config(object):

    @property
    def log_level(self):
        return current_app.config['LOG_LEVEL']

    @property
    def log_format_console(self):
        return current_app.config['LOG_FORMAT_CONSOLE']

    @property
    def log_format_default(self):
        return '%(asctime)s %(name)10s %(levelname)10s: %(message)10s'

    @property
    def log_format_time(self):
        return current_app.config['LOG_FORMAT_TIME']

    @property
    def log_all_requests(self):
        return current_app.config['LOG_ALL_REQUESTS']

    @property
    def log_format_time_default(self):
        return '%Y-%m-%dT%T'

    @property
    def error_msg_key(self):
        return current_app.config['JWT_ERROR_MESSAGE_KEY']

    @property
    def cloud_provider(self):
        return current_app.config['LOGGER_CLOUD_PROVIDER']


config = _Config()
