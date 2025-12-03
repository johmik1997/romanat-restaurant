<template>
  <div
    id="app"
    class="font-display bg-background-light dark:bg-background-dark min-h-screen"
  >
      <router-view />
  </div>
</template>

<script>
import DefaultLayout from "../layouts/DefaultLayout.vue";

export default {
  name: "StaffHomePage",
  components: { DefaultLayout },
};
</script>
