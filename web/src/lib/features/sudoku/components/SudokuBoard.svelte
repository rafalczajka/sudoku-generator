<script lang="ts">
	import type { Sudoku } from '../types';

	let { sudoku, showSolution }: { sudoku: Sudoku | null; showSolution: boolean } = $props();
</script>

{#if sudoku}
	<div class="board" aria-label={showSolution ? 'Sudoku solution' : 'Sudoku puzzle'}>
		{#each showSolution ? sudoku.solution : sudoku.puzzle as row, rowIndex (rowIndex)}
			{#each row as value, columnIndex (columnIndex)}
				<div
					class:solved={showSolution && sudoku.puzzle[rowIndex][columnIndex] === 0}
					class="cell"
					class:box-right={columnIndex === 2 || columnIndex === 5}
					class:box-bottom={rowIndex === 2 || rowIndex === 5}
				>
					{value || ''}
				</div>
			{/each}
		{/each}
	</div>
{:else}
	<div class="empty">
		<p>The first puzzle may take a little longer while the server wakes up.</p>
	</div>
{/if}

<style>
	.board,
	.empty {
		width: 100%;
		aspect-ratio: 1;
	}

	.board {
		display: grid;
		grid-template-columns: repeat(9, 1fr);
		border: 2px solid var(--color-text);
		background: var(--color-text);
	}

	.cell {
		display: grid;
		place-items: center;
		border-right: 1px solid var(--color-border);
		border-bottom: 1px solid var(--color-border);
		background: var(--color-surface);
		font-size: clamp(1.2rem, 4.5vw, 1.65rem);
		font-weight: var(--font-weight-bold);
		font-variant-numeric: tabular-nums;
	}

	.cell:nth-child(9n) {
		border-right: 0;
	}

	.cell:nth-last-child(-n + 9) {
		border-bottom: 0;
	}

	.cell.box-right {
		border-right: 2px solid var(--color-text);
	}

	.cell.box-bottom {
		border-bottom: 2px solid var(--color-text);
	}

	.cell.solved {
		color: var(--color-accent);
		font-weight: var(--font-weight-medium);
	}

	.empty {
		display: grid;
		place-items: center;
		padding: var(--space-8);
		border: 1px dashed var(--color-border-subtle);
		color: var(--color-text-muted);
		background: var(--color-surface-subtle);
		text-align: center;
	}

	.empty p {
		max-width: 280px;
		margin: 0;
		font-size: var(--font-size-small);
		line-height: var(--line-height-base);
	}
</style>
