"""This file is part of tracker.
tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import unittest

from tests.test_click_commands.CommandBaseTestingClass import CommandBaseTestingClass


class TestLog(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestLog, self).setUp()

    def test_logging_without_any_grouped_entries_existing(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("log")

        self.check_for_exit_code_zero()
        self.assertIn("Nothing to see yet.", self.output)

    def test_logging_with_one_grouped_entry(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("start")
        self.run_cli("stop")

        number_of_entries = 1
        self.check_for_log_message(number_of_entries)

    def check_for_log_message(self, number_of_entries: int) -> None:
        self.run_cli("log")
        self.check_for_exit_code_zero()

        self.assertIn("Showing all entries", self.output)
        self.assertIn(f"({number_of_entries} in total)", self.output)

    def test_logging_with_multiple_grouped_entries(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values()

        number_of_entries = 2
        self.check_for_log_message(number_of_entries)

    def test_logging_a_specific_entry(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values()

        self.run_cli("log", "-i 1")

        self.check_for_exit_code_zero()
        self.assertIn("Showing all entries of", self.output)

    def test_logging_a_specific_entry_with_unknown_id(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values()

        self.check_for_unknown_id_of_date(-1)
        self.check_for_unknown_id_of_date(0)    # IDs start with one
        self.check_for_unknown_id_of_date(100)

    def check_for_unknown_id_of_date(self, id_of_date: int) -> None:
        self.run_cli("log", f"-i {id_of_date}")

        self.check_for_exit_code_not_zero()

        self.assertIn(f"We couldn't find a date matching the ID {id_of_date}.", self.output)
        self.assertIn("EXIT", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
