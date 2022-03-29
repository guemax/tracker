"""This file is part of Tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import unittest
import os

from click.testing import CliRunner

from src.main import cli, add_subcommands_to_cli

from src.csv.CSVHandler import CSVHandler
from src.setup_test_values.setup_test_values import SetupTestValues


class CommandBaseTestingClass(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()
        self.output = None
        self.exit_code = -1

        self.csv_handler = CSVHandler()
        self.set_upper = SetupTestValues()

        add_subcommands_to_cli()

    def run_cli(self, command: str, option: str = "") -> None:
        parameters = [command, option] if option != "" else [command]

        result = self.runner.invoke(cli, parameters)

        self.output = result.output
        self.exit_code = result.exit_code

    # TODO: Duplicated code in this class and CSVBaseTestingClass()
    def clean_and_init_tracker_file(self) -> None:
        self.remove_tracker_file()
        self.csv_handler.init_tracker_csv_file()

    def remove_tracker_file(self) -> None:
        try:
            os.remove(self.csv_handler.tracker_file)
        except FileNotFoundError:
            # File is not existing, that's good, nothing to do for us.
            pass

    def setup_test_values(self, number_of_entries: int = 4) -> None:
        self.set_upper.set_number_of_entries(number_of_entries)
        self.set_upper.setup()
