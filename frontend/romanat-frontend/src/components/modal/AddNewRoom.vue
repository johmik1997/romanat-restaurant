<template>
  <transition name="fade">
    <div
      v-if="isOpen"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black/50"
    >
      <div
        class="bg-white rounded-xl shadow-lg w-full max-w-5xl p-6 relative max-h-[95vh] h-[85vh] overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-bold text-gray-900">
            {{ isEditMode ? 'Edit Room' : 'Add New Room' }}
          </h2>
          <button @click="closeModal" class="text-gray-500 hover:text-gray-700">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>

        <form @submit.prevent="submitForm" class="flex flex-col gap-4">
          <!-- Room Number -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Room Number *</label>
              <input
                v-model="room.room_number"
                type="text"
                placeholder="e.g., 101"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 text-black focus:border-[#0f766e]"
                required
                :disabled="isEditMode"
              />
              <p v-if="isEditMode" class="text-xs text-gray-500 mt-1">Room number cannot be changed</p>
            </div>

            <!-- Room Type -->
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Room Type *</label>
              <select
                v-model="room.room_type_id"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 text-black focus:border-[#0f766e]"
                required
              >
                <option value="" disabled>Select type</option>
                <option v-for="type in roomTypes" :key="type.id" :value="type.id">
                  {{ type.name }}
                </option>
              </select>
            </div>
          </div>

          <!-- Floor -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Floor *</label>
              <select
                v-model="room.floor"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 text-black focus:border-[#0f766e]"
                required
              >
                <option value="" disabled>Select floor</option>
                <option v-for="n in 10" :key="n" :value="n">{{ n }}</option>
              </select>
            </div>

            <!-- Price -->
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Price ($) *</label>
              <input
                v-model="room.price"
                type="number"
                min="0"
                step="0.01"
                placeholder="e.g., 120.00"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 text-black focus:border-[#0f766e]"
                required
              />
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Capacity -->
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Capacity *</label>
              <select
                v-model="room.capacity"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 text-black focus:border-[#0f766e]"
                required
              >
                <option value="" disabled>Select capacity</option>
                <option value="1">1 Guest</option>
                <option value="2">2 Guests</option>
                <option value="3">3 Guests</option>
                <option value="4">4 Guests</option>
              </select>
            </div>

            <!-- Category -->
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Category</label>
              <select
                v-model="room.category"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 text-black focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
              >
                <option value="normal">Normal</option>
                <option value="deluxe">Deluxe</option>
                <option value="suite">Suite</option>
                <option value="executive">Executive</option>
                <option value="presidential">Presidential</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Size -->
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Size (sq.m)</label>
              <input
                v-model="room.size"
                type="number"
                min="0"
                placeholder="e.g., 35"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 text-black focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
              />
            </div>

            <!-- View -->
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">View</label>
              <input
                v-model="room.view"
                type="text"
                placeholder="e.g., Ocean, City, Mountain"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 text-black focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
              />
            </div>
          </div>

          <!-- Featured -->
          <div class="flex items-center gap-2">
            <input type="checkbox" v-model="room.featured" class="rounded border-gray-300 text-[#0f766e] focus:ring-[#0f766e]"/>
            <label class="text-gray-700 text-sm">Featured Room</label>
          </div>

          <!-- Status -->
          <div>
            <label class="block text-gray-700 text-sm font-medium mb-1">Status</label>
            <select v-model="room.status" class="w-full px-3 py-2 border border-gray-300 text-black rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 focus:border-[#0f766e]">
              <option value="available">Available</option>
              <option value="occupied">Occupied</option>
              <option value="maintenance">Maintenance</option>
              <option value="cleaning">Cleaning</option>
              <option value="reserved">Reserved</option>
            </select>
          </div>

          <!-- Amenities -->
          <div>
            <label class="block text-gray-700 text-sm font-medium mb-1">Amenities</label>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-2">
              <label v-for="amenity in availableAmenities" :key="amenity" class="flex items-center">
                <input 
                  type="checkbox" 
                  :value="amenity" 
                  v-model="room.amenities" 
                  class="rounded border-gray-300 text-[#0f766e] focus:ring-[#0f766e]"
                />
                <span class="ml-2 text-sm text-gray-700">{{ amenity }}</span>
              </label>
            </div>
          </div>

          <!-- Title & Subtitle -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Title</label>
              <input
                v-model="room.title"
                type="text"
                placeholder="Room title"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 text-black focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
              />
            </div>
            
            <div>
              <label class="block text-gray-700 text-sm font-medium mb-1">Subtitle</label>
              <input
                v-model="room.subtitle"
                type="text"
                placeholder="Room subtitle"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 text-black focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
              />
            </div>
          </div>

          <!-- Description -->
          <div>
            <label class="block text-gray-700 text-sm font-medium mb-1">Description</label>
            <textarea
              v-model="room.description"
              placeholder="Room description..."
              rows="3"
              class="w-full px-3 py-2 border border-gray-300 text-black rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
            ></textarea>
          </div>

          <!-- Thumbnail Upload -->
          <div>
            <label class="text-sm font-medium text-gray-700">Thumbnail</label>
            
            <div class="flex items-start gap-4 mt-2">
              <!-- Current thumbnail (edit mode) -->
              <div v-if="isEditMode && room.thumbnail && !thumbnailPreview" class="w-32 h-32">
                <img
                  :src="room.thumbnail"
                  class="w-full h-full object-cover rounded-lg border"
                  alt="Current thumbnail"
                />
                <p class="text-xs text-gray-500 mt-1">Current thumbnail</p>
              </div>
              
              <!-- New thumbnail upload -->
              <div
                class="w-40 h-40 border border-dashed border-gray-400 rounded-lg flex items-center justify-center cursor-pointer overflow-hidden bg-gray-50 hover:border-gray-600 transition"
                @click="thumbnailInput?.click()"
              >
                <!-- Preview -->
                <img
                  v-if="thumbnailPreview"
                  :src="thumbnailPreview"
                  class="w-full h-full object-cover"
                />
                
                <!-- Placeholder -->
                <div v-else class="text-center text-gray-500 text-sm">
                  {{ isEditMode ? 'Change thumbnail' : 'Click to upload' }}
                </div>
                
                <input
                  type="file"
                  accept="image/*"
                  ref="thumbnailInput"
                  @change="onThumbnailChange"
                  class="hidden"
                />
              </div>
            </div>
            
            <!-- Clear thumbnail button -->
            <div class="mt-2">
              <button
                v-if="thumbnailPreview"
                type="button"
                @click="clearThumbnail"
                class="text-sm text-red-600 hover:text-red-800"
              >
                Remove new thumbnail
              </button>
              <button
                v-else-if="isEditMode && room.thumbnail"
                type="button"
                @click="removeExistingThumbnail"
                class="text-sm text-red-600 hover:text-red-800"
              >
                Remove current thumbnail
              </button>
            </div>
          </div>

          <!-- Additional Images -->
          <div class="mt-6">
            <label class="text-sm font-medium text-gray-700">Additional Images</label>
            
            <!-- Current images (edit mode) -->
            <div v-if="isEditMode && existingImages.length > 0" class="mb-4">
              <p class="text-sm text-gray-600 mb-2">Current images:</p>
              <div class="grid grid-cols-3 gap-4">
                <div
                  v-for="(img, index) in existingImages"
                  :key="index"
                  class="relative w-32 h-32 border rounded-lg overflow-hidden bg-gray-50 group"
                >
                  <img :src="img" class="w-full h-full object-cover" />
                  <button
                    type="button"
                    @click="removeExistingImage(index)"
                    class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity"
                  >
                    ×
                  </button>
                </div>
              </div>
            </div>
            
            <!-- New images upload -->
            <div class="grid grid-cols-3 gap-4">
              <!-- Preview new images -->
              <div
                v-for="(img, index) in imagesPreview"
                :key="'new-' + index"
                class="relative w-32 h-32 border border-dashed border-gray-400 rounded-lg overflow-hidden bg-gray-50 group"
              >
                <img :src="img" class="w-full h-full object-cover" />
                <button
                  type="button"
                  @click="removeAdditionalImage(index)"
                  class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity"
                >
                  ×
                </button>
              </div>
              
              <!-- + Upload Box -->
              <div
                class="w-32 h-32 border border-dashed border-gray-400 rounded-lg flex items-center justify-center cursor-pointer hover:border-gray-600 transition bg-gray-50 text-gray-500 text-3xl font-bold"
                @click="additionalInput?.click()"
              >
                +
                <input
                  type="file"
                  accept="image/*"
                  ref="additionalInput"
                  @change="onAdditionalImagesChange"
                  multiple
                  class="hidden"
                />
              </div>
            </div>
          </div>

          <!-- About & Notes -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-black text-sm font-medium mb-1">About this Room</label>
              <textarea
                v-model="room.about"
                placeholder="Room details and features..."
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 text-black rounded-lg focus:ring-2 focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
              ></textarea>
            </div>
            
            <div>
              <label class="block text-black text-sm font-medium mb-1">Notes</label>
              <textarea
                v-model="room.notes"
                placeholder="Internal notes..."
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg text-black focus:ring-2 focus:ring-[#0f766e]/20 focus:border-[#0f766e]"
              ></textarea>
            </div>
          </div>

          <!-- Form Actions -->
          <div class="flex justify-end gap-2 mt-6 pt-6 border-t">
            <button 
              type="button" 
              @click="closeModal" 
              class="px-6 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 text-gray-700 transition-colors"
            >
              Cancel
            </button>
            <button 
              type="submit" 
              class="px-6 py-2 rounded-lg bg-[#0f766e] text-white hover:bg-[#0f766e]/90 transition-colors"
            >
              {{ isEditMode ? 'Update Room' : 'Add Room' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, defineProps, defineEmits, onMounted, watch, computed } from 'vue';
import { createRoom, updateRoom, fetchRoomType, fetchRoomById, deleteRoom } from '../../api/auth/roomApi'; // Added deleteRoom

const props = defineProps({ 
  isOpen: Boolean,
  roomData: {
    type: [Object, String, Number],
    default: null
  }
});

const emits = defineEmits(['close', 'save']);

// Refs
const roomTypes = ref([]);
const thumbnailInput = ref(null);
const additionalInput = ref(null);
const thumbnailPreview = ref(null);
const imagesPreview = ref([]);
const existingImages = ref([]);
const imagesToRemove = ref([]);

const availableAmenities = [
  'WiFi', 'TV', 'Air Conditioning', 'Mini Bar', 'Safe',
  'Balcony', 'Ocean View', 'Room Service', 'Hot Tub',
  'Free Parking', 'Breakfast Included', 'Pet Friendly'
];

// Room data - FIXED: Added room.thumbnail property
const room = ref({
  room_number: '',
  room_type_id: '',
  floor: '',
  price: '',
  capacity: '2',
  amenities: [],
  description: '',
  category: 'normal',
  size: '',
  view: '',
  featured: false,
  status: 'available',
  notes: '',
  thumbnail: '', // Added this field
  thumbnail_file: null,
  images_files: [],
  title: '',
  subtitle: '',
  about: '',
  remove_thumbnail: false
});

// Computed
const isEditMode = computed(() => !!props.roomData);

// Watch for modal open/close
watch(() => props.isOpen, (newVal) => {
  if (newVal) {
    initializeForm();
  } else {
    cleanup();
  }
});

// Watch for room data changes
watch(() => props.roomData, (newData) => {
  if (newData && props.isOpen) {
    initializeForm();
  }
});

const closeModal = () => {
  cleanup();
  emits('close');
};

// Initialize form based on mode - FIXED: Properly fetches room data
const initializeForm = async () => {
  if (props.roomData) {
    // Edit mode: Load room data
    try {
      let roomData;
      if (typeof props.roomData === 'number' || typeof props.roomData === 'string') {
        // If it's an ID, fetch from API
        roomData = await fetchRoomById(props.roomData);
      } else {
        // If it's an object, use it directly
        roomData = props.roomData;
      }

      console.log('Loaded room data:', roomData);

      // Reset previews
      thumbnailPreview.value = null;
      imagesPreview.value = [];
      existingImages.value = roomData.images || roomData.additional_images || [];
      imagesToRemove.value = [];

      // Populate form - FIXED: Properly map API response to form fields
      room.value = {
        room_number: roomData.room_number || '',
        room_type_id: roomData.room_type?.id || roomData.room_type_id || '',
        floor: roomData.floor || '',
        price: roomData.price || '',
        capacity: roomData.capacity || '2',
        amenities: Array.isArray(roomData.amenities) ? roomData.amenities : 
                  (typeof roomData.amenities === 'string' ? JSON.parse(roomData.amenities) : []),
        description: roomData.description || '',
        category: roomData.category || 'normal',
        size: roomData.size || '',
        view: roomData.view || '',
        featured: roomData.featured || false,
        status: roomData.status || 'available',
        notes: roomData.notes || '',
        thumbnail: roomData.thumbnail || roomData.thumbnail_url || '',
        thumbnail_file: null,
        images_files: [],
        title: roomData.title || '',
        subtitle: roomData.subtitle || '',
        about: roomData.about || '',
        remove_thumbnail: false
      };
    } catch (error) {
      console.error('Error loading room data:', error);
      alert('Failed to load room details');
      closeModal();
    }
  } else {
    // Add mode: Reset form
    resetForm();
  }
};

// Image handling
const onThumbnailChange = (e) => {
  const file = e.target.files[0];
  if (file) {
    if (!file.type.startsWith('image/')) {
      alert('Please select an image file');
      return;
    }
    
    if (file.size > 5 * 1024 * 1024) {
      alert('File size must be less than 5MB');
      return;
    }
    
    thumbnailPreview.value = URL.createObjectURL(file);
    room.value.thumbnail_file = file;
    room.value.remove_thumbnail = false;
  }
};

const clearThumbnail = () => {
  if (thumbnailPreview.value) {
    URL.revokeObjectURL(thumbnailPreview.value);
  }
  thumbnailPreview.value = null;
  room.value.thumbnail_file = null;
  room.value.remove_thumbnail = true;
  if (thumbnailInput.value) {
    thumbnailInput.value.value = '';
  }
};

const removeExistingThumbnail = () => {
  room.value.thumbnail = '';
  room.value.remove_thumbnail = true;
};

const onAdditionalImagesChange = (e) => {
  const files = Array.from(e.target.files);
  
  files.forEach(file => {
    if (!file.type.startsWith('image/')) {
      alert('Please select only image files');
      return;
    }
    
    if (file.size > 5 * 1024 * 1024) {
      alert(`File ${file.name} is too large. Max size is 5MB`);
      return;
    }
    
    imagesPreview.value.push(URL.createObjectURL(file));
    room.value.images_files.push(file);
  });
  
  if (additionalInput.value) {
    additionalInput.value.value = '';
  }
};

const removeAdditionalImage = (index) => {
  URL.revokeObjectURL(imagesPreview.value[index]);
  imagesPreview.value.splice(index, 1);
  room.value.images_files.splice(index, 1);
};

const removeExistingImage = (index) => {
  imagesToRemove.value.push(existingImages.value[index]);
  existingImages.value.splice(index, 1);
};

// Form submission - FIXED: Proper FormData handling
const submitForm = async () => {
  try {
    const formData = new FormData();
    
    // Append all fields
    Object.keys(room.value).forEach(key => {
      if (key === 'thumbnail_file' && room.value.thumbnail_file) {
        formData.append('thumbnail', room.value.thumbnail_file); // Changed to 'thumbnail'
      } 
      else if (key === 'images_files') {
        room.value.images_files.forEach(file => {
          formData.append('additional_images', file); // Changed to 'additional_images'
        });
      }
      else if (key === 'amenities') {
        formData.append(key, JSON.stringify(room.value[key]));
      }
      else if (key === 'remove_thumbnail' && room.value[key]) {
        formData.append('remove_thumbnail', 'true');
      }
      else if (room.value[key] !== null && room.value[key] !== undefined && 
               room.value[key] !== '' && key !== 'thumbnail_file' && 
               key !== 'images_files') {
        formData.append(key, room.value[key]);
      }
    });
    
    console.log('Submitting form data for', isEditMode.value ? 'edit' : 'add');
    
    let response;
    if (isEditMode.value) {
      const roomId = props.roomData?.id || props.roomData;
      response = await updateRoom(roomId, formData);
    } else {
      response = await createRoom(formData);
    }
    
    emits('save', response);
    resetForm();
    closeModal();
    
  } catch (error) {
    console.error('Error saving room:', error);
    let errorMessage = `Failed to ${isEditMode.value ? 'update' : 'add'} room. Please try again.`;
    
    if (error.detail) {
      errorMessage = error.detail;
    } else if (error.message) {
      errorMessage = error.message;
    } else if (typeof error === 'string') {
      errorMessage = error;
    }
    
    alert(errorMessage);
  }
};

// Reset form
const resetForm = () => {
  cleanup();
  
  room.value = {
    room_number: '',
    room_type_id: '',
    floor: '',
    price: '',
    capacity: '2',
    amenities: [],
    description: '',
    category: 'normal',
    size: '',
    view: '',
    featured: false,
    status: 'available',
    notes: '',
    thumbnail: '',
    thumbnail_file: null,
    images_files: [],
    title: '',
    subtitle: '',
    about: '',
    remove_thumbnail: false
  };
  
  existingImages.value = [];
  imagesToRemove.value = [];
  
  if (thumbnailInput.value) thumbnailInput.value.value = '';
  if (additionalInput.value) additionalInput.value.value = '';
};

// Cleanup
const cleanup = () => {
  if (thumbnailPreview.value) {
    URL.revokeObjectURL(thumbnailPreview.value);
  }
  imagesPreview.value.forEach(url => URL.revokeObjectURL(url));
  thumbnailPreview.value = null;
  imagesPreview.value = [];
};

// Fetch room types
onMounted(async () => {
  try {
    const response = await fetchRoomType();
    roomTypes.value = response.result || response || [];
  } catch (err) {
    console.error('Failed to fetch room types', err);
    roomTypes.value = [];
  }
});
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active { transition: opacity 0.2s; }
.fade-enter-from,
.fade-leave-to { opacity: 0; }
</style>