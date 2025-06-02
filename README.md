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

We can use [pre-commit](https://pre-commit.com/) to automatically setup our pre commit hooks. It is
configured by `.pre-commit-config.yaml`.

Ensure dev dependencies are installed:

```bash
python -m pip install .[dev]
```

Then install and setup `pre-commit`

```bash
pre-commit install
```

You can run on all files like so:
```bash
pre-commit run --all-files
```

Now this will be run on all new commits, rejecting any that fail and auto fixing that which it can.
