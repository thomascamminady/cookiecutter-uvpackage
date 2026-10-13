import importlib
from pathlib import Path

import pytest

from {{ cookiecutter.project_slug }}.utils.config import Config
from {{ cookiecutter.project_slug }}.utils.logger import create_logger


def test_package_imports() -> None:
    module = importlib.import_module("{{ cookiecutter.project_slug }}")
    assert module.__name__ == "{{ cookiecutter.project_slug }}"


def test_logger_writes_debug_log(tmp_path: Path) -> None:
    config = Config(foldername_log=tmp_path / "logs")
    assert config.filename_debug_log == Path(tmp_path, "logs", "debug.log")
    logger = create_logger("test_logger", config)
    try:
        logger.debug("hello")
        assert "hello" in config.filename_debug_log.read_text()
        assert create_logger("test_logger", config) is logger
    finally:
        for handler in logger.handlers:
            handler.close()


def test_altair_theme_is_applied() -> None:
    alt = pytest.importorskip("altair")
    from {{ cookiecutter.project_slug }}.utils.altairconfig import AltairConfig  # noqa: PLC0415

    AltairConfig(where="html", width=300).setup()
    chart = (
        alt.Chart(alt.Data(values=[{"a": 1, "b": 2}]))
        .mark_point()
        .encode(x="a:Q", y="b:Q")
    )
    spec = chart.to_dict(validate=True)
    assert spec["config"]["view"]["continuousWidth"] == 300
