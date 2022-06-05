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
along with tracker. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from logging.handlers import RotatingFileHandler


def __setup_file_handler(formatter: logging.Formatter, level) -> RotatingFileHandler:
    file_handler = RotatingFileHandler("files/tracker.log", maxBytes=2000, backupCount=1)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    return file_handler


def __setup_console_handler(formatter: logging.Formatter, level) -> logging.StreamHandler:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    return console_handler


def setup_logging():
    logger = logging.getLogger()

    fmt = '%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt=fmt, datefmt='%d-%b-%y %H:%M:%S')

    debug = False
    if debug:
        logger.addHandler(__setup_file_handler(formatter, logging.DEBUG))
        logger.addHandler(__setup_console_handler(formatter, logging.DEBUG))

        logger.setLevel(logging.DEBUG)
    else:
        logger.addHandler(__setup_file_handler(formatter, logging.INFO))
        logger.setLevel(logging.INFO)
