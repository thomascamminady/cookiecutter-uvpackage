SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all

PACKAGE := {{ cookiecutter.project_slug }}
REMOTE := git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.git

.PHONY: all help install git remote format lint typecheck test coverage check docs hello_world

all: install git ## Bootstrap: install, initialize git, open VS Code, push to GitHub
	@if command -v code >/dev/null; then code .; fi
	$(MAKE) remote

help: ## Show this help
	@grep -E '^[a-z_]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'

install: ## Install Python and all dependencies
	uv python install
	uv sync --all-extras --all-groups

git: ## Initialize the repository, install pre-commit hooks, make the first commit
	@if [ ! -d .git ]; then git init -b main; fi
	uv run pre-commit install
	git add -A
	uv run pre-commit run --all-files || true
	git add -A
	@if ! git rev-parse --verify HEAD >/dev/null 2>&1; then \
		git commit -m "Initial commit"; \
	fi

remote: ## Add the GitHub remote and push
	git remote add origin $(REMOTE) 2>/dev/null || true
	@if git push -u origin main; then \
		echo "✅ Pushed to GitHub."; \
	else \
		echo "⚠️  Could not push. Create the repository first: https://github.com/new"; \
		echo "   Name: {{ cookiecutter.github_reponame }}, then run: git push -u origin main"; \
	fi

format: ## Auto-fix lint issues and format the code
	uv run ruff check --fix
	uv run ruff format

lint: ## Lint and check formatting
	uv run ruff check
	uv run ruff format --check

typecheck: ## Type check with ty
	uv run ty check

test: ## Run the tests
	uv run pytest

coverage: ## Run the tests with a coverage report
	uv run pytest --cov

check: lint typecheck test ## Run all checks (same as CI)

docs: ## Build the documentation into docs/
	uv run --group docs pdoc $(PACKAGE) -o docs --docformat numpy

hello_world: ## Run the example script
	uv run scripts/hello_world.py
