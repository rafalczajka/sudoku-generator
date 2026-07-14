<script lang="ts">
	import type { Snippet } from 'svelte';

	let {
		children,
		variant = 'secondary',
		disabled = false,
		onclick
	}: {
		children: Snippet;
		variant?: 'primary' | 'secondary';
		disabled?: boolean;
		onclick?: (event: MouseEvent) => void;
	} = $props();
</script>

<button type="button" class:primary={variant === 'primary'} {disabled} {onclick}>
	{@render children()}
</button>

<style>
	button {
		padding: 0 var(--space-4);
		background: transparent;
		font-weight: var(--font-weight-bold);
		transition: background var(--transition-fast);
	}

	button:hover:not(:disabled) {
		background: var(--color-hover);
	}

	.primary {
		width: 160px;
		border-color: var(--color-primary);
		color: var(--color-on-primary);
		background: var(--color-primary);
	}

	.primary:hover:not(:disabled) {
		background: var(--color-primary-hover);
	}

	@media (max-width: 480px) {
		.primary {
			width: 100%;
		}
	}
</style>
