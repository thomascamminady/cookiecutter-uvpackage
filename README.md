
# Cookiecutter PyPackage

Cookiecutter template for a Python package.

## Features

- Uses `uv` for dependency management and packaging.
- Uses `pre-commit` hooks.
- Deploys `pdoc` documentation via GitHub Pages.
- Can be configured with a single call of `make`.
- Strikes a balance between complexity and simplicity, tailored towards data scientists.

## Development

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/thomascamminady/cookiecutter-pypackage
```

Create a remote repository with the specified name and enable GitHub Actions as the deployment method for GitHub Pages.

Change into the new project folder and run:

```bash
make
```

And you're done!

> **Note**: For this to work, you **must not** be in an active `poetry` environment.

- GitHub repo: [https://github.com/thomascamminady/cookiecutter-pypackage](https://github.com/thomascamminady/cookiecutter-pypackage)
- Forked from: [https://github.com/audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- Free software: BSD license

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
