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

from tracker.commands.console_logger import *


class TestConsoleLogger(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = click.testing.CliRunner()
        self.output = io.StringIO()

        self.message = "A simple test message"

        self.start_redirecting_output()

    def test_debug(self):
        debug(self.message)
        self.assertIn(self.message, self.output.getvalue())

    def test_info(self):
        info(self.message)
        self.assertIn(self.message, self.output.getvalue())

    def test_warn(self):
        info(self.message)
        self.assertIn(self.message, self.output.getvalue())

    def test_error(self):
        self.start_redirect_errors()

        error(self.message)
        self.assertIn(self.message, self.output.getvalue())

        self.stop_redirect_errors()

    def test_fatal(self):
        self.start_redirect_errors()

        fatal(self.message)
        self.assertIn(self.message, self.output.getvalue())

        self.stop_redirect_errors()

    def start_redirecting_output(self):
        sys.stdout = self.output

    def start_redirect_errors(self):
        sys.stderr = self.output

    @staticmethod
    def stop_redirecting_output():
        sys.stdout = sys.__stdout__

    @staticmethod
    def stop_redirect_errors():
        sys.stderr = sys.__stderr__

    def tearDown(self) -> None:
        self.stop_redirecting_output()
