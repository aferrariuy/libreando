<script lang="ts">
  import { darkMode } from '$lib/stores/theme';

  export let onToggleTheme: () => void; // Prop for the callback function

  function handleClick() {
    if (onToggleTheme) {
      onToggleTheme(); // Call the callback prop
    }
  }
</script>

<header>
  <div class="logo">
    Libreando
  </div>
  <div class="theme-toggle">    <button on:click={handleClick} aria-label="Toggle theme"> <!-- Use handleClick -->
      {#if $darkMode}
        <span>☀️</span> <!-- Sun icon for light mode -->
      {:else}
        <span>🌙</span> <!-- Moon icon for dark mode -->
      {/if}
    </button>
  </div>
</header>

<style>
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: var(--header-bg);
    color: var(--header-text);
    border-bottom: 1px solid var(--header-border-color);
  }

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
  }

  .theme-toggle button {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.5rem;
    color: inherit;
  }
</style>
