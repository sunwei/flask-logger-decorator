DDD Api Gateway Framework
=========================

|Build Status| |Pypi Status| |Coveralls Status|

Installation
------------

From source code:

::

    python setup.py install

From pypi:

::

    pip install flask-logger-decorator

Usage
-----

::

    from flask_logger_decorator.logger_extension import LoggerExtension


    logger = LoggerExtension()
    logger.init_app(app)

    #examples
    2019-08-28T10:33:34 flask-request-logger      DEBUG: trace_uuid=befc1448-8f6d-4d1e-88ca-d3e04cd16f8e endpoint=/api/v1/user method=GET  query_args: post_values:
    2019-08-28T10:33:34 flask-request-logger      DEBUG: trace_uuid=befc1448-8f6d-4d1e-88ca-d3e04cd16f8e ip=127.0.0.1 method=GET  path:/api/v1/user status_code:401



License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

See `License file <https://github.com/sunwei/ddd-base/blob/master/LICENSE>`_

.. |Build Status| image:: https://travis-ci.com/sunwei/flask-logger-decorator.svg?branch=master
   :target: https://travis-ci.com/sunwei/flask-logger-decorator
.. |Pypi Status| image:: https://badge.fury.io/py/flask-logger-decorator.svg
   :target: https://badge.fury.io/py/flask-logger-decorator
.. |Coveralls Status| image:: https://coveralls.io/repos/github/sunwei/flask-logger-decorator/badge.svg?branch=master
   :target: https://coveralls.io/github/sunwei/flask-logger-decorator?branch=master
