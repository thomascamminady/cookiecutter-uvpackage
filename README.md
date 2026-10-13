# cookiecutter-uvpackage

An opinionated [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for strictly typed Python packages managed with
[uv](https://docs.astral.sh/uv/).

## Features

- **uv everywhere**: dependencies, lockfile, Python installs, builds
  (`uv_build`), and standalone scripts with inline dependencies.
- **Strict by default**: [Ruff](https://docs.astral.sh/ruff/) with all rules
  enabled and [ty](https://docs.astral.sh/ty/) with all rules as errors.
- **One set of tool versions**: pre-commit, CI and your editor all run Ruff,
  ty and pytest from `uv.lock`.
- **CI/CD**: GitHub Actions for lint, type check and tests, plus pdoc
  documentation deployed to GitHub Pages. Actions are pinned to commit SHAs.
- **Automated updates**: Dependabot for Python packages, GitHub Actions and
  pre-commit hooks, with a 7-day cooldown.
- **Batteries**: rich logging, an Altair theme, and a
  [Fire](https://github.com/google/python-fire) script example.

## Quick start

```bash
uvx cookiecutter gh:thomascamminady/cookiecutter-uvpackage
cd my_project
make
```

`make` installs Python and all dependencies, initializes git with the
pre-commit hooks, makes the first commit, opens VS Code, and pushes to
`github.com/<github_username>/<github_reponame>` (create that repository
first). For the documentation, set Settings → Pages → Source to GitHub Actions.

## Template options

| Option                      | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| `full_name`, `email`        | Author                                                    |
| `github_username`           | GitHub user or organization                               |
| `project_name`              | Human-readable name                                       |
| `project_slug`              | Package name (derived; lowercase letters, digits, `_`)    |
| `github_reponame`           | Repository name (defaults to `project_slug`)              |
| `project_short_description` | One-line description                                      |
| `version`                   | Initial version (default `0.1.0`)                         |
| `python_version`            | Minimum Python version: 3.14 (default), 3.13, 3.12, 3.11  |
| `open_source_license`       | MIT, BSD-3-Clause, ISC, Apache-2.0, GPL-3.0, or closed    |

## Generated project

```text
my_project/
├── .github/
│   ├── dependabot.yml         # uv, GitHub Actions and pre-commit updates
│   └── workflows/
│       ├── ci.yml             # ruff, ty, pytest
│       └── docs.yml           # pdoc -> GitHub Pages
├── .vscode/                   # Ruff + ty editor setup
├── data/                      # Local data (git-ignored)
├── ideation/                  # Scratch notebook and drawing board (git-ignored)
├── scripts/
│   └── hello_world.py         # Standalone uv script using Fire
├── src/my_project/
│   ├── py.typed
│   └── utils/
│       ├── altairconfig.py    # Altair theme (`viz` extra)
│       ├── config.py
│       └── logger.py          # rich + file logging
├── tests/
├── .pre-commit-config.yaml
├── Makefile                   # make check / format / coverage / docs / help
├── pyproject.toml
├── ruff.toml
└── ty.toml
```

## Developing the template

```bash
uv sync
uv run pre-commit install
uv run pytest                      # all tests, including the slow ones
uv run pytest -m "not integration" # fast tests only
```

The integration tests bake a project for every supported Python version and
run `uv sync`, Ruff, ty, pytest and `uv build` in it. CI additionally
bootstraps a baked project with `make` and runs its pre-commit hooks.

## Credits

Originally based on
[audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
BSD licensed.
