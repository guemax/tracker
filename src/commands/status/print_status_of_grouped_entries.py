from num2words import num2words

from src.handler.entry_handler.EntryHandler import EntryHandler
from src.console_logger.console_logger import info


def print_status_of_grouped_entries():
    entry_handler = EntryHandler()
    number_of_grouped_entries = len(entry_handler.get_entries_grouped_by_date())

    word_number_of_grouped_entries = num2words(number_of_grouped_entries).title()

    if number_of_grouped_entries == 0:
        info(f" - {word_number_of_grouped_entries} ({number_of_grouped_entries}) grouped entries found.")
    elif number_of_grouped_entries == 1:
        info(f" - {word_number_of_grouped_entries} ({number_of_grouped_entries}) grouped entry found.")
    else:
        info(f" - {word_number_of_grouped_entries} ({number_of_grouped_entries}) grouped entries found.")
