<template>
  <div class="flex flex-col gap-2 rounded-xl p-6 bg-white  border-[#E1E5E8] ">
    <p class="text-base font-medium text-gray-600 ">{{ label }}</p>
    <p class="text-4xl font-bold text-[#111418] ">{{ value }}</p>
  </div>
</template>

<script>
export default {
  name: 'MetricCard',
  props: {
    label: {
      type: String,
      required: true
    },
    value: {
      type: [String, Number],
      required: true
    }
  }
}
</script>