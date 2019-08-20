# -*- coding: utf-8 -*-
"""Test ApiGW"""
from flask_logger_decorator.api import Api


def test_create_api():
    api_test = Api("name", "path", "specs")

    assert api_test.name is "name"
    assert api_test.path is "path"
    assert api_test.specs is "specs"
