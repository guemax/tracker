import datetime

import pandas

from .summary_handler_interface import SummaryHandlerInterface


class WeekSummaryHandler(SummaryHandlerInterface):
    def __init__(self):
        super(WeekSummaryHandler, self).__init__()
        self.__current_week_number = datetime.datetime.now().isocalendar()[1]

    def summary(self) -> pandas.DataFrame:
        entries = self._entry_handler.get_data()

        # Add column for the week number to filter for this week's number
        entries["week_number"] = entries["start_date"].map(self.__get_week_number)

        # Remove all rows not containing this week's weeknumber
        entries.drop(entries.loc[entries['week_number'] != self.__current_week_number].index, inplace=True)

        entries_grouped_by_date = entries.groupby("start_date", as_index=False)

        data_with_average_work_hours = entries_grouped_by_date \
            .agg(
                    mean=pandas.NamedAgg(column="work_hours", aggfunc="mean"),
                    sum=pandas.NamedAgg(column="work_hours", aggfunc="sum")
                )

        data_with_average_work_hours["mean"] = data_with_average_work_hours["mean"].map(self.__chop_microseconds)
        data_with_average_work_hours = data_with_average_work_hours.rename(
            columns={
                "start_date": "Date",
                "mean": "Mean",
                "sum": "Sum"
            }
        )
        data_with_average_work_hours.index += 1
        return data_with_average_work_hours

    @staticmethod
    def __get_week_number(date: str) -> int:
        date = datetime.datetime.strptime(date, "%b, %d %Y")
        return date.isocalendar()[1]

    @staticmethod
    def __chop_microseconds(delta: datetime.timedelta) -> datetime.timedelta:
        return datetime.timedelta(seconds=round(delta.total_seconds()))

    def boost_index(self):
        pass
