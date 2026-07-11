import random
from typing import Optional

Board = list[list[int]]

DIGITS = set(range(1, 10))

TARGET_CLUES = {
    'easy': 40,
    'medium': 34,
    'hard': 28,
    'expert': 24,
}


def candidates(board: Board, row: int, col: int) -> list[int]:
    """Return the values that can be placed in the given cell."""
    if board[row][col] != 0:
        return []

    used = set(board[row])
    used.update(board[r][col] for r in range(9))

    box_row = 3 * (row // 3)
    box_col = 3 * (col // 3)

    used.update(
        board[r][c]
        for r in range(box_row, box_row + 3)
        for c in range(box_col, box_col + 3)
    )

    return list(DIGITS - used)


def find_mrv_cell(
    board: Board,
) -> Optional[tuple[int, int, list[int]]]:
    """
    Find the empty cell with the fewest candidate values.

    MRV = Minimum Remaining Values.
    """
    best_cell = None
    best_values = None

    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                continue

            values = candidates(board, row, col)

            # A cell without candidates indicates an immediate contradiction.
            if not values:
                return row, col, []

            if best_values is None or len(values) < len(best_values):
                best_cell = (row, col)
                best_values = values

                # A cell with exactly one candidate is already optimal.
                if len(values) == 1:
                    return row, col, values

    if best_cell is None:
        return None

    return best_cell[0], best_cell[1], best_values


def fill_complete_grid(board: Board) -> bool:
    """Generate a complete valid grid in random order."""
    cell = find_mrv_cell(board)

    if cell is None:
        return True

    row, col, values = cell
    random.shuffle(values)

    for value in values:
        board[row][col] = value

        if fill_complete_grid(board):
            return True

    board[row][col] = 0
    return False


def count_solutions(board: Board, limit: int = 2) -> int:
    """
    Count solutions, stopping once the given limit is reached.

    The generator only needs to distinguish between three cases:
    no solutions, one solution, and at least two solutions.
    """
    total = 0

    def search() -> None:
        nonlocal total

        if total >= limit:
            return

        cell = find_mrv_cell(board)

        if cell is None:
            total += 1
            return

        row, col, values = cell

        for value in values:
            board[row][col] = value
            search()
            board[row][col] = 0

            if total >= limit:
                return

    search()
    return total


def analyze_difficulty(board: Board) -> dict:
    """
    Estimate the puzzle difficulty.

    The result depends on this solver's behavior, so the thresholds should
    be treated as a starting point for further calibration.
    """
    work = [row[:] for row in board]

    stats = {
        'guesses': 0,
        'backtracks': 0,
        'nodes': 0,
    }

    def solve() -> bool:
        stats['nodes'] += 1

        cell = find_mrv_cell(work)

        if cell is None:
            return True

        row, col, values = cell

        if not values:
            return False

        if len(values) > 1:
            stats['guesses'] += 1

        # A stable order makes the difficulty assessment reproducible.
        for value in sorted(values):
            work[row][col] = value

            if solve():
                return True

        work[row][col] = 0
        stats['backtracks'] += 1
        return False

    if not solve():
        raise ValueError('Plansza nie ma rozwiązania')

    clues = sum(
        value != 0
        for row in board
        for value in row
    )

    score = (
        stats['guesses'] * 10
        + stats['backtracks'] * 3
    )

    if score == 0 and clues >= 36:
        level = 'easy'
    elif score < 80:
        level = 'medium'
    elif score < 600:
        level = 'hard'
    else:
        level = 'expert'

    return {
        'level': level,
        'clues': clues,
        'score': score,
        **stats,
    }


def make_removal_groups(
    rotational_symmetry: bool,
) -> list[list[tuple[int, int]]]:
    """
    With rotational symmetry, cells (r, c) and (8-r, 8-c)
    are removed together.
    """
    if not rotational_symmetry:
        groups = [
            [(row, col)]
            for row in range(9)
            for col in range(9)
        ]
        random.shuffle(groups)
        return groups

    groups = []
    visited = set()

    for row in range(9):
        for col in range(9):
            if (row, col) in visited:
                continue

            opposite = (8 - row, 8 - col)

            group = sorted({
                (row, col),
                opposite,
            })

            groups.append(group)
            visited.update(group)

    random.shuffle(groups)
    return groups


def make_candidate(
    target_clues: int,
    rotational_symmetry: bool = True,
) -> tuple[Board, Board]:
    """Create a single puzzle candidate."""
    puzzle = [[0] * 9 for _ in range(9)]

    if not fill_complete_grid(puzzle):
        raise RuntimeError('Nie udało się wygenerować pełnej planszy')

    solution = [row[:] for row in puzzle]
    clue_count = 81

    groups = make_removal_groups(rotational_symmetry)

    for group in groups:
        occupied = [
            (row, col)
            for row, col in group
            if puzzle[row][col] != 0
        ]

        if clue_count - len(occupied) < target_clues:
            continue

        previous_values = [
            puzzle[row][col]
            for row, col in occupied
        ]

        for row, col in occupied:
            puzzle[row][col] = 0

        # Keep the removal only if the puzzle still has a unique solution.
        if count_solutions(puzzle, limit=2) == 1:
            clue_count -= len(occupied)
        else:
            for (row, col), value in zip(
                occupied,
                previous_values,
            ):
                puzzle[row][col] = value

    return puzzle, solution


def generate_sudoku(
    level: str = 'medium',
    rotational_symmetry: bool = True,
    max_attempts: int = 50,
    seed: Optional[int] = None,
) -> tuple[Board, Board, dict]:
    """
    Generate a Sudoku puzzle at the requested approximate difficulty level.

    Returns:
        puzzle, solution, statistics
    """
    if level not in TARGET_CLUES:
        allowed = ', '.join(TARGET_CLUES)
        raise ValueError(f'Nieznany poziom. Dostępne: {allowed}')

    if seed is not None:
        random.seed(seed)

    target_clues = TARGET_CLUES[level]
    level_order = ['easy', 'medium', 'hard', 'expert']

    closest_candidate = None

    for _ in range(max_attempts):
        puzzle, solution = make_candidate(
            target_clues=target_clues,
            rotational_symmetry=rotational_symmetry,
        )

        stats = analyze_difficulty(puzzle)

        if stats['level'] == level:
            return puzzle, solution, stats

        distance = abs(
            level_order.index(stats['level'])
            - level_order.index(level)
        )

        if (
            closest_candidate is None
            or distance < closest_candidate[0]
        ):
            closest_candidate = (
                distance,
                puzzle,
                solution,
                stats,
            )

    # If no exact difficulty match was found, return the closest candidate.
    _, puzzle, solution, stats = closest_candidate
    return puzzle, solution, stats


def print_board(board: Board) -> None:
    for row_index, row in enumerate(board):
        if row_index in (3, 6):
            print('------+-------+------')

        parts = []

        for col_index, value in enumerate(row):
            if col_index in (3, 6):
                parts.append('|')

            parts.append(str(value) if value else '.')

        print(' '.join(parts))


def _legacy_main() -> None:
    puzzle, solution, stats = generate_sudoku(
        level='hard',
        rotational_symmetry=True,
        seed=None,
    )

    print('Sudoku:')
    print_board(puzzle)

    print('\nStatystyki:')
    print(stats)

    print('\nRozwiązanie:')
    print_board(solution)
