<template>
  <div class="mt-10">
    <!-- Tabs Navigation -->
    <div class="border-b border-gray-200">
      <nav class="flex -mb-px space-x-8">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          class="whitespace-nowrap py-4 px-1 border-b-2 font-semibold text-lg transition-colors duration-300"
          :class="activeTab === tab.id
            ? 'text-primary border-primary'
            : 'text-gray-500 hover:text-gray-700 border-transparent hover:border-gray-300'"
        >
          {{ tab.name }}
        </button>
      </nav>
    </div>

    <!-- Tab Content -->
    <div class="py-8">
      <!-- Details Tab -->
      <div v-if="activeTab === 'details'">
        <h3 class="text-2xl font-serif font-bold text-gray-800 mb-4">About this room</h3>
        <p class="text-gray-600 leading-relaxed text-lg">{{ room.description }}</p>

        <div class="grid grid-cols-2 gap-6 mt-8">
          <div class="flex items-center gap-3">
            <div class="h-12 w-12 bg-primary/10 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <div>
              <p class="font-semibold text-gray-800">{{ room.size }}</p>
              <p class="text-gray-600 text-sm">Room Size</p>
            </div>
          </div>

          <div class="flex items-center gap-3" v-if="room.view">
            <div class="h-12 w-12 bg-primary/10 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z" />
              </svg>
            </div>
            <div>
              <p class="font-semibold text-gray-800 capitalize">{{ room.view }} View</p>
              <p class="text-gray-600 text-sm">Balcony Access</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Amenities Tab -->
      <div v-else-if="activeTab === 'amenities'">
        <RoomAmenities :amenities="room.amenities" />
      </div>

      <!-- Reviews Tab -->
      <div v-else-if="activeTab === 'reviews'">
        <h3 class="text-2xl font-serif font-bold text-gray-800 mb-6">Guest Reviews</h3>
        <div v-if="room.reviews && room.reviews.length > 0" class="space-y-6">
          <div v-for="review in room.reviews" :key="review.id" class="bg-gray-50 rounded-2xl p-6">
            <div class="flex items-center gap-4 mb-4">
              <div class="h-12 w-12 bg-primary/10 rounded-full flex items-center justify-center">
                <span class="text-primary font-semibold">
                  {{ review.reviewer_name.split(' ').map(n => n[0]).join('') }}
                </span>
              </div>
              <div>
                <p class="font-semibold text-gray-800">{{ review.reviewer_name }}</p>
                <div class="flex items-center gap-1">
                  <svg class="w-4 h-4 text-accent" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <span class="text-sm text-gray-600">{{ review.rating }}</span>
                </div>
              </div>
            </div>
            <p class="text-gray-600 leading-relaxed">{{ review.comment }}</p>
          </div>
        </div>
        <p v-else class="text-gray-500">No reviews yet.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import RoomAmenities from './RoomAmenities.vue'

const props = defineProps({
  room: {
    type: Object,
    required: true
  }
})

const activeTab = ref('details')

const tabs = [
  { id: 'details', name: 'Details' },
  { id: 'amenities', name: 'Amenities' },
  { id: 'reviews', name: 'Reviews' }
]
</script>
