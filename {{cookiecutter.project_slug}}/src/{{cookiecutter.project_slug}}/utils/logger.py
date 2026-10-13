"""Logger that writes to the terminal (via rich) and to a debug log file."""

import logging

from rich.logging import RichHandler

from {{ cookiecutter.project_slug }}.utils.config import Config


def create_logger(name: str, config: Config | None = None) -> logging.Logger:
    """Create a logger with a rich terminal handler and a file handler.

    Calling this again with the same name returns the existing logger
    without adding duplicate handlers.

    Parameters
    ----------
    name
        Name of the logger.
    config
        Paths and log levels. Defaults to ``Config()``.

    Returns
    -------
    logging.Logger
        The configured logger.
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    config = config or Config()
    config.foldername_log.mkdir(parents=True, exist_ok=True)

    shell_handler = RichHandler()
    shell_handler.setLevel(config.logger_shell_level)
    shell_handler.setFormatter(logging.Formatter(config.logger_shell_fmt))

    file_handler = logging.FileHandler(
        config.filename_debug_log, encoding="utf-8"
    )
    file_handler.setLevel(config.logger_file_level)
    file_handler.setFormatter(logging.Formatter(config.logger_file_fmt))

    logger.setLevel(config.logger_level)
    logger.addHandler(shell_handler)
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger


logger = create_logger("{{ cookiecutter.project_slug }}")
