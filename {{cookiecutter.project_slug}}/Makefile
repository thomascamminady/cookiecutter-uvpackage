init:
	code .
	poetry env use 3.10
	poetry install
	poetry update
	git init
	git lfs install
	git lfs track "*.fit"
	git lfs track "*.hdf5"
	git add .
	poetry run pre-commit run --all-files
	git commit -am "Initial commit after initializing the project."
	poetry shell

test:
	pytest .

coverage:
	pytest --cov={{cookiecutter.project_slug}} tests/
