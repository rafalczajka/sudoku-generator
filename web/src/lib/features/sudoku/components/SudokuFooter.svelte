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
		.puzzle-details {
			align-items: stretch;
			flex-direction: column;
		}
	}
</style>
