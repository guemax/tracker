import click

from .print_status_of_unfinished_entries import print_status_of_unfinished_entries
from .print_status_of_grouped_entries import print_status_of_grouped_entries
from .print_status_of_entries import print_status_of_entries

from src.console_logger.console_logger import info


@click.command()
def status():   # pragma: no cover
    """Provide information about the current tracking process"""
    # TODO: Add real information
    timer_handler = TimerHandler()
    entry_handler = GroupedEntryHandler()

    unfinished_entries_present = timer_handler.unfinished_entry_present()
    number_of_entries = len(entry_handler.get_data())
    number_of_grouped_entries = len(
        entry_handler.get_entries_grouped_by_date())

    info("Status information from Tracker:\n")

    print_status_of_unfinished_entries()
    print_status_of_entries()
    print_status_of_grouped_entries()

    info("\nOK")
