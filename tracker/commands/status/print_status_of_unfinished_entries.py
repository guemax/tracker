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

from tracker.handler.timer_handler.TimerHandler import TimerHandler
from .print_list_item import print_list_item


def print_status_of_unfinished_entries():
    timer_handler = TimerHandler()
    unfinished_entries_present = timer_handler.unfinished_entry_present()

    if unfinished_entries_present:
        print_list_item("A timer exists which has not been stopped yet.")
    else:
        print_list_item("No unfinished timer exists.")
