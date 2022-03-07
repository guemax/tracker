import unittest

from src.handler.summary_handler.week_summary_handler import WeekSummaryHandler

from tests.test_csv.CSVBaseTestingClass import CSVBaseTestingClass


class TestTimerHandler(CSVBaseTestingClass):
    def setUp(self) -> None:
        super(TestTimerHandler, self).setUp()

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


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
