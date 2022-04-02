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
from datetime import datetime

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestSummaryOfYear(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestSummaryOfYear, self).setUp()

    def test_summary_without_any_entries_created_this_year(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("summary", "-ty")
        self.check_for_exit_code_zero()

        self.assertIn("Nothing to show yet. There have been no entries created this year.\n"
                      "  (use \"tracker start\" to create one)", self.output)
        self.assertIn("OK", self.output)

    def test_summary_with_one_entry_created_this_year(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(1)

        self.run_cli("summary", "-ty")
        self.check_for_exit_code_zero()

        self.assertIn("Showing entries as summary (1 in total).\n"
                      "Range is \"this-year\".", self.output)
        self.assertIn("OK", self.output)

    def test_summary_with_multiple_entries_created_this_year(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(720)

        self.run_cli("summary", "-ty")
        self.check_for_exit_code_zero()

        # See the test for the YearSummaryHandler() for more information
        expected_length_of_entries = datetime.today().timetuple().tm_yday
        self.assertIn(f"Showing entries as summary ({expected_length_of_entries} in total).\n"
                      "Range is \"this-year\".", self.output)
        self.assertIn("OK", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
