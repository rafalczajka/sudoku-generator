<script lang="ts">
	import Button from '$lib/components/Button.svelte';

	import type { Difficulty } from '../types';

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
		<Button variant="primary" onclick={onGenerate} disabled={loading}>
			{loading ? 'Generating…' : 'Generate'}
		</Button>
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

	select {
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

	select:focus-visible {
		outline: 2px solid #777777;
		outline-offset: 2px;
	}

	select:disabled {
		cursor: wait;
		opacity: 0.65;
	}

	@media (max-width: 480px) {
		.actions {
			grid-template-columns: 1fr;
		}
	}
</style>
