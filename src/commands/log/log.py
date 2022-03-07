import click

from src.console_logger.console_logger import info
from src.handler.entry_handler import EntryHandler


@click.command()
def log():
    """Show old entries grouped by date"""
    entry_handler = EntryHandler.EntryHandler()
    entries_grouped_by_date = entry_handler.get_entries_grouped_by_date()
    number_of_grouped_entries = len(entries_grouped_by_date)

    if number_of_grouped_entries == 0:
        info("Nothing to see yet.\n"
             "Start creating entries by typing \"tracker start\" and finish them by typing \"tracker stop\".")
    else:
        info(f"Showing all entries grouped by date. ({number_of_grouped_entries} in total).\n"
             f"Use \"tracker log <ID>\" to show all entries of the date with the ID <ID>.\n")
        info(f"{entries_grouped_by_date}\n")
