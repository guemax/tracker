import click

from src.commands.summary import summary
from src.commands.status import status
from src.commands.start import start
from src.commands.stop import stop
from src.commands.log import log


@click.group(help="A command-line tool to track your computer usage time.")
def cli():
    pass


def add_subcommands_to_cli():
    cli.add_command(summary.summary)
    cli.add_command(status.status)
    cli.add_command(start.start)
    cli.add_command(stop.stop)
    cli.add_command(log.log)


# Called when importing this file
add_subcommands_to_cli()
