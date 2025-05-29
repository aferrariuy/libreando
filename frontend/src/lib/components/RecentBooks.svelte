<script lang="ts">
    console.log('RecentBooks.svelte script loaded');
    import type { Book } from '$lib/types';
    import { onMount } from 'svelte';

    export let recentBooks: Book[];

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

        const scrollAmount = carouselElement.clientWidth; // Scroll by the visible width of the carousel

        if (direction === 'prev') {
            carouselElement.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        } else {
            carouselElement.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
        // The 'scroll' event listener on carouselElement will handle updating gradients
    }

    onMount(() => {
        console.log('onMount: carouselElement', carouselElement);
        if (carouselElement) {
            carouselElement.addEventListener('scroll', updateGradientVisibility);
            // Initial check
            updateGradientVisibility();
        } else {
            console.log('onMount: carouselElement is undefined, retrying after a short delay');
            // Fallback if carouselElement is not immediately available
            setTimeout(() => {
                if (carouselElement) {
                    carouselElement.addEventListener('scroll', updateGradientVisibility);
                    updateGradientVisibility();
                } else {
                    console.error('carouselElement is still undefined after retry');
                }
            }, 100); // Retry after 100ms
        }
    });
</script>

<style>
    :root {
        --size-content-1: 12.5rem;
        --size-4: 1rem;
        --size-2: 0.5rem;
        --ratio-portrait: 3/4;
        --gradient-width: 62.5rem;
        --carousel-padding-inline: 0.625rem;
        --button-size: 2.5rem;
        --button-font-size: 1.5rem;

        --surface-2: #f0f0f0;
        --surface-3: #ccc;
        --card-border-color: #ddd;
        --card-background-color: #fff;

        --shadow-2: 0 3px 6px rgba(0,0,0,0.16);
        --radius-2: 8px;
        --radius-button: 50%;
        --radius-image: 4px;

        --font-antique: 'Georgia', serif;
        --font-size-base: 1.1rem;
        --font-size-small: 0.9rem;
        --text-color: #333;
        --text-color-light: #666;
        --link-color: blue;

        --transition-duration: 0.3s;
        --transition-timing-function: ease-in-out;
        --ease-spring-4: cubic-bezier(0.175, 0.885, 0.32, 1.275);

        --button-bg-color: rgba(173, 173, 173, 0.5);
        --button-hover-bg-color: rgba(0, 0, 0, 0.8);
        --button-text-color: white;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --surface-2: #333;
            --surface-3: #555;
            --card-border-color: #555;
            --card-background-color: #222;
            --text-color: #eee;
            --text-color-light: #bbb;
        }
    }

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
        padding: var(--size-2); /* Usar variable para padding */
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
        padding-inline: var(--carousel-padding-inline); /* Añadir padding horizontal para el scroll-padding */
        overflow-x: scroll;
        scroll-snap-type: x mandatory;
        scroll-behavior: smooth;
        -webkit-overflow-scrolling: touch;
        overscroll-behavior-x: contain;
        scroll-padding-inline: var(--carousel-padding-inline); /* Asegura que el snap se alinee con el padding */

        /* Ocultar scrollbar */
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
        width: 0; /* Estos se usan para el scroll-padding, no necesitan ancho */
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
        height: var(--size-content-1); /* Usar la misma variable para la altura de la imagen */
        object-fit: cover;
        margin-bottom: var(--size-2); /* Usar variable para margin-bottom */
        border-radius: var(--radius-image);
    }
    .carousel__slide h3 {
        font-size: var(--font-size-base);
        margin-bottom: calc(var(--size-2) / 2); /* 0.25rem */
        color: var(--text-color);
    }
    .carousel__slide p {
        font-size: var(--font-size-small);
        color: var(--text-color-light);
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
                    <div class="carousel__slide" tabindex="0" data-label="Book {book.id}">
                        <img src="{book.cover_image}" alt="{book.title}" />
                        <h3>{book.title}</h3>
                        <p>{book.author.name}</p>
                    </div>
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
