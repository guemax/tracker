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
        self.start_redirect_errors()

    def test_debug_deprecated(self):
        debug_deprecated(self.message)
        self.assertIn(self.message, self.output.getvalue())

    def test_debug(self) -> None:
        debug(self.message, print_status=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nOK", self.output.getvalue())

        self.erase_output()

        debug(self.message, print_status=True)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nOK", self.output.getvalue())

        self.erase_output()

        debug(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nOK", self.output.getvalue())

    def test_info_deprecated(self):
        info_deprecated(self.message)
        self.assertIn(self.message, self.output.getvalue())

    def test_info(self) -> None:
        info(self.message, print_status=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nOK", self.output.getvalue())

        info(self.message, print_status=True)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nOK", self.output.getvalue())

        info(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nOK", self.output.getvalue())

    def test_warn_deprecated(self):
        info_deprecated(self.message)
        self.assertIn(self.message, self.output.getvalue())

    def test_warn(self) -> None:
        self.start_redirect_errors()

        warn(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nEXIT", self.output.getvalue())

        self.erase_errors()

        warn(self.message, print_status=True, exit_tracker=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nEXIT", self.output.getvalue())

        self.erase_errors()

        self.assertRaises(SystemExit, warn, self.message, True, True)
        self.assertRaises(SystemExit, warn, self.message, False, True)

    def test_error_deprecated(self):
        self.start_redirect_errors()

        error_deprecated(self.message)
        self.assertIn(self.message, self.output.getvalue())

        self.stop_redirect_errors()

    def test_error(self) -> None:
        self.start_redirect_errors()

        error(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nEXIT", self.output.getvalue())

        self.erase_errors()

        error(self.message, print_status=True, exit_tracker=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nEXIT", self.output.getvalue())

        self.erase_errors()

        self.assertRaises(SystemExit, error, self.message, True, True)
        self.assertRaises(SystemExit, error, self.message, False, True)

    def test_fatal_deprecated(self):
        self.start_redirect_errors()

        fatal_deprecated(self.message)
        self.assertIn(self.message, self.output.getvalue())

        self.stop_redirect_errors()

    def test_fatal(self) -> None:
        self.start_redirect_errors()

        error(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nEXIT", self.output.getvalue())

        self.erase_errors()

        error(self.message, print_status=True, exit_tracker=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nEXIT", self.output.getvalue())

        self.erase_errors()

        self.assertRaises(SystemExit, error, self.message, True, True)
        self.assertRaises(SystemExit, error, self.message, False, True)

    def erase_output(self) -> None:
        self.stop_redirecting_output()
        self.output = io.StringIO()
        self.start_redirecting_output()

    def erase_errors(self) -> None:
        self.start_redirect_errors()
        self.output = io.StringIO()
        self.start_redirect_errors()

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
        self.stop_redirect_errors()
