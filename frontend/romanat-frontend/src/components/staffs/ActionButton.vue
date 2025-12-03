<template>
  <button 
    :class="buttonClasses"
    @click="$emit('click')"
  >
    <span class="material-symbols-outlined text-lg">{{ icon }}</span>
    <span class="truncate">{{ label }}</span>
  </button>
</template>

<script>
export default {
  name: 'ActionButton',
  props: {
    label: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    variant: {
      type: String,
      default: 'primary', // 'primary' or 'secondary'
      validator: (value) => ['primary', 'secondary'].includes(value)
    }
  },
  computed: {
    buttonClasses() {
      const baseClasses = 'flex min-w-[84px] cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-lg h-10 px-4 text-sm font-bold leading-normal tracking-[0.015em] transition-colors'
      
      const variants = {
        primary: 'bg-[#0f766e] text-white hover:bg-[#0f766e]/90',
        secondary: 'bg-white dark:bg-gray-700 text-[#111418] dark:text-white border border-[#E1E5E8] dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-600'
      }
      
      return `${baseClasses} ${variants[this.variant]}`
    }
  }
}
</script>