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

    # je kan zelf levels toevoegen, hoe dan?
    logging.addLevelName(25, 'STAGE')
    logger.setLevel(logging.STAGE)
    logger.log(26, 'Message in new logging level')

    return dic["critical"]


def log_exceptions():
    """Hoe log je een exception?"""
    logger.exception('bla die bla')
