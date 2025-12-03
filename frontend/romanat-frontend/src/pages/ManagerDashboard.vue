<template>
  <div class="flex-1 p-4 md:p-6 lg:p-8">
    <div class="flex flex-col w-full space-y-6">

      <!-- Page Header -->
      <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4">
        <div class="flex flex-col gap-2">
          <h1 class="text-gray-900 text-2xl md:text-3xl font-bold">Dashboard</h1>
          <p class="text-gray-500 text-sm md:text-base">An overview of hotel performance metrics.</p>
        </div>

        <div class="flex items-center gap-3">
          <!-- Search Bar -->
          <div class="relative flex-1 sm:flex-none">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search..."
              class="w-full sm:w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-lg
                     bg-white text-gray-900 placeholder-gray-500
                     focus:ring-2 focus:ring-primary/20 focus:border-primary transition-colors
                     duration-200"
            />
            <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-lg">
              search
            </span>
          </div>

          <!-- Notifications -->
          <button class="p-2 rounded-lg hover:bg-gray-100 text-gray-600 transition-colors duration-200">
            <span class="material-symbols-outlined text-xl">notifications</span>
          </button>

          <!-- User Avatar -->
          <div class="relative">
            <div
              class="bg-center bg-no-repeat bg-cover rounded-full size-10 border-2 border-white shadow-sm"
              style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuDw6ZDekvFvaxqQX42mxDDyGteR8PNbDs2H9nr6Ik8TDQdEuKoZnF_BV6sVfJsSQrMK03ORsPlMNYHGdh55cXAwEcrDF7aBxninLY6EGTZHjHbUS4ulfT2ZRjt_sAQNo6YbiQ89RHs1Xcj52Q34OEf5RIYQo2atxeqHpDtNnievGEcV72S3Hdtwrvgbe4a-XdgQVIpoEhfuhwh7D2HcXU0iXH1sxnowg4XYFd4CqNh2EqVRFZSDFXFkVqkGRAi_AdnfalSgGdlzxpY');"
            ></div>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex justify-center items-center h-64">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
      </div>

      <!-- Error State -->
      <div v-if="error" class="p-4 bg-red-100 text-red-700 rounded-lg">
        {{ error }}
      </div>

      <!-- PAGE CONTENT -->
      <div v-if="!loading && !error">

        <!-- Stats Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
          <DashboardStat
            title="Expected Arrivals"
            :value="metrics.expected_arrivals"
            percent="+12%"
            trend="up"
          />
          <DashboardStat
            title="Expected Departures"
            :value="metrics.expected_departures"
            percent="-4%"
            trend="down"
          />
          <DashboardStat
            title="In-House Guests"
            :value="metrics.in_house_guests"
            percent="+5%"
            trend="up"
          />
          <DashboardStat
            title="Revenue Today"
            :value="`$${metrics.revenue_today}`"
            percent="+8%"
            trend="up"
          />
        </div>

        <!-- Charts Section -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 md:gap-6">

          <!-- Revenue Chart -->
          <div class="lg:col-span-2 flex flex-col gap-4 rounded-xl border border-gray-200 p-4 md:p-6 bg-white shadow-sm">
            <div class="flex flex-col gap-1">
              <p class="text-gray-900 text-lg font-semibold">Revenue Over Time</p>
              <div class="flex flex-wrap items-baseline gap-2">
                <p class="text-gray-900 text-2xl md:text-[32px] font-bold">${{ metrics.revenue_today }}</p>
                <p class="text-gray-500 text-sm">Today</p>
                <p class="text-green-500 text-sm font-medium flex items-center gap-1">
                  <span class="material-symbols-outlined text-base">trending_up</span>
                  +15%
                </p>
              </div>
            </div>

            <RevenueChart :data="chartData" />
          </div>

          <!-- Booking Source Chart -->
          <BookingSourceChart />
        </div>

        <!-- Activity Table -->
        <DashboardActivityTable :reservations="today_reservations" />

      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import DashboardStat from "../components/dashboard/DashboardStat.vue"
import BookingSourceChart from "../components/dashboard/BookingSourceChart.vue"
import DashboardActivityTable from "../components/dashboard/DashboardActivityTable.vue"
import RevenueChart from "../components/dashboard/RevenueChart.vue"
import { fetchDashboardData } from "../api/auth/dashboardApi"

const loading = ref(true)
const error = ref(null)
const metrics = ref({})
const today_reservations = ref([])
const chartData = ref([])
const searchQuery = ref("")

// Load dashboard data
const loadDashboard = async () => {
  loading.value = true
  error.value = null

  try {
   const data = await fetchDashboardData()

    metrics.value = data.metrics
    today_reservations.value = data.today_reservations

    // revenue chart example — convert to chart points
    chartData.value = data.today_reservations.map(r => ({
      name: r.room.room_number,
      value: r.total_price
    }))

  } catch (err) {
    error.value = err.message
  }

  loading.value = false
}

onMounted(() => {
  loadDashboard()
})
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

button, input {
  transition: all 0.2s ease-in-out;
}

input:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
</style>
