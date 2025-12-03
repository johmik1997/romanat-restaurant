<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
    <!-- Total Rooms -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Total Rooms</p>
          <p class="text-3xl font-bold text-gray-900">{{ stats.totalRooms }}</p>
        </div>
        <div class="p-3 bg-blue-100 rounded-lg">
          <span class="material-symbols-outlined text-blue-600 text-2xl">meeting_room</span>
        </div>
      </div>
    </div>

    <!-- Available Rooms -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Available</p>
          <p class="text-3xl font-bold text-green-600">{{ stats.availableRooms }}</p>
        </div>
        <div class="p-3 bg-green-100 rounded-lg">
          <span class="material-symbols-outlined text-green-600 text-2xl">check_circle</span>
        </div>
      </div>
    </div>

    <!-- Occupied Rooms -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Occupied</p>
          <p class="text-3xl font-bold text-red-600">{{ stats.occupiedRooms }}</p>
        </div>
        <div class="p-3 bg-red-100 rounded-lg">
          <span class="material-symbols-outlined text-red-600 text-2xl">person</span>
        </div>
      </div>
    </div>

    <!-- Occupancy Rate -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Occupancy Rate</p>
          <p class="text-3xl font-bold text-purple-600">{{ stats.occupancyRate }}%</p>
        </div>
        <div class="p-3 bg-purple-100 rounded-lg">
          <span class="material-symbols-outlined text-purple-600 text-2xl">trending_up</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RoomStats',
  props: {
    stats: {
      type: Object,
      required: true
    }
  }
}
</script>