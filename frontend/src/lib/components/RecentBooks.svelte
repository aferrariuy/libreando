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

        console.log('scrollLeft:', scrollLeft, 'clientWidth:', clientWidth, 'scrollWidth:', scrollWidth);
        console.log('canScrollLeft:', canScrollLeft, 'canScrollRight:', canScrollRight);
        console.log('showLeftGradient:', showLeftGradient, 'showRightGradient:', showRightGradient);
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
    /* Define CSS variables with fallback values */
    :root {
        --size-content-1: 200px; /* Example width for a carousel item */
        --size-4: 1rem; /* Gap between items */
        --size-2: 0.5rem; /* Padding */
        --ratio-portrait: 3/4; /* Aspect ratio for carousel items */
        --surface-2: #f0f0f0; /* Light background for items */
        --surface-3: #ccc; /* Light border for items */
        --shadow-2: 0 3px 6px rgba(0,0,0,0.16); /* Subtle shadow */
        --radius-2: 8px; /* Border radius */
        --font-antique: 'Georgia', serif; /* Example font */
        --font-size-5: 1.5rem; /* Base font size for text in slide */
        --font-size-7: 2.5rem; /* Larger font size for snapped text */
        --ease-spring-4: cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Spring-like transition */
        --link: blue; /* Color for snapped text */

        /* Theme-related variables from previous version, for consistency */
        --card-border-color: #ddd;
        --card-background-color: #fff;
        --text-color: #333;
        --text-color-light: #666;
    }

    /* Dark mode adjustments for consistency with previous theme */
    @media (prefers-color-scheme: dark) {
        :root {
            --surface-2: #333;
            --surface-3: #555;
            --card-border-color: #555;
            --card-background-color: #222; /* Used by gradients */
            --text-color: #eee;
            --text-color-light: #bbb;
        }
    }

    .carousel-container {
        position: relative;
        width: 100%;
        overflow: hidden; /* Keeps gradients contained if they were to overflow */
    }

    .carousel-container::before,
    .carousel-container::after {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        width: 1000px; /* Ancho del gradiente, debe coincidir con scroll-padding */
        pointer-events: none; /* Permite hacer clic a través del gradiente */
        z-index: 5; /* Asegura que el gradiente esté sobre el carrusel pero debajo de los botones */
        opacity: 0; /* Inicialmente oculto */
        transition: opacity 0.3s ease-in-out;
    }

    .carousel-container::before {
        left: 0;
        background: radial-gradient(ellipse 50% 100% at left, var(--card-background-color) 0%, transparent 70%); /* Gradiente ovalado a la izquierda, más suave y menos recto */
    }

    .carousel-container::after {
        right: 0;
        background: radial-gradient(ellipse 50% 100% at right, var(--card-background-color) 0%, transparent 70%); /* Gradiente ovalado a la derecha, más suave y menos recto */
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
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
        border: none;
        padding: 0.75rem; /* Increased padding */
        cursor: pointer;
        z-index: 10;
        border-radius: 50%; /* Make buttons circular */
        width: 40px; /* Fixed width */
        height: 40px; /* Fixed height */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem; /* Larger icon/text */
        line-height: 1; /* Ensure text is centered vertically */
        transition: background-color 0.3s ease;
    }

    .carousel-button:hover {
        background-color: rgba(0, 0, 0, 0.8);
    }

    .carousel-button.prev {
        left: 10px;
    }

    .carousel-button.next {
        right: 10px;
    }

    .carousel {
        width: 100%; /* Use standard width for debugging */

        display: flex; /* Use flexbox for simpler layout */
        gap: var(--size-4); /* Gap between items */
        
        /* Remove direct inline padding from the carousel itself */
        padding-left: 0;
        padding-right: 0;
        padding-block: var(--size-2); /* Vertical padding */
        
        /* scroll-padding defines the optimal viewing region for scroll snapping. */

       
        overflow-x: scroll; /* Enable horizontal scrolling */
        scroll-snap-type: x mandatory; /* Snap to items */
        scroll-behavior: smooth; /* Smooth scrolling */
        -webkit-overflow-scrolling: touch; /* For smooth scrolling on iOS */
        overscroll-behavior-x: contain; /* Prevent page scroll when carousel edge is reached */

        /* Hide scrollbar for Chrome, Safari and Opera */
        &::-webkit-scrollbar {
            display: none;
        }
        /* Hide scrollbar for IE, Edge and Firefox */
        -ms-overflow-style: none;  /* IE and Edge */
        scrollbar-width: none;  /* Firefox */
    }

    .carousel::before, /* Added ::before rule */
    .carousel::after {
        content: '';
        display: block;
        flex-shrink: 0; /* Prevent this spacer from shrinking */
        width: 0;   /* Aumentado para cubrir más la tarjeta */
    }

    .carousel__slide {
        flex: 0 0 auto; /* Prevent items from shrinking */
        width: 200px; /* Fixed width for debugging */

        background: var(--card-background-color);
        padding: 0.5rem; /* Added padding to match previous design */
        text-align: center; /* Centered text */

        display: flex; /* Use flexbox for internal content */
        flex-direction: column; /* Arrange content vertically */
        align-items: center; /* Center items horizontally */
        justify-content: center; /* Center items vertically */

        aspect-ratio: var(--ratio-portrait);

        border: 1px solid var(--surface-3);
        box-shadow: var(--shadow-2);
        border-radius: var(--radius-2);

        transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out; /* Smooth transform and opacity on hover/focus */
        scroll-snap-align: start; /* Ensure items snap to the start */
    }

    .carousel__slide:hover {
        transform: translateY(-5px); /* Lift effect on hover */
    }

    .carousel__slide img {
        max-width: 100%;
        height: 200px; /* Fixed height for images */
        object-fit: cover; /* Ensure images cover the area */
        margin-bottom: 0.5rem;
        border-radius: 4px;
    }
    .carousel__slide h3 {
        font-size: 1.1rem;
        margin-bottom: 0.25rem;
        color: var(--text-color);
    }
    .carousel__slide p {
        font-size: 0.9rem;
        color: var(--text-color-light); /* Lighter text for author */
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
