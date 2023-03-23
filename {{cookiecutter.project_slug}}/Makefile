init:
	code .
	poetry env use 3.10
	poetry install
	poetry update
	git init
	echo "logs/" >> .gitignore
	git lfs install
	git lfs track "*.fit"
	git lfs track "*.hdf5"
	git lfs track "*.html"
	git lfs track "*.parquet"
	git add .
	poetry run pre-commit run --all-files
	git commit -am "Initial commit after initializing the project."
	poetry shell

test:
	pytest .

coverage:
	pytest --cov={{cookiecutter.project_slug}} tests/
