import pandas

from src.handler.entry_handler.EntryHandler import EntryHandler
from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler


class SummaryHandlerInterface:
    def __init__(self) -> None:
        self._grouped_entry_handler = GroupedEntryHandler()
        self._entry_handler = EntryHandler()

    def summary(self) -> pandas.DataFrame:
        pass

    # def summary(self) -> pandas.DataFrame:
    #     entries = self.__entry_handler.get_data()
    #
    #     entries_grouped_by_date = entries.groupby("start_date", as_index=False)
    #
    #     data_with_average_work_hours = entries_grouped_by_date \
    #         .agg(
    #                 mean=pandas.NamedAgg(column="work_hours", aggfunc="mean"),
    #                 sum=pandas.NamedAgg(column="work_hours", aggfunc="sum")
    #             )
    #
    #     data_with_average_work_hours["mean"] = data_with_average_work_hours["mean"].map(self.__chop_microseconds)
    #     data_with_average_work_hours = data_with_average_work_hours.rename(
    #         columns={
    #             "start_date": "Date",
    #             "mean": "Mean",
    #             "sum": "Sum"
    #         }
    #     )
    #     data_with_average_work_hours.index += 1
    #     return data_with_average_work_hours
    #
    # @staticmethod
    # def __chop_microseconds(delta: datetime.timedelta) -> datetime.timedelta:
    #     return datetime.timedelta(seconds=round(delta.total_seconds()))
    #
    # def boost_index(self):
    #     pass
