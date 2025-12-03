<template>
  <div class="flex flex-wrap items-center justify-between gap-4">
    <div class="flex flex-col gap-1">
      <h1 class="text-3xl font-bold leading-tight tracking-tight text-gray-900">{{ title }}</h1>
      <p class="text-base font-normal leading-normal text-gray-500">{{ subtitle }}</p>
    </div>
    <button 
      @click="$emit('add-guest')"
      class="flex min-w-[84px] cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-lg h-10 px-4 bg-gray-800 text-white tracking-wide hover:bg-gray-700  focus:ring-[#0f766e]/50 border border-[#0f766e]/30 placeholder:text-gray-500 rounded-l-none border-l-0 pl-2 text-base font-normal leading-normal"
    >
      <span class="material-symbols-outlined text-xl">add</span>
      <span class="truncate">{{ actionText }}</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'PageHeader',
  props: {
    title: {
      type: String,
      default: 'Page Title'
    },
    subtitle: {
      type: String,
      default: 'Page subtitle description'
    },
    actionText: {
      type: String,
      default: 'Add New'
    }
  },
  emits: ['add-guest']
}
</script>