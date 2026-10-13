#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">={{ cookiecutter.python_version }}"
# dependencies = [
#     "fire>=0.7.1",
# ]
# ///
"""Example of a self-contained script with inline dependencies.

Run it with `uv run scripts/hello_world.py --name=you` or, since it is
executable, `./scripts/hello_world.py --name=you`.
"""

import fire


def main(name: str = "World") -> None:
    """Greet someone.

    Parameters
    ----------
    name
        Who to greet.
    """
    print(f"Hello, {name}!")


if __name__ == "__main__":
    fire.Fire(main)
