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
