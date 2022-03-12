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

    def test_starting_a_timer_when_one_already_exists(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start"])
        self.assertEqual(self.result.exit_code, 0)

        self.run_cli(["start"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("A timer already exists", self.result.output)

    def test_starting_a_timer_with_invalid_option(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start", "--unknown-option"])
        self.assertEqual(self.result.exit_code, 2)

        self.assertIn("Error", self.result.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
