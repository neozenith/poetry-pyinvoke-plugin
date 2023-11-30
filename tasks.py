# Standard Library
import shutil

# Third Party
from invoke import task


@task
def format(c):
    """Autoformat code for code style."""
    c.run("black .")
    c.run("isort .")


@task
def lint(c):
    """Linting and style checking."""
    c.run("black --check .", pty=True)
    c.run("isort --check .", pty=True)
    c.run("flake8 .", pty=True)
    c.run("mypy .", pty=True)


@task
def test(c):
    """Run test suite."""
    c.run("python3 -m pytest")


@task
def build(c):
    """Build wheel."""
    shutil.rmtree("dist/", ignore_errors=True)
    c.run("poetry build -f wheel")


@task
def greeting(c, name, other="Sylvie"):
    """Example task that takes an argument for testing purposes."""
    print(f"Hello {name}, from {other}")
