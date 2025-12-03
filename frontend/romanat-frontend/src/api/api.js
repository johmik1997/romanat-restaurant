import { authorize, load } from '../localStorage'
import axios from 'axios'

const baseURL = import.meta.env.VITE_APP_BASE_URL || 'http://127.0.0.1:8000'

axios.defaults.headers.common['Content-Type'] = 'application/json'

const axiosInstance = axios.create({
  baseURL: `${baseURL}/api`,
  timeout: 10000,
})

const api = (axiosInstance) => {
  
  // 1️⃣ Load the stored user on initial page load
  load('logged_in_user').then((user) => {
    if (user?.access_token) {
      axiosInstance.defaults.headers.common['Authorization'] =
        'Bearer ' + user.access_token
    }
  })

  // 2️⃣ Watch for user changes (login/logout)
  authorize('logged_in_user', (loginData) => {
    if (loginData && loginData.access_token) {
      axiosInstance.defaults.headers.common['Authorization'] =
        'Bearer ' + loginData.access_token
    } else {
      delete axiosInstance.defaults.headers.common['Authorization']
    }
  })

  return {
    get: (url, config) => axiosInstance.get(url, config),
    post: (url, body) => axiosInstance.post(url, body),
    put: (url, body) => axiosInstance.put(url, body),
    patch: (url, body) => axiosInstance.patch(url, body),
    delete: (url) => axiosInstance.delete(url),
  }
}

export default api(axiosInstance)
