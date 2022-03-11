"""This file is part of Tracker.

Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import io
import sys
import unittest

import click.testing

from tracker.console_logger.console_logger import *


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
