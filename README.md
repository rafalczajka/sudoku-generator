# Sudoku Generator

A Python Sudoku generator with a command-line interface and a Flask API.

## Setup

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Activate the virtual environment before running the project.

## CLI

```bash
python -m generator
```

## Python

```python
from generator import generate_sudoku

puzzle, solution, stats = generate_sudoku(level='medium')
```

Available levels: `easy`, `medium`, `hard`, and `expert`.

## API

```bash
flask --app api run --debug
```

Generate a Sudoku puzzle:

```http
GET /api/sudoku?level=medium
```

Health check:

```http
GET /api/health
```
