<template>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
    <!-- Total Revenue -->
    <div class="bg-white rounded-xl border border-gray-200 p-6">
      <div class="flex items-center justify-between">
        <div>
            <button 
  :class="{ 'active': activeFilter === 'all' }" 
  @click="$emit('filter-change', 'all')"
>
  All ({{ counts.all }})
</button>
<button 
  :class="{ 'active': activeFilter === 'current' }" 
  @click="$emit('filter-change', 'current')"
>
  Current ({{ counts.current }})
</button>
<button 
  :class="{ 'active': activeFilter === 'past' }" 
  @click="$emit('filter-change', 'past')"
>
  Past ({{ counts.past }})
</button>
        </div>
        </div>
    </div>
    </div>
    </template>
