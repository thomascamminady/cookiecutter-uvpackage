======================
Cookiecutter PyPackage
======================

Cookiecutter_ template for a Python package.

Features
--------

* Uses ``poetry`` for dependency management and packaging.
* Uses ``pre-commit`` hooks.
* Deploys ``pdoc`` documentation via Github Pages.
* Can be configured with a single command.
* Strikes a balance between complexity and simplicity, tailored towards data scientists.

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/thomascamminady/cookiecutter-pypackage

Change into the new project folder and run::

    make

Note that for this to work, you **must** not be in an active ``poetry`` environment.


* GitHub repo: https://github.com/thomascamminady/cookiecutter-pypackage
* Forked from: https://github.com/audreyfeldroy/cookiecutter-pypackage
* Free software: BSD license

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
