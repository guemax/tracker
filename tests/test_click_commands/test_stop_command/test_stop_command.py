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
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestStopCommand(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestStopCommand, self).setUp()

    def test_stopping_a_timer_without_message(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("start")
        self.run_cli("stop")
        self.check_for_exit_code_zero()

        self.assertIn("Existing timer stopped", self.output)
        self.assertIn("OK", self.output)

    def test_starting_a_timer_with_message(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        message = "my personal message"

        self.run_cli("start")
        self.run_cli("stop", f"-m {message}")
        self.check_for_exit_code_zero()

        self.assertIn("Existing timer stopped", self.output)
        self.assertIn(f"Added message", self.output)
        self.assertIn(message, self.output)
        self.assertIn("OK", self.output)

    def test_stopping_a_timer_when_no_one_exists(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("stop")
        self.check_for_exit_code_minus_one()

        self.assertIn("No timer exists yet", self.output)

    def test_stopping_a_timer_when_no_one_exists_starting_one_and_stopping_it(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("stop")
        self.check_for_exit_code_minus_one()
        self.assertIn("No timer exists yet", self.output)

        self.run_cli("start")
        self.check_for_exit_code_zero()

        self.run_cli("stop")
        self.check_for_exit_code_zero()

        self.assertIn("Existing timer stopped", self.output)
        self.assertIn("OK", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
