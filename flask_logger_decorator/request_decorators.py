import uuid
from functools import wraps
from datetime import datetime
from calendar import timegm
from flask import request
from flask_logger_decorator.config import config


def tracing_request():
    if request.method not in config.exempt_methods:
        jwt_data = _decode_jwt_from_request(request_type='refresh')
        ctx_stack.top.jwt = jwt_data
        _load_user(jwt_data[config.identity_claim_key])


def request_tracing(fn):
    """
    A decorator to tracing request.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        tracing_request()
        return fn(*args, **kwargs)
    return wrapper

