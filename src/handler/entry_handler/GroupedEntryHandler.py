import pandas

from src.csv.CSVAttributes import CSVAttributes
from src.exceptions.InvalidIDOfDateException import InvalidIDOfDateException


class GroupedEntryHandler(CSVAttributes):
    def __init__(self):
        super(GroupedEntryHandler, self).__init__()

        self.data = None

    def get_entries_of_specific_date(self, id_of_date: int) -> list:
        entries_grouped_by_date = self.get_entries_grouped_by_date()
        try:
            date = entries_grouped_by_date.at[id_of_date, "Date"]
        except KeyError:
            raise InvalidIDOfDateException

        self.data = self.get_data()
        self.data = self.group_entries_by_date()

        entries_of_date_at_index: pandas.DataFrame = self.data.get_group(date)
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

    def get_entries_grouped_by_date(self) -> pandas.DataFrame:
        self.data = self.get_data()

        self.data = self.group_entries_by_date()
        self.data = self.sum_work_hours_up()
        self.data = self.rename_columns()

        self.change_index()

        self.data = self.reorder_entries_from_the_latest_down_to_the_oldest_one()

        return self.data

    def get_data(self) -> pandas.DataFrame:
        data = pandas.read_csv(self.tracker_file, header=0)

        # Change this column to a time type for allowing summing up the total work hours later
        data["work_hours"] = pandas.to_timedelta(data.work_hours)

        return data.fillna("")

    def group_entries_by_date(self) -> pandas.DataFrame:
        data_grouped_by_date = self.data.groupby("start_date", as_index=False)
        return data_grouped_by_date

    def sum_work_hours_up(self) -> pandas.DataFrame:
        data_with_sum_of_work_hours = self.data \
            .agg(
                    work_hours=pandas.NamedAgg(column="work_hours", aggfunc="sum"),
                    individual_entries=pandas.NamedAgg(column="start_date", aggfunc="size")
                )
        return data_with_sum_of_work_hours

    def rename_columns(self) -> pandas.DataFrame:
        data_with_renamed_columns = self.data \
            .rename(columns={
                                "start_date": "Date", "work_hours": "Total work time",
                                "individual_entries": "Individual entries"
                            }
                    )
        return data_with_renamed_columns

    def change_index(self) -> None:
        self.name_index_column()
        self.boost_index()

    def name_index_column(self) -> None:
        self.data.index.name = "ID"

    def boost_index(self) -> None:
        self.data.index += 1

    def reorder_entries_from_the_latest_down_to_the_oldest_one(self) -> pandas.DataFrame:
        reordered_data = self.data.iloc[::-1]
        return reordered_data
