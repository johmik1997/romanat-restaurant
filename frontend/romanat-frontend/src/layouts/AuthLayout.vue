<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4 text-black">
    <!-- Background Decorations -->
    <div class="absolute top-0 left-0 w-72 h-72 bg-blue-200 rounded-full -translate-x-1/2 -translate-y-1/2 opacity-50"></div>
    <div class="absolute bottom-0 right-0 w-96 h-96 bg-indigo-200 rounded-full translate-x-1/2 translate-y-1/2 opacity-50"></div>
    
    <!-- Main Content -->
    <div class="relative w-full max-w-6xl flex bg-white rounded-3xl shadow-2xl overflow-hidden">
      <!-- Left Side - Brand/Info -->
      <div class="hidden lg:flex lg:flex-1 bg-gradient-to-br from-[#0f766e]/30 to-[#0f766e]/90 text-white p-12 relative overflow-hidden">
        <!-- Background Pattern -->
        <div class="absolute inset-0 opacity-10">
          <div class="absolute top-10 left-10 w-20 h-20 border-2 border-white rounded-full"></div>
          <div class="absolute top-32 right-16 w-12 h-12 border-2 border-white rounded-full"></div>
          <div class="absolute bottom-20 left-20 w-16 h-16 border-2 border-white rounded-full"></div>
        </div>
        
        <div class="relative z-10 flex flex-col justify-between h-full">
          <!-- Logo/Brand -->
          <div>
            <div class="flex items-center space-x-3 mb-8">
              <div class="w-12 h-12 bg-white bg-opacity-20 rounded-xl flex items-center justify-center">
                <span class="material-icons-outlined text-2xl">hotel</span>
              </div>
              <span class="text-2xl font-bold">Romanat Restaurant</span>
            </div>
            
            <h1 class="text-4xl font-bold mb-6">
              Welcome to<br>Your Perfect Stay
            </h1>
            <p class="text-black text-lg leading-relaxed">
              Experience luxury and comfort like never before. Join thousands of satisfied guests who trust us for their perfect getaway.
            </p>
          </div>

          <!-- Features List -->
          <div class="space-y-4">
            <div v-for="feature in features" :key="feature.text" class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-white bg-opacity-20 rounded-full flex items-center justify-center">
                <span class="material-icons-outlined text-sm">check</span>
              </div>
              <span class="text-blue-100">{{ feature.text }}</span>
            </div>
          </div>

          <!-- Testimonial -->
          <div class="bg-white bg-opacity-10 rounded-2xl p-6 backdrop-blur-sm">
            <p class="text-black italic mb-4">
              "The best hotel experience I've ever had. The staff went above and beyond to make our stay memorable."
            </p>
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 bg-white bg-opacity-20 rounded-full"></div>
              <div>
                <p class="font-semibold">Sarah Johnson</p>
                <p class="text-black text-sm">Regular Guest</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Side - Auth Form -->
      <div class="flex-1 p-8 lg:p-12">
        <!-- Mobile Logo -->
        <div class="lg:hidden flex items-center justify-center mb-8">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center">
              <span class="material-icons-outlined text-white text-xl">hotel</span>
            </div>
            <span class="text-xl font-bold text-gray-900">Hotel Haven</span>
          </div>
        </div>

        <!-- Back Button -->
        <button 
          @click="goBack"
          class="flex items-center space-x-2 text-gray-600 hover:text-gray-800 mb-8 transition-colors"
        >
          <span class="material-icons-outlined">arrow_back</span>
          <span>Back to home</span>
        </button>

        <!-- Auth Content -->
        <div class="max-w-md mx-auto">
          <slot />
        </div>

        <!-- Footer -->
        <div class="mt-12 text-center">
          <p class="text-gray-600 text-sm">
            © 2024 Hotel Haven. All rights reserved.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthLayout',
  data() {
    return {
      features: [
        { text: 'Secure and reliable booking system' },
        { text: '24/7 Customer support' },
        { text: 'Best price guarantee' },
        { text: 'Instant booking confirmation' }
      ]
    }
  },
  methods: {
    goBack() {
      this.$router.push('/')
    }
  },
  mounted() {
    // Ensure Material Icons are loaded
    if (!document.querySelector('link[href*="material-icons"]')) {
      const link = document.createElement('link')
      link.href = 'https://fonts.googleapis.com/icon?family=Material+Icons+Outlined'
      link.rel = 'stylesheet'
      document.head.appendChild(link)
    }
  }
}
</script>

<style scoped>
/* Smooth transitions for all interactive elements */
button, a {
  transition: all 0.3s ease;
}

/* Custom shadow for depth */
.shadow-2xl {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

/* Backdrop blur for modern glass effect */
.backdrop-blur-sm {
  backdrop-filter: blur(4px);
}
</style>