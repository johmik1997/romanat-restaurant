<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
    <div class="bg-white rounded-2xl w-full max-w-4xl mx-4 max-h-[90vh] overflow-y-auto shadow-2xl">
      <!-- Header -->
      <div class="sticky top-0 bg-white border-b border-gray-200 p-6 rounded-t-2xl">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4">
            <img 
              :src="user.avatar || '/api/placeholder/80/80'" 
              class="w-16 h-16 rounded-full object-cover border-2 border-gray-300"
              :alt="user.first_name"
            >
            <div>
              <h2 class="text-2xl font-bold text-gray-900">{{ user.first_name }}</h2>
              <p class="text-gray-600">{{ user.email }}</p>
              <div class="flex items-center gap-2 mt-1">
                <span :class="statusBadgeClasses" class="text-xs">
                  {{ user.status === 'Active' ? 'Active' : 'Inactive' }}
                </span>
                <span :class="roleBadgeClasses" class="text-xs">
                  {{ formatRole(user.role.name) }}
                </span>
              </div>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <button 
              @click="$emit('edit', user)"
              class="p-2 text-green-600 hover:text-green-900 hover:bg-green-50 rounded-lg transition-colors"
              title="Edit User"
            >
              <span class="material-symbols-outlined text-xl">edit</span>
            </button>
            <button 
              @click="$emit('close')" 
              class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <span class="material-symbols-outlined text-2xl">close</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div class="p-6">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <!-- Left Column - User Information -->
          <div class="lg:col-span-2 space-y-6">
            <!-- Personal Information Card -->
            <div class="bg-gray-50 rounded-xl p-6 border border-gray-200">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <span class="material-symbols-outlined text-gray-600">person</span>
                Personal Information
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="text-sm font-medium text-gray-500">Full Name</label>
                  <p class="text-gray-900 font-medium mt-1">{{ user.first_name + " "+user.last_name }}</p>
                </div>
                <div>
                  <label class="text-sm font-medium text-gray-500">Email Address</label>
                  <p class="text-gray-900 font-medium mt-1">{{ user.email }}</p>
                </div>
                <div>
                  <label class="text-sm font-medium text-gray-500">Phone Number</label>
                  <p class="text-gray-900 font-medium mt-1">{{ user.phone || 'Not provided' }}</p>
                </div>
                <div>
                  <label class="text-sm font-medium text-gray-500">Department</label>
                  <p class="text-gray-900 font-medium mt-1">{{ user.department || 'Not assigned' }}</p>
                </div>
              </div>
            </div>

            <!-- Role & Permissions Card -->
            <div class="bg-gray-50 rounded-xl p-6 border border-gray-200">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <span class="material-symbols-outlined text-gray-600">admin_panel_settings</span>
                Role & Permissions
              </h3>
              
              <!-- Role Information -->
              <div class="mb-6">
                <label class="text-sm font-medium text-gray-500 mb-2">User Role</label>
                <div class="flex items-center gap-3 p-3 bg-white rounded-lg border border-gray-200">
                  <span :class="roleIconClasses" class="material-symbols-outlined text-2xl">
                    {{ roleIcon }}
                  </span>
                  <div>
                    <p class="font-semibold text-gray-900">{{ formatRole(user.role.name) }}</p>
                    <p class="text-sm text-gray-600">{{ roleDescription }}</p>
                  </div>
                </div>
              </div>

              <!-- Permissions -->
              <div>
                <label class="text-sm font-medium text-gray-500 mb-3">Assigned Permissions</label>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                  <div 
                    v-for="permission in userPermissions" 
                    :key="permission.value"
                    class="flex items-center gap-3 p-3 bg-white rounded-lg border border-gray-200"
                  >
                    <span class="material-symbols-outlined text-green-500 text-lg">check_circle</span>
                    <div>
                      <p class="font-medium text-gray-900 text-sm">{{ permission.label }}</p>
                      <p class="text-xs text-gray-500">{{ permission.description }}</p>
                    </div>
                  </div>
                </div>
                <div v-if="userPermissions.length === 0" class="text-center py-4 text-gray-500">
                  <span class="material-symbols-outlined text-4xl mb-2">lock_open</span>
                  <p>No specific permissions assigned</p>
                </div>
              </div>
            </div>

            <!-- Activity Log Card -->
            <div class="bg-gray-50 rounded-xl p-6 border border-gray-200">
              <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <span class="material-symbols-outlined text-gray-600">history</span>
                Recent Activity
              </h3>
              <div class="space-y-4">
                <div 
                  v-for="activity in recentActivities" 
                  :key="activity.id"
                  class="flex items-start gap-3 p-3 bg-white rounded-lg border border-gray-200"
                >
                  <span class="material-symbols-outlined text-blue-500 mt-0.5" :class="activity.iconColor">
                    {{ activity.icon }}
                  </span>
                  <div class="flex-1">
                    <p class="text-sm font-medium text-gray-900">{{ activity.action }}</p>
                    <p class="text-xs text-gray-500 mt-1">{{ activity.details }}</p>
                    <p class="text-xs text-gray-400 mt-1">{{ activity.timestamp }}</p>
                  </div>
                </div>
                <div v-if="recentActivities.length === 0" class="text-center py-4 text-gray-500">
                  <span class="material-symbols-outlined text-4xl mb-2">inventory_2</span>
                  <p>No recent activity</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column - Quick Info & Actions -->
          <div class="space-y-6">
            <!-- Account Status Card -->
            <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm">
              <h3 class="text-lg font-semibold text-gray-900 mb-4">Account Status</h3>
              <div class="space-y-4">
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Status</span>
                  <span :class="statusBadgeClasses" class="text-xs">
                    {{ user.status === 'Active' ? 'Active' : 'Inactive' }}
                  </span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Last Login</span>
                  <span class="text-sm font-medium text-gray-900">{{ formatLastLogin(user.last_login) }}</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Account Created</span>
                  <span class="text-sm font-medium text-gray-900">{{ formatDate(user.created_at) }}</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Password Last Changed</span>
                  <span class="text-sm font-medium text-gray-900">{{ formatDate(user.password_changed_at) || 'Never' }}</span>
                </div>
              </div>
            </div>

            <!-- Quick Actions Card -->
            <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm">
              <h3 class="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h3>
              <div class="space-y-3">
                <button 
                  @click="sendResetPassword"
                  class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-blue-200 hover:border-blue-300 hover:bg-blue-50 transition-colors"
                >
                  <span class="material-symbols-outlined text-blue-600">key</span>
                  <div>
                    <p class="font-medium text-gray-900">Reset Password</p>
                    <p class="text-sm text-gray-500">Send password reset email</p>
                  </div>
                </button>
                
                <button 
                  @click="toggleUserStatus"
                  :class="[
                    'w-full flex items-center gap-3 p-3 text-left rounded-lg border transition-colors',
                    user.status === 'active' 
                      ? 'border-orange-200 hover:border-orange-300 hover:bg-orange-50' 
                      : 'border-green-200 hover:border-green-300 hover:bg-green-50'
                  ]"
                >
                  <span 
                    class="material-symbols-outlined"
                    :class="user.status === 'Active' ? 'text-orange-600' : 'text-green-600'"
                  >
                    {{ user.status === 'Active' ? 'lock' : 'lock_open' }}
                  </span>
                  <div>
                    <p class="font-medium text-gray-900">
                      {{ user.status === 'Active' ? 'Deactivate User' : 'Activate User' }}
                    </p>
                    <p class="text-sm text-gray-500">
                      {{ user.status === 'Active' ? 'Temporarily disable account' : 'Reactivate user account' }}
                    </p>
                  </div>
                </button>
                
                <button 
                  @click="sendWelcomeEmail"
                  class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-purple-200 hover:border-purple-300 hover:bg-purple-50 transition-colors"
                >
                  <span class="material-symbols-outlined text-purple-600">mail</span>
                  <div>
                    <p class="font-medium text-gray-900">Send Welcome Email</p>
                    <p class="text-sm text-gray-500">System introduction and guidelines</p>
                  </div>
                </button>
                
                <button 
                  @click="generateAccessReport"
                  class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-gray-300 hover:bg-gray-50 transition-colors"
                >
                  <span class="material-symbols-outlined text-gray-600">summarize</span>
                  <div>
                    <p class="font-medium text-gray-900">Access Report</p>
                    <p class="text-sm text-gray-500">Generate usage statistics</p>
                  </div>
                </button>
              </div>
            </div>

            <!-- System Access Card -->
            <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm">
              <h3 class="text-lg font-semibold text-gray-900 mb-4">System Access</h3>
              <div class="space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Can Manage Users</span>
                  <span class="material-symbols-outlined text-green-500" v-if="hasPermission('users:write')">
                    check_circle
                  </span>
                  <span class="material-symbols-outlined text-gray-300" v-else>
                    cancel
                  </span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Can View Reports</span>
                  <span class="material-symbols-outlined text-green-500" v-if="hasPermission('reports:read')">
                    check_circle
                  </span>
                  <span class="material-symbols-outlined text-gray-300" v-else>
                    cancel
                  </span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Can Manage Reservations</span>
                  <span class="material-symbols-outlined text-green-500" v-if="hasPermission('reservations:write')">
                    check_circle
                  </span>
                  <span class="material-symbols-outlined text-gray-300" v-else>
                    cancel
                  </span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Can Manage Rooms</span>
                  <span class="material-symbols-outlined text-green-500" v-if="hasPermission('rooms:write')">
                    check_circle
                  </span>
                  <span class="material-symbols-outlined text-gray-300" v-else>
                    cancel
                  </span>
                </div>
              </div>
            </div>

            <!-- Contact Information -->
            <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm">
              <h3 class="text-lg font-semibold text-gray-900 mb-4">Contact</h3>
              <div class="space-y-3">
                <button 
                  @click="sendEmail"
                  class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-gray-300 hover:bg-gray-50 transition-colors"
                >
                  <span class="material-symbols-outlined text-gray-600">mail</span>
                  <div>
                    <p class="font-medium text-gray-900">Send Email</p>
                    <p class="text-sm text-gray-500">{{ user.email }}</p>
                  </div>
                </button>
                
                <button 
                  v-if="user.phone"
                  @click="makeCall"
                  class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-gray-300 hover:bg-gray-50 transition-colors"
                >
                  <span class="material-symbols-outlined text-gray-600">call</span>
                  <div>
                    <p class="font-medium text-gray-900">Make Call</p>
                    <p class="text-sm text-gray-500">{{ user.phone }}</p>
                  </div>
                </button>
                
                <button 
                  @click="sendSMS"
                  v-if="user.phone"
                  class="w-full flex items-center gap-3 p-3 text-left rounded-lg border border-gray-200 hover:border-gray-300 hover:bg-gray-50 transition-colors"
                >
                  <span class="material-symbols-outlined text-gray-600">sms</span>
                  <div>
                    <p class="font-medium text-gray-900">Send SMS</p>
                    <p class="text-sm text-gray-500">{{ user.phone }}</p>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserDetailsModal',
  props: {
    isOpen: Boolean,
    user: Object
  },
  data() {
    return {
      permissionOptions: [
        { 
          value: 'users:read', 
          label: 'View Users', 
          description: 'Can view user list and details' 
        },
        { 
          value: 'users:write', 
          label: 'Manage Users', 
          description: 'Can create, edit, and delete users' 
        },
        { 
          value: 'reservations:read', 
          label: 'View Reservations', 
          description: 'Can view reservation details' 
        },
        { 
          value: 'reservations:write', 
          label: 'Manage Reservations', 
          description: 'Can create and modify reservations' 
        },
        { 
          value: 'rooms:read', 
          label: 'View Rooms', 
          description: 'Can view room information' 
        },
        { 
          value: 'rooms:write', 
          label: 'Manage Rooms', 
          description: 'Can update room status and details' 
        },
        { 
          value: 'reports:read', 
          label: 'View Reports', 
          description: 'Can access system reports' 
        },
        { 
          value: 'reports:write', 
          label: 'Generate Reports', 
          description: 'Can create and export reports' 
        }
      ]
    }
  },
  computed: {
    statusBadgeClasses() {
      return this.user.status === 'Active' 
        ? 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800'
        : 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800'
    },
    
    roleBadgeClasses() {
      const classes = {
        'admin': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800',
        'manager': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800',
        'receptionist': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800',
        'housekeeping': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800'
      }
      return classes[this.user.role] || 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800'
    },
    
    roleIconClasses() {
      const classes = {
        'admin': 'text-red-600',
        'manager': 'text-blue-600',
        'receptionist': 'text-green-600',
        'housekeeping': 'text-purple-600'
      }
      return classes[this.user.role] || 'text-gray-600'
    },
    
    roleIcon() {
      const icons = {
        'admin': 'admin_panel_settings',
        'manager': 'manage_accounts',
        'receptionist': 'support_agent',
        'housekeeping': 'cleaning_services'
      }
      return icons[this.user.role] || 'person'
    },
    
    roleDescription() {
      const descriptions = {
        'admin': 'Full system access and administrative privileges',
        'manager': 'Department management and oversight',
        'receptionist': 'Front desk operations and guest services',
        'housekeeping': 'Room maintenance and cleaning operations'
      }
      return descriptions[this.user.role] || 'System user'
    },
    
    userPermissions() {
      if (!this.user.permissions) return []
      return this.permissionOptions.filter(permission => 
        this.user.permissions.includes(permission.value)
      )
    },
    
    recentActivities() {
      // Mock data - replace with actual API call
      return [
        {
          id: 1,
          action: 'Password Changed',
          details: 'User updated their password',
          timestamp: '2 hours ago',
          icon: 'key',
          iconColor: 'text-green-500'
        },
        {
          id: 2,
          action: 'Logged In',
          details: 'Accessed system from Chrome on Windows',
          timestamp: '4 hours ago',
          icon: 'login',
          iconColor: 'text-blue-500'
        },
        {
          id: 3,
          action: 'Updated Profile',
          details: 'Changed phone number and department',
          timestamp: '1 day ago',
          icon: 'edit',
          iconColor: 'text-purple-500'
        },
        {
          id: 4,
          action: 'Viewed Reports',
          details: 'Accessed monthly occupancy report',
          timestamp: '2 days ago',
          icon: 'summarize',
          iconColor: 'text-orange-500'
        }
      ]
    }
  },
  methods: {
    formatRole(role) {
      const roleMap = {
        'admin': 'Administrator',
        'manager': 'Manager',
        'receptionist': 'Receptionist',
        'housekeeping': 'Housekeeping'
      }
      return roleMap[role] || role
    },
    
    formatLastLogin(dateString) {
      if (!dateString) return 'Never'
      const date = new Date(dateString)
      const now = new Date()
      const diffTime = Math.abs(now - date)
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
      
      if (diffDays === 1) return 'Yesterday'
      if (diffDays < 7) return `${diffDays} days ago`
      if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
      return date.toLocaleDateString()
    },
    
    formatDate(dateString) {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    },
    
    hasPermission(permission) {
      return this.user.permissions && this.user.permissions.includes(permission)
    },
    
    sendResetPassword() {
      if (confirm(`Send password reset email to ${this.user.name}?`)) {
        // API call to send reset password email
        console.log('Password reset email sent to:', this.user.email)
        alert(`Password reset instructions have been sent to ${this.user.email}`)
      }
    },
    
    toggleUserStatus() {
      const newStatus = this.user.status === 'active' ? 'inactive' : 'active'
      const action = newStatus === 'active' ? 'activate' : 'deactivate'
      
      if (confirm(`Are you sure you want to ${action} ${this.user.name}?`)) {
        // API call to update user status
        this.user.status = newStatus
        console.log(`User ${this.user.name} status updated to ${newStatus}`)
      }
    },
    
    sendWelcomeEmail() {
      if (confirm(`Send welcome email to ${this.user.name}?`)) {
        // API call to send welcome email
        console.log('Welcome email sent to:', this.user.email)
        alert(`Welcome email has been sent to ${this.user.email}`)
      }
    },
    
    generateAccessReport() {
      console.log('Generating access report for:', this.user.name)
      // Implement report generation logic
      alert(`Access report for ${this.user.name} is being generated...`)
    },
    
    sendEmail() {
      window.location.href = `mailto:${this.user.email}`
    },
    
    makeCall() {
      if (this.user.phone) {
        window.location.href = `tel:${this.user.phone}`
      }
    },
    
    sendSMS() {
      if (this.user.phone) {
        window.location.href = `sms:${this.user.phone}`
      }
    }
  }
}
</script>

<style scoped>
/* Custom styles for better appearance */
</style>