import type { Difficulty, Sudoku } from '$lib/types/sudoku';

export async function fetchSudoku(level: Difficulty): Promise<Sudoku> {
	const response = await fetch(`/api/sudoku?level=${level}`);

	if (!response.ok) {
		throw new Error('The Sudoku could not be generated.');
	}

	return response.json();
}
