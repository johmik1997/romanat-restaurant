<template>
  <div class="min-h-screen flex items-center justify-center p-6 relative overflow-hidden bg-[#0a0f0f]">

    <!-- Background -->
    <div 
      class="absolute inset-0 bg-cover bg-center opacity-40"
      :style="{ backgroundImage: `url('${backgroundImage}')` }"
    ></div>

    <!-- Soft Dark Overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/70 backdrop-blur-sm"></div>

    <!-- Signup Card -->
    <div class="relative z-10 w-full max-w-lg p-10 rounded-3xl bg-black/30 shadow-2xl backdrop-blur-xl border border-white/10">

      <!-- Logo -->
      <div class="flex flex-col items-center mb-8">
        <div class="h-14 w-14 text-[#0f766e] drop-shadow-lg">
          <svg fill="none" stroke="currentColor" stroke-width="1.3" viewBox="0 0 24 24">
            <path d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21"/>
          </svg>
        </div>
        <p class="mt-4 text-2xl font-semibold text-white tracking-wide">
          Serenity Cove
        </p>
      </div>

      <!-- Heading -->
      <div class="text-center mb-10">
        <h1 class="text-3xl font-bold text-white mb-1">Create Your Account</h1>
        <p class="text-gray-400">Join us and start planning your perfect stay</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleSignup" class="space-y-6">
        
        <!-- First + Last Name -->
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm text-gray-300 mb-2">First Name</label>
            <input v-model="form.firstName" type="text" placeholder="John" class="input"/>
          </div>
          <div>
            <label class="block text-sm text-gray-300 mb-2">Last Name</label>
            <input v-model="form.lastName" type="text" placeholder="Doe" class="input"/>
          </div>
        </div>

        <!-- Email -->
        <div>
          <label class="block text-sm text-gray-300 mb-2">Email Address</label>
          <input v-model="form.email" type="email" placeholder="you@example.com" class="input"/>
        </div>
        <div>
          <label class="block text-sm text-gray-300 mb-2">Username</label>
          <input v-model="form.username" type="text" placeholder="username" class="input"/>
        </div>

        <!-- Phone -->
        <div>
          <label class="block text-sm text-gray-300 mb-2">Phone Number</label>
          <input v-model="form.phone" type="tel" placeholder="+1 555-123-4567" class="input"/>
        </div>

        <!-- Password -->
        <div>
          <label class="block text-sm text-gray-300 mb-2">Password</label>
          <div class="relative">
            <input v-model="form.password" :type="showPassword ? 'text' : 'password'" placeholder="••••••••" class="input pr-12"/>
            <button type="button" @click="showPassword = !showPassword" class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white">
              <svg v-if="!showPassword" class="w-5 h-5" fill="currentColor"><path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/><path d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7C18.268 14.057 14.478 17 10 17S1.732 14.057.458 10z"/></svg>
              <svg v-else class="w-5 h-5" fill="currentColor"><path d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14..."/></svg>
            </button>
          </div>
        </div>

        <!-- Error -->
        <div v-if="error" class="flex items-center gap-2 text-red-400 text-sm bg-red-400/10 p-3 border border-red-400/20 rounded-lg">
          <svg class="w-4 h-4" fill="currentColor"><path d="M18 10A8 8 0 112 10..."/></svg>
          <span>{{ error }}</span>
        </div>

        <!-- Signup Button -->
        <button type="submit" class="w-full h-12 rounded-xl bg-[#0f766e] text-white font-semibold shadow-lg hover:bg-[#0d5d56] transition-all duration-300 flex items-center justify-center gap-2">
          <svg v-if="loading" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path d="M4 4v5h.582m15.356 2A8.001..."/>
          </svg>
          <span>{{ loading ? 'Creating account...' : 'Sign Up' }}</span>
        </button>

      </form>

      <!-- Login Link -->
      <div class="mt-8 text-center text-gray-400 text-sm">
        Already have an account?
        <a @click="router.push('/login')" class="text-[#0f766e] ml-1 font-medium hover:underline cursor-pointer">
          Login
        </a>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import axios from "axios"
import { register } from "../api/auth/loginApi"

const router = useRouter()

const backgroundImage = "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=2070&q=80"

const form = ref({
  firstName: "",
  lastName: "",
  email: "",
  phone: "",
  password: "",
  username:"",
  role:""
})

const showPassword = ref(false)
const loading = ref(false)
const error = ref("")


// Handle form submit
const handleSignup = async () => {
  if (!form.value.firstName || !form.value.lastName || !form.value.email || !form.value.phone || !form.value.password||!form.value.username) {
    error.value = "Please fill in all fields"
    return
  }

  loading.value = true
  error.value = ""

  try {
    await register({
      first_name: form.value.firstName,
      last_name: form.value.lastName,
      email: form.value.email,
      phone: form.value.phone,
      password: form.value.password,
      username:form.value.username
    })
    router.push("/login")
  } catch (err) {
    error.value = err.detail || "Signup failed. Please try again."
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.input {
  width: 100%;
  height: 3rem;
  border-radius: 0.75rem;
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  padding: 0 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  placeholder-color: #9ca3af;
  transition: all 0.3s;
}
.input:focus {
  border-color: #0f766e;
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.3);
  outline: none;
}
</style>
