import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestLog(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestLog, self).setUp()

    def test_logging_a_specific_entry(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values()

        self.run_cli(["log", "-i 1"])

        self.assertIn("Showing all entries of", self.result.output)

    def test_logging_a_sepcific_entry_with_unknown_id(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values()

        self.check_for_not_matching_id_of_date(-1)
        self.check_for_not_matching_id_of_date(0)
        self.check_for_not_matching_id_of_date(100)

    def check_for_not_matching_id_of_date(self, id_of_date: int) -> None:
        self.run_cli(["log", f"-i {id_of_date}"])

        self.assertIn(f"We couldn't find a date matching the ID {id_of_date}.", self.result.output)
        self.assertIn("EXIT", self.result.output)

    def test_logging_without_any_grouped_entries_existing(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["log"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Nothing to see yet.", self.result.output)

    def test_logging_with_one_grouped_entry(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start"])
        self.run_cli(["stop"])

        total_dates = 1
        self.check_for_log_message(total_dates)

    def check_for_log_message(self, total_dates: int) -> None:
        self.run_cli(["log"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Showing all entries", self.result.output)
        self.assertIn(f"({total_dates} in total)", self.result.output)

    def test_logging_with_multiple_grouped_entries(self) -> None:
        self.clean_and_init_tracker_file()

        self.setup_test_values()

        total_dates = 2
        self.check_for_log_message(total_dates)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
