import axios from "axios";
import { get as getFromStore } from "../../localStorage";

const baseurl = import.meta.env.VITE_APP_BASE_URL || "https://romanat-restaurant-7.onrender.com";

const getAuthHeaders = () => {
  const user = getFromStore("logged_in_user");
  if (!user?.access_token) {
    throw { detail: "Authentication required" };
  }
  return {
    Authorization: `Bearer ${user.access_token}`,
    "Content-Type": "application/json",
  };
};

/**
 * Fetch EVERYTHING the backend dashboard returns.
 * (metrics, today_reservations, room_status)
 */
export const fetchDashboardData = async () => {
  try {
    const headers = getAuthHeaders();

    const response = await axios.get(
      `${baseurl}/api/dashboard/receptionist/`,
      { headers }
    );

    return response.data;
  } catch (err) {
    if (err.response?.data) throw err.response.data;
    throw new Error("Failed to fetch dashboard data");
  }
};

/**
 * These endpoints DO NOT EXIST on the backend.
 * So we remove them or route them to fetchDashboardData().
 */

// Return stats from dashboard data
export const fetchReceptionistStats = async () => {
  const full = await fetchDashboardData();
  return full.metrics; // the backend already returns these
};

// Return today's reservations
export const fetchTodayReservations = async () => {
  const full = await fetchDashboardData();
  return full.today_reservations;
};

// Return room status counts
export const fetchQuickRoomStatus = async () => {
  const full = await fetchDashboardData();
  return full.room_status;
};

// These do not exist at all — return empty instead of errors
export const fetchRecentActivities = async () => {
  return [];
};

export const fetchVIPAlerts = async () => {
  return [];
};
