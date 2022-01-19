from src.handler.timer_handler.TimerHandler import TimerHandler
from src.console_logger.console_logger import info


def print_status_of_unfinished_entries():
    timer_handler = TimerHandler()
    unfinished_entries_present = timer_handler.unfinished_entry_present()

    if unfinished_entries_present:
        info(" - A timer exists which has not been stopped yet.")
    else:
        info(" - No unfinished timer exists.")
