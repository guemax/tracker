import pandas

from src.handler.entry_handler.EntryHandler import EntryHandler
from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler


class SummaryHandlerInterface:
    def __init__(self) -> None:
        self._grouped_entry_handler = GroupedEntryHandler()
        self._entry_handler = EntryHandler()

        self._data = None

    def summary(self) -> pandas.DataFrame:  # pragma: no cover
        pass
