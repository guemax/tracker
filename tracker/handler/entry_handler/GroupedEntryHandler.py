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

import pandas

from tracker.handler.entry_handler.BaseEntryHandlerClass import BaseEntryHandlerClass


class GroupedEntryHandler(BaseEntryHandlerClass):
    def __init__(self):
        super(GroupedEntryHandler, self).__init__()

    def get_entries_grouped_by_date(self) -> pandas.DataFrame:
        self.data = self.get_data()

        self.data = self.group_entries_by_date()
        self.data = self.sum_work_hours_up()
        self.data = self.rename_columns()

        self.change_index()

        self.data = self.reorder_entries_from_the_latest_down_to_the_oldest_one()

        return self.data

    def sum_work_hours_up(self) -> pandas.DataFrame:
        data_with_sum_of_work_hours = self.data \
            .agg(
                    work_hours=pandas.NamedAgg(column="work_hours", aggfunc="sum"),
                    individual_entries=pandas.NamedAgg(column="start_date", aggfunc="size")
                )
        return data_with_sum_of_work_hours

    def rename_columns(self) -> pandas.DataFrame:
        data_with_renamed_columns = self.data \
            .rename(columns={
                                "start_date": "Date", "work_hours": "Total work time",
                                "individual_entries": "Individual entries"
                            }
                    )
        return data_with_renamed_columns

    def change_index(self) -> None:
        self.name_index_column()
        self.boost_index()

    def name_index_column(self) -> None:
        self.data.index.name = "ID"

    def boost_index(self) -> None:
        self.data.index += 1

    def reorder_entries_from_the_latest_down_to_the_oldest_one(self) -> pandas.DataFrame:
        reordered_data = self.data.iloc[::-1]
        return reordered_data
