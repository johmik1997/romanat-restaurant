<template>
  <div class="bg-[#3f7181] rounded-2xl shadow-2xl p-6 mx-4">
    <div class="grid grid-cols-1 md:grid-cols-5 gap-4 items-end">
      <!-- Check-in -->
      <div class="relative">
        <label class="block text-xs font-semibold text-gray-900 mb-2">Check-in</label>
        <div class="relative">
          <input 
            type="date" 
            class="w-full rounded-lg border border-gray-300 py-3 pl-10 pr-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent"
            v-model="checkinDate"
          />
          <div class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-700">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Check-out -->
      <div class="relative">
        <label class="block text-xs font-semibold text-gray-800 mb-2">Check-out</label>
        <div class="relative">
          <input 
            type="date" 
            class="w-full rounded-lg border border-gray-300 py-3 pl-10 pr-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent"
            v-model="checkoutDate"
          />
          <div class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Guests -->
      <div class="relative">
        <label class="block text-xs font-semibold text-gray-900 mb-2">Guests</label>
        <div class="relative">
          <select 
            class="w-full rounded-lg border border-gray-300 py-3 pl-10 pr-8 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent appearance-none"
            v-model="guests"
          >
            <option>1 Adult</option>
            <option>2 Adults</option>
            <option>2 Adults, 1 Child</option>
            <option>2 Adults, 2 Children</option>
          </select>
          <div class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-600">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
            </svg>
          </div>
          <div class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-600 pointer-events-none">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Room Type -->
      <div class="relative">
        <label class="block text-xs font-semibold text-gray-900 mb-2">Room Type</label>
        <div class="relative">
          <select 
            class="w-full rounded-lg border border-gray-300 py-3 pl-10 pr-8 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent appearance-none"
            v-model="roomType"
          >
            <option>Any</option>
            <option>Deluxe Room</option>
            <option>Executive Suite</option>
            <option>Presidential Suite</option>
          </select>
          <div class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-600">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
            </svg>
          </div>
          <div class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-600 pointer-events-none">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Search Button -->
      <button 
        class="bg-[#14ccbd] text-white rounded-lg py-3 font-bold hover:bg-teal-700 transition-all duration-300 shadow-lg hover:shadow-xl hover:scale-105 flex items-center justify-center gap-2"
        @click="checkAvailability"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
        </svg>
        Search
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const checkinDate = ref('')
const checkoutDate = ref('')
const guests = ref('2 Adults')
const roomType = ref('Any')

import { useRouter } from 'vue-router'

const router = useRouter()

const checkAvailability = () => {
  if (!checkinDate.value || !checkoutDate.value) {
    alert("Please select check-in and check-out dates")
    return
  }
  router.push({ name: 'Rooms' })
}

</script>