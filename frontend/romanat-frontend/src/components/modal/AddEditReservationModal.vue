<template>
  <transition name="fade">
    <div
      v-if="show"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50"
    >
      <div
        class="bg-white rounded-xl shadow-lg w-full max-w-4xl p-6 relative max-h-[95vh] h-[85vh] overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-bold text-gray-900">{{ isEditMode ? 'Edit Reservation' : 'Add New Reservation' }}</h2>
          <button @click="close" class="text-gray-500 hover:text-gray-700">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <div class="p-6 overflow-y-auto max-h-[60vh]">
          <form @submit.prevent="saveReservation" class="space-y-6 text-black">
            <!-- Customer Selection -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Customer *</label>
              <select 
                v-model="form.customer_id"
                required
                :disabled="isEditMode"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40 disabled:bg-gray-50 disabled:cursor-not-allowed"
              >
                <option value="">Select a customer</option>
                <option v-for="customer in customers" :key="customer.id" :value="customer.id">
                  {{ customer.first_name }} {{ customer.last_name }} - {{ customer.email }}
                </option>
              </select>
            </div>

            <!-- Room Selection -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Room *</label>
              <select 
                v-model="form.room_id"
                required
                :disabled="isEditMode && reservation?.status !== 'pending'"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 disabled:bg-gray-50 disabled:cursor-not-allowed"
              >
                <option value="">Select a room</option>
                <option 
                  v-for="room in filteredRooms" 
                  :key="room.id" 
                  :value="room.id"
                  :disabled="room.status !== 'available' && room.id !== parseInt(form.room_id)"
                >
                  {{ room.room_number }} - {{ room.room_type?.name || 'N/A' }} (${{ room.price }}/night)
                  <span v-if="room.status !== 'available' && room.id !== parseInt(form.room_id)">
                    - {{ room.status === 'occupied' ? 'Occupied' : 'Unavailable' }}
                  </span>
                </option>
              </select>
              <p v-if="isEditMode && reservation?.status !== 'pending'" class="text-sm text-gray-500 mt-1">
                Room cannot be changed for {{ reservation?.status }} reservations
              </p>
            </div>

            <!-- Dates -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Check-in Date *</label>
                <input 
                  v-model="form.check_in"
                  type="date" 
                  required
                  :min="minDate"
                  :disabled="isEditMode && ['checked_in', 'checked_out'].includes(reservation?.status)"
                  @change="updateCalculations"
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 disabled:bg-gray-50 disabled:cursor-not-allowed"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Check-out Date *</label>
                <input 
                  v-model="form.check_out"
                  type="date" 
                  required
                  :min="form.check_in || minDate"
                  :disabled="isEditMode && ['checked_in', 'checked_out'].includes(reservation?.status)"
                  @change="updateCalculations"
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 disabled:bg-gray-50 disabled:cursor-not-allowed"
                />
              </div>
            </div>

            <!-- Number of Guests -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Number of Guests *</label>
              <input 
                v-model="form.number_of_guests"
                type="number" 
                min="1"
                max="10"
                required
                :disabled="isEditMode && ['checked_in', 'checked_out'].includes(reservation?.status)"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 disabled:bg-gray-50 disabled:cursor-not-allowed"
              />
            </div>

            <!-- Status -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Status *</label>
              <select 
                v-model="form.status"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
              >
                <option value="pending">Pending</option>
                <option value="confirmed">Confirmed</option>
                <option value="checked_in">Checked In</option>
                <option value="checked_out">Checked Out</option>
                <option value="cancelled">Cancelled</option>
              </select>
            </div>

            <!-- Total Price -->
            <div class="bg-gray-50 p-4 rounded-lg">
              <label class="block text-sm font-medium text-gray-700 mb-2">Total Price</label>
              <div class="flex items-center justify-between">
                <span class="text-2xl font-bold text-gray-900">${{ calculatedTotalPrice }}</span>
                <span class="text-sm text-gray-500">{{ totalNights }} night(s)</span>
              </div>
              <div class="mt-2 text-sm text-gray-600">
                <div class="flex justify-between">
                  <span>Room rate:</span>
                  <span>${{ selectedRoom?.price || '0.00' }}/night</span>
                </div>
                <div class="flex justify-between">
                  <span>Taxes & fees (15%):</span>
                  <span>${{ taxesAndFees }}</span>
                </div>
              </div>
            </div>

            <!-- Special Requests -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Special Requests</label>
              <textarea 
                v-model="form.special_requests"
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/500"
                placeholder="Any special requests or notes..."
              ></textarea>
            </div>
          </form>
        </div>

        <!-- Footer -->
        <div class="flex justify-end gap-3 p-6 border-t border-gray-200 bg-gray-50">
          <button 
            @click="close"
            type="button"
            class="px-6 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Cancel
          </button>
          <button 
            @click="saveReservation"
            :disabled="!isFormValid"
            class="px-6 py-2 text-sm font-medium text-white bg-[#0f766e] border border-transparent rounded-lg hover:bg-[#0f766e]/60 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            {{ isEditMode ? 'Update Reservation' : 'Create Reservation' }}
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { fetchCustomers } from '../../api/auth/loginApi'
import { fetchRoom } from '../../api/auth/roomApi'
import { getReservationById } from '../../api/auth/reservation'

