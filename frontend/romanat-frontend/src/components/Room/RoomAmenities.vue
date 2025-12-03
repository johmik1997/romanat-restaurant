<template>
  <div>
    <h3 class="text-2xl font-serif font-bold text-gray-800 mb-6">What this room offers</h3>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <div 
        v-for="amenity in amenities" 
        :key="amenity.name"
        class="flex items-center gap-4 p-4 bg-white rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-300"
      >
        <div class="h-12 w-12 bg-primary/10 rounded-xl flex items-center justify-center">
          <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 20 20">
            <!-- Add SVG paths for different amenities -->
            <path v-if="amenity.icon === 'wifi'" d="M17.778 8.222c-4.296-4.296-11.26-4.296-15.556 0A1 1 0 01.808 6.808c5.076-5.077 13.308-5.077 18.384 0a1 1 0 01-1.414 1.414zM14.95 11.05a7 7 0 00-9.9 0 1 1 0 01-1.414-1.414 9 9 0 0112.728 0 1 1 0 01-1.414 1.414zM12.12 13.88a3 3 0 00-4.242 0 1 1 0 01-1.415-1.415 5 5 0 017.072 0 1 1 0 01-1.415 1.415zM9 16a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z"/>
            <path v-else-if="amenity.icon === 'ac_unit'" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
            <!-- Add more SVG paths for other amenities -->
          </svg>
        </div>
        <span class="text-gray-700 font-medium">{{ amenity }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  amenities: {
    type: Array,
    required: true
  }
})
</script>