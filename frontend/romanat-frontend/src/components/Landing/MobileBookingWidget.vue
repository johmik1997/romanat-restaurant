<template>
  <div class="space-y-4">
    <!-- Check-in / Check-out Row -->
    <div class="grid grid-cols-2 gap-3">
      <div>
        <label class="block text-xs font-semibold text-white/80 mb-1">Check-in</label>
        <input 
          type="date" 
          class="w-full rounded-lg bg-white/20 border border-white/30 text-white py-3 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
          v-model="checkinDate"
        />
      </div>
      <div>
        <label class="block text-xs font-semibold text-white/80 mb-1">Check-out</label>
        <input 
          type="date" 
          class="w-full rounded-lg bg-white/20 border border-white/30 text-white py-3 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
          v-model="checkoutDate"
        />
      </div>
    </div>

    <!-- Guests & Room Type -->
    <div class="grid grid-cols-2 gap-3">
      <div>
        <label class="block text-xs font-semibold text-white/80 mb-1">Guests</label>
        <select 
          class="w-full rounded-lg bg-white/20 border border-white/30 text-white py-3 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
          v-model="guests"
        >
          <option class="text-black">1 Adult</option>
          <option class="text-black">2 Adults</option>
          <option class="text-black">2 Adults, 1 Child</option>
          <option class="text-black">2 Adults, 2 Children</option>
        </select>
      </div>
      <div>
        <label class="block text-xs font-semibold text-white/80 mb-1">Room Type</label>
        <select 
          class="w-full rounded-lg bg-white/20 border border-white/30 text-white py-3 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
          v-model="roomType"
        >
          <option class="text-black">Any</option>
          <option class="text-black">Deluxe Room</option>
          <option class="text-black">Executive Suite</option>
          <option class="text-black">Presidential Suite</option>
        </select>
      </div>
    </div>

    <!-- Search Button -->
    <button 
      class="w-full bg-primary text-white rounded-lg py-4 font-bold hover:bg-teal-700 transition-colors flex items-center justify-center gap-2 shadow-lg"
      @click="checkAvailability"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
      </svg>
      Check Availability
    </button>

    <!-- Quick Info -->
    <div class="flex items-center justify-center gap-4 text-white/70 text-xs">
      <div class="flex items-center gap-1">
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/>
        </svg>
        Best Rate Guarantee
      </div>
      <div class="flex items-center gap-1">
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
        </svg>
        Free Cancellation
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const checkinDate = ref('')
const checkoutDate = ref('')
const guests = ref('2 Adults')
const roomType = ref('Any')

const checkAvailability = () => {
  console.log('Checking availability on mobile:', {
    checkinDate: checkinDate.value,
    checkoutDate: checkoutDate.value,
    guests: guests.value,
    roomType: roomType.value
  })
}
</script>