<template>
  <div class="flex">

    <!-- Sidebar -->
    <Sidebar
      class="fixed top-0 left-0 h-screen w-64 bg-white shadow-md border-r"
    />

    <!-- Main content -->
    <div class="flex flex-col flex-1 ml-64 min-h-screen">

      <!-- Header -->
      <header
        class="h-16 bg-white border-b shadow-sm flex items-center justify-between px-6 sticky top-0 z-40"
      >
        <!-- Dynamic Title -->
        <h1 class="text-xl font-semibold text-gray-800">
          <!-- {{ title }} -->
        </h1>

        <!-- Right side icons -->
        <div class="flex items-center gap-6">

          <!-- Notifications -->
          <button class="relative hover:text-black">
            <span class="material-symbols-outlined text-gray-600 text-2xl">
              notifications
            </span>
            <span
              class="absolute -top-1 -right-1 bg-red-600 text-white text-xs px-1 rounded-full"
            >3</span>
          </button>

          <!-- Profile dropdown -->
          <div class="relative">
            <button
              @click="toggleDropdown"
              class="flex items-center gap-2 focus:outline-none"
            >
              <img
                src="https://i.pravatar.cc/40"
                class="w-10 h-10 rounded-full border"
              />
              <span class="material-symbols-outlined text-gray-600">
                expand_more
              </span>
            </button>

            <!-- Dropdown Menu -->
            <div
              v-if="dropdownOpen"
              class="absolute right-0 mt-2 bg-white text-black border rounded-lg shadow-lg w-48 py-2"
            >
              <router-link
                to="/profile"
                class="block px-4 py-2 hover:bg-gray-100"
              >
                Profile
              </router-link>

              <router-link
                to="/settings"
                class="block px-4 py-2 hover:bg-gray-100"
              >
                Settings
              </router-link>

              <hr />

              <button
                @click="logout"
                class="block w-full text-left px-4 py-2 hover:bg-gray-100"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </header>

      <!-- Page content -->
      <main class="p-8">
        <slot></slot>
      </main>

    </div>
  </div>
</template>

<script>
import Sidebar from '../components/staffs/Sidebar.vue'

export default {
  name: 'DefaultLayout',

  components: { Sidebar },

  props: {
    title: {
      type: String,
      default: "Dashboard",
    },
  },

  data() {
    return {
      dropdownOpen: false,
    }
  },

  methods: {
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen
    },

    logout() {
      // You can replace with real logout logic
      console.log("Logging out...")
      this.$router.push("/login")
    },
  },

  mounted() {
    // Close dropdown if clicked outside
    window.addEventListener("click", (e) => {
      if (!this.$el.contains(e.target)) {
        this.dropdownOpen = false
      }
    })
  }
}
</script>
