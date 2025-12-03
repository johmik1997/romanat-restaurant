<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
    <div class="bg-white rounded-2xl max-w-md w-full">
      <div class="p-6">
        <!-- Warning Icon -->
        <div class="flex justify-center mb-4">
          <span class="material-symbols-outlined text-6xl text-red-500">warning</span>
        </div>

        <!-- Content -->
        <div class="text-center">
          <h3 class="text-xl font-bold text-gray-900 mb-2">Delete Room</h3>
          <p class="text-gray-600 mb-6">
            Are you sure you want to delete room <strong>{{ room?.room_number }}</strong>? This action cannot be undone.
          </p>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-3">
          <button @click="$emit('close')" class="flex-1 bg-gray-300 text-gray-700 py-3 rounded-lg hover:bg-gray-400 transition-colors">
            Cancel
          </button>
          <button @click="handleConfirm" class="flex-1 bg-red-600 text-white py-3 rounded-lg hover:bg-red-700 transition-colors">
            Delete Room
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isOpen: Boolean,
    room: Object
  },
  methods: {
    handleConfirm() {
      this.$emit('confirm-delete', this.room)
      this.$emit('close')
    }
  }
}
</script>