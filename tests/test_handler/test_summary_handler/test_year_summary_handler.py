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

import datetime
import unittest

from src.handler.summary_handler.year_summary_handler import YearSummaryHandler

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestYearSummaryHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestYearSummaryHandler, self).setUp()

        self.year_summary_handler = YearSummaryHandler()

    def test_summary_without_any_entries_created_this_year(self) -> None:
        self.clean_and_init_tracker_file()

        summarized_entries = self.year_summary_handler.summary()
        self.assertTrue(summarized_entries.empty)

    def test_summary_with_one_entry_created_this_year(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values(1)

        summarized_entries = self.year_summary_handler.summary()

        self.assertFalse(summarized_entries.empty)
        self.assertEqual(1, len(summarized_entries))

    def test_summary_with_multiple_entries_created_this_year(self) -> None:
        self.clean_and_init_tracker_file()

        # Set up two entries per day (40 grouped entries) for 370 days (more than one year)
        self.setup_test_values(720)

        summarized_entries = self.year_summary_handler.summary()

        self.assertFalse(summarized_entries.empty)

        # YearSummaryHandler() will only show entries created this year, so if it's the first day of a year, it
        # will only show the two entries create on that day, not the ones from the previous year, so length of
        # summarized_entries will be the day of the year as an integer.
        expected_length_of_entries = datetime.datetime.today().timetuple().tm_yday
        self.assertEqual(expected_length_of_entries, len(summarized_entries))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
