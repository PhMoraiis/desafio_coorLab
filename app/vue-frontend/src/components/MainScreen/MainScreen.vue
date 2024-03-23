<template>
  <div class="p-4 sm:ml-64 mt-12">
    <div class="p-4 rounded dark:border-gray-700 mt-4">
      <div class="grid grid-cols-1">
        <div
          class="flex items-center justify-start gap-6 p-12 h-24 rounded bg-gray-300 shadow-md dark:bg-gray-800"
        >
          <Calculator class="w-20 h-12 lg:w-12 text-gray-900 dark:text-white" />
          <p class="text-2xl text-gray-900 dark:text-white font-inter">
            Calculadora de Viagens
          </p>
        </div>
      </div>
      <div
        class="flex flex-col shadow-md lg:flex-row items-start h-full w-full mb-4 rounded bg-gray-50 dark:bg-gray-300"
      >
        <FormCalc @tripFound="handleTripFound" />
        <!-- Ouvindo o evento tripFound -->

        <ResultCalc :tripDetails="tripDetails" />
        <!-- Passando os detalhes da viagem como props -->
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import ResultCalc from "@/components/ResultCalc/ResulCalc.vue";
import FormCalc from "@/components/FormCalc/FormCalc.vue";
import { Calculator } from "lucide-vue-next";
import { ref } from "vue";

const tripDetails = ref(""); // Ref para armazenar os detalhes da viagem

const handleTripFound = (data: any) => {
  tripDetails.value = data; // Atualizando tripDetails com os detalhes da viagem
};
</script>

