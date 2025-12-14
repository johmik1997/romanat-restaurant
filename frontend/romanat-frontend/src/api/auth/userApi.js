import api from '../api'

/**
 * Authenticate user with username and password
 * @param {Object} creds
 * @param {string} creds.username
 * @param {string} creds.password
 * @returns {Promise}
 * 
 */

export const fetchRoles = async () => {
  try {
    const response = await api.get('/accounts/roles/');
    return response; // <-- return full response, not response.data
  } catch (error) {
    if (error.response?.data) throw error.response.data;
    throw new Error("Network error");
  }
};


export const createUser = async (userData) => {
  try {
    const response = await api.post('/accounts/users/', userData)
    return response.data
  } catch (error) {
    console.error('Error creating user:', error)
    throw error
  }
}


export const getUsers = async ({ search = '', role = '', status = '', page = 1, page_size = 10 } = {}) => {
  try {
    const params = {}

    if (search) params.search = search
    if (role && role !== 'all') params.role = role
    if (status && status !== 'all') params.status = status
    if (page) params.page = page
    if (page_size) params.page_size = page_size

    const response = await api.get('/accounts/users/', { params })
    return response.data  // expects DRF pagination format
  } catch (err) {
    if (err.response?.data) throw err.response.data
    throw new Error("Network error")
  }
}


export const getUserById = async (id) => {
  try {
    const response = await api.get(`/accounts/users/${id}/`)
    return response.data
  } catch (error) {
    console.error('Error fetching reservation:', error)
    throw error
  }
}

export const getCustomerReservation= async ()=>{
  try{
    const response = await api.get('/accounts/customer/reservation/')
    return response.data
  }
  catch(err){
 console.error('Error fetching reservation:', err)
    throw err
  }
};

export const cancelCustomerReservation = async (reservationId) => {
  try {
      const response = await api.post(`/accounts/customer/reservation/${reservationId}/cancel/`)
  return response.data;
  } catch (err) {
     console.error('Error fetching reservation:', err)
        throw err
  }
};

export const updateUser = async (id, userData) => {
  try {
    const response = await api.put(`/accounts/users/${id}/`, userData)
    return response.data
  } catch (error) {
    console.error('Error updating user:', error)
    throw error
  }
};

export const deleteUser = async (id) => {
  try {
    const response = await api.delete(`/accounts/users/${id}/`)
    return response.data
  } catch (error) {
    console.error('Error deleting user:', error)
    throw error
  }
}


export const updateUserStatus = async (id, status) => {
  const response = await api.patch(`accounts/users/${id}/update-status/`, {
    status: status,
  });
  return response.data;
};
