class LoggerExtendedException(Exception):
    """
    Base except which all flask_logger_extended errors extend
    """
    pass


class LoggerCloudProviderError(LoggerExtendedException):
    """
    An error decoding a JWT
    """
    pass
