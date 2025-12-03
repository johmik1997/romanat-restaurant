<template>
  <div class="min-h-screen flex items-center justify-center p-6 relative overflow-hidden bg-[#334f4f]">

    <!-- Background -->
    <div 
      class="absolute inset-0 bg-cover bg-center opacity-40"
      :style="{ backgroundImage: `url('${backgroundImage}')` }"
    ></div>

    <!-- Soft Dark Overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/70 backdrop-blur-sm"></div>

    <!-- Login Card -->
    <div class="relative z-10 w-full max-w-md p-10 rounded-3xl bg-black/30 shadow-2xl backdrop-blur-xl border border-white/10">

      <!-- Logo -->
      <div class="flex flex-col items-center mb-8">
        <div class="h-14 w-14 text-[#0f766e] drop-shadow-lg">
          <svg fill="none" stroke="currentColor" stroke-width="1.3" viewBox="0 0 24 24">
            <path d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21"/>
          </svg>
        </div>
        <p class="mt-4 text-2xl font-semibold text-white tracking-wide">
          Romanat
        </p>
      </div>

      <!-- Heading -->
      <div class="text-center mb-10">
        <h1 class="text-3xl font-bold text-white mb-1">Welcome Back</h1>
        <p class="text-gray-400">Access your reservations and manage your stay</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleLogin" class="space-y-6">

        <!-- Email -->
        <div>
          <label class="block text-sm text-gray-300 mb-2">Username</label>
          <div class="relative">
            <input 
              v-model="form.username"
              type="text"
              placeholder="Enter username"
              class="w-full h-12 rounded-xl bg-white/10 text-white px-4 border border-white/10 placeholder-gray-400 focus:ring-2 focus:ring-[#0f766e] focus:outline-none transition-all duration-300"
            />
          </div>
        </div>

        <!-- Password -->
        <div>
          <label class="block text-sm text-gray-300 mb-2">Password</label>
          <div class="relative">
            <input 
              v-model="form.password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="••••••••"
              class="w-full h-12 rounded-xl bg-white/10 text-white px-4 pr-12 border border-white/10 placeholder-gray-400 focus:ring-2 focus:ring-[#0f766e] focus:outline-none transition-all duration-300"
            />
            <button 
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white transition-colors duration-300"
            >
              <!-- Eye icon for hidden password -->
              <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              <!-- Eye slash icon for visible password -->
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Error Message -->
        <div 
          v-if="error"
          class="flex items-center gap-2 text-red-400 text-sm bg-red-400/10 p-3 border border-red-400/20 rounded-lg"
        >
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
          </svg>
          <span>{{ error }}</span>
        </div>

        <!-- Login Button -->
        <button 
          type="submit"
          :disabled="loading"
          class="w-full h-12 rounded-xl bg-[#0f766e] text-white font-semibold shadow-lg hover:bg-[#0d5d56] disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-300 flex items-center justify-center gap-2"
        >
          <!-- Loading Spinner -->
          <svg 
            v-if="loading"
            class="w-5 h-5 animate-spin"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
          </svg>
          <span>{{ loading ? 'Signing in...' : 'Login' }}</span>
        </button>

      </form>

      <!-- Sign Up Link -->
      <div class="mt-8 text-center text-gray-400 text-sm">
        Don't have an account?
        <router-link to="/signup" class="text-[#0f766e] ml-1 font-medium hover:underline cursor-pointer transition-colors duration-300">
          Sign Up
        </router-link>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authenticate } from '../api/auth/loginApi.js' // your auth.js
import { save as stor } from '../localStorage/index.js' // your reactive localStorage wrapper

const router = useRouter()

const backgroundImage = 'https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80'

const form = ref({
  username: '',
  password: ''
})

const showPassword = ref(false)
const loading = ref(false)
const error = ref('')

const handleLogin = async () => {
  if (!form.value.username || !form.value.password) {
    error.value = 'Please fill in all fields'
    return
  }
console.log(form.value.username, form.value.password);

  loading.value = true
  error.value = ''

  try {
    const data = await authenticate(form.value)

    await stor('logged_in_user', {
      access_token: data.access,
      refresh_token: data.refresh,
      username: form.value.username,
      is_admin: data.is_admin || false,
      requiresReset: data.requiresReset || false,
      id: data.id,
      roleName:data.role.name,

    })
    form.value.username=''
    form.value.password=''
    router.push('/')
  } catch (err) {
    error.value = err.detail || 'Invalid username or password.'
  } finally {
    loading.value = false
  }
}


   
</script>

<style scoped>
/* Custom glow effect */
.shadow-glow {
  box-shadow: 0 0 15px 5px rgba(15, 118, 110, 0.3);
}

/* Smooth transitions for all interactive elements */
button, input, a {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Focus styles for accessibility */
input:focus {
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.3);
  border-color: rgba(15, 118, 110, 0.5);
}

/* Custom animation for the logo */
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

.h-14.w-14 {
  animation: float 3s ease-in-out infinite;
}
</style>