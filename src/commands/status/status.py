import num2words
import click

from src.console_logger.console_logger import info
from src.handler.timer_handler.TimerHandler import TimerHandler
from src.handler.entry_handler.GroupedEntryHandler import GroupedEntryHandler


@click.command()
def status():   # pragma: no cover
    """Provide information about the current tracking process"""
    # TODO: Add real information
    timer_handler = TimerHandler()
    entry_handler = GroupedEntryHandler()

    unfinished_entries_present = timer_handler.unfinished_entry_present()
    number_of_entries = len(entry_handler.get_data())
    number_of_grouped_entries = len(entry_handler.get_entries_grouped_by_date())

    info("Status information from Tracker:\n")

    if unfinished_entries_present:
        info(" - A timer exists which has not been stopped yet.")
    else:
        info(" - No unfinished timer exists.")

    word_number_of_entries = num2words.num2words(number_of_entries).title()
    word_number_of_grouped_entries = num2words.num2words(number_of_grouped_entries).title()

    if number_of_entries == 0:
        info(f" - {word_number_of_entries} ({number_of_entries}) entries found. "
             f"Create one by typing \"tracker start\".")
    elif number_of_entries == 1:
        info(f" - {word_number_of_entries} ({number_of_entries}) entry found.")
    else:
        info(f" - {word_number_of_entries} ({number_of_entries}) entries found.")

    if number_of_grouped_entries == 0:
        info(f" - {word_number_of_grouped_entries} ({number_of_grouped_entries}) grouped entries found.")
    elif number_of_grouped_entries == 1:
        info(f" - {word_number_of_grouped_entries} ({number_of_grouped_entries}) grouped entry found.")
    else:
        info(f" - {word_number_of_grouped_entries} ({number_of_grouped_entries}) grouped entries found.")

    info("\nOK")
