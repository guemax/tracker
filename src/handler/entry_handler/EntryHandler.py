import pandas

from src.exceptions.InvalidIDOfDateException import InvalidIDOfDateException
from src.handler.entry_handler.BaseEntryHandlerClass import BaseEntryHandlerClass
from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler


class EntryHandler(BaseEntryHandlerClass):
    def __init__(self):
        super(EntryHandler, self).__init__()

        self.entries = None
        self.grouped_entry_handler = GroupedEntryHandler()

    def get_entries_of_specific_date(self, id_of_date: int) -> list:
        try:
            date = self.get_string_of_date_by_id(id_of_date)
        except KeyError:
            raise InvalidIDOfDateException

        self.data = self.get_data()
        self.data = self.group_entries_by_date()

        self.entries = self.data.get_group(date)

        self.change_index()
        self.merge_date_and_time_columns()

        self.remove_start_and_stop_date_and_start_and_stop_time_columns()
        self.reorder_columns()

        self.entries = self.rename_columns()

        # Make pandas print a message over more than one line in the console
        pandas.set_option("display.max_colwidth", None)

        return [date, self.entries]

    def get_string_of_date_by_id(self, id_of_date: int) -> str:
        entries_grouped_by_date = self.grouped_entry_handler.get_entries_grouped_by_date()

        date = entries_grouped_by_date.at[id_of_date, "Date"]
        return date

    def change_index(self) -> None:
        self.reset_index()
        self.boost_index()

    def reset_index(self) -> None:
        self.entries.reset_index()

    def boost_index(self) -> None:
        self.entries.index += 1

    def rename_columns(self) -> pandas.DataFrame:
        entries_with_renamed_columns = self.entries \
            .rename(columns={
                                "start": "Start",
                                "stop": "Stop",
                                "work_hours": "Work hours", "message": "Message"
                            }
                    )
        return entries_with_renamed_columns

    def merge_date_and_time_columns(self) -> None:
        # Below is just work around for pandas' error: pandas.core.common.SettingWithCopyError
        pandas.set_option("mode.chained_assignment", None)

        self.merge_start_date_and_start_time()
        self.merge_stop_date_and_stop_time()

        pandas.set_option("mode.chained_assignment", "warn")

    def merge_start_date_and_start_time(self) -> None:
        self.entries.loc[:, "start"] = self.entries["start_date"] + " at " + self.entries["start_time"]

    def merge_stop_date_and_stop_time(self) -> None:
        self.entries.loc[:, "stop"] = self.entries["stop_date"] + " at " + self.entries["stop_time"]

    def remove_start_and_stop_date_and_start_and_stop_time_columns(self) -> None:
        self.entries = self.entries.drop(columns=["start_date", "start_time", "stop_date", "stop_time"])

    def reorder_columns(self) -> None:
        self.entries = self.entries[["start", "stop", "work_hours", "message"]]
