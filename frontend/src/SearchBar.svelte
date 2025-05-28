<script>
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();
    export let searchTerm = '';

    function handleInput(event) {
        searchTerm = event.target.value;
        dispatch('search', searchTerm);
    }
</script>

<div class="search-bar">
    <input
        type="text"
        placeholder="Search by title or author..."
        bind:value={searchTerm}
        on:input={handleInput}
    />
</div>

<style>
    .search-bar {
        margin-bottom: 1em;
    }

    input {
        width: 100%;
        padding: 0.8em;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 1em;
    }
</style>
