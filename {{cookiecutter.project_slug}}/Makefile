init:
	code .
	poetry env use 3.10
	poetry install
	poetry update
	git init
	poetry run pre-commit install
	git add .
	poetry run pre-commit run --all
	git commit -am "Initial commit after initializing project with cookiecutter."

make test:
	pytest .

make coverage:
	pytest --cov={{cookiecutter.project_slug}} tests/
