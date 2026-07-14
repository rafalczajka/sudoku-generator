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
	<section class="workspace" aria-label="Sudoku generator">
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
	}
</style>
