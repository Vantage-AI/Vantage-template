import unittest


class TestLogging(unittest.TestCase):

    def test_show_handler(self):
        from src.logging import show_handler
        show_handler()

    def test_show_formatter(self):
        from src.logging import show_formatter
        self.assertEqual(show_formatter(), 67)

    def test_logging_levels(self):
        from src.logging import logging_levels
        self.assertEqual(logging_levels(), 50)

    def test_log_exceptions(self):
        from src.logging import log_exceptions
        log_exceptions()
