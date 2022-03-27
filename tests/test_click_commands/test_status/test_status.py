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

    def test_showing_the_status_with_two_entries_present(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["start"])
        self.run_cli(["stop"])

        self.run_cli(["start"])
        self.run_cli(["stop"])

        self.run_cli(["status"])
        self.assertEqual(self.result.exit_code, 0)

        self.assertIn("Status information from Tracker", self.result.output)
        self.assertIn(" - No unfinished timer exists.", self.result.output)
        self.assertIn(" - Two (2) entries found.", self.result.output)
        # The two entries were created at the same day, so they are in one group -> one grouped entry
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
