#!/bin/bash
set -ex

# Common alias
echo 'alias ltr="ls -ltr"' >> $HOME/.bashrc
echo 'alias pytestcov="pytest --cov=devcontainer_tutorial tests/"' >> $HOME/.bashrc

# Convenience workspace directory for later use
WORKSPACE_DIR=$(pwd)

# Change some Poetry settings to better deal with working in a container
poetry self update
poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true

poetry install
#pre-commit autoupdate

clear
poetry shell
