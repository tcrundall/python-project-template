# Template python project

A fun way for me to craft a starting point for a python project.

All commands are to be run in the project's top level directory (i.e. this one) unless specified
otherwise.

## Installing

I like using `uv` as my python version manager + other. If you are like me, replace `python -m` with
`uv` in the following commands.

Create a virtual environment:

```bash
python -m venv
```

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install .
```

## Run tests

Ensure dev dependencies are installed:

```bash
python -m pip install .[dev]
```

Then run tests

```bash
pytest
```

## Using tool

There is currently a place holder "cli" (command line interface) `example-cli`. Assuming you
installed the package as described above, you should be able to execute the cli:

```bash
exaple-cli
> "Hello"
```

## Linting

Linters were invented so that programmers wouldn't have to worry about formatting. I like
[ruff](https://docs.astral.sh/ruff/).

Ensure dev dependencies are installed:

```bash
python -m pip install .[dev]
```

Then run linter:

```bash
ruff format
```

Ruff settings can be specified in `pyproject.toml`.

## Type hints

Type hints allow python to let you know about some bugs before you run the code. You can check type
hints using a type checker.

I like [pyright](https://microsoft.github.io/pyright/#/).

Ensure dev dependencies are installed:

```bash
python -m pip install .[dev]
```

Then run linter:

```bash
pyright
```

Ruff settings can be specified in `pyproject.toml`.

## Pre-commit hooks

If you want to automate e.g. formatting and type checking before each commit, then create an
executable `.git/hooks/pre-commit` with the following content:

```sh
#!/bin/sh
set -eux

ruff format --exit-non-zero-on-format || exit 1 # exit if ruff returns non-zero exit code
pyright || exit 1 # exit if pyright returns non-zero exit code
```

> **TODO**: only perform format on code to be committed
