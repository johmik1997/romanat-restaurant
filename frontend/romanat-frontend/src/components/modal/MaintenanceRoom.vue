<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
    <div class="bg-white rounded-2xl w-full max-w-2xl mx-4 max-h-[90vh] overflow-y-auto shadow-2xl">
      <!-- Header -->
      <div class="sticky top-0 bg-white border-b border-gray-200 p-6 rounded-t-2xl">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-gray-900">Log Maintenance</h2>
            <p class="text-gray-600 mt-1">Report maintenance issue for Room {{ room?.room_number }}</p>
          </div>
          <button 
            @click="$emit('close')" 
            class="text-gray-400 hover:text-gray-600 transition-colors p-2 hover:bg-gray-100 rounded-lg"
          >
            <span class="material-symbols-outlined text-2xl">close</span>
          </button>
        </div>
      </div>

      <!-- Form -->
      <form @submit.prevent="submitMaintenance" class="p-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Maintenance Type -->
          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Maintenance Type <span class="text-red-500">*</span>
            </label>
            <select
              v-model="form.type"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
              required
            >
              <option value="">Select Maintenance Type</option>
              <option value="Electrical">Electrical Issue</option>
              <option value="Plumbing">Plumbing Issue</option>
              <option value="HVAC">HVAC/AC Issue</option>
              <option value="Furniture">Furniture Repair</option>
              <option value="Appliance">Appliance Repair</option>
              <option value="Cleaning">Deep Cleaning</option>
              <option value="Painting">Painting</option>
              <option value="Carpet">Carpet Cleaning/Repair</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <!-- Priority -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Priority <span class="text-red-500">*</span>
            </label>
            <select
              v-model="form.priority"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
              required
            >
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
              <option value="urgent">Urgent</option>
            </select>
          </div>

          <!-- Status -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Status <span class="text-red-500">*</span>
            </label>
            <select
              v-model="form.status"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
              required
            >
              <option value="reported">Reported</option>
              <option value="in-progress">In Progress</option>
              <option value="completed">Completed</option>
            </select>
          </div>

          <!-- Description -->
          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Description <span class="text-red-500">*</span>
            </label>
            <textarea
              v-model="form.description"
              placeholder="Describe the maintenance issue in detail..."
              rows="4"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300 resize-none"
              required
            ></textarea>
          </div>

          <!-- Estimated Duration -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Estimated Duration
            </label>
            <select
              v-model="form.estimatedDuration"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
            >
              <option value="1">1 hour</option>
              <option value="2">2 hours</option>
              <option value="4">4 hours</option>
              <option value="8">8 hours</option>
              <option value="24">24 hours</option>
              <option value="48">48 hours</option>
              <option value="custom">Custom</option>
            </select>
          </div>

          <!-- Assigned To -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Assigned To
            </label>
            <select
              v-model="form.assignedTo"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
            >
              <option value="">Unassigned</option>
              <option value="maintenance-team">Maintenance Team</option>
              <option value="housekeeping">Housekeeping</option>
              <option value="external-vendor">External Vendor</option>
              <option value="technician">Technician</option>
            </select>
          </div>

          <!-- Custom Duration -->
          <div v-if="form.estimatedDuration === 'custom'" class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Custom Duration
            </label>
            <div class="grid grid-cols-2 gap-4">
              <div>
                <input
                  type="number"
                  v-model.number="form.customDays"
                  placeholder="Days"
                  min="0"
                  class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
                >
              </div>
              <div>
                <input
                  type="number"
                  v-model.number="form.customHours"
                  placeholder="Hours"
                  min="0"
                  max="23"
                  class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300"
                >
              </div>
            </div>
          </div>

          <!-- Additional Notes -->
          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Additional Notes
            </label>
            <textarea
              v-model="form.notes"
              placeholder="Any additional information or instructions..."
              rows="3"
              class="w-full rounded-xl border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent transition-colors duration-300 resize-none"
            ></textarea>
          </div>
        </div>

        <!-- Priority Indicators -->
        <div class="mt-6 p-4 border rounded-xl" :class="priorityClasses">
          <div class="flex items-center gap-2">
            <span class="material-symbols-outlined" :class="priorityIconClasses">
              {{ priorityIcon }}
            </span>
            <div>
              <p class="font-medium" :class="priorityTextClasses">{{ priorityLabel }}</p>
              <p class="text-sm">{{ priorityDescription }}</p>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-3 pt-6 mt-6 border-t border-gray-200">
          <button
            type="button"
            @click="$emit('close')"
            class="flex-1 bg-gray-100 text-gray-700 py-3 px-4 rounded-xl hover:bg-gray-200 transition-all duration-300 font-medium"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="flex-1 bg-primary text-white py-3 px-4 rounded-xl hover:bg-primary/90 transition-all duration-300 font-medium shadow-lg hover:shadow-xl"
          >
            Log Maintenance
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MaintenanceModal',
  props: {
    isOpen: Boolean,
    room: Object
  },
  data() {
    return {
      form: {
        type: '',
        priority: 'medium',
        status: 'reported',
        description: '',
        estimatedDuration: '2',
        assignedTo: '',
        customDays: 0,
        customHours: 0,
        notes: ''
      }
    }
  },
  computed: {
    priorityClasses() {
      const classes = {
        'low': 'border-green-200 bg-green-50',
        'medium': 'border-yellow-200 bg-yellow-50',
        'high': 'border-orange-200 bg-orange-50',
        'urgent': 'border-red-200 bg-red-50'
      }
      return classes[this.form.priority] || classes.medium
    },
    priorityIconClasses() {
      const classes = {
        'low': 'text-green-600',
        'medium': 'text-yellow-600',
        'high': 'text-orange-600',
        'urgent': 'text-red-600'
      }
      return classes[this.form.priority] || classes.medium
    },
    priorityTextClasses() {
      const classes = {
        'low': 'text-green-800',
        'medium': 'text-yellow-800',
        'high': 'text-orange-800',
        'urgent': 'text-red-800'
      }
      return classes[this.form.priority] || classes.medium
    },
    priorityIcon() {
      const icons = {
        'low': 'low_priority',
        'medium': 'schedule',
        'high': 'warning',
        'urgent': 'error'
      }
      return icons[this.form.priority] || icons.medium
    },
    priorityLabel() {
      const labels = {
        'low': 'Low Priority',
        'medium': 'Medium Priority',
        'high': 'High Priority',
        'urgent': 'Urgent Priority'
      }
      return labels[this.form.priority] || labels.medium
    },
    priorityDescription() {
      const descriptions = {
        'low': 'Address within 7 days',
        'medium': 'Address within 3 days',
        'high': 'Address within 24 hours',
        'urgent': 'Address immediately - room unavailable'
      }
      return descriptions[this.form.priority] || descriptions.medium
    }
  },
  watch: {
    isOpen: {
      handler(val) {
        if (val) {
          this.resetForm()
        }
      }
    }
  },
  methods: {
    resetForm() {
      this.form = {
        type: '',
        priority: 'medium',
        status: 'reported',
        description: '',
        estimatedDuration: '2',
        assignedTo: '',
        customDays: 0,
        customHours: 0,
        notes: ''
      }
    },
    submitMaintenance() {
      if (!this.validateForm()) {
        return
      }

      const maintenanceData = {
        ...this.form,
        roomId: this.room?.id,
        roomNumber: this.room?.room_number,
        reportedDate: new Date().toISOString(),
        estimatedDuration: this.getEstimatedDuration()
      }

      this.$emit('maintenance-logged', maintenanceData)
      this.$emit('close')
    },
    validateForm() {
      if (!this.form.type) {
        alert('Please select a maintenance type')
        return false
      }
      if (!this.form.description.trim()) {
        alert('Please provide a description')
        return false
      }
      return true
    },
    getEstimatedDuration() {
      if (this.form.estimatedDuration === 'custom') {
        return {
          days: this.form.customDays,
          hours: this.form.customHours,
          totalHours: (this.form.customDays * 24) + this.form.customHours
        }
      }
      
      return {
        hours: parseInt(this.form.estimatedDuration),
        totalHours: parseInt(this.form.estimatedDuration)
      }
    }
  }
}
</script>