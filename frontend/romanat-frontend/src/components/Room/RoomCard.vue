<template>
  <router-link
    :to="{ name: 'RoomDetail', params: { id: room.id } }"
    class="block cursor-pointer"
  >
    <div class="flex flex-col bg-white rounded-2xl shadow-lg overflow-hidden transition-all duration-300 hover:shadow-2xl hover:-translate-y-2 group">
      <!-- Image Section -->
      <div class="relative">
        <img 
          :src="room.image || '/default-room.jpg'" 
          :alt="room.title" 
          class="w-full h-64 object-cover"
          @error="handleImageError"
        />
        <!-- Rating Badge -->
        <div v-if="room.reviews && room.reviews.rating" class="absolute top-3 right-3 flex items-center gap-1 bg-black/70 text-white px-3 py-1.5 rounded-full text-sm font-bold">
          <svg class="w-4 h-4 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
          </svg>
          <span>{{ room.reviews.rating }}</span>
        </div>
        <!-- Featured Badge -->
        <div v-if="room.featured" class="absolute top-3 left-3">
          <span class="bg-[#0f766e] text-white text-xs px-3 py-1.5 rounded-full font-bold">
            Featured
          </span>
        </div>
        <!-- Status Badge -->
        <div v-if="room.status" class="absolute bottom-3 left-3">
          <span :class="['text-xs px-3 py-1.5 rounded-full font-bold', 
            room.status === 'available' ? 'bg-green-500 text-white' :
            room.status === 'occupied' ? 'bg-red-500 text-white' :
            'bg-gray-500 text-white'
          ]">
            {{ room.status }}
          </span>
        </div>
      </div>
      
      <!-- Content Section -->
      <div class="p-6 flex flex-col flex-grow">
        <!-- Title -->
        <h3 class="text-xl font-bold text-gray-800 mb-2">{{ room.title }}</h3>
        
        <!-- Subtitle (conditional) -->
        <h4 v-if="room.subtitle" class="text-lg font-semibold text-gray-600 mb-2">{{ room.subtitle }}</h4>
        
        <!-- Description -->
        <p class="text-gray-600 mb-4 flex-grow line-clamp-3">{{ room.description }}</p>
        
        <!-- Room Details -->
        <div class="flex items-center gap-4 mb-4 text-sm text-gray-500">
          <div class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
            </svg>
            <span>{{ room.capacity || '2 Guests' }}</span>
          </div>
          <div class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
            </svg>
            <span>{{ room.category ? room.category.charAt(0).toUpperCase() + room.category.slice(1) : 'Standard' }}</span>
          </div>
        </div>
        
        <!-- Amenities -->
        <div v-if="room.amenities && room.amenities.length" class="flex items-center gap-3 mb-4 text-gray-500 flex-wrap">
          <div v-for="amenity in displayedAmenities" :key="amenity" class="flex items-center gap-1" :title="getAmenityName(amenity)">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path v-if="amenity === 'wifi'" d="M17.778 8.222c-4.296-4.296-11.26-4.296-15.556 0A1 1 0 01.808 6.808c5.076-5.077 13.308-5.077 18.384 0a1 1 0 01-1.414 1.414zM14.95 11.05a7 7 0 00-9.9 0 1 1 0 01-1.414-1.414 9 9 0 0112.728 0 1 1 0 01-1.414 1.414zM12.12 13.88a3 3 0 00-4.242 0 1 1 0 01-1.415-1.415 5 5 0 017.072 0 1 1 0 01-1.415 1.415zM9 16a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z"/>
              <path v-else-if="amenity === 'ac'" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
              <path v-else-if="amenity === 'tv'" d="M2 6a2 2 0 012-2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V6zm12.553 1.106A1 1 0 0014 8v4a1 1 0 00.553.894l2 1A1 1 0 0018 13V7a1 1 0 00-1.447-.894l-2 1z"/>
              <path v-else-if="amenity === 'minibar'" d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z"/>
              <path v-else-if="amenity === 'pool'" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"/>
              <path v-else-if="amenity === 'breakfast'" d="M4 2a1 1 0 011 1v2.268l4.562-2.634a1 1 0 011 1.732L6 8v8a1 1 0 11-2 0V8L1.438 5.366a1 1 0 011-1.732L7 5.268V3a1 1 0 011-1h4zm10 0a1 1 0 011 1v14a1 1 0 11-2 0V3a1 1 0 011-1zm3 2a1 1 0 011 1v10a1 1 0 11-2 0V5a1 1 0 011-1z"/>
              <path v-else-if="amenity === 'pets'" d="M4 4a2 2 0 00-2 2v4a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2H4zm10 6a2 2 0 11-4 0 2 2 0 014 0z"/>
              <path v-else d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
            </svg>
          </div>
          <span v-if="room.amenities.length > 3" class="text-xs text-gray-400">
            +{{ room.amenities.length - 3 }} more
          </span>
        </div>
        
        <!-- Price & Book Button -->
        <div class="flex items-center justify-between mt-auto pt-4 border-t border-gray-100">
          <div>
            <span class="text-2xl font-bold text-[#0f766e]">${{ room.price }}</span>
            <span class="text-sm text-gray-500 ml-1">/night</span>
          </div>
           <router-link
    :to="{ name: 'RoomDetail', params: { id: room.id } }"
    class="block cursor-pointer"
  >
          <button 
            class="flex items-center justify-center rounded-xl h-12 px-6 bg-[#0f766e] text-white text-sm font-bold tracking-wide hover:bg-teal-700 transition-colors shadow-lg hover:shadow-xl group-hover:bg-teal-800"
            @click.prevent="$emit('book', room)"
          >
            Book Now
          </button>
          </router-link>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  room: {
    type: Object,
    required: true,
    default: () => ({
      id: '',
      title: 'Room',
      description: '',
      price: 0,
      image: '',
      category: 'standard',
      capacity: '2 Guests',
      featured: false,
      status: 'available',
      amenities: [],
      reviews: {}
    })
  }
})

const emit = defineEmits(['book'])

// Handle image loading errors
const handleImageError = (event) => {
  event.target.src = '/default-room.jpg'
}

// Display only first 3 amenities to avoid clutter
const displayedAmenities = computed(() => {
  return props.room.amenities ? props.room.amenities.slice(0, 3) : []
})

// Map amenity keys to human-readable names
const getAmenityName = (amenityKey) => {
  const amenityMap = {
    'wifi': 'Free WiFi',
    'ac': 'Air Conditioning',
    'tv': 'Flat Screen TV',
    'minibar': 'Minibar',
    'pool': 'Pool Access',
    'breakfast': 'Free Breakfast',
    'pets': 'Pet Friendly'
  }
  return amenityMap[amenityKey] || amenityKey
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Smooth transitions for all interactive elements */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}
</style>