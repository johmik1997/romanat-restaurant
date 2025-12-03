<template>
  <div class="overflow-x-auto">
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Change</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="item in data" :key="item.category" class="hover:bg-gray-50">
          <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
            {{ item.category }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
            ${{ item.amount.toLocaleString() }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm">
            <span :class="changeColor(item.change)" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium">
              {{ item.change }}
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'FinancialTable',
  props: {
    data: Array
  },
  methods: {
    changeColor(change) {
      return change.startsWith('+') ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
    }
  }
}
</script>