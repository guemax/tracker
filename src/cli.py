"""This file is part of Tracker.

Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Tracker. If not, see <http://www.gnu.org/licenses/>.
"""

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
