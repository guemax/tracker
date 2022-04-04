"""This file is part of tracker.
Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import click


class ConsoleLogger:
    def __init__(self, level: str):
        self.levels = {"DEBUG": "white", "INFO": "white", "WARNING": "yellow", "ERROR": "red", "FATAL": "red"}
        self.level_color = self.levels[level]

    def print(self, message: str, error: bool = False):
        if error:
            click.echo(click.style(message, fg=self.level_color), err=True)
        else:
            click.echo(click.style(message, fg=self.level_color))
