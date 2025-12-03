<template>
  <div id="app" class="font-display bg-background-light dark:bg-background-dark text-[#333333] dark:text-gray-200 min-h-screen">
        <!-- <LandingLayout> -->
          <router-view />
        <!-- </LandingLayout> -->
          </div>
</template>

<script>
import LandingLayout from '../layouts/LandingLayout.vue';

export default {
  name: 'GuestHomePage',
  components: {
    LandingLayout
  }
}
</script>