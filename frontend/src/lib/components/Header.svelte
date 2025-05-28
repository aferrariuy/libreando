<script lang="ts">
  export let darkMode: boolean;
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
  <div class="theme-toggle">
    <button on:click={handleClick} aria-label="Toggle theme"> <!-- Use handleClick -->
      {#if darkMode}
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
    background-color: var(--header-bg, #f0f0f0); /* Default light theme background */
    color: var(--header-text, #333); /* Default light theme text */
    border-bottom: 1px solid var(--header-border, #ddd);
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
    color: inherit; /* Inherit color from header */
  }

  /* Basic dark mode styling for the header itself */
  :global(html.dark) header {
    --header-bg: #333;
    --header-text: #f0f0f0;
    --header-border: #555;
  }
</style>
