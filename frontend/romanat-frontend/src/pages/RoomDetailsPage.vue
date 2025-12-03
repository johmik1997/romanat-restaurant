<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <!-- Back Button -->
    <div class="mb-6">
      <button 
        @click="$router.back()" 
        class="flex items-center gap-2 text-gray-600 hover:text-gray-900 transition-colors"
      >
        <span class="material-symbols-outlined text-lg">arrow_back</span>
        Back to Room Management
      </button>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900">Room Details</h1>
        <p class="text-gray-600 mt-2">Complete information about room {{ room?.room_number }}</p>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center py-12">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto"></div>
        <p class="mt-4 text-gray-600">Loading room details...</p>
      </div>

      <!-- Room Details -->
      <div v-else-if="room" class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Left Column - Images & Basic Info -->
        <div class="lg:col-span-2 space-y-6">
          <!-- Image Carousel -->
          <RoomImageCarousel :images="roomImages" />

          <!-- Title and Subtitle -->
          <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div class="mb-4">
              <h2 class="text-2xl font-bold text-gray-900 mb-2">
                {{ room.title || `Room ${room.room_number}` }}
              </h2>
              <p v-if="room.subtitle" class="text-lg text-gray-600">
                {{ room.subtitle }}
              </p>
              <p v-else class="text-gray-500 italic">No subtitle provided</p>
            </div>
          </div>

          <!-- Room Tabs -->
          <RoomTabs :room="room" />

          <!-- Additional Images -->
          <div v-if="room.images && room.images.length > 0" class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Gallery</h3>
            <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
              <img 
                v-for="(image, index) in room.images" 
                :key="index"
                :src="image" 
                :alt="`Room ${room.room_number} image ${index + 1}`"
                class="w-full h-32 object-cover rounded-lg cursor-pointer hover:opacity-80 transition-opacity"
                @click="openImageModal(image)"
              />
            </div>
          </div>

          <!-- Description -->
          <div v-if="room.description" class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Description</h3>
            <p class="text-gray-700 leading-relaxed">{{ room.description }}</p>
          </div>

          <!-- About -->
          <div v-if="room.about" class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">About This Room</h3>
            <p class="text-gray-700 leading-relaxed">{{ room.about }}</p>
          </div>

          <!-- Notes -->
          <div v-if="room.notes" class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Special Notes</h3>
            <p class="text-gray-700 leading-relaxed">{{ room.notes }}</p>
          </div>
        </div>

        <!-- Right Column - Details & Actions -->
        <div class="space-y-6">
          <!-- Room Info Card -->
          <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div class="flex justify-between items-start mb-4">
              <div>
                <h2 class="text-xl font-bold text-gray-900">Room {{ room.room_number }}</h2>
                <p class="text-gray-600">{{ room.room_type?.name }}</p>
              </div>
              <span :class="statusBadgeClasses(room.status)" class="text-sm">
                {{ formatStatus(room.status) }}
              </span>
            </div>
            
            <!-- Pricing -->
            <div class="mb-6">
              <div class="flex items-baseline gap-2">
                <span class="text-3xl font-bold text-gray-900">${{ room.price }}</span>
                <span class="text-gray-500">per night</span>
              </div>
            </div>

            <!-- Details Grid -->
            <div class="grid grid-cols-2 gap-4 mb-6">
              <div>
                <span class="text-sm text-gray-500 block">Floor</span>
                <span class="font-medium text-gray-900">{{ room.floor }}</span>
              </div>
              <div>
                <span class="text-sm text-gray-500 block">Category</span>
                <span :class="categoryBadgeClasses(room.category)" class="text-xs">
                  {{ room.category }}
                </span>
              </div>
              <div>
                <span class="text-sm text-gray-500 block">Size</span>
                <span class="font-medium text-gray-900">{{ room.size }} m²</span>
              </div>
              <div>
                <span class="text-sm text-gray-500 block">Capacity</span>
                <span class="font-medium text-gray-900">{{ room.capacity }} Guests</span>
              </div>
              <div>
                <span class="text-sm text-gray-500 block">View</span>
                <span class="font-medium text-gray-900">{{ room.view }}</span>
              </div>
              <div>
                <span class="text-sm text-gray-500 block">Featured</span>
                <span class="font-medium text-gray-900">{{ room.featured ? 'Yes' : 'No' }}</span>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex gap-3 pt-4 border-t border-gray-200">
              <button 
                @click="handleEditRoom"
                class="flex-1 bg-primary text-white py-2 px-4 rounded-lg hover:bg-primary/90 transition-colors flex items-center justify-center gap-2"
              >
                <span class="material-symbols-outlined text-lg">edit</span>
                Edit Room
              </button>
              <button 
                @click="handleDeleteRoom"
                class="flex-1 bg-red-600 text-white py-2 px-4 rounded-lg hover:bg-red-700 transition-colors flex items-center justify-center gap-2"
              >
                <span class="material-symbols-outlined text-lg">delete</span>
                Delete
              </button>
            </div>
          </div>

          <!-- Booking Widget -->
          <RoomBookingWidget :room="room" />

          <!-- Amenities -->
          <div v-if="room.amenities && room.amenities.length > 0" class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Amenities</h3>
            <div class="grid grid-cols-2 gap-3">
              <div 
                v-for="amenity in room.amenities" 
                :key="amenity"
                class="flex items-center gap-2 text-gray-700"
              >
                <span class="material-symbols-outlined text-primary text-lg">check_circle</span>
                <span class="text-sm">{{ amenity }}</span>
              </div>
            </div>
          </div>

          <!-- Reviews -->
          <div v-if="room.reviews && room.reviews.length > 0" class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Guest Reviews</h3>
            <div class="space-y-4">
              <div 
                v-for="review in room.reviews" 
                :key="review.id"
                class="border-l-4 border-primary pl-4 py-2"
              >
                <div class="flex items-center gap-2 mb-2">
                  <div class="flex text-yellow-400">
                    <span 
                      v-for="star in 5" 
                      :key="star"
                      class="material-symbols-outlined text-sm"
                      :class="star <= review.rating ? 'fill' : ''"
                    >
                      star
                    </span>
                  </div>
                  <span class="text-sm text-gray-500">{{ formatDate(review.created_at) }}</span>
                </div>
                <p class="text-gray-700 text-sm">{{ review.comment }}</p>
                <p class="text-gray-600 text-xs mt-1">- {{ review.guest_name }}</p>
              </div>
            </div>
          </div>

          <!-- No Reviews -->
          <div v-else class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">Guest Reviews</h3>
            <div class="text-center py-4">
              <span class="material-symbols-outlined text-4xl text-gray-300 mb-2">reviews</span>
              <p class="text-gray-500">No reviews yet</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="text-center py-12">
        <span class="material-symbols-outlined text-6xl text-red-300 mb-4">error</span>
        <h3 class="text-lg font-medium text-gray-900 mb-2">Room not found</h3>
        <p class="text-gray-500 mb-4">{{ error }}</p>
        <button 
          @click="$router.back()" 
          class="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/90 transition-colors"
        >
          Go Back
        </button>
      </div>
    </div>

    <!-- Image Modal -->
    <div 
      v-if="selectedImage" 
      class="fixed inset-0 bg-black bg-opacity-90 z-50 flex items-center justify-center"
      @click="selectedImage = null"
    >
      <div class="relative max-w-4xl max-h-full">
        <button 
          @click="selectedImage = null"
          class="absolute top-4 right-4 text-white hover:text-gray-300 z-10"
        >
          <span class="material-symbols-outlined text-3xl">close</span>
        </button>
        <img 
          :src="selectedImage" 
          alt="Enlarged room view"
          class="max-w-full max-h-screen object-contain"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { fetchRoomById } from '../api/auth/roomApi'
