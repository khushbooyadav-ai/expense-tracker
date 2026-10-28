# Expense Tracker

[![Tests](https://github.com/khushbooyadav-ai/expense-tracker/actions/workflows/tests.yml/badge.svg)](https://github.com/khushbooyadav-ai/expense-tracker/actions/workflows/tests.yml)

A simple command-line tool to record and total my daily expenses, written in Python.

## Features

- Add an expense with a name and an amount
- View all expenses in a numbered list
- Show the total amount spent
- Delete an expense by its number
- An interactive menu that keeps running until you choose to quit
- Expenses are saved to a file, so they are kept between runs
- Friendly error message if the amount is not a number
- Logging of what the program does, for tracing problems

## Install

You need Python 3.10 or newer.

```
git clone https://github.com/khushbooyadav-ai/expense-tracker.git
cd expense-tracker
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

On macOS or Linux, activate the environment with `source .venv/bin/activate` instead. On Windows, if PowerShell blocks the activate script, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` first.

The tracker itself needs no extra libraries.

## Usage

```
expenses add tea 20
expenses list
expenses total
expenses delete 1
expenses --help
```

Run `expenses` with no arguments to use the interactive menu.

## Example

```
expenses add tea 20
Expense added successfully.

expenses list
1. tea: 20.0

expenses total
Total expenses: 20.0
```

## Where your data is stored

Expenses and the log file are saved in a folder called `.expense-tracker` inside your home folder (for example `C:\Users\YourName\.expense-tracker` on Windows). Every run uses the same data, wherever you start the command from.

## Development

Install the development tools, switch on the pre-commit hook, and run the checks:

```
pip install -r requirements.txt
pip install -e .
pre-commit install
python -m pytest
ruff check main.py test_main.py
ruff format --check main.py test_main.py
mypy main.py
```

The pre-commit hook runs ruff on every commit. If it fails, fix the problem (ruff format fixes files for you), run `git add` again, and commit again. The same checks run on GitHub on every push.

## Built with

- Python 3.10+ (no runtime libraries)
- Development tools: pytest, mypy, ruff, pre-commit
- GitHub Actions for automatic checks

## What I practised

- Lists and dictionaries to store records
- Functions to keep the code organised
- A `while` loop to build a menu
- Formatted output with f-strings
- Saving and loading data with JSON files
- Handling errors with try / except
- Classes and objects (an `Expense` class)
- Git branches, issues and pull requests
- Command-line tools with argparse
- Type hints and mypy
- Automated tests with pytest
- Logging
- Continuous integration with GitHub Actions
- Formatting and linting with ruff, and pre-commit hooks
- Packaging with pyproject.toml, and releases

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the version history.