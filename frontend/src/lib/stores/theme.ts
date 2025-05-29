import { writable } from 'svelte/store';
import { browser } from '$app/environment';

const STORAGE_KEY = 'libreando-dark-mode';

function getInitialValue(): boolean {
  // Server-side rendering safety check
  if (!browser) return false;
  
  // Check localStorage first
  const stored = localStorage.getItem(STORAGE_KEY);
  if (stored !== null) {
    return stored === 'true';
  }
  
  // Fallback to system preference if no stored value
  if (window.matchMedia) {
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  
  return false;
}

function createDarkModeStore() {
  const { subscribe, set, update } = writable(getInitialValue());

  return {
    subscribe,
    set: (value: boolean) => {
      set(value);
      if (browser) {
        localStorage.setItem(STORAGE_KEY, value.toString());
        // Apply theme immediately to document
        if (value) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      }
    },
    update,
    toggle: () => {
      update(current => {
        const newValue = !current;
        if (browser) {
          localStorage.setItem(STORAGE_KEY, newValue.toString());
          // Apply theme immediately to document
          if (newValue) {
            document.documentElement.classList.add('dark');
          } else {
            document.documentElement.classList.remove('dark');
          }
        }
        return newValue;
      });
    }
  };
}

export const darkMode = createDarkModeStore();
