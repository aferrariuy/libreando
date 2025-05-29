<script lang="ts">

    import type { Book } from '$lib/types';
    import BookDetailsPopup from '$lib/components/BookDetailsPopup.svelte';    export let allBooks: Book[];
    export let searchTerm: string;
    export let selectedCategory: string;

    let showPopup: boolean = false;
    let selectedBook: Book | null = null;

    function openBookDetails(book: Book) {
        selectedBook = book;
        showPopup = true;
    }

    function closeBookDetails() {
        showPopup = false;
        selectedBook = null;
    }
</script>

<style>
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
</style>

<section id="catalog">
    <h2>Catálogo de Libros</h2>
    {#if allBooks.length > 0}
        <div class="book-catalog">
            {#each allBooks as book (book.id)}

                <button class="book-card" on:click={() => openBookDetails(book)}>
                    <img src="{book.cover_image}" alt="{book.title}" />
                    <h3>{book.title}</h3>
                    <p>Autor: {book.author.name}</p>
                    <p>Precio: ${book.price}</p>
                </button>
            {/each}
        </div>
    {:else if searchTerm || selectedCategory}
        <p>No se encontraron libros con los criterios seleccionados.</p>
    {:else}
        <p>Cargando catálogo de libros...</p>
    {/if}

</section>

{#if showPopup && selectedBook}
    <BookDetailsPopup book={selectedBook} close={closeBookDetails} />
{/if}
