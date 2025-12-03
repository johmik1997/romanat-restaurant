<template>
  <div class="relative w-full rounded-2xl overflow-hidden shadow-xl">
    <div 
      v-if="currentImage"
      class="bg-cover bg-center flex flex-col justify-end min-h-[500px] transition-all duration-500"
      :style="{ backgroundImage: `linear-gradient(0deg, rgba(0, 0, 0, 0.3) 0%, rgba(0, 0, 0, 0) 30%), url('${currentImage}')` }"
    >
      <!-- Image Dots Indicator -->
      <div class="flex justify-center gap-2 p-6">
        <div 
          v-for="(image, index) in images" 
          :key="index"
          class="size-3 rounded-full transition-all duration-300 cursor-pointer"
          :class="currentIndex === index ? 'bg-white' : 'bg-white/50'"
          @click="setCurrentImage(index)"
        ></div>
      </div>
    </div>
    
    <!-- Fallback if no images -->
    <div 
      v-else
      class="bg-gray-200 min-h-[500px] flex items-center justify-center rounded-2xl"
    >
      <div class="text-center text-gray-500">
        <svg class="w-16 h-16 mx-auto mb-4" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"/>
        </svg>
        <p class="text-lg">No images available</p>
      </div>
    </div>
    
    <!-- Navigation Arrows -->
    <button 
      v-if="images && images.length > 1"
      @click="previousImage"
      class="absolute top-1/2 left-6 -translate-y-1/2 bg-white/90 backdrop-blur-sm p-3 rounded-full text-gray-700 hover:bg-white transition-all duration-300 hover:scale-110 shadow-lg"
    >
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
      </svg>
    </button>
    <button 
      v-if="images && images.length > 1"
      @click="nextImage"
      class="absolute top-1/2 right-6 -translate-y-1/2 bg-white/90 backdrop-blur-sm p-3 rounded-full text-gray-700 hover:bg-white transition-all duration-300 hover:scale-110 shadow-lg"
    >
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const props = defineProps({
  images: {
    type: Array,
    default: () => [] // Provide empty array as default
  }
})

const currentIndex = ref(0)
const currentImage = ref('')
let autoSlideInterval

const setCurrentImage = (index) => {
  if (!props.images || props.images.length === 0) return
  currentIndex.value = index
  currentImage.value = props.images[index]
}

const nextImage = () => {
  if (!props.images || props.images.length === 0) return
  currentIndex.value = (currentIndex.value + 1) % props.images.length
  currentImage.value = props.images[currentIndex.value]
}

const previousImage = () => {
  if (!props.images || props.images.length === 0) return
  currentIndex.value = (currentIndex.value - 1 + props.images.length) % props.images.length
  currentImage.value = props.images[currentIndex.value]
}

const startAutoSlide = () => {
  if (!props.images || props.images.length <= 1) return
  stopAutoSlide()
  autoSlideInterval = setInterval(nextImage, 5000)
}

const stopAutoSlide = () => {
  if (autoSlideInterval) {
    clearInterval(autoSlideInterval)
  }
}

// Initialize when component mounts
onMounted(() => {
  // Set initial image when images array is available
  if (props.images && props.images.length > 0) {
    currentImage.value = props.images[0]
    startAutoSlide()
  }
})

// Watch for changes in images prop
watch(() => props.images, (newImages) => {
  if (newImages && newImages.length > 0) {
    currentImage.value = newImages[0]
    currentIndex.value = 0
    startAutoSlide()
  } else {
    currentImage.value = ''
    stopAutoSlide()
  }
}, { immediate: true })

onUnmounted(() => {
  stopAutoSlide()
})
</script>

<style scoped>
/* Smooth transitions for image changes */
.bg-cover {
  transition: background-image 0.5s ease-in-out;
}
</style>