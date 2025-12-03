<template>
  <section
    class="relative flex min-h-screen w-full flex-col items-center justify-center bg-cover bg-center text-center text-white overflow-hidden"
    :style="{
      backgroundImage: `linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6)), url('${heroImage}')`
    }"
  >
    <!-- Main Content -->
    <div class="relative z-10 w-full px-4">
      <div class="container mx-auto max-w-6xl">
        <!-- Hero Text Content -->
        <div class="mb-8 lg:mb-16 text-center">
          <div class="inline-flex items-center gap-2 bg-white/20 backdrop-blur-sm rounded-full px-4 py-2 mb-6">
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
              <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
            </svg>
            <span class="text-sm font-semibold">Luxury Beachfront Resort</span>
          </div>
          
          <h1 class="font-serif text-4xl md:text-6xl lg:text-7xl font-bold leading-tight mb-6">
            Your Sanctuary
            <span class="block text-accent mt-2">Awaits</span>
          </h1>
          <p class="max-w-2xl mx-auto text-lg md:text-xl text-white/90 leading-relaxed mb-8">
            Experience unparalleled luxury and tranquility by the sea at our exclusive beachfront resort.
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button 
              class="rounded-full bg-[#0f766e] px-8 py-4 font-semibold text-white hover:bg-teal-500 transition-transform duration-300 shadow-lg hover:shadow-xl hover:scale-105 flex items-center justify-center gap-2"
              @click="scrollToRooms"
              aria-label="Explore Rooms"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
              </svg>
              Explore Rooms
            </button>
            <button 
              class="rounded-full bg-white/20 backdrop-blur-sm px-8 py-4 font-semibold text-white hover:bg-white/30 transition-transform duration-300 border border-white/30 hover:scale-105 flex items-center justify-center gap-2"
              @click="scrollToExperiences"
              aria-label="View Experiences"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
              View Experiences
            </button>
          </div>
        </div>

        <!-- Booking Widget -->
        <div class="relative mb-32" >
          <div class="hidden lg:block absolute -bottom-32 left-1/2 transform -translate-x-1/2 w-full max-w-4xl">
            <BookingWidget />
          </div>
          <div class="lg:hidden mt-8 mb-12">
            <div class="bg-black/30 backdrop-blur-sm rounded-2xl p-4 border border-white/20">
              <h3 class="text-white font-semibold text-lg mb-4 text-center">Check Availability</h3>
              <MobileBookingWidget />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Scroll Indicator -->
    <!-- <div class="absolute bottom-12 left-1/2 transform -translate-x-1/2 z-10 hidden lg:flex flex-col items-center text-white/70">
      <span class="text-sm mb-2">Scroll to explore</span>
      <div class="w-6 h-10 border-2 border-white/50 rounded-full flex justify-center">
        <div class="w-1 h-3 bg-white/50 rounded-full mt-2 animate-bounce"></div>
      </div>
    </div> -->
  </section>
</template>


<script setup>
import BookingWidget from './BookingWidget.vue'
import MobileBookingWidget from './MobileBookingWidget.vue'

const heroImage = 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80'

const scrollToRooms = () => {
  document.getElementById('rooms')?.scrollIntoView({ behavior: 'smooth' })
}

const scrollToExperiences = () => {
  document.getElementById('experiences')?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped>
/* Custom animation for scroll indicator */
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.animate-bounce {
  animation: bounce 2s infinite;
}
</style>