SHELL := /bin/bash

# phony targets
.PHONY: all uv git test coverage

all:
	$(MAKE) uv
	$(MAKE) git
	if command -v code > /dev/null; then code . ; fi
	$(MAKE) remotegit

uv:
	uv python install {{ cookiecutter.python_version }}
	uv sync
	uv tool install isort
	uv tool install pre-commit
	uv tool install pytest
	uv tool install pyclean

git:
	git init
	git lfs install
	uvx pre-commit autoupdate
	uvx pre-commit run --all-files || true
	git add .
	git commit -am "First commit after initializing the project."

remotegit:
	git branch -M main
	git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.git || true
	@echo "Attempting to push to remote repository..."
	@if git push -u origin main 2>/dev/null; then \
		echo "✅ Successfully pushed to GitHub!"; \
	else \
		echo "⚠️  Could not push to remote repository."; \
		echo "Please create the repository on GitHub first:"; \
		echo "https://github.com/new"; \
		echo "Repository name: {{ cookiecutter.github_reponame }}"; \
		echo "Then run: git push -u origin main"; \
	fi


test:
	uvx pytest .

coverage:
	uvx pytest --cov={{cookiecutter.project_slug}} tests/

hello_world:
	uv run scripts/hello_world.py
