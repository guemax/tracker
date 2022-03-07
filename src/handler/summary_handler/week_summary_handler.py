import datetime

import pandas

from .summary_handler_interface import SummaryHandlerInterface


class WeekSummaryHandler(SummaryHandlerInterface):
    def __init__(self):
        super(WeekSummaryHandler, self).__init__()
        self.__current_week_number = datetime.datetime.now().isocalendar()[1]

    def summary(self) -> pandas.DataFrame:
        self._data = self._entry_handler.get_data()

        # Add column for the week number to filter for this week's number
        self._data["week_number"] = self._data["start_date"].map(self.__get_week_number)

        # Remove all rows not containing this week's weeknumber
        self._data.drop(self._data.loc[self._data['week_number'] != self.__current_week_number].index, inplace=True)

        self._data = self._data.groupby("start_date", as_index=False)

        self._data = self._data \
            .agg(
                    mean=pandas.NamedAgg(column="work_hours", aggfunc="mean"),
                    sum=pandas.NamedAgg(column="work_hours", aggfunc="sum")
                )

        self._data["mean"] = self._data["mean"].map(self.__chop_microseconds)
        self._data = self._data.rename(
            columns={
                "start_date": "Date",
                "mean": "Mean",
                "sum": "Sum"
            }
        )
        self._data.index += 1
        return self._data

    @staticmethod
    def __get_week_number(date: str) -> int:
        date = datetime.datetime.strptime(date, "%b, %d %Y")
        return date.isocalendar()[1]

    @staticmethod
    def __chop_microseconds(delta: datetime.timedelta) -> datetime.timedelta:
        return datetime.timedelta(seconds=round(delta.total_seconds()))

    def boost_index(self):
        pass
