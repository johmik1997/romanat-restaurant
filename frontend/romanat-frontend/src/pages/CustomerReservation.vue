<template>
  <div class="min-h-screen bg-gray-50 p-4 md:p-6">
    <!-- Header with Title and Actions -->
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8">
      <div>
        <h1 class="text-2xl md:text-3xl font-bold text-gray-900">My Reservation</h1>
        <p class="text-gray-600 mt-1">View and manage your booking details</p>
      </div>
      
      <!-- Action Buttons -->
      <div v-if="reservation && reservation.status !== 'cancelled'" class="flex gap-3">
        <button
          @click="downloadReceipt"
          class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 text-gray-700 font-medium flex items-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          Download Receipt
        </button>
        
        <button
          @click="requestChanges"
          v-if="reservation.status === 'pending' || reservation.status === 'confirmed'"
          class="px-4 py-2 border border-blue-600 text-blue-600 rounded-lg hover:bg-blue-50 font-medium flex items-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
          Request Changes
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex flex-col items-center justify-center py-20">
      <div class="animate-spin h-12 w-12 border-4 border-green-600 border-t-transparent rounded-full mb-4"></div>
      <p class="text-gray-600">Loading your reservation details...</p>
    </div>

    <!-- Error State -->
    <div v-if="error" class="bg-red-50 border border-red-200 rounded-xl p-6 max-w-xl mx-auto">
      <div class="flex items-center gap-3 text-red-800 mb-3">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3 class="font-semibold">Unable to load reservation</h3>
      </div>
      <p class="text-red-600">{{ error }}</p>
      <button @click="loadReservation" class="mt-4 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 font-medium">
        Try Again
      </button>
    </div>

    <!-- No Reservation State -->
    <div v-if="!loading && !reservation" class="text-center py-16 max-w-md mx-auto">
      <div class="bg-gray-100 w-24 h-24 rounded-full flex items-center justify-center mx-auto mb-6">
        <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
        </svg>
      </div>
      <h3 class="text-xl font-semibold text-gray-900 mb-2">No Reservation Found</h3>
      <p class="text-gray-600 mb-8">You don't have any active reservations at the moment.</p>
      <router-link to="/rooms" class="inline-block px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 font-semibold">
        Browse Available Rooms
      </router-link>
    </div>

    <!-- Reservation Details -->
    <div v-if="reservation && !loading" class="max-w-4xl mx-auto">
      <!-- Status Banner -->
      <div :class="statusBannerClass(reservation.status)" class="rounded-xl p-5 mb-6 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div :class="statusIconClass(reservation.status)" class="w-10 h-10 rounded-full flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="reservation.status === 'confirmed'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              <path v-if="reservation.status === 'pending'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              <path v-if="reservation.status === 'checked_in'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              <path v-if="reservation.status === 'checked_out'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              <path v-if="reservation.status === 'cancelled'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <p class="font-semibold capitalize">{{ reservation.status.replace('_', ' ') }}</p>
            <p class="text-sm opacity-90">{{ statusMessage(reservation.status) }}</p>
          </div>
        </div>
        <span class="font-bold text-lg">#{{ reservation.id }}</span>
      </div>

      <!-- Main Card -->
      <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
        <!-- Card Header -->
        <div class="border-b border-gray-200 p-6">
          <h2 class="text-xl font-bold text-gray-900">Reservation Details</h2>
          <p class="text-gray-600 mt-1">Booked on {{ formatDateTime(reservation.created_at) }}</p>
        </div>

        <!-- Card Content -->
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Left Column -->
            <div class="space-y-6">
              <!-- Room Details -->
              <div class="bg-gray-50 rounded-xl p-5">
                <h3 class="font-semibold text-gray-900 mb-4 flex items-center gap-2">
                  <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                  </svg>
                  Room Information
                </h3>
                <div class="space-y-3">
                  <div class="flex justify-between">
                    <span class="text-gray-600">Room Number:</span>
                    <span class="font-semibold text-gray-900">{{ reservation.room.room_number }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Room Type:</span>
                    <span class="font-semibold text-gray-900">{{ reservation.room.room_type.name }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Capacity:</span>
                    <span class="text-gray-900">{{ reservation.room.capacity }} guests</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Price per night:</span>
                    <span class="text-gray-900">${{ reservation.room.price }}</span>
                  </div>
                  <!-- Room Amenities -->
                  <div v-if="reservation.room.amenities && reservation.room.amenities.length > 0">
                    <span class="text-gray-600">Amenities:</span>
                    <div class="flex flex-wrap gap-2 mt-2">
                      <span 
                        v-for="amenity in reservation.room.amenities" 
                        :key="amenity"
                        class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded"
                      >
                        {{ amenity }}
                      </span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Guest Information -->
              <div class="bg-gray-50 rounded-xl p-5">
                <h3 class="font-semibold text-gray-900 mb-4 flex items-center gap-2">
                  <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  Guest Information
                </h3>
                <div class="space-y-3">
                  <div class="flex justify-between">
                    <span class="text-gray-600">Name:</span>
                    <span class="font-semibold text-gray-900">{{ reservation.customer.first_name }} {{ reservation.customer.last_name }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Email:</span>
                    <span class="text-gray-900">{{ reservation.customer.email }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Phone:</span>
                    <span class="text-gray-900">{{ reservation.customer.phone }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Number of Guests:</span>
                    <span class="font-semibold text-gray-900">{{ reservation.number_of_guests }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right Column -->
            <div class="space-y-6">
              <!-- Dates -->
              <div class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-5">
                <h3 class="font-semibold text-gray-900 mb-4">Stay Duration</h3>
                <div class="grid grid-cols-2 gap-4">
                  <div class="bg-white rounded-lg p-4">
                    <p class="text-gray-400 text-sm font-medium">Check-in</p>
                    <p class="text-gray-900 font-bold text-lg mt-1">{{ formatDate(reservation.check_in) }}</p>
                    <p class="text-gray-600 text-sm">After 2:00 PM</p>
                  </div>
                  <div class="bg-white rounded-lg p-4">
                    <p class="text-gray-400 text-sm font-medium">Check-out</p>
                    <p class="text-gray-900 font-bold text-lg mt-1">{{ formatDate(reservation.check_out) }}</p>
                    <p class="text-gray-600 text-sm">Before 11:00 AM</p>
                  </div>
                </div>
                <div class="mt-4 pt-4 border-t border-blue-100">
                  <div class="flex justify-between items-center">
                    <span class="text-gray-600">Total Nights:</span>
                    <span class="font-semibold text-gray-900">{{ calculateNights(reservation.check_in, reservation.check_out) }} nights</span>
                  </div>
                </div>
              </div>

              <!-- Price Breakdown -->
              <div class="bg-gray-50 rounded-xl p-5">
                <h3 class="font-semibold text-gray-900 mb-4">Price Breakdown</h3>
                <div class="space-y-3">
                  <div class="flex justify-between">
                    <span class="text-gray-600">Room rate × {{ calculateNights(reservation.check_in, reservation.check_out) }} nights:</span>
                    <span class="text-gray-900">${{ (parseFloat(reservation.room.price) * calculateNights(reservation.check_in, reservation.check_out)).toFixed(2) }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span class="text-gray-600">Taxes & Fees (15%):</span>
                    <span class="text-gray-900">${{ (parseFloat(reservation.total_price) * 0.15).toFixed(2) }}</span>
                  </div>
                  <div class="pt-3 border-t border-gray-200">
                    <div class="flex justify-between items-center">
                      <span class="text-lg font-semibold text-gray-900">Total Amount:</span>
                      <span class="text-2xl font-bold text-green-600">${{ reservation.total_price }}</span>
                    </div>
                    <p class="text-gray-500 text-sm mt-1">Paid upon check-in</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Card Footer -->
        <div class="border-t border-gray-200 p-6 bg-gray-50">
          <div class="flex flex-col sm:flex-row gap-4 justify-between">
            <!-- Contact Information -->
            <div>
              <p class="text-sm text-gray-600 mb-2">Need help with your reservation?</p>
              <div class="flex items-center gap-3">
                <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
                <a href="tel:+1234567890" class="text-gray-900 font-medium hover:text-blue-600">+1 (234) 567-890</a>
              </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex flex-col sm:flex-row gap-3">
              <button
                v-if="reservation.status === 'pending' || reservation.status === 'confirmed'"
                @click="cancelReservation"
                class="px-6 py-3 bg-red-600 text-white rounded-lg hover:bg-red-700 font-semibold flex items-center justify-center gap-2"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
                Cancel Reservation
              </button>
              
              <button
                @click="contactSupport"
                class="px-6 py-3 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 font-semibold"
              >
                Contact Support
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Timeline -->
      <div v-if="reservation.status !== 'cancelled'" class="mt-8 bg-white rounded-2xl shadow-lg p-6">
        <h3 class="font-semibold text-gray-900 mb-6">Reservation Timeline</h3>
        <div class="relative">
          <!-- Timeline line -->
          <div class="absolute left-4 top-0 bottom-0 w-0.5 bg-gray-200"></div>
          
          <div class="space-y-8">
            <div class="flex items-start">
              <div :class="statusStepClass('created')" class="relative z-10 flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
              </div>
              <div class="ml-6">
                <p class="font-medium text-gray-900">Reservation Created</p>
                <p class="text-gray-600 text-sm mt-1">{{ formatDateTime(reservation.created_at) }}</p>
              </div>
            </div>

            <div class="flex items-start">
              <div :class="statusStepClass('confirmed')" class="relative z-10 flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
              </div>
              <div class="ml-6">
                <p class="font-medium text-gray-900">Reservation Confirmed</p>
                <p class="text-gray-600 text-sm mt-1">
                  {{ reservation.status === 'confirmed' || reservation.status === 'checked_in' || reservation.status === 'checked_out' 
                    ? formatDateTime(reservation.created_at) 
                    : 'Pending confirmation' }}
                </p>
              </div>
            </div>

            <div class="flex items-start">
              <div :class="statusStepClass('checked_in')" class="relative z-10 flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
              </div>
              <div class="ml-6">
                <p class="font-medium text-gray-900">Check-in</p>
                <p class="text-gray-600 text-sm mt-1">
                  {{ reservation.status === 'checked_in' || reservation.status === 'checked_out' 
                    ? formatDate(reservation.check_in) + ' (After 2:00 PM)' 
                    : 'Scheduled for ' + formatDate(reservation.check_in) }}
                </p>
              </div>
            </div>

            <div class="flex items-start">
              <div :class="statusStepClass('checked_out')" class="relative z-10 flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
              </div>
              <div class="ml-6">
                <p class="font-medium text-gray-900">Check-out</p>
                <p class="text-gray-600 text-sm mt-1">
                  {{ reservation.status === 'checked_out' 
                    ? formatDate(reservation.check_out) + ' (Before 11:00 AM)' 
                    : 'Scheduled for ' + formatDate(reservation.check_out) }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { getCustomerReservation, cancelCustomerReservation } from "../api/auth/userApi"

const loading = ref(true)
const error = ref(null)
const reservation = ref(null)

const loadReservation = async () => {
  loading.value = true
  error.value = null

  try {
    const data = await getCustomerReservation()
    reservation.value = data || null
  } catch (err) {
    error.value = err.message || "Failed to load reservation"
  }

  loading.value = false
}

const statusBannerClass = (status) => {
  return {
    pending: "bg-yellow-100 text-yellow-800",
    confirmed: "bg-green-100 text-green-800",
    checked_in: "bg-blue-100 text-blue-800",
    checked_out: "bg-gray-100 text-gray-800",
    cancelled: "bg-red-100 text-red-800",
  }[status] || "bg-gray-100 text-gray-800"
}

const statusIconClass = (status) => {
  return {
    pending: "bg-yellow-500",
    confirmed: "bg-green-500",
    checked_in: "bg-blue-500",
    checked_out: "bg-gray-500",
    cancelled: "bg-red-500",
  }[status] || "bg-gray-500"
}

const statusMessage = (status) => {
  const messages = {
    pending: "Your reservation is pending confirmation",
    confirmed: "Your reservation has been confirmed",
    checked_in: "You are currently checked in",
    checked_out: "Your stay has been completed",
    cancelled: "This reservation has been cancelled",
  }
  return messages[status] || ""
}

const statusStepClass = (step) => {
  const statusOrder = ['pending', 'confirmed', 'checked_in', 'checked_out']
  const currentStatus = reservation.value?.status
  const currentStepIndex = statusOrder.indexOf(currentStatus)
  const stepIndex = statusOrder.indexOf(step)
  
  // Always show created step as completed
  if (step === 'created') return "bg-green-500"
  
  if (currentStepIndex >= stepIndex) {
    return "bg-green-500"
  } else {
    return "bg-gray-300"
  }
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const formatDateTime = (date) => {
  return new Date(date).toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const calculateNights = (checkIn, checkOut) => {
  const oneDay = 24 * 60 * 60 * 1000
  const checkInDate = new Date(checkIn)
  const checkOutDate = new Date(checkOut)
  return Math.round(Math.abs((checkOutDate - checkInDate) / oneDay))
}

const cancelReservation = async () => {
  if (!reservation.value) return
  
  // Check if reservation can be cancelled
  if (!['pending', 'confirmed'].includes(reservation.value.status)) {
    alert(`Cannot cancel reservation with status: ${reservation.value.status}`)
    return
  }
  
  const confirmed = confirm("Are you sure you want to cancel this reservation? This action cannot be undone.")
  if (!confirmed) return

  try {
    loading.value = true
    await cancelCustomerReservation(reservation.value.id)
    await loadReservation()
    alert("Reservation cancelled successfully.")
  } catch (e) {
    error.value = e.message || "Failed to cancel reservation. Please try again."
    alert(error.value)
  } finally {
    loading.value = false
  }
}

const downloadReceipt = () => {
  // Implement receipt download functionality
  if (reservation.value) {
    // Create a simple receipt HTML
    const receiptContent = `
      <html>
        <head>
          <title>Receipt - Reservation #${reservation.value.id}</title>
          <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            .header { text-align: center; margin-bottom: 30px; }
            .hotel-name { font-size: 24px; font-weight: bold; }
            .receipt-title { font-size: 18px; margin-top: 10px; }
            .section { margin-bottom: 20px; }
            .section-title { font-weight: bold; margin-bottom: 10px; }
            .row { display: flex; justify-content: space-between; margin-bottom: 5px; }
            .total { font-weight: bold; font-size: 18px; margin-top: 10px; }
            .footer { margin-top: 40px; text-align: center; font-size: 12px; }
          </style>
        </head>
        <body>
          <div class="header">
            <div class="hotel-name">Hotel Management System</div>
            <div class="receipt-title">Reservation Receipt #${reservation.value.id}</div>
          </div>
          
          <div class="section">
            <div class="section-title">Guest Information</div>
            <div class="row">
              <span>Name:</span>
              <span>${reservation.value.customer.first_name} ${reservation.value.customer.last_name}</span>
            </div>
            <div class="row">
              <span>Email:</span>
              <span>${reservation.value.customer.email}</span>
            </div>
            <div class="row">
              <span>Phone:</span>
              <span>${reservation.value.customer.phone}</span>
            </div>
          </div>
          
          <div class="section">
            <div class="section-title">Reservation Details</div>
            <div class="row">
              <span>Room Number:</span>
              <span>${reservation.value.room.room_number}</span>
            </div>
            <div class="row">
              <span>Room Type:</span>
              <span>${reservation.value.room.room_type.name}</span>
            </div>
            <div class="row">
              <span>Check-in:</span>
              <span>${formatDate(reservation.value.check_in)}</span>
            </div>
            <div class="row">
              <span>Check-out:</span>
              <span>${formatDate(reservation.value.check_out)}</span>
            </div>
            <div class="row">
              <span>Number of Nights:</span>
              <span>${calculateNights(reservation.value.check_in, reservation.value.check_out)}</span>
            </div>
            <div class="row">
              <span>Number of Guests:</span>
              <span>${reservation.value.number_of_guests}</span>
            </div>
          </div>
          
          <div class="section">
            <div class="section-title">Payment Details</div>
            <div class="row">
              <span>Room Rate (${calculateNights(reservation.value.check_in, reservation.value.check_out)} nights × $${reservation.value.room.price}):</span>
              <span>$${(parseFloat(reservation.value.room.price) * calculateNights(reservation.value.check_in, reservation.value.check_out)).toFixed(2)}</span>
            </div>
            <div class="row">
              <span>Taxes & Fees (15%):</span>
              <span>$${(parseFloat(reservation.value.total_price) * 0.15).toFixed(2)}</span>
            </div>
            <div class="row total">
              <span>Total Amount:</span>
              <span>$${reservation.value.total_price}</span>
            </div>
          </div>
          
          <div class="footer">
            <p>Generated on ${new Date().toLocaleDateString()}</p>
            <p>Thank you for choosing our hotel!</p>
          </div>
        </body>
      </html>
    `
    
    // Create a Blob and download
    const blob = new Blob([receiptContent], { type: 'text/html' })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `receipt-reservation-${reservation.value.id}.html`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    window.URL.revokeObjectURL(url)
  }
}

const requestChanges = () => {
  // Implement change request functionality
  alert("To request changes, please contact our support team.")
}

const contactSupport = () => {
  window.location.href = "mailto:support@hotel.com?subject=Reservation%20Inquiry%20#"+reservation.value.id
}

onMounted(loadReservation)
</script>