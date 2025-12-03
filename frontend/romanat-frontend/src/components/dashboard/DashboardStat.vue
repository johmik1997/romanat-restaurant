<template>
  <div class="flex flex-col gap-4 p-4 md:p-6 rounded-xl border border-gray-200 
              bg-white shadow-sm hover:shadow-md transition-shadow duration-200">
    
    <!-- Header -->
    <div class="flex items-center justify-between">
      <p class="text-gray-500 text-sm font-medium">{{ title }}</p>
      
      <!-- Trend Indicator -->
      <div 
        class="flex items-center gap-1 px-2 py-1 rounded-full text-xs font-medium"
        :class="trendClasses"
      >
        <span class="material-symbols-outlined text-sm">
          {{ trend === 'up' ? 'trending_up' : 'trending_down' }}
        </span>
        {{ percent }}
      </div>
    </div>

    <!-- Value -->
    <p class="text-gray-900 text-2xl md:text-3xl font-bold">{{ value }}</p>

    <!-- Progress Bar -->
    <div class="w-full bg-gray-200 rounded-full h-2">
      <div 
        class="h-2 rounded-full transition-all duration-500"
        :class="trend === 'up' ? 'bg-green-500' : 'bg-red-500'"
        :style="{ width: progressWidth }"
      ></div>
    </div>

  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  value: {
    type: String,
    required: true
  },
  percent: {
    type: String,
    required: true
  },
  trend: {
    type: String,
    validator: (value) => ['up', 'down'].includes(value),
    required: true
  }
})

const trendClasses = computed(() => {
  return props.trend === 'up' 
    ? 'bg-green-50 text-green-600'
    : 'bg-red-50 text-red-600'
})

const progressWidth = computed(() => {
  if (props.title.includes('Revenue')) return '75%'
  if (props.title.includes('Occupancy')) return '82%'
  if (props.title.includes('Bookings')) return '65%'
  if (props.title.includes('Rate')) return '70%'
  return '50%'
})
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 20;
}
</style>