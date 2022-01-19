import pandas

from src.csv.CSVAttributes import CSVAttributes


class BaseEntryHandlerClass(CSVAttributes):
    def __init__(self):
        super(BaseEntryHandlerClass, self).__init__()

        self.data = None

    def get_data(self) -> pandas.DataFrame:
        data = pandas.read_csv(self.tracker_file, header=0)

        # Change this column to a time type for allowing summing up the total work hours later
        data["work_hours"] = pandas.to_timedelta(data.work_hours)

        return data.fillna("")

    def group_entries_by_date(self) -> pandas.DataFrame:
        data_grouped_by_date = self.data.groupby("start_date", as_index=False)
        return data_grouped_by_date
