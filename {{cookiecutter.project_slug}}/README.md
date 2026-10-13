# {{ cookiecutter.project_name }}
{% if cookiecutter.project_short_description %}
{{ cookiecutter.project_short_description }}
{% endif %}
[Repository](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}) ·
[Documentation](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.github_reponame }})

## Development

Requires [uv](https://docs.astral.sh/uv/). Run `make` once to install
everything, initialize git with pre-commit hooks, and push to GitHub.

| Command         | Description                                 |
| --------------- | ------------------------------------------- |
| `make install`  | Install Python and all dependencies         |
| `make check`    | Lint, type check and test (same as CI)      |
| `make format`   | Auto-fix lint issues and format the code    |
| `make coverage` | Run the tests with a coverage report        |
| `make docs`     | Build the documentation into `docs/`        |

## Documentation

The documentation is built with [pdoc](https://pdoc.dev) and deployed to
GitHub Pages. Enable it once under Settings → Pages → Build and deployment →
Source: GitHub Actions.

## Credits

Created with [cookiecutter](https://github.com/cookiecutter/cookiecutter) and
[thomascamminady/cookiecutter-uvpackage](https://github.com/thomascamminady/cookiecutter-uvpackage).
