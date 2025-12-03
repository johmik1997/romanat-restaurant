<template>
  <div class="mt-6 flow-root">
    <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
        <div class="overflow-hidden shadow-sm rounded-xl">
          <table class="min-w-full">
            <thead class="bg-gray-50">
              <tr>
                <th class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">
                  <input type="checkbox" v-model="selectAll" @change="toggleSelectAll" class="rounded border-gray-300" />
                </th>
                <th v-for="column in columns" :key="column.key" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">
                  {{ column.label }}
                </th>
                <th class="relative py-3.5 pl-3 pr-4 sm:pr-6">Actions</th>
              </tr>
            </thead>

            <tbody class="bg-white">
              <tr v-for="guest in guests" :key="guest.id" class="hover:bg-gray-50">
                
                <!-- Checkbox -->
                <td class="whitespace-nowrap px-3 py-4" @click.stop>
                  <input 
                    type="checkbox" 
                    v-model="selectedGuests" 
                    :value="guest.id"
                    class="rounded border-gray-300"
                  />
                </td>

                <!-- NAME -->
                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-900">
                  <div class="font-medium">
                    {{ guest.first_name }} {{ guest.last_name }}
                  </div>
                  <div class="text-xs text-gray-500">
                    ID: {{ guest.id }}
                  </div>
                </td>

                <!-- EMAIL -->
                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                  {{ guest.email }}
                </td>

                <!-- PHONE -->
                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                  {{ guest.phone || 'N/A' }}
                </td>

                <!-- ROLE -->
                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                  <span :class="roleBadgeClasses(guest.role?.name)">
                    {{ guest.role?.name || 'N/A' }}
                  </span>
                </td>

                <!-- REGISTERED BY -->
                <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                  {{ guest.registered_by || 'Self' }}
                </td>

                <!-- STATUS -->
                <td class="whitespace-nowrap px-3 py-4 text-sm">
                  <span :class="statusClasses(guest.status)">
                    {{ formatStatus(guest.status) }}
                  </span>
                </td>

                <!-- ACTIONS -->
                <td class="whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                  <div class="flex items-center justify-end gap-2">
                    <button 
                      @click="viewGuest(guest)" 
                      class="p-1.5 text-blue-500 rounded hover:bg-gray-100"
                      title="View Details"
                    >
                      <span class="material-symbols-outlined text-xl">visibility</span>
                    </button>
                    <button 
                      @click="editGuest(guest)" 
                      class="p-1.5 text-green-500 rounded hover:bg-gray-100"
                      title="Edit"
                    >
                      <span class="material-symbols-outlined text-xl">edit</span>
                    </button>
                    <button 
                      v-if="guest.role?.name !== 'Admin'"
                      @click="deleteGuest(guest)" 
                      class="p-1.5 text-red-500 rounded hover:bg-gray-100"
                      title="Delete"
                    >
                      <span class="material-symbols-outlined text-xl">delete</span>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- Empty State -->
          <div v-if="guests.length === 0" class="text-center py-12">
            <span class="material-symbols-outlined text-6xl text-gray-300 mb-4">group</span>
            <h3 class="text-lg font-medium text-gray-900 mb-2">No guests found</h3>
            <p class="text-gray-500">Try adjusting your search or filters</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GuestTable',
  props: {
    guests: {
      type: Array,
      required: true,
      default: () => []
    },
    columns: {
      type: Array,
      default: () => [
        { key: 'name', label: 'Guest Name' },
        { key: 'email', label: 'Email' },
        { key: 'phone', label: 'Phone' },
        { key: 'role', label: 'Role' },
        { key: 'registered_by', label: 'Registered By' },
        { key: 'status', label: 'Status' }
      ]
    }
  },
  data() {
    return {
      selectedGuests: [],
      selectAll: false
    }
  },
  emits: ['view-guest', 'edit-guest', 'delete-guest', 'selection-change'],
  watch: {
    selectedGuests(newVal) {
      this.$emit('selection-change', newVal)
      this.selectAll = newVal.length === this.guests.length && this.guests.length > 0
    },
    guests() {
      this.selectedGuests = []
      this.selectAll = false
    }
  },
  methods: {
    viewGuest(guest) {
      this.$emit('view-guest', guest)
    },
    
    editGuest(guest) {
      this.$emit('edit-guest', guest)
    },
    
    deleteGuest(guest) {
      this.$emit('delete-guest', guest)
    },
    
    toggleSelectAll() {
      if (this.selectAll) {
        this.selectedGuests = this.guests.map(g => g.id)
      } else {
        this.selectedGuests = []
      }
    },
    
    statusClasses(status) {
      const statusMap = {
        'Active': 'inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20',
        'active': 'inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20',
        'Inactive': 'inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10',
        'inactive': 'inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10',
        'Pending': 'inline-flex items-center rounded-md bg-yellow-50 px-2 py-1 text-xs font-medium text-yellow-700 ring-1 ring-inset ring-yellow-600/20',
        'pending': 'inline-flex items-center rounded-md bg-yellow-50 px-2 py-1 text-xs font-medium text-yellow-700 ring-1 ring-inset ring-yellow-600/20',
        'Suspended': 'inline-flex items-center rounded-md bg-red-50 px-2 py-1 text-xs font-medium text-red-700 ring-1 ring-inset ring-red-600/10',
        'suspended': 'inline-flex items-center rounded-md bg-red-50 px-2 py-1 text-xs font-medium text-red-700 ring-1 ring-inset ring-red-600/10'
      }
      return statusMap[status] || statusMap['Inactive']
    },
    
    formatStatus(status) {
      if (!status) return 'Inactive'
      return status.charAt(0).toUpperCase() + status.slice(1).toLowerCase()
    },
    
    roleBadgeClasses(role) {
      const roleMap = {
        'Admin': 'inline-flex items-center rounded-md bg-purple-50 px-2 py-1 text-xs font-medium text-purple-700',
        'Manager': 'inline-flex items-center rounded-md bg-blue-50 px-2 py-1 text-xs font-medium text-blue-700',
        'Receptionist': 'inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700',
        'Customer': 'inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-700',
        'Guest': 'inline-flex items-center rounded-md bg-yellow-50 px-2 py-1 text-xs font-medium text-yellow-700'
      }
      return roleMap[role] || 'inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-700'
    }
  }
}
</script>