<template>
  <div class="p-8">
    <!-- Page Header -->
    <PageHeader 
      title="Room Management"
      subtitle="Manage room status, availability, and assignments."
      action-text="Add New Room"
      @add-guest="openModal"
    />

    <!-- Room Statistics -->
    <RoomStats :stats="roomStats" />

    <!-- Search and Filters -->
    <RoomFilters 
      @search="handleSearch"
      @filter-change="handleFilterChange"
      @export-rooms="handleExportRooms"
      @refresh-rooms="handleRefreshRooms"
    />

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto"></div>
      <p class="mt-4 text-gray-600">Loading rooms...</p>
    </div>

    <!-- Table -->
    <div v-else class="mt-6 bg-white rounded-xl border border-gray-200 overflow-hidden shadow-sm">
      <table class="min-w-full bg-white rounded-xl overflow-hidden">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Image</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Room</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Floor</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Size & View</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Capacity</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white">
          <tr v-for="room in rooms" 
              :key="room.id"
              class="hover:bg-gray-50 transition-colors duration-150 cursor-pointer"
              @click="goToRoomDetails(room.id)">
            <!-- Thumbnail -->
            <td class="px-6 py-4">
              <img 
                :src="room.thumbnail || '/api/placeholder/56/56'" 
                class="w-14 h-14 rounded-lg object-cover shadow-sm"
                alt="Room Image"
              />
            </td>

            <!-- Room Number -->
            <td class="px-6 py-4 font-medium text-gray-900">
              {{ room.room_number }}
            </td>

            <!-- Room Type -->
            <td class="px-6 py-4 text-gray-900">
              {{ room.room_type?.name || 'N/A' }}
            </td>

            <!-- Floor -->
            <td class="px-6 py-4 text-gray-900">
              {{ room.floor }}
            </td>

            <!-- Price -->
            <td class="px-6 py-4 text-gray-900">
              ${{ room.price }}
            </td>

            <!-- Category -->
            <td class="px-6 py-4 text-gray-900">
              <span :class="categoryBadgeClasses(room.category)">
                {{ room.category || 'Standard' }}
              </span>
            </td>

            <!-- Size -->
            <td class="px-6 py-4 text-gray-900">
              {{ room.size }} m² • {{ room.view || 'N/A' }}
            </td>
            <td class="px-6 py-4 text-gray-900">
              {{ room.capacity }} Guests
            </td>
            <td class="px-6 py-4">
              <span :class="statusBadgeClasses(room.status)">
                {{ formatStatus(room.status) }}
              </span>
            </td>
            <td class="px-6 py-4 text-sm font-medium">
             <div class="flex items-center gap-2">
        <button @click.stop="editRoom(room)" class="p-1.5 text-gray-500 rounded hover:bg-gray-100">
          <span class="material-symbols-outlined text-green-500 text-xl">edit</span>
        </button>
        <button @click.stop="deleteRoom(room)" class="p-1.5 text-gray-500 rounded hover:bg-gray-100">
          <span class="material-symbols-outlined text-red-500 text-xl">delete</span>
        </button>
      </div>
            </td>
          </tr>
        </tbody>
      </table>
      
      <!-- Pagination -->
      <div v-if="totalCount > 0" class="px-6 py-4 border border-gray-200 rounded-2xl bg-white shadow-sm">
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
          <div class="text-sm text-gray-700">
            Showing 
            <span class="font-medium">{{ paginationStart }}</span> 
            to 
            <span class="font-medium">{{ paginationEnd }}</span> 
            of 
            <span class="font-medium">{{ totalCount }}</span> rooms
          </div>
          
          <div class="flex items-center gap-2">
            <button 
              @click="previousPage"
              :disabled="currentPage === 1"
              :class="[
                'px-4 py-2 border border-gray-300 rounded-lg font-medium transition-colors',
                currentPage === 1 
                  ? 'bg-gray-50 text-gray-400 cursor-not-allowed' 
                  : 'bg-white text-gray-700 hover:bg-gray-50 hover:border-gray-400'
              ]"
            >
              Previous
            </button>
            
            <div class="flex items-center gap-1">
              <button 
                v-for="page in visiblePages" 
                :key="page"
                @click="goToPage(page)"
                :class="[
                  'w-10 h-10 flex items-center justify-center rounded-lg font-medium transition-colors',
                  currentPage === page 
                    ? 'bg-[#0f766e] text-white' 
                    : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
                ]"
              >
                {{ page }}
              </button>
              <span v-if="showEllipsis" class="px-2 text-gray-500">...</span>
            </div>
            
            <button 
              @click="nextPage"
              :disabled="currentPage >= totalPages"
              :class="[
                'px-4 py-2 border border-gray-300 rounded-lg font-medium transition-colors',
                currentPage >= totalPages 
                  ? 'bg-gray-50 text-gray-400 cursor-not-allowed' 
                  : 'bg-white text-gray-700 hover:bg-gray-50 hover:border-gray-400'
              ]"
            >
              Next
            </button>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="rooms.length === 0 && !loading" class="text-center py-12">
        <span class="material-symbols-outlined text-6xl text-gray-300 mb-4">meeting_room</span>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No rooms found</h3>
        <p class="text-gray-500 mb-4">Try adjusting your search or filters</p>
        <button @click="resetFilters" class="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/90 transition-colors">
          Reset Filters
        </button>
      </div>
    </div>
    
   <AddEditRoomModal
      :isOpen="showRoomModal"
      :roomData="selectedRoom"
      @close="closeRoomModal"
      @save="handleSaveRoom"
    />
    
  </div>
