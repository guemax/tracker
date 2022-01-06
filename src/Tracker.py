from .csv import CSVHandler


class Tracker:
    def __init__(self):
        self.csv_handler = CSVHandler.CSVHandler()

    def init(self):
        self.csv_handler.init_tracker_csv_file()
