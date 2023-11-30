# Standard Library
import subprocess


def test_invoke() -> None:
    """Check that the plugin command works when this project installs itself."""
    result = subprocess.run("poetry inv lint", capture_output=True, shell=True, text=True)
    output = result.stdout.strip()
    assert "Invoke: invoke lint" in output


def test_invoke_list() -> None:
    result = subprocess.run("poetry inv -- --list", capture_output=True, shell=True, text=True)
    output = result.stdout.strip()
    assert "lint" in output
    assert "test" in output


def test_invoke_command_help() -> None:
    result = subprocess.run("poetry inv -- --help greeting", capture_output=True, shell=True, text=True)
    output = result.stdout.strip()
    assert "Example task that takes an argument for testing purposes." in output


def test_invoke_command_positional_args() -> None:
    result = subprocess.run("poetry inv greeting -- Loki", capture_output=True, shell=True, text=True)
    output = result.stdout.strip()
    assert "Hello Loki" in output


def test_invoke_command_keyword_args() -> None:
    result = subprocess.run("poetry inv greeting -- --name Loki", capture_output=True, shell=True, text=True)
    output = result.stdout.strip()
    assert "Hello Loki" in output


def test_invoke_command_short_keyword_args() -> None:
    result = subprocess.run("poetry inv greeting -- -n Loki", capture_output=True, shell=True, text=True)
    output = result.stdout.strip()
    assert "Hello Loki" in output
