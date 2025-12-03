<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
    <!-- Total Revenue -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Total Revenue</p>
          <p class="text-2xl font-bold text-gray-900">${{ stats.totalRevenue.toLocaleString() }}</p>
          <p class="text-sm text-green-600 mt-1">
            <span class="material-symbols-outlined text-base align-middle">trending_up</span>
            +{{ stats.revenueGrowth }}% vs last period
          </p>
        </div>
        <div class="p-3 bg-green-100 rounded-lg">
          <span class="material-symbols-outlined text-green-600 text-2xl">attach_money</span>
        </div>
      </div>
    </div>

    <!-- Average Occupancy -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Avg Occupancy</p>
          <p class="text-2xl font-bold text-gray-900">{{ stats.averageOccupancy }}%</p>
          <p class="text-sm text-green-600 mt-1">
            <span class="material-symbols-outlined text-base align-middle">trending_up</span>
            +{{ stats.occupancyGrowth }}%
          </p>
        </div>
        <div class="p-3 bg-blue-100 rounded-lg">
          <span class="material-symbols-outlined text-blue-600 text-2xl">hotel</span>
        </div>
      </div>
    </div>

    <!-- Total Guests -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Total Guests</p>
          <p class="text-2xl font-bold text-gray-900">{{ stats.totalGuests.toLocaleString() }}</p>
          <p class="text-sm text-green-600 mt-1">
            <span class="material-symbols-outlined text-base align-middle">trending_up</span>
            +{{ stats.guestGrowth }}%
          </p>
        </div>
        <div class="p-3 bg-purple-100 rounded-lg">
          <span class="material-symbols-outlined text-purple-600 text-2xl">group</span>
        </div>
      </div>
    </div>

    <!-- ADR -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-sm font-medium text-gray-600">Average Daily Rate</p>
          <p class="text-2xl font-bold text-gray-900">${{ stats.averageDailyRate }}</p>
          <p class="text-sm text-green-600 mt-1">
            <span class="material-symbols-outlined text-base align-middle">trending_up</span>
            +{{ stats.adrGrowth }}%
          </p>
        </div>
        <div class="p-3 bg-orange-100 rounded-lg">
          <span class="material-symbols-outlined text-orange-600 text-2xl">show_chart</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReportStats',
  props: {
    stats: {
      type: Object,
      required: true
    }
  }
}
</script>