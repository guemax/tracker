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

from .status_of_entries import status_of_entries
from .status_of_grouped_entries import status_of_grouped_entries
from .status_of_unfinished_entries import status_of_unfinished_entries

from tracker.commands.console_logger import info


@click.command()
def status() -> None:
    """Provide information about the current tracking process"""
    info(f"Status information from Tracker:\n\n"
         f" - {status_of_unfinished_entries()}\n"
         f" - {status_of_entries()}\n"
         f" - {status_of_grouped_entries()}\n"
         f"\nOK")
