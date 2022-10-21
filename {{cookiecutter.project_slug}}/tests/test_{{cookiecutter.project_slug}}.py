"""Tests for `{{ cookiecutter.project_slug }}` package."""


from {{ cookiecutter.project_slug }} import __version__
from {{ cookiecutter.project_slug }}.add1 import add1


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_add1() -> None:
    assert add1(2) == 3
