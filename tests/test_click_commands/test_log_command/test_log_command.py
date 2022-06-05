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


class TestLogCommand(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestLogCommand, self).setUp()

    def test_logging_a_specific_entry(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values()

        self.run_cli("log", "-i 1")

        self.assertIn("Showing all entries of", self.output)

    def test_logging_a_sepcific_entry_with_unknown_id(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values()

        self.check_for_not_matching_id_of_date(-1)
        self.check_for_not_matching_id_of_date(0)
        self.check_for_not_matching_id_of_date(100)

    def check_for_not_matching_id_of_date(self, id_of_date: int) -> None:
        self.run_cli("log", f"-i {id_of_date}")

        self.assertIn(f"We couldn't find a date matching the ID {id_of_date}.", self.output)
        self.assertIn("EXIT", self.output)

    def test_logging_without_any_grouped_entries_existing(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("log")
        self.check_for_exit_code_zero()

        self.assertIn("Nothing to see yet.", self.output)

    def test_logging_with_one_grouped_entry(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("start")
        self.run_cli("stop")

        total_dates = 1
        self.check_for_log_message(total_dates)

    def check_for_log_message(self, total_dates: int) -> None:
        self.run_cli("log")
        self.check_for_exit_code_zero()

        self.assertIn("Showing all entries", self.output)
        self.assertIn(f"({total_dates} in total)", self.output)

    def test_logging_with_multiple_grouped_entries(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.setup_test_values()

        total_dates = 2
        self.check_for_log_message(total_dates)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
