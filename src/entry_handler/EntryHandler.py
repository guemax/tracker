import pandas

from ..csv.CSVAttributes import CSVAttributes


class EntryHandler(CSVAttributes):
    def __init__(self):
        super(EntryHandler, self).__init__()

        self.data = None
        self.data_grouped_by_day = None

    def get_entries(self) -> pandas.DataFrame:
        self.data = self.get_data()
        self.data["work_hours"] = pandas.to_timedelta(self.data.work_hours)

        data_grouped_by_day = self.data.groupby("start_date", as_index=False)
        data_grouped_by_day = data_grouped_by_day \
            .agg(
                work_hours=pandas.NamedAgg(column="work_hours", aggfunc="sum"),
                individual_entries=pandas.NamedAgg(column="start_date", aggfunc="size")
            ) \
            .rename(columns={
                                "start_date": "Date", "work_hours": "Total work time",
                                "individual_entries": "Individual entries"
                            }
                    )
        data_grouped_by_day.index.name = "ID"
        data_grouped_by_day.index += 1
        # Reorder the DataFrame to go from the latest entry down to the oldest one
        data_grouped_by_day = data_grouped_by_day.iloc[::-1]

        return data_grouped_by_day

    def get_data(self) -> pandas.DataFrame:
        data = pandas.read_csv(self.tracker_file, header=0)
        return data.fillna("")
