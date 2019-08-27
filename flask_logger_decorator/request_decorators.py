from functools import wraps
from reprlib import Repr
import inspect
from flask import request, g
from flask_logger_decorator.config import config
from flask_logger_decorator.logger import debug

__r = Repr()
__r.maxarray = __r.maxarray * 10
__r.maxdict = __r.maxdict * 10
__r.maxstring = __r.maxstring * 10


def request_tracing(fn):
    """
    A decorator to tracing request.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        tracing_request(fn, *args, **kwargs)
        return fn(*args, **kwargs)
    return wrapper


def tracing_request(fn, *args, **kwargs):
    function_args = ' '.join(_get_fn_args(fn, *args, **kwargs))
    trace_info = ' '.join(_get_fn_extra_info(fn))
    func_msg = 'func_name:{} func_args:{} trace_info:{}'.format(
        fn.__name__, function_args, trace_info)
    request_msg = get_request_trace_info()
    debug(config.request_log_name, 'req_msg={}; func_msg={}'.format(request_msg, func_msg))


def _get_fn_args(fn, *args, **kwargs):
    traced_func_args = []
    for k, v in inspect.getcallargs(fn, *args, **kwargs).items():
        if k == 'self':
            continue

        v = '********' if k in {'password', 'secret'} else __r.repr(v).replace('"', "'")
        traced_func_args.append('{}={}'.format(k, v))
    return traced_func_args


def _get_fn_extra_info(fn):
    trace_info_list = ['trace_pathname={}'.format(inspect.getfile(fn))]
    try:
        trace_info_list.append('trace_lineno={}'.format(inspect.getsourcelines(fn)[1]))
    except IndexError:
        pass
    return trace_info_list


def _get_request_query_args():
    traced_request_args = []
    for k, v in request.args.items():
        v = '********' if k in {'password', 'secret'} else __r.repr(v).replace('"', "'")
        traced_request_args.append('{}={}'.format(k, v))
    return traced_request_args


def _get_request_post_values():
    traced_post_values = []
    if request.method in {'POST', 'PUT'}:
        json_args = request.json
        if json_args is not None:
            for k, v in json_args.items():
                v = '********' if k in {'password', 'secret'} else __r.repr(v).replace('"', "'")
                traced_post_values.append('{}={}'.format(k, v))
        else:
            for k, v in request.form.items():
                v = '********' if k in {'password', 'secret'} else __r.repr(v).replace('"', "'")
                traced_post_values.append('{}={}'.format(k, v))
    return traced_post_values


def get_request_trace_info():
    trace_uuid = getattr(g, config.log_request_id)
    query_args = ' '.join(_get_request_query_args())
    post_values = ' '.join(_get_request_post_values())
    return 'trace_uuid={} endpoint={} method={} ' \
        ' query_args:{} post_values:{}'.format(
            trace_uuid, request.path, request.method,
            query_args, post_values)


def get_response_trace_info(response):
    trace_uuid = getattr(g, config.log_request_id)
    return 'trace_uuid={} ip={} method={} ' \
           ' path:{} status_code:{}'.format(
            trace_uuid, request.remote_addr, request.method,
            request.path, response.status_code)
