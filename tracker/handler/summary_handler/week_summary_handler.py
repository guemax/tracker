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

import datetime

import pandas

from .summary_handler_interface import SummaryHandlerInterface


class WeekSummaryHandler(SummaryHandlerInterface):
    def __init__(self):
        super(WeekSummaryHandler, self).__init__()
        self.__current_week_number = datetime.datetime.now().isocalendar()[1]

    def summary(self) -> pandas.DataFrame:
        self._data = self._entry_handler.get_data()

        self._data = self.add_column_for_week_number()
        self._data = self.drop_rows_with_entries_not_created_this_week()

        self._data = self.group_entries_by_day_of_week()
        self._data = self.calculate_sum_and_mean_of_work_hours()
        self._data = self.remove_microseconds_from_mean_values()
        self._data = self.rename_columns()

        self._data = self.boost_index()

        return self._data

    def add_column_for_week_number(self) -> pandas.DataFrame:
        data = self._data
        data["week_number"] = self._data["start_date"].map(self.__get_week_number)

        return data

    @staticmethod
    def __get_week_number(date: str) -> int:
        date = datetime.datetime.strptime(date, "%b, %d %Y")
        return date.isocalendar()[1]

    def drop_rows_with_entries_not_created_this_week(self) -> pandas.DataFrame:
        entries_to_drop = self._data.loc[self._data['week_number'] != self.__current_week_number]
        return self._data.drop(entries_to_drop.index)

    def group_entries_by_day_of_week(self) -> pandas.DataFrame:
        return self._data.groupby("start_date", as_index=False)

    def calculate_sum_and_mean_of_work_hours(self) -> pandas.DataFrame:
        return self._data \
            .agg(
                mean=pandas.NamedAgg(column="work_hours", aggfunc="mean"),
                sum=pandas.NamedAgg(column="work_hours", aggfunc="sum")
                )

    def remove_microseconds_from_mean_values(self) -> pandas.DataFrame:
        data = self._data
        data["mean"] = self._data["mean"].map(self.__chop_microseconds)

        return data

    @staticmethod
    def __chop_microseconds(delta: datetime.timedelta) -> datetime.timedelta:
        return datetime.timedelta(seconds=round(delta.total_seconds()))

    def rename_columns(self) -> pandas.DataFrame:
        return self._data.rename(
            columns={
                "start_date": "Date",
                "mean": "Mean",
                "sum": "Sum"
            }
        )

    def boost_index(self):
        data = self._data
        data.index += 1

        return data
