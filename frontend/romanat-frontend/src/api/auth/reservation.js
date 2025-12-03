import api from '../api'
import axios from 'axios'

// Define base URL
const baseurl = import.meta.env.VITE_APP_BASE_URL || 'http://127.0.0.1:8000'


/**
 * Create a reservation
 */
export const createReservation = async (reservationData) => {
  try {
    const response = await api.post('/reservations/', reservationData)
    return response.data
  } catch (error) {
    console.error('Error creating reservation:', error)
    throw error
  }
}

export const getReservations = async (params = {}) => {
  try {
    const {
      search = '',
      status = '',
      page = 1,
      page_size = 10,
      check_in_from = '',
      check_in_to = '',
      check_out_from='',
      check_out_to='',
      ordering = '-created_at' // Changed default ordering
    } = params;

    // Build query params object
    const queryParams = {};

    if (search) queryParams.search = search;

    if (status && status !== 'all') {
      queryParams.status = status.toLowerCase();
    }

    if (check_in_from) {
      queryParams.check_in_from = check_in_from;
    }
    if (check_in_to){ queryParams.check_in_to = check_in_to;
    }
    if (check_out_from) {
      queryParams.check_out_from = check_out_from;
    }
    if (check_out_to){ queryParams.check_out_to = check_out_to;
    }
    if (ordering) queryParams.ordering = ordering;
    queryParams.page = page;
    queryParams.page_size = page_size;

    // Pass params as the second argument, not inside an object
    const response = await api.get('/reservations/', { params: queryParams });

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
}
/**
 * Get reservation by ID
 */
export const getReservationById = async (id) => {
  try {
    const response = await api.get(`/reservations/${id}/`)
    return response.data
  } catch (error) {
    console.error('Error fetching reservation:', error)
    throw error
  }
}


/**
 * Update reservation
 */
export const updateReservation = async (id, reservationData) => {
  try {
    const response = await api.put(`/reservations/${id}/`, reservationData)
    return response.data
  } catch (error) {
    console.error('Error updating reservation:', error)
    throw error
  }
}


/**
 * Delete reservation
 */
export const deleteReservation = async (id) => {
  try {
    const response = await api.delete(`/reservations/${id}/`)
    return response.data
  } catch (error) {
    console.error('Error deleting reservation:', error)
    throw error
  }
}


/**
 * Update status only
 */
export const updateReservationStatus = async (id, status) => {
  try {
    const response = await api.patch(`/reservations/${id}/update-status/`, {
      status: status.toLowerCase(),   // ensure backend accepts it
    })
    return response.data
  } catch (error) {
    console.error('Error updating reservation status:', error)
    throw error
  }
}
