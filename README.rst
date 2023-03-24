======================
Cookiecutter PyPackage
======================

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/thomascamminady/cookiecutter-pypackage
* Forked from: https://github.com/audreyfeldroy/cookiecutter-pypackage
* Free software: BSD license

Features
--------

* Uses `poetry` for dependency management and packaging.
* Uses `pre-commit` hooks.
* Can be configured with a single command.
* Strikes a balance between complexity and simplicity, tailored towards data scientists.


Project folder
--------
A project folder with the following layout will be created::

    .
    ├── LICENSE
    ├── Makefile
    ├── README.rst
    ├── data
    ├── notebooks
    │   ├── main.ipynb
    │   └── output
    ├── pyproject.toml
    ├── tests
    │   ├── __init__.py
    │   └── test_{{cookiecutter.project_slug}}.py
    └── {{cookiecutter.project_slug}}
        ├── __init__.py
        └── utils
            ├── __init__.py
            ├── config.py
            └── logger.py

The variable ``{{cookiecutter.project_slug}}`` will be replaced by your project name. 

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/thomascamminady/cookiecutter-pypackage
    
Change into the new project folder and run::

    make init 
    
    
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
