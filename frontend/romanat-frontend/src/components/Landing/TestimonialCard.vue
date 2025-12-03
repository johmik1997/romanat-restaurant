<template>
  <div class="group bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-2 p-8 relative overflow-hidden">
    <!-- Background Decoration -->
    <div class="absolute top-0 right-0 w-20 h-20 bg-[#0f766e]/5 rounded-full -translate-y-10 translate-x-10"></div>
    
    <!-- Rating Stars -->
    <div class="flex items-center gap-1 mb-4">
      <span 
        v-for="star in 5" 
        :key="star"
        class="material-symbols-outlined text-lg"
        :class="star <= rating ? 'text-yellow-500' : 'text-gray-300'"
        :style="{ fontVariationSettings: star <= rating ? '\'FILL\' 1' : '\'FILL\' 0' }"
      >
        star
      </span>
    </div>

    <!-- Testimonial Text -->
    <p class="text-gray-600 mb-6 leading-relaxed text-lg relative z-10">
      "{{ text }}"
    </p>

    <!-- Guest Info -->
    <div class="flex items-center gap-4">
      <div class="relative">
        <img 
          :src="avatar" 
          :alt="name" 
          class="h-14 w-14 rounded-2xl object-cover border-2 border-white shadow-md"
        />
        <div class="absolute -bottom-1 -right-1 h-6 w-6 bg-primary rounded-full flex items-center justify-center">
          <span class="material-symbols-outlined text-white text-sm">check</span>
        </div>
      </div>
      <div class="flex-1">
        <h3 class="font-bold text-gray-800 text-lg">{{ name }}</h3>
        <p class="text-secondary text-sm font-medium mb-1">{{ role }}</p>
        <div class="flex items-center gap-4 text-xs text-gray-500">
          <span class="flex items-center gap-1">
            <span class="material-symbols-outlined text-xs">king_bed</span>
            {{ roomType }}
          </span>
          <span class="flex items-center gap-1">
            <span class="material-symbols-outlined text-xs">calendar_today</span>
            {{ stayDate }}
          </span>
        </div>
      </div>
    </div>

    <!-- Quote Icon -->
    <div class="absolute bottom-6 right-6 text-primary/10">
      <span class="material-symbols-outlined text-6xl">format_quote</span>
    </div>

    <!-- Hover Effect Border -->
    <div class="absolute inset-0 rounded-2xl border-2 border-transparent group-hover:border-[#0f766e]/20 transition-colors duration-300 pointer-events-none"></div>
  </div>
</template>

<script setup>
defineProps({
  name: {
    type: String,
    required: true
  },
  role: {
    type: String,
    required: true
  },
  text: {
    type: String,
    required: true
  },
  avatar: {
    type: String,
    required: true
  },
  rating: {
    type: Number,
    default: 5
  },
  stayDate: {
    type: String,
    default: 'Recent Stay'
  },
  roomType: {
    type: String,
    default: 'Guest'
  }
})
</script>