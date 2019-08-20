# -*- coding: utf-8 -*-
"""Test data"""
import os
import pytest
import json

TEST_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_DATA_PATH = os.path.join(TEST_PATH, 'test_data')


def _get_test_data(filename):
    api_conf_json_path = os.path.join(TEST_DATA_PATH, filename)
    with open(api_conf_json_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data
