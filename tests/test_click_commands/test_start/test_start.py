import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestStart(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestStart, self).setUp()

    def test_starting_a_timer(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("New timer started", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_starting_a_timer_with_invalid_option(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start", "--unknown-option"])
        self.assertEqual(self.result.exit_code, 2)

        self.assertIn("Error", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
