<template>
  <section id="experiences" class="w-full bg-white py-20">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold sm:text-4xl font-serif text-primary">Unforgettable Experiences</h2>
        <p class="mt-4 text-lg text-gray-600">
          Indulge in luxury with our curated services and unique amenities designed for your ultimate comfort.
        </p>
      </div>
      <div class="mx-auto mt-12 grid max-w-2xl grid-cols-1 gap-8 sm:mt-16 lg:max-w-none lg:grid-cols-4">
        <div 
          v-for="experience in experiences" 
          :key="experience.id"
          class="bg-background-light rounded-2xl p-6 text-center shadow-md hover:shadow-lg transition-shadow duration-300"
        >
          <div class="h-16 w-16 mx-auto bg-primary/10 text-primary rounded-full flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-3xl">{{ experience.icon }}</span>
          </div>
          <h3 class="text-xl font-bold text-gray-800 mb-2">{{ experience.title }}</h3>
          <p class="text-gray-600">{{ experience.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const experiences = ref([
  {
    id: 1,
    icon: 'spa',
    title: 'Rejuvenating Spa',
    description: 'Unwind and revitalize with our signature spa treatments using natural ingredients.'
  },
  {
    id: 2,
    icon: 'restaurant',
    title: 'Gourmet Dining',
    description: 'Savor exquisite dishes prepared by our world-class chefs using locally sourced ingredients.'
  },
  {
    id: 3,
    icon: 'pool',
    title: 'Infinity Pool',
    description: 'Soak up the sun with stunning ocean views from our temperature-controlled rooftop pool.'
  },
  {
    id: 4,
    icon: 'tour',
    title: 'City Tours',
    description: 'Explore the best of the city with our exclusive guided tours and personalized itineraries.'
  }
])
</script>