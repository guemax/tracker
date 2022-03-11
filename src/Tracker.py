from .csv import CSVHandler


class Tracker:
    def __init__(self):     # pragma: no cover
        self.csv_handler = CSVHandler.CSVHandler()

    def init_tracker_file(self):     # pragma: no cover
        self.csv_handler.init_tracker_csv_file()
