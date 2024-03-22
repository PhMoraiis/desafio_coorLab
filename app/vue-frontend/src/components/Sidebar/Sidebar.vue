<script setup lang="ts">
import { ref, onMounted } from "vue";
import { Calculator, Menu, Moon, Sun, X } from "lucide-vue-next";
import { Switch } from "@/components/ui/switch";

const isOpen = ref(false);
const darkMode = ref(false);
const defaultTheme = false;

function toggleDarkMode() {
  darkMode.value = !darkMode.value;
  if (darkMode.value) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
  // Save the current theme preference to local storage
  localStorage.setItem('darkMode', JSON.stringify(darkMode.value));
}

function toggleNavbar() {
  isOpen.value = !isOpen.value;
}

// Check local storage on component mount to load previous theme preference
onMounted(() => {
  const savedDarkMode = localStorage.getItem('darkMode');
  try {
    if (savedDarkMode !== null) {
      darkMode.value = JSON.parse(savedDarkMode);
      if (darkMode.value) {
        document.documentElement.classList.add("dark");
      } else {
        document.documentElement.classList.remove("dark");
      }
    } else {
      // If no saved value in localStorage, use the default theme
      darkMode.value = defaultTheme;
    }
  } catch (error) {
    console.error("Error parsing darkMode from localStorage:", error);
    // If an error occurs while parsing JSON, use the default theme
    darkMode.value = defaultTheme;
  }
});
</script>

<template>
  <nav class="fixed top-0 z-50 w-full bg-white border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
    <div class="px-3 py-3 lg:px-5 lg:pl-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center justify-start rtl:justify-end">
          <button type="button" @click="toggleNavbar" class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700">
            <template v-if="isOpen">
              <X class="w-6 h-6 text-gray-400" />
            </template>
            <template v-else>
              <Menu class="w-6 h-6 text-gray-400" />
            </template>
          </button>
          <a href="" class="flex ms-2 md:me-24">
            <img v-if="!darkMode" src="https:/images/logo-dark.png" class="h-8 me-3" alt="CB Viagens Logo (Light)" />
            <img v-else src="https:/images/logo.png" class="h-8 me-3" alt="CB Viagens Logo (Dark)" />
          </a>
        </div>
        <div class="flex items-center">
          <div class="flex items-center ms-3 gap-4">
            <div class="flex gap-2 items-center">
              <Sun class="text-gray-500 dark:text-gray-200" />
              <Switch :checked="darkMode" @click="toggleDarkMode" />
              <Moon class="text-gray-500 dark:text-gray-200" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <aside id="logo-sidebar" :class="{ '-translate-x-full': !isOpen, 'translate-x-0': isOpen }" class="fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform bg-white border-r border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700" aria-label="Sidebar">
    <div class="h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800">
      <ul class="space-y-2 font-medium">
        <li>
          <a href="#" class="flex items-center p-2 font-inter text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
            <Calculator class="w-6 h-6" />
            <span class="ms-3">Calculadora de Viagens</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>
