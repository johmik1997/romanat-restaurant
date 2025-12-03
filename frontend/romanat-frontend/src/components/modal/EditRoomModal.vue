<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
    <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
      <div class="p-6">
        <!-- Header -->
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-gray-900">Edit Room</h2>
          <button @click="$emit('close')" class="text-gray-500 hover:text-gray-700">
            <span class="material-symbols-outlined text-2xl">close</span>
          </button>
        </div>

        <!-- Edit Form -->
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Form fields similar to AddRoomModal but pre-filled -->
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Room Number</label>
              <input v-model="form.room_number" type="text" class="w-full rounded-lg border border-gray-300 px-3 py-2" required />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Price</label>
              <input v-model="form.price" type="number" class="w-full rounded-lg border border-gray-300 px-3 py-2" required />
            </div>
            <!-- Add more fields as needed -->
          </div>

          <!-- Action Buttons -->
          <div class="flex gap-3 pt-6 border-t border-gray-200">
            <button type="button" @click="$emit('close')" class="flex-1 bg-gray-300 text-gray-700 py-3 rounded-lg hover:bg-gray-400 transition-colors">
              Cancel
            </button>
            <button type="submit" class="flex-1 bg-primary text-white py-3 rounded-lg hover:bg-primary/90 transition-colors">
              Update Room
            </button>
          </div>
        </form>
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
  data() {
    return {
      form: {}
    }
  },
  watch: {
    room: {
      immediate: true,
      handler(newRoom) {
        if (newRoom) {
          this.form = { ...newRoom }
        }
      }
    }
  },
  methods: {
    handleSubmit() {
      this.$emit('update-room', this.form)
      this.$emit('close')
    }
  }
}
</script>