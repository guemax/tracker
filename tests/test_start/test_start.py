import unittest

from click.testing import CliRunner

from src.main import cli, setup_cli


class TestStart(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()
        self.result = None

        setup_cli()

    def test_starting_a_timer(self) -> None:
        self.result = self.runner.invoke(cli, ["start"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("New timer started", self.result.output)
        self.assertIn("OK", self.result.output)

    def test_starting_a_timer_with_invalid_option(self) -> None:
        self.result = self.runner.invoke(cli, ["start", "--unknown-option"])
        self.assertEqual(self.result.exit_code, 2)

        self.assertIn("Error", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
