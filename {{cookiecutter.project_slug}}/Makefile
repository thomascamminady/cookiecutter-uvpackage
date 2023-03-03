init:
	code .
	poetry env use 3.10
	poetry install
	git init
	pre-commit install
	git add .
	git commit -am "Initial commit after initializing project with cookiecutter."

make test:
	pytest .
make coverage:
	pytest --cov={{cookiecutter.project_slug}} tests/