</template>
<script>
import PageHeader from '../components/staffs/PageHeader.vue'
import RoomStats from '../components/staffs/RoomStats.vue'
import RoomFilters from '../components/staffs/RoomFilters.vue'
import AddEditRoomModal from '../components/modal/AddNewRoom.vue'
import { fetchRoom, deleteRoom } from '../api/auth/roomApi' // Added deleteRoom import

export default {
  name: 'RoomManagementTable',
  components: { 
    PageHeader, 
    RoomStats, 
    RoomFilters, 
    AddEditRoomModal 
  },
  data() {
    return {
      showAddRoomModal: false,
      searchQuery: '',
      loading: false,
      showRoomModal: false,
      selectedRoom: null,
      filters: {
        status: 'all',
        type: 'all',
        floor: 'all',
        minPrice: '',
        maxPrice: ''
      },
      roomStats: {
        totalRooms: 0,
        availableRooms: 0,
        occupiedRooms: 0,
        occupancyRate: 0
      },
      rooms: [],
      totalCount: 0,
      currentPage: 1,
      itemsPerPage: 10,
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.totalCount / this.itemsPerPage)
    },
    paginationStart() {
      return this.totalCount === 0 ? 0 : (this.currentPage - 1) * this.itemsPerPage + 1
    },
    paginationEnd() {
      return Math.min(this.currentPage * this.itemsPerPage, this.totalCount)
    },
    visiblePages() {
      const pages = []
      const maxVisible = 5
      let start = Math.max(1, this.currentPage - Math.floor(maxVisible / 2))
      let end = Math.min(this.totalPages, start + maxVisible - 1)
      
      // Adjust start if we're near the end
      if (end - start + 1 < maxVisible) {
        start = Math.max(1, end - maxVisible + 1)
      }
      
      for (let i = start; i <= end; i++) {
        pages.push(i)
      }
      return pages
    },
    showEllipsis() {
      return this.totalPages > this.visiblePages.length && 
             this.visiblePages[this.visiblePages.length - 1] < this.totalPages
    }
  },
  async mounted() {
    await this.loadRooms()
  },
  methods: {
    async loadRooms() {
      this.loading = true
      try {
        // Build query params for backend
        const params = {
          page: this.currentPage,
          page_size: this.itemsPerPage,
          search: this.searchQuery.trim()
        }

        // Add filters if they're not 'all' or empty
        if (this.filters.status !== 'all') {
          params.status = this.filters.status
        }
        if (this.filters.type !== 'all') {
          params.type = this.filters.type
        }
        if (this.filters.floor !== 'all') {
          params.floor = this.filters.floor
        }
        if (this.filters.minPrice) {
          params.minPrice = this.filters.minPrice
        }
        if (this.filters.maxPrice) {
          params.maxPrice = this.filters.maxPrice
        }

        // Call API with params
        const response = await fetchRoom(params)
        
        // Update data based on API response format
        if (response && Array.isArray(response.results)) {
          // Django REST Framework pagination format
          this.rooms = response.results
          this.totalCount = response.count || 0
        } else if (response && Array.isArray(response.result)) {
          // Your custom format
          this.rooms = response.result
          this.totalCount = response.count || response.total || response.result.length
        } else if (Array.isArray(response)) {
          // Simple array response
          this.rooms = response
          this.totalCount = response.length
        } else {
          console.error('Unexpected API response format:', response)
          this.rooms = []
          this.totalCount = 0
        }
        
        this.updateRoomStats()
      } catch (error) {
        console.error('Error loading rooms:', error)
        this.rooms = []
        this.totalCount = 0
      } finally {
        this.loading = false
      }
    },

    openModal() {
      this.selectedRoom = null
      this.showRoomModal = true
    },
    
    // Open modal for editing
    editRoom(room) {
      console.log('Edit room:', room)
      this.selectedRoom = room.id || room // Pass room ID or object
      this.showRoomModal = true
    },
    
    async deleteRoom(room) {
      if (confirm(`Are you sure you want to delete room ${room.room_number}? This action cannot be undone.`)) {
        try {
          const roomId = room.id || room
          await deleteRoom(roomId) // Use the imported deleteRoom function
          await this.loadRooms()
          alert('Room deleted successfully!')
        } catch (error) {
          console.error('Error deleting room:', error)
          alert('Failed to delete room. Please try again.')
        }
      }
    },
    
    closeRoomModal() {
      this.showRoomModal = false
      this.selectedRoom = null
    },

    // Handle save from modal
    async handleSaveRoom() {
      await this.loadRooms() // Refresh the room list
      this.closeRoomModal()
    },

    updateRoomStats() {
      const totalRooms = this.totalCount
      const availableRooms = this.rooms.filter(r => r.status === "available").length
      const occupiedRooms = this.rooms.filter(r => r.status === "occupied").length
      const occupancyRate = totalRooms > 0 ? Math.round((occupiedRooms / totalRooms) * 100) : 0

      this.roomStats = {
        totalRooms,
        availableRooms,
        occupiedRooms,
        occupancyRate
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

    handleSearch(query) { 
      this.searchQuery = query
      this.currentPage = 1 // Reset to first page on new search
      this.loadRooms()
    },
    
    handleFilterChange(filters) { 
      this.filters = { ...filters }
      this.currentPage = 1 // Reset to first page on filter change
      this.loadRooms()
    },
    
    handleExportRooms() { 
      console.log('Export rooms') 
    },
    
    async handleRefreshRooms() { 
      await this.loadRooms()
    },
    
    goToRoomDetails(id) {
      this.$router.push(`/staff/rooms/${id}`)
    },
    
    resetFilters() {
      this.searchQuery = ''
      this.filters = { 
        status: 'all', 
        type: 'all', 
        floor: 'all', 
        minPrice: '', 
        maxPrice: '' 
      }
      this.currentPage = 1
      this.loadRooms()
    },
    
    statusBadgeClasses(status) {
      const formattedStatus = this.formatStatus(status)
      const classes = {
        'Available': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800',
        'Occupied': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800',
        'Reserved': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800',
        'Maintenance': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800',
        'Cleaning': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800'
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
    
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--
        this.loadRooms()
      }
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
        this.loadRooms()
      }
    },

    goToPage(page) {
      if (page !== this.currentPage) {
        this.currentPage = page
        this.loadRooms()
      }
    }
  }
}
</script>