<template>
<section class="bg-primary/10 dark:bg-primary/20 py-16 sm:py-24">
  <div class="mx-auto max-w-7xl px-6 lg:px-8 text-center">
    <h2 class="text-3xl font-bold sm:text-4xl">Special Offers</h2>
    <p class="mt-4 text-lg text-gray-600 dark:text-gray-300">Take advantage of our exclusive deals and seasonal promotions.</p>
    <div class="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
      <OfferCard
        title="Weekend Getaway"
        description="Book a 2-night stay and enjoy complimentary breakfast."
        image="https://source.unsplash.com/400x300/?hotel,room"
      />
      <OfferCard
        title="Spa Retreat"
        description="Relax with 20% off all spa services this month."
        image="https://source.unsplash.com/400x300/?spa,relax"
      />
      <OfferCard
        title="Family Package"
        description="Kids stay free with every booking of 2 adults."
        image="https://source.unsplash.com/400x300/?family,vacation"
      />
    </div>
  </div>
</section>
</template>

<script setup>
import OfferCard from './OfferCard.vue'
</script>
