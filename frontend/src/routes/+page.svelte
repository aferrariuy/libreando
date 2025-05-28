<script lang="ts">
	import { onMount } from 'svelte';

	interface Author {
		id: number;
		name: string;
	}

	interface Category {
		id: number;
		name: string;
	}

	interface Book {
		id: number;
		title: string;
		author: Author;
		category: Category;
		price: string;
		description: string;
		cover_image: string; // URL from Cloudinary
		created_at: string;
	}

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
			// The API might return paginated results, ensure you get the actual book list
			recentBooks = data.results ? data.results : data;
		} catch (error) {
			console.error('Error fetching recent books:', error);
			// Handle error appropriately in UI, e.g., show a message
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

	// Reactive statement to refetch allBooks when searchTerm or selectedCategory changes
	$: if (searchTerm || selectedCategory) {
		fetchAllBooks();
	} else if (searchTerm === '' && selectedCategory === '') {
        // Refetch all books if filters are cleared
        fetchAllBooks();
    }

	// No longer need filteredBooks, as filtering is done by the API
	// $: filteredBooks = allBooks.filter(book => { ... });
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

	.carousel {
		display: flex;
		overflow-x: auto;
		gap: 1rem;
		padding-bottom: 1rem; /* For scrollbar visibility */
	}

	.carousel-item {
		flex: 0 0 auto; /* Prevent items from shrinking */
		width: 150px; /* Adjust as needed */
		border: 1px solid var(--card-border-color);
		background-color: var(--card-background-color);
		padding: 0.5rem;
		text-align: center;
		border-radius: 4px;
	}

	.carousel-item img {
		max-width: 100%;
		height: auto;
		margin-bottom: 0.5rem;
	}
	.carousel-item h3, .carousel-item p {
		color: var(--text-color);
	}

	.search-filter-area {
		display: flex;
		gap: 1rem;
		margin-bottom: 1rem;
		align-items: center;
	}

	.search-filter-area input,
	.search-filter-area select {
		padding: 0.5rem;
		border: 1px solid var(--input-border-color);
		background-color: var(--input-background-color);
		color: var(--input-text-color);
		border-radius: 4px;
	}

	.search-filter-area input::placeholder {
		color: var(--text-color);
		opacity: 0.7;
	}


	.book-catalog {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
		gap: 1.5rem;
	}

	.book-card {
		border: 1px solid var(--card-border-color);
		background-color: var(--card-background-color);
		padding: 1rem;
		border-radius: 4px;
	}

	.book-card img {
		max-width: 100%;
		height: auto;
		margin-bottom: 0.5rem;
		border-bottom: 1px solid var(--header-border-color);
		padding-bottom: 0.5rem;
	}

	.book-card h3 {
		margin-bottom: 0.25rem;
		font-size: 1.1em;
		color: var(--text-color);
	}

	.book-card p {
		margin-bottom: 0.25rem;
		font-size: 0.9em;
		color: var(--text-color);
		opacity: 0.8;
	}
	/* Ensure paragraphs inside sections also get the correct text color */
	section p {
		color: var(--text-color);
	}
</style>

<div class="container">
	<!-- Sección de Libros Añadidos Recientemente -->
	<section id="recent-books">
		<h2>Añadidos Recientemente</h2>
		{#if recentBooks.length > 0}
			<div class="carousel">
				{#each recentBooks as book (book.id)}
					<div class="carousel-item">
						<img src="{book.cover_image}" alt="{book.title}" />
						<h3>{book.title}</h3>
						<p>{book.author.name}</p>
					</div>
				{/each}
			</div>
		{:else}
			<p>Cargando libros recientes...</p>
		{/if}
	</section>

	<!-- Área de Búsqueda y Filtro -->
	<section id="search-filter">
		<h2>Buscar y Filtrar</h2>
		<div class="search-filter-area">
			<input type="text" placeholder="Buscar por título o autor..." bind:value={searchTerm} />
			<select bind:value={selectedCategory}>
				<option value="">Todas las categorías</option>
				{#each categories as category (category.id)}
					<option value="{category.id}">{category.name}</option>
				{/each}
			</select>
		</div>
	</section>

	<!-- Catálogo Completo de Libros -->
	<section id="catalog">
		<h2>Catálogo de Libros</h2>
		{#if allBooks.length > 0}
			<div class="book-catalog">
				{#each allBooks as book (book.id)}
					<div class="book-card">
						<img src="{book.cover_image}" alt="{book.title}" />
						<h3>{book.title}</h3>
						<p>Autor: {book.author.name}</p>
						<p>Precio: ${book.price}</p>
					</div>
				{/each}
			</div>
		{:else if searchTerm || selectedCategory}
			<p>No se encontraron libros con los criterios seleccionados.</p>
		{:else}
			<p>Cargando catálogo de libros...</p>
		{/if}
	</section>
</div>

<!-- filepath: c:\Users\Alien\Documents\DEV\libreando\libreando\frontend\src\routes\+page.svelte -->
<!-- <h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p> -->
