<template>
  <div
    class="flex flex-col items-start justify-center w-full p-12"
  >
    <div class="gap-4 mb-6 max-w-md">
      <h1 class="text-xl font-inter">
        Estas são as melhores alternativas de viagem para a data selecionada:
      </h1>
    </div>
    <div class="flex flex-col gap-4 w-full">
      <div class="flex flex-col items-center lg:flex-row gap-4">
        <div class="flex flex-col lg:flex-row w-full">
          <div class="bg-[#00a9b7] px-8 py-12 rounded-xl shadow-md flex items-center justify-center">
            <Gem class="text-gray-100 w-12 h-12" />
          </div>
          <div
            class="shadow-md p-12 bg-gray-500 dark:bg-gray-800 rounded-xl w-full flex flex-col items-start justify-center text-gray-800 dark:text-gray-100"
          >
            <h1 class="font-interBd text-xl">TC Transportes</h1>
            <span class="text-gray-800 dark:text-gray-300">Leito</span>
            <span class="text-gray-800 dark:text-gray-300">Tempo estimado</span>
          </div>
        </div>
        <div
          class="shadow-md bg-gray-500 dark:bg-gray-800 rounded-xl w-2/4 lg:w-1/4 flex flex-col items-start justify-center p-6 text-gray-800 dark:text-gray-100 h-[176px]"
        >
          <h2 class="font-interBd text-xl">Preço</h2>
          <span class="text-gray-800 dark:text-gray-300">R$120000</span>
        </div>
      </div>
      <div class="flex flex-col items-center lg:flex-row gap-4">
        <div class="flex flex-col lg:flex-row w-full">
          <div class="bg-[#00a9b7] px-8 py-12 rounded-xl shadow-md flex items-center justify-center">
            <HandCoins class="text-gray-100 w-12 h-12" />
          </div>
          <div
            class="shadow-md p-12 bg-gray-500 dark:bg-gray-800 rounded-xl w-full flex flex-col items-start justify-center text-gray-800 dark:text-gray-100"
          >
            <h1 class="font-interBd text-xl">TC Transportes</h1>
            <span class="text-gray-800 dark:text-gray-300">Leito</span>
            <span class="text-gray-800 dark:text-gray-300">Tempo estimado</span>
          </div>
        </div>
        <div
          class="shadow-md bg-gray-500 dark:bg-gray-800 rounded-xl w-2/4 lg:w-1/4 flex flex-col items-start justify-center p-6 text-gray-800 dark:text-gray-100 h-[176px]"
        >
          <h2 class="font-interBd text-xl">Preço</h2>
          <span class="text-gray-800 dark:text-gray-300">R$120000</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Gem, HandCoins } from "lucide-vue-next";
</script>
