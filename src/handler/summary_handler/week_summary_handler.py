import datetime

import pandas

from .summary_handler_interface import SummaryHandlerInterface


class WeekSummaryHandler(SummaryHandlerInterface):
    def __init__(self):
        super(WeekSummaryHandler, self).__init__()
        self.__current_week_number = datetime.datetime.now().isocalendar()[1]

    def summary(self) -> pandas.DataFrame:
        self._data = self._entry_handler.get_data()

        self.add_column_for_day_of_week()
        self.drop_rows_with_entries_not_created_this_week()

        self.group_entries_by_day_of_week()
        self.calculate_sum_and_mean_of_work_hours()
        self.rename_columns()

        self.boost_index()

        return self._data

    def add_column_for_day_of_week(self) -> None:
        self._data["week_number"] = self._data["start_date"].map(self.__get_week_number)

    @staticmethod
    def __get_week_number(date: str) -> int:
        date = datetime.datetime.strptime(date, "%b, %d %Y")
        return date.isocalendar()[1]

    def drop_rows_with_entries_not_created_this_week(self) -> None:
        self._data.drop(self._data.loc[self._data['week_number'] != self.__current_week_number].index, inplace=True)

    def group_entries_by_day_of_week(self) -> None:
        self._data = self._data.groupby("start_date", as_index=False)

    def calculate_sum_and_mean_of_work_hours(self) -> None:
        self._data = self._data \
            .agg(
                mean=pandas.NamedAgg(column="work_hours", aggfunc="mean"),
                sum=pandas.NamedAgg(column="work_hours", aggfunc="sum")
        )

        self._data["mean"] = self._data["mean"].map(self.__chop_microseconds)


    @staticmethod
    def __chop_microseconds(delta: datetime.timedelta) -> datetime.timedelta:
        return datetime.timedelta(seconds=round(delta.total_seconds()))

    def rename_columns(self) -> None:
        self._data = self._data.rename(
            columns={
                "start_date": "Date",
                "mean": "Mean",
                "sum": "Sum"
            }
        )

    def boost_index(self):
        self._data.index += 1

