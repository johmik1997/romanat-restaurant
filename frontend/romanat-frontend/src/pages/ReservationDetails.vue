<template>
  <div class="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center h-64">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-[#0f766e]"></div>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="flex justify-center items-center h-64">
        <div class="text-center">
          <div class="text-red-500 text-lg mb-2">Failed to load reservation</div>
          <button @click="loadReservationData" class="btn-[#0f766e]">
            Try Again
          </button>
        </div>
      </div>

      <!-- Content when data is loaded -->
      <div v-else>
        <!-- Page Header -->
        <div class="mb-8">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between sm:space-x-4">
            <div class="mb-4 sm:mb-0">
              <div class="flex items-center space-x-2 mb-2">
                <button 
                  @click="$router.back()" 
                  class="p-2 hover:bg-gray-100 rounded-full transition-colors"
                >
                  <span class="material-icons-outlined text-gray-600">arrow_back</span>
                </button>
                <h1 class="text-2xl sm:text-3xl font-bold text-gray-900">
                  Reservation #{{`RES-${reservationData.id}` }}
                </h1>
              </div>
              <div class="flex items-center space-x-4">
                <span
                  class="inline-flex items-center rounded-full px-3 py-1 text-xs font-medium"
                  :class="statusBadge"
                >
                  {{ formatStatus(reservationData.status) }}
                </span>
                <span class="text-sm text-gray-500">
                  Created: {{ formatDate(reservationData.created_at) }}
                </span>
              </div>
            </div>
            
            <!-- Action Buttons -->
            <div class="flex space-x-2">
              <button class="btn-secondary" @click="printReservation">
                <span class="material-icons-outlined text-sm mr-1">print</span>
                Print
              </button>
              <button class="btn-secondary" @click="sendEmail">
                <span class="material-icons-outlined text-sm mr-1">email</span>
                Email
              </button>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 lg:gap-6">
          <!-- Left Column -->
          <div class="lg:col-span-2 space-y-6">
            <!-- Guest Information -->
            <div class="bg-white rounded-lg shadow-sm border border-gray-200">
              <div class="px-6 py-4 border-b border-gray-200">
                <h2 class="text-lg font-semibold text-gray-900">
                  Guest Information
                </h2>
              </div>
              <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- [#0f766e] Guest Details -->
                <div class="md:col-span-2">
                  <h3 class="text-md font-semibold text-gray-700 mb-3">Primary Guest</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <InfoItem 
                      label="Full Name" 
                      :value="getCustomerFullName(reservationData.customer)" 
                    />
                    <InfoItem label="Email Address" :value="reservationData.customer?.email" />
                    <InfoItem label="Phone Number" :value="reservationData.customer?.phone" />
                    <InfoItem 
                      label="Date of Birth" 
                      :value="formatDate(reservationData.customer?.date_of_birth)" 
                    />
                    <InfoItem label="Customer Status" :value="reservationData.customer?.status" />
                    <InfoItem label="Registration" :value="reservationData.customer?.registered_by" />
                  </div>
                </div>

                <!-- Guest Preferences -->
                <div class="md:col-span-2 pt-4 border-t border-gray-200">
                  <h3 class="text-md font-semibold text-gray-700 mb-3">Reservation Details</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <InfoItem label="Number of Guests" :value="reservationData.number_of_guests" />
                    <InfoItem label="Total Price" :value="formatCurrency(reservationData.total_price)" />
                  </div>
                </div>
              </div>
            </div>

            <!-- Room & Stay Details -->
            <div class="bg-white rounded-lg shadow-sm border border-gray-200">
              <div class="px-6 py-4 border-b border-gray-200">
                <h2 class="text-lg font-semibold text-gray-900">
                  Room & Stay Details
                </h2>
              </div>
              <div class="p-6">
                <!-- Room Information -->
                <div class="mb-6">
                  <h3 class="text-md font-semibold text-gray-700 mb-3">Room Information</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <InfoItem label="Room Type" :value="reservationData.room?.room_type?.name" />
                    <InfoItem label="Room Number" :value="reservationData.room?.room_number" />
                    <InfoItem label="Floor" :value="reservationData.room?.floor" />
                    <InfoItem label="Category" :value="reservationData.room?.category" />
                    <InfoItem label="View" :value="reservationData.room?.view" />
                    <InfoItem label="Room Size" :value="reservationData.room?.size" />
                    <InfoItem label="Capacity" :value="reservationData.room?.capacity" />
                    <InfoItem label="Room Status" :value="reservationData.room?.status" />
                    <InfoItem label="Room Price" :value="formatCurrency(reservationData.room?.price)" />
                  </div>
                </div>

                <!-- Stay Duration -->
                <div class="mb-6 pt-4 border-t border-gray-200">
                  <h3 class="text-md font-semibold text-gray-700 mb-3">Stay Duration</h3>
                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <InfoItem label="Check-In Date" :value="formatDate(reservationData.check_in)" />
                    <InfoItem label="Check-Out Date" :value="formatDate(reservationData.check_out)" />
                    <InfoItem 
                      label="Total Nights" 
                      :value="calculateNights(reservationData.check_in, reservationData.check_out)" 
                    />
                  </div>
                </div>

                <!-- Room Description -->
                <div class="pt-4 border-t border-gray-200" v-if="reservationData.room?.description">
                  <h3 class="text-md font-semibold text-gray-700 mb-3">Room Description</h3>
                  <p class="text-sm text-gray-600">{{ reservationData.room.description }}</p>
                </div>
              </div>
            </div>

            <!-- Payment Summary -->
            <div class="bg-white rounded-lg shadow-sm border border-gray-200">
              <div class="px-6 py-4 border-b border-gray-200">
                <h2 class="text-lg font-semibold text-gray-900">
                  Payment Summary
                </h2>
              </div>
              <div class="p-6">
                <!-- Charges Breakdown -->
                <div class="mb-4">
                  <h4 class="text-sm font-medium text-gray-700 mb-3">Charges Breakdown</h4>
                  <div class="space-y-2">
                    <div class="flex justify-between text-sm">
                      <span class="text-gray-600">Room charges</span>
                      <span class="text-gray-900 font-medium">{{ formatCurrency(reservationData.room?.price) }}</span>
                    </div>
                    <div class="flex justify-between text-sm">
                      <span class="text-gray-600">Taxes & Fees</span>
                      <span class="text-gray-900 font-medium">{{ calculateTaxes(reservationData.total_price) }}</span>
                    </div>
                  </div>
                </div>

                <!-- Totals -->
                <div class="border-t border-gray-200 pt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
                  <InfoItem label="Subtotal" :value="formatCurrency(reservationData.room?.price)" />
                  <InfoItem label="Taxes & Fees" :value="calculateTaxes(reservationData.total_price)" />
                  <InfoItem label="Total Cost" :value="formatCurrency(reservationData.total_price)" />
                  
                  <div class="md:col-span-2 pt-4 border-t border-gray-200">
                    <span
                      class="inline-flex items-center rounded-full px-3 py-1 text-xs font-medium"
                      :class="paymentStatusBadge"
                    >
                      {{ getPaymentStatus(reservationData.status) }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column -->
          <div class="space-y-6">
    <!-- Quick Actions -->
<div class="bg-white rounded-xl shadow-md border border-gray-200 overflow-hidden">
  <div class="px-6 py-4 border-b border-gray-200">
    <h3 class="text-lg font-semibold text-black">
      Quick Actions
    </h3>
  </div>
  <div class="p-6 flex flex-col gap-3">
    <!-- Status-Based Actions -->
    <button 
      v-if="showCheckInButton" 
      @click="updateReservationStatusHandler('checked_in')"
      :disabled="updatingStatus"
      class="bg-[#0f766e] text-white w-full flex items-center justify-center gap-2 py-3 rounded-lg hover:bg-teal-400 transition-colors"
    >
      <span v-if="updatingStatus" class="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></span>
      <span v-else class="material-icons-outlined text-sm">login</span>
      Check-In Guest
    </button>

    <button 
      v-if="showCheckOutButton" 
      @click="updateReservationStatusHandler('checked_out')"
      :disabled="updatingStatus"
      class="bg-[#0f766e] text-white w-full flex items-center justify-center gap-2 py-3 rounded-lg hover:bg-teal-600 transition-colors"
    >
      <span v-if="updatingStatus" class="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></span>
      <span v-else class="material-icons-outlined text-sm">logout</span>
      Check-Out Guest
    </button>

    <button 
      v-if="showConfirmButton" 
      @click="updateReservationStatusHandler('confirmed')"
      :disabled="updatingStatus"
      class="bg-[#29982e] w-full text-white flex items-center justify-center gap-2 py-3 rounded-lg hover:bg-teal-600 transition-colors"
    >
      <span v-if="updatingStatus" class="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></span>
      <span v-else class="material-icons-outlined text-sm">check_circle</span>
      Confirm Reservation
    </button>

    <button 
      v-if="showCancelButton" 
      @click="cancelReservation"
      :disabled="updatingStatus"
      class="bg-red-700 w-full flex items-center justify-center gap-2 py-3 rounded-lg hover:bg-red-600 transition-colors"
    >
      <span v-if="updatingStatus" class="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></span>
      <span v-else class="material-icons-outlined text-sm">cancel</span>
      Cancel Reservation
    </button>
  </div>
</div>


            <!-- Room Images -->
            <div v-if="reservationData.room" class="bg-white rounded-lg shadow-sm border border-gray-200">
              <div class="px-6 py-4 border-b border-gray-200">
                <h3 class="text-lg font-semibold text-gray-900">
                  Room Images
                </h3>
              </div>
              <div class="p-6">
                <div class="grid grid-cols-2 gap-4">
                  <!-- Thumbnail -->
                  <div v-if="reservationData.room.thumbnail" class="col-span-2">
                    <img 
                      :src="reservationData.room.thumbnail" 
                      :alt="reservationData.room.title"
                      class="w-full h-48 object-cover rounded-lg"
                    />
                    <p class="text-xs text-gray-500 mt-2 text-center">Main Image</p>
                  </div>
                  
                  <!-- Additional Images -->
                  <div 
                    v-for="(image, index) in reservationData.room.images" 
                    :key="index"
                    class="h-24"
                  >
                    <img 
                      :src="image" 
                      :alt="`Room image ${index + 1}`"
                      class="w-full h-full object-cover rounded-lg"
                    />
                  </div>
                </div>
              </div>
            </div>

            <!-- System Information -->
            <div class="bg-white rounded-lg shadow-sm border border-gray-200">
              <div class="px-6 py-4 border-b border-gray-200">
                <h3 class="text-lg font-semibold text-gray-900">
                  System Information
                </h3>
              </div>
              <div class="p-6">
                <div class="space-y-3">
                  <InfoItem label="Reservation ID" :value="reservationData.id" />
                  <InfoItem label="Created" :value="formatDateTime(reservationData.created_at)" />
                  <InfoItem label="Last Updated" :value="formatDateTime(reservationData.updated_at)" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getReservationById, updateReservationStatus } from '../api/auth/reservation'
import InfoItem from '../components/modal/InfoItem.vue'



const route = useRoute()
const router = useRouter()
const reservationId = route.params.id
const reservationData = ref({
  customer: {},
  number_of_guests: 0,
  total_price: 0,
  // other default fields
})
const loading = ref(true)
const error = ref(null)
const updatingStatus = ref(false)

// Load reservation data
const loadReservationData = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await getReservationById(reservationId)
    reservationData.value = response
  } catch (err) {
    console.error('Failed to load reservation:', err)
    error.value = 'Failed to load reservation details'
  } finally {
    loading.value = false
  }
}

