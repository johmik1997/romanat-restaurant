<template>
  <div class="min-h-screen bg-gray-50 p-6 overflow-x-auto">
    <!-- Header -->
    <div class="mb-8">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">User Management</h1>
          <p class="text-gray-600 mt-2">Manage system users and their permissions</p>
        </div>
        <button 
          @click="showCreateModal = true"
          class="bg-[#0f766e] text-white px-6 py-3 rounded-xl hover:bg-[#0f766e]/90 transition-colors flex items-center gap-2 shadow-lg hover:shadow-xl"
        >
          <span class="material-symbols-outlined">person_add</span>
          Add New User
        </button>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
      <div class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm">
        <div class="flex items-center gap-4">
          <div class="p-3 bg-blue-100 rounded-xl">
            <span class="material-symbols-outlined text-blue-600 text-2xl">group</span>
          </div>
          <div>
            <p class="text-2xl font-bold text-gray-900">{{ userStats.totalUsers }}</p>
            <p class="text-gray-600">Total Users</p>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm">
        <div class="flex items-center gap-4">
          <div class="p-3 bg-green-100 rounded-xl">
            <span class="material-symbols-outlined text-green-600 text-2xl">admin_panel_settings</span>
          </div>
          <div>
            <p class="text-2xl font-bold text-gray-900">{{ userStats.adminUsers }}</p>
            <p class="text-gray-600">Administrators</p>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm">
        <div class="flex items-center gap-4">
          <div class="p-3 bg-purple-100 rounded-xl">
            <span class="material-symbols-outlined text-purple-600 text-2xl">support_agent</span>
          </div>
          <div>
            <p class="text-2xl font-bold text-gray-900">{{ userStats.staffUsers }}</p>
            <p class="text-gray-600">Staff Members</p>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm">
        <div class="flex items-center gap-4">
          <div class="p-3 bg-orange-100 rounded-xl">
            <span class="material-symbols-outlined text-orange-600 text-2xl">lock</span>
          </div>
          <div>
            <p class="text-2xl font-bold text-gray-900">{{ userStats.inactiveUsers }}</p>
            <p class="text-gray-600">Inactive Users</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Filters and Search -->
    <div class="bg-white rounded-2xl p-6 border border-gray-200 shadow-sm mb-6">
      <div class="flex flex-col lg:flex-row gap-4 items-center justify-between">
        <div class="flex flex-col sm:flex-row gap-4 w-full lg:w-auto">
          <!-- Search -->
          <div class="relative flex-1">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search users by name, email, or role..."
              class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent"
              @input="debouncedSearch"
            >
            <span class="material-symbols-outlined absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400">
              search
            </span>
          </div>

          <!-- Role Filter -->
          <select
            v-model="filters.role"
            class="px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent text-black"
            @change="loadUsers"
          >
            <option value="all">All Roles</option>
            <option value="admin">Administrator</option>
            <option value="manager">Manager</option>
            <option value="receptionist">Receptionist</option>
            <option value="housekeeping">Housekeeping</option>
          </select>

          <!-- Status Filter -->
          <select
            v-model="filters.status"
            class="px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#0f766e]/50 focus:border-transparent text-black"
            @change="loadUsers"
          >
            <option value="all">All Status</option>
            <option value="active">Active</option>
            <option value="inactive">Inactive</option>
          </select>
        </div>

        <div class="flex gap-3 w-full lg:w-auto">
          <button 
            @click="resetFilters"
            class="px-4 py-3 border border-gray-300 rounded-xl hover:bg-gray-50 transition-colors flex items-center gap-2"
          >
            <span class="material-symbols-outlined">refresh</span>
            Reset
          </button>
          <button 
            @click="exportUsers"
            class="px-4 py-3 bg-green-600 text-white rounded-xl hover:bg-green-700 transition-colors flex items-center gap-2"
          >
            <span class="material-symbols-outlined">download</span>
            Export
          </button>
        </div>
      </div>
    </div>

    <!-- Users Table -->
    <div class="bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden mb-6">
      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                User
              </th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Role
              </th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Phone Number
              </th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Address
              </th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Registered By
              </th>
              <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr 
              v-for="user in users" 
              :key="user.id"
              class="hover:bg-gray-50 transition-colors"
            >
              <!-- User Info -->
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <!-- <div class="shrink-0 h-10 w-10">
                    <img 
                      class="h-10 w-10 rounded-full object-cover" 
                      :src="user.avatar || '/api/placeholder/40/40'" 
                      :alt="user.first_name"
                    >
                  </div> -->
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900">
                      {{ user.first_name + " " +user.last_name }}
                    </div>
                    <div class="text-sm text-gray-500">
                      {{ user.email }}
                    </div>
                  </div>
                </div>
              </td>

              <!-- Role -->
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center gap-2">
                  <span :class="roleIconClasses(user.role)" class="material-symbols-outlined text-lg">
                    {{ roleIcon(user.role?.name) }}
                  </span>
                  <div>
                    <span :class="roleBadgeClasses(user.role)" class="text-xs">
                      {{ formatRole(user.role?.name) }}
                    </span>
                    <div class="text-xs text-gray-500 mt-1">
                      {{ user.permissions?.length || 0 }} permissions
                    </div>
                  </div>
                </div>
              </td>

              <!-- Department -->
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ user?.phone || 'Not assigned' }}
              </td>

              <!-- Status -->
              <td class="px-6 py-4 whitespace-nowrap">
                <span :class="statusBadgeClasses(user?.status)" class="text-xs">
                  {{ user.status === 'Active' ? 'Active' : 'Inactive' }}
                </span>
              </td>

              <!-- Last Login -->
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ user.address }}
              </td>

              <!-- Created Date -->
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                {{ (user.registered_by) }}
              </td>

              <!-- Actions -->
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex items-center justify-end gap-2">
                  <button 
                    @click="viewUser(user)"
                    class="text-blue-600 hover:text-blue-900 p-2 rounded-lg hover:bg-blue-50 transition-colors"
                    title="View Details"
                  >
                    <span class="material-symbols-outlined text-xl">visibility</span>
                  </button>
                  <button 
                    @click="editUser(user)"
                    class="text-green-600 hover:text-green-900 p-2 rounded-lg hover:bg-green-50 transition-colors"
                    title="Edit User"
                  >
                    <span class="material-symbols-outlined text-xl">edit</span>
                  </button>
                  <!-- <button 
                    v-if="user.id !== currentUserId"
                    @click="toggleUserStatus(user)"
                    :class="[
                      'p-2 rounded-lg transition-colors',
                      user.status === 'Active' 
                        ? 'text-orange-600 hover:text-orange-900 hover:bg-orange-50' 
                        : 'text-green-600 hover:text-green-900 hover:bg-green-50'
                    ]"
                    :title="user.status === 'active' ? 'Deactivate User' : 'Activate User'"
                  >
                    <span class="material-symbols-outlined text-xl">
                      {{ user.status === 'active' ? 'lock' : 'lock_open' }}
                    </span>
                  </button> -->
                  <button 
                    v-if="user.id !== currentUserId"
                    @click="deleteUser(user)"
                    class="text-red-600 hover:text-red-900 p-2 rounded-lg hover:bg-red-50 transition-colors"
                    title="Delete User"
                  >
                    <span class="material-symbols-outlined text-xl">delete</span>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Empty State -->
      <div v-if="users.length === 0" class="text-center py-12">
        <span class="material-symbols-outlined text-6xl text-gray-300 mb-4">group</span>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No users found</h3>
        <p class="text-gray-500 mb-4">Try adjusting your search or filters</p>
        <button 
          @click="showCreateModal = true"
          class="bg-[#0f766e] text-white px-4 py-2 rounded-lg hover:bg-[#0f766e]/90 transition-colors flex items-center gap-2 mx-auto"
        >
          <span class="material-symbols-outlined">person_add</span>
          Add New User
        </button>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="totalCount > 0" class="px-6 py-4 border border-gray-200 rounded-2xl bg-white shadow-sm">
      <div class="flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="text-sm text-gray-700">
          Showing 
          <span class="font-medium">{{ paginationStart }}</span> 
          to 
          <span class="font-medium">{{ paginationEnd }}</span> 
          of 
          <span class="font-medium">{{ totalCount }}</span> users
        </div>
        
        <div class="flex items-center gap-2">
          <button 
            @click="previousPage"
            :disabled="currentPage === 1"
            :class="[
              'px-4 py-2 border border-gray-300 rounded-lg font-medium transition-colors',
              currentPage === 1 
                ? 'bg-gray-50 text-gray-400 cursor-not-allowed' 
                : 'bg-white text-gray-700 hover:bg-gray-50 hover:border-gray-400'
            ]"
          >
            Previous
          </button>
          
          <div class="flex items-center gap-1">
            <button 
              v-for="page in visiblePages" 
              :key="page"
              @click="goToPage(page)"
              :class="[
                'w-10 h-10 flex items-center justify-center rounded-lg font-medium transition-colors',
                currentPage === page 
                  ? 'bg-[#0f766e] text-white' 
                  : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
              ]"
            >
              {{ page }}
            </button>
            <span v-if="showEllipsis" class="px-2 text-gray-500">...</span>
          </div>
          
          <button 
            @click="nextPage"
            :disabled="currentPage >= totalPages"
            :class="[
              'px-4 py-2 border border-gray-300 rounded-lg font-medium transition-colors',
              currentPage >= totalPages 
                ? 'bg-gray-50 text-gray-400 cursor-not-allowed' 
                : 'bg-white text-gray-700 hover:bg-gray-50 hover:border-gray-400'
            ]"
          >
            Next
          </button>
        </div>
      </div>
    </div>

    <!-- Modals -->
    <UserModal
      :isOpen="showCreateModal || showEditModal"
      :user="selectedUser"
      :mode="showEditModal ? 'edit' : 'create'"
      @close="closeModal"
      @save="handleSaveUser"
    />

    <UserDetailsModal
      :isOpen="showViewModal"
      :user="selectedUser"
      @close="showViewModal = false"
      @edit="editUserFromView"
    />

    <div v-if="showDeleteModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div class="bg-white rounded-2xl max-w-md w-full mx-4 p-6 shadow-2xl">
        <div class="flex items-center gap-3 mb-4">
          <span class="material-symbols-outlined text-red-600 text-3xl">warning</span>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Delete User</h3>
            <p class="text-gray-600">This action cannot be undone</p>
          </div>
        </div>
        
        <p class="text-gray-700 mb-6">
          Are you sure you want to delete user <strong>{{ selectedUser?.name }}</strong>? 
          This will permanently remove their account and all associated data.
        </p>
        <div class="flex gap-3">
          <button 
            @click="showDeleteModal = false"
            class="flex-1 bg-gray-100 text-gray-700 py-3 rounded-xl hover:bg-gray-200 transition-colors font-medium"
          >
            Cancel
          </button>
          <button 
            @click="confirmDelete"
            class="flex-1 bg-red-600 text-white py-3 rounded-xl hover:bg-red-700 transition-colors font-medium"
          >
            Delete User
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UserModal from '../components/modal/UserModal.vue'
import UserDetailsModal from '../components/modal/UserDetailModal.vue'
import { createUser, getUsers } from '../api/auth/userApi';

