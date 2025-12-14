<template>
  <section id="rooms" class="w-full bg-background-light py-20">
    <div class="container mx-auto max-w-7xl px-4">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <div class="inline-flex items-center gap-2 bg-primary/10 text-[#0f766e]  rounded-full px-4 py-2 mb-6">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/>
          </svg>
          <span class="text-sm font-semibold">Luxury Accommodations</span>
        </div>
        <h2 class="text-[#0f766e] text-4xl font-serif font-bold mb-4">
          Discover Your Perfect Retreat
        </h2>
        <p class="max-w-2xl mx-auto text-gray-600 text-lg">
          Each of our meticulously designed rooms offers a unique blend of comfort, luxury, and breathtaking views tailored to create unforgettable experiences.
        </p>
      </div>

      <!-- Room Filter Tabs -->
      <div class="flex flex-wrap justify-center gap-4 mb-12">
        <button
          v-for="category in roomCategories"
          :key="category.id"
          @click="setActiveCategory(category.id)"
          class="px-6 py-3 rounded-full font-medium transition-all duration-300"
          :class="activeCategory === category.id 
            ? 'bg-[#0f766e]  text-white shadow-lg' 
            : 'bg-white text-gray-600 hover:bg-gray-50 border border-gray-200'"
        >
          {{ category.name }}
        </button>
      </div>

      <!-- Rooms Grid/Scroll -->
      <div class="relative">
        <!-- Scrollable Container -->
        <div class="overflow-x-auto scrollbar-hide pb-6">
          <div class="flex gap-8 w-min px-6">
            <div 
              v-for="room in filteredRooms" 
              :key="room.id"
              class="room-card group bg-white rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 flex-shrink-0 w-80"
            >
              <div class="relative h-72 overflow-hidden">
                <img 
                  :src="room.image" 
                  :alt="room.title" 
                  class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                />
                <div class="absolute inset-0 bg-gradient-to from-black/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                 <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                  <span class="bg-primary text-white text-xs px-3 py-1 rounded-full font-medium">
                    {{ room.size }}
                  </span>
                  <span v-if="room.featured" class="bg-accent text-white text-xs px-3 py-1 rounded-full font-medium">
                    Featured
                  </span>
                </div>

                <button 
                  class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm text-primary p-2 rounded-full opacity-0 group-hover:opacity-100 transition-all duration-300 hover:bg-white hover:scale-110"
                  @click.stop="quickView(room)"
                >
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                  </svg>
                </button>
              </div>

              <!-- Room Content -->
              <div class="p-6">
                <!-- Title and Subtitle -->
                <div class="mb-4">
                  <h3 class="text-xl font-bold text-gray-800 mb-1 group-hover:text-primary transition-colors">
                    {{ room.title }}
                  </h3>
                  <p class="text-secondary font-medium">{{ room.subtitle }}</p>
                </div>

                <!-- Description -->
                <p class="text-gray-600 text-sm mb-6 leading-relaxed">
                  {{ room.description }}
                </p>

                <!-- Room Features -->
                <div class="flex items-center gap-4 text-sm text-gray-500 mb-6">
                  <div class="flex items-center gap-1">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
                      <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
                    </svg>
                    {{ room.view }}
                  </div>
                  <div class="flex items-center gap-1">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" clip-rule="evenodd"/>
                    </svg>
                    {{ room.capacity }}
                  </div>
                </div>

                <!-- Price and CTA -->
                <div class="flex items-center justify-between">
                  <div>
                    <span class="text-2xl font-bold text-primary">
                      ${{ room.price }}<span class="text-sm font-normal text-gray-500">/night</span>
                    </span>
                    <p class="text-xs text-gray-500 mt-1">Including taxes & fees</p>
                  </div>
                 <!-- In your existing RoomCard.vue, update the "View Details" button: -->
<router-link 
  :to="`/rooms/${room.id}`"
  class="bg-[#0f766e] text-white px-4 py-3 rounded-xl font-semibold hover:bg-teal-700 transition-all duration-300 hover:scale-105 shadow-lg hover:shadow-xl flex items-center gap-2"
>
  <span>View Details</span>
  <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
  </svg>
