import click

from ..entry_handler import EntryHandler


@click.command()
def log():
    """Show old entries grouped by date"""
    entry_handler = EntryHandler.EntryHandler()
    entries_grouped_by_date = entry_handler.get_entries()
    number_of_grouped_entries = len(entries_grouped_by_date)

    if number_of_grouped_entries == 0:
        print("Nothing to see yet.\n"
              "Start creating entries by typing 'tracker start' and finish them by typing 'tracker stop'.")
    else:
        print(f"Showing all entries grouped by date. ({number_of_grouped_entries} in total).\n"
              f"Use 'tracker log <ID>' to show all entries of the date with the ID <ID>.\n")
        print(f"{entries_grouped_by_date}\n")
