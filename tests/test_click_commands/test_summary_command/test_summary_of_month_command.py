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
from datetime import datetime

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestSummaryOfMonth(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestSummaryOfMonth, self).setUp()

    def test_summary_without_any_entries_created_this_month(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("summary", "-tm")
        self.check_for_exit_code_zero()

        self.assertIn("Nothing to show yet. There have been no entries created this month.\n"
                      "  (use \"tracker start\" to create one)", self.output)
        self.assertIn("OK", self.output)

    def test_summary_with_one_entry_created_this_month(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(1)

        self.run_cli("summary", "-tm")
        self.check_for_exit_code_zero()

        self.assertIn("Showing entries as summary (1 in total).\n"
                      "Range is \"this-month\".", self.output)
        self.assertIn("OK", self.output)

    def test_summary_with_multiple_entries_created_this_month(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(80)

        self.run_cli("summary", "-tm")
        self.check_for_exit_code_zero()

        # See the test for the MonthSummaryHandler() for more information
        expected_length_of_entries = datetime.today().day
        self.assertIn(f"Showing entries as summary ({expected_length_of_entries} in total).\n"
                      "Range is \"this-month\".", self.output)
        self.assertIn("OK", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
