init:
	code .
	poetry env use 3.10
	poetry install
	poetry update
	git init
	git lfs install
	git lfs track "*.fit"
	git lfs track "*.hdf5"
	poetry run pre-commit install
	git add .
	poetry run pre-commit run --all
	git commit -am "Initial commit after initializing project with cookiecutter."

test:
	pytest .

coverage:
	pytest --cov={{cookiecutter.project_slug}} tests/
