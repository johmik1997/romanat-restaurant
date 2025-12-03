<template>
  <section id="experiences" class="w-full bg-background-light py-20">
    <div class="container mx-auto max-w-7xl px-4">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-[#0f766e]  text-4xl font-serif font-bold mb-4">
          Luxury Experiences & Amenities
        </h2>
        <p class="max-w-2xl mx-auto text-gray-600 text-lg">
          Discover our curated collection of world-class amenities and unforgettable experiences designed for your ultimate comfort and enjoyment.
        </p>
      </div>

      <!-- Main Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Left Column - Featured Experiences -->
        <div>
          <h3 class="text-2xl font-serif font-bold text-gray-800 mb-8 text-center lg:text-left">
            Signature Experiences
          </h3>
          <div class="space-y-6">
            <div 
              v-for="experience in featuredExperiences" 
              :key="experience.id"
              class="group bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition-all duration-300"
            >
              <div class="flex flex-col md:flex-row">
                <div class="md:w-2/5 h-48 md:h-auto overflow-hidden">
                  <img 
                    :src="experience.image" 
                    :alt="experience.title"
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                  />
                </div>
                <div class="md:w-3/5 p-6">
                  <div class="flex items-center mb-3">
                    <div class="h-10 w-10 bg-[#0f766e] /10 text-[#0f766e]  rounded-full flex items-center justify-center mr-3">
                      <span class="material-symbols-outlined text-xl">{{ experience.icon }}</span>
                    </div>
                    <h4 class="text-xl font-bold text-gray-800">{{ experience.title }}</h4>
                  </div>
                  <p class="text-gray-600 mb-4">{{ experience.description }}</p>
                  <div class="flex items-center justify-between">
                    <span class="text-primary font-semibold">{{ experience.duration }}</span>
                    <router-link 
      to="/rooms">
                    <button 
                      class="text-sm bg-[#0f766e]  text-white px-4 py-2 rounded-lg hover:bg-teal-700 transition-colors"
                      @click="bookExperience(experience)"
                    >
                      Book Now
                    </button>
                        </router-link>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column - Amenities Grid -->
        <div>
          <h3 class="text-2xl font-serif font-bold text-gray-800 mb-8 text-center lg:text-left">
            Premium Amenities
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div 
              v-for="amenity in amenities" 
              :key="amenity.id"
              class="group bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
            >
              <div class="flex flex-col items-center text-center">
                <div class="h-20 w-20 bg-primary/10 text-[#0f766e]  rounded-2xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                  <span class="material-symbols-outlined text-3xl">{{ amenity.icon }}</span>
                </div>
                <h4 class="text-lg font-bold text-gray-800 mb-2">{{ amenity.title }}</h4>
                <p class="text-sm text-gray-600 mb-4">{{ amenity.description }}</p>
                
                <!-- Additional Info -->
                <div class="w-full mt-3 pt-3 border-t border-gray-100">
                  <div class="flex justify-between items-center text-xs text-gray-500">
                    <span class="flex items-center">
                      <span class="material-symbols-outlined text-xs mr-1">schedule</span>
                      {{ amenity.hours }}
                    </span>
                    <span class="flex items-center">
                      <span class="material-symbols-outlined text-xs mr-1">location_on</span>
                      {{ amenity.location }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Special Offer Banner -->
          <div class="mt-8 bg-gradient-to-r from-[#0f766e]  to-teal-500 rounded-2xl p-6 text-white">
            <div class="flex items-center justify-between">
              <div>
                <h4 class="text-xl font-bold font-serif mb-2">Wellness Package</h4>
                <p class="text-white/90 text-sm">Complimentary spa treatment with any 3-night stay</p>
              </div>
              <button 
                class="bg-white text-[#0f766e]  px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors whitespace-nowrap"
                @click="viewWellnessPackage"
              >
                Learn More
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom CTA -->
      <div class="mt-16 text-center">
        <div class="bg-white rounded-2xl p-8 shadow-lg">
          <h3 class="text-2xl font-serif font-bold text-gray-800 mb-4">
            Ready to Experience Luxury?
          </h3>
          <p class="text-gray-600 mb-6 max-w-2xl mx-auto">
            Contact our concierge team to customize your perfect stay and discover all we have to offer.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="#contact">
            <button 
              class="bg-[#0f766e]  text-white px-8 py-3 rounded-lg font-semibold hover:bg-teal-500 transition-colors"
              @click="contactConcierge"
            >
              Contact Concierge
            </button>
            </a>
            <button 
              class="border-2 border-primary text-primary px-8 py-3 rounded-lg font-semibold hover:bg-[#0f766e]  hover:text-white transition-colors"
              @click="viewAllAmenities"
            >
              View All Amenities
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const featuredExperiences = ref([
  {
    id: 1,
    icon: 'spa',
    title: 'Signature Spa Journey',
    description: 'Indulge in our exclusive 3-hour wellness experience featuring hot stone therapy, aromatherapy, and personalized massage treatments.',
    duration: '3 Hours',
    image: 'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80',
    price: 189
  },
  {
    id: 2,
    icon: 'restaurant',
    title: 'Chef\'s Table Experience',
    description: 'An intimate dining experience with our executive chef, featuring a 7-course tasting menu with wine pairings in a private setting.',
    duration: '2.5 Hours',
    image: 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80',
    price: 225
  },
  {
    id: 3,
    icon: 'sailing',
    title: 'Sunset Catamaran Cruise',
    description: 'Private catamaran tour along the coastline with champagne toast, gourmet appetizers, and breathtaking sunset views.',
    duration: '2 Hours',
    image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80',
    price: 150
  }
])

const amenities = ref([
 
 
  {
    id: 3,
    icon: 'spa',
    title: 'Wellness Spa',
    description: 'Full-service spa with treatment rooms, steam room, and relaxation lounge.',
    hours: '9AM - 9PM',
    location: 'Level 1'
  },
  {
    id: 4,
    icon: 'restaurant',
    title: 'Fine Dining',
    description: 'Award-winning restaurant featuring locally sourced ingredients and ocean views.',
    hours: '7AM - 11PM',
    location: 'Lobby Level'
  },
  {
    id: 5,
    icon: 'business_center',
    title: 'Business Center',
    description: 'Fully equipped business facilities with meeting rooms and high-speed internet.',
    hours: '24 Hours',
    location: 'Level 3'
  },
  {
    id: 6,
    icon: 'local_laundry_service',
    title: 'Concierge Services',
    description: '24/7 concierge to assist with reservations, tours, and personalized requests.',
    hours: '24 Hours',
    location: 'Lobby'
  }
])

const bookExperience = (experience) => {

}

const viewWellnessPackage = () => {
  console.log('Viewing wellness package details')
}

const contactConcierge = () => {
  console.log('Contacting concierge')
}

const viewAllAmenities = () => {
  console.log('Viewing all amenities')
  // Implement view all logic
}
</script>

<style scoped>
/* Custom styles for better visual appeal */
.group:hover .material-symbols-outlined {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}
</style>