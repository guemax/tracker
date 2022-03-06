from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestSummaryOfWeek(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestSummaryOfWeek, self).setUp()

    def test_summary_without_any_entries_created_this_week(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["summary", "-tw"])

        self.assertIn("Showing entries as summary (0 in total).\n"
                      "Range is \"this-week\".", self.result.output)

        self.assertIn("OK", self.result.output)

    def test_summary_with_some_entries_created_this_week(self) -> None:
        pass
