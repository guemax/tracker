import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass
from src.setup_test_values import setup_test_values


class TestLog(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestLog, self).setUp()

    def test_logging_a_specific_entry(self) -> None:
        self.clean_and_init_tracker_file()
        setup_test_values()

        self.run_cli(["log", "-i 1"])

        self.assertIn("Showing all entries of", self.result.output)

    def test_logging_a_sepcific_entry_with_unknown_id(self) -> None:
        self.clean_and_init_tracker_file()
        setup_test_values()

        id_of_date = -1
        self.run_cli(["log", f"-i {id_of_date}"])

        self.assertIn(f"We couldn't find a date matching the ID {id_of_date}.", self.result.output)
        self.assertIn("EXIT", self.result.output)

        id_of_date = 0
        self.run_cli(["log", f"-i {id_of_date}"])

        self.assertIn(f"We couldn't find a date matching the ID {id_of_date}.", self.result.output)
        self.assertIn("EXIT", self.result.output)

        id_of_date = 100
        self.run_cli(["log", f"-i {id_of_date}"])

        self.assertIn(f"We couldn't find a date matching the ID {id_of_date}.", self.result.output)
        self.assertIn("EXIT", self.result.output)

    def test_logging_without_any_entries_existing(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["log"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Nothing to see yet.", self.result.output)

    def test_logging_with_one_entry(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start"])
        self.run_cli(["stop"])

        total_dates = 1
        self.check_for_log_message(total_dates)

    def test_logging_with_multiple_entries(self) -> None:
        self.clean_and_init_tracker_file()

        setup_test_values()

        total_dates = 2
        self.check_for_log_message(total_dates)

    def check_for_log_message(self, total_dates: int) -> None:
        self.run_cli(["log"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Showing all entries", self.result.output)
        self.assertIn(f"({total_dates} in total)", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
