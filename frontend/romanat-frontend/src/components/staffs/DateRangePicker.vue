<template>
  <div class="flex items-center gap-4">
    <div class="flex items-center gap-2">
      <label class="text-sm font-medium text-gray-700">From:</label>
      <input 
        v-model="dateRange.start"
        type="date"
        class="bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
      />
    </div>
    <div class="flex items-center gap-2">
      <label class="text-sm font-medium text-gray-700">To:</label>
      <input 
        v-model="dateRange.end"
        type="date"
        class="bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
      />
    </div>
    <button 
      @click="applyDateRange"
      class="bg-primary text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-primary/90 transition-colors"
    >
      Apply
    </button>
    <button 
      @click="resetDateRange"
      class="bg-white border border-gray-200 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium hover:bg-gray-50 transition-colors"
    >
      Reset
    </button>
  </div>
</template>

<script>
export default {
  name: 'DateRangePicker',
  data() {
    return {
      dateRange: {
        start: this.getDefaultStartDate(),
        end: this.getDefaultEndDate()
      }
    }
  },
  methods: {
    getDefaultStartDate() {
      const date = new Date()
      date.setMonth(date.getMonth() - 1)
      return date.toISOString().split('T')[0]
    },
    getDefaultEndDate() {
      return new Date().toISOString().split('T')[0]
    },
    applyDateRange() {
      this.$emit('date-range-change', this.dateRange)
    },
    resetDateRange() {
      this.dateRange = {
        start: this.getDefaultStartDate(),
        end: this.getDefaultEndDate()
      }
      this.$emit('date-range-change', this.dateRange)
    }
  },
  mounted() {
    this.applyDateRange()
  },
  emits: ['date-range-change']
}
</script>