const updateReservationStatusHandler = async (newStatus) => {
  try {
    updatingStatus.value = true;
    await updateReservationStatus(reservationId, newStatus);

    await loadReservationData(); // refresh UI
    console.log("Status updated:", newStatus);
  } catch (err) {
    console.error("Failed to update status:", err);
    error.value = "Unable to update reservation status";
  } finally {
    updatingStatus.value = false;
  }
};


// Cancel reservation handler
const cancelReservation = async () => {
  if (!confirm('Are you sure you want to cancel this reservation? This action cannot be undone.')) {
    return
  }
  
  try {
    updatingStatus.value = true
    await updateReservationStatus(reservationId, 'cancelled')
    await loadReservationData()
    console.log('Reservation cancelled successfully')
  } catch (err) {
    console.error('Failed to cancel reservation:', err)
    error.value = 'Failed to cancel reservation'
  } finally {
    updatingStatus.value = false
  }
}

// Utility functions
const formatStatus = (status) => {
  if (!status) return 'Unknown'
  return status.split('_').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')
}

const formatDate = (dateString) => {
  if (!dateString) return '—'
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const formatDateTime = (dateString) => {
  if (!dateString) return '—'
  return new Date(dateString).toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const formatCurrency = (amount) => {
  if (!amount) return '$0.00'
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(parseFloat(amount))
}

const calculateNights = (checkIn, checkOut) => {
  if (!checkIn || !checkOut) return '—'
  const start = new Date(checkIn)
  const end = new Date(checkOut)
  const nights = Math.ceil((end - start) / (1000 * 60 * 60 * 24))
  return `${nights} night${nights !== 1 ? 's' : ''}`
}

const calculateTaxes = (totalPrice) => {
  if (!totalPrice) return '$0.00'
  const price = parseFloat(totalPrice)
  const taxes = price * 0.15 // Assuming 15% tax rate
  return formatCurrency(taxes)
}

const getCustomerFullName = (customer) => {
  if (!customer) return '—'
  return `${customer.first_name || ''} ${customer.last_name || ''}`.trim() || customer.username
}

const getPaymentStatus = (reservationStatus) => {
  const statusMap = {
    'pending': 'Pending Payment',
    'confirmed': 'Deposit Paid',
    'checked_in': 'Paid in Full',
    'checked_out': 'Paid in Full',
    'cancelled': 'Refunded'
  }
  return statusMap[reservationStatus] || 'Pending'
}

// Action button visibility
const showCheckInButton = computed(() => {
  return reservationData.value.status === 'confirmed' || reservationData.value.status === 'pending'
})

const showCheckOutButton = computed(() => {
  return reservationData.value.status === 'checked_in'
})

const showConfirmButton = computed(() => {
  return reservationData.value.status === 'pending'
})

const showCancelButton = computed(() => {
  return reservationData.value.status !== 'cancelled' && reservationData.value.status !== 'checked_out'
})

// Status badge classes
const statusBadge = computed(() => {
  const status = reservationData.value.status
  const statusClasses = {
    'checked_in': 'bg-green-100 text-green-800',
    'confirmed': 'bg-blue-100 text-blue-800',
    'checked_out': 'bg-gray-100 text-gray-800',
    'cancelled': 'bg-red-100 text-red-800',
    'pending': 'bg-yellow-100 text-yellow-800'
  }
  return statusClasses[status] || 'bg-gray-100 text-gray-800'
})

const paymentStatusBadge = computed(() => {
  const status = reservationData.value.status
  const statusClasses = {
    'checked_in': 'bg-green-100 text-green-800',
    'confirmed': 'bg-blue-100 text-blue-800',
    'checked_out': 'bg-green-100 text-green-800',
    'cancelled': 'bg-red-100 text-red-800',
    'pending': 'bg-yellow-100 text-yellow-800'
  }
  return statusClasses[status] || 'bg-gray-100 text-gray-800'
})

// Additional functions
const printReservation = () => {
  window.print()
}

const sendEmail = () => {
  // Implement email functionality
  console.log('Send email functionality')
}

onMounted(() => {
  loadReservationData()
})
</script>
