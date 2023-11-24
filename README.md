# poetry-pyinvoke-plugin

A plugin for poetry that allows you to invoke commands in your `tasks.py` file delegating to `pyinvoke`.

Heavily inspired by the work from `keattang` on the [poetry-exec-plugin](https://github.com/keattang/poetry-exec-plugin) project.

## Installation

Installation requires poetry 1.6.0+. To install this plugin run:

```sh
pip install poetry-pyinvoke-plugin
# OR
poetry self add poetry-pyinvoke-plugin
```

For other methods of installing plugins see the [poetry documentation](https://python-poetry.org/docs/master/plugins/#the-plugin-add-command).

## Usage

`tasks.py`
```python
from invoke import task

@task
def lint(c):
  c.run("flake8")
  c.run("black --check .")
```

Then:
```sh
poetry invoke lint
# OR
poetry inv lint
```

### Using command-line options

If passing any command-line options to `poetry invoke`, 
these may have to be separated by `--` to indicate that the command-line options should be passed to `poetry invoke` instead of `poetry`.

For instance to list all commands available to invoke, `poetry invoke --list` would fail as it is providing `--list` to `poetry`. Instead you should use `poetry invoke -- --list`. 

This works similarly for commands, for example `poetry invoke cmd -- --opt 1` for a command `cmd` that takes an option `--opt`.

## Publishing

To publish a new version create a release from `main` (after pull request).
