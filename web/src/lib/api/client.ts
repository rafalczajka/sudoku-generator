import { env } from '$env/dynamic/public';

export function apiEndpoint(path: string): string {
	const apiUrl = (env.PUBLIC_API_URL ?? '').replace(/\/$/, '');
	return `${apiUrl}${path}`;
}
