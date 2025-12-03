<template>
  <div class="p-8">
    <PageHeader 
      title="Guest Management"
      subtitle="View, search, and manage all guest information."
      action-text="Add New Guest"
      @add-guest="openAddModal"
    />

    <!-- Search + Filters -->
    <div class="mt-8 flex flex-col gap-4">
      <SearchBar 
        placeholder="Search by name, email, or phone..."
        @search="handleSearch"
      />
      
      <!-- Status Filter Tabs -->
      <div class="border-b border-gray-200">
        <nav class="-mb-px flex space-x-8">
          <button
            v-for="tab in tabs"
            :key="tab.key"
            @click="setActiveTab(tab)"
            :class="tabClasses(tab)"
          >
            {{ tab.name }}
            <span
              v-if="tab.count !== undefined"
              class="ml-2 bg-gray-200 text-gray-600 text-xs px-2 py-1 rounded-full"
            >
              {{ tab.count }}
            </span>
          </button>
        </nav>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="flex flex-wrap gap-3 my-4">
      <button 
        @click="handleExport"
        class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
      >
        Export Selected
      </button>
      <button 
        @click="bulkActivate"
        class="px-4 py-2 text-sm font-medium text-green-700 bg-green-50 border border-green-200 rounded-lg hover:bg-green-100 transition-colors"
      >
        Activate Selected
      </button>
      <button 
        @click="bulkDeactivate"
        class="px-4 py-2 text-sm font-medium text-red-700 bg-red-50 border border-red-200 rounded-lg hover:bg-red-100 transition-colors"
      >
        Deactivate Selected
      </button>
    </div>

    <!-- Guest Table -->
    <GuestTable 
      :guests="paginatedGuests"
      @view-guest="handleViewGuest"
      @edit-guest="handleEditGuest"
      @delete-guest="handleDeleteGuest"
      @selection-change="handleSelectionChange"
    />
    


    <!-- Pagination -->
    <div v-if="totalCount > 0" class="px-6 py-4 border border-gray-200 rounded-2xl bg-white shadow-sm">
      <div class="flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="text-sm text-gray-700">
          Showing 
          <span class="font-medium">{{ paginationStart }}</span> 
          to 
          <span class="font-medium">{{ paginationEnd }}</span> 
          of 
          <span class="font-medium">{{ totalCount }}</span> guests
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

    <!-- Add/Edit Guest Modal -->
    <AddEditGuestModal
      :show="showGuestModal"
      :guest="selectedGuest"
      @close="closeGuestModal"
      @save="handleSaveGuest"
    />
      <UserDetailsModal
      :isOpen="showViewModal"
      :user="selectedGuest"
      @close="showViewModal = false"
      @edit="editUserFromView"
    />
  </div>
</template>

<script>
import PageHeader from '../components/staffs/PageHeader.vue'
import SearchBar from '../components/staffs/SearchBar.vue'
import GuestTable from '../components/staffs/GuestTable.vue'
import AddEditGuestModal from '../components/modal/AddEditGuestModal.vue'
import UserDetailsModal from '../components/modal/UserDetailModal.vue'

import { 
  fetchCustomers, 
  createCustomer, 
  updateCustomer, 
  deleteCustomer,
  updateCustomerStatus 
} from '../api/auth/loginApi'

