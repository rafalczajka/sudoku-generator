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
		min-height: 46px;
		border: 1px solid #cccccc;
		border-radius: 6px;
		padding: 0 18px;
		color: #191919;
		background: transparent;
		font-weight: 700;
		cursor: pointer;
		transition: background 120ms ease;
	}

	button:hover:not(:disabled) {
		background: #f4f4f4;
	}

	button:focus-visible {
		outline: 2px solid #777777;
		outline-offset: 2px;
	}

	button:disabled {
		cursor: wait;
		opacity: 0.65;
	}

	.primary {
		width: 160px;
		border-color: #191919;
		color: #ffffff;
		background: #191919;
	}

	.primary:hover:not(:disabled) {
		background: #3b3b3b;
	}

	@media (max-width: 480px) {
		.primary {
			width: 100%;
		}
	}
</style>
