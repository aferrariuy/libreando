<script lang="ts">
    import { isModalOpen, selectedBook } from './stores.ts';
    import type { Book } from './types.d.ts';

    let book: Book | null;

    selectedBook.subscribe(value => {
        book = value;
    });

    function closeModal() {
        isModalOpen.set(false);
        selectedBook.set(null); // Clear selected book when closing
    }
</script>

{#if $isModalOpen && book}
    <div class="modal-overlay" on:click={closeModal}>
        <div class="modal-content" on:click|stopPropagation>
            <button class="close-button" on:click={closeModal}>&times;</button>
            <h2>{book.title}</h2>
            <p><strong>Author:</strong> {book.author.name}</p>
            <p><strong>Category:</strong> {book.category.name}</p>
            <p><strong>Price:</strong> ${book.price}</p>
            <img src={book.cover_image} alt={book.title} class="modal-image" />
            <p>{book.description}</p>
        </div>
    </div>
{/if}

<style>
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }

    .modal-content {
        background: white;
        padding: 2em;
        border-radius: 8px;
        max-width: 600px;
        width: 90%;
        position: relative;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        max-height: 90vh;
        overflow-y: auto;
    }

    .close-button {
        position: absolute;
        top: 10px;
        right: 10px;
        background: none;
        border: none;
        font-size: 1.5em;
        cursor: pointer;
        color: #333;
    }

    .modal-image {
        max-width: 100%;
        height: auto;
        margin-top: 1em;
        border-radius: 4px;
    }

    h2 {
        margin-top: 0;
        color: #333;
    }

    p {
        color: #555;
        line-height: 1.6;
    }
</style>
