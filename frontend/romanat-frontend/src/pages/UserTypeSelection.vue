<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
    <div class="max-w-4xl w-full">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Welcome to <span class="text-blue-600">Romanat Restaurant </span>
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto">
          Please select your role to continue to your personalized experience
        </p>
      </div>

      <!-- Selection Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-3xl mx-auto">
        <!-- Guest Card -->
        <div 
          class="relative bg-white rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 cursor-pointer group overflow-hidden"
          @click="selectUserType('guest')"
          @mouseenter="hoveredCard = 'guest'"
          @mouseleave="hoveredCard = null"
        >
          <div class="absolute inset-0 bg-gradient-to-br from-blue-500 to-blue-600 opacity-0 group-hover:opacity-5 transition-opacity duration-300"></div>
          
          <!-- Decorative Element -->
          <div class="absolute top-0 right-0 w-32 h-32 bg-blue-100 rounded-full -translate-y-16 translate-x-16 group-hover:scale-110 transition-transform duration-300"></div>
          
          <div class="relative p-8">
            <!-- Icon -->
            <div class="w-20 h-20 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-blue-500 transition-colors duration-300">
              <span class="material-icons-outlined text-3xl text-blue-600 group-hover:text-white transition-colors duration-300">
                person
              </span>
            </div>

            <!-- Content -->
            <h3 class="text-2xl font-bold text-gray-900 mb-3">Guest</h3>
            <p class="text-gray-600 mb-6 leading-relaxed">
              Book rooms, manage reservations, and enjoy our premium hospitality services as our valued guest.
            </p>

            <!-- Features -->
            <ul class="space-y-2 mb-6">
              <li class="flex items-center text-gray-600">
                <span class="material-icons-outlined text-green-500 text-lg mr-2">check_circle</span>
                Book rooms & suites
              </li>
              <li class="flex items-center text-gray-600">
                <span class="material-icons-outlined text-green-500 text-lg mr-2">check_circle</span>
                Manage reservations
              </li>
              <li class="flex items-center text-gray-600">
                <span class="material-icons-outlined text-green-500 text-lg mr-2">check_circle</span>
                Access hotel amenities
              </li>
            </ul>

            <!-- CTA -->
            <div class="flex items-center justify-between">
              <span class="text-blue-600 font-semibold">Continue as Guest</span>
              <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center group-hover:bg-blue-500 transition-colors duration-300">
                <span class="material-icons-outlined text-blue-600 group-hover:text-white transition-colors duration-300">
                  arrow_forward
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Staff Card -->
        <div 
          class="relative bg-white rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 cursor-pointer group overflow-hidden"
          @click="selectUserType('staff')"
          @mouseenter="hoveredCard = 'staff'"
          @mouseleave="hoveredCard = null"
        >
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-500 to-purple-600 opacity-0 group-hover:opacity-5 transition-opacity duration-300"></div>
          
          <!-- Decorative Element -->
          <div class="absolute top-0 right-0 w-32 h-32 bg-indigo-100 rounded-full -translate-y-16 translate-x-16 group-hover:scale-110 transition-transform duration-300"></div>
          
          <div class="relative p-8">
            <!-- Icon -->
            <div class="w-20 h-20 bg-indigo-100 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-indigo-500 transition-colors duration-300">
              <span class="material-icons-outlined text-3xl text-indigo-600 group-hover:text-white transition-colors duration-300">
                admin_panel_settings
              </span>
            </div>

            <!-- Content -->
            <h3 class="text-2xl font-bold text-gray-900 mb-3">Staff Member</h3>
            <p class="text-gray-600 mb-6 leading-relaxed">
              Access the staff dashboard to manage reservations, guests, and hotel operations efficiently.
            </p>

            <!-- Features -->
            <ul class="space-y-2 mb-6">
              <li class="flex items-center text-gray-600">
                <span class="material-icons-outlined text-green-500 text-lg mr-2">check_circle</span>
                Manage guest reservations
              </li>
              <li class="flex items-center text-gray-600">
                <span class="material-icons-outlined text-green-500 text-lg mr-2">check_circle</span>
                Room management
              </li>
              <li class="flex items-center text-gray-600">
                <span class="material-icons-outlined text-green-500 text-lg mr-2">check_circle</span>
                Administrative tools
              </li>
            </ul>

            <!-- CTA -->
            <div class="flex items-center justify-between">
              <span class="text-indigo-600 font-semibold">Staff Login</span>
              <div class="w-10 h-10 bg-indigo-100 rounded-full flex items-center justify-center group-hover:bg-indigo-500 transition-colors duration-300">
                <span class="material-icons-outlined text-indigo-600 group-hover:text-white transition-colors duration-300">
                  arrow_forward
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="text-center mt-12">
        <p class="text-gray-500 text-sm">
          Need help? Contact support at 
          <a href="mailto:support@hotelhaven.com" class="text-blue-600 hover:text-blue-700 underline">
            support@hotelhaven.com
          </a>
        </p>
      </div>

      <!-- Loading Overlay -->
      <div v-if="loading" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white rounded-2xl p-8 flex flex-col items-center">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
          <p class="text-gray-700">Redirecting...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserTypeSelection',
  data() {
    return {
      hoveredCard: null,
      loading: false
    }
  },
  methods: {
    async selectUserType(type) {
      this.loading = true
      
      // Simulate API call or processing
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      this.loading = false
      
      // Redirect based on user type
      if (type === 'guest') {
        this.$router.push('/guest')
      } else if (type === 'staff') {
        this.$router.push('/staff')
      }
    }
  },
  mounted() {
    // Add material icons if not already added
    if (!document.querySelector('link[href*="material-icons"]')) {
      const link = document.createElement('link')
      link.href = 'https://fonts.googleapis.com/icon?family=Material+Icons+Outlined'
      link.rel = 'stylesheet'
      document.head.appendChild(link)
    }
  }
}
</script>

<!-- Keep the same template and style -->
<style scoped>
/* Custom animations */
.group:hover .group-hover\:scale-110 {
  transform: scale(1.1);
}

.group:hover .group-hover\:-translate-y-2 {
  transform: translateY(-0.5rem);
}

/* Smooth transitions */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}

/* Custom shadow effects */
.shadow-xl {
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.hover\:shadow-2xl:hover {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

/* Material Icons sizing */
.material-icons-outlined {
  font-size: inherit;
}
</style>