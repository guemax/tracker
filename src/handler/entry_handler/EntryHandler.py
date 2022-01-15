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

        self.entries = self.rename_columns()
        self.merge_date_and_time_columns()

        self.remove_start_and_stop_date_and_start_and_stop_time_columns()
        self.reorder_columns()

        # Make pandas print a message over more than one line in the console
        pandas.set_option("display.max_colwidth", None)

        return [date, self.entries]

    def rename_columns(self) -> pandas.DataFrame:
        entries_with_renamed_columns = self.entries \
            .rename(columns={
                                "start_date": "Start Date", "start_time": "Start Time",
                                "stop_date": "Stop Date", "stop_time": "Stop Time",
                                "work_hours": "Work hours", "message": "Message"
                            }
                    )
        return entries_with_renamed_columns

    def remove_start_and_stop_date_and_start_and_stop_time_columns(self) -> None:
        self.entries = self.entries.drop(columns=["Start Date", "Start Time", "Stop Date", "Stop Time"])

    def reorder_columns(self) -> None:
        self.entries = self.entries[["Start", "Stop", "Work hours", "Message"]]

    def merge_date_and_time_columns(self) -> None:
        self.merge_start_date_and_start_time()
        self.merge_stop_date_and_stop_time()

    def merge_start_date_and_start_time(self) -> None:
        self.entries["Start"] = self.entries[["Start Date", "Start Time"]].apply(lambda x: " at ".join(x), axis=1)

    def merge_stop_date_and_stop_time(self) -> None:
        self.entries["Stop"] = self.entries[["Stop Date", "Stop Time"]].apply(lambda x: " at ".join(x), axis=1)

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
