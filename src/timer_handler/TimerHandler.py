from datetime import datetime

import pandas

from src.csv.CSVAttributes import CSVAttributes
from src.exceptions.InvalidTimerModification import InvalidTimerModification


class TimerHandler(CSVAttributes):
    def __init__(self) -> None:
        super(TimerHandler, self).__init__()

    def start_timer(self) -> list:
        if self.unfinished_entry_present():
            raise InvalidTimerModification()

        start_date = datetime.now().strftime("%b, %d %Y")
        start_time = datetime.now().strftime("%H:%M:%S")

        with open(self.tracker_file, "a") as f:
            row = {
                "start_date": start_date, "start_time": start_time, "stop_date": None, "stop_time": None,
                "message": None
                }
            data = pandas.DataFrame(row, index=[0])
            data.to_csv(f, header=False, index=False)

        return [start_date, start_time]

    def stop_timer(self, message: str) -> list:
        if not self.unfinished_entry_present():
            raise InvalidTimerModification()

        stop_date = datetime.now().strftime("%b, %d %Y")
        stop_time = datetime.now().strftime("%H:%M:%S")

        data = pandas.read_csv(self.tracker_file, dtype=str)

        index = len(data) - 1
        data.at[index, "stop_date"] = stop_date
        data.at[index, "stop_time"] = stop_time
        data.at[index, "message"] = message

        data.to_csv(self.tracker_file, index=False)

        return [stop_date, stop_time]

    def unfinished_entry_present(self) -> bool:
        data = pandas.read_csv(self.tracker_file, dtype=str)
        data = data.fillna("")

        if len(data) == 0:
            return False

        index = len(data) - 1

        if data.at[index, "start_time"] != "" and data.at[index, "stop_time"] == "":
            return True

        return False
