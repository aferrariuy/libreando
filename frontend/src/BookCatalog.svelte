<script lang="ts">
    import { onMount } from 'svelte';
    import BookCard from './BookCard.svelte';
    import SearchBar from './SearchBar.svelte';
    import FilterDropdown from './FilterDropdown.svelte';
    import BookDetailModal from './BookDetailModal.svelte';
    import { isModalOpen, selectedBook } from './stores.ts';
    import type { Book } from './types.d.ts';

    let books: Book[] = [];
    let loading = true;
    let error: string | null = null;
    let searchTerm = '';
    let previousSearchTerm = ''; // Track previous search term
    let selectedCategory = '';
    let previousSelectedCategory = ''; // Track previous selected category

    let isFetching = false; // Add a flag to prevent re-entry

    async function fetchBooks() {
        if (isFetching) return; // If already fetching, do nothing
        isFetching = true; // Set flag to true

        loading = true;
        error = null;
        try {
            let url = new URL('/api/books/', window.location.origin);
            if (searchTerm) {
                url.searchParams.append('search', searchTerm);
            }
            if (selectedCategory) {
                url.searchParams.append('category__name', selectedCategory);
            }
            const response = await fetch(url.toString());
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            books = await response.json();
        } catch (e: unknown) {
            if (e instanceof Error) {
                error = e.message;
            } else {
                error = 'An unknown error occurred';
            }
        } finally {
            loading = false;
            isFetching = false; // Reset flag
        }
    }

    onMount(fetchBooks); // Enable initial fetch

    // Only fetch when searchTerm or selectedCategory changes
    $: if ((searchTerm !== previousSearchTerm || selectedCategory !== previousSelectedCategory) && !loading && !isFetching) {
        previousSearchTerm = searchTerm;
        previousSelectedCategory = selectedCategory;
        fetchBooks();
    }

</script>

<div class="controls">
    <SearchBar on:search={e => { searchTerm = e.detail; /* fetchBooks(); */ }} />
    <FilterDropdown on:filter={e => { selectedCategory = e.detail; /* fetchBooks(); */ }} />
</div>

<div class="book-catalog">
    {#if loading}
        <p>Loading books...</p>
    {:else if error}
        <p class="error">Error: {error}</p>
    {:else if books.length === 0}
        <p>No books found matching your criteria.</p>
    {:else}
        {#each books as book (book.id)}
            <BookCard {book} />
        {/each}
    {/if}
</div>

<BookDetailModal />

<style>
    .controls {
        display: flex;
        gap: 1em;
        margin-bottom: 1em;
        padding: 1em;
        max-width: 1200px;
        margin: 0 auto 1em auto;
    }
    .controls > :first-child {
        flex-grow: 1;
    }

    .book-catalog {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 1em;
        padding: 1em;
    }

    .error {
        color: red;
    }
</style>
