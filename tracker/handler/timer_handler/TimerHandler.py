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
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

from .StartTimer import StartTimer
from .StopTimer import StopTimer

from .TimerBaseClass import TimerBaseClass


class TimerHandler(TimerBaseClass):
    def __init__(self) -> None:
        super(TimerHandler, self).__init__()

        self.start = StartTimer()
        self.stop = StopTimer()

    def start_timer(self, do_overwrite: bool = False) -> list:
        return self.start.do(do_overwrite)

    def stop_timer(self, message: str) -> list:
        return self.stop.do(message)
