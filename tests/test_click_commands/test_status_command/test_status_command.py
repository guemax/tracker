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


class TestStatusCommand(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestStatusCommand, self).setUp()

    def test_showing_the_status_with_no_entries_present(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from Tracker:\n\n"
                      " - No unfinished timer exists.\n"
                      " - Zero (0) entries found. (use \"Tracker start\" to create one)\n"
                      " - Zero (0) grouped entries found.", self.output)
        self.assertIn("OK", self.output)

    def test_showing_the_status_with_one_entry_present(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.run_cli("start")
        self.run_cli("stop")

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from Tracker:\n\n"
                      " - No unfinished timer exists.\n"
                      " - One (1) entry found.\n"
                      " - One (1) grouped entry found.", self.output)
        self.assertIn("OK", self.output)

    def test_showing_the_status_with_two_entries_present(self) -> None:
        self.remove_files_folder_and_init_tracker_file()

        self.setup_test_values(2)

        self.run_cli("status")
        self.check_for_exit_code_zero()

        # The two entries were created at the same day, so they are in one group -> one grouped entry
        self.assertIn("Status information from Tracker:\n\n"
                      " - No unfinished timer exists.\n"
                      " - Two (2) entries found.\n"
                      " - One (1) grouped entry found.", self.output)
        self.assertIn("OK", self.output)

    def test_showing_the_status_with_unfinished_timer_exisiting(self) -> None:
        self.remove_files_folder_and_init_tracker_file()
        self.run_cli("start")

        self.run_cli("status")
        self.check_for_exit_code_zero()

        self.assertIn("Status information from Tracker:\n\n"
                      " - A timer exists which has not been stopped yet."
                      " (use \"Tracker stop -m \'message\'\" to stop it)\n"
                      " - One (1) entry found.\n"
                      " - One (1) grouped entry found.", self.output)
        self.assertIn("OK", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
