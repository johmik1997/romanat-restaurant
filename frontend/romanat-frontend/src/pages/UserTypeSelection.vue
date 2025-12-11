<template>
  <div class="user-selection-container">
    <div class="container-wrapper">
      <!-- Welcome Header with Hotel Info -->
      <div class="welcome-section">
        <div class="welcome-content">
          <h1 class="main-title">
            Welcome to <span class="title-highlight">Romanat Restaurant</span>
          </h1>
          <p class="main-subtitle">
            Experience luxury hospitality with world-class amenities and personalized service
          </p>
          
          <div class="hotel-brief">
            <div class="brief-item">
              <span class="brief-icon">⭐</span>
              <span class="brief-text">5-Star Luxury Hotel</span>
            </div>
            <div class="brief-item">
              <span class="brief-icon">📍</span>
              <span class="brief-text">City Center Location</span>
            </div>
            <div class="brief-item">
              <span class="brief-icon">🏆</span>
              <span class="brief-text">Since 1995</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Main Content Grid -->
      <div class="main-grid">
        <!-- Left Column: Hotel Information -->
        <div class="info-column">
          <div class="info-card">
            <div class="info-card-header">
              <h3 class="info-card-title">
                <span class="material-icons-outlined">info</span>
                About Romanat
              </h3>
            </div>
            
            <div class="info-card-content">
              <p class="info-text">
                Welcome to Romanat Restaurant, where luxury meets comfort. We pride ourselves on delivering exceptional experiences with our premium accommodations, exquisite dining, and impeccable service.
              </p>
              
              <div class="features-grid">
                <div class="feature-card">
                  <div class="feature-icon-wrapper">
                    <span class="material-icons-outlined">hotel</span>
                  </div>
                  <div class="feature-content">
                    <h4 class="feature-title">Premium Rooms</h4>
                    <p class="feature-description">120+ luxurious rooms & suites</p>
                  </div>
                </div>
                
                <div class="feature-card">
                  <div class="feature-icon-wrapper">
                    <span class="material-icons-outlined">restaurant</span>
                  </div>
                  <div class="feature-content">
                    <h4 class="feature-title">Fine Dining</h4>
                    <p class="feature-description">4 award-winning restaurants</p>
                  </div>
                </div>
                
                <div class="feature-card">
                  <div class="feature-icon-wrapper">
                    <span class="material-icons-outlined">spa</span>
                  </div>
                  <div class="feature-content">
                    <h4 class="feature-title">Spa & Wellness</h4>
                    <p class="feature-description">Full-service spa & fitness center</p>
                  </div>
                </div>
                
                <div class="feature-card">
                  <div class="feature-icon-wrapper">
                    <span class="material-icons-outlined">groups</span>
                  </div>
                  <div class="feature-content">
                    <h4 class="feature-title">Events</h4>
                    <p class="feature-description">Weddings & conferences</p>
                  </div>
                </div>
              </div>
              
              <div class="contact-info">
                <div class="contact-item">
                  <span class="material-icons-outlined contact-icon">phone</span>
                  <div class="contact-details">
                    <span class="contact-label">24/7 Support</span>
                    <span class="contact-value">+1 (555) 123-4567</span>
                  </div>
                </div>
                
                <div class="contact-item">
                  <span class="material-icons-outlined contact-icon">email</span>
                  <div class="contact-details">
                    <span class="contact-label">Email</span>
                    <span class="contact-value">hello@romanat.com</span>
                  </div>
                </div>
                
                <div class="contact-item">
                  <span class="material-icons-outlined contact-icon">schedule</span>
                  <div class="contact-details">
                    <span class="contact-label">Check-in/out</span>
                    <span class="contact-value">3 PM / 12 PM</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: User Selection -->
        <div class="selection-column">
          <div class="selection-header">
            <h2 class="selection-title">Select Your Role</h2>
            <p class="selection-subtitle">
              Choose your role to access personalized features and services
            </p>
          </div>

          <div class="cards-grid">
            <!-- Guest Card -->
            <div 
              class="card guest-card"
              @click="selectUserType('guest')"
              @mouseenter="hoveredCard = 'guest'"
              @mouseleave="hoveredCard = null"
            >
              <div class="card-gradient-overlay guest-overlay"></div>
              
              <div class="decorative-circle guest-circle"></div>
              
              <div class="card-content">
                <div class="card-icon guest-icon">
                  <span class="material-icons-outlined icon-inner guest-icon-inner">
                    person
                  </span>
                </div>

                <h3 class="card-title">Guest</h3>
                <p class="card-description">
                  Book rooms, manage reservations, and enjoy our premium hospitality services.
                </p>

                <ul class="features-list">
                  <li class="feature-item">
                    <span class="material-icons-outlined feature-icon">check_circle</span>
                    Room bookings
                  </li>
                  <li class="feature-item">
                    <span class="material-icons-outlined feature-icon">check_circle</span>
                    Reservation management
                  </li>
                  <li class="feature-item">
                    <span class="material-icons-outlined feature-icon">check_circle</span>
                    Amenity access
                  </li>
                </ul>

                <div class="cta-container">
                  <span class="cta-text guest-text">Continue as Guest</span>
                  <div class="cta-button guest-button">
                    <span class="material-icons-outlined cta-icon guest-button-icon">
                      arrow_forward
                    </span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Staff Card -->
            <div 
              class="card staff-card"
              @click="selectUserType('staff')"
              @mouseenter="hoveredCard = 'staff'"
              @mouseleave="hoveredCard = null"
            >
              <div class="card-gradient-overlay staff-overlay"></div>
              
              <div class="decorative-circle staff-circle"></div>
              
              <div class="card-content">
                <div class="card-icon staff-icon">
                  <span class="material-icons-outlined icon-inner staff-icon-inner">
                    admin_panel_settings
                  </span>
                </div>

                <h3 class="card-title">Staff Member</h3>
                <p class="card-description">
                  Access the staff dashboard to manage hotel operations efficiently.
                </p>

                <ul class="features-list">
                  <li class="feature-item">
                    <span class="material-icons-outlined feature-icon">check_circle</span>
                    Manage reservations
                  </li>
                  <li class="feature-item">
                    <span class="material-icons-outlined feature-icon">check_circle</span>
                    Guest management
                  </li>
                  <li class="feature-item">
                    <span class="material-icons-outlined feature-icon">check_circle</span>
                    Administrative tools
                  </li>
                </ul>

                <div class="cta-container">
                  <span class="cta-text staff-text">Staff Login</span>
                  <div class="cta-button staff-button">
                    <span class="material-icons-outlined cta-icon staff-button-icon">
                      arrow_forward
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div class="footer">
        <div class="footer-content">
          <p class="footer-text">
            Need assistance? Contact our support team at 
            <a href="mailto:support@romanat.com" class="support-link">
              support@romanat.com
            </a>
          </p>
          
          <div class="social-links">
            <a href="#" class="social-link">
              <span class="material-icons-outlined">facebook</span>
            </a>
            <a href="#" class="social-link">
              <span class="material-icons-outlined">camera_alt</span>
            </a>
            <a href="#" class="social-link">
              <span class="material-icons-outlined">chat_bubble</span>
            </a>
            <a href="#" class="social-link">
              <span class="material-icons-outlined">linkedin</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Loading Overlay -->
      <div v-if="loading" class="loading-overlay">
        <div class="loading-content">
          <div class="loading-spinner"></div>
          <p class="loading-text">Redirecting...</p>
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

