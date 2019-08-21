import logging
import pytest
from flask_logger_decorator.config import config


@pytest.mark.usefixtures("app")
def test_default_configs(app):
    with app.test_request_context():
        assert config.request_log_name == 'flask-request-logger'

        assert config.log_level is None
        assert config.log_format_console is None
        assert config.log_format_time is None
        assert config.log_request_id is None
        assert config.log_all_requests is None
        assert config.log_format_default == '%(asctime)s %(name)10s %(levelname)10s: %(message)10s'
        assert config.log_format_time_default == '%Y-%m-%dT%T'


@pytest.mark.usefixtures("app")
def test_override_configs(app):
    app.config['LOG_LEVEL'] = logging.DEBUG
    app.config['LOG_ALL_REQUESTS'] = True
    app.config['LOG_REQUEST_ID_G_OBJECT_ATTRIBUTE'] = 'flask_log_request_id'

    with app.test_request_context():
        assert config.log_level == logging.DEBUG
        assert config.LOG_ALL_REQUESTS is True
        assert config.log_request_id == 'flask_log_request_id'
