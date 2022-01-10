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
        message = "Error: Unable to continue"
        info(message)

        self.assertIn(message, self.output.getvalue())

    def test_fatal(self):
        message = "Fatal: Shutting down"
        info(message)

        self.assertIn(message, self.output.getvalue())

    def start_redirect(self):
        sys.stdout = self.output

    @staticmethod
    def stop_redirect():
        sys.stdout = sys.__stdout__

    def tearDown(self) -> None:
        self.stop_redirect()
