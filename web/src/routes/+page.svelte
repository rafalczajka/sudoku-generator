<script lang="ts">
	import { fetchSudoku } from '$lib/api/sudoku';
	import SudokuBoard from '$lib/components/SudokuBoard.svelte';
	import SudokuControls from '$lib/components/SudokuControls.svelte';
	import type { Difficulty, Sudoku } from '$lib/types/sudoku';

	let level: Difficulty = $state('medium');
	let sudoku: Sudoku | null = $state(null);
	let showSolution = $state(false);
	let loading = $state(false);
	let error = $state('');

	async function generateSudoku() {
		loading = true;
		error = '';
		showSolution = false;

		try {
			sudoku = await fetchSudoku(level);
		} catch (requestError) {
			error = requestError instanceof Error ? requestError.message : 'Something went wrong.';
		} finally {
			loading = false;
		}
	}
</script>

<svelte:head>
	<title>Sudoku Generator</title>
	<meta name="description" content="Generate Sudoku puzzles at four difficulty levels." />
</svelte:head>

<main>
	<section class="workspace" aria-label="Sudoku generator">
		<h1>Sudoku Generator</h1>
		<SudokuControls bind:level {loading} onGenerate={generateSudoku} />

		{#if error}
			<p class="message" role="alert">{error} Please try again.</p>
		{:else}
			<SudokuBoard {sudoku} {showSolution} />
		{/if}

		{#if sudoku && !error}
			<div class="footer">
				<p><strong>{sudoku.stats.level}</strong> · {sudoku.stats.clues} clues</p>
				<button onclick={() => (showSolution = !showSolution)}>
					{showSolution ? 'Hide solution' : 'Show solution'}
				</button>
			</div>
		{:else if !error}
			<div class="footer-placeholder" aria-hidden="true"></div>
		{/if}
	</section>
</main>

<style>
	:global(*) {
		box-sizing: border-box;
	}

	:global(html) {
		font-family:
			Inter,
			ui-sans-serif,
			system-ui,
			-apple-system,
			BlinkMacSystemFont,
			'Segoe UI',
			sans-serif;
		color: #191919;
		background: #ffffff;
	}

	:global(body) {
		margin: 0;
		min-width: 320px;
	}

	:global(button),
	:global(select) {
		font: inherit;
	}

	main {
		display: flex;
		align-items: center;
		width: min(480px, calc(100% - 32px));
		min-height: 100vh;
		margin: 0 auto;
		padding: 20px 0;
	}

	.workspace {
		width: 100%;
	}

	h1 {
		margin: 0 0 20px;
		font-size: 2rem;
		font-weight: 650;
		letter-spacing: -0.02em;
		text-align: center;
	}

	.footer,
	.footer-placeholder {
		min-height: 60px;
	}

	.footer {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 16px;
		padding-top: 14px;
	}

	.footer p {
		margin: 0;
		color: #666666;
		font-size: 0.9rem;
		text-transform: capitalize;
	}

	.footer strong {
		color: #191919;
	}

	.footer button {
		min-height: 46px;
		border: 1px solid #cccccc;
		border-radius: 6px;
		padding: 0 18px;
		color: #191919;
		background: transparent;
		font-weight: 700;
		cursor: pointer;
	}

	.footer button:hover {
		background: #f4f4f4;
	}

	.footer button:focus-visible {
		outline: 2px solid #777777;
		outline-offset: 2px;
	}

	.message {
		margin: 0;
		padding: 16px;
		border-radius: 6px;
		color: #8c281c;
		background: #fbe8e2;
		font-size: 0.9rem;
	}

	@media (max-width: 480px) {
		main {
			width: calc(100% - 24px);
			padding: 24px 0;
		}

		.footer,
		.footer-placeholder {
			min-height: 93px;
		}

		.footer {
			align-items: stretch;
			flex-direction: column;
		}
	}
</style>
