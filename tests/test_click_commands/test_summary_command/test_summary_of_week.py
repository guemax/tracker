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


class TestSummaryOfWeek(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestSummaryOfWeek, self).setUp()

    def test_summary_without_any_entries_created_this_week(self) -> None:
        self.clean_and_init_tracker_file()

        self.run_cli(["summary", "-tw"])

        self.assertIn("Nothing to show yet. There have been no entries created this week.\n"
                      "Create one using \"tracker start\".", self.output)
        self.assertIn("OK", self.output)

    def test_summary_with_some_entries_created_this_week(self) -> None:
        self.clean_and_init_tracker_file()
        self.setup_test_values(1)

        self.run_cli(["summary", "-tw"])

        self.assertIn("Showing entries as summary (1 in total).\n"
                      "Range is \"this-week\".", self.output)
        self.assertIn("OK", self.output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
