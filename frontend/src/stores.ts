import { writable } from 'svelte/store';
import type { Book } from './types.d.ts';

export const isModalOpen = writable(false);
export const selectedBook = writable<Book | null>(null);