<style scoped>
/* Container styles */
.user-selection-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem 1rem;
}

.container-wrapper {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}

/* Welcome Section */
.welcome-section {
  text-align: center;
  margin-bottom: 3rem;
  padding: 0 1rem;
}

.welcome-content {
  max-width: 800px;
  margin: 0 auto;
}

.main-title {
  font-size: 2.75rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 1rem;
  line-height: 1.2;
}

@media (min-width: 768px) {
  .main-title {
    font-size: 3.5rem;
  }
}

.title-highlight {
  background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.main-subtitle {
  font-size: 1.25rem;
  color: #64748b;
  margin-bottom: 2rem;
  line-height: 1.6;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hotel-brief {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.brief-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: white;
  border-radius: 50px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  font-weight: 500;
  color: #475569;
}

.brief-icon {
  font-size: 1.25rem;
}

/* Main Grid Layout */
.main-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

@media (min-width: 1024px) {
  .main-grid {
    grid-template-columns: 1fr 1.2fr;
    gap: 4rem;
  }
}

/* Left Column - Hotel Information */
.info-column {
  order: 2;
}

@media (min-width: 1024px) {
  .info-column {
    order: 1;
  }
}

.info-card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  height: 100%;
}

.info-card-header {
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  padding: 1.75rem 2rem;
}

.info-card-title {
  color: white;
  font-size: 1.5rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin: 0;
}

.info-card-title .material-icons-outlined {
  font-size: 1.75rem;
}

.info-card-content {
  padding: 2rem;
}

.info-text {
  color: #64748b;
  line-height: 1.7;
  margin-bottom: 2rem;
  font-size: 1.05rem;
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.25rem;
  margin-bottom: 2.5rem;
}

@media (min-width: 640px) {
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.feature-card {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.25rem;
  background: #f8fafc;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
  cursor: default;
}

.feature-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #cbd5e1;
}

.feature-icon-wrapper {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.feature-icon-wrapper .material-icons-outlined {
  font-size: 1.5rem;
}

.feature-content {
  flex: 1;
}

.feature-title {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.feature-description {
  font-size: 0.875rem;
  color: #64748b;
  line-height: 1.5;
}

/* Contact Info */
.contact-info {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  background: #f8fafc;
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.contact-icon {
  width: 40px;
  height: 40px;
  background: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2563eb;
  flex-shrink: 0;
  border: 1px solid #e2e8f0;
}

.contact-details {
  display: flex;
  flex-direction: column;
}

.contact-label {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.125rem;
}

.contact-value {
  font-weight: 500;
  color: #1e293b;
}

/* Right Column - User Selection */
.selection-column {
  order: 1;
}

@media (min-width: 1024px) {
  .selection-column {
    order: 2;
  }
}

.selection-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.selection-title {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.75rem;
}

.selection-subtitle {
  color: #64748b;
  font-size: 1.125rem;
  max-width: 500px;
  margin: 0 auto;
}

/* Cards Grid */
.cards-grid {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .cards-grid {
    gap: 2rem;
  }
}

/* Card Styles - Updated */
.card {
  position: relative;
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid transparent;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  border-color: #e2e8f0;
}

.card-content {
  position: relative;
  padding: 2rem;
}

/* Card-specific gradients */
.guest-card {
  background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
}

.staff-card {
  background: linear-gradient(135deg, #ffffff 0%, #f5f3ff 100%);
}

/* Gradient overlays */
.card-gradient-overlay {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.guest-overlay {
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
}

.staff-overlay {
  background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
}

.card:hover .card-gradient-overlay {
  opacity: 0.05;
}

/* Decorative circles */
.decorative-circle {
  position: absolute;
  top: 0;
  right: 0;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  transform: translate(50px, -50px);
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.guest-circle {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
}

.staff-circle {
  background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
}

.card:hover .decorative-circle {
  transform: translate(50px, -50px) scale(1.1);
}

/* Card icon */
.card-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}

.guest-icon {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
}

.staff-icon {
  background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
}

.card:hover .guest-icon {
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
}

.card:hover .staff-icon {
  background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
}

.icon-inner {
  font-size: 2rem;
  transition: color 0.3s ease;
}

.guest-icon-inner {
  color: #2563eb;
}

.staff-icon-inner {
  color: #7c3aed;
}

.card:hover .icon-inner {
  color: white;
}

/* Card content */
.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.75rem;
}

.card-description {
  color: #64748b;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

/* Features list */
.features-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 2rem;
}

.feature-item {
  display: flex;
  align-items: center;
  color: #475569;
  font-size: 0.95rem;
}

.feature-icon {
  color: #10b981;
  font-size: 1.125rem;
  margin-right: 0.75rem;
  flex-shrink: 0;
}

/* CTA */
.cta-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
}

.cta-text {
  font-weight: 600;
  font-size: 1.125rem;
}

.guest-text {
  color: #2563eb;
}

.staff-text {
  color: #7c3aed;
}

.cta-button {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.guest-button {
  background: #dbeafe;
}

.staff-button {
  background: #e0e7ff;
}

.card:hover .guest-button {
  background: #2563eb;
}

.card:hover .staff-button {
  background: #7c3aed;
}

.cta-icon {
  transition: color 0.3s ease;
}

.guest-button-icon {
  color: #2563eb;
}

.staff-button-icon {
  color: #7c3aed;
}

.card:hover .cta-icon {
  color: white;
}

/* Footer */
.footer {
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid #e2e8f0;
}

.footer-content {
  text-align: center;
}

.footer-text {
  color: #64748b;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
}

.support-link {
  color: #2563eb;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

.support-link:hover {
  color: #1d4ed8;
  text-decoration: underline;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: #f1f5f9;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-link:hover {
  background: #2563eb;
  color: white;
  transform: translateY(-2px);
}

/* Loading Overlay */
.loading-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
  backdrop-filter: blur(4px);
}

.loading-content {
  background: white;
  border-radius: 16px;
  padding: 3rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.loading-spinner {
  animation: spin 1s linear infinite;
  border-radius: 50%;
  height: 48px;
  width: 48px;
  border: 3px solid #e2e8f0;
  border-top-color: #2563eb;
  margin-bottom: 1.5rem;
}

.loading-text {
  color: #475569;
  font-weight: 500;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Material Icons sizing fix */
:deep(.material-icons-outlined) {
  font-size: inherit;
}
</style>