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


class StartTimer(TimerBaseClass):
    def __init__(self) -> None:
        super(StartTimer, self).__init__()

        self.__do_overwrite = False
        self.__overwritten_timer = False

    def do(self, do_overwrite: bool = False) -> list:
        self.__do_overwrite = do_overwrite

        if self.__cannot_start_timer():
            raise InvalidTimerModification()
        elif self.__should_overwrite_existing_timer():
            self.__overwrite_existing_timer()

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

        return [start_date, start_time, self.__overwritten_timer]

    def __cannot_start_timer(self) -> bool:
        return not self.__do_overwrite and self.unfinished_entry_present()

    def __should_overwrite_existing_timer(self) -> bool:
        return self.__do_overwrite and self.unfinished_entry_present()

    def __overwrite_existing_timer(self) -> None:
        data = pandas.read_csv(self.tracker_file, dtype=str)

        last_row = data.tail(1)
        data.drop(last_row.index, inplace=True)

        data.to_csv(self.tracker_file, index=False)
        self.__overwritten_timer = True
