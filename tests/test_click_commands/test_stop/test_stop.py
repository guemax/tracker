import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestStart(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestStart, self).setUp()

    def test_stopping_a_timer_without_message(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start"])
        self.run_cli(["stop"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Existing timer stopped", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_starting_a_timer_with_message(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start"])
        self.run_cli(["stop", "-m \"My message\""])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Existing timer stopped", self.result.output)
        self.assertIn("with message", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_stopping_a_timer_when_no_one_exists(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["stop"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("No timer exists yet", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
