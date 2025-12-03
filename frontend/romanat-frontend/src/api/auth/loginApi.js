import axios from "axios";
import { get as getFromStore } from "../../localStorage";

const baseurl =
  import.meta.env.VITE_APP_BASE_URL || "http://127.0.0.1:8000";

/**
 * LOGIN
 */
export const authenticate = async (creds) => {
  try {
    const response = await axios.post(
      `${baseurl}/api/accounts/login/`,
      creds,
      { headers: { "Content-Type": "application/json" } }
    );
    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * CUSTOMER SIGNUP (public)
 */
export const register = async (forms) => {
  try {
    const response = await axios.post(
      `${baseurl}/api/accounts/signup/`,
      forms,
      { headers: { "Content-Type": "application/json" } }
    );
    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Create customer (authenticated)
 */
export const createCustomer = async (customerData) => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    const response = await axios.post(
      `${baseurl}/api/accounts/users/`,
      customerData,
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Get customers with filters
 */
export const getCustomers = async (params = {}) => {
  try {
    const {
      search = '',
      role = 'customer',
      status = '',
      page = 1,
      page_size = 10,
      ordering = '-date_joined'
    } = params;

    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      console.log("not found the access token");
      throw { detail: "Authentication required" };
    }

    // Build query parameters
    const queryParams = new URLSearchParams();
    
    if (role) queryParams.append('role', role);
    if (search) queryParams.append('search', search);
    if (status) queryParams.append('status', status);
    if (page) queryParams.append('page', page);
    if (page_size) queryParams.append('page_size', page_size);
    if (ordering) queryParams.append('ordering', ordering);

    const url = `${baseurl}/api/accounts/users/?${queryParams.toString()}`;

    const response = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${user.access_token}`,
        "Content-Type": "application/json",
      },
    });

    return response.data;

  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Get customer by ID
 */
export const getCustomerById = async (id) => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    const response = await axios.get(
      `${baseurl}/api/accounts/users/${id}/`,
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Update customer
 */
export const updateCustomer = async (id, customerData) => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    // Remove password if empty (for partial updates)
    if (customerData.password && customerData.password.trim() === '') {
      delete customerData.password;
    }

    const response = await axios.put(
      `${baseurl}/api/accounts/users/${id}/`,
      customerData,
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Update customer partially (PATCH)
 */
export const patchCustomer = async (id, customerData) => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    const response = await axios.patch(
      `${baseurl}/api/accounts/users/${id}/`,
      customerData,
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Update customer status only
 */
export const updateCustomerStatus = async (id, status) => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    const response = await axios.patch(
      `${baseurl}/api/accounts/users/${id}/`,
      { status },
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Delete customer
 */
export const deleteCustomer = async (id) => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    const response = await axios.delete(
      `${baseurl}/api/accounts/users/${id}/`,
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Get all users (for admin) with advanced filtering
 */
export const fetchAllUsers = async (params = {}) => {
  try {
    const {
      role = '',
      status = '',
      search = '',
      page = 1,
      page_size = 20
    } = params;

    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    // Build query parameters
    const queryParams = new URLSearchParams();
    
    if (role) queryParams.append('role', role);
    if (status) queryParams.append('status', status);
    if (search) queryParams.append('search', search);
    if (page) queryParams.append('page', page);
    if (page_size) queryParams.append('page_size', page_size);

    const url = `${baseurl}/api/accounts/users/?${queryParams.toString()}`;

    const response = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${user.access_token}`,
        "Content-Type": "application/json",
      },
    });

    return response.data;

  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Get customer statistics
 */
export const getCustomerStats = async () => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    const response = await axios.get(
      `${baseurl}/api/accounts/customer-stats/`,
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Legacy function - kept for backward compatibility
 */
export const fetchCustomers = async () => {
  try {
    const stored = localStorage.getItem("logged_in_user");
    const user = stored ? JSON.parse(stored) : null;

    if (!user?.access_token) {
      console.log("not found the access token");
      throw { detail: "Authentication required" };
    }

    const response = await axios.get(
      `${baseurl}/api/accounts/list/?role=customer`,
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;

  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};

/**
 * Export customers to CSV
 */
export const exportCustomers = async (customerIds = []) => {
  try {
    const user = getFromStore("logged_in_user");

    if (!user?.access_token) {
      throw { detail: "Authentication required" };
    }

    const response = await axios.post(
      `${baseurl}/api/accounts/export-customers/`,
      { customer_ids: customerIds },
      {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Network error");
  }
};