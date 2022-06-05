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

from datetime import datetime

import pandas

from tracker.handler.timer_handler.TimerBaseClass import TimerBaseClass
from tracker.exceptions.InvalidTimerModification import InvalidTimerModification


class StopTimer(TimerBaseClass):
    def __init__(self) -> None:
        super(StopTimer, self).__init__()

    def do(self, message: str) -> list:
        if self.__cannot_stop_timer():
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

    def __cannot_stop_timer(self) -> bool:
        return not self.unfinished_entry_present()
