<template>
  <div class="p-8">
    <!-- Page Header -->
    <PageHeader 
      title="Reports & Analytics"
      subtitle="Comprehensive hotel performance insights and visualizations"
      action-text="Export Dashboard"
      @add-guest="handleExportDashboard"
    />

    <!-- Date Range Picker -->
    <div class="bg-white rounded-xl border border-gray-200 p-6 mb-8">
      <div class="flex items-center justify-between">
        <h3 class="text-lg font-semibold text-gray-900">Report Period</h3>
        <DateRangePicker @date-range-change="handleDateRangeChange" />
      </div>
    </div>

    <!-- Key Metrics -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <MetricCard 
        v-for="metric in keyMetrics"
        :key="metric.title"
        :title="metric.title"
        :value="metric.value"
        :change="metric.change"
        :trend="metric.trend"
        :icon="metric.icon"
        :color="metric.color"
      />
    </div>

    <!-- Charts Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
      <!-- Revenue Chart -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-semibold text-gray-900">Revenue Trend</h3>
          <div class="flex gap-2">
            <button 
              v-for="period in revenuePeriods"
              :key="period"
              @click="selectedRevenuePeriod = period"
              :class="revenuePeriodClasses(period)"
            >
              {{ period }}
            </button>
          </div>
        </div>
        <div class="h-80">
          <RevenueChart :data="revenueData" :period="selectedRevenuePeriod" />
        </div>
      </div>

      <!-- Occupancy Chart -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-semibold text-gray-900">Occupancy Rate</h3>
          <div class="flex items-center gap-2 text-sm text-gray-600">
            <div class="flex items-center gap-1">
              <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
            </div>
          </div>
        </div>
        <div class="h-80">
          <OccupancyChart :data="occupancyData" />
        </div>
      </div>

      <!-- Room Type Performance -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-lg font-semibold text-gray-900">Room Type Performance</h3>
          <select 
            v-model="roomTypeMetric"
            class="bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
          >
            <option value="revenue">Revenue</option>
            <option value="occupancy">Occupancy</option>
            <option value="adr">ADR</option>
          </select>
        </div>
        <div class="h-80">
          <RoomTypeChart :data="roomTypeData" :metric="roomTypeMetric" />
        </div>
      </div>

      <!-- Guest Demographics -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-6">Guest Distribution</h3>
        <div class="h-80">
          <GuestDemographicsChart :data="guestDemographicsData" />
        </div>
      </div>
    </div>

    <!-- Detailed Data Tables -->
    <div class="grid grid-cols-1 gap-6 mb-8">
      <!-- Financial Summary -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-6">Financial Summary</h3>
        <FinancialTable :data="financialData" />
      </div>

      <!-- Occupancy Details -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-6">Daily Occupancy Details</h3>
        <OccupancyTable :data="dailyOccupancyData" />
      </div>
    </div>

    <!-- Additional Insights -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- Top Performing Rooms -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-6">Top Performing Rooms</h3>
        <TopRoomsList :rooms="topRooms" />
      </div>

      <!-- Guest Satisfaction -->
      <div class="bg-white rounded-xl border border-gray-200 p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-6">Guest Satisfaction</h3>
        <SatisfactionMetrics :metrics="satisfactionMetrics" />
      </div>
    </div>
  </div>
</template>

<script>
import PageHeader from '../components/staffs/PageHeader.vue'
import DateRangePicker from '../components/staffs/DateRangePicker.vue'
import MetricCard from '../components/staffs/MetricCard.vue'
import RevenueChart from '../components/charts/RevenueChart.vue'
import OccupancyChart from '../components/charts/OccupancyChart.vue'
import RoomTypeChart from '../components/charts/RoomTypeChart.vue'
import GuestDemographicsChart from '../components/charts/GuestDemographicsChart.vue'
import FinancialTable from '../components/Tables/FinancialTable.vue'
import OccupancyTable from '../components/Tables/OccupancyTable.vue'
import TopRoomsList from '../components/lists/TopRoomsLists.vue'
import SatisfactionMetrics from '../components/lists/SatisfactionMetrics.vue'

