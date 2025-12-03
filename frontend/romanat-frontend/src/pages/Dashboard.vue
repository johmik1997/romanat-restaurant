<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <!-- Header -->
    <div class="mb-8">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">Receptionist Dashboard</h1>
          <p class="text-gray-600 mt-2">Today's overview of guests and room status</p>
          <div class="flex items-center gap-2 mt-2 text-sm text-gray-500">
            <span class="material-symbols-outlined text-lg">calendar_today</span>
            <span>{{ currentDate }}</span>
            <span class="mx-2">•</span>
            <span class="material-symbols-outlined text-lg">schedule</span>
            <span>{{ currentTime }}</span>
          </div>
        </div>
        <div class="flex items-center gap-4">
          <!-- Quick Stats -->
          <div v-if="userInfo" class="hidden md:flex items-center gap-6 text-sm">
            <div class="text-right">
              <p class="text-gray-600">Shift</p>
              <p class="font-semibold text-gray-900">{{ userInfo.shift || 'Not assigned' }}</p>
            </div>
            <div class="text-right">
              <p class="text-gray-600">Receptionist</p>
              <p class="font-semibold text-gray-900">{{ userInfo.name }}</p>
            </div>
          </div>
          <button class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded-lg transition-colors">
            <span class="material-symbols-outlined">notifications</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto"></div>
      <p class="mt-4 text-gray-600">Loading dashboard data...</p>
    </div>

    <!-- Main Grid Layout -->
    <div v-else class="grid grid-cols-1 xl:grid-cols-4 gap-6">
      <!-- Left Column - Metrics & Quick Actions -->
      <div class="xl:col-span-3 space-y-6">
        <!-- Metric Cards Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <MetricCard 
            label="Expected Arrivals" 
            :value="dashboardData.metrics.expected_arrivals"
            icon="flight_land"
            :trend="dashboardData.metrics.arrival_trend"
            :trendValue="dashboardData.metrics.arrival_trend_value"
            color="blue"
          />
          <MetricCard 
            label="Expected Departures" 
            :value="dashboardData.metrics.expected_departures"
            icon="flight_takeoff"
            :trend="dashboardData.metrics.departure_trend"
            :trendValue="dashboardData.metrics.departure_trend_value"
            color="green"
          />
          <MetricCard 
            label="Rooms Occupied" 
            :value="dashboardData.metrics.rooms_occupied"
            :total="dashboardData.metrics.total_rooms"
            icon="hotel"
            :trend="dashboardData.metrics.occupancy_trend"
            color="purple"
          />
          <MetricCard 
            label="Rooms Available" 
            :value="dashboardData.metrics.rooms_available"
            icon="meeting_room"
            :trend="dashboardData.metrics.availability_trend"
            :trendValue="dashboardData.metrics.availability_trend_value"
            color="teal"
          />
          <MetricCard 
            label="In-House Guests" 
            :value="dashboardData.metrics.in_house_guests"
            icon="group"
            :trend="dashboardData.metrics.guest_trend"
            :trendValue="dashboardData.metrics.guest_trend_value"
            color="orange"
          />
          <MetricCard 
            label="Pending Check-ins" 
            :value="dashboardData.metrics.expected_arrivals" 
            icon="pending"
            :trend="dashboardData.metrics.pending_trend"
            :trendValue="dashboardData.metrics.pending_trend_value"
            color="red"
          />
          <MetricCard 
            label="VIP Guests" 
            :value="0"
            icon="star"
            trend="stable"
            color="yellow"
          />
          <MetricCard 
            label="Revenue Today" 
            :value="`$${dashboardData.metrics.revenue_today}`"
            icon="attach_money"
            :trend="dashboardData.metrics.revenue_trend"
            :trendValue="dashboardData.metrics.revenue_trend_value"
            color="emerald"
          />
        </div>

        <!-- Quick Actions Bar -->
        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h3>
          <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            <ActionButton 
              label="New Reservation" 
              icon="add" 
              variant="primary" 
              @click="handleNewReservation"
              class="h-20"
            />
            <ActionButton 
              label="Check-in" 
              icon="login" 
              variant="secondary" 
              @click="handleCheckIn"
              class="h-20"
            />
            <ActionButton 
              label="Check-out" 
              icon="logout" 
              variant="secondary" 
              @click="handleCheckOut"
              class="h-20"
            />
            <ActionButton 
              label="Calendar" 
              icon="event" 
              variant="secondary" 
              @click="handleViewCalendar"
              class="h-20"
            />
            <ActionButton 
              label="Room Status" 
              icon="bed" 
              variant="secondary" 
              @click="handleRoomStatus"
              class="h-20"
            />
            <ActionButton 
              label="Guest Search" 
              icon="search" 
              variant="secondary" 
              @click="handleGuestSearch"
              class="h-20"
            />
          </div>
        </div>

        <!-- Today's Reservations Section -->
        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
          <div class="border-b border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <h3 class="text-lg font-semibold text-gray-900">Today's Reservations</h3>
                <p class="text-gray-600 mt-1">Arrivals, departures, and in-house guests</p>
              </div>
              <div class="flex items-center gap-3">
                <div class="relative">
                  <input
                    v-model="searchQuery"
                    type="text"
                    placeholder="Search reservations..."
                    class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-transparent"
                  >
                  <span class="material-symbols-outlined absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400">
                    search
                  </span>
                </div>
                <button class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded-lg transition-colors">
                  <span class="material-symbols-outlined">filter_list</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Reservation Tabs -->
          <div class="border-b border-gray-200">
            <nav class="flex -mb-px">
              <button
                v-for="tab in reservationTabs"
                :key="tab.id"
                @click="activeReservationTab = tab.id"
                class="px-6 py-4 border-b-2 font-medium text-sm transition-colors duration-300 flex items-center gap-2"
                :class="activeReservationTab === tab.id
                  ? 'border-primary text-primary'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'"
              >
                <span class="material-symbols-outlined text-lg">{{ tab.icon }}</span>
                {{ tab.name }}
                <span :class="tabBadgeClasses(tab.count)" class="ml-1">
                  {{ tab.count }}
                </span>
              </button>
            </nav>
          </div>

          <!-- Reservations Table -->
          <ReservationTable
            :reservations="filteredReservations"
            :active-tab="activeReservationTab"
            @check-in="checkInGuest"
            @check-out="checkOutGuest"
            @view-details="viewReservation"
            @edit-reservation="editReservation"
            @cancel-reservation="cancelReservation"
          />

          <!-- Empty State -->
          <div v-if="filteredReservations.length === 0" class="text-center py-12">
            <span class="material-symbols-outlined text-6xl text-gray-300 mb-4">meeting_room</span>
            <h3 class="text-lg font-medium text-gray-900 mb-2">No reservations today</h3>
            <p class="text-gray-500 mb-4">Create a new reservation or check for upcoming bookings</p>
            <button 
              @click="handleNewReservation"
              class="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/90 transition-colors flex items-center gap-2 mx-auto"
            >
              <span class="material-symbols-outlined">add</span>
              New Reservation
            </button>
          </div>
        </div>
      </div>

      <!-- Right Column - Sidebar -->
      <div class="space-y-6">
        <!-- Today's Overview -->
        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Today's Overview</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between p-3 bg-blue-50 rounded-lg">
              <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-blue-600">flight_land</span>
                <div>
                  <p class="font-medium text-blue-900">Arrivals</p>
                  <p class="text-sm text-blue-700">{{ dashboardData.metrics.expected_arrivals }} guests</p>
                </div>
              </div>
              <span class="text-blue-600 font-semibold">All Day</span>
            </div>
            
            <div class="flex items-center justify-between p-3 bg-green-50 rounded-lg">
              <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-green-600">flight_takeoff</span>
                <div>
                  <p class="font-medium text-green-900">Departures</p>
                  <p class="text-sm text-green-700">{{ dashboardData.metrics.expected_departures }} guests</p>
                </div>
              </div>
              <span class="text-green-600 font-semibold">All Day</span>
            </div>
            
            <div class="flex items-center justify-between p-3 bg-purple-50 rounded-lg">
              <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-purple-600">hotel</span>
                <div>
                  <p class="font-medium text-purple-900">Occupancy</p>
                  <p class="text-sm text-purple-700">{{ dashboardData.metrics.occupancy_rate }} occupied</p>
                </div>
              </div>
              <div class="w-16 bg-purple-200 rounded-full h-2">
                <div 
                  class="bg-purple-600 h-2 rounded-full" 
                  :style="{ width: parseInt(dashboardData.metrics.occupancy_rate) + '%' }"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Room Status -->
        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Room Status</h3>
          <div class="space-y-3">
            <div 
              v-for="status in formattedRoomStatuses" 
              :key="status.type"
              class="flex items-center justify-between p-3 rounded-lg border"
              :class="status.borderColor"
            >
              <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-lg" :class="status.iconColor">
                  {{ status.icon }}
                </span>
                <span class="font-medium" :class="status.textColor">{{ status.label }}</span>
              </div>
              <span class="font-semibold" :class="status.textColor">{{ status.count }}</span>
            </div>
          </div>
        </div>

        <!-- Recent Activity -->
        <div v-if="recentActivities.length > 0" class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Recent Activity</h3>
          <div class="space-y-4">
            <div 
              v-for="activity in recentActivities" 
              :key="activity.id"
              class="flex items-start gap-3 p-3 hover:bg-gray-50 rounded-lg transition-colors"
            >
              <span class="material-symbols-outlined text-gray-400 mt-0.5" :class="activity.iconColor">
                {{ activity.icon }}
              </span>
              <div class="flex-1">
                <p class="text-sm font-medium text-gray-900">{{ activity.message }}</p>
                <p class="text-xs text-gray-500 mt-1">{{ activity.time }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- VIP Alerts -->
        <div v-if="vipAlerts.length > 0" class="bg-white rounded-2xl shadow-sm border border-yellow-200 p-6">
          <h3 class="text-lg font-semibold text-yellow-900 mb-4 flex items-center gap-2">
            <span class="material-symbols-outlined">star</span>
            VIP Alerts
          </h3>
          <div class="space-y-3">
            <div 
              v-for="alert in vipAlerts" 
              :key="alert.id"
              class="p-3 bg-yellow-50 border border-yellow-200 rounded-lg"
            >
              <p class="text-sm font-medium text-yellow-900">{{ alert.guest_name }}</p>
              <p class="text-xs text-yellow-700 mt-1">{{ alert.message }}</p>
              <p class="text-xs text-yellow-600 mt-2">{{ alert.time }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Quick Stats Footer -->
    <div v-if="!loading" class="mt-8 grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
      <div class="bg-white p-4 rounded-xl border border-gray-200">
        <p class="text-2xl font-bold text-gray-900">{{ dashboardData.metrics.total_guests_today }}</p>
        <p class="text-sm text-gray-600">Total Guests Today</p>
      </div>
      <div class="bg-white p-4 rounded-xl border border-gray-200">
        <p class="text-2xl font-bold text-gray-900">{{ dashboardData.metrics.average_stay }}</p>
        <p class="text-sm text-gray-600">Avg. Stay (nights)</p>
      </div>
      <div class="bg-white p-4 rounded-xl border border-gray-200">
        <p class="text-2xl font-bold text-gray-900">{{ dashboardData.metrics.walk_ins }}</p>
        <p class="text-sm text-gray-600">Walk-in Reservations</p>
      </div>
      <div class="bg-white p-4 rounded-xl border border-gray-200">
        <p class="text-2xl font-bold text-gray-900">${{ dashboardData.metrics.revenue_today }}</p>
        <p class="text-sm text-gray-600">Today's Revenue</p>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../components/staffs/Headers.vue'
import MetricCard from '../components/staffs/MetricCard.vue'
import ActionButton from '../components/staffs/ActionButton.vue'
import ReservationTable from '../components/staffs/ReservationTable.vue'
import { getReservations } from '../api/auth/reservation'
import { fetchDashboardData } from '../api/auth/dashboardApi'
import { get as getFromStore } from '../localStorage'

export default {
  name: 'ReceptionistDashboard',
  components: { Header, MetricCard, ActionButton, ReservationTable },
  data() {
    return {
      dashboardData: {
        metrics: {},
        today_reservations: [],
        room_status: []
      },
      loading: true,
      searchQuery: '',
      currentTime: '',
      currentDate: '',
      activeReservationTab: 'arrivals',
      reservationTabs: [
        { id: 'arrivals', name: 'Arrivals', icon: 'flight_land', count: 0 },
        { id: 'departures', name: 'Departures', icon: 'flight_takeoff', count: 0 },
        { id: 'in-house', name: 'In-House', icon: 'hotel', count: 0 },
        { id: 'pending', name: 'Pending', icon: 'pending', count: 0 }
      ],
      recentActivities: [],
      vipAlerts: [],
      userInfo: null
    }
  },
  computed: {
    filteredReservations() {
      let filtered = this.dashboardData.today_reservations || []
      
      // Filter by active tab
      const today = new Date().toISOString().split('T')[0]
      switch (this.activeReservationTab) {
        case 'arrivals':
          filtered = filtered.filter(r => r.check_in === today && r.status === 'confirmed')
          break
        case 'departures':
          filtered = filtered.filter(r => r.check_out === today && r.status === 'checked-in')
          break
        case 'in-house':
          filtered = filtered.filter(r => r.status === 'checked-in')
          break
        case 'pending':
          filtered = filtered.filter(r => r.status === 'pending')
          break
      }
      
      // Filter by search query
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase()
        filtered = filtered.filter(r => {
          const guestName = r.guest?.name || r.guest_name || ''
          const roomNumber = r.room?.room_number || r.room_number || ''
          const reservationId = r.reservation_id || r.id || ''
          const guestEmail = r.guest?.email || r.email || ''
          
          return (
            guestName.toLowerCase().includes(query) ||
            roomNumber.toLowerCase().includes(query) ||
            reservationId.toString().toLowerCase().includes(query) ||
            guestEmail.toLowerCase().includes(query)
          )
        })
      }
      
      return filtered
    },
    
    formattedRoomStatuses() {
      return (this.dashboardData.room_status || []).map(item => {
        const config = this.getRoomStatusConfig(item.status)
        return {
          type: item.status,
          label: config.label,
          count: item.count || 0,
          icon: config.icon,
          iconColor: config.iconColor,
          textColor: config.textColor,
          borderColor: config.borderColor
        }
      })
    },
    
    // Mock recent activities for now
    recentActivities() {
      return [
        {
          id: 1,
          message: 'Dashboard loaded successfully',
          time: 'Just now',
          icon: 'check_circle',
          iconColor: 'text-green-500'
        }
      ]
    }
  },
  async mounted() {
    await this.loadDashboardData()
    this.startClock()
    this.loadUserInfo()
    this.updateTabCounts()
  },
  beforeUnmount() {
    if (this.clockInterval) {
      clearInterval(this.clockInterval)
    }
  },
  methods: {
    async loadDashboardData() {
      this.loading = true
      try {
        // Fetch data from your dashboard API
        const data = await fetchDashboardData()
        console.log('Dashboard data:', data)
        
        if (data) {
          this.dashboardData = data
        } else {
          // Fallback to empty data
          this.dashboardData = {
            metrics: {
              expected_arrivals: 0,
              expected_departures: 0,
              in_house_guests: 0,
              total_rooms: 0,
              rooms_occupied: 0,
              rooms_available: 0,
              occupancy_rate: "0%",
              revenue_today: 0,
              total_guests_today: 0,
              walk_ins: 0,
              average_stay: 0,
              arrival_trend: "stable",
              arrival_trend_value: "0%",
              departure_trend: "stable",
              departure_trend_value: "0%",
              occupancy_trend: "stable",
              availability_trend: "stable",
              availability_trend_value: "0%",
              guest_trend: "stable",
              guest_trend_value: "0%",
              pending_trend: "stable",
              pending_trend_value: "0%",
              revenue_trend: "stable",
              revenue_trend_value: "0%"
            },
            today_reservations: [],
            room_status: []
          }
        }
        
        this.updateTabCounts()
      } catch (err) {
        console.error('Error loading dashboard data:', err)
        // Set empty data on error
        this.dashboardData = {
          metrics: {
            expected_arrivals: 0,
            expected_departures: 0,
            in_house_guests: 0,
            total_rooms: 0,
            rooms_occupied: 0,
            rooms_available: 0,
            occupancy_rate: "0%",
            revenue_today: 0,
            total_guests_today: 0,
            walk_ins: 0,
            average_stay: 0
          },
          today_reservations: [],
          room_status: []
        }
      } finally {
        this.loading = false
      }
    },
    
    getRoomStatusConfig(status) {
      const configs = {
        'available': {
          label: 'Available',
          icon: 'check_circle',
          iconColor: 'text-green-600',
          textColor: 'text-green-700',
          borderColor: 'border-green-200'
        },
        'occupied': {
          label: 'Occupied',
          icon: 'person',
          iconColor: 'text-red-600',
          textColor: 'text-red-700',
          borderColor: 'border-red-200'
        },
        'maintenance': {
          label: 'Maintenance',
          icon: 'build',
          iconColor: 'text-yellow-600',
          textColor: 'text-yellow-700',
          borderColor: 'border-yellow-200'
        },
        'cleaning': {
          label: 'Cleaning',
          icon: 'cleaning_services',
          iconColor: 'text-purple-600',
          textColor: 'text-purple-700',
          borderColor: 'border-purple-200'
        },
        'reserved': {
          label: 'Reserved',
          icon: 'event',
          iconColor: 'text-blue-600',
          textColor: 'text-blue-700',
          borderColor: 'border-blue-200'
        }
      }
      
      return configs[status] || {
        label: status ? status.charAt(0).toUpperCase() + status.slice(1) : 'Unknown',
        icon: 'help',
        iconColor: 'text-gray-600',
        textColor: 'text-gray-700',
        borderColor: 'border-gray-200'
      }
    },
    
    updateTabCounts() {
      const today = new Date().toISOString().split('T')[0]
      const reservations = this.dashboardData.today_reservations || []
      
      this.reservationTabs = this.reservationTabs.map(tab => {
        let count = 0
        switch (tab.id) {
          case 'arrivals':
            count = reservations.filter(r => 
              r.check_in === today && (r.status === 'confirmed' || r.status === 'reserved')
            ).length
            break
          case 'departures':
            count = reservations.filter(r => 
              r.check_out === today && r.status === 'checked-in'
            ).length
            break
          case 'in-house':
            count = reservations.filter(r => 
              r.status === 'checked-in' || r.status === 'occupied'
            ).length
            break
          case 'pending':
            count = reservations.filter(r => 
              r.status === 'pending' || r.status === 'waiting'
            ).length
            break
        }
        return { ...tab, count }
      })
    },
    
    loadUserInfo() {
      const user = getFromStore("logged_in_user")
      if (user) {
        this.userInfo = {
          name: user.name || user.username || user.email || 'Receptionist',
          shift: user.shift || 'Morning (7AM - 3PM)'
        }
      }
    },
    
    startClock() {
      this.updateTime()
      this.clockInterval = setInterval(() => {
        this.updateTime()
      }, 60000)
    },
    
    updateTime() {
      const now = new Date()
      this.currentTime = now.toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: true 
      })
      this.currentDate = now.toLocaleDateString('en-US', { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
      })
    },
    
    tabBadgeClasses(count) {
      return count > 0 
        ? 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-primary text-white'
        : 'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-600'
    },
    
    handleNewReservation() {
      this.$router.push('/staff/reservations/new')
    },
    
    handleCheckIn() {
      this.activeReservationTab = 'arrivals'
    },
    
    handleCheckOut() {
      this.activeReservationTab = 'departures'
    },
    
    handleViewCalendar() {
      this.$router.push('/staff/calendar')
    },
    
    handleRoomStatus() {
      this.$router.push('/staff/rooms')
    },
    
    handleGuestSearch() {
      this.searchQuery = ''
      setTimeout(() => {
        const searchInput = document.querySelector('input[type="text"]')
        if (searchInput) searchInput.focus()
      }, 100)
    },
    
    async checkInGuest(reservation) {
      try {
        console.log('Check in guest:', reservation)
        // Here you would make an API call to update reservation status
        // For demo, update locally
        await this.loadDashboardData()
      } catch (err) {
        console.error('Error checking in guest:', err)
      }
    },
    
    async checkOutGuest(reservation) {
      try {
        console.log('Check out guest:', reservation)
        await this.loadDashboardData()
      } catch (err) {
        console.error('Error checking out guest:', err)
      }
    },
    
    viewReservation(reservation) {
      if (reservation.id) {
        this.$router.push(`/staff/reservations/${reservation.id}`)
      }
    },
    
    editReservation(reservation) {
      if (reservation.id) {
        this.$router.push(`/staff/reservations/edit/${reservation.id}`)
      }
    },
    
    async cancelReservation(reservation) {
      if (confirm(`Are you sure you want to cancel reservation ${reservation.reservation_id || reservation.id}?`)) {
        try {
          console.log('Cancel reservation:', reservation)
          await this.loadDashboardData()
        } catch (err) {
          console.error('Error cancelling reservation:', err)
        }
      }
    }
  }
}
</script>