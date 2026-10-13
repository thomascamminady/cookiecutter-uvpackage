"""Tests that bake the template and check the generated project."""

import json
import os
import re
import subprocess
import tomllib
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

TEMPLATE_DIR = Path(__file__).resolve().parent.parent
UNRENDERED = re.compile(r"\{\{\s*cookiecutter\.|\{%")


def load_choices(variable: str) -> list[str]:
    """Return the choices of a choice variable in cookiecutter.json."""
    context: object = json.loads(
        (TEMPLATE_DIR / "cookiecutter.json").read_text()
    )
    assert isinstance(context, dict)
    return [str(choice) for choice in context[variable]]


PYTHON_VERSIONS = load_choices("python_version")
LICENSES = load_choices("open_source_license")


def bake(output_dir: Path, **extra_context: str) -> Path:
    """Generate a project without prompts and return its path."""
    project = cookiecutter(
        str(TEMPLATE_DIR),
        no_input=True,
        extra_context={"project_name": "Test Project", **extra_context},
        output_dir=str(output_dir),
    )
    return Path(project)


def run(command: list[str], cwd: Path) -> None:
    """Run a command in `cwd` and fail the test with its output on error."""
    # Don't leak this repository's virtual environment into the baked project.
    env = {k: v for k, v in os.environ.items() if k != "VIRTUAL_ENV"}
    result = subprocess.run(
        command, cwd=cwd, env=env, capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, (
        f"{' '.join(command)} failed:\n{result.stdout}\n{result.stderr}"
    )


def test_bake_with_defaults(tmp_path: Path) -> None:
    project = bake(tmp_path)
    assert project.name == "test_project"
    for path in [
        "pyproject.toml",
        "Makefile",
        "LICENSE",
        "src/test_project/__init__.py",
        "src/test_project/py.typed",
        "tests/test_smoke.py",
        "scripts/hello_world.py",
    ]:
        assert (project / path).is_file(), path
    assert os.access(project / "scripts/hello_world.py", os.X_OK)


def test_all_jinja_is_rendered(tmp_path: Path) -> None:
    project = bake(tmp_path)
    for path in project.rglob("*"):
        if path.is_file():
            assert not UNRENDERED.search(path.read_text()), path


@pytest.mark.parametrize("python_version", PYTHON_VERSIONS)
def test_python_version(tmp_path: Path, python_version: str) -> None:
    project = bake(tmp_path, python_version=python_version)
    assert (project / ".python-version").read_text().strip() == python_version
    pyproject = (project / "pyproject.toml").read_text()
    assert f'requires-python = ">={python_version}"' in pyproject


@pytest.mark.parametrize("license_name", LICENSES)
def test_license(tmp_path: Path, license_name: str) -> None:
    project = bake(tmp_path, open_source_license=license_name)
    license_file = project / "LICENSE"
    pyproject = (project / "pyproject.toml").read_text()
    tomllib.loads(pyproject)
    if license_name == "Not open source":
        assert not license_file.exists()
        assert "license =" not in pyproject
        assert "Private :: Do Not Upload" in pyproject
    else:
        text = license_file.read_text()
        assert text.strip()
        assert not text.startswith("\n")
        assert text.endswith("\n")
        assert not text.endswith("\n\n")
        assert "license-files" in pyproject


@pytest.mark.parametrize("slug", ["my-project", "MyProject", "class", "1abc"])
def test_invalid_slug_is_rejected(tmp_path: Path, slug: str) -> None:
    with pytest.raises(FailedHookException):
        bake(tmp_path, project_slug=slug)


@pytest.mark.integration
@pytest.mark.parametrize("python_version", PYTHON_VERSIONS)
def test_baked_project_passes_checks(
    tmp_path: Path, python_version: str
) -> None:
    project = bake(tmp_path, python_version=python_version)
    run(["uv", "sync", "--all-extras", "--all-groups"], project)
    run(["uv", "run", "ruff", "check"], project)
    run(["uv", "run", "ruff", "format", "--check"], project)
    run(["uv", "run", "ty", "check"], project)
    run(["uv", "run", "pytest"], project)
    run(["uv", "build"], project)
