import { apiEndpoint } from '$lib/api/client';

import type { Difficulty, Sudoku } from './types';

export async function fetchSudoku(level: Difficulty): Promise<Sudoku> {
	const response = await fetch(apiEndpoint(`/api/sudoku?level=${level}`));

	if (!response.ok) {
		throw new Error('The Sudoku could not be generated.');
	}

	return response.json();
}
