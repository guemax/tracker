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


from tracker.handler.tracker_file_handler.TrackerFileAttributes import TrackerFileAttributes


class TimerBaseClass(TrackerFileAttributes):
    def __init__(self) -> None:
        super(TimerBaseClass, self).__init__()

    def unfinished_entry_present(self) -> bool:
        data = pandas.read_csv(self.tracker_file, dtype=str)
        data = data.fillna("")

        if len(data) == 0:
            return False

        index = len(data) - 1

        if data.at[index, "start_time"] != "" and data.at[index, "stop_time"] == "":
            return True

        return False
