<script lang="ts">
	import { onMount } from 'svelte';
import type { Book, Category } from '$lib/types';
	import RecentBooks from '$lib/components/RecentBooks.svelte';
	import FilterSearch from '$lib/components/FilterSearch.svelte';
	import BookCatalog from '$lib/components/BookCatalog.svelte';

	let recentBooks: Book[] = [];
	let allBooks: Book[] = [];
	let categories: Category[] = [];

	let searchTerm = '';
	let selectedCategory = ''; // Store category ID

	const API_BASE_URL = 'http://localhost:8000'; // Your Django API base URL

	async function fetchRecentBooks() {
		try {
			const response = await fetch(`${API_BASE_URL}/api/books/?ordering=-created_at&limit=10`);
			if (!response.ok) throw new Error('Failed to fetch recent books');
			const data = await response.json();
			recentBooks = data.results ? data.results : data;
		} catch (error) {
			console.error('Error fetching recent books:', error);
		}
	}

	async function fetchAllBooks() {
		try {
			let url = `${API_BASE_URL}/api/books/?ordering=-created_at`;
			const params = new URLSearchParams();
			if (searchTerm) {
				params.append('search', searchTerm);
			}
			if (selectedCategory) {
				params.append('category', selectedCategory);
			}
			const queryString = params.toString();
			if (queryString) {
				url += `&${queryString}`;
			}
			const response = await fetch(url);
			if (!response.ok) throw new Error('Failed to fetch all books');
			const data = await response.json();
			allBooks = data.results ? data.results : data;
		} catch (error) {
			console.error('Error fetching all books:', error);
		}
	}

	async function fetchCategories() {
		try {
			const response = await fetch(`${API_BASE_URL}/api/categories/`);
			if (!response.ok) throw new Error('Failed to fetch categories');
			const data = await response.json();
			categories = data.results ? data.results : data;
		} catch (error) {
			console.error('Error fetching categories:', error);
		}
	}

	onMount(async () => {
		await fetchRecentBooks();
		await fetchAllBooks(); // Initial fetch for all books
		await fetchCategories();
	});

	// Handlers for FilterSearch component
	function handleSearch(term: string) {
		searchTerm = term;
		fetchAllBooks();
	}

	function handleCategoryChange(categoryId: string) {
		selectedCategory = categoryId;
		fetchAllBooks();
	}
</script>

<style>
	/* Light mode variables (default) */
	:root {
		--background-color: #fff;
		--text-color: #333;
		--card-background-color: #f9f9f9;
		--card-border-color: #ddd;
		--header-border-color: #eee;
		--input-background-color: #fff;
		--input-border-color: #ccc;
		--input-text-color: #333;
		--button-background-color: #eee;
		--button-text-color: #333;
	}

	/* Dark mode variables */
	:global(html.dark) {
		--background-color: #1a1a1a;
		--text-color: #f0f0f0;
		--card-background-color: #2a2a2a;
		--card-border-color: #444;
		--header-border-color: #333;
		--input-background-color: #2a2a2a;
		--input-border-color: #444;
		--input-text-color: #f0f0f0;
		--button-background-color: #333;
		--button-text-color: #f0f0f0;
	}

	.container {
		padding: 2rem;
		background-color: var(--background-color);
		color: var(--text-color);
		min-height: 100vh; /* Ensure it takes full viewport height */
	}

	section {
		margin-bottom: 3rem;
	}

	h2 {
		margin-bottom: 1rem;
		border-bottom: 2px solid var(--header-border-color);
		padding-bottom: 0.5rem;
		color: var(--text-color);
	}
</style>

<div class="container">
	<RecentBooks recentBooks={recentBooks} />
	<FilterSearch
		bind:searchTerm={searchTerm}
		bind:selectedCategory={selectedCategory}
		categories={categories}
		onSearch={handleSearch}
		onCategoryChange={handleCategoryChange}
	/>
	<BookCatalog
		allBooks={allBooks}
		searchTerm={searchTerm}
		selectedCategory={selectedCategory}
	/>
</div>
