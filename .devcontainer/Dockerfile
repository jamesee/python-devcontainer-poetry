FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye
# Install the xz-utils package
WORKDIR   /workspace
RUN apt-get update && apt-get install -y xz-utils
RUN pip install --upgrade pip poetry