</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Navigation Arrows -->
        <button 
          @click="scrollLeft"
          class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-white/90 backdrop-blur-sm border border-gray-200 rounded-full p-3 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110 opacity-0 group-hover:opacity-100"
          :class="{ 'opacity-50 cursor-not-allowed': isAtStart }"
        >
          <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
          </svg>
        </button>
        <button 
          @click="scrollRight"
          class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-white/90 backdrop-blur-sm border border-gray-200 rounded-full p-3 shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110 opacity-0 group-hover:opacity-100"
          :class="{ 'opacity-50 cursor-not-allowed': isAtEnd }"
        >
          <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </button>
      </div>

      <!-- View More Button -->
      <div class="text-center mt-12" v-if="hasMoreRooms">
        <button
          @click="loadMoreRooms"
          class="bg-[#0f766e]  text-white px-4 py-2 rounded-xl font-semibold hover:bg-teal-700 transition-all duration-300 hover:scale-105 shadow-lg hover:shadow-xl flex items-center gap-3 mx-auto"
        >
         <router-link 
      to="/rooms">
      <span>Discover More Rooms</span>
    </router-link>
         
        </button>
      </div>

      <!-- Room Count -->
      <div class="text-center mt-8">
        <p class="text-gray-500 text-sm">
          Showing {{ displayedRooms.length }} of {{ filteredRooms.length }} rooms
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const rooms = ref([])
const roomCategories = [
  { id: 'all', name: 'All Rooms' },
  { id: 'suite', name: 'Suites' },
  { id: 'standard', name: 'Standard' },
  { id: 'family', name: 'Family' }
]

const activeCategory = ref('all')
const displayedCount = ref(3)
const scrollContainer = ref(null)
const isAtStart = ref(true)
const isAtEnd = ref(false)

// Fetch rooms from API
const fetchRooms = async () => {
  try {
    const { data } = await axios.get('https://romanat-restaurant-7.onrender.com/api/rooms/')
    // Map API fields to frontend structure
    rooms.value = data.map(r => ({
      id: r.id,
      room_number: r.room_number,
      title: r.title || `Room ${r.room_number}`,
      subtitle: r.subtitle || '',
      description: r.description || '',
      price: parseFloat(r.price),
      image: r.thumbnail || (r.images.length ? r.images[0] : 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80'),
      images: r.images,
      category: r.category.toLowerCase(),
      size: r.size || '',
      view: r.view || '',
      capacity: r.capacity || '',
      featured: r.featured,
      status: r.status,
      notes: r.notes || ''
    }))
  } catch (error) {
    console.error('Failed to fetch rooms:', error)
  }
}

const filteredRooms = computed(() => {
  if (activeCategory.value === 'all') return rooms.value
  return rooms.value.filter(room => room.category === activeCategory.value)
})

const displayedRooms = computed(() => filteredRooms.value.slice(0, displayedCount.value))
const hasMoreRooms = computed(() => displayedRooms.value.length < filteredRooms.value.length)

const setActiveCategory = (categoryId) => {
  activeCategory.value = categoryId
  displayedCount.value = 3
}

const viewRoomDetails = (room) => {
  console.log('Viewing room details:', room)
}

const quickView = (room) => {
  console.log('Quick view:', room)
}

const loadMoreRooms = () => {
  displayedCount.value += 3
}

const scrollLeft = () => {
  if (scrollContainer.value) scrollContainer.value.scrollBy({ left: -320, behavior: 'smooth' })
}

const scrollRight = () => {
  if (scrollContainer.value) scrollContainer.value.scrollBy({ left: 320, behavior: 'smooth' })
}

const updateScrollState = () => {
  if (scrollContainer.value) {
    const { scrollLeft, scrollWidth, clientWidth } = scrollContainer.value
    isAtStart.value = scrollLeft === 0
    isAtEnd.value = scrollLeft + clientWidth >= scrollWidth - 10
  }
}

onMounted(() => {
  scrollContainer.value = document.querySelector('.overflow-x-auto')
  if (scrollContainer.value) {
    scrollContainer.value.addEventListener('scroll', updateScrollState)
    updateScrollState()
  }
  fetchRooms()
})
</script>


<style scoped>
.room-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.room-card:hover {
  transform: translateY(-8px);
}

/* Hide scrollbar for modern browsers */
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Smooth scrolling */
.overflow-x-auto {
  scroll-behavior: smooth;
}
</style>