<template>
  <div>
    <h1>Stock Data</h1>
    <div class="grid-container">
      <div v-for="data in stockData" :key="data.id" class="grid-row">
        <div class="grid-cell"><strong>Symbol:</strong> {{ data.symbol }}</div>
        <div class="grid-cell"><strong>Date:</strong> {{ data.date }}</div>
        <div class="grid-cell"><strong>Close:</strong> {{ data.close }}</div>
        <div class="grid-cell"><strong>Daily Return:</strong> {{ data.daily_return }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const stockData = ref([]);

onMounted(() => {
  fetch('http://localhost:8000/api/stock-data/')
    .then(response => response.json())
    .then(data => {
      stockData.value = data;
    })
    .catch(error => {
      console.error('Error fetching stock data:', error);
    });
});
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.grid-cell {
  padding: 10px;
  border: 1px solid #ddd;
  background-color: #f9f9f9;
}
</style>