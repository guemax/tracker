import pandas

from src.exceptions.InvalidIDOfDateException import InvalidIDOfDateException
from src.handler.entry_handler.BaseEntryHandlerClass import BaseEntryHandlerClass
from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler


class EntryHandler(BaseEntryHandlerClass):
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

        self.data = self.get_data()
        self.data = self.group_entries_by_date()

        self.data: pandas.DataFrame = self.data.get_group(date)
        self.data.reset_index()
        self.boost_index()

        self.data = self.data \
            .rename(columns={
                                "start_date": "Start Date", "start_time": "Start Time",
                                "stop_date": "Stop Date", "stop_time": "Stop Time",
                                "work_hours": "Work hours", "message": "Message"
                            }
                    )
        self.data["Start"] = self.data[["Start Date", "Start Time"]].apply(lambda x: " at ".join(x), axis=1)
        self.data["Stop"] = self.data[["Stop Date", "Stop Time"]].apply(lambda x: " at ".join(x), axis=1)

        self.data = self.data.drop(columns=["Start Date", "Start Time", "Stop Date", "Stop Time"])
        self.data = self.data[["Start", "Stop", "Work hours", "Message"]]

        pandas.set_option("display.max_colwidth", None)

        return [date, self.data]
