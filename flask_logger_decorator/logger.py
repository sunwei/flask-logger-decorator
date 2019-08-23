import logging
import sys
from flask_logger_decorator.config import config


class Logger(object):

    def __init__(self, name=None):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.handlers = []
        self._setup_stdout(self.logger)

    @staticmethod
    def _setup_stdout(logger):
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(config.log_level)

        fmt = (config.log_format_console or config.log_format_default)
        fmt_date = config.log_format_time or config.log_format_time_default
        formatter = logging.Formatter(fmt, fmt_date)

        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)
