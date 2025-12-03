<template>
  <div class="mt-12 pt-8 border-t border-gray-200">
    <h3 class="text-2xl font-serif font-bold text-gray-800 mb-6">Availability Calendar</h3>
    
    <div class="bg-white p-6 rounded-2xl shadow-lg border border-gray-100">
      <!-- Calendar Navigation -->
      <div class="flex items-center justify-between px-2 mb-6">
        <button 
          @click="previousMonth"
          class="p-3 rounded-xl hover:bg-gray-100 transition-colors duration-300 group"
        >
          <svg class="w-5 h-5 text-gray-600 group-hover:text-[#0f766e]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
          </svg>
        </button>
        
        <h4 class="font-serif text-xl font-bold text-gray-800">{{ currentMonthYear }}</h4>
        
        <button 
          @click="nextMonth"
          class="p-3 rounded-xl hover:bg-gray-100 transition-colors duration-300 group"
        >
          <svg class="w-5 h-5 text-gray-600 group-hover:text-[#0f766e]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </button>
      </div>

      <!-- Calendar Grid -->
      <div class="grid grid-cols-7 gap-2 text-center text-sm">
        <!-- Weekday Headers -->
        <div 
          v-for="day in weekdays" 
          :key="day"
          class="text-gray-500 font-semibold py-3 text-sm"
        >
          {{ day }}
        </div>

        <!-- Calendar Days -->
        <div
          v-for="day in calendarDays"
          :key="day.date"
          class="relative"
        >
          <button
            @click="selectDate(day)"
            :disabled="!day.isCurrentMonth || day.isBooked"
            class="w-full h-12 rounded-xl transition-all duration-300 flex flex-col items-center justify-center relative"
            :class="getDayClasses(day)"
          >
            <span class="text-sm font-medium">{{ day.day }}</span>
            
            <!-- Status Indicators -->
            <div v-if="day.isToday" class="absolute -top-1 -right-1 w-2 h-2 bg-accent rounded-full"></div>
            <div v-if="day.isSelected" class="absolute -top-1 -right-1 w-2 h-2 bg-[#0f766e] rounded-full"></div>
            
            <!-- Booking Status -->
            <div v-if="day.isBooked" class="absolute bottom-1 w-1 h-1 bg-red-400 rounded-full"></div>
            <div v-else-if="day.isAvailable" class="absolute bottom-1 w-1 h-1 bg-green-400 rounded-full"></div>
          </button>
        </div>
      </div>

      <!-- Legend -->
      <div class="mt-6 pt-6 border-t border-gray-200">
        <div class="flex flex-wrap gap-6 text-xs text-gray-600">
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 bg-green-400 rounded-full"></div>
            <span>Available</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 bg-red-400 rounded-full"></div>
            <span>Booked</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 bg-accent rounded-full"></div>
            <span>Today</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 bg-[#0f766e] rounded-full"></div>
            <span>Selected</span>
          </div>
        </div>
      </div>

      <!-- Selected Dates Info -->
      <div v-if="selectedDates.length > 0" class="mt-6 p-4 bg-[#0f766e]/5 rounded-xl border border-[#0f766e]/20">
        <h5 class="font-semibold text-[#0f766e] mb-2">Selected Period</h5>
        <div class="flex items-center gap-4 text-sm text-gray-700">
          <div class="flex items-center gap-2">
            <svg class="w-4 h-4 text-[#0f766e]" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"/>
            </svg>
            <span>{{ formatDate(selectedDates[0]) }}</span>
          </div>
          <span class="text-gray-400">→</span>
          <div class="flex items-center gap-2">
            <svg class="w-4 h-4 text-[#0f766e]" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"/>
            </svg>
            <span>{{ formatDate(selectedDates[1]) }}</span>
          </div>
          <div class="ml-auto">
            <span class="font-semibold text-[#0f766e]">{{ selectedDates.length }} nights</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const currentDate = ref(new Date())
const selectedDates = ref([])

const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

// Sample booked dates - in real app, this would come from an API
const bookedDates = ref([
  '2024-01-03',
  '2024-01-10',
  '2024-01-11',
  '2024-01-22',
  '2024-01-23',
  '2024-01-24'
])

const currentMonthYear = computed(() => {
  return currentDate.value.toLocaleDateString('en-US', { 
    month: 'long', 
    year: 'numeric' 
  })
})

const calendarDays = computed(() => {
  const year = currentDate.value.getFullYear()
  const month = currentDate.value.getMonth()
  
  // First day of the month
  const firstDay = new Date(year, month, 1)
  // Last day of the month
  const lastDay = new Date(year, month + 1, 0)
  // First day of the calendar (might be from previous month)
  const startDay = new Date(firstDay)
  startDay.setDate(startDay.getDate() - startDay.getDay())
  
  const days = []
  const today = new Date()
  today.setHours(0, 0, 0, 0)

  // Generate 42 days (6 weeks) to cover the calendar
  for (let i = 0; i < 42; i++) {
    const date = new Date(startDay)
    date.setDate(startDay.getDate() + i)
    
    const dateString = date.toISOString().split('T')[0]
    const isCurrentMonth = date.getMonth() === month
    const isToday = date.toDateString() === today.toDateString()
    const isBooked = bookedDates.value.includes(dateString)
    const isAvailable = isCurrentMonth && !isBooked && date >= today
    const isSelected = selectedDates.value.some(selectedDate => 
      selectedDate.toDateString() === date.toDateString()
    )

    days.push({
      date: dateString,
      day: date.getDate(),
      isCurrentMonth,
      isToday,
      isBooked,
      isAvailable,
      isSelected,
      dateObj: new Date(date)
    })
  }

  return days
})

const getDayClasses = (day) => {
  const classes = []
  
  if (!day.isCurrentMonth) {
    classes.push('text-gray-300 cursor-not-allowed')
  } else if (day.isBooked) {
    classes.push('bg-red-50 text-red-400 cursor-not-allowed hover:bg-red-100')
  } else if (day.isSelected) {
    classes.push('bg-[#0f766e] text-white hover:bg-teal-600')
  } else if (day.isToday) {
    classes.push('bg-accent/20 text-gray-800 hover:bg-accent/30')
  } else if (day.isAvailable) {
    classes.push('bg-white text-gray-700 hover:bg-gray-50 border border-gray-200')
  } else {
    classes.push('bg-gray-100 text-gray-400 cursor-not-allowed')
  }

  return classes
}

const previousMonth = () => {
  currentDate.value = new Date(
    currentDate.value.getFullYear(),
    currentDate.value.getMonth() - 1,
    1
  )
}

const nextMonth = () => {
  currentDate.value = new Date(
    currentDate.value.getFullYear(),
    currentDate.value.getMonth() + 1,
    1
  )
}

const selectDate = (day) => {
  if (!day.isAvailable || !day.isCurrentMonth) return

  if (selectedDates.value.length === 0) {
    // First date selection
    selectedDates.value = [day.dateObj]
  } else if (selectedDates.value.length === 1) {
    // Second date selection - create range
    const firstDate = selectedDates.value[0]
    if (day.dateObj > firstDate) {
      selectedDates.value = [firstDate, day.dateObj]
    } else {
      selectedDates.value = [day.dateObj, firstDate]
    }
  } else {
    // Reset selection
    selectedDates.value = [day.dateObj]
  }
}

const formatDate = (date) => {
  return date.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric'
  })
}

// Initialize with current month
onMounted(() => {
  currentDate.value = new Date()
})
</script>

<style scoped>
/* Custom styles for better calendar appearance */
button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

button:not(:disabled):hover {
  transform: scale(1.05);
}
</style>