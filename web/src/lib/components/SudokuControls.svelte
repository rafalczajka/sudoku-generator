<script lang="ts">
	import type { Difficulty } from '$lib/types/sudoku';

	const levels: { value: Difficulty; label: string }[] = [
		{ value: 'easy', label: 'Easy' },
		{ value: 'medium', label: 'Medium' },
		{ value: 'hard', label: 'Hard' },
		{ value: 'expert', label: 'Expert' }
	];

	let {
		level = $bindable(),
		loading,
		onGenerate
	}: {
		level: Difficulty;
		loading: boolean;
		onGenerate: () => void;
	} = $props();
</script>

<div class="controls">
	<label for="difficulty">Difficulty</label>
	<div class="actions">
		<select id="difficulty" bind:value={level} disabled={loading}>
			{#each levels as option (option.value)}
				<option value={option.value}>{option.label}</option>
			{/each}
		</select>
		<button onclick={onGenerate} disabled={loading}>
			{loading ? 'Generating…' : 'Generate'}
		</button>
	</div>
</div>

<style>
	.controls {
		margin-bottom: 20px;
	}

	label {
		display: block;
		margin-bottom: 9px;
		font-size: 0.8rem;
		font-weight: 700;
	}

	.actions {
		display: grid;
		grid-template-columns: 1fr auto;
		gap: 10px;
	}

	select,
	button {
		min-height: 46px;
		border-radius: 6px;
	}

	select {
		width: 100%;
		padding: 0 38px 0 14px;
		border: 1px solid #cccccc;
		color: #191919;
		background: #ffffff;
		cursor: pointer;
	}

	button {
		width: 160px;
		border: 0;
		padding: 0 18px;
		color: #ffffff;
		background: #191919;
		font-weight: 700;
		cursor: pointer;
		transition: background 120ms ease;
	}

	button:hover:not(:disabled) {
		background: #3b3b3b;
	}

	button:focus-visible,
	select:focus-visible {
		outline: 2px solid #777777;
		outline-offset: 2px;
	}

	button:disabled,
	select:disabled {
		cursor: wait;
		opacity: 0.65;
	}

	@media (max-width: 480px) {
		.actions {
			grid-template-columns: 1fr;
		}

		button {
			width: 100%;
		}
	}
</style>
