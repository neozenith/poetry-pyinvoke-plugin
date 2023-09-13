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

## Publishing

To publish a new version create a release from `main` (after pull request).
