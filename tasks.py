from invoke import task


@task
def lint(c):
    c.run("black --check .")
