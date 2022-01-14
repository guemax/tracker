import io
import sys
import unittest

import click.testing

from src.console_logger.console_logger import *


class TestConsoleLogger(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = click.testing.CliRunner()
        self.output = io.StringIO()

        self.start_redirect()

    def test_debug(self):
        message = "Starting Tracker"
        debug(message)

        self.assertIn(message, self.output.getvalue())

    def test_info(self):
        message = "Starting Tracker"
        info(message)

        self.assertIn(message, self.output.getvalue())

    def test_warn(self):
        message = "Warning: Cannot open Tracker file"
        info(message)

        self.assertIn(message, self.output.getvalue())

    def test_error(self):
        self.start_error_redirect()

        message = "Error: Unable to continue"
        error(message)

        self.assertIn(message, self.output.getvalue())

        self.stop_error_redirect()

    def test_fatal(self):
        self.start_error_redirect()

        message = "Fatal: Shutting down"
        fatal(message)

        self.assertIn(message, self.output.getvalue())

        self.stop_error_redirect()

    def start_redirect(self):
        sys.stdout = self.output

    def start_error_redirect(self):
        sys.stderr = self.output

    @staticmethod
    def stop_redirect():
        sys.stdout = sys.__stdout__

    @staticmethod
    def stop_error_redirect():
        sys.stderr = sys.__stderr__

    def tearDown(self) -> None:
        self.stop_redirect()
