<template>
  <div class="flex flex-col gap-4">
    <!-- Quick Date Filters -->
    <div class="flex flex-wrap gap-2">
      <button 
        v-for="period in quickPeriods"
        :key="period.key"
        @click="selectQuickPeriod(period)"
        :class="quickPeriodClasses(period)"
      >
        {{ period.label }}
      </button>
    </div>

    <!-- Custom Date Range -->
    <DateRangePicker @date-range-change="$emit('date-range-change', $event)" />

    <!-- Additional Filters -->
    <div class="flex flex-wrap items-center gap-4">
      <!-- Report Type -->
      <div class="flex items-center gap-2">
        <label class="text-sm font-medium text-gray-700">Report Type:</label>
        <select 
          v-model="filters.reportType"
          @change="$emit('filter-change', filters)"
          class="bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
        >
          <option value="all">All Reports</option>
          <option value="financial">Financial</option>
          <option value="occupancy">Occupancy</option>
          <option value="guest">Guest Analytics</option>
          <option value="operational">Operational</option>
        </select>
      </div>

      <!-- Export Format -->
      <div class="flex items-center gap-2">
        <label class="text-sm font-medium text-gray-700">Format:</label>
        <select 
          v-model="filters.exportFormat"
          class="bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
        >
          <option value="pdf">PDF</option>
          <option value="excel">Excel</option>
          <option value="csv">CSV</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script>
import DateRangePicker from './DateRangePicker.vue'

export default {
  name: 'ReportFilters',
  components: {
    DateRangePicker
  },
  data() {
    return {
      filters: {
        reportType: 'all',
        exportFormat: 'pdf'
      },
      quickPeriods: [
        { key: 'today', label: 'Today' },
        { key: 'yesterday', label: 'Yesterday' },
        { key: 'week', label: 'This Week' },
        { key: 'month', label: 'This Month' },
        { key: 'quarter', label: 'This Quarter' },
        { key: 'year', label: 'This Year' }
      ],
      selectedPeriod: 'month'
    }
  },
  methods: {
    selectQuickPeriod(period) {
      this.selectedPeriod = period.key
      this.$emit('quick-period-change', period)
    },
    quickPeriodClasses(period) {
      const baseClasses = 'px-3 py-2 rounded-lg text-sm font-medium transition-colors'
      return period.key === this.selectedPeriod
        ? `${baseClasses} bg-primary text-white`
        : `${baseClasses} bg-white text-gray-700 border border-gray-200 hover:bg-gray-50`
    }
  },
  emits: ['date-range-change', 'filter-change', 'quick-period-change']
}
</script>