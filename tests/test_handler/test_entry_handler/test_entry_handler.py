import unittest

import pandas

from src.handler.entry_handler.EntryHandler import EntryHandler
from src.exceptions.InvalidIDOfDateException import InvalidIDOfDateException

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

        self.assertIn(date, entries_of_date.at[1, "Start"])

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
