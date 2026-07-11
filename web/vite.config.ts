import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

const base = (process.env.BASE_PATH ?? '') as '' | `/${string}`;

export default defineConfig({
	server: {
		host: true,
		port: 5173,
		proxy: {
			'/api': {
				target: process.env.API_PROXY_TARGET ?? 'http://127.0.0.1:5000',
				changeOrigin: true
			}
		}
	},
	plugins: [
		sveltekit({
			paths: {
				base
			},
			compilerOptions: {
				// Force runes mode for the project, except for libraries. Can be removed in svelte 6.
				runes: ({ filename }) =>
					filename.split(/[/\\]/).includes('node_modules') ? undefined : true
			},

			adapter: adapter()
		})
	]
});
