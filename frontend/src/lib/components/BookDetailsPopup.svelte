<script lang="ts">

  import type { Book } from '$lib/types';

  export let book: Book;
  export let close: () => void; // Declara el evento 'close' como una función

</script>


<div class="modal-overlay" on:click|self={close} on:keydown={(e) => { if (e.key === 'Escape') close(); }} role="button" tabindex="0">
  <div class="modal-content" role="dialog" aria-modal="true" tabindex="-1">
    {#if book}
      <!-- Close Button -->
      <button class="close-button" on:click={close} aria-label="Cerrar modal">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      
      <!-- Header Section with Background Gradient -->
      <div class="modal-header">
        <div class="header-background"></div>
        <div class="header-content">
          <div class="book-cover-container">
            {#if book.cover_image}
              <div class="cover-wrapper">
                <img src={book.cover_image} alt={book.title} class="book-cover" />
                <div class="cover-glow"></div>
              </div>
            {:else}
              <div class="cover-placeholder">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 19.5A2.5 2.5 0 0 0 6.5 22h11A2.5 2.5 0 0 0 20 19.5v-15A2.5 2.5 0 0 0 17.5 2h-11A2.5 2.5 0 0 0 4 4.5v15Z" fill="currentColor" opacity="0.1"/>
                  <path d="M4 19.5A2.5 2.5 0 0 0 6.5 22h11A2.5 2.5 0 0 0 20 19.5v-15A2.5 2.5 0 0 0 17.5 2h-11A2.5 2.5 0 0 0 4 4.5v15Z" stroke="currentColor" stroke-width="2"/>
                </svg>
              </div>
            {/if}
          </div>
          <div class="book-title-section">
            <h1 class="book-title">{book.title}</h1>
            <div class="book-subtitle">
              <span class="author-badge">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2"/>
                </svg>
                {book.author ? book.author.name : 'Autor desconocido'}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Section -->
      <div class="modal-body">
        <div class="info-grid">
          <div class="info-card">
            <div class="info-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M4 6h16M4 12h16M4 18h7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="info-content">
              <span class="info-label">Género</span>
              <span class="info-value">{book.category ? book.category.name : 'No especificado'}</span>
            </div>
          </div>
          
          <div class="info-card">
            <div class="info-icon price-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="info-content">
              <span class="info-label">Precio</span>
              <span class="info-value price">${book.price || 'Consultar'}</span>
            </div>
          </div>
        </div>        {#if book.description}
          <div class="description-section">
            <h3 class="section-title">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <polyline points="14,2 14,8 20,8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="16" y1="13" x2="8" y2="13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="16" y1="17" x2="8" y2="17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <polyline points="10,9 9,9 8,9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Descripción
            </h3>
            <div class="description-content">
              <p>{book.description}</p>
            </div>
          </div>
        {/if}
      </div>
    {:else}
      <div class="empty-state">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="none">
          <path d="M4 19.5A2.5 2.5 0 0 0 6.5 22h11A2.5 2.5 0 0 0 20 19.5v-15A2.5 2.5 0 0 0 17.5 2h-11A2.5 2.5 0 0 0 4 4.5v15Z" stroke="currentColor" stroke-width="2"/>
          <path d="M8 7h8M8 12h6M8 17h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <p>No se ha seleccionado ningún libro</p>
      </div>
    {/if}
  </div>
</div>

<svelte:window on:keydown={(e) => e.key === 'Escape' && close()} />

<style>  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--modal-overlay);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    backdrop-filter: blur(12px);
    animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    padding: 20px;
  }

  .modal-content {
    background: var(--modal-background);
    border-radius: 24px;
    box-shadow: 
      0 20px 60px var(--shadow-color),
      0 0 0 1px var(--border-color);
    width: 100%;
    max-width: 800px;
    max-height: 90vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transform: scale(0.9) translateY(20px);
    animation: modalEnter 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    position: relative;
    color: var(--text-color);
    border: 1px solid var(--border-color);
  }

  .close-button {
    position: absolute;
    top: 20px;
    right: 20px;
    background: var(--card-background-color);
    backdrop-filter: blur(10px);
    border: 2px solid var(--border-color);
    width: 44px;
    height: 44px;
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--light-text-color);
    box-shadow: 0 4px 20px var(--shadow-color);
  }

  .close-button:hover {
    background: var(--secondary-color);
    transform: scale(1.1);
    color: var(--text-color);
    box-shadow: 0 8px 30px var(--shadow-color);
  }  .modal-header {
    position: relative;
    padding: 40px;
    background: linear-gradient(135deg, 
      var(--modal-background) 0%, 
      var(--card-background-color) 100%);
    border-bottom: 1px solid var(--border-color);
    color: var(--text-color);
    overflow: hidden;
  }

  .header-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
      radial-gradient(circle at 20% 30%, var(--shadow-color) 0%, transparent 50%),
      radial-gradient(circle at 80% 70%, var(--shadow-color) 0%, transparent 50%);
  }

  .header-content {
    position: relative;
    z-index: 2;
    display: flex;
    align-items: flex-start;
    gap: 24px;
  }

  .book-cover-container {
    flex-shrink: 0;
    position: relative;
  }

  .cover-wrapper {
    position: relative;
    display: block;
  }  .book-cover {
    width: 120px;
    height: 180px;
    object-fit: cover;
    border-radius: 16px;
    box-shadow: 
      0 20px 40px var(--shadow-color),
      0 0 0 1px var(--border-color);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .book-cover:hover {
    transform: scale(1.05) rotateY(5deg);
  }
  .cover-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, var(--shadow-color), transparent);
    border-radius: 16px;
    pointer-events: none;
  }
  .cover-placeholder {
    width: 120px;
    height: 180px;
    background: var(--surface-2);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--light-text-color);
    border: 2px dashed var(--light-text-color);
    opacity: 0.6;
  }

  .book-title-section {
    flex: 1;
    min-width: 0;
  }  .book-title {
    font-size: 2rem;
    font-weight: 800;
    margin: 0 0 12px 0;
    line-height: 1.1;
    color: var(--text-color);
    text-shadow: none;
  }

  .book-subtitle {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 16px;
  }
  .author-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--card-background-color);
    border: 2px solid var(--border-color);
    padding: 8px 16px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--text-color);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .author-badge:hover {
    background: var(--surface-2);
    transform: translateY(-1px);
  }
  .modal-body {
    padding: 40px;
    overflow-y: auto;
    flex: 1;
    padding-bottom: 40px; /* Extra padding at bottom since no footer */
  }

  .info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 32px;
  }
  .info-card {
    background: var(--card-background-color);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
  }  .info-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--light-text-color), var(--border-color));
    transform: scaleX(0);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .info-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px var(--shadow-color);
  }

  .info-card:hover::before {
    transform: scaleX(1);
  }
  .info-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, var(--light-text-color), var(--border-color));
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    flex-shrink: 0;
  }
  .price-icon {
    background: linear-gradient(135deg, var(--price-color), var(--success-color));
  }

  .info-content {
    flex: 1;
    min-width: 0;
  }
  .info-label {
    display: block;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--light-text-color);
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .info-value {
    display: block;
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--text-color);
  }
  .price {
    color: var(--price-color);
    font-weight: 700;
  }
  .description-section {
    background: var(--card-background-color);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    padding: 28px;
    margin-top: 24px;
  }

  .section-title {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-color);
    margin: 0 0 20px 0;
    padding-bottom: 12px;
    border-bottom: 2px solid var(--border-color);
  }

  .description-content {
    line-height: 1.7;
    color: var(--text-color);
  }
  .description-content p {
    margin: 0;
    font-size: 1rem;
  }
  .empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 60px 40px;
    text-align: center;
    color: var(--light-text-color);
  }

  .empty-state svg {
    margin-bottom: 20px;
    opacity: 0.5;
  }

  .empty-state p {
    font-size: 1.125rem;
    margin: 0;
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes modalEnter {
    from { 
      transform: scale(0.9) translateY(20px); 
      opacity: 0; 
    }
    to { 
      transform: scale(1) translateY(0); 
      opacity: 1; 
    }
  }
  /* Responsive Design */
  @media (max-width: 768px) {
    .modal-overlay {
      padding: 10px;
    }

    .modal-content {
      border-radius: 20px;
      max-height: 95vh;
    }

    .modal-header {
      padding: 24px 20px;
    }

    .header-content {
      flex-direction: column;
      text-align: center;
      gap: 20px;
    }

    .book-title {
      font-size: 1.5rem;
    }

    .modal-body {
      padding: 24px 20px 32px 20px; /* Adjusted bottom padding */
    }

    .info-grid {
      grid-template-columns: 1fr;
      gap: 16px;
    }
  }

  @media (max-width: 480px) {
    .book-cover {
      width: 100px;
      height: 150px;
    }

    .cover-placeholder {
      width: 100px;
      height: 150px;
    }

    .close-button {
      top: 15px;
      right: 15px;
      width: 36px;
      height: 36px;
    }
  }
</style>
