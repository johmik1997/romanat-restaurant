<template>
  <div class="sticky top-28 bg-white p-8 rounded-2xl shadow-2xl border border-gray-100">
    <!-- Price & Rating -->
    <div class="flex items-baseline justify-between mb-6">
      <div>
        <span class="text-4xl font-bold text-primary">${{ room.price }}</span>
        <span class="text-gray-600 text-xl">/ night</span>
      </div>
      <div class="flex items-center gap-1 text-accent">
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
        </svg>
        <span class="font-bold text-lg">{{ averageRating || 0 }}</span>
        <span class="text-gray-500 text-sm">({{ reviewCount || 0 }} reviews)</span>
      </div>
    </div>

    <!-- Booking Form -->
    <div class="space-y-4">
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Check-in</label>
          <input 
            type="date" 
            v-model="booking.checkIn"
            class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
          />
        </div>
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Check-out</label>
          <input 
            type="date" 
            v-model="booking.checkOut"
            class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-700 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
          />
        </div>
      </div>

      <!-- Guests Selection -->
      <div class="space-y-4">
        <div class="bg-gray-50 rounded-xl p-4 border border-gray-200">
          <div class="flex items-center justify-between mb-3">
            <label class="block text-sm font-semibold text-gray-800 flex items-center gap-2">
              <span class="material-symbols-outlined text-gray-600 text-lg">group</span>
              Guests
            </label>
            <span class="text-xs text-gray-500 bg-white px-2 py-1 rounded-full border">
              Max: {{ room.capacity }} guests
            </span>
          </div>
          <select 
            v-model="booking.guests"
            :class="[
              'w-full bg-white rounded-lg border px-4 py-3.5 text-gray-900 focus:outline-none focus:ring-2 transition-all duration-300 appearance-none cursor-pointer',
              guestsExceedCapacity ? 'border-red-300 focus:border-red-500 focus:ring-red-500/50' : 'border-gray-300 focus:border-primary focus:ring-primary/50'
            ]"
          >
            <option 
              v-for="option in guestOptions" 
              :key="option" 
              :value="option"
              :disabled="option > room.capacity"
              class="py-2"
            >
              {{ option }} {{ option === 1 ? 'Guest' : 'Guests' }}
              {{ option > room.capacity ? ' (Exceeds capacity)' : '' }}
            </option>
          </select>
          
          <!-- Capacity Warning -->
          <div v-if="guestsExceedCapacity" class="mt-3 p-3 bg-red-50 border border-red-200 rounded-lg flex items-start gap-2">
            <span class="material-symbols-outlined text-red-500 text-lg flex-shrink-0">warning</span>
            <div class="text-red-700 text-sm">
              <p class="font-medium">Exceeds room capacity</p>
              <p>This room can accommodate maximum {{ room.capacity }} guests</p>
            </div>
          </div>
        </div>

        <!-- Reserve Button -->
        <button 
          @click="reserveRoom"
          :disabled="!canReserve"
          :class="[
            'w-full group relative flex items-center justify-center rounded-xl h-16 px-6 text-lg font-bold transition-all duration-300 shadow-lg overflow-hidden',
            canReserve 
              ? 'bg-gradient-to-r from-teal-700 to-teal-600 text-white hover:from-teal-600 hover:to-teal-500 hover:shadow-xl hover:scale-[1.02] active:scale-100' 
              : 'bg-gray-300 text-gray-500 cursor-not-allowed'
          ]"
        >
          <!-- Animated background effect for enabled state -->
          <div v-if="canReserve" class="absolute inset-0 bg-gradient-to-r from-teal-600 to-teal-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          
          <!-- Button content -->
          <div class="relative flex items-center gap-3">
            <span class="material-symbols-outlined text-xl">
              {{ canReserve ? 'hotel' : 'block' }}
            </span>
            {{ canReserve ? 'Reserve Now' : 'Cannot Reserve' }}
          </div>
          
          <!-- Loading animation (optional) -->
          <div v-if="canReserve" class="absolute right-6 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
            <span class="material-symbols-outlined text-lg">arrow_forward</span>
          </div>
        </button>
      </div>
    </div>

    <div class="mt-6 text-center text-sm text-gray-500">You won't be charged yet</div>

    <!-- Pricing Breakdown -->
    <div class="mt-6 pt-6 border-t border-gray-200 space-y-4 text-sm">
      <div class="flex justify-between text-gray-600">
        <span>${{ room.price }} x {{ nights }} night(s)</span>
        <span>${{ subtotal }}</span>
      </div>
      <div class="flex justify-between text-gray-600">
        <span>Taxes & fees</span>
        <span>${{ taxes }}</span>
      </div>
      <div class="flex justify-between font-bold text-xl text-gray-800 mt-4 pt-4 border-t border-gray-200">
        <span>Total</span>
        <span>${{ total }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { get as getFromStore } from '../../localStorage'

const props = defineProps({
  room: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const booking = ref({
  checkIn: '',
  checkOut: '',
  guests: 1
})

const guestOptions = ref([1, 2, 3, 4, 5, 6, 7, 8]) // Extended options to show capacity limits

// Computed properties
const guestsExceedCapacity = computed(() => {
  return booking.value.guests > props.room.capacity
})

const canReserve = computed(() => {
  return !guestsExceedCapacity.value && 
         booking.value.checkIn && 
         booking.value.checkOut && 
         booking.value.guests > 0
})

const nights = computed(() => {
  if (!booking.value.checkIn || !booking.value.checkOut) return 1
  const start = new Date(booking.value.checkIn)
  const end = new Date(booking.value.checkOut)
  const diff = Math.ceil((end - start) / (1000 * 60 * 60 * 24))
  return diff > 0 ? diff : 1
})

const subtotal = computed(() => props.room.price * nights.value)
const taxes = computed(() => parseFloat((subtotal.value * 0.1).toFixed(2)))
const total = computed(() => subtotal.value + taxes.value)

const reserveRoom = async () => {
  // Double-check capacity before proceeding
  if (guestsExceedCapacity.value) {
    alert(`This room can only accommodate ${props.room.capacity} guests. Please reduce the number of guests.`)
    return
  }

  if (!canReserve.value) {
    alert('Please fill in all required fields correctly.')
    return
  }

  const user = getFromStore('logged_in_user')
  if (!user?.access_token) {
    alert('You must be logged in to reserve a room.')
    return
  }

  try {
    const response = await axios.post(
      'https://romanat-restaurant-7.onrender.com/api/reservations/',
      {
        room_id: props.room.id,
        check_in: booking.value.checkIn,
        check_out: booking.value.checkOut,
        number_of_guests: parseInt(booking.value.guests),
        total_price: total.value,
        customer_id: user.id
      },
      {
        headers: {
          'Authorization': `Bearer ${user.access_token}`,
          'Content-Type': 'application/json'
        }
      }
    )

    // Reservation created successfully
    const reservationId = response.data.id

    // Redirect to confirm/payment page with reservationId
    router.push({
      name: 'Booking',
      state: { booking: response.data }
    })
  } catch (error) {
    console.error(error)
    if (error.response?.data?.detail) {
      alert(error.response.data.detail)
    } else {
      alert('Failed to create reservation. Please try again.')
    }
  }
}
</script>