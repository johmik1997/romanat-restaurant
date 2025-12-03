<template>
  <header class="flex flex-wrap items-center justify-between gap-4 mb-8">
    <div class="flex flex-col">
      <h1 class="text-3xl font-black tracking-tight text-[#111418] ">{{ title }}</h1>
      <p class="text-gray-500">{{ subtitle }}</p>
    </div>
    <div class="flex-1 min-w-[300px] max-w-lg">
      <label class="flex flex-col h-12 w-full">
        <div class="flex w-full flex-1 items-stretch rounded-lg h-full">
        
          <input 
            v-model="searchQuery"
            class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-[#111418] dark:text-white focus:outline-0 focus:ring-2 focus:ring-[#0f766e]/50 border border-[#0f766e]/30 bg-white  h-full placeholder:text-gray-500 px-4 rounded-l-none border-l-0 pl-2 text-base font-normal leading-normal" 
            :placeholder="searchPlaceholder" 
          />
        </div>
      </label>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  props: {
    title: {
      type: String,
      default: 'Dashboard'
    },
    subtitle: {
      type: String,
      default: 'A summary of today\'s activities at a glance.'
    },
    searchPlaceholder: {
      type: String,
      default: 'Search guest name, room, or booking ID...'
    }
  },
  data() {
    return {
      searchQuery: ''
    }
  },
  watch: {
    searchQuery(newVal) {
      this.$emit('search', newVal)
    }
  }
}
</script>