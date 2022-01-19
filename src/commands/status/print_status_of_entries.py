from num2words import num2words

from src.handler.entry_handler.EntryHandler import EntryHandler
from src.console_logger.console_logger import info


def print_status_of_entries():
    entry_handler = EntryHandler()
    number_of_entries = len(entry_handler.get_data())

    word_number_of_entries = num2words(number_of_entries).title()

    if number_of_entries == 0:
        info(f" - {word_number_of_entries} ({number_of_entries}) entries found. "
             f"Create one by typing \"tracker start\".")
    elif number_of_entries == 1:
        info(f" - {word_number_of_entries} ({number_of_entries}) entry found.")
    else:
        info(f" - {word_number_of_entries} ({number_of_entries}) entries found.")
