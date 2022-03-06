import pandas

from .summary_handler_interface import SummaryHandlerInterface


class WeekSummaryHandler(SummaryHandlerInterface):
    def __init__(self):
        super(WeekSummaryHandler, self).__init__()

    def summary(self) -> pandas.DataFrame:
        return pandas.DataFrame()
