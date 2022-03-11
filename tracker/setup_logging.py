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

import logging
import sys


def setup_logging(debug: bool = False):
    logging.basicConfig(
        level=logging.INFO,
        filename="tracker/files/tracker.log",
        filemode="w",
        format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
    )
    set_debug(debug)


def set_debug(debug: bool = False):
    if debug:
        enable_logging_in_console()


def enable_logging_in_console():    # pragma: no cover
    logger = logging.getLogger()
    stream_handler = logging.StreamHandler(sys.stdout)

    logger.addHandler(stream_handler)
