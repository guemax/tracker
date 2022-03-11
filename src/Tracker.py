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

from .csv import CSVHandler


class Tracker:
    def __init__(self):     # pragma: no cover
        self.csv_handler = CSVHandler.CSVHandler()

    def init_tracker_file(self):     # pragma: no cover
        self.csv_handler.init_tracker_csv_file()
