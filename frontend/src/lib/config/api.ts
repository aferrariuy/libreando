import { env } from '$env/dynamic/public';

// Use the environment variable or fallback to localhost for development
export const API_BASE_URL = env.PUBLIC_API_BASE_URL || 'http://localhost:8000';

// Export API endpoints
export const API_ENDPOINTS = {
  books: `${API_BASE_URL}/api/books/`,
  categories: `${API_BASE_URL}/api/categories/`,
  authors: `${API_BASE_URL}/api/authors/`,
} as const;
