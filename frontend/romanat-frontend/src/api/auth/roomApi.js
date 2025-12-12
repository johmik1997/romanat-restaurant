import axios from "axios";
import { get as getFromStore } from "../../localStorage";

const baseurl = import.meta.env.VITE_APP_BASE_URL || "https://romanat-restaurant-7.onrender.com";

// Helper function to get auth headers
const getAuthHeaders = () => {
  const user = getFromStore("logged_in_user");
  if (!user?.access_token) {
    throw { detail: "Authentication required" };
  }
  return {
    Authorization: `Bearer ${user.access_token}`
  };
};

export const createRoom = async (formData) => {
  try {
    const headers = {
      ...getAuthHeaders(),
      "Content-Type": "multipart/form-data",
    };
    
    const response = await axios.post(`${baseurl}/api/rooms/`, formData, {
      headers
    });
    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

export const updateRoom = async (roomId, formData) => {
  try {
    const headers = {
      ...getAuthHeaders(),
      "Content-Type": "multipart/form-data",
    };
    
    const response = await axios.put(`${baseurl}/api/rooms/${roomId}/`, formData, {
      headers
    });
    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

export const deleteRoom = async (roomId) => {
  try {
    const headers = {
      ...getAuthHeaders(),
      "Content-Type": "application/json",
    };
    
    const response = await axios.delete(`${baseurl}/api/rooms/${roomId}/`, {
      headers
    });
    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

export const fetchRoomType = async () => {
  try {
    const headers = {
      ...getAuthHeaders(),
      "Content-Type": "application/json",
    };
    
    const response = await axios.get(`${baseurl}/api/room-types/`, {
      headers
    });
    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

export const fetchRoom = async (params = {}) => {
  try {
    const {
      search = '',
      status = '',
      type = '',
      floor = '',
      minPrice = '',
      maxPrice = '',
      page = 1,
      page_size = 10,
      ordering = 'room_number'
    } = params;

    const queryParams = new URLSearchParams();
    
    if (search) queryParams.append('search', search);
    if (status && status !== 'all') queryParams.append('status', status);
    if (type && type !== 'all') queryParams.append('room_type__name', type);
    if (floor && floor !== 'all') queryParams.append('floor', floor);
    if (minPrice) queryParams.append('price__gte', minPrice);
    if (maxPrice) queryParams.append('price__lte', maxPrice);
    if (ordering) queryParams.append('ordering', ordering);
    if (page) queryParams.append('page', page);
    if (page_size) queryParams.append('page_size', page_size);
    
    const url = `${baseurl}/api/rooms/?${queryParams.toString()}`;
    
    const response = await axios.get(url);
    
    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

export const fetchRoomById = async (roomId) => {
  try {
    const headers = {
      ...getAuthHeaders(),
      "Content-Type": "application/json",
    };
    
    const response = await axios.get(`${baseurl}/api/rooms/${roomId}/`, {
      headers
    });
    
    return response.data;
  } catch (error) {
    console.error('Error fetching room by ID:', error);
    if (error.response?.data) throw error.response.data;
    throw new Error('Failed to fetch room details');
  }
};