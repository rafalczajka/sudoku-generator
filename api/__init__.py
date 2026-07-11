"""HTTP API for the Sudoku generator."""

from flask import Flask, jsonify, request

from generator import generate_sudoku

DIFFICULTY_LEVELS = ('easy', 'medium', 'hard', 'expert')


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.get('/api/health')
    def health():
        return {'status': 'ok'}

    @app.get('/api/sudoku')
    def sudoku():
        level = request.args.get('level', 'medium').strip().lower()

        if level not in DIFFICULTY_LEVELS:
            return jsonify({
                'error': 'Invalid difficulty level.',
                'allowed_levels': DIFFICULTY_LEVELS,
            }), 400

        puzzle, solution, stats = generate_sudoku(level=level)

        return {
            'puzzle': puzzle,
            'solution': solution,
            'stats': stats,
        }

    return app
