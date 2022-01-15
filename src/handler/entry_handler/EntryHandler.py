import pandas

from src.csv.CSVAttributes import CSVAttributes
from src.exceptions.InvalidIDOfDateException import InvalidIDOfDateException
from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler


class EntryHandler(CSVAttributes):
    def __init__(self):
        super(EntryHandler, self).__init__()

        self.data = None
        self.grouped_entry_handler = GroupedEntryHandler()

    def get_entries_of_specific_date(self, id_of_date: int) -> list:
        entries_grouped_by_date = self.grouped_entry_handler.get_entries_grouped_by_date()
        try:
            date = entries_grouped_by_date.at[id_of_date, "Date"]
        except KeyError:
            raise InvalidIDOfDateException

        self.grouped_entry_handler.data = self.grouped_entry_handler.get_data()
        self.grouped_entry_handler.data = self.grouped_entry_handler.group_entries_by_date()

        entries_of_date_at_index: pandas.DataFrame = self.grouped_entry_handler.data.get_group(date)
        entries_of_date_at_index.reset_index()
        entries_of_date_at_index.index += 1

        entries_of_date_at_index = entries_of_date_at_index \
            .rename(columns={
                                "start_date": "Start Date", "start_time": "Start Time",
                                "stop_date": "Stop Date", "stop_time": "Stop Time",
                                "work_hours": "Work hours", "message": "Message"
                            }
                    )
        entries_of_date_at_index["Start"] = entries_of_date_at_index[["Start Date", "Start Time"]].apply(lambda x: " at ".join(x), axis=1)
        entries_of_date_at_index["Stop"] = entries_of_date_at_index[["Stop Date", "Stop Time"]].apply(lambda x: " at ".join(x), axis=1)

        entries_of_date_at_index = entries_of_date_at_index.drop(columns=["Start Date", "Start Time", "Stop Date", "Stop Time"])
        entries_of_date_at_index = entries_of_date_at_index[["Start", "Stop", "Work hours", "Message"]]

        pandas.set_option("display.max_colwidth", None)

        return [date, entries_of_date_at_index]
