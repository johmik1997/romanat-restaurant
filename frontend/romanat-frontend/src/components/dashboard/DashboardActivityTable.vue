<template>
  <div class="rounded-xl border border-gray-200 bg-white 
              shadow-sm overflow-hidden">
    
    <!-- Table Header -->
    <div class="flex items-center justify-between p-4 md:p-6 border-b border-gray-200">
      <div class="flex flex-col gap-1">
        <p class="text-gray-900 text-lg font-semibold">Recent Activity</p>
        <p class="text-gray-500 text-sm">Latest bookings and reservations</p>
      </div>
      
      <button class="flex items-center gap-2 px-4 py-2 text-sm text-primary hover:bg-primary/5 
                    rounded-lg transition-colors duration-200">
        <span>View All</span>
        <span class="material-symbols-outlined text-lg">chevron_right</span>
      </button>
    </div>

    <!-- Table -->
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead>
          <tr class="border-b border-gray-200">
            <th 
              v-for="header in tableHeaders" 
              :key="header.key"
              class="text-left p-4 text-sm font-medium text-gray-500 whitespace-nowrap"
            >
              {{ header.label }}
            </th>
          </tr>
        </thead>
        
        <tbody class="divide-y divide-gray-200">
          <tr 
            v-for="activity in activities" 
            :key="activity.id"
            class="hover:bg-gray-50 transition-colors duration-150"
          >
            <td class="p-4 text-sm text-gray-900 font-medium whitespace-nowrap">
              #{{ activity.bookingId }}
            </td>
            
            <td class="p-4 text-sm text-gray-900 whitespace-nowrap">
              {{ activity.guestName }}
            </td>
            
            <td class="p-4 text-sm text-gray-500 whitespace-nowrap">
              {{ activity.roomType }}
            </td>
            
            <td class="p-4 text-sm text-gray-500 whitespace-nowrap">
              {{ activity.checkIn }} - {{ activity.checkOut }}
            </td>
            
            <td class="p-4 whitespace-nowrap">
              <span 
                class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                :class="statusClasses[activity.status]"
              >
                {{ activity.status }}
              </span>
            </td>
            
            <td class="p-4 text-sm text-gray-900 font-semibold whitespace-nowrap">
              {{ activity.amount }}
            </td>
            
            <td class="p-4 whitespace-nowrap">
              <button class="p-1.5 text-gray-400 hover:text-gray-600 
                           rounded-lg transition-colors duration-200">
                <span class="material-symbols-outlined text-lg">more_vert</span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Table Footer -->
    <div class="flex items-center justify-between p-4 md:p-6 border-t border-gray-200">
      <p class="text-sm text-gray-500">
        Showing {{ activities.length }} of 124 bookings
      </p>
      
      <div class="flex items-center gap-2">
        <button class="p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200">
          <span class="material-symbols-outlined text-lg">chevron_left</span>
        </button>
        
        <button class="p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200">
          <span class="material-symbols-outlined text-lg">chevron_right</span>
        </button>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const tableHeaders = ref([
  { key: 'bookingId', label: 'Booking ID' },
  { key: 'guestName', label: 'Guest Name' },
  { key: 'roomType', label: 'Room Type' },
  { key: 'dates', label: 'Dates' },
  { key: 'status', label: 'Status' },
  { key: 'amount', label: 'Amount' },
  { key: 'actions', label: '' }
])

const activities = ref([
  {
    id: 1,
    bookingId: 'BK001234',
    guestName: 'John Smith',
    roomType: 'Deluxe Suite',
    checkIn: '15 Nov',
    checkOut: '18 Nov',
    status: 'Confirmed',
    amount: '$845.00'
  },
  {
    id: 2,
    bookingId: 'BK001235',
    guestName: 'Sarah Johnson',
    roomType: 'Executive Room',
    checkIn: '16 Nov',
    checkOut: '19 Nov',
    status: 'Pending',
    amount: '$625.50'
  },
  {
    id: 3,
    bookingId: 'BK001236',
    guestName: 'Michael Brown',
    roomType: 'Presidential Suite',
    checkIn: '17 Nov',
    checkOut: '20 Nov',
    status: 'Confirmed',
    amount: '$1,250.00'
  },
  {
    id: 4,
    bookingId: 'BK001237',
    guestName: 'Emily Davis',
    roomType: 'Standard Room',
    checkIn: '18 Nov',
    checkOut: '21 Nov',
    status: 'Cancelled',
    amount: '$450.00'
  },
  {
    id: 5,
    bookingId: 'BK001238',
    guestName: 'Robert Wilson',
    roomType: 'Family Suite',
    checkIn: '19 Nov',
    checkOut: '22 Nov',
    status: 'Confirmed',
    amount: '$920.00'
  }
])

const statusClasses = {
  'Confirmed': 'bg-green-100 text-green-800',
  'Pending': 'bg-yellow-100 text-yellow-800',
  'Cancelled': 'bg-red-100 text-red-800',
  'Completed': 'bg-blue-100 text-blue-800'
}
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

table {
  border-collapse: separate;
  border-spacing: 0;
}
</style>