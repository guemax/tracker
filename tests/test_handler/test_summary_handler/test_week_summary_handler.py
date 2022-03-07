import datetime
import unittest

from src.handler.summary_handler.week_summary_handler import WeekSummaryHandler

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestWeekSummaryHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestWeekSummaryHandler, self).setUp()

        self.week_summary_handler = WeekSummaryHandler()

    def test_summary_without_any_entries_created_this_week(self) -> None:
        self.clean_and_init_tracker_file()

        summarized_entries = self.week_summary_handler.summary()
        self.assertTrue(summarized_entries.empty)

    def test_summary_with_one_entry_created_this_week(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values(1)

        summarized_entries = self.week_summary_handler.summary()

        self.assertFalse(summarized_entries.empty)
        self.assertEqual(1, len(summarized_entries))

    def test_summary_with_multiple_entries_created_this_week(self) -> None:
        self.clean_and_init_tracker_file()

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
