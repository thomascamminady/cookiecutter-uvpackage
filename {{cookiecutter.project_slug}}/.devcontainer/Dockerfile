# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.231.6/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon):
# 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN sudo apt-get update
RUN sudo apt-get --assume-yes install vim

RUN pip install --upgrade pip

ARG POETRY_VERSION="none"
RUN if [ "${POETRY_VERSION}" != "none" ]; then su vscode -c "umask 0002 && pip3 install poetry==${POETRY_VERSION}"; fi

# ARG NOX_VERSION="none"
# RUN if [ "${NOX_VERSION}" != "none" ]; then su vscode -c "umask 0002 && pip3 install nox-poetry nox==${NOX_VERSION}"; fi


RUN pip install pyclean
RUN pip install pre-commit

COPY .pre-commit-config.yaml .
RUN git init .
