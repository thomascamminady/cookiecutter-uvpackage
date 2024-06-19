SHELL := /bin/bash

# phony targets
.PHONY: all poetry git test coverage

all:
	$(MAKE) poetry
	$(MAKE) git
	if command -v code > /dev/null; then code . --profile "Wahooligan"; fi
	$(MAKE) remotegit

poetry:
	poetry config --local virtualenvs.create true
	poetry config --local virtualenvs.in-project true
	if command -v python3.11 > /dev/null; then poetry env use 3.11; \
	elif command -v python3.10 > /dev/null; then poetry env use 3.10; \
	else echo "Neither Python 3.11 nor Python 3.10 were found. Please install one of them."; exit 1; fi
	poetry install
	poetry update
	# poetry export -f requirements.txt --output requirements.txt

git:
	git init
	git lfs install
	git add .
	poetry run pre-commit install
	poetry run pre-commit run --all-files
	git commit -am "First commit after initializing the project."

remotegit:
	git branch -M main
	-git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.git
	-git push -u origin main

test:
	poetry run pytest .

coverage:
	poetry run pytest --cov={{cookiecutter.project_slug}} tests/
