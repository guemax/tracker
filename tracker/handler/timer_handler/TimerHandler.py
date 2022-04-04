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

from datetime import datetime

import pandas

from tracker.csv.CSVAttributes import CSVAttributes
from tracker.exceptions.InvalidTimerModification import InvalidTimerModification


class TimerHandler(CSVAttributes):
    def __init__(self) -> None:
        super(TimerHandler, self).__init__()

    def start_timer(self, overwrite: bool = False) -> list:
        overwritten = False

        if not overwrite and self.unfinished_entry_present():
            raise InvalidTimerModification()
        elif overwrite and self.unfinished_entry_present():
            self.overwrite_existing_timer()
            overwritten = True

        start_date = datetime.now().strftime("%b, %d %Y")
        start_time = datetime.now().strftime("%H:%M:%S")

        row = {
                "start_date": start_date, "start_time": start_time, "stop_date": None, "stop_time": None,
                "work_hours": None, "message": None
        }
        new_row = pandas.DataFrame(row, index=[0])

        data = pandas.read_csv(self.tracker_file, dtype=str)
        data = pandas.concat([data, new_row], ignore_index=True)

        data.to_csv(self.tracker_file, index=False)

        return [start_date, start_time, overwritten]

    def overwrite_existing_timer(self) -> None:
        data = pandas.read_csv(self.tracker_file, dtype=str)

        last_row = data.tail(1)
        data.drop(last_row.index, inplace=True)

        data.to_csv(self.tracker_file, index=False)

    def stop_timer(self, message: str) -> list:
        if not self.unfinished_entry_present():
            raise InvalidTimerModification()

        stop_date = datetime.now().strftime("%b, %d %Y")
        stop_time = datetime.now().strftime("%H:%M:%S")

        data = pandas.read_csv(self.tracker_file, dtype=str)

        index = len(data) - 1

        start_time = data.at[index, "start_time"]

        stop_time_obj = datetime.strptime(stop_time, "%H:%M:%S")
        start_time_obj = datetime.strptime(start_time, "%H:%M:%S")
        work_hours = str(stop_time_obj - start_time_obj)

        data.at[index, "stop_date"] = stop_date
        data.at[index, "stop_time"] = stop_time
        data.at[index, "work_hours"] = work_hours
        data.at[index, "message"] = message

        data.to_csv(self.tracker_file, index=False)

        return [stop_date, stop_time, work_hours]

    def unfinished_entry_present(self) -> bool:
        data = pandas.read_csv(self.tracker_file, dtype=str)
        data = data.fillna("")

        if len(data) == 0:
            return False

        index = len(data) - 1

        if data.at[index, "start_time"] != "" and data.at[index, "stop_time"] == "":
            return True

        return False
