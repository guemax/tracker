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


class TestFilterCommand(CommandBaseTestingClass):
    def setUp(self) -> None:
        super(TestFilterCommand, self).setUp()

    def test_filtering_without_passing_any_filters(self) -> None:
        self.setup_test_values(20)

        self.run_cli("filter")
        self.assertIn("No filter passed. Showing all entries.", self.output)


if __name__ == "__main__":
    unittest.main()
