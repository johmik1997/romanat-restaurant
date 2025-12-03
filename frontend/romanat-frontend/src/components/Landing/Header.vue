<template>
  <header
    class="fixed top-0 left-0 right-0 z-50 w-full transition-all duration-300 bg-white/95 backdrop-blur-lg border-b border-gray-100"
  >
    <div class="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">

        <router-link to="/guest" class="flex items-center gap-3 group">
          <div class="size-7 text-teal-600 transition-transform group-hover:scale-110">
            <svg fill="currentColor" viewBox="0 0 48 48">
              <path d="M24 4C25.7818 14.2173 33.7827 22.2182 44 24C33.7827 25.7818 25.7818 33.7827 24 44C22.2182 33.7827 14.2173 25.7818 4 24C14.2173 22.2182 22.2182 14.2173 24 4Z"/>
            </svg>
          </div>
          <h2 class="text-xl font-semibold text-gray-900 group-hover:text-teal-600 transition-colors">Romanat</h2>
        </router-link>

        <nav class="hidden md:flex items-center gap-8">
          <a 
            v-for="link in navigationLinks" 
            :key="link.name"
            :href="link.href" 
            class="text-sm font-medium text-gray-600 hover:text-teal-600 transition-colors duration-200 relative after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 after:bg-teal-600 after:transition-all hover:after:w-full"
          >
            {{ link.name }}
          </a>
        </nav>

        <!-- Buttons -->
        <div class="flex items-center gap-3">

          <!-- User Section -->
          <div class="relative" v-if="username">
            <button
              @click="dropdownOpen = !dropdownOpen"
              class="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-700 hover:text-teal-600 transition-colors rounded-lg hover:bg-gray-50"
            >
              <div class="size-8 bg-teal-100 rounded-full flex items-center justify-center text-teal-600 text-sm font-medium">
                {{ username.charAt(0).toUpperCase() }}
              </div>
              <span>Hi, {{ username }}</span>
            </button>

            <!-- Dropdown -->
            <div
              v-if="dropdownOpen"
              class="absolute right-0 mt-2 w-48 bg-white rounded-xl shadow-lg border border-gray-100 py-2 z-50"
            >
              <button
                @click="handleLogout"
                class="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 hover:text-red-600 transition-colors flex items-center gap-2"
              >
                <svg class="size-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
                </svg>
                Sign Out
              </button>
            </div>
          </div>

          <!-- Sign In Button -->
          <router-link
            v-else
            to="/login"
            class="px-6 py-2 text-sm font-medium text-teal-600 hover:text-teal-700 transition-colors rounded-lg hover:bg-teal-50"
          >
            Sign In
          </router-link>

         <router-link v-if="reservation && ['pending','confirmed','checked_in'].includes(reservation.status)" to="/customer/reservation">
  <button
    class="px-6 py-2.5 bg-teal-600 text-white text-sm font-medium rounded-lg hover:bg-teal-700 transition-colors shadow-sm hover:shadow-md"
  >
    View My Reservation
  </button>
</router-link>

<router-link v-else to="/rooms">
  <button
    class="px-6 py-2.5 bg-teal-600 text-white text-sm font-medium rounded-lg hover:bg-teal-700 transition-colors shadow-sm hover:shadow-md"
  >
    Book Now
  </button>
</router-link>

        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { store, load, remove } from '../../localStorage/index.js'
import { getCustomerReservation } from '../../api/auth/userApi.js'

const router = useRouter()
const dropdownOpen = ref(false)

const navigationLinks = [
  { name: 'Rooms', href: '#rooms' },
  { name: 'Experiences', href: '#experiences' },
  { name: 'Testimonials', href: '#testimonials' },
  { name: 'Contact', href: '#contact' }
]

const username = computed(() => store.logged_in_user?.username || null)

const reservation = ref(null)

onMounted(async () => {
  await load('logged_in_user')
  try {
    const data = await getCustomerReservation() // API returns reservation of logged-in user
    reservation.value = data // null if no active reservation
  } catch (e) {
    console.error("Failed to fetch reservation", e)
  }
})

const handleLogout = async () => {
  await remove('logged_in_user')
  dropdownOpen.value = false
  router.push('/login')
}

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.relative')) {
    dropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})
</script>

<style scoped>
header {
  backdrop-filter: blur(12px);
}
</style>