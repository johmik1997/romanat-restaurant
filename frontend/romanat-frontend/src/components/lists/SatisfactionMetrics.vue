<template>
  <div class="space-y-4">
    <div v-for="metric in metrics" :key="metric.metric" class="space-y-2">
      <div class="flex items-center justify-between">
        <span class="text-sm font-medium text-gray-700">{{ metric.metric }}</span>
        <span class="text-sm text-gray-500">{{ metric.change }} vs last period</span>
      </div>
      <div class="flex items-center gap-3">
        <div class="flex-1 bg-gray-200 rounded-full h-2">
          <div 
            class="bg-green-500 h-2 rounded-full" 
            :style="{ width: (metric.value / 5 * 100) + '%' }"
          ></div>
        </div>
        <span class="text-sm font-medium text-gray-900">{{ metric.value }}/5</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SatisfactionMetrics',
  props: {
    metrics: Array
  }
}
</script>