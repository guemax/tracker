import click

from src.console_logger.console_logger import info
from src.handler.entry_handler import EntryHandler


@click.command()
@click.option("-i", "--id", "id_of_date", help="ID of a specific day", type=int)
def log(id_of_date: int):
    """Show old entries grouped by date"""
    if id_of_date:
        entry_handler = EntryHandler.EntryHandler()
        entries_of_specific_date = entry_handler.get_entries_of_specific_date(id_of_date)

        date = entries_of_specific_date[0]
        entries_of_specific_date = entries_of_specific_date[1]

        number_of_entries = len(entries_of_specific_date)

        if number_of_entries == 0:
            info("Nothing to see yet.\n"
                 "Start creating entries by typing \"tracker start\" and finish them by typing \"tracker stop\".")
        else:
            info(f"Showing all entries of {date}. ({number_of_entries} in total).\n")
            info(f"{entries_of_specific_date}\n")
    else:
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
