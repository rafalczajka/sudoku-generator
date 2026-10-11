import { PUBLIC_API_URL } from '$app/env/public';

export function apiEndpoint(path: string): string {
	const apiUrl = PUBLIC_API_URL.replace(/\/$/, '');
	return `${apiUrl}${path}`;
}
