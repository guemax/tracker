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

import pandas

from src.csv.CSVAttributes import CSVAttributes
from src.handler.entry_handler.BaseEntryHandlerClass import BaseEntryHandlerClass

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestBaseEntryHandlerClass(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestBaseEntryHandlerClass, self).setUp()

        self.data = None
        self.csv_attributes = CSVAttributes()
        self.base_entry_handler = BaseEntryHandlerClass()

    def test_getting_empty_data(self) -> None:
        self.clean_and_init_tracker_file()
        self.data = self.base_entry_handler.get_data()
        self.assertEqual(list(self.data.columns), self.csv_attributes.column_names)

    def test_getting_filled_data(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values()

        self.data = self.base_entry_handler.get_data()

        self.assertEqual(list(self.data.columns), self.csv_attributes.column_names)
        self.assertTrue(len(self.data) > 0)

        self.assertTrue(self.data["work_hours"].dtypes == "timedelta64[ns]")

    def test_grouping_entries_by_date_with_empty_data(self) -> None:
        self.clean_and_init_tracker_file()

        self.base_entry_handler.data = self.base_entry_handler.get_data()
        entries_grouped_by_date = self.base_entry_handler.group_entries_by_date()

        self.assertEqual(len(entries_grouped_by_date), 0)

    def test_grouping_entries_by_date_with_filled_data(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values()

        self.base_entry_handler.data = self.base_entry_handler.get_data()
        entries_grouped_by_date = self.base_entry_handler.group_entries_by_date()

        self.assertNotEqual(type(entries_grouped_by_date), pandas.DataFrame)
        self.assertNotEqual(len(entries_grouped_by_date), 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