export default {
  name: 'Reports',
  components: {
    PageHeader,
    DateRangePicker,
    MetricCard,
    RevenueChart,
    OccupancyChart,
    RoomTypeChart,
    GuestDemographicsChart,
    FinancialTable,
    OccupancyTable,
    TopRoomsList,
    SatisfactionMetrics
  },
  data() {
    return {
      selectedRevenuePeriod: 'month',
      roomTypeMetric: 'revenue',
      revenuePeriods: ['week', 'month', 'quarter', 'year'],
      keyMetrics: [
        {
          title: 'Total Revenue',
          value: '$125,430',
          change: '+12.5%',
          trend: 'up',
          icon: 'attach_money',
          color: 'green'
        },
        {
          title: 'Average Occupancy',
          value: '78.2%',
          change: '+5.3%',
          trend: 'up',
          icon: 'hotel',
          color: 'blue'
        },
        {
          title: 'Average Daily Rate',
          value: '$189',
          change: '+3.2%',
          trend: 'up',
          icon: 'trending_up',
          color: 'purple'
        },
        {
          title: 'RevPAR',
          value: '$148',
          change: '+8.7%',
          trend: 'up',
          icon: 'bar_chart',
          color: 'orange'
        }
      ],
      revenueData: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
          {
            label: 'Room Revenue',
            data: [85000, 92000, 78000, 95000, 110000, 125000, 135000, 128000, 115000, 125430, 140000, 155000],
            borderColor: '#137fec',
            backgroundColor: 'rgba(19, 127, 236, 0.1)'
          },
          {
            label: 'Other Revenue',
            data: [15000, 18000, 22000, 25000, 28000, 32000, 35000, 38000, 42000, 45000, 48000, 52000],
            borderColor: '#10b981',
            backgroundColor: 'rgba(16, 185, 129, 0.1)'
          }
        ]
      },
      occupancyData: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [
          {
            label: 'Occupancy Rate',
            data: [65, 68, 72, 75, 78, 82, 85, 83, 79, 78, 76, 80],
            borderColor: '#8b5cf6',
            backgroundColor: 'rgba(139, 92, 246, 0.1)'
          }
        ]
      },
      roomTypeData: [
        { type: 'Standard', revenue: 450000, occupancy: 75, adr: 120 },
        { type: 'Deluxe', revenue: 380000, occupancy: 82, adr: 180 },
        { type: 'Suite', revenue: 280000, occupancy: 68, adr: 280 },
        { type: 'Executive', revenue: 320000, occupancy: 74, adr: 350 },
        { type: 'Presidential', revenue: 150000, occupancy: 55, adr: 650 }
      ],
      guestDemographicsData: {
        labels: ['Business', 'Leisure', 'Family', 'Couples', 'Group'],
        datasets: [
          {
            data: [35, 25, 20, 15, 5],
            backgroundColor: [
              '#137fec', '#10b981', '#8b5cf6', '#f59e0b', '#ef4444'
            ]
          }
        ]
      },
      financialData: [
        { category: 'Room Revenue', amount: 125430, change: '+12.5%' },
        { category: 'Food & Beverage', amount: 28450, change: '+8.2%' },
        { category: 'Spa Services', amount: 15600, change: '+15.3%' },
        { category: 'Other Services', amount: 8950, change: '+5.7%' },
        { category: 'Total Revenue', amount: 178430, change: '+11.2%' }
      ],
      dailyOccupancyData: [
        { date: '2023-10-20', occupied: 38, available: 7, occupancy: 84.4 },
        { date: '2023-10-21', occupied: 40, available: 5, occupancy: 88.9 },
        { date: '2023-10-22', occupied: 35, available: 10, occupancy: 77.8 },
        { date: '2023-10-23', occupied: 37, available: 8, occupancy: 82.2 },
        { date: '2023-10-24', occupied: 39, available: 6, occupancy: 86.7 },
        { date: '2023-10-25', occupied: 42, available: 3, occupancy: 93.3 },
        { date: '2023-10-26', occupied: 41, available: 4, occupancy: 91.1 }
      ],
      topRooms: [
        { number: '501', type: 'Presidential', revenue: 19500, occupancy: 92 },
        { number: '401', type: 'Executive', revenue: 16800, occupancy: 88 },
        { number: '301', type: 'Suite', revenue: 14200, occupancy: 85 },
        { number: '201', type: 'Deluxe', revenue: 11800, occupancy: 90 },
        { number: '101', type: 'Standard', revenue: 9800, occupancy: 82 }
      ],
      satisfactionMetrics: [
        { metric: 'Overall Rating', value: 4.7, change: '+0.2' },
        { metric: 'Cleanliness', value: 4.8, change: '+0.1' },
        { metric: 'Service', value: 4.6, change: '+0.3' },
        { metric: 'Amenities', value: 4.5, change: '+0.1' },
        { metric: 'Value', value: 4.4, change: '+0.2' }
      ]
    }
  },
  methods: {
    handleDateRangeChange(dateRange) {
      console.log('Date range changed:', dateRange)
      // Fetch new data based on date range
    },
    handleExportDashboard() {
      console.log('Exporting dashboard data...')
      // Export functionality
    },
    revenuePeriodClasses(period) {
      const baseClasses = 'px-3 py-1 rounded-lg text-sm font-medium transition-colors'
      return period === this.selectedRevenuePeriod
        ? `${baseClasses} bg-primary text-white`
        : `${baseClasses} bg-white text-gray-700 border border-gray-200 hover:bg-gray-50`
    }
  }
}
</script>