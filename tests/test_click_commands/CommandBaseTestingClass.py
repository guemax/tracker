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

from click.testing import CliRunner

from tracker.__main__ import cli, setup_cli
from tests.BaseTestingClass import BaseTestingClass


class CommandBaseTestingClass(BaseTestingClass):
    def setUp(self) -> None:
        super(CommandBaseTestingClass, self).setUp()

        self.runner = CliRunner()
        self.output = None
        self.exit_code = -1

        setup_cli(cli)

    def run_cli(self, command: str, option: str = "") -> None:
        parameters = [command, option] if option != "" else [command]

        result = self.runner.invoke(cli, parameters)

        self.output = result.output
        self.exit_code = result.exit_code

    def check_for_exit_code_zero(self) -> None:
        self.assertEqual(self.exit_code, 0)

    def check_for_exit_code_two(self) -> None:
        self.assertEqual(self.exit_code, 2)     # Usage error, unexpected extra argument

    def check_for_exit_code_not_zero(self) -> None:
        self.assertNotEqual(self.exit_code, 0)

    def check_for_exit_code_minus_one(self) -> None:
        self.assertEqual(self.exit_code, -1)
