<template>
  <div class="auth-layout">
    <!-- Background Decorations -->
    <div class="background-circle circle-left"></div>
    <div class="background-circle circle-right"></div>
    
    <!-- Main Content -->
    <div class="main-container">
      <!-- Left Side - Brand/Info -->
      <div class="left-side">
        <!-- Background Pattern -->
        <div class="pattern-overlay">
          <div class="pattern-circle circle-1"></div>
          <div class="pattern-circle circle-2"></div>
          <div class="pattern-circle circle-3"></div>
        </div>
        
        <div class="left-content">
          <!-- Logo/Brand -->
          <div class="brand-section">
            <div class="logo-container">
              <div class="logo-icon">
                <span class="material-icons-outlined">hotel</span>
              </div>
              <span class="brand-name">Romanat Restaurant</span>
            </div>
            
            <h1 class="welcome-title">
              Welcome to<br>Your Perfect Stay
            </h1>
            <p class="welcome-description">
              Experience luxury and comfort like never before. Join thousands of satisfied guests who trust us for their perfect getaway.
            </p>
          </div>

          <!-- Features List -->
          <div class="features-list">
            <div v-for="feature in features" :key="feature.text" class="feature-item">
              <div class="feature-icon">
                <span class="material-icons-outlined">check</span>
              </div>
              <span class="feature-text">{{ feature.text }}</span>
            </div>
          </div>

          <!-- Testimonial -->
          <div class="testimonial-card">
            <p class="testimonial-text">
              "The best hotel experience I've ever had. The staff went above and beyond to make our stay memorable."
            </p>
            <div class="testimonial-author">
              <div class="author-avatar"></div>
              <div>
                <p class="author-name">Sarah Johnson</p>
                <p class="author-title">Regular Guest</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Side - Auth Form -->
      <div class="right-side">
        <!-- Mobile Logo -->
        <div class="mobile-logo">
          <div class="mobile-logo-container">
            <div class="mobile-logo-icon">
              <span class="material-icons-outlined">hotel</span>
            </div>
            <span class="mobile-brand-name">Romanat Restaurant</span>
          </div>
        </div>

        <!-- Back Button -->
        <button 
          @click="goBack"
          class="back-button"
        >
          <span class="material-icons-outlined">arrow_back</span>
          <span>Back to home</span>
        </button>

        <!-- Auth Content -->
        <div class="auth-content">
          <slot />
        </div>

        <!-- Footer -->
        <div class="footer">
          <p class="footer-text">
            © 2024 Romanat Restaurant. All rights reserved.
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
/* Main container */
.auth-layout {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  position: relative;
  overflow: hidden;
  background: linear-gradient(135deg, #eff6ff 0%, #e0e7ff 100%);
  color: #1f2937;
}

/* Background circles */
.background-circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.5;
}

.circle-left {
  top: 0;
  left: 0;
  width: 18rem;
  height: 18rem;
  background-color: #bfdbfe;
  transform: translate(-50%, -50%);
}

.circle-right {
  bottom: 0;
  right: 0;
  width: 24rem;
  height: 24rem;
  background-color: #c7d2fe;
  transform: translate(50%, 50%);
}

/* Main container */
.main-container {
  position: relative;
  width: 100%;
  max-width: 72rem;
  display: flex;
  background-color: white;
  border-radius: 1.5rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  overflow: hidden;
}

/* Left side */
.left-side {
  display: none;
  flex: 1;
  background: linear-gradient(135deg, rgba(15, 118, 110, 0.3), rgba(15, 118, 110, 0.9));
  color: white;
  padding: 3rem;
  position: relative;
  overflow: hidden;
}

@media (min-width: 1024px) {
  .left-side {
    display: flex;
  }
}

.pattern-overlay {
  position: absolute;
  inset: 0;
  opacity: 0.1;
}

.pattern-circle {
  position: absolute;
  border: 2px solid white;
  border-radius: 50%;
}

.circle-1 {
  top: 2.5rem;
  left: 2.5rem;
  width: 5rem;
  height: 5rem;
}

.circle-2 {
  top: 8rem;
  right: 4rem;
  width: 3rem;
  height: 3rem;
}

.circle-3 {
  bottom: 5rem;
  left: 5rem;
  width: 4rem;
  height: 4rem;
}

.left-content {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

/* Brand section */
.brand-section {
  margin-bottom: 2rem;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 2rem;
}

.logo-icon {
  width: 3rem;
  height: 3rem;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-icon .material-icons-outlined {
  font-size: 1.5rem;
}

.brand-name {
  font-size: 1.5rem;
  font-weight: 700;
}

.welcome-title {
  font-size: 2.25rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.welcome-description {
  color: #dbeafe;
  font-size: 1.125rem;
  line-height: 1.75;
}

/* Features list */
.features-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.feature-icon {
  width: 2rem;
  height: 2rem;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.feature-icon .material-icons-outlined {
  font-size: 0.875rem;
}

.feature-text {
  color: #dbeafe;
  font-size: 0.875rem;
}

/* Testimonial */
.testimonial-card {
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 1.5rem;
  backdrop-filter: blur(4px);
}

.testimonial-text {
  color: #dbeafe;
  font-style: italic;
  margin-bottom: 1rem;
  line-height: 1.5;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.author-avatar {
  width: 2.5rem;
  height: 2.5rem;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
}

.author-name {
  font-weight: 600;
  font-size: 0.875rem;
}

.author-title {
  color: #dbeafe;
  font-size: 0.75rem;
}

/* Right side */
.right-side {
  flex: 1;
  padding: 2rem;
}

@media (min-width: 1024px) {
  .right-side {
    padding: 3rem;
  }
}

/* Mobile logo */
.mobile-logo {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 2rem;
}

@media (min-width: 1024px) {
  .mobile-logo {
    display: none;
  }
}

.mobile-logo-container {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.mobile-logo-icon {
  width: 2.5rem;
  height: 2.5rem;
  background-color: #0f766e;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mobile-logo-icon .material-icons-outlined {
  color: white;
  font-size: 1.25rem;
}

.mobile-brand-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
}

/* Back button */
.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #4b5563;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  margin-bottom: 2rem;
  font-size: 0.875rem;
  transition: color 0.3s ease;
}

.back-button:hover {
  color: #1f2937;
}

.back-button .material-icons-outlined {
  font-size: 1.125rem;
}

/* Auth content */
.auth-content {
  max-width: 28rem;
  margin-left: auto;
  margin-right: auto;
}

/* Footer */
.footer {
  margin-top: 3rem;
  text-align: center;
}

.footer-text {
  color: #4b5563;
  font-size: 0.75rem;
}

/* Material icons */
.material-icons-outlined {
  font-family: 'Material Icons Outlined';
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  -webkit-font-feature-settings: 'liga';
  -webkit-font-smoothing: antialiased;
}

/* Smooth transitions */
button,
a {
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