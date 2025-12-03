<template>
<div class="bg-background text-[#111418] font-display">
<Header />
<main>
<slot />
</main>
<FooterSection />
</div>
</template>


<script setup>
import Header from '../components/Landing/Header.vue'
import FooterSection from '../components/Landing/FooterSection.vue'
</script>