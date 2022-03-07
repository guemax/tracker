import datetime

import pandas

from .summary_handler_interface import SummaryHandlerInterface


class YearSummaryHandler(SummaryHandlerInterface):
    def __init__(self):
        super(YearSummaryHandler, self).__init__()
        self.__current_year_number = datetime.datetime.now().year

    def summary(self) -> pandas.DataFrame:
        self._data = self._entry_handler.get_data()

        self._data = self.add_column_for_year_number()
        self._data = self.drop_rows_with_entries_not_created_this_year()

        self._data = self.group_entries_by_date()
        self._data = self.calculate_sum_and_mean_of_work_hours()
        self._data = self.remove_microseconds_from_mean_values()
        self._data = self.rename_columns()

        self._data = self.boost_index()

        return self._data

    def add_column_for_year_number(self) -> pandas.DataFrame:
        data = self._data
        data["year_number"] = self._data["start_date"].map(self.__get_year_number)

        return data

    @staticmethod
    def __get_year_number(date: str) -> int:
        date = datetime.datetime.strptime(date, "%b, %d %Y")
        return date.year

    def drop_rows_with_entries_not_created_this_year(self) -> pandas.DataFrame:
        entries_to_drop = self._data.loc[self._data['year_number'] != self.__current_year_number]
        return self._data.drop(entries_to_drop.index)

    def group_entries_by_date(self) -> pandas.DataFrame:
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
