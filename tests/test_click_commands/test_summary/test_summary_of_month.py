import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestSummaryOfMonth(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestSummaryOfMonth, self).setUp()

    def test_summary_without_any_entries_created_this_month(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["summary", "-tm"])

        self.assertIn("Nothing to show yet. There have been no entries created this month.\n"
                      "Create one using \"tracker start\".", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_summary_with_one_entry_created_this_month(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values(1)

        self.run_cli(["summary", "-tm"])

        self.assertIn("Showing entries as summary (1 in total).\n"
                      "Range is \"this-month\".", self.result.output)
        self.assertIn("OK", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
