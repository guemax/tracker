import unittest

from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler
from src.handler.timer_handler.TimerHandler import TimerHandler

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestGroupedEntryHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestGroupedEntryHandler, self).setUp()
        self.grouped_entry_handler = GroupedEntryHandler()
        self.timer_handler = TimerHandler()

        self.column_names = ["Date", "Total work time", "Individual entries"]

    def test_logging_without_any_grouped_entries(self) -> None:
        self.clean_and_init_tracker_file()
        self.assertEqual(self.get_length_of_grouped_entries(), 0)

    def get_length_of_grouped_entries(self) -> int:
        return len(self.grouped_entry_handler.get_entries_grouped_by_date())

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

        column_names = list(self.grouped_entry_handler.get_entries_grouped_by_date().columns)
        self.assertEqual(column_names, self.column_names)

        index_name = self.grouped_entry_handler.get_entries_grouped_by_date().index.name
        self.assertEqual(index_name, "ID")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
