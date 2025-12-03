<template>
  <div class="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-lg transition-shadow">
    <div class="flex items-start justify-between mb-4">
      <div>
        <h3 class="text-lg font-semibold text-gray-900">{{ report.title }}</h3>
        <p class="text-sm text-gray-500">{{ report.description }}</p>
      </div>
      <div :class="iconContainerClasses">
        <span class="material-symbols-outlined text-xl">{{ report.icon }}</span>
      </div>
    </div>

    <div class="space-y-3 mb-4">
      <div class="flex items-center justify-between text-sm">
        <span class="text-gray-500">Frequency:</span>
        <span class="font-medium text-gray-900">{{ report.frequency }}</span>
      </div>
      <div class="flex items-center justify-between text-sm">
        <span class="text-gray-500">Last Generated:</span>
        <span class="font-medium text-gray-900">{{ report.lastGenerated }}</span>
      </div>
      <div class="flex items-center justify-between text-sm">
        <span class="text-gray-500">Records:</span>
        <span class="font-medium text-gray-900">{{ report.recordCount }}</span>
      </div>
    </div>

    <div class="flex gap-2">
      <button 
        @click="$emit('generate-report', report)"
        class="flex-1 bg-primary text-white py-2 px-3 rounded-lg text-sm font-medium hover:bg-primary/90 transition-colors"
      >
        Generate
      </button>
      <button 
        @click="$emit('view-report', report)"
        class="flex-1 border border-gray-300 text-gray-700 py-2 px-3 rounded-lg text-sm font-medium hover:bg-gray-50 transition-colors"
      >
        View
      </button>
      <button 
        @click="$emit('export-report', report)"
        class="flex items-center justify-center border border-gray-300 text-gray-700 py-2 px-3 rounded-lg text-sm font-medium hover:bg-gray-50 transition-colors"
      >
        <span class="material-symbols-outlined text-lg">download</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReportCard',
  props: {
    report: {
      type: Object,
      required: true
    }
  },
  computed: {
    iconContainerClasses() {
      const typeClasses = {
        financial: 'p-3 bg-blue-100 rounded-lg text-blue-600',
        occupancy: 'p-3 bg-green-100 rounded-lg text-green-600',
        guest: 'p-3 bg-purple-100 rounded-lg text-purple-600',
        operational: 'p-3 bg-orange-100 rounded-lg text-orange-600'
      }
      return typeClasses[this.report.type] || typeClasses.financial
    }
  },
  emits: ['generate-report', 'view-report', 'export-report']
}
</script>