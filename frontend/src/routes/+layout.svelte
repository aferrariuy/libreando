<script lang="ts">
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte'; // Import Footer

  let darkMode = false; // State for dark mode

  function toggleTheme() {
    darkMode = !darkMode;
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }
</script>

<Header {darkMode} onToggleTheme={toggleTheme} /> <!-- Pass toggleTheme as onToggleTheme prop -->

<main>
  <slot></slot>
</main>

<Footer {darkMode} /> <!-- Add Footer and pass darkMode state -->

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
