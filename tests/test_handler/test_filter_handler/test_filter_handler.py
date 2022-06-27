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

import unittest
from datetime import date

from tests.BaseTestingClass import BaseTestingClass

from tracker.handler.filter_handler.FilterHandler import FilterHandler
from tracker.handler.filter_handler.FilterObject import FilterObject


class TestFilterHandler(BaseTestingClass):
    def setUp(self) -> None:
        super(TestFilterHandler, self).setUp()

        self.filter_handler = FilterHandler()

    def test_filtering_for_day(self) -> None:
        self.setup_test_values(4)   # creates entries containing the date of today
        day = date.today().day

        filters = FilterObject(day=str(day))

        entries = self.filter_handler.filter_for(filters)
        self.assertFalse(entries.empty)
        self.assertEqual(len(entries), 2)

        filters = FilterObject(day=str(day + 1))

        entries = self.filter_handler.filter_for(filters)
        self.assertTrue(entries.empty)  # Cannot find entry of tomorrow...

    def test_filtering_for_month(self) -> None:
        self.setup_test_values(4)   # creates entries containing the date of today
        month = date.today().month

        filters = FilterObject(month=str(month))

        entries = self.filter_handler.filter_for(filters)
        self.assertFalse(entries.empty)

        # Only needed for the first of every month; two entries per day are created
        day = date.today().day
        expected_number_of_entries = 2 if day == 1 else 4
        self.assertEqual(len(entries), expected_number_of_entries)

        filters = FilterObject(month=str(month + 1))

        entries = self.filter_handler.filter_for(filters)
        self.assertTrue(entries.empty)  # Cannot find entry of tomorrow

    def test_filtering_for_year(self) -> None:
        self.setup_test_values(4)  # creates entries containing the date of today
        year = date.today().year

        filters = FilterObject(year=str(year))

        entries = self.filter_handler.filter_for(filters)
        self.assertFalse(entries.empty)

        # Only neded for the first of every year; two entries per day are created
        day = date.today().day
        month = date.today().month
        expected_number_of_entries = 2 if month == 1 and day == 1 else 4
        self.assertEqual(len(entries), expected_number_of_entries)

        filters = FilterObject(year=str(year + 1))

        entries = self.filter_handler.filter_for(filters)
        self.assertTrue(entries.empty)  # Cannot find entry of tomorrow

    def test_filtering_for_message(self) -> None:
        # TODO: Write test for that, difficult because message is chosen randomly!
        pass

    def test_filtering_for_date(self) -> None:
        self.setup_test_values(2)
        current_date = date.today()

        filters = FilterObject(str(current_date.day), str(current_date.month), str(current_date.year), "")

        entries = self.filter_handler.filter_for(filters)
        self.assertFalse(entries.empty)

        filters = FilterObject(str(current_date.day + 1), str(current_date.month), str(current_date.year), "")

        entries = self.filter_handler.filter_for(filters)
        self.assertTrue(entries.empty)

        filters = FilterObject(str(current_date.day), str(current_date.month + 1), str(current_date.year), "")

        entries = self.filter_handler.filter_for(filters)
        self.assertTrue(entries.empty)

        filters = FilterObject(str(current_date.day), str(current_date.month), str(current_date.year + 1), "")

        entries = self.filter_handler.filter_for(filters)
        self.assertTrue(entries.empty)


if __name__ == "__main__":
    unittest.main()
