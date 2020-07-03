"""Summary about logging."""

import logging

logger = logging.getLogger(__name__)  # convention for naming loggers

print("Hello, we zijn nu hier.")
# Don't use print for logging, because
# - It's diffecult to track where the message comes from.
# - Print outputs to stdout, which might be undiserable for users.
# - You can't control the visibilaty.


def show_handler():
    """Docstring tbd."""
    file_handler = logging.FileHandler('data/logging.log')
    file_handler.setLevel(logging.ERROR)
    logger.addHandler(file_handler)


def show_formatter():
    """Docstring tbd."""
    website = "https://docs.python.org/3/library/logging.html#logrecord-attributes"

    formatter = logging.Formatter('%(asctime)s:%(message)s')
    stream_handler = logging.StreamHandler()  # handler for output in console
    stream_handler.setFormatter(formatter)  # change format of handdler
    logger.addHandler(stream_handler)
    return len(website)


def logging_levels():
    """Docstring tbd."""
    dic = {"debug": 10,  # Detailed information, typically of interest only when diagnosing problems.
           "info": 20,  # Confirmation that things are working as expected.
           "warning": 30,  # An indication that something unexpected happened, or indicative of some problem in the near
           # future (e.g. 'disk space low'). The software is still working as expected.
           "error": 40,  # Due to a more serious problem, the software has not been able to perform some function.
           "critical": 50}  # A serious error, indicating that te program itself may be unable to continue running.

    # default level is warning.
    logger.setLevel(logging.DEBUG)

    # adding a level takes several steps, see add_logging_level()
    add_logging_level('STAGE', 25)
    logger.setLevel(logging.STAGE)
    logger.stage('Message in new logging level')

    return dic["critical"]


def add_logging_level(level_name, level_num):
    """Adds a new logging level to the `logging` module and the currently configured logging class.

    `levelName` becomes an attribute of the `logging` module with the value `levelNum`. `methodName` becomes a
    convenience method for both `logging` itself and the class returned by `logging.getLoggerClass()`.
    """
    method_name = level_name.lower()

    if hasattr(logging, level_name):
        raise AttributeError('{} already defined in logging module'.format(level_name))
    if hasattr(logging, method_name):
        raise AttributeError('{} already defined in logging module'.format(method_name))
    if hasattr(logging.getLoggerClass(), method_name):
        raise AttributeError('{} already defined in logger class'.format(method_name))

    def log_for_level(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    def log_to_root(message, *args, **kwargs):
        logging.log(level_num, message, *args, **kwargs)

    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(logging.getLoggerClass(), method_name, log_for_level)
    setattr(logging, method_name, log_to_root)


def log_exceptions():
    """Hoe log je een exception?"""
    logger.exception('bla die bla')
