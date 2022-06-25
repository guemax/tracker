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
import unittest

from tracker.commands.console_logger import *


class TestConsoleLogger(unittest.TestCase):
    def setUp(self) -> None:
        self.output = io.StringIO()
        self.message = "A simple test message"

        self.__start_redirecting()

    def test_debug(self) -> None:
        debug(self.message, print_status=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nOK", self.output.getvalue())

        self.clear_output()

        debug(self.message, print_status=True)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nOK", self.output.getvalue())

        self.clear_output()

        debug(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nOK", self.output.getvalue())

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

    def test_warn(self) -> None:
        warn(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nEXIT", self.output.getvalue())

        self.clear_output()

        warn(self.message, print_status=True, exit_tracker=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nEXIT", self.output.getvalue())

        self.clear_output()

        self.assertRaises(SystemExit, warn, self.message, True, True)
        self.assertRaises(SystemExit, warn, self.message, False, True)

    def test_error(self) -> None:
        error(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nEXIT", self.output.getvalue())

        self.clear_output()

        error(self.message, print_status=True, exit_tracker=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nEXIT", self.output.getvalue())

        self.clear_output()

        self.assertRaises(SystemExit, error, self.message, True, True)
        self.assertRaises(SystemExit, error, self.message, False, True)

    def test_fatal(self) -> None:
        error(self.message)
        self.assertIn(self.message, self.output.getvalue())
        self.assertNotIn("\n\nEXIT", self.output.getvalue())

        self.clear_output()

        error(self.message, print_status=True, exit_tracker=False)
        self.assertIn(self.message, self.output.getvalue())
        self.assertIn("\n\nEXIT", self.output.getvalue())

        self.clear_output()

        self.assertRaises(SystemExit, error, self.message, True, True)
        self.assertRaises(SystemExit, error, self.message, False, True)

    def clear_output(self) -> None:
        self.__stop_redirecting()
        self.output = io.StringIO()
        self.__start_redirecting()

    def __start_redirecting(self) -> None:
        self.__start_redirecting_stdout()
        self.__start_redirecting_stderr()

    def __start_redirecting_stdout(self) -> None:
        sys.stdout = self.output

    def __start_redirecting_stderr(self) -> None:
        sys.stderr = self.output

    def __stop_redirecting(self) -> None:
        self.__stop_redirecting_stdout()
        self.__stop_redirecting_stderr()

    @staticmethod
    def __stop_redirecting_stdout() -> None:
        sys.stdout = sys.__stdout__

    @staticmethod
    def __stop_redirecting_stderr() -> None:
        sys.stderr = sys.__stderr__

    def tearDown(self) -> None:
        self.__stop_redirecting_stdout()
        self.__stop_redirecting_stderr()
