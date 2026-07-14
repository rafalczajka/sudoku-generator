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
		margin-bottom: var(--space-5);
	}

	label {
		display: block;
		margin-bottom: var(--space-2);
		font-size: var(--font-size-small);
		font-weight: var(--font-weight-bold);
	}

	.actions {
		display: grid;
		grid-template-columns: 1fr auto;
		gap: var(--space-3);
	}

	select {
		width: 100%;
		padding: 0 var(--space-10) 0 var(--space-4);
		background: var(--color-surface);
	}

	@media (max-width: 480px) {
		.actions {
			grid-template-columns: 1fr;
		}
	}
</style>
