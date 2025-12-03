<template>
  <section class="py-16 bg-gradient-to-r from-primary to-teal-800 text-white">
    <div class="container mx-auto max-w-4xl px-4 text-center">
      <h2 class="text-3xl font-bold font-serif mb-4">Ready for Your Dream Getaway?</h2>
      <p class="text-xl mb-8 max-w-2xl mx-auto">
        Book your stay today and experience the luxury and tranquility of Serenity Cove.
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <button 
          class="bg-white text-[#0f766e]  px-8 py-3 rounded-lg font-bold hover:bg-gray-100 transition-colors shadow-lg"
          @click="bookStay"
        >
          Book Your Stay
        </button>
        <button 
          class="bg-transparent border-2 border-white text-white px-8 py-3 rounded-lg font-bold hover:bg-white/10 transition-colors"
          @click="contactUs"
        >
          Contact Us
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
const bookStay = () => {
  // Handle booking action
  console.log('Initiating booking process')
}

const contactUs = () => {
  // Handle contact action
  console.log('Opening contact form')
}
</script>