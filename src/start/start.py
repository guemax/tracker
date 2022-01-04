import click

from ..csv_handler import CSVHandler


@click.command()
def start():
    """Start a new timer"""
    csv_handler = CSVHandler.CSVHandler()
    time = csv_handler.create_new_entry()

    print(f"New timer started at {time}")
    print("OK")
