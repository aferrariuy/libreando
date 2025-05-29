<script lang="ts">
    import type { Category } from '$lib/types';

    export let searchTerm: string;
    export let selectedCategory: string;
    export let categories: Category[];
    export let onSearch: (term: string) => void;
    export let onCategoryChange: (categoryId: string) => void;

    function handleSearchInput(event: Event) {
        const value = (event.target as HTMLInputElement).value;
        onSearch(value);
    }

    function handleCategoryChange(event: Event) {
        const value = (event.target as HTMLSelectElement).value;
        onCategoryChange(value);
    }
</script>

<style>
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
</style>

<section id="search-filter">
    <h2>Buscar y Filtrar</h2>
    <div class="search-filter-area">
        <input
            type="text"
            placeholder="Buscar por título o autor..."
            value={searchTerm}
            oninput={handleSearchInput}
        />
        <select value={selectedCategory} onchange={handleCategoryChange}>
            <option value="">Todas las categorías</option>
            {#each categories as category (category.id)}
                <option value="{category.id}">{category.name}</option>
            {/each}
        </select>
    </div>
</section>
