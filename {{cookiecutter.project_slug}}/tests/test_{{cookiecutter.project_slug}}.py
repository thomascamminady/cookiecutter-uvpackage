"""Tests for `{{ cookiecutter.project_slug }}` package."""


from {{ cookiecutter.project_slug }} import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"
