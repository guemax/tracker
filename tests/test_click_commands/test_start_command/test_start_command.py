"""This file is part of tracker.
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


class TestStartCommand(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestStartCommand, self).setUp()

    def test_starting_a_timer(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("start")
        self.check_for_exit_code_zero()

        self.assertIn("New timer started", self.output)
        self.assertIn("OK", self.output)

    def test_starting_a_timer_when_one_already_exists(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("start")
        self.check_for_exit_code_zero()

        self.run_cli("start")
        self.check_for_exit_code_minus_one()

        self.assertIn("A timer already exists", self.output)
        self.assertIn("EXIT", self.output)

    def test_starting_a_timer_stopping_it_and_starting_another_one(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("start")
        self.check_for_exit_code_zero()

        self.run_cli("stop", "-m \"\"")
        self.check_for_exit_code_zero()

        self.run_cli("start")
        self.check_for_exit_code_zero()

        self.assertIn("New timer started", self.output)
        self.assertIn("OK", self.output)

    def test_starting_a_timer_with_invalid_option(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("start", "--unknown-option")
        self.check_for_exit_code_two()

        self.assertIn("Error", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
