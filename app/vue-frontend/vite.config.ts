import path from "path"
import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"

import tailwind from "tailwindcss"
import autoprefixer from "autoprefixer"

export default defineConfig({
  server: {
    port: 8080,
  },
  css: {
    postcss: {
      plugins: [tailwind(), autoprefixer()],
    },
  },
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})