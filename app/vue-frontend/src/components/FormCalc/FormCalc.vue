<template>
  <div
    class="flex flex-col items-center justify-center lg:w-2/3 mx-auto mt-4 bg-gray-300 dark:bg-gray-800 p-12 lg:m-6 rounded-xl shadow-md"
  >
    <div class="flex gap-4 items-center justify-center mb-6 dark:text-gray-100">
      <PlaneTakeoff strokeWidth="{0.75}" class="w-12 h-12" />
      <h1 class="text-xl font-inter">Calcule o Valor da sua Viagem</h1>
    </div>
    <form
      class="flex flex-col w-full gap-6 mt-6 dark:text-gray-100"
      @submit.prevent="validateAndSubmit"
    >
      <div class="flex flex-col gap-1">
        <Label class="text-lg" for="destiny">Destino</Label>
        <span class="text-sm text-gray-500 dark:text-gray-400"
          >Selecione o seu Destino</span
        >
        <select
          v-model="selectedDestination"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-[#00a9b7] focus:border-[#00a9b7] block w-full p-2.5 dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#00a9b7] dark:focus:border-[#00a9b7]"
          name="destiny"
          id="destiny"
        >
          <option value="" disabled selected hidden>
            Selecione o seu Destino
          </option>
          <option
            v-for="destination in destinations"
            :key="destination"
            :value="destination"
          >
            {{ destination }}
          </option>
        </select>
      </div>

      <div class="flex flex-col gap-1 mb-8">
        <Label class="text-lg" for="date">Data</Label>
        <span class="text-sm text-gray-500 dark:text-gray-400"
          >Selecione uma Data</span
        >
        <input
          v-model="selectedDate"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-[#00a9b7] focus:border-[#00a9b7] block w-full p-2.5 dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#00a9b7] dark:focus:border-[#00a9b7]"
          type="date"
          name="date"
          id="date"
        />
      </div>

      <div class="flex flex-col gap-4">
        <Button class="bg-[#00a9b7] dark:bg-[#00a9b7]" type="submit">
          Buscar
        </Button>
        <Button
          class="bg-[#e9d736] dark:bg-[#e9d736] text-gray-800 hover:text-gray-100"
          type="button"
          @click="clearForm"
        >
          Limpar
        </Button>
      </div>
    </form>

    <div
      v-if="showModal"
      class="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-800 bg-opacity-75"
      @click="closeModal"
    >
      <div
        class="bg-white dark:bg-gray-800 dark:border-gray-400 dark:border-[1px] p-16 rounded-xl shadow-lg flex flex-col items-center justify-center max-w-xl gap-4"
        @click.stop
      >
        <TriangleAlert :stroke-width="1.2" class="w-20 h-20 text-[#00a9b7]" />
        <p
          class="text-xl font-interBd text-center text-gray-600 dark:text-gray-100"
        >
          Por favor, insira os valores para realizar a cotação.
        </p>
        <Button
          class="mt-4 bg-[#00a9b7] dark:bg-[#00a9b7] dark:text-gray-100 dark:hover:text-gray-600"
          @click="closeModal"
          >Fechar</Button
        >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { PlaneTakeoff, TriangleAlert } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { ref, onMounted, defineEmits } from "vue";
import { API } from "@/services/API";

const emit  = defineEmits(["tripFound"]);

const selectedDestination = ref("");
const selectedDate = ref("");
const destinations = ref([]);
const showModal = ref(false);

const fetchDestinations = async () => {
  try {
    const response = await API.get("/cities/");
    destinations.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar destinos:", error);
  }
};

onMounted(() => {
  fetchDestinations();
});

const validateAndSubmit = async () => {
  if (!selectedDestination.value || !selectedDate.value) {
    showModal.value = true;
  } else {
    showModal.value = false;
    try {
      const response = await API.get(
        `/trips/?city=${selectedDestination.value}`
      );
      console.log("Viagens encontradas: ", response.data);
      emit("tripFound", response.data);
    } catch (error) {
      console.error("Erro ao buscar viagens:", error);
    }
  }
};

const closeModal = () => {
  showModal.value = false;
};

const clearForm = () => {
  selectedDestination.value = "";
  selectedDate.value = "";
};
</script>

