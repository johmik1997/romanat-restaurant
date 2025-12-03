<template>
  <div class="flex flex-col gap-4 rounded-xl border border-gray-200 
              p-4 md:p-6 bg-white shadow-sm h-full">
    
    <!-- Header -->
    <div class="flex flex-col gap-1">
      <p class="text-gray-900 text-lg font-semibold">Booking Sources</p>
      <p class="text-gray-500 text-sm">Distribution of booking channels</p>
    </div>

    <!-- Chart Container -->
    <div class="flex-1 flex items-center justify-center min-h-[200px] md:min-h-[220px]">
      
      <!-- Doughnut Chart SVG -->
      <div class="relative w-40 h-40 md:w-48 md:h-48">
        <!-- Background Circle -->
        <svg class="w-full h-full" viewBox="0 0 100 100">
          <!-- Website Segment -->
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="transparent"
            stroke="#3B82F6"
            stroke-width="20"
            stroke-dasharray="126 251"
            stroke-dashoffset="0"
            class="transition-all duration-500"
          />
          
          <!-- Mobile App Segment -->
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="transparent"
            stroke="#10B981"
            stroke-width="20"
            stroke-dasharray="63 251"
            stroke-dashoffset="-126"
            class="transition-all duration-500"
          />
          
          <!-- Travel Agencies Segment -->
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="transparent"
            stroke="#F59E0B"
            stroke-width="20"
            stroke-dasharray="38 251"
            stroke-dashoffset="-189"
            class="transition-all duration-500"
          />
          
          <!-- Direct Booking Segment -->
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="transparent"
            stroke="#EF4444"
            stroke-width="20"
            stroke-dasharray="25 251"
            stroke-dashoffset="-227"
            class="transition-all duration-500"
          />
        </svg>

        <!-- Center Text -->
        <div class="absolute inset-0 flex items-center justify-center flex-col">
          <p class="text-gray-900 text-xl font-bold">1,248</p>
          <p class="text-gray-500 text-xs">Total Bookings</p>
        </div>
      </div>

    </div>

    <!-- Legend -->
    <div class="grid grid-cols-2 gap-3 mt-2">
      <div v-for="source in bookingSources" :key="source.name" class="flex items-center gap-2">
        <div 
          class="w-3 h-3 rounded-full"
          :style="{ backgroundColor: source.color }"
        ></div>
        <div class="flex-1 min-w-0">
          <p class="text-gray-700 text-sm font-medium truncate">{{ source.name }}</p>
          <p class="text-gray-500 text-xs">{{ source.percentage }}</p>
        </div>
        <p class="text-gray-900 text-sm font-semibold">{{ source.value }}</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const bookingSources = ref([
  {
    name: 'Website',
    percentage: '50%',
    value: '624',
    color: '#3B82F6'
  },
  {
    name: 'Mobile App',
    percentage: '25%',
    value: '312',
    color: '#10B981'
  },
  {
    name: 'Travel Agencies',
    percentage: '15%',
    value: '187',
    color: '#F59E0B'
  },
  {
    name: 'Direct Booking',
    percentage: '10%',
    value: '125',
    color: '#EF4444'
  }
])
</script>