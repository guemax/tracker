import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestStatus(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestStatus, self).setUp()

    def test_showing_the_status_with_no_entries_present(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["status"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Status information from Tracker", self.result.output)
        self.assertIn(" - No unfinished timer exists.", self.result.output)
        self.assertIn(" - Zero (0) entries found. Create one by typing \"tracker start\".", self.result.output)
        self.assertIn(" - Zero (0) grouped entries found.", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_showing_the_status_with_one_entry_present(self) -> None:
        self.clean_and_init_tracker_file()
        self.run_cli(["start"])
        self.run_cli(["stop"])

        self.run_cli(["status"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Status information from Tracker", self.result.output)
        self.assertIn(" - No unfinished timer exists.", self.result.output)
        self.assertIn(" - One (1) entry found.", self.result.output)
        self.assertIn(" - One (1) grouped entry found.", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_showing_the_status_with_unfinished_timer_exisiting(self) -> None:
        self.clean_and_init_tracker_file()
        self.run_cli(["start"])

        self.run_cli(["status"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Status information from Tracker", self.result.output)
        self.assertIn(" - A timer exists which has not been stopped yet.", self.result.output)
        self.assertIn(" - One (1) entry found.", self.result.output)
        self.assertIn(" - One (1) grouped entry found.", self.result.output)
        self.assertIn("OK", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
