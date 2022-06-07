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


class FilterHandler:
    def __init__(self, filters: list) -> None:
        self.filters = filters

    def remove_unused_filters(self) -> list:
        cleaned_filters = []

        for item in self.filters:
            if item != "" and item != 0:
                cleaned_filters.append(item)

        return cleaned_filters
