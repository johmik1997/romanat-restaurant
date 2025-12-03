<template>
  <div class="flex flex-col gap-4">
    <!-- Search Bar -->
    <div class="flex w-full">
      <label class="flex flex-col h-12 w-full">
        <div class="flex w-full flex-1 items-stretch rounded-lg h-full">
          <div class="text-gray-500 flex bg-white items-center justify-center pl-4 rounded-l-lg border border-gray-200 border-r-0">
            <span class="material-symbols-outlined">search</span>
          </div>
          <input 
            v-model="searchQuery"
            @input="$emit('search', searchQuery)"
            class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-[#111418] focus:outline-0 focus:ring-2 focus:ring-[#0f766e]/50 border border-[#0f766e]/30 bg-white  h-full placeholder:text-gray-500 px-4 rounded-l-none border-l-0 pl-2 text-base font-normal leading-normal" 
            placeholder="Search by room number, type, or floor..." 
          />
        </div>
      </label>
    </div>

    <!-- Filter Controls -->
    <div class="flex flex-wrap items-center justify-between gap-4">
      <div class="flex flex-wrap gap-2">
        <!-- Status Filter -->
        <div class="relative">
          <select 
            v-model="filters.status"
            @change="$emit('filter-change', filters)"
            class="appearance-none bg-white border border-gray-200 rounded-lg px-3 py-2 pr-8 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary/50"
          >
            <option value="all">All Status</option>
            <option value="available">Available</option>
            <option value="occupied">Occupied</option>
            <option value="Reserved">Reserved</option>
            <option value="Maintenance">Maintenance</option>
            <option value="Cleaning">Cleaning</option>
          </select>
          <span class="material-symbols-outlined absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 text-lg pointer-events-none">
            expand_more
          </span>
        </div>

        <!-- Room Type Filter -->
        <div class="relative">
          <select 
            v-model="filters.type"
            @change="$emit('filter-change', filters)"
            class="appearance-none bg-white border border-gray-200 rounded-lg px-3 py-2 pr-8 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary/50"
          >
            <option value="all">All Types</option>
            <option value="Standard">Standard</option>
            <option value="Deluxe">Deluxe</option>
            <option value="Suite">Suite</option>
            <option value="Executive">Executive</option>
            <option value="Presidential">Presidential</option>
          </select>
          <span class="material-symbols-outlined absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 text-lg pointer-events-none">
            expand_more
          </span>
        </div>

        <!-- Floor Filter -->
        <div class="relative">
          <select 
            v-model="filters.floor"
            @change="$emit('filter-change', filters)"
            class="appearance-none bg-white border border-gray-200 rounded-lg px-3 py-2 pr-8 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary/50"
          >
            <option value="all">All Floors</option>
            <option v-for="floor in floors" :key="floor" :value="floor">Floor {{ floor }}</option>
          </select>
          <span class="material-symbols-outlined absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 text-lg pointer-events-none">
            expand_more
          </span>
        </div>

        <!-- Price Range -->
        <div class="flex items-center gap-2">
          <input 
            v-model="filters.minPrice"
            @input="$emit('filter-change', filters)"
            type="number" 
            placeholder="Min Price"
            class="w-24 bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary/50"
          />
          <span class="text-gray-400">-</span>
          <input 
            v-model="filters.maxPrice"
            @input="$emit('filter-change', filters)"
            type="number" 
            placeholder="Max Price"
            class="w-24 bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-primary/50"
          />
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex gap-2">
        <button 
          @click="$emit('export-rooms')"
          class="flex items-center gap-2 bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
        >
          <span class="material-symbols-outlined text-lg">download</span>
          Export
        </button>
        <button 
          @click="$emit('refresh-rooms')"
          class="flex items-center gap-2 bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
        >
          <span class="material-symbols-outlined text-lg">refresh</span>
          Refresh
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RoomFilters',
  data() {
    return {
      searchQuery: '',
      filters: {
        status: 'all',
        type: 'all',
        floor: 'all',
        minPrice: '',
        maxPrice: ''
      },
      floors: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
  },
  watch: {
    filters: {
      handler(newFilters) {
        this.$emit('filter-change', newFilters)
      },
      deep: true
    }
  },
  emits: ['search', 'filter-change', 'export-rooms', 'refresh-rooms']
}
</script>