import RoomBookingWidget from '../components/Room/RoomBookingWidget.vue'
import RoomImageCarousel from '../components/Room/RoomImageCarousel.vue'
import RoomTabs from '../components/Room/RoomTabs.vue'

export default {
  name: 'RoomDetails',
  components: {
    RoomTabs,
    RoomImageCarousel,
    RoomBookingWidget
  },
  data() {
    return {
      room: null,
      loading: false,
      error: null,
      selectedImage: null
    }
  },
  computed: {
    roomImages() {
      if (!this.room) return []
      
      const images = []
      if (this.room.thumbnail) {
        images.push(this.room.thumbnail)
      }
      if (this.room.images && this.room.images.length > 0) {
        images.push(...this.room.images)
      }
      
      return images.length > 0 ? images : []
    }
  },
  async mounted() {
    await this.loadRoomDetails()
  },
  methods: {
    async loadRoomDetails() {
      const roomId = this.$route.params.id
      
      if (!roomId) {
        this.error = 'Room ID is required'
        return
      }

      try {
        this.loading = true
        this.error = null
        
        const response = await fetchRoomById(roomId)
        
        if (response && response.id) {
          this.room = response
        } else {
          this.error = 'Room not found'
        }
      } catch (error) {
        console.error('Error loading room details:', error)
        this.error = 'Failed to load room details. Please try again.'
      } finally {
        this.loading = false
      }
    },

    formatStatus(status) {
      const statusMap = {
        'available': 'Available',
        'occupied': 'Occupied',
        'reserved': 'Reserved',
        'maintenance': 'Maintenance',
        'cleaning': 'Cleaning'
      }
      return statusMap[status] || status
    },

    statusBadgeClasses(status) {
      const formattedStatus = this.formatStatus(status)
      const classes = {
        'Available': 'inline-flex px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800',
        'Occupied': 'inline-flex px-3 py-1 rounded-full text-xs font-medium bg-red-100 text-red-800',
        'Reserved': 'inline-flex px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800',
        'Maintenance': 'inline-flex px-3 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800',
        'Cleaning': 'inline-flex px-3 py-1 rounded-full text-xs font-medium bg-purple-100 text-purple-800'
      }
      return classes[formattedStatus] || classes['Available']
    },

    categoryBadgeClasses(category) {
      const classes = {
        'normal': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800',
        'deluxe': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800',
        'suite': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800',
        'executive': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800',
        'presidential': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800'
      }
      return classes[category] || classes['normal']
    },

    openImageModal(image) {
      this.selectedImage = image
    },

    handleEditRoom() {
      if (this.room) {
        this.$router.push(`/rooms/edit/${this.room.id}`)
      }
    },

    handleDeleteRoom() {
      if (this.room && confirm(`Are you sure you want to delete room ${this.room.room_number}? This action cannot be undone.`)) {
        console.log('Delete room:', this.room.id)
        this.$router.push('/rooms')
      }
    },

    formatDate(dateString) {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    }
  }
}
</script>

<style scoped>
.material-symbols-outlined.fill {
  font-variation-settings: 'FILL' 1;
}
</style>