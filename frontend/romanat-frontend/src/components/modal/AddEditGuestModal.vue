<template>
  <transition name="fade">
    <div
      v-if="show"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50"
    >
      <div
        class="bg-white rounded-xl shadow-lg w-full max-w-2xl p-6 relative max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-bold text-gray-900">{{ isEditMode ? 'Edit Guest' : 'Add New Guest' }}</h2>
          <button @click="close" class="text-gray-500 hover:text-gray-700">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <div class="p-4">
          <form @submit.prevent="saveGuest" class="space-y-6 text-black">
            <!-- First Name -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">First Name *</label>
              <input 
                v-model="form.first_name"
                type="text" 
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
                placeholder="Enter first name"
              />
            </div>

            <!-- Last Name -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Last Name *</label>
              <input 
                v-model="form.last_name"
                type="text" 
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
                placeholder="Enter last name"
              />
            </div>

            <!-- Email -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Email *</label>
              <input 
                v-model="form.email"
                type="email" 
                required
                :disabled="isEditMode"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40 disabled:bg-gray-50"
                placeholder="Enter email address"
              />
            </div>

            <!-- Phone -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Phone Number</label>
              <input 
                v-model="form.phone"
                type="tel" 
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
                placeholder="Enter phone number"
              />
            </div>

            <!-- Username -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Username *</label>
              <input 
                v-model="form.username"
                type="text" 
                required
                :disabled="isEditMode"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40 disabled:bg-gray-50"
                placeholder="Enter username"
              />
            </div>

            <!-- Password (only for new guests) -->
            <div v-if="!isEditMode">
              <label class="block text-sm font-medium text-gray-700 mb-2">Password *</label>
              <input 
                v-model="form.password"
                type="password" 
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
                placeholder="Enter password"
              />
              <p class="text-xs text-gray-500 mt-1">Minimum 8 characters</p>
            </div>

            <!-- Role -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Role *</label>
              <select 
                v-model="form.role"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
              >
                <option value="">Select a role</option>
                <option value="Customer">Customer</option>
                <option value="Receptionist">Receptionist</option>
                <option value="Manager">Manager</option>
                <option value="Admin">Admin</option>
              </select>
            </div>

            <!-- Status -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Status *</label>
              <select 
                v-model="form.status"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
              >
                <option value="active">Active</option>
                <option value="inactive">Inactive</option>
                <option value="pending">Pending</option>
                <option value="suspended">Suspended</option>
              </select>
            </div>

            <!-- Address -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Address</label>
              <textarea 
                v-model="form.address"
                rows="2"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
                placeholder="Enter address"
              ></textarea>
            </div>

            <!-- Notes -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Notes</label>
              <textarea 
                v-model="form.notes"
                rows="2"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-[#0f766e]/40"
                placeholder="Any additional notes..."
              ></textarea>
            </div>
          </form>
        </div>

        <!-- Footer -->
        <div class="flex justify-end gap-3 p-6 border-t border-gray-200 bg-gray-50">
          <button 
            @click="close"
            type="button"
            class="px-6 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Cancel
          </button>
          <button 
            @click="saveGuest"
            :disabled="!isFormValid"
            class="px-6 py-2 text-sm font-medium text-white bg-[#0f766e] border border-transparent rounded-lg hover:bg-[#0f766e]/60 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            {{ isEditMode ? 'Update Guest' : 'Create Guest' }}
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'AddEditGuestModal',
  props: {
    show: {
      type: Boolean,
      default: false
    },
    guest: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        username: '',
        password: '',
        role: 'Customer',
        status: 'active',
        address: '',
        notes: ''
      }
    }
  },
  computed: {
    isEditMode() {
      return this.guest !== null
    },
    
    isFormValid() {
      const requiredFields = ['first_name', 'last_name', 'email', 'username', 'role', 'status']
      if (!this.isEditMode) {
        requiredFields.push('password')
      }
      
      return requiredFields.every(field => {
        const value = this.form[field]
        return value && value.toString().trim().length > 0
      })
    }
  },
  watch: {
    show(newVal) {
      if (newVal) {
        this.initializeForm()
      } else {
        this.resetForm()
      }
    },
    
    guest(newGuest) {
      if (newGuest) {
        this.initializeForm()
      }
    }
  },
  methods: {
    initializeForm() {
      if (this.guest) {
        // Edit mode: populate form with guest data
        this.form = {
          first_name: this.guest.first_name || '',
          last_name: this.guest.last_name || '',
          email: this.guest.email || '',
          phone: this.guest.phone || '',
          username: this.guest.username || '',
          password: '', // Don't show password in edit mode
          role: this.guest.role?.name || 'Customer',
          status: this.guest.status?.toLowerCase() || 'active',
          address: this.guest.address || '',
          notes: this.guest.notes || ''
        }
      } else {
        // Add mode: reset form
        this.resetForm()
      }
    },
    
    resetForm() {
      this.form = {
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        username: '',
        password: '',
        role: 'Customer',
        status: 'active',
        address: '',
        notes: ''
      }
    },
    
    close() {
      this.$emit('close')
    },
    
    async saveGuest() {
      if (!this.isFormValid) {
        alert('Please fill in all required fields.')
        return
      }

      try {
        // Prepare guest data
        const guestData = {
          first_name: this.form.first_name.trim(),
          last_name: this.form.last_name.trim(),
          email: this.form.email.trim(),
          phone: this.form.phone.trim() || null,
          username: this.form.username.trim(),
          role: this.form.role,
          status: this.form.status,
          address: this.form.address.trim() || null,
          notes: this.form.notes.trim() || null
        }

        // Add password for new guests
        if (!this.isEditMode) {
          guestData.password = this.form.password
        }

        console.log('Saving guest:', guestData)
        
        // Emit the guest data
        this.$emit('save', guestData)
        this.resetForm()
        
      } catch (error) {
        console.error('Error saving guest:', error)
        alert(`Failed to ${this.isEditMode ? 'update' : 'create'} guest. Please try again.`)
      }
    }
  }
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}
</style>