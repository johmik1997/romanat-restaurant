<template>
  <div class="bg-white  border border-[#E1E5E8]  rounded-xl">
    <div class="border-b border-[#E1E5E8]  px-6">
      <nav class="-mb-px flex space-x-6">
        <a 
          v-for="tab in tabs" 
          :key="tab.name"
          :href="tab.href" 
          :class="tabClasses(tab)"
        >
          {{ tab.name }}
        </a>
      </nav>
    </div>
    
    <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-[#E1E5E8] ">
        <thead class="bg-gray-50">
          <tr>
            <th 
              v-for="column in columns" 
              :key="column.key"
              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" 
              scope="col"
            >
              {{ column.label }}
            </th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-[#E1E5E8] ">
          <tr v-for="reservation in reservations" :key="reservation.id">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-[#111418] ">
              {{ reservation.guestName }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              {{ reservation.arrivalTime }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 ">
              {{ reservation.room }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">
              <span :class="statusClasses(reservation.status)">
                {{ reservation.status }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <a :href="reservation.actionLink" class="text-[#0f766e] hover:text-[#0f766e]/80">
                {{ reservation.actionText }}
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReservationTable',
  props: {
    reservations: {
      type: Array,
      required: true
    },
    activeTab: {
      type: String,
      default: 'Arrivals'
    }
  },
  data() {
    return {
      tabs: [
        { name: 'Arrivals', href: '#', isActive: true },
        { name: 'Departures', href: '#', isActive: false },
        { name: 'In-House Guests', href: '#', isActive: false }
      ],
      columns: [
        { key: 'guestName', label: 'Guest Name' },
        { key: 'arrivalTime', label: 'Est. Arrival Time' },
        { key: 'room', label: 'Room Type / Number' },
        { key: 'status', label: 'Status' },
        { key: 'actions', label: 'Actions' }
      ]
    }
  },
  methods: {
    tabClasses(tab) {
      return [
        'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm',
        tab.isActive 
          ? 'border-[#0f766e] text-[#0f766e]' 
          : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-200 dark:hover:border-gray-500'
      ]
    },
    statusClasses(status) {
      const statusMap = {
        'Checked-in': 'bg-[#4CAF50]/20 text-[#4CAF50]',
        'Pending Arrival': 'bg-[#FFA000]/20 text-[#FFA000]',
        'Cancelled': 'bg-[#D32F2F]/20 text-[#D32F2F]'
      }
      
      return `inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${statusMap[status] || 'bg-gray-100 text-gray-800'}`
    }
  }
}
</script>