<template>
  <section class="relative bg-gradient-to-br from-primary via-teal-700 to-teal-800 py-16 text-white overflow-hidden">
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute top-10 left-10 w-20 h-20 bg-accent rounded-full"></div>
      <div class="absolute bottom-10 right-10 w-16 h-16 bg-white rounded-full"></div>
      <div class="absolute top-1/2 left-1/4 w-12 h-12 bg-accent rounded-lg"></div>
    </div>
    
    <div class="container mx-auto max-w-7xl px-4 relative z-10">
      <div class="flex flex-col lg:flex-row items-center justify-between gap-12">
        <!-- Left Content -->
        <div class="lg:w-1/2 text-center lg:text-left">
          <div class="inline-flex items-center gap-2 bg-white/20 backdrop-blur-sm rounded-full px-4 py-2 mb-6">
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/>
            </svg>
            <span class="text-sm font-semibold">Limited Time Offer</span>
          </div>
          
          <h2 class="text-4xl md:text-5xl font-serif font-bold mb-6 leading-tight">
            Summer <span class="text-accent">Escape</span> Package
          </h2>
          
          <p class="text-xl mb-8 text-white/90 leading-relaxed">
            Book 3 nights and get the 4th night free! Experience luxury with our premium amenities and exclusive beach access.
          </p>
          
          <div class="flex items-center gap-4 mb-8 flex-wrap justify-center lg:justify-start">
            <div class="flex items-center gap-2 bg-white/10 rounded-lg px-4 py-2">
              <svg class="w-5 h-5 text-accent" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/>
              </svg>
              <span class="text-sm">Valid until August 31st</span>
            </div>
            <div class="flex items-center gap-2 bg-white/10 rounded-lg px-4 py-2">
              <svg class="w-5 h-5 text-accent" fill="currentColor" viewBox="0 0 20 20">
                <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"/>
              </svg>
              <span class="text-sm">Up to 4 guests</span>
            </div>
          </div>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
            <button 
              class="bg-accent text-white px-8 py-4 rounded-xl font-bold hover:bg-amber-500 transition-all duration-300 shadow-lg hover:shadow-xl hover:scale-105 flex items-center justify-center gap-2 group"
              @click="claimOffer"
            >
              <svg class="w-5 h-5 transition-transform duration-300 group-hover:scale-110" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M4 2a2 2 0 00-2 2v11a3 3 0 106 0V4a2 2 0 00-2-2H4zm1 14a1 1 0 100-2 1 1 0 000 2zm5-1.757l4.9-4.9a2 2 0 000-2.828L13.485 5.1a2 2 0 00-2.828 0L10 5.757v8.486zM16 18H9.071l6-6H16a2 2 0 012 2v2a2 2 0 01-2 2z" clip-rule="evenodd"/>
              </svg>
              Claim This Offer
            </button>
            <button 
              class="border-2 border-white text-white px-8 py-4 rounded-xl font-bold hover:bg-white hover:text-[#0f766e]  transition-all duration-300 backdrop-blur-sm hover:scale-105 flex items-center justify-center gap-2 group"
              @click="viewDetails"
            >
              <svg class="w-5 h-5 transition-transform duration-300 group-hover:scale-110" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
              </svg>
              View Details
            </button>
          </div>
        </div>

        <!-- Right Content - Benefits Card -->
        <div class="lg:w-1/2">
          <div class="bg-white/10 backdrop-blur-lg rounded-3xl p-8 border border-white/20 shadow-2xl">
            <div class="flex items-center gap-3 mb-6">
              <div class="h-12 w-12 bg-accent rounded-xl flex items-center justify-center">
                <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                </svg>
              </div>
              <h3 class="text-2xl font-bold font-serif">Package Includes</h3>
            </div>
            
            <ul class="space-y-4 mb-8">
              <li 
                v-for="benefit in benefits" 
                :key="benefit.id"
                class="flex items-start gap-4 p-3 rounded-xl hover:bg-white/5 transition-all duration-200 group"
              >
                <div class="h-8 w-8 bg-accent/20 rounded-full flex items-center justify-center flex-shrink-0 mt-1 group-hover:bg-accent/30 transition-colors">
                  <svg class="w-4 h-4 text-accent" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                  </svg>
                </div>
                <div class="flex-1">
                  <h4 class="font-semibold text-lg group-hover:text-accent transition-colors">{{ benefit.title }}</h4>
                  <p class="text-white/80 text-sm mt-1">{{ benefit.description }}</p>
                </div>
              </li>
            </ul>
            
            <!-- Price Section -->
            <div class="bg-white/5 rounded-2xl p-6 border border-white/10 hover:bg-white/10 transition-colors duration-300">
              <div class="flex items-end justify-between mb-2">
                <div>
                  <p class="text-white/70 text-sm">Starting from</p>
                  <div class="flex items-baseline gap-2">
                    <span class="text-3xl font-bold">$899</span>
                    <span class="text-white/70 line-through text-lg">$1,199</span>
                  </div>
                </div>
                <div class="text-right">
                  <div class="bg-accent text-white px-3 py-1 rounded-full text-sm font-bold">
                    Save 25%
                  </div>
                </div>
              </div>
              <p class="text-white/70 text-sm">for 4 nights • Includes all benefits</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Additional Info -->
      <div class="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
        <div class="bg-white/5 rounded-2xl p-6 backdrop-blur-sm hover:bg-white/10 transition-all duration-300 hover:-translate-y-1 group">
          <div class="w-12 h-12 bg-accent/20 rounded-xl flex items-center justify-center mx-auto mb-3 group-hover:bg-accent/30 transition-colors">
            <svg class="w-6 h-6 text-accent" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/>
            </svg>
          </div>
          <h4 class="font-semibold mb-2">24/7 Support</h4>
          <p class="text-white/80 text-sm">Dedicated concierge service</p>
        </div>
        <div class="bg-white/5 rounded-2xl p-6 backdrop-blur-sm hover:bg-white/10 transition-all duration-300 hover:-translate-y-1 group">
          <div class="w-12 h-12 bg-accent/20 rounded-xl flex items-center justify-center mx-auto mb-3 group-hover:bg-accent/30 transition-colors">
            <svg class="w-6 h-6 text-accent" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/>
            </svg>
          </div>
          <h4 class="font-semibold mb-2">Free Cancellation</h4>
          <p class="text-white/80 text-sm">Cancel up to 48 hours before</p>
        </div>
        <div class="bg-white/5 rounded-2xl p-6 backdrop-blur-sm hover:bg-white/10 transition-all duration-300 hover:-translate-y-1 group">
          <div class="w-12 h-12 bg-accent/20 rounded-xl flex items-center justify-center mx-auto mb-3 group-hover:bg-accent/30 transition-colors">
            <svg class="w-6 h-6 text-accent" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/>
            </svg>
          </div>
          <h4 class="font-semibold mb-2">Room Upgrade</h4>
          <p class="text-white/80 text-sm">Subject to availability</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const benefits = ref([
  { 
    id: 1, 
    title: '4th Night Free',
    description: 'Stay 3 nights and get the 4th night completely free'
  },
  { 
    id: 2, 
    title: 'Daily Gourmet Breakfast',
    description: 'Full breakfast buffet for two each morning'
  },
  { 
    id: 3, 
    title: 'Spa Treatment',
    description: '60-minute signature massage for two at our luxury spa'
  },
  { 
    id: 4, 
    title: 'Beach Cabana',
    description: 'Private beach cabana with butler service'
  },
  { 
    id: 5, 
    title: 'Welcome Amenity',
    description: 'Champagne and fruit basket upon arrival'
  },
  { 
    id: 6, 
    title: 'Late Check-out',
    description: 'Complimentary late check-out until 2 PM'
  }
])

const claimOffer = () => {
  console.log('Claiming special offer')
  // Redirect to booking page with offer code
  // or open booking modal
}

const viewDetails = () => {
  console.log('Viewing offer details')
  // Show detailed modal or navigate to offer page
}
</script>

<style scoped>
/* Custom background pattern animation */
@keyframes float {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg); 
  }
  50% { 
    transform: translateY(-20px) rotate(180deg); 
  }
}

.absolute div {
  animation: float 6s ease-in-out infinite;
}

.absolute div:nth-child(2) {
  animation-delay: -2s;
}

.absolute div:nth-child(3) {
  animation-delay: -4s;
}

/* Smooth transitions for all interactive elements */
button, .group {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>