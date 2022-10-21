======================
Cookiecutter PyPackage
======================

.. image:: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/shield.svg
    :target: https://pyup.io/repos/github/audreyfeldroy/cookiecutter-pypackage/
    :alt: Updates

.. image:: https://travis-ci.org/audreyfeldroy/cookiecutter-pypackage.svg?branch=master
    :target: https://travis-ci.org/github/audreyfeldroy/cookiecutter-pypackage
    :alt: Build Status

.. image:: https://readthedocs.org/projects/cookiecutter-pypackage/badge/?version=latest
    :target: https://cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/thomascamminady/cookiecutter-pypackage
* Free software: BSD license

Features
--------

* Testing setup with ``pytest``
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter



Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/thomascamminady/cookiecutter-pypackage
