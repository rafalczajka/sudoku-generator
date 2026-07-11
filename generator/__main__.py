"""Simple command-line interface for the Sudoku generator."""

import sys

from .sudoku_generator import TARGET_CLUES, generate_sudoku, print_board


def choose_level() -> str:
    """Ask the user for a difficulty level and return its name."""
    levels = list(TARGET_CLUES)

    print('Choose a difficulty level:')
    for number, level in enumerate(levels, start=1):
        print(f'  {number}. {level}')

    while True:
        choice = input('Your choice [2]: ').strip().lower()
        
        if not choice:
            return 'medium'
        if choice in levels:
            return choice
        if choice.isdigit() and 1 <= int(choice) <= len(levels):
            return levels[int(choice) - 1]

        print('Invalid choice. Enter a level number or name.')


def main() -> None:
    """Run the generator in interactive mode."""
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    level = choose_level()
    print(f'\nGenerating Sudoku ({level})...\n')
    puzzle, solution, stats = generate_sudoku(level=level)

    print('Sudoku:')
    print_board(puzzle)
    print('\nStatistics:')
    actual_level = stats['level']
    clues = stats['clues']
    score = stats['score']
    print(
        f'level: {actual_level}, clues: {clues}, score: {score}'
    )
    print('\nSolution:')
    print_board(solution)


if __name__ == '__main__':
    main()
