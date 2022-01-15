import unittest

import pandas

from src.setup_test_values import setup_test_values
from src.handler.entry_handler.EntryHandler import EntryHandler
from src.handler.timer_handler.TimerHandler import TimerHandler
from src.exceptions.InvalidIDOfDateException import InvalidIDOfDateException

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestEntryHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestEntryHandler, self).setUp()
        self.entry_handler = EntryHandler()
        self.timer_handler = TimerHandler()

        self.column_names = ["Date", "Total work time", "Individual entries"]

    def test_logging_entries_of_specific_date(self) -> None:
        self.clean_and_init_tracker_file()
        setup_test_values()

        entries = self.entry_handler.get_entries_of_specific_date(1)
        date = entries[0]
        entries_of_date = entries[1]

        self.assertEqual(type(date), str)
        self.assertEqual(type(entries_of_date), pandas.DataFrame)

        self.assertIn(date, entries_of_date.at[1, "Start"])

    def test_logging_entries_of_specific_date_without_any_entries(self) -> None:
        self.clean_and_init_tracker_file()

        self.check_for_invalid_id_of_date_exception(0)
        self.check_for_invalid_id_of_date_exception(1)
        self.check_for_invalid_id_of_date_exception(2)

    def check_for_invalid_id_of_date_exception(self, id_of_date: int) -> None:
        self.assertRaises(InvalidIDOfDateException, self.entry_handler.get_entries_of_specific_date, id_of_date)

    def test_logging_entries_of_soecific_date_with_unknown_id(self) -> None:
        self.clean_and_init_tracker_file()
        setup_test_values()

        self.check_for_invalid_id_of_date_exception(0)
        self.check_for_invalid_id_of_date_exception(-1)
        self.check_for_invalid_id_of_date_exception(100)

    def test_logging_without_any_grouped_entries(self) -> None:
        self.clean_and_init_tracker_file()
        self.assertEqual(self.get_length_of_grouped_entries(), 0)

    def get_length_of_grouped_entries(self) -> int:
        return len(self.entry_handler.get_entries_grouped_by_date())

    def test_logging_with_more_grouped_entries(self) -> None:
        self.clean_and_init_tracker_file()

        self.add_new_entry()
        self.assertEqual(self.get_length_of_grouped_entries(), 1)

        self.timer_handler.start_timer()
        self.timer_handler.stop_timer("")

        # Entries are grouped by date, so adding two or more entries at the same day won't increase the length
        self.add_new_entry()
        self.assertEqual(self.get_length_of_grouped_entries(), 1)

        self.add_new_entry()
        self.add_new_entry()
        self.assertEqual(self.get_length_of_grouped_entries(), 1)

    def add_new_entry(self):
        self.timer_handler.start_timer()
        self.timer_handler.stop_timer("")

    def test_column_names_of_grouped_entries(self):
        self.clean_and_init_tracker_file()
        self.add_new_entry()

        column_names = list(self.entry_handler.get_entries_grouped_by_date().columns)
        self.assertEqual(column_names, self.column_names)

        index_name = self.entry_handler.get_entries_grouped_by_date().index.name
        self.assertEqual(index_name, "ID")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
