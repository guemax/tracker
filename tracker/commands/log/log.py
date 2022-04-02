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

from .log_all_entries_grouped_by_date import log_all_entries_grouped_by_date
from .log_entries_of_specific_date import log_entries_of_specific_date


@click.command()
@click.option("-i", "--id", "id_of_date", help="ID of a specific date", type=int, default=None)
def log(id_of_date: int):
    """Show old entries grouped by date or, when an ID is supplied, show entries of specific date"""
    if id_of_date is None:
        log_all_entries_grouped_by_date()
    else:
        log_entries_of_specific_date(id_of_date)
