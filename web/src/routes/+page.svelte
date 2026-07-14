<script lang="ts">
	import { asset } from '$app/paths';
	import { onMount } from 'svelte';

	import { warmUpApi } from '$lib/api/health';
	import { fetchSudoku } from '$lib/api/sudoku';
	import Button from '$lib/components/Button.svelte';
	import SudokuBoard from '$lib/components/SudokuBoard.svelte';
	import SudokuControls from '$lib/components/SudokuControls.svelte';
	import type { Difficulty, Sudoku } from '$lib/types/sudoku';

	let level: Difficulty = $state('medium');
	let sudoku: Sudoku | null = $state(null);
	let showSolution = $state(false);
	let loading = $state(false);
	let error = $state('');

	onMount(warmUpApi);

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

		<footer>
			{#if sudoku && !error}
				<div class="puzzle-details">
					<p><strong>{sudoku.stats.level}</strong> · {sudoku.stats.clues} clues</p>
					<Button onclick={() => (showSolution = !showSolution)}>
						{showSolution ? 'Hide solution' : 'Show solution'}
					</Button>
				</div>
			{/if}

			<a class="download" href={asset('/printable-grid-6.pdf')} download>
				Download printable grids (PDF)
			</a>
		</footer>
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
		width: min(480px, calc(100% - 32px));
		margin: 0 auto;
		padding: 32px 0;
	}

	h1 {
		margin: 0 0 20px;
		font-size: 2rem;
		font-weight: 650;
		letter-spacing: -0.02em;
		text-align: center;
	}

	footer {
		padding-top: 12px;
	}

	.puzzle-details {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 16px;
		margin-bottom: 12px;
	}

	.puzzle-details p {
		margin: 0;
		color: #666666;
		font-size: 0.9rem;
		text-transform: capitalize;
	}

	.puzzle-details strong {
		color: #191919;
	}

	.message {
		margin: 0;
		padding: 16px;
		border-radius: 6px;
		color: #8c281c;
		background: #fbe8e2;
		font-size: 0.9rem;
	}

	.download {
		display: block;
		width: fit-content;
		margin: 0 auto;
		color: #666666;
		font-size: 0.85rem;
		text-underline-offset: 3px;
	}

	.download:hover {
		color: #191919;
	}

	.download:focus-visible {
		outline: 2px solid #777777;
		outline-offset: 3px;
	}

	@media (max-width: 480px) {
		main {
			width: calc(100% - 24px);
			padding: 24px 0;
		}

		.puzzle-details {
			align-items: stretch;
			flex-direction: column;
		}
	}
</style>
