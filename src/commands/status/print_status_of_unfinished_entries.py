from src.handler.timer_handler.TimerHandler import TimerHandler
from .print_list_item import print_list_item


def print_status_of_unfinished_entries():
    timer_handler = TimerHandler()
    unfinished_entries_present = timer_handler.unfinished_entry_present()

    if unfinished_entries_present:
        print_list_item("A timer exists which has not been stopped yet.")
    else:
        print_list_item("No unfinished timer exists.")
