<template>
  <div class="login-container">
    <!-- Background -->
    <div 
      class="background-image"
      :style="{ backgroundImage: `url('${backgroundImage}')` }"
    ></div>

    <!-- Soft Dark Overlay -->
    <div class="background-overlay"></div>

    <!-- Login Card -->
    <div class="login-card">

      <!-- Logo -->
      <div class="logo-container">
        <div class="logo-icon">
          <svg fill="none" stroke="currentColor" stroke-width="1.3" viewBox="0 0 24 24">
            <path d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21"/>
          </svg>
        </div>
        <p class="logo-text">
          Romanat
        </p>
      </div>

      <!-- Heading -->
      <div class="heading-container">
        <h1 class="heading-title">Welcome Back</h1>
        <p class="heading-subtitle">Access your reservations and manage your stay</p>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleLogin" class="login-form">

        <!-- Username -->
        <div class="form-group">
          <label class="form-label">Username</label>
          <div class="input-container">
            <input 
              v-model="form.username"
              type="text"
              placeholder="Enter username"
              class="form-input"
            />
          </div>
        </div>

        <!-- Password -->
        <div class="form-group">
          <label class="form-label">Password</label>
          <div class="input-container">
            <input 
              v-model="form.password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="••••••••"
              class="form-input"
            />
            <button 
              type="button"
              @click="showPassword = !showPassword"
              class="password-toggle"
            >
              <svg v-if="!showPassword" class="eye-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              <svg v-else class="eye-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>
              </svg>
            </button>
          </div>
        </div>

        <!-- Error Message -->
        <div 
          v-if="error"
          class="error-message"
        >
          <svg class="error-icon" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
          </svg>
          <span>{{ error }}</span>
        </div>

        <!-- Login Button -->
        <button 
          type="submit"
          :disabled="loading"
          class="login-button"
        >
          <svg 
            v-if="loading"
            class="loading-spinner"
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
      <div class="signup-link">
        Don't have an account?
        <router-link to="/signup" class="signup-text">
          Sign Up
        </router-link>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authenticate } from '../api/auth/loginApi.js'
import { save as stor } from '../localStorage/index.js'

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

  loading.value = true
  error.value = ''

  try {
    const data = await authenticate(form.value)

    // Save user data to localStorage
    await stor('logged_in_user', {
      access_token: data.access,
      refresh_token: data.refresh,
      username: form.value.username,
      is_admin: data.is_admin || false,
      requiresReset: data.requiresReset || false,
      id: data.id,
      roleName: data.role.name,
      // Save additional role info if available
      role: data.role,
      permissions: data.permissions || []
    })

    // Clear form
    form.value.username = ''
    form.value.password = ''

    // Redirect based on role
    await redirectBasedOnRole(data.role.name)

  } catch (err) {
    error.value = err.detail || 'Invalid username or password.'
    console.error('Login error:', err)
  } finally {
    loading.value = false
  }
}

const redirectBasedOnRole = async (roleName) => {
  // Wait a moment to ensure localStorage is updated
  await new Promise(resolve => setTimeout(resolve, 100))
  
  switch(roleName.toLowerCase()) {
    case 'receptionist':
    case 'manager':
    case 'admin':
      // Redirect to staff home page which will handle dashboard redirection
      router.push('/staff')
      break
    case 'customer':
    case 'guest':
      // Redirect to guest home page
      router.push('/guest')
      break
    default:
      // Default fallback - redirect to user type selection
      console.warn('Unknown role:', roleName, 'redirecting to home')
      router.push('/')
  }
}
</script>

<style scoped>
/* Container styles */
.login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
  background-color: #334f4f;
}

.background-image {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0.4;
}

.background-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7));
  backdrop-filter: blur(4px);
}

/* Login card */
.login-card {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: 28rem;
  padding: 2.5rem;
  border-radius: 1.5rem;
  background-color: rgba(0, 0, 0, 0.3);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Logo */
.logo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
}

.logo-icon {
  height: 3.5rem;
  width: 3.5rem;
  color: #0f766e;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.3));
  animation: float 3s ease-in-out infinite;
}

.logo-text {
  margin-top: 1rem;
  font-size: 1.5rem;
  font-weight: 600;
  color: white;
  letter-spacing: 0.025em;
}

/* Heading */
.heading-container {
  text-align: center;
  margin-bottom: 2.5rem;
}

.heading-title {
  font-size: 1.875rem;
  font-weight: 700;
  color: white;
  margin-bottom: 0.25rem;
}

.heading-subtitle {
  color: #9ca3af;
}

/* Form */
.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  display: block;
  font-size: 0.875rem;
  color: #d1d5db;
  margin-bottom: 0.5rem;
}

.input-container {
  position: relative;
}

.form-input {
  width: 100%;
  height: 3rem;
  border-radius: 0.75rem;
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  padding: 0 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.form-input::placeholder {
  color: #9ca3af;
}

.form-input:focus {
  outline: none;
  border-color: rgba(15, 118, 110, 0.5);
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.3);
}

.password-toggle {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  transition: color 0.3s;
}

.password-toggle:hover {
  color: white;
}

.eye-icon {
  width: 1.25rem;
  height: 1.25rem;
}

/* Error message */
.error-message {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #f87171;
  font-size: 0.875rem;
  background-color: rgba(248, 113, 113, 0.1);
  padding: 0.75rem;
  border: 1px solid rgba(248, 113, 113, 0.2);
  border-radius: 0.5rem;
}

.error-icon {
  width: 1rem;
  height: 1rem;
}

/* Login button */
.login-button {
  width: 100%;
  height: 3rem;
  border-radius: 0.75rem;
  background-color: #0f766e;
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.login-button:hover:not(:disabled) {
  background-color: #0d5d56;
}

.login-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.loading-spinner {
  width: 1.25rem;
  height: 1.25rem;
  animation: spin 1s linear infinite;
}

/* Sign up link */
.signup-link {
  margin-top: 2rem;
  text-align: center;
  color: #9ca3af;
  font-size: 0.875rem;
}

.signup-text {
  color: #0f766e;
  margin-left: 0.25rem;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.3s;
}

.signup-text:hover {
  text-decoration: underline;
  color: #0d5d56;
}

/* Animations */
@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-5px);
  }
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Smooth transitions */
button,
input,
a {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>