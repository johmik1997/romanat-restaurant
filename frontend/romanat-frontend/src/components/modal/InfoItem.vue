<template>
  <div :class="customClass">
    <dt class="text-sm font-medium text-gray-500 mb-1">{{ label }}</dt>
    <dd class="text-sm text-gray-900 font-medium">{{ displayValue }}</dd>
  </div>
</template>

<script setup>
import { computed } from 'vue'

// Assign the props to a variable
const props = defineProps({
  label: String,
  value: [String, Number],
  class: { type: String, default: '' }
})

// Use the prop in a computed property
const displayValue = computed(() => props.value ?? '—')

// Optional: rename class prop to customClass to avoid reserved word
const customClass = computed(() => props.class)
</script>
