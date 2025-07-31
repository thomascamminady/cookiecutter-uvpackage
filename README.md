# Cookiecutter UV Package Template

A modern, opinionated Cookiecutter template for Python packages using UV for dependency management.

## Features

-   **UV-first**: Uses `uv` for dependency management, packaging, and tool execution
-   **Modern Python**: Supports Python 3.9+ with configurable Python version selection
-   **Quality Assurance**: Pre-commit hooks with Ruff, MyPy, Pytest, and more
-   **Documentation**: Automated documentation generation with pdoc and GitHub Pages
-   **CI/CD**: GitHub Actions for testing, documentation, and dependency updates
-   **Developer Experience**: Single `make` command setup, rich logging, and comprehensive tooling

## Quick Start

Install the latest Cookiecutter:

```bash
pip install -U cookiecutter
# or
uv tool install cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/thomascamminady/cookiecutter-uvpackage
```

Create a remote repository with the specified name and enable GitHub Actions as the deployment method for GitHub Pages.

Change into the new project folder and run:

```bash
make
```

## Template Options

-   `full_name`: Your full name
-   `email`: Your email address
-   `github_username`: Your GitHub username
-   `project_name`: The name of your project
-   `project_slug`: Python package name (auto-generated)
-   `github_reponame`: GitHub repository name (auto-generated)
-   `project_short_description`: Brief description of your project
-   `version`: Initial version (default: 0.1.0)
-   `python_version`: Python version to use (3.9, 3.10, 3.11, 3.12, 3.13 - default: 3.11)
-   `open_source_license`: Choose from MIT, BSD, ISC, Apache, GPL, or proprietary

## Generated Project Structure

```
my_project/
├── .github/
│   ├── workflows/
│   │   ├── run-tests.yml      # CI/CD pipeline
│   │   └── docs.yml           # Documentation deployment
│   └── dependabot.yml         # Automated dependency updates
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── py.typed            # Type hints support
│       └── utils/
│           ├── config.py       # Configuration management
│           └── logger.py       # Rich logging setup
├── tests/
│   └── test_true.py           # Basic test setup
├── scripts/
│   └── hello_world.py         # Example UV script
├── data/                      # Data files
├── ideation/
│   ├── drawingboard.excalidraw
│   └── main.ipynb            # Jupyter notebook for exploration
├── pyproject.toml            # Project configuration
├── uv.lock                   # Dependency lock file
├── .pre-commit-config.yaml   # Code quality hooks
├── Makefile                  # Development automation
└── README.md
```

## Development Workflow

The template includes a comprehensive development workflow:

1. **Setup**: `make` - installs dependencies, sets up git, and configures pre-commit
2. **Testing**: `make test` - runs pytest with coverage
3. **Code Quality**: Pre-commit hooks run automatically with Ruff, MyPy, and more
4. **Documentation**: Auto-generated with pdoc and deployed to GitHub Pages
5. **Dependency Updates**: Automated with Dependabot

## Tools Included

-   **UV**: Fast Python package installer and resolver
-   **Ruff**: Lightning-fast linter and formatter
-   **MyPy**: Static type checking
-   **Pytest**: Testing framework with coverage reporting
-   **Pre-commit**: Git hooks for code quality
-   **Rich**: Beautiful terminal output and logging
-   **pdoc**: Automatic documentation generation

## Template Maintenance

This template is automatically maintained with:

-   Dependabot for dependency updates
-   Pre-commit hooks for code quality
-   GitHub Actions for testing template generation
-   Regular updates to tools and best practices

## Links

-   GitHub repo: [https://github.com/thomascamminady/cookiecutter-uvpackage](https://github.com/thomascamminady/cookiecutter-uvpackage)
-   Original inspiration: [https://github.com/audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
-   UV documentation: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
-   License: BSD
