import unittest
import os

from click.testing import CliRunner

from src.main import cli, add_subcommands_to_cli

from src.csv.CSVHandler import CSVHandler
from src.setup_test_values.setup_test_values import SetupTestValues


class CommandBaseTestingClass(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()
        self.result = None

        self.csv_handler = CSVHandler()
        self.set_upper = SetupTestValues()

        add_subcommands_to_cli()

    def run_cli(self, options: list) -> None:
        self.result = self.runner.invoke(cli, options)

    def clean_and_init_tracker_file(self) -> None:
        self.remove_tracker_file()
        self.csv_handler.init_tracker_csv_file()

    def remove_tracker_file(self) -> None:
        try:
            os.remove(self.csv_handler.tracker_file)
        except FileNotFoundError:
            # File is not existing, that's good, nothing to do for us.
            pass

    def setup_test_values(self) -> None:
        self.set_upper.setup()
