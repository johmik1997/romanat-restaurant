<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
    <div class="bg-white rounded-2xl w-full max-w-md mx-4 shadow-2xl">
      <!-- Header -->
      <div class="border-b border-gray-200 p-6">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-xl font-bold text-gray-900">Change Room Status</h2>
            <p class="text-gray-600 mt-1">Update availability for Room {{ room?.room_number }}</p>
          </div>
          <button 
            @click="$emit('close')" 
            class="text-gray-400 hover:text-gray-600 transition-colors p-2 hover:bg-gray-100 rounded-lg"
          >
            <span class="material-symbols-outlined text-2xl">close</span>
          </button>
        </div>
      </div>

      <!-- Current Status -->
      <div class="p-6 border-b border-gray-200">
        <div class="flex items-center justify-between">
          <span class="text-sm font-medium text-gray-700">Current Status:</span>
          <span :class="currentStatusBadgeClasses" class="text-sm font-medium">
            {{ formatStatus(room?.status) }}
          </span>
        </div>
      </div>

      <!-- Status Options -->
      <div class="p-6">
        <div class="space-y-3">
          <div 
            v-for="status in statusOptions" 
            :key="status.value"
            @click="selectStatus(status.value)"
            class="flex items-center gap-4 p-4 border-2 rounded-xl cursor-pointer transition-all duration-300 hover:shadow-md"
            :class="selectedStatus === status.value 
              ? 'border-primary bg-primary/5' 
              : 'border-gray-200 hover:border-gray-300'"
          >
            <div class="flex items-center justify-center w-8 h-8 rounded-full border-2"
                 :class="selectedStatus === status.value ? 'border-primary bg-primary' : 'border-gray-300'">
              <span v-if="selectedStatus === status.value" class="material-symbols-outlined text-white text-sm">
                check
              </span>
            </div>
            
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <span class="material-symbols-outlined text-lg" :class="status.iconColor">
                  {{ status.icon }}
                </span>
                <span class="font-medium text-gray-900">{{ status.label }}</span>
              </div>
              <p class="text-sm text-gray-600">{{ status.description }}</p>
            </div>
            
            <span :class="status.badgeClasses" class="text-xs">
              {{ status.badge }}
            </span>
          </div>
        </div>

        <!-- Additional Notes -->
        <div v-if="selectedStatus === 'maintenance'" class="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
          <div class="flex items-start gap-2">
            <span class="material-symbols-outlined text-yellow-600 text-lg mt-0.5">info</span>
            <div>
              <p class="text-sm font-medium text-yellow-800">Maintenance Mode</p>
              <p class="text-sm text-yellow-700 mt-1">
                Room will be unavailable for reservations and marked for maintenance.
              </p>
            </div>
          </div>
        </div>

        <div v-if="selectedStatus === 'cleaning'" class="mt-4 p-4 bg-purple-50 border border-purple-200 rounded-lg">
          <div class="flex items-start gap-2">
            <span class="material-symbols-outlined text-purple-600 text-lg mt-0.5">cleaning_services</span>
            <div>
              <p class="text-sm font-medium text-purple-800">Cleaning in Progress</p>
              <p class="text-sm text-purple-700 mt-1">
                Room is currently being cleaned and will be available shortly.
              </p>
            </div>
          </div>
        </div>

        <!-- Notes Input -->
        <div class="mt-6">
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Status Notes (Optional)
          </label>
          <textarea
            v-model="statusNotes"
            placeholder="Add any notes about this status change..."
            rows="3"
            class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300 resize-none"
          ></textarea>
        </div>

        <!-- Estimated Duration (for maintenance/cleaning) -->
        <div v-if="selectedStatus === 'maintenance' || selectedStatus === 'cleaning'" class="mt-4">
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Estimated Duration
          </label>
          <select
            v-model="estimatedDuration"
            class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
          >
            <option value="1">1 hour</option>
            <option value="2">2 hours</option>
            <option value="4">4 hours</option>
            <option value="8">8 hours (1 day)</option>
            <option value="24">24 hours</option>
            <option value="48">48 hours (2 days)</option>
            <option value="custom">Custom duration</option>
          </select>
        </div>

        <!-- Custom Duration Input -->
        <div v-if="estimatedDuration === 'custom'" class="mt-4">
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Custom Duration
          </label>
          <div class="flex gap-3">
            <input
              type="number"
              v-model.number="customDays"
              placeholder="Days"
              min="0"
              class="flex-1 rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
            >
            <input
              type="number"
              v-model.number="customHours"
              placeholder="Hours"
              min="0"
              max="23"
              class="flex-1 rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
            >
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex gap-3 p-6 border-t border-gray-200">
        <button
          type="button"
          @click="$emit('close')"
          class="flex-1 bg-gray-100 text-gray-700 py-3 px-4 rounded-xl hover:bg-gray-200 transition-all duration-300 font-medium"
        >
          Cancel
        </button>
        <button
          type="button"
          @click="confirmStatusChange"
          :disabled="!selectedStatus"
          :class="[
            'flex-1 py-3 px-4 rounded-xl transition-all duration-300 font-medium',
            selectedStatus 
              ? 'bg-primary text-white hover:bg-primary/90 shadow-lg hover:shadow-xl' 
              : 'bg-gray-300 text-gray-500 cursor-not-allowed'
          ]"
        >
          Update Status
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChangeStatusModal',
  props: {
    isOpen: Boolean,
    room: Object
  },
  data() {
    return {
      selectedStatus: null,
      statusNotes: '',
      estimatedDuration: '2',
      customDays: 0,
      customHours: 0,
      statusOptions: [
        {
          value: 'available',
          label: 'Available',
          description: 'Room is ready for reservations and check-ins',
          icon: 'check_circle',
          iconColor: 'text-green-600',
          badge: 'Ready',
          badgeClasses: 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800'
        },
        {
          value: 'occupied',
          label: 'Occupied',
          description: 'Guest is currently checked in to this room',
          icon: 'person',
          iconColor: 'text-red-600',
          badge: 'In Use',
          badgeClasses: 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800'
        },
        {
          value: 'reserved',
          label: 'Reserved',
          description: 'Room is booked for future dates',
          icon: 'event_available',
          iconColor: 'text-blue-600',
          badge: 'Booked',
          badgeClasses: 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800'
        },
        {
          value: 'maintenance',
          label: 'Maintenance',
          description: 'Room requires repairs or maintenance work',
          icon: 'build',
          iconColor: 'text-yellow-600',
          badge: 'Repairs',
          badgeClasses: 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800'
        },
        {
          value: 'cleaning',
          label: 'Cleaning',
          description: 'Room is being cleaned or prepared',
          icon: 'cleaning_services',
          iconColor: 'text-purple-600',
          badge: 'Cleaning',
          badgeClasses: 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800'
        }
      ]
    }
  },
  computed: {
    currentStatusBadgeClasses() {
      const status = this.room?.status
      const classes = {
        'available': 'text-green-600',
        'occupied': 'text-red-600',
        'reserved': 'text-blue-600',
        'maintenance': 'text-yellow-600',
        'cleaning': 'text-purple-600'
      }
      return classes[status] || 'text-gray-600'
    }
  },
  watch: {
    room: {
      immediate: true,
      handler(val) {
        if (val) {
          this.selectedStatus = val.status
        }
      }
    },
    isOpen: {
      handler(val) {
        if (val) {
          this.selectedStatus = this.room?.status
          this.statusNotes = ''
          this.estimatedDuration = '2'
          this.customDays = 0
          this.customHours = 0
        }
      }
    }
  },
  methods: {
    formatStatus(status) {
      const statusMap = {
        'available': 'Available',
        'occupied': 'Occupied',
        'reserved': 'Reserved',
        'maintenance': 'Maintenance',
        'cleaning': 'Cleaning'
      }
      return statusMap[status] || status
    },

    selectStatus(status) {
      this.selectedStatus = status
    },

    confirmStatusChange() {
      if (!this.selectedStatus) return

      const statusData = {
        status: this.selectedStatus,
        notes: this.statusNotes,
        changedBy: 'Staff User', // Replace with actual user
        timestamp: new Date().toISOString()
      }

      // Add duration info for maintenance/cleaning
      if (this.selectedStatus === 'maintenance' || this.selectedStatus === 'cleaning') {
        statusData.estimatedDuration = this.getEstimatedDuration()
      }

      this.$emit('status-change', this.selectedStatus, statusData)
      this.$emit('close')
    },

    getEstimatedDuration() {
      if (this.estimatedDuration === 'custom') {
        return {
          days: this.customDays,
          hours: this.customHours,
          totalHours: (this.customDays * 24) + this.customHours
        }
      }
      
      return {
        hours: parseInt(this.estimatedDuration),
        totalHours: parseInt(this.estimatedDuration)
      }
    }
  }
}
</script>

<style scoped>
/* Smooth transitions for interactive elements */
.status-option {
  transition: all 0.3s ease;
}

.status-option:hover {
  transform: translateY(-1px);
}
</style>