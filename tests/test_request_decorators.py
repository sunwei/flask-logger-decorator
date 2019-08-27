# -*- coding: utf-8 -*-
"""Test Parser"""
import pytest
import re
from unittest.mock import MagicMock, ANY
from flask_logger_decorator.logger import FLASK_LOGGER
from flask_logger_decorator.request_decorators import get_request_trace_info, request_tracing


@pytest.mark.usefixtures("app")
def test_get_request_with_x_request(app):
    with app.test_request_context(headers={'X-Request-ID': '1-67891234-def'}):
        app.preprocess_request()
        trace_info = get_request_trace_info()
        result = "trace_uuid=1-67891234-def endpoint=/ method=GET  query_args: post_values:"
        assert trace_info == result


@pytest.mark.usefixtures("app")
def test_get_request_with_x_correlation(app):
    with app.test_request_context(headers={'X-Correlation-ID': '1-67891234-def'}):
        app.preprocess_request()
        trace_info = get_request_trace_info()
        result = "trace_uuid=1-67891234-def endpoint=/ method=GET  query_args: post_values:"
        assert trace_info == result


@pytest.mark.usefixtures("app")
def test_get_request_with_amazon(app):
    with app.test_request_context('/?limit=1',
                                  headers={'X-Amzn-Trace-Id': 'Self=1-67891234-def;Root=1-67891233-abc'}):
        app.preprocess_request()
        trace_info = get_request_trace_info()
        result = "trace_uuid=1-67891234-def endpoint=/ method=GET  query_args:limit='1' post_values:"
        assert trace_info == result


@pytest.mark.usefixtures("app")
def test_post_request_trace_info(app):
    with app.test_client() as c:
        c.post('/', data={
            'attr': 'value', 'other': 'data'
        })
        trace_info = get_request_trace_info()
        post_value = "post_values:attr='value' other='data'"

        assert post_value in trace_info


@pytest.mark.usefixtures("app")
def test_request_decorator(app):

    @app.route('/test-decorator', methods=('GET', 'POST'))
    @request_tracing
    def f(a="abc", b="cdf"):
        return a.join(':').join(b)

    with app.test_client() as c:
        mock_logger = MagicMock()
        FLASK_LOGGER['flask-request-logger'] = mock_logger

        c.post('/test-decorator', data={
            'attr': 'value', 'other': 'data'
        })

        assert mock_logger.debug.called
