<script lang="ts">  import '$lib/styles/global.css';
  import { onMount } from 'svelte';
  import { darkMode } from '$lib/stores/theme';
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte'; // Import Footer

  // Initialize dark mode on mount
  onMount(() => {
    // Apply initial theme state
    if ($darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  });

  function toggleTheme() {
    darkMode.toggle();
  }
</script>

<Header onToggleTheme={toggleTheme} /> <!-- Pass toggleTheme as onToggleTheme prop -->

<main>
  <slot></slot>
</main>

<Footer /> <!-- Add Footer -->

<style>
  main {
    padding: 1rem;
    flex: 1; /* Ensure main content takes available space */
    display: flex;
    flex-direction: column;
  }

  /* Ensure the layout itself is a flex column to push footer down */
  :global(body) {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
</style>
