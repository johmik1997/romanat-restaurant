<template>
  <div class="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-lg transition-shadow">
    <!-- Room Header -->
    <div class="flex items-start justify-between mb-4">
      <div>
        <h3 class="text-lg font-semibold text-gray-900">{{ room.roomNumber }}</h3>
        <p class="text-sm text-gray-500">{{ room.type }}</p>
      </div>
      <span :class="statusBadgeClasses">
        {{ room.status }}
      </span>
    </div>

    <!-- Room Details -->
    <div class="space-y-3 mb-4">
      <div class="flex items-center justify-between text-sm">
        <span class="text-gray-500">Floor:</span>
        <span class="font-medium text-gray-900">{{ room.floor }}</span>
      </div>
      <div class="flex items-center justify-between text-sm">
        <span class="text-gray-500">Beds:</span>
        <span class="font-medium text-gray-900">{{ room.beds }}</span>
      </div>
      <div class="flex items-center justify-between text-sm">
        <span class="text-gray-500">Capacity:</span>
        <span class="font-medium text-gray-900">{{ room.capacity }} guests</span>
      </div>
      <div class="flex items-center justify-between text-sm">
        <span class="text-gray-500">Price:</span>
        <span class="font-medium text-gray-900">${{ room.price }}/night</span>
      </div>
    </div>

    <!-- Guest Info (if occupied) -->
    <div v-if="room.status === 'Occupied' && room.currentGuest" class="mb-4 p-3 bg-gray-50 rounded-lg">
      <p class="text-sm font-medium text-gray-900">{{ room.currentGuest.name }}</p>
      <p class="text-xs text-gray-500">Check-out: {{ room.currentGuest.checkOut }}</p>
    </div>

    <!-- Action Buttons -->
    <div class="flex gap-2">
      <button 
        v-if="room.status === 'Available'"
        @click="$emit('book-room', room)"
        class="flex-1 bg-primary text-white py-2 px-3 rounded-lg text-sm font-medium hover:bg-primary/90 transition-colors"
      >
        Book Now
      </button>
      <button 
        v-if="room.status === 'Occupied'"
        @click="$emit('check-out', room)"
        class="flex-1 bg-green-600 text-white py-2 px-3 rounded-lg text-sm font-medium hover:bg-green-700 transition-colors"
      >
        Check-out
      </button>
      <button 
        v-if="room.status === 'Reserved'"
        @click="$emit('check-in', room)"
        class="flex-1 bg-blue-600 text-white py-2 px-3 rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors"
      >
        Check-in
      </button>
      <button 
        @click="$emit('view-details', room)"
        class="flex-1 border border-gray-300 text-gray-700 py-2 px-3 rounded-lg text-sm font-medium hover:bg-gray-50 transition-colors"
      >
        Details
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RoomCard',
  props: {
    room: {
      type: Object,
      required: true
    }
  },
  computed: {
    statusBadgeClasses() {
      const statusClasses = {
        'Available': 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800',
        'Occupied': 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800',
        'Reserved': 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800',
        'Maintenance': 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800',
        'Cleaning': 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800'
      }
      return statusClasses[this.room.status] || statusClasses['Available']
    }
  },
  emits: ['book-room', 'check-out', 'check-in', 'view-details']
}
</script>