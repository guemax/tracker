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

from tracker.handler.entry_handler.EntryHandler import EntryHandler
from tracker.exceptions.InvalidIDOfDateException import InvalidIDOfDateException

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestEntryHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestEntryHandler, self).setUp()

        self.entry_handler = EntryHandler()

    def test_logging_entries_of_specific_date(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values()

        entries = self.entry_handler.get_entries_of_specific_date(1)
        date = entries[0]
        entries_of_date = entries[1]

        self.assertEqual(type(date), str)
        self.assertEqual(type(entries_of_date), pandas.DataFrame)

    def test_logging_entries_of_specific_date_without_any_entries_existing(self) -> None:
        self.clean_and_init_tracker_file()

        self.check_for_invalid_id_of_date_exception(0)
        self.check_for_invalid_id_of_date_exception(1)
        self.check_for_invalid_id_of_date_exception(2)

    def check_for_invalid_id_of_date_exception(self, id_of_date: int) -> None:
        self.assertRaises(InvalidIDOfDateException, self.entry_handler.get_entries_of_specific_date, id_of_date)

    def test_logging_entries_of_specific_date_with_unknown_id(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values()

        self.check_for_invalid_id_of_date_exception(0)
        self.check_for_invalid_id_of_date_exception(-1)
        self.check_for_invalid_id_of_date_exception(100)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
