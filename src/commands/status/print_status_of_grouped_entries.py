from num2words import num2words

from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler
from .print_list_item import print_list_item


def print_status_of_grouped_entries():
    grouped_entry_handler = GroupedEntryHandler()

    number_of_grouped_entries = len(grouped_entry_handler.get_entries_grouped_by_date())
    number_of_grouped_entries_as_word = num2words(number_of_grouped_entries).title()

    if number_of_grouped_entries == 0:
        print_list_item(f"{number_of_grouped_entries_as_word} ({number_of_grouped_entries}) grouped entries found.")
    elif number_of_grouped_entries == 1:
        print_list_item(f"{number_of_grouped_entries_as_word} ({number_of_grouped_entries}) grouped entry found.")
    else:
        print_list_item(f"{number_of_grouped_entries_as_word} ({number_of_grouped_entries}) grouped entries found.")
