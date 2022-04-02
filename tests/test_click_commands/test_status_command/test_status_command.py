"""This file is part of tracker.
tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import unittest

from ..CommandBaseTestingClass import CommandBaseTestingClass


class TestStatus(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestStatus, self).setUp()

    def test_showing_the_status_with_no_entries_present(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from tracker", self.output)
        self.assertIn(" - No unfinished timer exists.", self.output)
        self.assertIn(" - Zero (0) entries found. (use \"tracker start\" to create one)", self.output)
        self.assertIn(" - Zero (0) grouped entries found.", self.output)
        self.assertIn("OK", self.output)

    def test_showing_the_status_with_one_entry_present(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(1)

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from tracker", self.output)
        self.assertIn(" - No unfinished timer exists.", self.output)
        self.assertIn(" - One (1) entry found.", self.output)
        self.assertIn(" - One (1) grouped entry found.", self.output)
        self.assertIn("OK", self.output)

    def test_showing_the_status_with_two_entries_present(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(2)

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from tracker", self.output)
        self.assertIn(" - No unfinished timer exists.", self.output)
        self.assertIn(" - Two (2) entries found.", self.output)
        # The two entries were created at the same day, so they are in one group -> one grouped entry
        self.assertIn(" - One (1) grouped entry found.", self.output)
        self.assertIn("OK", self.output)

    def test_showing_the_status_with_multiple_grouped_entries_present(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.setup_test_values(12)

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from tracker", self.output)
        self.assertIn(" - No unfinished timer exists.", self.output)
        self.assertIn(" - Twelve (12) entries found.", self.output)
        # Two entries per group -> six grouped entries
        self.assertIn(" - Six (6) grouped entries found.", self.output)
        self.assertIn("OK", self.output)

    def test_showing_the_status_with_unfinished_timer_exisiting(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.run_cli("start")

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from tracker", self.output)
        self.assertIn(
            " - A timer exists which has not been stopped yet. (use \"tracker stop -m 'message'\" to stop it)",
            self.output
        )
        self.assertIn(" - One (1) entry found.", self.output)
        self.assertIn(" - One (1) grouped entry found.", self.output)
        self.assertIn("OK", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
