<template>
  <aside class="fixed w-64 h-screen bg-white border-r border-gray-200 flex flex-col">
    
    <!-- Brand / User Section -->
    <div class="flex items-center gap-3 p-6 border-b border-gray-200">
      <div
        class="size-12 bg-center bg-cover rounded-full border border-gray-300"
        :style="{ backgroundImage: `url(${profileImage})` }"
      ></div>

      <div class="min-w-0 flex-1">
        <h1 class="text-gray-900 text-base font-semibold truncate">{{ hotelName }}</h1>
        <p class="text-gray-500 text-sm truncate">{{ userRole }}</p>
      </div>
    </div>

    <!-- Main Navigation -->
    <nav class="flex-1 p-4">
      <div class="flex flex-col gap-1 h-full">
        <!-- Main Links - role-based -->
        <div class="flex-1">
          <router-link
            v-for="item in filteredNavItems"
            :key="item.name"
            :to="item.href"
            class="flex items-center gap-3 px-3 py-2 rounded-lg transition-all duration-200 mb-1"
            :class="isActive(item.href)
              ? 'bg-blue-50 text-blue-700 border border-blue-200 font-semibold'
              : 'text-gray-700 hover:bg-gray-50 hover:text-gray-900'"
          >
            <span class="material-symbols-outlined text-xl flex-shrink-0">{{ item.icon }}</span>
            <span class="text-sm font-medium">{{ item.name }}</span>
          </router-link>
        </div>
<div class="mt-auto pt-6 border-t border-gray-200">
  <div
    v-for="item in secondaryNavItems"
    :key="item.name"
    class="flex items-center gap-3 px-3 py-2 rounded-lg transition-all duration-200 cursor-pointer mb-1
           text-gray-600 hover:bg-gray-50 hover:text-gray-900"
    @click="handleClick(item)">
      <span class="material-symbols-outlined text-xl flex-shrink-0">{{ item.icon }}</span>
      <span class="text-sm font-medium">{{ item.name }}</span>
    </div>
  </div>

      </div>
    </nav>
  </aside>
</template>

<script>
import { get as getFromStore, load, remove } from "../../localStorage";

export default {
  name: "Sidebar",

  data() {
    return {
      hotelName: "Romanat Restaurant",
      userRole: null,
      profileImage: "https://lh3.googleusercontent.com/...",

      mainNavItems: [
        { name: "Manager Dashboard", href: "/staff/manager/dashboard", icon: "admin_panel_settings", roles: ["Manager","Admin"] },
        { name: "Dashboard", href: "/staff/receptionist/dashboard", icon: "dashboard", roles: ["Receptionist"] },
        { name: "Reservations", href: "/staff/reservation", icon: "calendar_month", roles: ["Receptionist", "Manager"] },
        { name: "Guests", href: "/staff/guests", icon: "group", roles: ["Receptionist", "Manager"] },
        { name: "Rooms", href: "/staff/rooms", icon: "bed", roles: ["Manager"] },
        { name: "Reports", href: "/staff/report", icon: "bar_chart", roles: ["Manager"] },
        { name: "User Management", href: "/staff/user", icon: "admin_panel_settings", roles: ["Manager", "Admin"] }
      ],

      secondaryNavItems: [
        { name: "Settings", href: "/staff/settings", icon: "settings" },
        { name: "Help & Support", href: "/staff/help", icon: "help" },
        { name: "Log Out", action: "logout", icon: "logout" } // 👈 FIXED
      ]
    };
  },

  computed: {
    filteredNavItems() {
      if (!this.userRole) return [];
      return this.mainNavItems.filter(item => item.roles.includes(this.userRole));
    }
  },

  async created() {
    const stored = await load("logged_in_user");

    if (stored && stored.roleName) {
      this.userRole = stored.roleName;
    } else {
      this.userRole = "Receptionist"; // default fallback
    }
  },

  methods: {
    isActive(route) {
      return this.$route.path === route || this.$route.path.startsWith(route);
    },

    async handleClick(item) {
      if (item.action === "logout") {
        await remove("logged_in_user"); // remove from localStorage + reactive store
        this.$router.push("/login");    // redirect to login
      } else if (item.href) {
        this.$router.push(item.href);
      }
    }
  }
};
</script>




<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}
</style>
