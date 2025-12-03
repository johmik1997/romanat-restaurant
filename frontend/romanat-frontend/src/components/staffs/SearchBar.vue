<template>
  <div class="flex w-full">
    <label class="flex flex-col h-12 w-full">
      <div class="flex w-full flex-1 items-stretch rounded-lg h-full">
        <div class="text-gray-500 flex bg-white items-center justify-center pl-4 rounded-l-lg border border-gray-200 border-r-0">
          <span class="material-symbols-outlined">search</span>
        </div>
        <input 
          v-model="searchQuery"
          @input="$emit('search', searchQuery)"
            class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-[#111418] dark:text-white focus:outline-0 focus:ring-2 focus:ring-[#0f766e]/50 border border-[#0f766e]/30 bg-white  h-full placeholder:text-gray-500 px-4 rounded-l-none border-l-0 pl-2 text-base font-normal leading-normal" 
          :placeholder="placeholder" 
        />
      </div>
    </label>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    placeholder: {
      type: String,
      default: 'Search...'
    }
  },
  data() {
    return {
      searchQuery: ''
    }
  },
  emits: ['search']
}
</script>