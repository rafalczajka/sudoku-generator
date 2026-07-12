<script lang="ts">
	import type { Sudoku } from '$lib/types/sudoku';

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
		border: 2px solid #191919;
		background: #191919;
	}

	.cell {
		display: grid;
		place-items: center;
		border-right: 1px solid #cccccc;
		border-bottom: 1px solid #cccccc;
		background: #ffffff;
		font-size: clamp(1rem, 3.2vw, 1.65rem);
		font-weight: 700;
		font-variant-numeric: tabular-nums;
	}

	.cell:nth-child(9n) {
		border-right: 0;
	}

	.cell:nth-last-child(-n + 9) {
		border-bottom: 0;
	}

	.cell.box-right {
		border-right: 2px solid #191919;
	}

	.cell.box-bottom {
		border-bottom: 2px solid #191919;
	}

	.cell.solved {
		color: #2563eb;
		font-weight: 500;
	}

	.empty {
		display: grid;
		place-items: center;
		padding: 32px;
		border: 1px dashed #cccccc;
		color: #777777;
		background: #fafafa;
		text-align: center;
	}

	.empty p {
		max-width: 280px;
		margin: 0;
		font-size: 0.9rem;
		line-height: 1.5;
	}

	@media (max-width: 480px) {
		.cell {
			font-size: clamp(0.95rem, 6vw, 1.35rem);
		}
	}
</style>
