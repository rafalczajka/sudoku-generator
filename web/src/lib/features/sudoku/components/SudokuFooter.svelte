<script lang="ts">
	import { asset } from '$app/paths';

	import Button from '$lib/components/Button.svelte';

	import type { SudokuStats } from '../types';

	let {
		stats,
		showSolution,
		onToggleSolution
	}: {
		stats: SudokuStats | null;
		showSolution: boolean;
		onToggleSolution: () => void;
	} = $props();
</script>

<footer>
	{#if stats}
		<div class="puzzle-details">
			<p><strong>{stats.level}</strong> · {stats.clues} clues</p>
			<Button onclick={onToggleSolution}>
				{showSolution ? 'Hide solution' : 'Show solution'}
			</Button>
		</div>
	{/if}

	<a class="download" href={asset('/printable-grid-6.pdf')} download>
		Download printable grids (PDF)
	</a>
</footer>

<style>
	footer {
		display: flex;
		align-items: center;
		flex-direction: column;
		padding-top: var(--space-3);
	}

	.puzzle-details {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
		gap: var(--space-4);
		margin-bottom: var(--space-3);
	}

	.puzzle-details p {
		margin: 0;
		color: var(--color-text-muted);
		font-size: var(--font-size-small);
		text-transform: capitalize;
	}

	.puzzle-details strong {
		color: var(--color-text);
	}

	.download {
		display: inline-flex;
		align-items: center;
		width: fit-content;
		min-height: var(--space-8);
		margin: 0 auto;
		padding: 0 var(--space-2);
		color: var(--color-text-muted);
		font-size: var(--font-size-small);
		text-underline-offset: 3px;
	}

	.download:hover {
		color: var(--color-text);
	}

	@media (max-width: 480px) {
		.puzzle-details {
			align-items: stretch;
			flex-direction: column;
		}
	}
</style>
