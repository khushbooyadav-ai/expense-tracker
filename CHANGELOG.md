# Changelog

## [0.1.0]

First release.

### Added
- Command-line interface with add, list, total and delete command, plus an interactive menu
- Expenses saved a JSON in a fixed folder (.expense-tracker in the home directory)
- Logging to a file in a same folder
- Type hints and docstrings
- Tests with pytest, and CI  that runs ruff, mypy and pytest on every push
- Per-commit hook that runs ruff before each commit
- Packaging with pyproject.toml, so it installs with pip and runs as the expenses command