<script>
    import { createEventDispatcher, onMount } from 'svelte';

    const dispatch = createEventDispatcher();
    export let selectedCategory = '';
    /** @type {any[]} */
    let categories = [];
    let loading = true;
    let error = '';

    onMount(async () => {
        try {
            const response = await fetch(new URL('/api/categories/', window.location.origin));
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            categories = await response.json();
        } catch (e) {
            error = (e && typeof e === 'object' && 'message' in e) ? String(e.message) : 'An unknown error occurred';
        } finally {
            loading = false;
        }
    });

    /**
     * @param {Event} event
     */
    function handleChange(event) {
        if (event && event.target && typeof event.target === 'object' && 'value' in event.target) {
            selectedCategory = String(event.target.value);
        }
        dispatch('filter', selectedCategory);
    }
</script>

<div class="filter-dropdown">
    {#if loading}
        <p>Loading categories...</p>
    {:else if error}
        <p class="error">Error loading categories: {error}</p>
    {:else}
        <select bind:value={selectedCategory} on:change={handleChange}>
            <option value="">All Categories</option>
            {#each categories as category}
                <option value={category.name ?? ''}>{category.name ?? 'Unknown'}</option>
            {/each}
        </select>
    {/if}
</div>

<style>
    .filter-dropdown {
        margin-bottom: 1em;
    }

    select {
        width: 100%;
        padding: 0.8em;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 1em;
        background-color: white;
    }

    .error {
        color: red;
    }
</style>
