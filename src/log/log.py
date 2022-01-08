import click

from ..entry_handler import EntryHandler


@click.command()
def log():
    """Show old entries grouped by date"""
    entry_handler = EntryHandler.EntryHandler()
    entries = entry_handler.get_entries()

    print(entries)
