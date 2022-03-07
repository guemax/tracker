import datetime
import unittest

from src.handler.summary_handler.month_summary_handler import MonthSummaryHandler

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestMonthSummaryHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestMonthSummaryHandler, self).setUp()

        self.month_summary_handler = MonthSummaryHandler()

    def test_summary_without_any_entries_created_this_month(self) -> None:
        self.clean_and_init_tracker_file()

        summarized_entries = self.month_summary_handler.summary()
        self.assertTrue(summarized_entries.empty)

    def test_summary_with_one_entry_created_this_month(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values(1)

        summarized_entries = self.month_summary_handler.summary()

        self.assertFalse(summarized_entries.empty)
        self.assertEqual(1, len(summarized_entries))

    def test_summary_with_multiple_entries_created_this_week(self) -> None:
        self.clean_and_init_tracker_file()

        # Set up two entries per day (40 grouped entries)
        self.setup_test_values(80)

        summarized_entries = self.month_summary_handler.summary()

        self.assertFalse(summarized_entries.empty)

        # MonthSummaryHandler() will only show entries created this month, so if it's the first of a given month, it
        # will only show the two entries create on that day, not the ones from the previous month, so length of
        # summarized_entries will be the day of the month as an integer.
        expected_length_of_entries = datetime.datetime.today().day
        self.assertEqual(expected_length_of_entries, len(summarized_entries))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
