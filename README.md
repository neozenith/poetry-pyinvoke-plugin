# poetry-pyinvoke-plugin

A plugin for poetry that allows you to invoke commands in your `tasks.py` file delegating to `pyinvoke`.

Heavily inspired by the work from `keattang` on the [poetry-exec-plugin](https://github.com/keattang/poetry-exec-plugin) project.

## Installation

Installation requires poetry 1.2.0+. To install this plugin run:

```sh
pip install poetry-pyinvoke-plugin
# OR
poetry add -D poetry-pyinvoke-plugin
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

To publish a new version,first bump the package version in `pyproject.toml` and commit your changes to the `main` branch (via pull request). Then in GitHub create a new release with the new version as the tag and name. You can use the handy auto release notes feature to populate the release description.
