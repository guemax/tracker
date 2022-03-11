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

import pandas

from src.csv.CSVAttributes import CSVAttributes


class BaseEntryHandlerClass(CSVAttributes):
    def __init__(self):
        super(BaseEntryHandlerClass, self).__init__()

        self.data = None

    def get_data(self) -> pandas.DataFrame:
        data = pandas.read_csv(self.tracker_file, header=0)

        # Change this column to a time type for allowing summing up the total work hours later
        data["work_hours"] = pandas.to_timedelta(data.work_hours)

        return data.fillna("")

    def group_entries_by_date(self) -> pandas.DataFrame:
        data_grouped_by_date = self.data.groupby("start_date", as_index=False)
        return data_grouped_by_date
