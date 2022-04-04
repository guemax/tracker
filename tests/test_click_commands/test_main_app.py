"""This file is part of tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

from tracker.cli import cli
from tracker.setup_cli import setup_cli

from tracker.version import __version__

from .CommandBaseTestingClass import CommandBaseTestingClass


class TestMainApp(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestMainApp, self).setUp()

        setup_cli(cli)

    def test_help_information(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli()
        self.check_for_help_menu()

        self.run_cli("--help")
        self.check_for_help_menu()

    def check_for_help_menu(self) -> None:
        self.assertIn("Usage: cli [OPTIONS] COMMAND [ARGS]...", self.output)
        self.assertIn("A command-line tool to track your computer usage time.", self.output)

        self.assertIn("Options:", self.output)
        self.assertIn("--version  Show the version and exit.", self.output)
        self.assertIn("--help     Show this message and exit.", self.output)

        self.assertIn("Commands:", self.output)
        self.assertIn("log", self.output)
        self.assertIn("start", self.output)
        self.assertIn("status", self.output)
        self.assertIn("stop", self.output)
        self.assertIn("summary", self.output)

    def test_version_information(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("--version")
        self.assertIn(f"tracker, version {__version__}", self.output)
