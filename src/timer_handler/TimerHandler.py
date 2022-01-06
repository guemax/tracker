from datetime import datetime

import pandas

from src.csv.CSVAttributes import CSVAttributes
from src.exceptions.InvalidTimerModification import InvalidTimerModification


class TimerHandler(CSVAttributes):
    def __init__(self) -> None:
        super(TimerHandler, self).__init__()

    def start_timer(self) -> str:
        if self.unfinished_entry_present():
            raise InvalidTimerModification()

        current_time = datetime.now().strftime("%b, %d %Y at %H:%M:%S")

        with open(self.tracker_file, "a") as f:
            data = pandas.DataFrame({"start_time": current_time, "stop_time": None, "message": None}, index=[0])
            data.to_csv(f, header=False, index=False)

        return current_time

    def stop_timer(self, message: str) -> str:
        if not self.unfinished_entry_present():
            raise InvalidTimerModification()

        stop_time = datetime.now().strftime("%b, %d %Y at %H:%M:%S")

        data = pandas.read_csv(self.tracker_file, dtype=str)

        index = len(data) - 1
        data.at[index, "stop_time"] = stop_time
        data.at[index, "message"] = message

        data.to_csv(self.tracker_file, index=False)

        return stop_time

    def unfinished_entry_present(self) -> bool:
        data = pandas.read_csv(self.tracker_file, dtype=str)
        data = data.fillna("")

        if len(data) == 0:
            return False

        index = len(data) - 1

        if data.at[index, "start_time"] != "" and data.at[index, "stop_time"] == "":
            return True

        return False
