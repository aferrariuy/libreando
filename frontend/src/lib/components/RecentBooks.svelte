<script lang="ts">

    import type { Book } from '$lib/types';
    import { onDestroy } from 'svelte';
    import BookDetailsPopup from '$lib/components/BookDetailsPopup.svelte';

    export let recentBooks: Book[];

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

    let carouselElement: HTMLElement;
    let showLeftGradient = false;
    let showRightGradient = false;

    function updateGradientVisibility() {
        if (!carouselElement) return;

        const { scrollWidth, clientWidth, scrollLeft } = carouselElement;

        const canScrollLeft = scrollLeft > 16;
        const canScrollRight = scrollLeft + clientWidth < scrollWidth;

        showLeftGradient = canScrollLeft;
        showRightGradient = canScrollRight;
    }

    function scrollCarousel(direction: 'prev' | 'next') {
        if (!carouselElement) return;

        const scrollAmount = carouselElement.clientWidth;

        if (direction === 'prev') {
            carouselElement.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        } else {
            carouselElement.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
    }

    $: if (carouselElement) {
        carouselElement.addEventListener('scroll', updateGradientVisibility);
        updateGradientVisibility();
    }

    onDestroy(() => {
        if (carouselElement) {
            carouselElement.removeEventListener('scroll', updateGradientVisibility);
        }
    });
</script>

<style>
    .carousel-container {
        position: relative;
        width: 100%;
        overflow: hidden;
    }

    .carousel-container::before,
    .carousel-container::after {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        width: var(--gradient-width);
        pointer-events: none;
        z-index: 5;
        opacity: 0;
        transition: opacity var(--transition-duration) var(--transition-timing-function);
    }

    .carousel-container::before {
        left: 0;
        background: radial-gradient(ellipse 50% 100% at left, var(--card-background-color) 0%, transparent 70%);
    }

    .carousel-container::after {
        right: 0;
        background: radial-gradient(ellipse 50% 100% at right, var(--card-background-color) 0%, transparent 70%);
    }

    .carousel-container.show-left-gradient::before {
        opacity: 1;
    }

    .carousel-container.show-right-gradient::after {
        opacity: 1;
    }

    .carousel-button {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background-color: var(--button-bg-color);
        color: var(--button-text-color);
        border: none;
        padding: var(--size-2);
        cursor: pointer;
        z-index: 10;
        border-radius: var(--radius-button);
        width: var(--button-size);
        height: var(--button-size);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: var(--button-font-size);
        line-height: 1;
        transition: background-color var(--transition-duration) var(--transition-timing-function);
    }

    .carousel-button:hover {
        background-color: var(--button-hover-bg-color);
    }

    .carousel-button.prev {
        left: var(--carousel-padding-inline);
    }

    .carousel-button.next {
        right: var(--carousel-padding-inline);
    }

    .carousel {
        width: 100%;
        display: flex;
        gap: var(--size-4);
        padding-block: var(--size-2);
        padding-inline: var(--carousel-padding-inline);
        overflow-x: scroll;
        scroll-snap-type: x mandatory;
        scroll-behavior: smooth;
        -webkit-overflow-scrolling: touch;
        overscroll-behavior-x: contain;
        scroll-padding-inline: var(--carousel-padding-inline);

        /* Hide scrollbar */
        &::-webkit-scrollbar {
            display: none;
        }
        -ms-overflow-style: none;
        scrollbar-width: none;
    }

    .carousel::before,
    .carousel::after {
        content: '';
        display: block;
        flex-shrink: 0;
        width: 0;
    }

    .carousel__slide {
        flex: 0 0 auto;
        width: var(--size-content-1);
        background: var(--card-background-color);
        padding: var(--size-2);
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        aspect-ratio: var(--ratio-portrait);
        border: 1px solid var(--surface-3);
        box-shadow: var(--shadow-2);
        border-radius: var(--radius-2);
        transition: transform var(--transition-duration) var(--transition-timing-function),
                    opacity var(--transition-duration) var(--transition-timing-function);
        scroll-snap-align: start;
    }

    .carousel__slide:hover {
        transform: translateY(-5px);
    }

    .carousel__slide img {
        max-width: 100%;
        height: var(--size-content-1);
        object-fit: cover;
        margin-bottom: var(--size-2);
        border-radius: var(--radius-image);
    }
    
    .carousel__slide h3 {
        font-size: var(--font-size-base);
        margin-bottom: calc(var(--size-2) / 2);
        color: var(--text-color);
    }
    
    .carousel__slide p {
        font-size: var(--font-size-small);
        color: var(--light-text-color);
    }
</style>

<section id="recent-books">
    <h2>Añadidos Recientemente</h2>
    {#if recentBooks.length > 0}

        <div class="carousel-container" class:show-left-gradient={showLeftGradient} class:show-right-gradient={showRightGradient}>
            <button
                class="carousel-button prev"
                on:click={() => scrollCarousel('prev')}
                aria-label="Previous set of books"
            >
                &lt;
            </button>
            <div class="carousel" aria-live="polite" bind:this={carouselElement}>
                {#each recentBooks as book (book.id)}

                    <button class="carousel__slide" tabindex="0" data-label="Book {book.id}" on:click={() => openBookDetails(book)}>
                        <img src="{book.cover_image}" alt="{book.title}" />
                        <h3>{book.title}</h3>
                        <p>{book.author.name}</p>
                    </button>
                {/each}
            </div>
            <button
                class="carousel-button next"
                on:click={() => scrollCarousel('next')}
                aria-label="Next set of books"
            >
                &gt;
            </button>
        </div>
    {:else}
        <p>Cargando libros recientes...</p>
    {/if}

</section>

{#if showPopup && selectedBook}
    <BookDetailsPopup book={selectedBook} close={closeBookDetails} />
{/if}
