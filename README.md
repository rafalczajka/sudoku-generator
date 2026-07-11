# Sudoku Generator

A Sudoku generator with a Python CLI, Flask API, and SvelteKit web client.

## Setup

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Activate the virtual environment before running the project.

## Development with Docker

Run the API and web client together:

```bash
docker compose up --build
```

The web client is available at `http://localhost:5173` and the API at
`http://localhost:5000`.

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

## Web

```bash
cd web
npm install
npm run dev
```

The client is available at `http://localhost:5173`. During development,
requests to `/api` are proxied to the Flask API at `http://localhost:5000`.
