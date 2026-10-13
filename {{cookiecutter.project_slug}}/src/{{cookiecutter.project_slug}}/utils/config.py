"""Project-wide configuration."""

import logging
from dataclasses import dataclass
from pathlib import Path

# src/<package>/utils/config.py -> project root (assumes an editable install,
# which is what `uv sync` does by default).
PROJECT_ROOT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True, slots=True, kw_only=True)
class Config:
    """Paths and logging settings."""

    foldername_root: Path = PROJECT_ROOT
    foldername_log: Path = PROJECT_ROOT / "logs"

    logger_level: int = logging.DEBUG
    logger_shell_level: int = logging.DEBUG
    logger_file_level: int = logging.DEBUG

    logger_shell_fmt: str = "%(message)s"
    logger_file_fmt: str = "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"

    @property
    def filename_debug_log(self) -> Path:
        """Path of the debug log file."""
        return self.foldername_log / "debug.log"
