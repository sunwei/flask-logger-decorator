# -*- coding: utf-8 -*-
"""Test Logger"""
import pytest
from unittest.mock import MagicMock, patch
from flask_logger_decorator.logger import (
    debug, info, warning, error, critical,
    get_logger, FLASK_LOGGER
)


def test_get_logger():
    mock_logger = MagicMock()
    mock_logger.return_value = MagicMock()

    FLASK_LOGGER['test-get-logger'] = mock_logger
    assert get_logger('test-get-logger') is mock_logger


# @pytest.mark.usefixtures("app")
# @patch('logging.Formatter')
# @patch('logging.StreamHandler')
# def test_setup_stdout(mock_handler, mock_formatter, app):
#     """Test setup stdout."""
#
#     mock_handler.return_value = MagicMock()
#     mock_formatter.return_value = MagicMock()
#
#     with app.test_request_context():
#         debug('test-setup-stdout', 'test message', None)
#         assert mock_handler.called
#         assert mock_formatter.called
#         mock_handler.return_value.setFormatter.assert_called_once()


@pytest.mark.usefixtures("app")
def test_debug(app):
    with app.test_request_context():
        mock_logger = MagicMock()
        mock_logger.debug = MagicMock()
        FLASK_LOGGER['test-debug'] = mock_logger
        debug('test-debug', 'test message', extra={'foo': 'bar'})

        mock_logger.debug.assert_called_with('test message', extra={'foo': 'bar'})


@pytest.mark.usefixtures("app")
def test_info(app):
    with app.test_request_context():
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()
        FLASK_LOGGER['test-info'] = mock_logger
        info('test-info', 'test message', extra={'foo': 'bar'})

        mock_logger.info.assert_called_with('test message', extra={'foo': 'bar'})


@pytest.mark.usefixtures("app")
def test_warning(app):
    with app.test_request_context():
        mock_logger = MagicMock()
        mock_logger.warning = MagicMock()
        FLASK_LOGGER['test-warning'] = mock_logger
        warning('test-warning', 'test message', extra={'foo': 'bar'})

        mock_logger.warning.assert_called_with('test message', extra={'foo': 'bar'})


@pytest.mark.usefixtures("app")
def test_error(app):
    with app.test_request_context():
        mock_logger = MagicMock()
        mock_logger.error = MagicMock()
        FLASK_LOGGER['test-error'] = mock_logger
        error('test-error', 'test message', extra={'foo': 'bar'})

        mock_logger.error.assert_called_with('test message', extra={'foo': 'bar'})


@pytest.mark.usefixtures("app")
def test_critical(app):
    with app.test_request_context():
        mock_logger = MagicMock()
        mock_logger.critical = MagicMock()
        FLASK_LOGGER['test-critical'] = mock_logger
        critical('test-critical', 'test message', extra={'foo': 'bar'})

        mock_logger.critical.assert_called_with('test message', extra={'foo': 'bar'})
