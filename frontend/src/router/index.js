// filepath: /home/sigma/stock_analysis_project/frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import StockData from '../components/StockData.vue';

const routes = [
  {
    path: '/stock-data',
    name: 'StockData',
    component: StockData
  },
  // Add other routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;