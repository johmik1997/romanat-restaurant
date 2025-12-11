<template>
  <div v-if="loading" class="loading-screen">
    <div class="loading-spinner"></div>
    <p>Loading dashboard...</p>
  </div>
    <router-view />
</template>

<script>
import DefaultLayout from "../layouts/DefaultLayout.vue";

export default {
  name: "StaffHomePage",
  components: { DefaultLayout },
  data() {
    return {
      loading: true,
      userRole: 'receptionist' // Default role - you'll need to get this from login
    }
  },
  mounted() {
    // Try to get user role from localStorage or wherever it's stored
    this.getUserRole();
    this.checkAndRedirect();
  },
  methods: {
    getUserRole() {
      // Try to get role from localStorage (adjust based on your auth system)
      const userData = localStorage.getItem('logged_in_user');
      if (userData) {
        try {
          const user = JSON.parse(userData);
          this.userRole = user.roleName || 'Receptionist';
          console.log(this.userRole);
          
        } catch (e) {
          console.error('Error parsing user data:', e);
          this.userRole = 'receptionist';
        }
      }
      
      // For testing - you can set role manually here
      // this.userRole = 'manager'; // Uncomment to test manager role
      // this.userRole = 'admin';   // Uncomment to test admin role
    },
    
    checkAndRedirect() {
      const currentPath = this.$route.path;
      
      // If we're at the base /staff path, redirect based on role
      if (currentPath === '/staff' || currentPath === '/staff/') {
        switch(this.userRole) {
          case 'Manager':
          case 'admin':
            this.$router.replace('/staff/manager/dashboard');
            break;
          case 'receptionist':
          default:
            this.$router.replace('/staff/receptionist/dashboard');
            break;
        }
      }
      
      // Hide loading after a short delay (even if no redirect happened)
      setTimeout(() => {
        this.loading = false;
      }, 500);
    }
  }
};
</script>

<style scoped>
.loading-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.loading-spinner {
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top: 4px solid white;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>