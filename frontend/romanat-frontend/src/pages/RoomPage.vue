<template>
    <div class="container mt-24 mx-auto px-4 py-8">
      <!-- Page Heading -->
      <div class="flex flex-col gap-3 mb-12 text-center">
        <h1 class="text-5xl font-serif font-bold text-[#0f766e] tracking-tighter drop-shadow-sm">Explore Our Rooms</h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">Discover the perfect sanctuary for your luxurious stay, where comfort meets elegance in every detail.</p>
      </div>

      <!-- Search & Filter Bar -->
      <div class="flex flex-col md:flex-row gap-4 mb-8">
        <div class="relative flex-1">
          <input 
            type="text" 
            placeholder="Search by room name..."
            v-model="searchQuery"
            class="w-full rounded-2xl border-2 border-teal-100 pl-4 py-4 bg-white focus:border-teal-300 focus:ring-4 focus:ring-teal-100 shadow-sm hover:shadow-md transition-all duration-300"
          />
        </div>
        
        <!-- Additional filters -->
        <div class="flex gap-4">
          <select 
            v-model="selectedRoomType"
            class="rounded-2xl border-2 border-teal-100 px-4 py-4 bg-white focus:border-teal-300 focus:ring-4 focus:ring-teal-100 shadow-sm hover:shadow-md transition-all duration-300"
          >
            <option value="">All Types</option>
            <option v-for="type in roomTypes" :key="type" :value="type">{{ type }}</option>
          </select>
          
          <select 
            v-model="sortBy"
            class="rounded-2xl border-2 border-teal-100 px-4 py-4 bg-white focus:border-teal-300 focus:ring-4 focus:ring-teal-100 shadow-sm hover:shadow-md transition-all duration-300"
          >
            <option value="default">Sort By</option>
            <option value="price-low">Price: Low to High</option>
            <option value="price-high">Price: High to Low</option>
            <option value="name">Name A-Z</option>
          </select>
        </div>
      </div>

      <!-- Filter Chips -->
      <div class="flex gap-3 mb-12 overflow-x-auto pb-4 px-2 scrollbar-hide">
        <button 
          v-for="filter in filters" 
          :key="filter.id"
          @click="setActiveFilter(filter.id)"
          :class="['flex h-12 shrink-0 items-center justify-center gap-x-3 rounded-full px-6 transition-all duration-300 transform hover:scale-105 border-2', 
                  activeFilter === filter.id 
                  ? 'bg-gradient-to-r from-teal-600 to-teal-700 text-white border-teal-600 shadow-lg' 
                  : 'bg-white text-gray-700 border-teal-100 hover:border-teal-300 hover:bg-teal-50 shadow-md hover:shadow-lg']"
        >
          <span class="text-sm font-semibold whitespace-nowrap">{{ filter.name }}</span>
          <div v-if="activeFilter === filter.id" class="w-2 h-2 bg-white rounded-full"></div>
        </button>
      </div>

      <!-- Rooms Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
        <RoomCard 
          v-for="room in filteredRooms" 
          :key="room.id" 
          :room="room"
          @book="bookRoom"
        />
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center py-16">
        <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-teal-600"></div>
      </div>

      <!-- Empty State -->
      <div v-if="!loading && filteredRooms.length === 0" class="text-center py-16">
        <div class="max-w-md mx-auto">
          <svg class="w-24 h-24 text-gray-300 mx-auto mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
          </svg>
          <h3 class="text-2xl font-semibold text-gray-600 mb-3">No Rooms Available</h3>
          <p class="text-gray-500 mb-6">We couldn't find any rooms matching your criteria. Try adjusting your search filters.</p>
          <button 
            @click="resetFilters"
            class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-teal-600 text-white font-semibold hover:bg-teal-700 transition-colors shadow-md hover:shadow-lg"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
            </svg>
            Reset Filters
          </button>
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import RoomCard from '../components/Room/RoomCard.vue'
import LandingLayout from '../layouts/LandingLayout.vue'

// Reactive data
const activeFilter = ref('all')
const rooms = ref([])
const loading = ref(true)
const searchQuery = ref('')
const selectedRoomType = ref('')
const sortBy = ref('default')

// Filters array
const filters = [
  { id: 'all', name: 'All Rooms' },
  { id: 'price', name: 'Sort by Price' },
  { id: 'type', name: 'Room Type' },
  { id: 'amenities', name: 'Amenities' }
]

// Fetch rooms from API
const fetchRooms = async () => {
  try {
    loading.value = true
    const { data } = await axios.get('http://127.0.0.1:8000/api/rooms/')
    
    // Enhanced room data mapping with fallbacks
    rooms.value = data.result.map(r => ({
      id: r.id,
      title: r.title || `Room ${r.room_number}`,
      description: r.description || 'No description available',
      price: parseFloat(r.price) || 0,
      image: r.thumbnail || (r.images && r.images.length ? r.images[0] : '/default-room.jpg'),
      category: r.category ? r.category.toLowerCase() : 'standard',
      capacity: r.capacity || '2 Guests',
      featured: r.featured || false,
      status: r.status || 'available',
      notes: r.notes || '',
      room_number: r.room_number || `Room ${r.id}` // Added room_number for search
    }))
  } catch (error) {
    console.error('Failed to fetch rooms:', error)
    // Set empty array on error
    rooms.value = []
  } finally {
    loading.value = false
  }
}

// Get unique room types for filter dropdown
const roomTypes = computed(() => {
  const types = [...new Set(rooms.value.map(room => room.category))]
  return types.map(type => type.charAt(0).toUpperCase() + type.slice(1))
})

// Main filtered rooms computation
const filteredRooms = computed(() => {
  let result = [...rooms.value]

  // Apply search filter
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.toLowerCase().trim()
    result = result.filter(room =>
      room.title.toLowerCase().includes(query) ||
      (room.room_number && room.room_number.toLowerCase().includes(query)) ||
      room.description.toLowerCase().includes(query)
    )
  }

  // Apply room type filter
  if (selectedRoomType.value) {
    const type = selectedRoomType.value.toLowerCase()
    result = result.filter(room => room.category === type)
  }

  // Apply active filter chip
  if (activeFilter.value === 'price') {
    result.sort((a, b) => a.price - b.price)
  } else if (activeFilter.value === 'type') {
    result.sort((a, b) => a.category.localeCompare(b.category))
  }

  // Apply additional sorting
  switch (sortBy.value) {
    case 'price-low':
      result.sort((a, b) => a.price - b.price)
      break
    case 'price-high':
      result.sort((a, b) => b.price - a.price)
      break
    case 'name':
      result.sort((a, b) => a.title.localeCompare(b.title))
      break
    default:
      // Default sorting (by ID or keep original order)
      break
  }

  return result
})

// Methods
const setActiveFilter = (filterId) => {
  activeFilter.value = filterId
  
  // Auto-set sortBy when price filter is selected
  if (filterId === 'price') {
    sortBy.value = 'price-low'
  }
}

const resetFilters = () => {
  activeFilter.value = 'all'
  searchQuery.value = ''
  selectedRoomType.value = ''
  sortBy.value = 'default'
}

const bookRoom = (room) => {
  console.log('Booking room:', room)
  // Navigate to booking page or open booking modal
  // Example: router.push(`/booking/${room.id}`)
}

// Lifecycle
onMounted(() => {
  fetchRooms()
})
</script>

<style scoped>
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

/* Custom select styling */
select {
  appearance: none;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="%230f766e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>');
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 16px;
  padding-right: 40px;
}
</style>