import { env } from '$env/dynamic/public';
import type { Difficulty, Sudoku } from '$lib/types/sudoku';

export async function fetchSudoku(level: Difficulty): Promise<Sudoku> {
	const apiUrl = (env.PUBLIC_API_URL ?? '').replace(/\/$/, '');
	const response = await fetch(`${apiUrl}/api/sudoku?level=${level}`);

	if (!response.ok) {
		throw new Error('The Sudoku could not be generated.');
	}

	return response.json();
}
