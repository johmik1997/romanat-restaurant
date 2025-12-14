<template>
  <LandingLayout>
    <div class="container mt-24 mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
      <!-- Page Header -->
      <div class="flex flex-wrap justify-between gap-6 mb-8">
        <div class="flex flex-col gap-3">
          <h1 class="text-4xl font-serif font-bold text-gray-800">Confirm and Pay</h1>
          <p class="text-xl text-gray-600">Please review your booking details and complete your payment below.</p>
        </div>
      </div>

      <!-- Main Content Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-5 gap-8 lg:gap-12">
        <div class="lg:col-span-3 flex flex-col gap-6">
          <!-- Room Details Card -->
          <div class="bg-white rounded-2xl shadow-lg p-6 border border-gray-100">
            <div class="flex overflow-x-auto scrollbar-hide -mx-6 px-6 mb-6">
              <div class="flex items-stretch gap-4 pb-4">
                <div v-for="(image, index) in booking.room?.images" :key="index" class="flex-1 min-w-80">
                  <div class="w-full h-48 bg-cover bg-center rounded-xl shadow-md" :style="{ backgroundImage: `url('${image}')` }"></div>
                </div>
              </div>
            </div>

            <div class="flex flex-col gap-3 mb-6">
              <h2 class="text-2xl font-serif font-bold text-gray-800">{{ booking.room?.title || 'Room Details' }}</h2>
              <p class="text-gray-600">{{ booking.room?.description }}</p>
              <div class="flex items-center gap-4 text-sm text-gray-500">
                <span>{{ booking.room?.category }}</span>
                <span>•</span>
                <span>{{ booking.room?.size }}</span>
                <span>•</span>
                <span>{{ booking.room?.capacity }}</span>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-6 border-t border-gray-200 pt-6">
              <div class="space-y-4">
                <div>
                  <p class="text-sm text-gray-500 mb-1">Check-in</p>
                  <p class="text-lg font-semibold text-gray-800">{{ formatDate(booking.check_in) }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-500 mb-1">Guests</p>
                  <p class="text-lg font-semibold text-gray-800">{{ booking.number_of_guests }}</p>
                </div>
              </div>
              <div class="space-y-4">
                <div>
                  <p class="text-sm text-gray-500 mb-1">Check-out</p>
                  <p class="text-lg font-semibold text-gray-800">{{ formatDate(booking.check_out) }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-500 mb-1">Nights</p>
                  <p class="text-lg font-semibold text-gray-800">{{ calculateNights(booking.check_in, booking.check_out) }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Cost Breakdown -->
          <div class="bg-white rounded-2xl shadow-lg p-6 border border-gray-100">
            <h3 class="text-xl font-serif font-bold text-gray-800 mb-6">Cost Breakdown</h3>
            <div class="space-y-4">
              <div class="flex justify-between items-center">
                <p class="text-gray-600">{{ calculateNights(booking.check_in, booking.check_out) }} nights x ${{ booking.room?.price }}/night</p>
                <p class="font-semibold text-gray-800">${{ calculateSubtotal() }}</p>
              </div>
              <div class="flex justify-between items-center">
                <p class="text-gray-600">Taxes & Fees</p>
                <p class="font-semibold text-gray-800">${{ calculateTaxes() }}</p>
              </div>
              <div class="border-t border-gray-200 pt-4">
                <div class="flex justify-between items-center">
                  <p class="text-lg font-bold text-gray-800">Total</p>
                  <p class="text-2xl font-bold text-[#0f766e]">${{ booking.total_price }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Payment -->
        <div class="lg:col-span-2 flex flex-col gap-6">
          <div class="bg-white rounded-2xl shadow-lg p-6 border border-gray-100 text-center">
            <h3 class="text-xl font-serif font-bold text-gray-800 mb-6">Complete Your Payment</h3>
            
            <button 
              @click="processChapaPayment"
              class="w-full bg-[#0f766e] text-white py-4 rounded-xl font-bold hover:bg-teal-700 transition-all duration-300 shadow-lg hover:shadow-xl hover:scale-105 flex items-center justify-center gap-3"
            >
              <span>Pay ${{ booking.total_price }}</span>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
            </button>

            <p v-if="paymentSuccess" class="mt-6 text-green-600 font-semibold">Payment Successful! Booking Confirmed.</p>
          </div>
        </div>
      </div>
    </div>
  </LandingLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import LandingLayout from '../layouts/LandingLayout.vue'

const route = useRoute()
const booking = ref({})
const paymentSuccess = ref(false)

// Format date
const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
}

// Calculate nights
const calculateNights = (checkIn, checkOut) => {
  if (!checkIn || !checkOut) return 0
  const start = new Date(checkIn)
  const end = new Date(checkOut)
  const diff = Math.ceil((end - start) / (1000 * 60 * 60 * 24))
  return diff > 0 ? diff : 0
}

// Subtotal & taxes
const calculateSubtotal = () => {
  if (!booking.value.room?.price) return '0.00'
  return (calculateNights(booking.value.check_in, booking.value.check_out) * parseFloat(booking.value.room.price)).toFixed(2)
}
const calculateTaxes = () => (parseFloat(calculateSubtotal()) * 0.1).toFixed(2)

// Chapa payment
const processChapaPayment = async () => {
  try {
    const user = JSON.parse(localStorage.getItem('logged_in_user') || '{}')
    const response = await fetch('https://romanat-restaurant-7.onrender.com/api/payments/payments/initialize/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${user.access_token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ reservation_id: booking.value.id })
    })

    const data = await response.json()
    if (response.ok && data.checkout_url) {
      // Redirect to Chapa checkout
      window.location.href = data.checkout_url
    } else {
      alert('Failed to initialize payment. Please try again.')
      console.error(data)
    }
  } catch (error) {
    console.error('Chapa payment error:', error)
    alert('Payment error. Check your network and try again.')
  }
}

onMounted(() => {
  if (history.state?.booking) booking.value = history.state.booking
})
</script>

<style scoped>
.scrollbar-hide::-webkit-scrollbar { display: none; }
.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
</style>
