# poetry-pyinvoke-plugin

A plugin for poetry that allows you to invoke commands in your `tasks.py` file delegating to `pyinvoke`.

Heavily inspired by the work from `keattang` on the [poetry-exec-plugin](https://github.com/keattang/poetry-exec-plugin) project.

<!--TOC-->

- [poetry-pyinvoke-plugin](#poetry-pyinvoke-plugin)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [User Guide](#user-guide)
  - [Configuration](#configuration)
  - [Command Line Usage](#command-line-usage)
    - [Quickstart](#quickstart-1)
  - [Detailed Command Usage](#detailed-command-usage)
    - [List All Tasks](#list-all-tasks)
    - [Run a Task](#run-a-task)
    - [Tasks with Arguments](#tasks-with-arguments)
      - [Singular Positional Argument](#singular-positional-argument)
      - [Named Arguments](#named-arguments)
      - [Multiple Named Arguments](#multiple-named-arguments)
    - [Task Help](#task-help)
    - [Plugin Help](#plugin-help)
    - [Invoke Help](#invoke-help)
- [Publishing](#publishing)
- [Contributing](#contributing)

<!--TOC-->

# Installation

Installation requires poetry 1.6.0+. To install this plugin run:

```sh
pip install poetry-pyinvoke-plugin
# OR
poetry self add poetry-pyinvoke-plugin
```

For other methods of installing plugins see the [poetry documentation](https://python-poetry.org/docs/master/plugins/#the-plugin-add-command).


# Quickstart

See [Configuration](#configuration) for details on how to setup a `tasks.py` file.

**List all tasks:**

```sh
poetry inv -- --list
```

**Run a task:**

```sh
poetry invoke lint
# OR
poetry inv lint
```

# User Guide

## Configuration

`tasks.py`
```python
from invoke import task

@task
def lint(c):
  c.run("flake8")
  c.run("black --check .")
```

## Command Line Usage


### Quickstart

Then:

```sh
poetry inv -- --list
```
**Example Output:**
```sh
Invoke: invoke --list 

Available tasks:

  build      Build wheel.
  format     Autoformat code for code style.
  greeting   Example task that takes an argument for testing purposes.
  lint       Linting and style checking.
  test       Run test suite.

```

**Run a task:**

```sh
poetry invoke lint
# OR
poetry inv lint
```

You can use either `poetry invoke` or `poetry inv`. The rest of this documentation will use `poetry inv`.


## Detailed Command Usage

### List All Tasks

This uses `--` to break the arguments to `poetry` and lets the remainder get passed to `invoke`.

**Command:**
```sh
poetry inv -- --list
```

**Example Output:**
```sh
Invoke: invoke --list 

Available tasks:

  build      Build wheel.
  format     Autoformat code for code style.
  greeting   Example task that takes an argument for testing purposes.
  lint       Linting and style checking.
  test       Run test suite.
```
----

### Run a Task

**Command:**
```sh
poetry inv lint
```

**Example Output:**
```sh
Invoke: invoke lint 

All done! ✨ 🍰 ✨
3 files would be left unchanged.
Skipped 3 files
Success: no issues found in 2 source files
```
----
### Tasks with Arguments

#### Singular Positional Argument

**Command:**
```sh
poetry inv greeting Loki
```

**Example Output:**
```sh
Invoke: invoke greeting Loki

Hello Loki, from Sylvie
```

**Command:**
```sh
poetry inv greeting -- Loki
```

**Example Output:**
```sh
Invoke: invoke greeting Loki

Hello Loki, from Sylvie
```

#### Named Arguments

**Command:**
```sh
poetry inv greeting -- --name Loki
```

**Example Output:**
```sh
Invoke: invoke greeting --name Loki

Hello Loki, from Sylvie
```

**Command:**
```sh
poetry inv greeting -- -n Loki
```

**Example Output:**
```sh
Invoke: invoke greeting -n Loki

Hello Loki, from Sylvie
```

#### Multiple Named Arguments

**Command:**
```sh
poetry inv greeting -- --name Loki --other Thor
```

**Example Output:**
```sh
Invoke: invoke greeting --name Loki --other Thor

Hello Loki, from Thor
```

**Command:**
```sh
poetry inv greeting -- -n Loki -o Thor
```

**Example Output:**
```sh
Invoke: invoke greeting -n Loki -o Thor

Hello Loki, from Thor
```
----

### Task Help

This uses `--` to break the arguments to `poetry` and lets the remainder get passed to `invoke`. It also uses `--help` positionally before the `task` command to get help for it.

**Command:**
```sh
poetry inv -- --help greeting
```

**Example Output:**
```sh
Invoke: invoke --help greeting

Usage: inv[oke] [--core-opts] greeting [--options] [other tasks here ...]

Docstring:
  Example task that takes an argument for testing purposes.

Options:
  -n STRING, --name=STRING
  -o STRING, --other=STRING
```

### Plugin Help

**Command:**
```sh
poetry inv --help
```

**Example Output:**
```sh
Description:
  Delegate out to pyinvoke tasks specified in your tasks.py file

Usage:
  inv [options] [--] <cmd> [<arguments>...]

Arguments:
  cmd                        The command to run from your tasks.py.
  arguments                  Additional arguments to append to the command.
```
----

### Invoke Help

This uses `--` to break the arguments to `poetry` and lets the remainder get passed to `invoke`.

**Command:**
```sh
poetry inv -- --help
```

**Example Output:**
```sh
Invoke: invoke --help 

Usage: inv[oke] [--core-opts] task1 [--task1-opts] ... taskN [--taskN-opts]
```
----

# Publishing

To publish a new version create a release from `main` (after pull request).

# Contributing

At all times, you have the power to fork this project, make changes as you see fit and then:

```sh
pip install https://github.com/user/repository/archive/branch.zip
```
[Stackoverflow: pip install from github branch](https://stackoverflow.com/a/24811490/622276)

That way you can run from your own custom fork in the interim or even in-house your work and simply use this project as a starting point. That is totally ok.

However if you would like to contribute your changes back, then open a Pull Request "across forks".

Once your changes are merged and published you can revert to the canonical version of `pip install`ing this package.

If you're not sure how to make changes or _if_ you should sink the time and effort, then open an Issue instead and we can have a chat to triage the issue.
