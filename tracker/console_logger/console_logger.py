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

from .ConsoleLogger import ConsoleLogger


def debug(message: str):
    logger = ConsoleLogger("DEBUG")
    logger.print(message)


def info(message: str):
    logger = ConsoleLogger("INFO")
    logger.print(message)


def warn(message: str):
    logger = ConsoleLogger("WARNING")
    logger.print(message, error=True)


def error(message: str):
    logger = ConsoleLogger("ERROR")
    logger.print(message, error=True)


def fatal(message: str):
    logger = ConsoleLogger("FATAL")
    logger.print(message, error=True)