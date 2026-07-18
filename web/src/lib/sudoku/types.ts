export type Difficulty = 'easy' | 'medium' | 'hard' | 'expert';

type Board = number[][];

export type SudokuStats = {
	level: Difficulty;
	clues: number;
	score: number;
};

export type Sudoku = {
	puzzle: Board;
	solution: Board;
	stats: SudokuStats;
};
