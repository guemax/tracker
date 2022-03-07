import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestSummaryOfYear(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestSummaryOfYear, self).setUp()

    def test_summary_without_any_entries_created_this_year(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["summary", "-ty"])

        self.assertIn("Nothing to show yet. There have been no entries created this year.\n"
                      "Create one using \"tracker start\".", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_summary_with_one_entry_created_this_year(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values(1)

        self.run_cli(["summary", "-ty"])

        self.assertIn("Showing entries as summary (1 in total).\n"
                      "Range is \"this-year\".", self.result.output)
        self.assertIn("OK", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
