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

from tracker.handler.timer_handler.TimerHandler import TimerHandler


def status_of_unfinished_entries() -> str:
    handler = TimerHandler()
    unfinished_entries_present = handler.unfinished_entry_present()

    if unfinished_entries_present:
        return "A timer exists which has not been stopped yet. (use \"tracker stop -m 'message'\" to stop it)"
    else:
        return "No unfinished timer exists."