export default {
  name: 'AddEditReservationModal',
  props: {
    show: {
      type: Boolean,
      default: false
    },
    reservation: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      form: {
        customer_id: "",
        room_id: "",
        check_in: "",
        check_out: "",
        number_of_guests: 1,
        status: "pending",
        special_requests: "",
        total_price: "0.00"
      },
      customers: [],
      allRooms: [],
      originalReservation: null
    }
  },
  computed: {
    isEditMode() {
      return this.reservation !== null
    },
    
    minDate() {
      return new Date().toISOString().split('T')[0]
    },
    
    totalNights() {
      if (!this.form.check_in || !this.form.check_out) return 0
      const checkIn = new Date(this.form.check_in)
      const checkOut = new Date(this.form.check_out)
      const diffTime = Math.abs(checkOut - checkIn)
      return Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    },
    
    selectedRoom() {
      if (!this.form.room_id) return null
      return this.allRooms.find(room => room.id === parseInt(this.form.room_id))
    },
    
    calculatedTotalPrice() {
      if (!this.selectedRoom || this.totalNights === 0) return '0.00'
      const roomTotal = parseFloat(this.selectedRoom.price) * this.totalNights
      const total = roomTotal + parseFloat(this.taxesAndFees)
      return total.toFixed(2)
    },
    
    taxesAndFees() {
      if (!this.selectedRoom || this.totalNights === 0) return '0.00'
      const roomTotal = parseFloat(this.selectedRoom.price) * this.totalNights
      return (roomTotal * 0.15).toFixed(2) // 15% taxes and fees
    },
    
    isFormValid() {
      return (
        this.form.customer_id &&
        this.form.room_id &&
        this.form.check_in &&
        this.form.check_out &&
        this.form.number_of_guests &&
        this.form.status
      )
    },
    
    filteredRooms() {
      // Filter rooms based on current selection
      return this.allRooms.filter(room => {
        // If editing and this is the current room, include it even if unavailable
        if (this.isEditMode && room.id === parseInt(this.form.room_id)) {
          return true
        }
        // Otherwise, only show available rooms
        return room.status === 'available'
      })
    }
  },
  watch: {
    show(newVal) {
      if (newVal) {
        this.initializeForm()
      } else {
        this.resetForm()
      }
    },
    
    reservation(newReservation) {
      if (newReservation) {
        this.initializeForm()
      }
    },
    
    'form.room_id': function(newRoomId) {
      if (newRoomId) {
        this.updateCalculations()
      }
    },
    
    'form.check_in': function() {
      this.updateCalculations()
    },
    
    'form.check_out': function() {
      this.updateCalculations()
    }
  },
  methods: {
    async initializeForm() {
      await Promise.all([
        this.loadCustomers(),
        this.loadAllRooms()
      ])
      
      if (this.reservation) {
        // Edit mode: Load reservation data
        await this.loadReservationData()
      } else {
        // Add mode: Set default values
        this.setDefaultDates()
      }
    },
    
    async loadReservationData() {
      try {
        let reservationData
        if (typeof this.reservation === 'number' || typeof this.reservation === 'string') {
          // If reservation is an ID, fetch from API
          reservationData = await getReservationById(this.reservation)
        } else {
          // If reservation is an object, use it directly
          reservationData = this.reservation
        }
        
        this.originalReservation = { ...reservationData }
        
        // Populate form with reservation data
        this.form = {
          customer_id: reservationData.customer?.id || reservationData.customer_id,
          room_id: reservationData.room?.id || reservationData.room_id,
          check_in: reservationData.check_in,
          check_out: reservationData.check_out,
          number_of_guests: reservationData.number_of_guests,
          status: reservationData.status,
          special_requests: reservationData.special_requests || "",
          total_price: reservationData.total_price || "0.00"
        }
      } catch (error) {
        console.error('Error loading reservation data:', error)
        alert('Failed to load reservation details')
        this.close()
      }
    },
    
    async loadCustomers() {
      try {
        const response = await fetchCustomers()
        this.customers = response.result || response || []
      } catch (error) {
        console.error('Error loading customers:', error)
        // Fallback sample data
        this.customers = [
          { id: 1, first_name: 'John', last_name: 'Smith', email: 'john@email.com' },
          { id: 2, first_name: 'Sarah', last_name: 'Johnson', email: 'sarah@email.com' }
        ]
      }
    },
    
    async loadAllRooms() {
      try {
        const response = await fetchRoom()
        this.allRooms = response.result || response || []
      } catch (error) {
        console.error('Error loading rooms:', error)
        // Fallback sample data
        this.allRooms = [
          { id: 1, room_number: '101', room_type: { name: 'Standard Queen' }, price: 100, status: 'available' },
          { id: 2, room_number: '201', room_type: { name: 'Deluxe King' }, price: 150, status: 'available' }
        ]
      }
    },
    
    setDefaultDates() {
      // Set default check-in to tomorrow
      const tomorrow = new Date()
      tomorrow.setDate(tomorrow.getDate() + 1)
      this.form.check_in = tomorrow.toISOString().split('T')[0]
      
      // Set default check-out to day after tomorrow
      const dayAfter = new Date(tomorrow)
      dayAfter.setDate(dayAfter.getDate() + 2)
      this.form.check_out = dayAfter.toISOString().split('T')[0]
    },
    
    updateCalculations() {
      // Update total price when dates or room changes
      if (this.form.room_id && this.form.check_in && this.form.check_out) {
        this.form.total_price = this.calculatedTotalPrice
      }
    },
    
    close() {
      this.$emit('close')
    },
    
    async saveReservation() {
      if (!this.isFormValid) {
        alert('Please fill in all required fields.')
        return
      }

      try {
        // Prepare reservation data
        const reservationData = {
          customer_id: parseInt(this.form.customer_id),
          room_id: parseInt(this.form.room_id),
          check_in: this.form.check_in,
          check_out: this.form.check_out,
          number_of_guests: parseInt(this.form.number_of_guests),
          status: this.form.status,
          special_requests: this.form.special_requests,
          total_price: this.calculatedTotalPrice
        }
        
        // If editing, include the ID
        if (this.isEditMode && this.originalReservation) {
          reservationData.id = this.originalReservation.id
        }
        
        console.log('Saving reservation:', reservationData)
        
        // Emit the reservation data
        this.$emit('save', reservationData)
        this.resetForm()
        
      } catch (error) {
        console.error('Error saving reservation:', error)
        alert(`Failed to ${this.isEditMode ? 'update' : 'create'} reservation. Please try again.`)
      }
    },
    
    resetForm() {
      this.form = {
        customer_id: "",
        room_id: "",
        check_in: "",
        check_out: "",
        number_of_guests: 1,
        status: "pending",
        special_requests: "",
        total_price: "0.00"
      }
      this.originalReservation = null
    }
  }
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}
</style>