<script lang="ts">

  import type { Book } from '$lib/types';


  export let book: Book;
  export let close: () => void; // Declara el evento 'close' como una función

</script>


<div class="modal-overlay" on:click|self={close} on:keydown={(e) => { if (e.key === 'Escape') close(); }} role="button" tabindex="0">
  <div class="modal-content" role="dialog" aria-modal="true" tabindex="-1">
    <button class="close-button" on:click={close}>X</button>
    {#if book}
      <div class="book-details-content">
        {#if book.cover_image}
          <img src={book.cover_image} alt={book.title} class="book-cover" />
        {/if}
        <h2>{book.title}</h2>
        <p><strong>Autor:</strong> {book.author ? book.author.name : 'Desconocido'}</p>
        <p><strong>Descripción:</strong> {book.description}</p>
        <p><strong>Género:</strong> {book.category ? book.category.name : 'Desconocido'}</p>
      </div>
    {:else}
      <p>No se ha seleccionado ningún libro.</p>
    {/if}
  </div>
</div>

<svelte:window on:keydown={(e) => e.key === 'Escape' && close()} />

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
    padding: 1.5rem; /* Reducir el padding */
    border-radius: 8px;
    position: relative;
    max-height: 90vh; /* Altura máxima para el popup */
    overflow-y: auto; /* Habilitar scroll vertical */

    max-width: 500px;
    width: 90%;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .book-details-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .book-cover {
    max-width: 150px;
    height: auto;
    border-radius: 4px;
    margin-bottom: 1rem;
  }

  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #333;
  }

  h2 {
    margin-top: 0;
    color: #333;
  }

  p {
    margin-bottom: 0.5rem;
    color: #555;
    font-size: 0.9rem; /* Reducir el tamaño de fuente de los párrafos */
  }

  strong {
    color: #000;
  }
</style>