export default {
  name: 'GuestManagement',

  components: {
    PageHeader,
    SearchBar,
    GuestTable,
    AddEditGuestModal,
    UserDetailsModal
  },

  data() {
    return {
      showGuestModal: false,
      activeTab: 'all',
      currentPage: 1,
      itemsPerPage: 10,
      totalCount: 0,
      searchQuery: '',
      showViewModal:false,
      selectedGuest: null,
      selectedGuests: [],
      customers: [],
      tabs: [
        { name: 'All', key: 'all' },
        { name: 'Active', key: 'active' },
        { name: 'Inactive', key: 'inactive' },
        { name: 'Pending', key: 'pending' },
        { name: 'VIP', key: 'vip' }
      ],
      loading: false
    }
  },

  computed: {
    filteredGuests() {
      let guests = this.customers

      // Filter by role (only show Customer role guests)
      guests = guests.filter(c => c.role?.name === "Customer")

      // Search filter
      if (this.searchQuery) {
        const q = this.searchQuery.toLowerCase()
        guests = guests.filter(g =>
          (g.first_name?.toLowerCase().includes(q)) ||
          (g.last_name?.toLowerCase().includes(q)) ||
          (g.email?.toLowerCase().includes(q)) ||
          (g.phone?.includes(q)) ||
          (g.username?.toLowerCase().includes(q))
        )
      }

      // Status filter
      if (this.activeTab !== 'all') {
        guests = guests.filter(g => {
          const status = g.status?.toLowerCase() || ''
          if (this.activeTab === 'vip') return g.is_vip
          return status === this.activeTab
        })
      }

      return guests
    },

    // Pagination
    paginatedGuests() {
      const start = (this.currentPage - 1) * this.itemsPerPage
      const end = start + this.itemsPerPage
      return this.filteredGuests.slice(start, end)
    },

    totalPages() {
      return Math.ceil(this.filteredGuests.length / this.itemsPerPage)
    },

    paginationStart() {
      return this.filteredGuests.length === 0 ? 0 : (this.currentPage - 1) * this.itemsPerPage + 1
    },

    paginationEnd() {
      return Math.min(this.currentPage * this.itemsPerPage, this.filteredGuests.length)
    },

    visiblePages() {
      const pages = []
      const maxVisible = 5
      let start = Math.max(1, this.currentPage - Math.floor(maxVisible / 2))
      let end = Math.min(this.totalPages, start + maxVisible - 1)
      
      if (end - start + 1 < maxVisible) {
        start = Math.max(1, end - maxVisible + 1)
      }
      
      for (let i = start; i <= end; i++) {
        pages.push(i)
      }
      return pages
    },

    showEllipsis() {
      return this.totalPages > this.visiblePages.length && 
             this.visiblePages[this.visiblePages.length - 1] < this.totalPages
    }
  },

  async mounted() {
    await this.loadCustomers()
  },

  methods: {
    async loadCustomers() {
      this.loading = true
      try {
        const params = {
          page: this.currentPage,
          page_size: this.itemsPerPage,
          search: this.searchQuery,
          role: 'Customer',
          status: this.activeTab !== 'all' ? this.activeTab : ''
        }

        const response = await fetchCustomers(params)
        
        // Handle API response format
        if (response && response.result !== undefined) {
          this.customers = response.result || []
          this.totalCount = response.count || 0
        } else if (response && Array.isArray(response.results)) {
          this.customers = response.results
          this.totalCount = response.count || 0
        } else if (Array.isArray(response)) {
          this.customers = response
          this.totalCount = response.length
        } else {
          console.warn('Unexpected API response format:', response)
          this.customers = []
          this.totalCount = 0
        }

        // Update tab counts
        this.updateTabCounts()
      } catch (err) {
        console.error('Error loading customers:', err)
        this.customers = []
        this.totalCount = 0
      } finally {
        this.loading = false
      }
    },

    updateTabCounts() {
      const allGuests = this.customers.filter(c => c.role?.name === "Customer")
      
      this.tabs = this.tabs.map(tab => {
        let count = 0
        switch(tab.key) {
          case 'all':
            count = allGuests.length
            break
          case 'active':
            count = allGuests.filter(g => g.status?.toLowerCase() === 'active').length
            break
          case 'inactive':
            count = allGuests.filter(g => g.status?.toLowerCase() === 'inactive').length
            break
          case 'pending':
            count = allGuests.filter(g => g.status?.toLowerCase() === 'pending').length
            break
          case 'vip':
            count = allGuests.filter(g => g.is_vip).length
            break
        }
        return { ...tab, count }
      })
    },

    setActiveTab(tab) {
      this.activeTab = tab.key
      this.currentPage = 1
      this.loadCustomers()
    },

    tabClasses(tab) {
      return [
        'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm flex items-center transition-colors duration-200',
        this.activeTab === tab.key 
          ? 'border-primary text-primary' 
          : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
      ]
    },

    handleSearch(query) {
      this.searchQuery = query
      this.currentPage = 1
      this.loadCustomers()
    },

    openAddModal() {
      this.selectedGuest = null
      this.showGuestModal = true
    },

    handleViewGuest(guest) {
      this.selectedGuest = guest
      this.showViewModal = true
    },

    handleEditGuest(guest) {
      console.log('Editing guest:', guest)
      this.selectedGuest = guest
      this.showGuestModal = true
    },

    async handleDeleteGuest(guest) {
      if (confirm(`Are you sure you want to delete guest "${guest.first_name} ${guest.last_name}"? This action cannot be undone.`)) {
        try {
          await deleteCustomer(guest.id)
          await this.loadCustomers()
          alert('Guest deleted successfully!')
        } catch (error) {
          console.error('Error deleting guest:', error)
          alert('Failed to delete guest. Please try again.')
        }
      }
    },

    closeGuestModal() {
      this.showGuestModal = false
      this.selectedGuest = null
    },

    async handleSaveGuest(guestData) {
      try {
        if (this.selectedGuest) {
          // Update existing guest
          await updateCustomer(this.selectedGuest.id, guestData)
          alert('Guest updated successfully!')
        } else {
          // Create new guest
          await createCustomer(guestData)
          alert('Guest created successfully!')
        }

        // Reload guests
        await this.fetchCustomers()
        this.closeGuestModal()
      } catch (error) {
        console.error('Error saving guest:', error)
        alert(`Failed to ${this.selectedGuest ? 'update' : 'create'} guest. Please try again.`)
      }
    },

    handleSelectionChange(selectedIds) {
      this.selectedGuests = selectedIds
    },

    async bulkActivate() {
      if (!this.selectedGuests.length) {
        alert('Please select guests to activate.')
        return
      }

      try {
        for (const id of this.selectedGuests) {
          await updateCustomerStatus(id, 'active')
        }
        
        await this.loadCustomers()
        const count = this.selectedGuests.length
        this.selectedGuests = []
        alert(`${count} guests activated successfully!`)
      } catch (error) {
        console.error('Error activating guests:', error)
        alert('Failed to activate guests. Please try again.')
      }
    },

    async bulkDeactivate() {
      if (!this.selectedGuests.length) {
        alert('Please select guests to deactivate.')
        return
      }

      try {
        for (const id of this.selectedGuests) {
          await updateCustomerStatus(id, 'inactive')
        }
        
        await this.loadCustomers()
        const count = this.selectedGuests.length
        this.selectedGuests = []
        alert(`${count} guests deactivated successfully!`)
      } catch (error) {
        console.error('Error deactivating guests:', error)
        alert('Failed to deactivate guests. Please try again.')
      }
    },

    handleExport() {
      const dataToExport = this.selectedGuests.length 
        ? this.customers.filter(g => this.selectedGuests.includes(g.id))
        : this.customers

      if (!dataToExport.length) {
        alert('No guests to export.')
        return
      }

      // Convert to CSV
      const headers = ['ID', 'Name', 'Email', 'Phone', 'Role', 'Status', 'Registered Date']
      const rows = dataToExport.map(g => [
        g.id,
        `${g.first_name} ${g.last_name}`,
        g.email,
        g.phone || 'N/A',
        g.role?.name || 'N/A',
        g.status || 'N/A',
        g.date_joined ? new Date(g.date_joined).toLocaleDateString() : 'N/A'
      ])

      const csvContent = [headers, ...rows].map(e => e.join(',')).join('\n')

      // Create downloadable file
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' })
      const link = document.createElement('a')
      link.href = URL.createObjectURL(blob)
      link.setAttribute('download', `guests_${new Date().toISOString().split('T')[0]}.csv`)
      link.click()
    },

    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--
        this.loadCustomers()
      }
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
        this.loadCustomers()
      }
    },

    goToPage(page) {
      if (page !== this.currentPage) {
        this.currentPage = page
        this.loadCustomers()
      }
    }
  }
}
</script>