export default {
  name: 'UserManagement',
  components: {
    UserModal,
    UserDetailsModal
  },
  data() {
    return {
      users: [],
      totalCount: 0,
      searchQuery: '',
      filters: {
        role: 'all',
        status: 'all'
      },
      currentPage: 1,
      itemsPerPage: 10,
      showCreateModal: false,
      showEditModal: false,
      showViewModal: false,
      showDeleteModal: false,
      selectedUser: null,
      currentUserId: 'current-user-id',
      searchTimeout: null
    }
  },
  computed: {
    userStats() {
      const totalUsers = this.totalCount
      const adminUsers = this.users.filter(u => u.role?.name === 'SuperAdmin').length
      const staffUsers = this.users.filter(u => ['Manager', 'Receptionist'].includes(u.role?.name)).length
      const inactiveUsers = this.users.filter(u => u.status === 'inactive').length

      return {
        totalUsers,
        adminUsers,
        staffUsers,
        inactiveUsers
      }
    },
    
    totalPages() {
      return Math.ceil(this.totalCount / this.itemsPerPage)
    },

    paginationStart() {
      return this.totalCount === 0 ? 0 : (this.currentPage - 1) * this.itemsPerPage + 1
    },

    paginationEnd() {
      return Math.min(this.currentPage * this.itemsPerPage, this.totalCount)
    },

    visiblePages() {
      if (this.totalPages <= 1) return []
      
      const pages = []
      const maxVisible = 5
      let start = Math.max(1, this.currentPage - Math.floor(maxVisible / 2))
      let end = Math.min(this.totalPages, start + maxVisible - 1)
      
      // Adjust start if we're near the end
      start = Math.max(1, end - maxVisible + 1)
      
      for (let i = start; i <= end; i++) {
        pages.push(i)
      }
      return pages
    },

    showEllipsis() {
      return this.totalPages > 5 && this.currentPage < this.totalPages - 2
    }
  },
  async mounted() {
    await this.loadUsers()
  },
  methods: {
    debouncedSearch() {
      // Clear existing timeout
      if (this.searchTimeout) {
        clearTimeout(this.searchTimeout)
      }
      
      // Set new timeout
      this.searchTimeout = setTimeout(() => {
        this.currentPage = 1
        this.loadUsers()
      }, 500) // 500ms delay
    },

    async loadUsers() {
      try {
        // Build query params for backend
        const params = {
          page: this.currentPage,
          page_size: this.itemsPerPage
        }

        // Add search query if exists
        if (this.searchQuery.trim()) {
          params.search = this.searchQuery.trim()
        }

        // Add role filter if not 'all'
        if (this.filters.role !== 'all') {
          params.role = this.filters.role
        }

        // Add status filter if not 'all'
        if (this.filters.status !== 'all') {
          params.status = this.filters.status
        }

        // Call API with params
        const response = await getUsers(params)
        
        // Update data
        this.users = response.results || response.result || []
        this.totalCount = response.count || 0
        
      } catch (error) {
        console.error('Error loading users:', error)
        this.users = []
        this.totalCount = 0
      }
    },

    formatRole(role) {
      const roleMap = {
        'admin': 'Administrator',
        'manager': 'Manager',
        'receptionist': 'Receptionist',
        'housekeeping': 'Housekeeping',
        'SuperAdmin': 'Super Administrator'
      }
      return roleMap[role] || role
    },

    roleIcon(role) {
      const icons = {
        'admin': 'admin_panel_settings',
        'manager': 'manage_accounts',
        'receptionist': 'support_agent',
        'housekeeping': 'cleaning_services',
        'SuperAdmin': 'admin_panel_settings'
      }
      return icons[role] || 'person'
    },

    roleIconClasses(role) {
      const classes = {
        'admin': 'text-red-600',
        'manager': 'text-blue-600',
        'receptionist': 'text-green-600',
        'housekeeping': 'text-purple-600',
        'SuperAdmin': 'text-red-600'
      }
      return classes[role] || 'text-gray-600'
    },

    roleBadgeClasses(role) {
      const classes = {
        'admin': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800',
        'manager': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800',
        'receptionist': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800',
        'housekeeping': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800',
        'SuperAdmin': 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800'
      }
      return classes[role] || 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800'
    },

    statusBadgeClasses(status) {
      return status === 'Active' 
        ? 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800'
        : 'inline-flex px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800'
    },

    formatDate(dateString) {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    },

    viewUser(user) {
      this.selectedUser = user
      this.showViewModal = true
    },

    editUser(user) {
      this.selectedUser = { ...user }
      this.showEditModal = true
    },

    editUserFromView(user) {
      this.showViewModal = false
      this.selectedUser = { ...user }
      this.showEditModal = true
    },

    toggleUserStatus(user) {
      const newStatus = user.status === 'Active' ? 'inactive' : 'active'
      if (confirm(`Are you sure you want to ${newStatus === 'active' ? 'activate' : 'deactivate'} ${user.name}?`)) {
        // API call to update user status
        user.status = newStatus
        console.log(`User ${user.name} status updated to ${newStatus}`)
      }
    },

    deleteUser(user) {
      this.selectedUser = user
      this.showDeleteModal = true
    },

    async confirmDelete() {
      try {
        // API call to delete user
        // await deleteUser(this.selectedUser.id)
        this.users = this.users.filter(u => u.id !== this.selectedUser.id)
        this.showDeleteModal = false
        this.selectedUser = null
        console.log('User deleted successfully')
      } catch (error) {
        console.error('Error deleting user:', error)
      }
    },

    closeModal() {
      this.showCreateModal = false
      this.showEditModal = false
      this.selectedUser = null
    },

    async handleSaveUser(userData) {
      if (this.showEditModal) {
        // Update existing user
        const index = this.users.findIndex(u => u.id === userData.id);
        if (index !== -1) {
          this.users[index] = { ...this.users[index], ...userData };
        }
      } else {
        // Create new user
        try {
          const response = await createUser(userData);

          // Depending on your backend:
          this.users.unshift(response.result || response.data || userData);

        } catch (error) {
          console.error("Error creating user:", error);
        }
      }

      this.closeModal();
      // Refresh the list after saving
      this.loadUsers()
    },

    resetFilters() {
      this.searchQuery = ''
      this.filters = {
        role: 'all',
        status: 'all'
      }
      this.currentPage = 1
      this.loadUsers()
    },

    exportUsers() {
      console.log('Exporting users...')
    },

    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--
        this.loadUsers()
      }
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
        this.loadUsers()
      }
    },

    goToPage(page) {
      if (page !== this.currentPage) {
        this.currentPage = page
        this.loadUsers()
      }
    }
  }
}
</script>

<style scoped>
</style>