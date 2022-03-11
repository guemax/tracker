from .Tracker import Tracker
from .cli import cli

from .setup_logging import setup_logging, set_debug


if __name__ == "__main__":  # pragma: no cover
    setup_logging()
    set_debug(False)

    # Set up tracker
    tracker = Tracker()
    tracker.init()

    # Start click
    cli()
