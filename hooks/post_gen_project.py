"""Finalize the generated project and print the next steps."""

from pathlib import Path

OPEN_SOURCE_LICENSE = "{{ cookiecutter.open_source_license }}"
GITHUB_USERNAME = "{{ cookiecutter.github_username }}"
GITHUB_REPONAME = "{{ cookiecutter.github_reponame }}"


def main() -> None:
    """Remove the empty license file of closed-source projects."""
    if OPEN_SOURCE_LICENSE == "Not open source":
        Path("LICENSE").unlink()

    print(f"""
✨ Project created!

Next steps:
1. Create the GitHub repository {GITHUB_USERNAME}/{GITHUB_REPONAME}.
2. Settings -> Pages -> Build and deployment -> Source: GitHub Actions.
3. cd into the project and run: make
""")


if __name__ == "__main__":
    main()
