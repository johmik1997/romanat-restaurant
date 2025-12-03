<template>
  <nav aria-label="Pagination" class="flex items-center justify-between border-t border-gray-200 px-4 sm:px-0 mt-6 pt-6">
    <div class="hidden sm:block">
      <p class="text-sm text-gray-700">
        Showing <span class="font-medium">{{ startItem }}</span> to <span class="font-medium">{{ endItem }}</span> of <span class="font-medium">{{ totalItems }}</span> results
      </p>
    </div>
    <div class="flex flex-1 justify-between sm:justify-end">
      <button 
        @click="$emit('previous-page')"
        :disabled="currentPage === 1"
        class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        Previous
      </button>
      <button 
        @click="$emit('next-page')"
        :disabled="currentPage * itemsPerPage >= totalItems"
        class="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        Next
      </button>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    currentPage: {
      type: Number,
      default: 1
    },
    itemsPerPage: {
      type: Number,
      default: 10
    },
    totalItems: {
      type: Number,
      default: 0
    }
  },
  computed: {
   startItem() {
  if (this.totalItems === 0) return 0;
  return (this.currentPage - 1) * this.itemsPerPage + 1;
},
endItem() {
  return Math.min(this.currentPage * this.itemsPerPage, this.totalItems);
}

  },
  emits: ['previous-page', 'next-page']
}
</script>