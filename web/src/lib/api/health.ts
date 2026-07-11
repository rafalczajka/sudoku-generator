import { apiEndpoint } from './client';

export function warmUpApi(): void {
	void fetch(apiEndpoint('/api/health')).catch(() => undefined);
}
