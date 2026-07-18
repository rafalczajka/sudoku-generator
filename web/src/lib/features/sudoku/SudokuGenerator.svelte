<script lang="ts">
	import { onMount } from 'svelte';

	import { warmUpApi } from '$lib/api/health';

	import { fetchSudoku } from './api';
	import SudokuBoard from './components/SudokuBoard.svelte';
	import SudokuControls from './components/SudokuControls.svelte';
	import SudokuFooter from './components/SudokuFooter.svelte';
	import type { Difficulty, Sudoku } from './types';

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

	function toggleSolution() {
		showSolution = !showSolution;
	}
</script>

<main>
	<section aria-label="Sudoku generator">
		<h1>Sudoku Generator</h1>
		<SudokuControls bind:level {loading} onGenerate={generateSudoku} />

		{#if error}
			<p class="message" role="alert">{error} Please try again.</p>
		{:else}
			<SudokuBoard {sudoku} {showSolution} />
		{/if}

		<SudokuFooter
			stats={sudoku && !error ? sudoku.stats : null}
			{showSolution}
			onToggleSolution={toggleSolution}
		/>
	</section>
</main>

<style>
	main {
		width: min(var(--content-width), calc(100% - var(--space-8)));
		margin: 0 auto;
		padding: var(--space-8) 0;
	}

	h1 {
		margin: 0 0 var(--space-5);
		font-size: var(--font-size-title);
		font-weight: var(--font-weight-bold);
		line-height: var(--line-height-title);
		letter-spacing: -0.02em;
		text-align: center;
	}

	.message {
		margin: 0;
		padding: var(--space-4);
		border-radius: var(--radius);
		color: var(--color-error);
		background: var(--color-error-surface);
		font-size: var(--font-size-small);
	}

	@media (max-width: 480px) {
		main {
			width: calc(100% - var(--space-6));
			padding: var(--space-6) 0;
		}
	}
</style>
