"""Validate the cookiecutter input before the project is generated."""

import keyword
import re
import sys

MODULE_REGEX = re.compile(r"[a-z_][a-z0-9_]*")
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"


def main() -> None:
    """Abort generation if the project slug is not a valid module name."""
    if not MODULE_REGEX.fullmatch(PROJECT_SLUG) or keyword.iskeyword(
        PROJECT_SLUG
    ):
        sys.exit(
            f"ERROR: {PROJECT_SLUG!r} is not a valid Python module name. "
            "Use lowercase letters, digits and underscores only."
        )


if __name__ == "__main__":
    main()
