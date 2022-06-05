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

import datetime
import unittest

from tracker.handler.summary_handler.week_summary_handler import WeekSummaryHandler

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestWeekSummaryHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestWeekSummaryHandler, self).setUp()

        self.week_summary_handler = WeekSummaryHandler()

    def test_summary_without_any_entries_created_this_week(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        summarized_entries = self.week_summary_handler.summary()
        self.assertTrue(summarized_entries.empty)

    def test_summary_with_one_entry_created_this_week(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(1)

        summarized_entries = self.week_summary_handler.summary()

        self.assertFalse(summarized_entries.empty)
        self.assertEqual(1, len(summarized_entries))

    def test_summary_with_multiple_entries_created_this_week(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        # Set up two entries per day (7 grouped entries)
        self.setup_test_values(14)

        summarized_entries = self.week_summary_handler.summary()

        self.assertFalse(summarized_entries.empty)

        # WeekSummaryHandler() will only show entries created this week, so if it's monday, it will only show the two
        # entries create on monday, not the ones from the previous week, so length of summarized_entries will be the
        # day of the week as an integer, where Monday is 1 and Sunday is 7.
        exspected_length_of_entries = datetime.datetime.today().weekday() + 1   # Monday would otherwise be 0, not 1
        self.assertEqual(exspected_length_of_entries, len(summarized_entries))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
