<script lang="ts">
  // No se necesita importar getContext si no se usa darkMode directamente en el script
</script>

<footer>
  <div class="copyright">
    © {new Date().getFullYear()} Libreando. All rights reserved.
  </div>
  <div class="social-icons">
    <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
      <!-- You can replace this with an SVG or an icon font if you prefer -->
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-instagram"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
    </a>
  </div>
</footer>

<style>  footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: var(--footer-bg);
    color: var(--footer-text);
    border-top: 1px solid var(--footer-border);
    text-align: center;
  }

  .copyright {
    font-size: 0.9rem;
  }

  .social-icons a {
    color: inherit;
    text-decoration: none;
    margin-left: 1rem;
  }

  .social-icons svg {
    vertical-align: middle;
  }
</style>
