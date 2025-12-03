<template>
  <div class="space-y-4">
    <div v-for="room in rooms" :key="room.number" class="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 bg-primary text-white rounded-lg flex items-center justify-center">
          <span class="material-symbols-outlined text-lg">meeting_room</span>
        </div>
        <div>
          <div class="font-medium text-gray-900">Room {{ room.number }}</div>
          <div class="text-sm text-gray-500">{{ room.type }}</div>
        </div>
      </div>
      <div class="text-right">
        <div class="font-medium text-gray-900">${{ room.revenue.toLocaleString() }}</div>
        <div class="text-sm text-gray-500">{{ room.occupancy }}% occupancy</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopRoomsList',
  props: {
    rooms: Array
  }
}
</script>