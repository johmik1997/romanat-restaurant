<template>
  <div class="flex items-center justify-between gap-2">
    <div class="flex gap-2 flex-wrap">
      <!-- All Guests Filter -->
      <button
        @click="$emit('filter-change', 'all')"
        class="px-4 py-2 rounded-lg transition-colors font-medium text-sm"
        :class="activeFilter === 'all' 
          ? 'bg-blue-500 text-white shadow-sm' 
          : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
      >
        All ({{ counts.all }})
      </button>

      <!-- Active Guests Filter -->
      <button
        @click="$emit('filter-change', 'current')"
        class="px-4 py-2 rounded-lg transition-colors font-medium text-sm"
        :class="activeFilter === 'current' 
          ? 'bg-green-500 text-white shadow-sm' 
          : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
      >
        Active ({{ counts.current }})
      </button>

      <!-- Past Guests Filter -->
      <button
        @click="$emit('filter-change', 'past')"
        class="px-4 py-2 rounded-lg transition-colors font-medium text-sm"
        :class="activeFilter === 'past' 
          ? 'bg-gray-500 text-white shadow-sm' 
          : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
      >
        Pending ({{ counts.past }})
      </button>

      <!-- VIP Guests Filter -->
      <button
        @click="$emit('filter-change', 'vip')"
        class="px-4 py-2 rounded-lg transition-colors font-medium text-sm"
        :class="activeFilter === 'vip' 
          ? 'bg-yellow-500 text-white shadow-sm' 
          : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
      >
        VIP ({{ counts.vip }})
      </button>
    </div>

    <!-- Action Buttons -->
    <div class="flex gap-1">
      <button 
        @click="$emit('filter-click')"
        class="p-2 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors"
        title="Advanced filters"
      >
        <span class="material-symbols-outlined text-xl">filter_list</span>
      </button>
      <button 
        @click="$emit('export-click')"
        class="p-2 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors"
        title="Export data"
      >
        <span class="material-symbols-outlined text-xl">download</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FilterChips',
  props: {
    activeFilter: {
      type: String,
      default: 'all'
    },
    counts: {
      type: Object,
      default: () => ({
        all: 0,
        current: 0,
        past: 0,
        vip: 0
      })
    }
  },
  emits: ['filter-change', 'filter-click', 'export-click']
}
</script>