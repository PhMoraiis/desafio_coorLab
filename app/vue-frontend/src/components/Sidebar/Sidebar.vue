<template>
  <nav
    class="fixed top-0 left-0 w-full h-full border-r bg-slate-500 space-y-8 sm:w-80"
  >
    <div class="flex flex-col h-full">
      <div class="h-20 flex items-center px-8">
        <a href="javascript:void(0)" class="flex-none">
          <img src="/images/logo.png" width="140" class="mx-auto" />
        </a>
      </div>
      <div class="flex-1 flex flex-col h-full overflow-auto">
        <ul class="px-4 font-inter text-md flex-1">
          <li>
            <a
              class="flex items-center gap-x-2 text-white p-2 rounded-lg bg-gray-700 duration-150 cursor-pointer"
            >
              <div class="text-white"><Calculator /></div>
              Calculadora de Viagem
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { Calculator } from "lucide-vue-next";
</script>
