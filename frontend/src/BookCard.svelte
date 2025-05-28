<script lang="ts">
    import { isModalOpen, selectedBook } from './stores.ts';
    import type { Book } from './types.d.ts';

    export let book: Book;

    function openModal() {
        selectedBook.set(book);
        isModalOpen.set(true);
    }
</script>

<div class="book-card" on:click={openModal}>
    <img src={book.cover_image} alt={book.title} />
    <h3>{book.title}</h3>
    <p>by {book.author.name}</p>
    <p>${book.price}</p>
</div>

<style>
    .book-card {
        border: 1px solid #ddd;
        padding: 1em;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        border-radius: 8px;
    }

    .book-card img {
        max-width: 100%;
        height: auto;
        margin-bottom: 0.5em;
        border-radius: 4px;
    }

    .book-card h3 {
        font-size: 1.2em;
        margin: 0.5em 0;
        color: #333;
    }

    .book-card p {
        font-size: 0.9em;
        color: #666;
        margin: 0.2em 0;
    }
</style>
