<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <!-- Header with Breadcrumb -->
    <div class="mb-6">
      <nav class="flex items-center gap-2 text-sm text-gray-600 mb-4">
        <router-link to="/staff/dashboard" class="hover:text-gray-900">Dashboard</router-link>
        <span class="material-symbols-outlined text-lg">chevron_right</span>
        <router-link to="/staff/rooms" class="hover:text-gray-900">Room Management</router-link>
        <span class="material-symbols-outlined text-lg">chevron_right</span>
        <span class="text-gray-900">Room {{ room?.room_number }}</span>
      </nav>
      
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">Room {{ room?.room_number }} - Details</h1>
          <p class="text-gray-600 mt-2">Complete room information and management</p>
        </div>
        <button 
          @click="$router.back()" 
          class="flex items-center gap-2 text-gray-600 hover:text-gray-900 transition-colors bg-white px-4 py-2 rounded-lg border border-gray-300 hover:border-gray-400"
        >
          <span class="material-symbols-outlined text-lg">arrow_back</span>
          Back to Rooms
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto"></div>
      <p class="mt-4 text-gray-600">Loading room details...</p>
    </div>

    <!-- Room Details -->
    <div v-else-if="room" class="space-y-6">
      <!-- Quick Stats Bar -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div class="bg-white rounded-xl p-4 border border-gray-200 shadow-sm">
          <div class="flex items-center gap-3">
            <div class="p-2 bg-blue-100 rounded-lg">
              <span class="material-symbols-outlined text-blue-600">calendar_month</span>
            </div>
            <div>
              <p class="text-sm text-gray-600">Status</p>
              <p :class="statusTextClasses(room.status)" class="font-semibold">
                {{ formatStatus(room.status) }}
              </p>
            </div>
          </div>
        </div>
        
        <div class="bg-white rounded-xl p-4 border border-gray-200 shadow-sm">
          <div class="flex items-center gap-3">
            <div class="p-2 bg-green-100 rounded-lg">
              <span class="material-symbols-outlined text-green-600">attach_money</span>
            </div>
            <div>
              <p class="text-sm text-gray-600">Revenue (Today)</p>
              <p class="text-lg font-semibold text-gray-900">${{ calculateTodayRevenue() }}</p>
            </div>
          </div>
        </div>
        
        <div class="bg-white rounded-xl p-4 border border-gray-200 shadow-sm">
          <div class="flex items-center gap-3">
            <div class="p-2 bg-purple-100 rounded-lg">
              <span class="material-symbols-outlined text-purple-600">bed</span>
            </div>
            <div>
              <p class="text-sm text-gray-600">Occupancy Rate</p>
              <p class="text-lg font-semibold text-gray-900">{{ calculateOccupancyRate() }}%</p>
            </div>
          </div>
        </div>
        
        <div class="bg-white rounded-xl p-4 border border-gray-200 shadow-sm">
          <div class="flex items-center gap-3">
            <div class="p-2 bg-orange-100 rounded-lg">
              <span class="material-symbols-outlined text-orange-600">star</span>
            </div>
            <div>
              <p class="text-sm text-gray-600">Rating</p>
              <p class="text-lg font-semibold text-gray-900">{{ averageRating }}/5</p>
            </div>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Left Column - Room Information -->
        <div class="lg:col-span-2 space-y-6">
          <!-- Image and Basic Info -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
            <RoomImageCarousel :images="roomImages" />
            <div class="p-6">
              <div class="flex items-start justify-between mb-4">
                <div>
                  <h2 class="text-2xl font-bold text-gray-900">{{ room.room_number }}</h2>
                  <p class="text-gray-600">{{ room.room_type?.name }}</p>
                </div>
                <div class="text-right">
                  <p class="text-3xl font-bold text-primary">${{ room.price }}</p>
                  <p class="text-gray-500">per night</p>
                </div>
              </div>
              
              <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
                <div>
                  <p class="text-sm text-gray-500">Floor</p>
                  <p class="font-semibold">{{ room.floor }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-500">Capacity</p>
                  <p class="font-semibold">{{ room.capacity }} Guests</p>
                </div>
                <div>
                  <p class="text-sm text-gray-500">Size</p>
                  <p class="font-semibold">{{ room.size }} m²</p>
                </div>
                <div>
                  <p class="text-sm text-gray-500">Category</p>
                  <span :class="categoryBadgeClasses(room.category)" class="text-xs">
                    {{ room.category }}
                  </span>
                </div>
              </div>
              
              <div class="flex gap-2">
                <span :class="statusBadgeClasses(room.status)" class="text-sm">
                  {{ formatStatus(room.status) }}
                </span>
                <span v-if="room.featured" class="inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">
                  Featured
                </span>
                <span v-if="room.view" class="inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                  {{ room.view }} View
                </span>
              </div>
            </div>
          </div>

          <!-- Room Management Tabs -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
            <div class="border-b border-gray-200">
              <nav class="flex -mb-px">
                <button
                  v-for="tab in managementTabs"
                  :key="tab.id"
                  @click="activeManagementTab = tab.id"
                  class="px-6 py-4 border-b-2 font-medium text-sm transition-colors duration-300"
                  :class="activeManagementTab === tab.id
                    ? 'border-primary text-primary'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'"
                >
                  {{ tab.name }}
                </button>
              </nav>
            </div>

            <div class="p-6">
              <!-- Details Tab -->
              <div v-if="activeManagementTab === 'details'">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <h4 class="font-semibold text-gray-900 mb-3">Room Information</h4>
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="text-gray-600">Room Number:</span>
                        <span class="font-medium">{{ room.room_number }}</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="text-gray-600">Room Type:</span>
                        <span class="font-medium">{{ room.room_type?.name }}</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="text-gray-600">Floor:</span>
                        <span class="font-medium">{{ room.floor }}</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="text-gray-600">Category:</span>
                        <span class="font-medium capitalize">{{ room.category }}</span>
                      </div>
                    </div>
                  </div>
                  
                  <div>
                    <h4 class="font-semibold text-gray-900 mb-3">Specifications</h4>
                    <div class="space-y-3">
                      <div class="flex justify-between">
                        <span class="text-gray-600">Size:</span>
                        <span class="font-medium">{{ room.size }} m²</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="text-gray-600">Capacity:</span>
                        <span class="font-medium">{{ room.capacity }} guests</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="text-gray-600">View:</span>
                        <span class="font-medium">{{ room.view || 'Standard' }}</span>
                      </div>
                      <div class="flex justify-between">
                        <span class="text-gray-600">Featured:</span>
                        <span class="font-medium">{{ room.featured ? 'Yes' : 'No' }}</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Description -->
                <div v-if="room.description" class="mt-6">
                  <h4 class="font-semibold text-gray-900 mb-3">Description</h4>
                  <p class="text-gray-700 leading-relaxed">{{ room.description }}</p>
                </div>

                <!-- Notes -->
                <div v-if="room.notes" class="mt-6">
                  <h4 class="font-semibold text-gray-900 mb-3">Staff Notes</h4>
                  <p class="text-gray-700 leading-relaxed bg-yellow-50 p-4 rounded-lg">{{ room.notes }}</p>
                </div>
              </div>

              <!-- Amenities Tab -->
              <div v-else-if="activeManagementTab === 'amenities'">
                <div class="flex justify-between items-center mb-4">
                  <h4 class="font-semibold text-gray-900">Room Amenities</h4>
                  <button 
                    @click="showAmenitiesModal = true"
                    class="text-sm bg-primary text-white px-3 py-1 rounded-lg hover:bg-primary/90 transition-colors"
                  >
                    Edit Amenities
                  </button>
                </div>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
                  <div 
                    v-for="amenity in room.amenities" 
                    :key="amenity"
                    class="flex items-center gap-2 p-3 bg-gray-50 rounded-lg"
                  >
                    <span class="material-symbols-outlined text-primary text-lg">check_circle</span>
                    <span class="text-sm font-medium text-gray-700 capitalize">{{ amenity }}</span>
                  </div>
                  <div v-if="!room.amenities || room.amenities.length === 0" class="col-span-3 text-center py-4 text-gray-500">
                    No amenities configured
                  </div>
                </div>
              </div>

              <!-- Maintenance Tab -->
              <div v-else-if="activeManagementTab === 'maintenance'">
                <div class="flex justify-between items-center mb-4">
                  <h4 class="font-semibold text-gray-900">Maintenance History</h4>
                  <button 
                    @click="showMaintenanceModal = true"
                    class="text-sm bg-orange-600 text-white px-3 py-1 rounded-lg hover:bg-orange-700 transition-colors flex items-center gap-1"
                  >
                    <span class="material-symbols-outlined text-sm">build</span>
                    Log Maintenance
                  </button>
                </div>
                <div class="space-y-3">
                  <div v-for="item in maintenanceHistory" :key="item.id" class="p-4 border border-gray-200 rounded-lg">
                    <div class="flex justify-between items-start mb-2">
                      <span class="font-medium text-gray-900">{{ item.type }}</span>
                      <span :class="maintenanceStatusClasses(item.status)" class="text-xs">
                        {{ item.status }}
                      </span>
                    </div>
                    <p class="text-sm text-gray-600 mb-2">{{ item.description }}</p>
                    <div class="flex justify-between text-xs text-gray-500">
                      <span>Reported: {{ formatDate(item.reported_date) }}</span>
                      <span>By: {{ item.reported_by }}</span>
                    </div>
                  </div>
                  <div v-if="maintenanceHistory.length === 0" class="text-center py-8 text-gray-500">
                    <span class="material-symbols-outlined text-4xl mb-2">construction</span>
                    <p>No maintenance records</p>
                  </div>
                </div>
              </div>

              <!-- Reservations Tab -->
              <div v-else-if="activeManagementTab === 'reservations'">
                <h4 class="font-semibold text-gray-900 mb-4">Current & Upcoming Reservations</h4>
                <div class="space-y-3">
                  <div v-for="reservation in currentReservations" :key="reservation.id" class="p-4 border border-gray-200 rounded-lg">
                    <div class="flex justify-between items-start mb-2">
                      <div>
                        <p class="font-medium text-gray-900">Reservation #{{ reservation.id }}</p>
                        <p class="text-sm text-gray-600">{{ reservation.guest_name }}</p>
                      </div>
                      <span :class="reservationStatusClasses(reservation.status)" class="text-xs">
                        {{ reservation.status }}
                      </span>
                    </div>
                    <div class="grid grid-cols-2 gap-4 text-sm">
                      <div>
                        <span class="text-gray-500">Check-in:</span>
                        <span class="font-medium ml-2">{{ formatDate(reservation.check_in) }}</span>
                      </div>
                      <div>
                        <span class="text-gray-500">Check-out:</span>
                        <span class="font-medium ml-2">{{ formatDate(reservation.check_out) }}</span>
                      </div>
                      <div>
                        <span class="text-gray-500">Guests:</span>
                        <span class="font-medium ml-2">{{ reservation.guests }}</span>
                      </div>
                      <div>
                        <span class="text-gray-500">Total:</span>
                        <span class="font-medium ml-2">${{ reservation.total_price }}</span>
                      </div>
                    </div>
                  </div>
                  <div v-if="currentReservations.length === 0" class="text-center py-8 text-gray-500">
                    <span class="material-symbols-outlined text-4xl mb-2">event_available</span>
                    <p>No current reservations</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column - Actions & Quick Tools -->
        <div class="space-y-6">
          <!-- Quick Actions -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
            <h3 class="font-semibold text-gray-900 mb-4">Quick Actions</h3>
            <div class="space-y-3">
              <button 
                @click="handleChangeStatus"
                class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-primary hover:bg-primary/5 transition-colors"
              >
                <span class="material-symbols-outlined text-primary">swap_horiz</span>
                <div>
                  <p class="font-medium text-gray-900">Change Status</p>
                  <p class="text-sm text-gray-500">Update room availability</p>
                </div>
              </button>
              
              <button 
                @click="handleEditRoom"
                class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-green-500 hover:bg-green-50 transition-colors"
              >
                <span class="material-symbols-outlined text-green-600">edit</span>
                <div>
                  <p class="font-medium text-gray-900">Edit Room Details</p>
                  <p class="text-sm text-gray-500">Modify room information</p>
                </div>
              </button>
              
              <button 
                @click="handleQuickClean"
                class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-purple-500 hover:bg-purple-50 transition-colors"
              >
                <span class="material-symbols-outlined text-purple-600">cleaning_services</span>
                <div>
                  <p class="font-medium text-gray-900">Mark as Cleaned</p>
                  <p class="text-sm text-gray-500">Update cleaning status</p>
                </div>
              </button>
              
              <button 
                @click="handleGenerateReport"
                class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-blue-500 hover:bg-blue-50 transition-colors"
              >
                <span class="material-symbols-outlined text-blue-600">summarize</span>
                <div>
                  <p class="font-medium text-gray-900">Generate Report</p>
                  <p class="text-sm text-gray-500">Room performance analytics</p>
                </div>
              </button>
            </div>
          </div>

          <!-- Room Status Widget -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-6">
            <h3 class="font-semibold text-gray-900 mb-4">Room Status</h3>
            <div class="space-y-4">
              <div class="flex justify-between items-center">
                <span class="text-gray-600">Current Status:</span>
                <span :class="statusBadgeClasses(room.status)" class="text-sm">
                  {{ formatStatus(room.status) }}
                </span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-600">Last Cleaned:</span>
                <span class="font-medium">{{ lastCleaned }}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-600">Next Reservation:</span>
                <span class="font-medium">{{ nextReservation || 'None' }}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-600">Maintenance Due:</span>
                <span class="font-medium text-green-600">{{ maintenanceDue || 'Up to date' }}</span>
              </div>
            </div>
          </div>

          <!-- Danger Zone -->
          <div class="bg-white rounded-xl border border-red-200 shadow-sm p-6">
            <h3 class="font-semibold text-red-800 mb-4">Danger Zone</h3>
            <p class="text-sm text-gray-600 mb-4">Irreversible actions. Proceed with caution.</p>
            <div class="space-y-3">
              <button 
                @click="handleDeleteRoom"
                class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-red-200 bg-red-50 hover:bg-red-100 transition-colors text-red-700"
              >
                <span class="material-symbols-outlined">delete</span>
                <div>
                  <p class="font-medium">Delete Room</p>
                  <p class="text-sm">Permanently remove this room</p>
                </div>
              </button>
              
              <button 
                @click="handleTempClose"
                class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-orange-200 bg-orange-50 hover:bg-orange-100 transition-colors text-orange-700"
              >
                <span class="material-symbols-outlined">lock</span>
                <div>
                  <p class="font-medium">Temporarily Close</p>
                  <p class="text-sm">Make room unavailable</p>
                </div>
              </button>
            </div>
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

    <!-- Modals -->
    <RoomModal
      :isOpen="showEditModal"
      :room="room"
      @close="showEditModal = false"
      @update-room="handleUpdateRoom"
    />

    <ChangeStatusModal
      :isOpen="showStatusModal"
      :room="room"
      @close="showStatusModal = false"
      @status-change="handleStatusChange"
    />

    <MaintenanceModal
      :isOpen="showMaintenanceModal"
      :room="room"
      @close="showMaintenanceModal = false"
      @maintenance-logged="handleMaintenanceLogged"
    />

    <DeleteConfirmationModal
      :isOpen="showDeleteModal"
      :room="room"
      @close="showDeleteModal = false"
      @confirm-delete="handleConfirmDelete"
    />
  </div>
</template>

<script>
import { fetchRoomById } from '../api/auth/roomApi'
import RoomImageCarousel from '../components/Room/RoomImageCarousel.vue'
import RoomModal from '../components/modal/AddNewRoom.vue'
import ChangeStatusModal from '../components/modal/ChangeRoomStatus.vue'
import MaintenanceModal from '../components/modal/MaintenanceRoom.vue'
import DeleteConfirmationModal from '../components/modal/DeleteConfirmationModal.vue'

export default {
  name: 'StaffRoomDetails',
  components: {
    RoomImageCarousel,
    RoomModal,
    ChangeStatusModal,
    MaintenanceModal,
    DeleteConfirmationModal
  },
  data() {
    return {
      room: null,
      loading: false,
      error: null,
      activeManagementTab: 'details',
      showEditModal: false,
      showStatusModal: false,
      showMaintenanceModal: false,
      showDeleteModal: false,
      showAmenitiesModal: false,
      managementTabs: [
        { id: 'details', name: 'Room Details' },
        { id: 'amenities', name: 'Amenities' },
        { id: 'maintenance', name: 'Maintenance' },
        { id: 'reservations', name: 'Reservations' }
      ],
      maintenanceHistory: [
        {
          id: 1,
          type: 'Routine Cleaning',
          description: 'Standard room cleaning and sanitization',
          status: 'completed',
          reported_date: new Date().toISOString(),
          reported_by: 'Housekeeping Staff'
        }
      ],
      currentReservations: []
    }
  },
  computed: {
    roomImages() {
      if (!this.room) return []
      const images = []
      if (this.room.thumbnail) images.push(this.room.thumbnail)
      if (this.room.images && this.room.images.length > 0) {
        images.push(...this.room.images)
      }
      return images.length > 0 ? images : []
    },
    averageRating() {
      if (!this.room?.reviews?.length) return 0
      const sum = this.room.reviews.reduce((acc, review) => acc + review.rating, 0)
      return (sum / this.room.reviews.length).toFixed(1)
    },
    lastCleaned() {
      return 'Today, 10:30 AM'
    },
    nextReservation() {
      return this.currentReservations[0] ? this.formatDate(this.currentReservations[0].check_in) : null
    },
    maintenanceDue() {
      return null
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
          // Simulate loading reservations and maintenance data
          this.loadAdditionalData()
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

    loadAdditionalData() {
      // Simulate API calls for additional data
      this.currentReservations = [
        {
          id: 'RES001',
          guest_name: 'John Smith',
          check_in: new Date(Date.now() + 86400000).toISOString(),
          check_out: new Date(Date.now() + 172800000).toISOString(),
          guests: 2,
          total_price: 299.97,
          status: 'confirmed'
        }
      ]
    },

    calculateTodayRevenue() {
      return (this.room?.price * 0.3).toFixed(2)
    },

    calculateOccupancyRate() {
      return Math.floor(Math.random() * 30) + 70 // Simulate 70-100% occupancy
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

    statusTextClasses(status) {
      const formattedStatus = this.formatStatus(status)
      const classes = {
        'Available': 'text-green-600',
        'Occupied': 'text-red-600',
        'Reserved': 'text-blue-600',
        'Maintenance': 'text-yellow-600',
        'Cleaning': 'text-purple-600'
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

    maintenanceStatusClasses(status) {
      const classes = {
        'completed': 'inline-flex px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800',
        'in-progress': 'inline-flex px-2 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800',
        'pending': 'inline-flex px-2 py-1 rounded-full text-xs font-medium bg-red-100 text-red-800'
      }
      return classes[status] || classes['pending']
    },

    reservationStatusClasses(status) {
      const classes = {
        'confirmed': 'inline-flex px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800',
        'checked-in': 'inline-flex px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800',
        'checked-out': 'inline-flex px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-800',
        'cancelled': 'inline-flex px-2 py-1 rounded-full text-xs font-medium bg-red-100 text-red-800'
      }
      return classes[status] || classes['confirmed']
    },

    formatDate(dateString) {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    },

    // Action Handlers
    handleEditRoom() {
      this.showEditModal = true
    },

    handleChangeStatus() {
      this.showStatusModal = true
    },

    handleQuickClean() {
      if (confirm('Mark room as cleaned and available?')) {
        // API call to update status
        this.room.status = 'available'
        console.log('Room marked as cleaned')
      }
    },

    handleGenerateReport() {
      console.log('Generating room report...')
      // Implementation for report generation
    },

    handleDeleteRoom() {
      this.showDeleteModal = true
    },

    handleTempClose() {
      if (confirm('Temporarily close this room? It will be unavailable for reservations.')) {
        this.room.status = 'maintenance'
        console.log('Room temporarily closed')
      }
    },

    // Modal Handlers
    handleUpdateRoom(updatedRoom) {
      this.room = { ...this.room, ...updatedRoom }
      console.log('Room updated:', updatedRoom)
    },

    handleStatusChange(newStatus) {
      this.room.status = newStatus
      console.log('Room status changed to:', newStatus)
    },

    handleMaintenanceLogged(maintenanceData) {
      this.maintenanceHistory.unshift({
        id: Date.now(),
        ...maintenanceData,
        reported_date: new Date().toISOString(),
        reported_by: 'Current User' // Replace with actual user
      })
      console.log('Maintenance logged:', maintenanceData)
    },

    async handleConfirmDelete(room) {
      try {
        // API call to delete room
        console.log('Deleting room:', room.id)
        this.$router.push('/staff/rooms')
      } catch (error) {
        console.error('Error deleting room:', error)
      }
    }
  }
}
</script>

<style scoped>
.material-symbols-outlined.fill {
  font-variation-settings: 'FILL' 1;
}
</style>