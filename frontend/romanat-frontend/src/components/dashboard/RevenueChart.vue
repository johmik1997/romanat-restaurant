<template>
  <div class="w-full">
    <!-- Chart Header with Filters -->
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-4">
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-blue-500"></div>
          <span class="text-sm text-gray-600">Revenue</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-green-500"></div>
          <span class="text-sm text-gray-600">Previous Period</span>
        </div>
      </div>
      
      <div class="flex items-center gap-2 text-sm">
        <button class="px-3 py-1 rounded-lg bg-blue-50 text-blue-600 font-medium">Weekly</button>
        <button class="px-3 py-1 rounded-lg text-gray-600 hover:bg-gray-100">Monthly</button>
        <button class="px-3 py-1 rounded-lg text-gray-600 hover:bg-gray-100">Quarterly</button>
      </div>
    </div>

    <!-- Chart Container -->
    <div class="relative w-full h-64">
      <!-- Y-axis Labels -->
      <div class="absolute left-0 top-0 bottom-0 w-12 flex flex-col justify-between text-xs text-gray-500 py-2">
        <span>$90k</span>
        <span>$70k</span>
        <span>$50k</span>
        <span>$30k</span>
        <span>$10k</span>
        <span>$0</span>
      </div>

      <!-- Chart Area -->
      <div class="ml-12 h-full flex items-end justify-between">
        <!-- Grid Lines -->
        <div class="absolute inset-0 ml-12 flex flex-col justify-between">
          <div class="border-t border-gray-200"></div>
          <div class="border-t border-gray-200"></div>
          <div class="border-t border-gray-200"></div>
          <div class="border-t border-gray-200"></div>
          <div class="border-t border-gray-200"></div>
          <div class="border-t border-gray-200"></div>
        </div>

        <!-- Bars for Current Period -->
        <div 
          v-for="(week, index) in revenueData"
          :key="'current-' + index"
          class="flex flex-col items-center gap-1 flex-1 mx-1"
        >
          <!-- Current Period Bar -->
          <div 
            class="w-6 bg-blue-500 rounded-t-lg transition-all duration-500 hover:bg-blue-600 cursor-pointer relative group"
            :style="{ height: (week.current / 90000 * 100) + '%' }"
          >
            <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white text-xs px-2 py-1 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-200 whitespace-nowrap">
              ${{ week.current.toLocaleString() }}
            </div>
          </div>
          
          <!-- Previous Period Bar -->
          <div 
            class="w-6 bg-green-500 rounded-t-lg transition-all duration-500 hover:bg-green-600 cursor-pointer relative group"
            :style="{ height: (week.previous / 90000 * 100) + '%' }"
          >
            <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white text-xs px-2 py-1 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-200 whitespace-nowrap">
              ${{ week.previous.toLocaleString() }}
            </div>
          </div>
          
          <!-- Week Label -->
          <span class="text-xs text-gray-500 mt-2">{{ week.week }}</span>
        </div>
      </div>
    </div>

    <!-- X-axis -->
    <div class="ml-12 border-t border-gray-200 pt-2">
      <div class="flex justify-between text-xs text-gray-500">
        <span>Week 1</span>
        <span>Week 2</span>
        <span>Week 3</span>
        <span>Week 4</span>
      </div>
    </div>

    <!-- Summary Stats -->
    <div class="grid grid-cols-3 gap-4 mt-6 pt-6 border-t border-gray-200">
      <div class="text-center">
        <p class="text-2xl font-bold text-gray-900">$89,450</p>
        <p class="text-sm text-gray-500">Total Revenue</p>
      </div>
      <div class="text-center">
        <p class="text-2xl font-bold text-green-600">+12.5%</p>
        <p class="text-sm text-gray-500">Growth</p>
      </div>
      <div class="text-center">
        <p class="text-2xl font-bold text-gray-900">142</p>
        <p class="text-sm text-gray-500">Bookings</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const revenueData = ref([
  { week: 'W1', current: 45200, previous: 40100 },
  { week: 'W2', current: 52300, previous: 47800 },
  { week: 'W3', current: 61400, previous: 53200 },
  { week: 'W4', current: 89450, previous: 79500 },
  { week: 'W5', current: 76200, previous: 68100 },
  { week: 'W6', current: 83500, previous: 72300 },
  { week: 'W7', current: 78400, previous: 69200 },
  { week: 'W8', current: 91200, previous: 81000 }
])
</script>