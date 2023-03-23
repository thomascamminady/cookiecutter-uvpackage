"""Top-level package for {{ cookiecutter.project_name }}."""
from {{ cookiecutter.project_name }}.utils.config import config
from {{ cookiecutter.project_name }}.utils.logger import logger

__all__ = ["config", "logger"]
__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"


