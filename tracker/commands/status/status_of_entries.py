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

from num2words import num2words

from tracker.handler.entry_handler.EntryHandler import EntryHandler


def status_of_entries() -> str:
    handler = EntryHandler()

    number_of_entries = len(handler.get_data())
    number_of_entries_as_word = num2words(number_of_entries).title()

    if number_of_entries == 0:
        return f"{number_of_entries_as_word} ({number_of_entries}) entries found. " \
               f"(use \"tracker start\" to create one)"
    elif number_of_entries == 1:
        return f"{number_of_entries_as_word} ({number_of_entries}) entry found."
    else:
        return f"{number_of_entries_as_word} ({number_of_entries}) entries found."
