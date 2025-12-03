<template>
  <div id="app" class="font-display bg-background-light dark:bg-background-dark text-[#333333] dark:text-gray-200 min-h-screen">
  <component :is="layout">
    <router-view />
</component>

  </div>
</template>

<script>
import DefaultLayout from './layouts/DefaultLayout.vue'
import LandingLayout from './layouts/LandingLayout.vue'
import AuthLayout from './layouts/AuthLayout.vue'
import EmptyLayout from './layouts/EmptyLayout.vue'

export default {
  name: 'App',
  components: {
    DefaultLayout,
    LandingLayout,
    AuthLayout,
    EmptyLayout
  },
  computed: {
layout() {
  const layout = this.$route.meta.layout || "EmptyLayout";
  return layout; // return actual component name, NOT "-layout"
}


  }
}
</script>