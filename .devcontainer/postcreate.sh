#!/bin/zsh

# Install dependencies
poetry install

# Allow precommit to install properly
git config --global --add safe.directory /workspace

# Install precommit hooks
pre-commit install && pre-commit install -t commit-msg
